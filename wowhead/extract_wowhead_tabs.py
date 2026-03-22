#!/usr/bin/env python3
"""
Wowhead Tabbed Content Extractor — Discovery-Based (v2)
========================================================
Extracts ALL content hidden behind JS tabs on Wowhead guide pages.
Does NOT hardcode tab names or positions — discovers them dynamically.

v2 improvements (Phase 3.5a):
  - Post-processing: strip comment widget noise from all extracted text
  - Post-processing: deduplicate repeated blocks within each hero section
  - Hero talent click verification + retry on failure
  - MutationObserver-based lazy load waiting (replaces fixed sleep)
  - Validation pass after each extraction (warns on missing heroes, short files, truncation)
  - Fixed "null" string key in JSON when no hero switches found (now "default")

Each spec has a DIFFERENT tab layout:
  - Different tab names ("AoE Priority" vs "Multitarget")
  - Hero talent switches may appear BEFORE or INSIDE content tabs
  - Different number of cooldown sub-tabs
  - Different advanced tips sub-tabs
  - Per-talent-point toggle buttons that adapt rotation to specific talents

The script discovers all interactive elements and clicks through every
combination, capturing the page state after each change.

Usage:
  python3 extract_wowhead_tabs.py <class> <spec> [--pages rotation,talents,bis,consumables,tier]
  python3 extract_wowhead_tabs.py warlock affliction --pages rotation
  python3 extract_wowhead_tabs.py warrior fury --pages rotation,talents
  python3 extract_wowhead_tabs.py --all

Outputs: wowhead/<class>/<spec>/extracted/<page>.md + .json

Requirements:
  pip install playwright
  playwright install chromium
"""

import argparse
import json
import os
import sys
import time
import re
from pathlib import Path
from itertools import product

# ---------------------------------------------------------------------------
# Spec / Role / URL mapping (mirrors generate_links.sh)
# ---------------------------------------------------------------------------

ROLE_MAP = {
    "blood": "tank", "vengeance": "tank", "guardian": "tank",
    "brewmaster": "tank", "protection": "tank",
}

HERO_TALENTS = {
    "death-knight/blood": ["deathbringer", "sanlayn"],
    "death-knight/frost": ["deathbringer", "rider-of-the-apocalypse"],
    "death-knight/unholy": ["rider-of-the-apocalypse", "sanlayn"],
    "demon-hunter/havoc": ["aldrachi-reaver", "fel-scarred"],
    "demon-hunter/devourer": ["annihilator", "void-scarred"],
    "demon-hunter/vengeance": ["aldrachi-reaver", "annihilator"],
    "druid/balance": ["elunes-chosen", "keeper-of-the-grove"],
    "druid/feral": ["druid-of-the-claw", "wildstalker"],
    "druid/guardian": ["druid-of-the-claw", "elunes-chosen"],
    "evoker/devastation": ["flameshaper", "scalecommander"],
    "evoker/augmentation": ["chronowarden", "scalecommander"],
    "hunter/beast-mastery": ["dark-ranger", "pack-leader"],
    "hunter/marksmanship": ["dark-ranger", "sentinel"],
    "hunter/survival": ["pack-leader", "sentinel"],
    "mage/arcane": ["spellslinger", "sunfury"],
    "mage/fire": ["frostfire", "sunfury"],
    "mage/frost": ["frostfire", "spellslinger"],
    "monk/brewmaster": ["master-of-harmony", "shado-pan"],
    "monk/windwalker": ["conduit-of-the-celestials", "shado-pan"],
    "paladin/protection": ["lightsmith", "templar"],
    "paladin/retribution": ["herald-of-the-sun", "templar"],
    "priest/shadow": ["archon", "voidweaver"],
    "rogue/assassination": ["deathstalker", "fatebound"],
    "rogue/outlaw": ["fatebound", "trickster"],
    "rogue/subtlety": ["deathstalker", "trickster"],
    "shaman/elemental": ["farseer", "stormbringer"],
    "shaman/enhancement": ["stormbringer", "totemic"],
    "warlock/affliction": ["hellcaller", "soul-harvester"],
    "warlock/demonology": ["diabolist", "soul-harvester"],
    "warlock/destruction": ["diabolist", "hellcaller"],
    "warrior/arms": ["colossus", "slayer"],
    "warrior/fury": ["mountain-thane", "slayer"],
    "warrior/protection": ["colossus", "mountain-thane"],
}

ALL_SPECS = list(HERO_TALENTS.keys())

PAGE_URLS = {
    "rotation":     "rotation-cooldowns-pve-{role}",
    "talents":      "talent-builds-pve-{role}",
    "bis":          "bis-gear",
    "consumables":  "enchants-gems-pve-{role}",
    "tier":         "tier-set-bonuses",
}

# Known hero talent display names (for identification — NOT for hardcoded clicking)
ALL_HERO_TALENT_NAMES = {
    "hellcaller", "soul harvester", "deathbringer", "san'layn", "rider of the apocalypse",
    "aldrachi reaver", "fel-scarred", "annihilator", "void-scarred",
    "elune's chosen", "keeper of the grove", "druid of the claw", "wildstalker",
    "flameshaper", "scalecommander", "chronowarden",
    "dark ranger", "pack leader", "sentinel",
    "spellslinger", "sunfury", "frostfire",
    "master of harmony", "shado-pan", "conduit of the celestials",
    "lightsmith", "templar", "herald of the sun",
    "archon", "voidweaver",
    "deathstalker", "fatebound", "trickster",
    "farseer", "stormbringer", "totemic",
    "diabolist",
    "colossus", "slayer", "mountain thane",
}

# Tab names to SKIP (site navigation, not content)
SKIP_TAB_NAMES = {
    "news", "comments", "add your comment", "changelog",
    "news (", " comments (",  # partial matches handled below
}

def get_role(spec):
    return ROLE_MAP.get(spec, "dps")

def build_url(cls, spec, page):
    role = get_role(spec)
    slug = PAGE_URLS[page].format(role=role)
    return f"https://www.wowhead.com/guide/classes/{cls}/{spec}/{slug}"

def should_skip_tab(name):
    """Check if a tab name is site chrome vs guide content."""
    low = name.lower().strip()
    if low in SKIP_TAB_NAMES:
        return True
    for skip in SKIP_TAB_NAMES:
        if low.startswith(skip):
            return True
    return False

def is_hero_talent_button(name):
    """Check if a button text matches a known hero talent name."""
    low = name.lower().strip()
    # Remove leading icon chars / whitespace
    low = low.lstrip(" \t\n\u200b")
    return low in ALL_HERO_TALENT_NAMES


# ---------------------------------------------------------------------------
# Post-processing: noise stripping + deduplication (Phase 3.5a items A, B)
# ---------------------------------------------------------------------------

# Anchors that reliably identify the start of comment widget noise
_COMMENT_WIDGET_ANCHORS = [
    "1 - 1 of 1",
    "1 - 2 of 2",
    "1 - 3 of 3",
    "1 - 4 of 4",
    "1 - 5 of 5",
    "You are not logged in",
    "Please keep the following in mind when posting a comment",
    "How to Play Your Class in the Battle for Azeroth",
    "How to Play Your Class in",
    "Please log in to submit feedback",
    "Post a Comment",
    "Comments (Newest First)",
    "Comment by ",
]

# Regex that matches the comment-count pattern "N - N of N"
_COMMENT_COUNT_RE = re.compile(r'^\d+\s*-\s*\d+\s+of\s+\d+$')

# Regex patterns for Wowhead user comments (not forum widget, but page comments)
# e.g. "By Username (Patch 12.0.1)" or "Patch 12.0.1"
_USER_COMMENT_PATTERNS = [
    re.compile(r'^By \w+.*\(Patch \d+\.\d+'),          # "By Username ... (Patch X.X.X)"
    re.compile(r'^\(Patch \d+\.\d+'),                    # "(Patch X.X.X)"
    re.compile(r'^Reply$'),                               # standalone "Reply"
    re.compile(r'^Report$'),                              # standalone "Report"
    re.compile(r'^\d+ (likes?|dislikes?)$'),              # vote counts "5 likes"
    re.compile(r'^Edited by \w+'),                        # "Edited by Username"
]


def strip_site_noise(text):
    """
    Remove Wowhead comment widget pollution and other site chrome from extracted text.
    Works line-by-line: when a noise anchor is found, removes from that line to the
    next section boundary (blank line followed by non-noise content, or end of text).
    """
    if not text:
        return text

    lines = text.split('\n')
    clean_lines = []
    skip_mode = False

    for line in lines:
        stripped = line.strip()

        # Check if this line triggers skip mode
        if not skip_mode:
            is_noise = False
            for anchor in _COMMENT_WIDGET_ANCHORS:
                if anchor in stripped:
                    is_noise = True
                    break
            if not is_noise and _COMMENT_COUNT_RE.match(stripped):
                is_noise = True
            if not is_noise:
                for pat in _USER_COMMENT_PATTERNS:
                    if pat.match(stripped):
                        is_noise = True
                        break

            if is_noise:
                skip_mode = True
                continue
            clean_lines.append(line)
        else:
            # In skip mode — look for end of noise block.
            # Noise blocks end when we hit a blank line followed by real content,
            # or when we see a header/section marker.
            if stripped == '':
                # Blank line — might be end of noise. Peek ahead by just exiting
                # skip mode; if next line is also noise it will re-trigger.
                skip_mode = False
                clean_lines.append(line)
            elif any(anchor in stripped for anchor in _COMMENT_WIDGET_ANCHORS):
                # Still in noise
                continue
            elif _COMMENT_COUNT_RE.match(stripped):
                continue
            elif stripped.startswith('#') or stripped.startswith('##'):
                # A markdown header — real content, end skip mode
                skip_mode = False
                clean_lines.append(line)
            else:
                # Continuation of noise block — skip
                continue

    return '\n'.join(clean_lines)


def deduplicate_blocks(text, min_block_len=80):
    """
    Remove paragraph-level duplicates within a text body.
    Splits on double-newlines, tracks seen paragraphs, removes exact repeats.
    Only deduplicates blocks longer than min_block_len chars to avoid
    removing short legitimate repeated lines (like single spell names).
    """
    if not text:
        return text

    # Split into blocks separated by double-newlines
    blocks = re.split(r'\n\s*\n', text)
    seen = set()
    unique_blocks = []

    for block in blocks:
        stripped = block.strip()
        if not stripped:
            continue
        # Only dedup blocks above threshold
        if len(stripped) >= min_block_len:
            # Normalize whitespace for comparison
            normalized = re.sub(r'\s+', ' ', stripped)
            if normalized in seen:
                continue
            seen.add(normalized)
        unique_blocks.append(block)

    return '\n\n'.join(unique_blocks)


def postprocess_content(text):
    """Apply all post-processing steps to extracted text content."""
    text = strip_site_noise(text)
    text = deduplicate_blocks(text)
    # Clean up excessive blank lines left by stripping
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip()


# ---------------------------------------------------------------------------
# Validation (Phase 3.5a item G)
# ---------------------------------------------------------------------------

def validate_extraction(data, cls, spec, page_name):
    """
    Post-extraction validation. Returns list of warning strings.
    Checks:
      - Hero talent section count vs expected (from HERO_TALENTS)
      - Placeholder text remaining
      - Suspiciously short content
      - Truncated lines (ending with '[' or mid-word indicators)
    """
    warnings = []
    spec_key = f"{cls}/{spec}"
    expected_heroes = HERO_TALENTS.get(spec_key, [])

    # Check hero talent count
    content = data.get("content", {})
    hero_keys = [k for k in content.keys() if k and k != "default"]
    if page_name == "rotation" and len(expected_heroes) > 0:
        if len(hero_keys) < len(expected_heroes):
            warnings.append(
                f"MISSING HERO TALENTS: found {len(hero_keys)} ({hero_keys}), "
                f"expected {len(expected_heroes)} ({expected_heroes})"
            )

    # Check for placeholder text in any content
    all_text = json.dumps(data.get("content", {}))
    if "Please select a Hero Talent" in all_text:
        warnings.append("PLACEHOLDER TEXT: 'Please select a Hero Talent' found in output")

    # Check total content length
    total_chars = len(all_text)
    if total_chars < 500 and page_name in ("rotation", "talents", "bis"):
        warnings.append(f"SUSPICIOUSLY SHORT: only {total_chars} chars of content")

    # Check for truncated lines in tab content
    truncation_patterns = [
        re.compile(r'\[$'),           # line ending with open bracket
        re.compile(r'\w{3,}\s*$'),    # OK — normal word ending, not truncated
    ]
    for hero_key, hero_data in content.items():
        if not isinstance(hero_data, dict):
            continue
        for group_key, group_data in hero_data.items():
            if not isinstance(group_data, dict) or "tabs" not in group_data:
                continue
            for tab_name, tab_data in group_data.get("tabs", {}).items():
                if isinstance(tab_data, dict):
                    tab_text = tab_data.get("content", "")
                elif isinstance(tab_data, str):
                    tab_text = tab_data
                else:
                    continue
                # Check last non-empty line
                lines = [l for l in tab_text.split('\n') if l.strip()]
                if lines:
                    last_line = lines[-1].rstrip()
                    if last_line.endswith('[') or last_line.endswith('('):
                        warnings.append(
                            f"TRUNCATED: {hero_key}/{group_key}/{tab_name} — "
                            f"last line ends with '{last_line[-20:]}'"
                        )

    return warnings


# ---------------------------------------------------------------------------
# Discovery Engine — finds all interactive elements on a page
# ---------------------------------------------------------------------------

class PageDiscovery:
    """
    Discovers the interactive structure of a wowhead guide page:
    - Hero talent switch buttons
    - Content tabs (role="tab")
    - Per-talent toggle buttons within tab panels
    - Nested tab groups (cooldown sub-tabs, advanced tips sub-tabs)
    """

    def __init__(self, page_obj):
        self.page = page_obj

    def discover_hero_switches(self):
        """Find hero talent switch buttons anywhere on the page."""
        switches = []
        seen_names = set()
        buttons = self.page.query_selector_all('button')
        for btn in buttons:
            try:
                if not btn.is_visible():
                    continue
                box = btn.bounding_box()
                if not box:
                    continue
                text = btn.inner_text().strip()
                if not text:
                    continue
                # Filter duplicated-text artifacts Wowhead creates after re-renders
                # e.g. "SlayerSlayer" or "Mountain ThaneMountain Thane"
                half = len(text) // 2
                if len(text) > 4 and len(text) % 2 == 0 and text[:half] == text[half:]:
                    continue
                if is_hero_talent_button(text) and text not in seen_names:
                    seen_names.add(text)
                    switches.append({"element": btn, "name": text, "type": "hero_switch"})
            except Exception:
                continue
        return switches

    def discover_tab_groups(self):
        """
        Find ALL tab groups on the page. Returns a list of tab groups,
        where each group is a list of {element, name} dicts.
        
        Tab groups are identified by [role="tablist"] containers.
        Each container may hold a different set of tabs.
        """
        groups = []
        tablists = self.page.query_selector_all('[role="tablist"]')
        for tablist in tablists:
            try:
                if not tablist.is_visible():
                    continue
            except Exception:
                continue

            tabs = tablist.query_selector_all('[role="tab"]')
            group = []
            for tab in tabs:
                try:
                    if not tab.is_visible():
                        continue
                    name = tab.inner_text().strip()
                    if name and not should_skip_tab(name):
                        group.append({"element": tab, "name": name, "type": "tab"})
                except Exception:
                    continue
            if group:
                groups.append(group)
        return groups

    def discover_toggle_buttons(self):
        """
        Find per-talent toggle buttons that are NOT hero switches and NOT tabs.
        These are buttons within the guide content area that toggle specific
        talent point selections, adapting the displayed rotation.
        """
        toggles = []
        # Look for buttons in the main guide body that aren't tabs or hero switches
        guide_area = self.page.query_selector('.guide-body') or self.page.query_selector('main')
        if not guide_area:
            return toggles

        buttons = guide_area.query_selector_all('button:not([role="tab"])')
        for btn in buttons:
            try:
                if not btn.is_visible():
                    continue
                text = btn.inner_text().strip()
                if not text or len(text) > 60:
                    continue
                if is_hero_talent_button(text):
                    continue
                # Check if it looks like a talent toggle (has icon + short name)
                # Common patterns: "Talent Name" with a WoW icon next to it
                role = btn.get_attribute('role')
                aria = btn.get_attribute('aria-pressed') or btn.get_attribute('aria-selected')
                classes = btn.get_attribute('class') or ''
                
                # Heuristic: talent toggles often have aria-pressed or are in toggle groups
                if aria is not None or 'toggle' in classes.lower() or 'switch' in classes.lower():
                    toggles.append({"element": btn, "name": text, "type": "talent_toggle"})
            except Exception:
                continue
        return toggles

    def get_page_content_snapshot(self):
        """
        Get a text snapshot of the currently visible guide content.
        Captures all visible text, skipping nav/footer/ads.
        """
        # Try multiple selectors for the main content area
        for selector in ['.guide-body', '.guide-content', 'article', 'main']:
            el = self.page.query_selector(selector)
            if el:
                try:
                    return el.inner_text()
                except Exception:
                    continue

        # Fallback: get all visible tabpanel content
        panels = self.page.query_selector_all('[role="tabpanel"]')
        visible_text = []
        for panel in panels:
            try:
                hidden = panel.get_attribute('hidden')
                if hidden is not None:
                    continue
                text = panel.inner_text().strip()
                if text:
                    visible_text.append(text)
            except Exception:
                continue
        return "\n\n---\n\n".join(visible_text) if visible_text else ""

    def get_talent_links(self):
        """
        Extract talent-calc/blizzard/ export codes from all <a href> links on the page.
        These are the base64 talent strings usable directly in SimC profiles as talents=<code>.
        Returns a list of unique talent code strings (the part after /talent-calc/blizzard/).
        """
        try:
            links = self.page.evaluate(
                "Array.from(document.querySelectorAll('a[href*=\"talent-calc/blizzard/\"]'))"
                ".map(a => a.href)"
            )
            codes = []
            seen = set()
            for href in links:
                # Extract the base64 code from the URL
                # Format: https://www.wowhead.com/talent-calc/blizzard/CODEHERE
                idx = href.find("/talent-calc/blizzard/")
                if idx >= 0:
                    code = href[idx + len("/talent-calc/blizzard/"):]
                    # Strip any trailing query params or fragments
                    code = code.split("?")[0].split("#")[0].strip()
                    if code and code not in seen:
                        seen.add(code)
                        codes.append(code)
            return codes
        except Exception:
            return []

    def get_visible_panel_text(self):
        """Get text only from currently visible/active tab panels."""
        panels = self.page.query_selector_all('[role="tabpanel"]')
        texts = []
        for panel in panels:
            try:
                hidden = panel.get_attribute('hidden')
                if hidden is not None:
                    continue
                style = panel.get_attribute('style') or ''
                if 'display: none' in style or 'display:none' in style:
                    continue
                text = panel.inner_text().strip()
                if text:
                    texts.append(text)
            except Exception:
                continue
        return "\n\n".join(texts)


# ---------------------------------------------------------------------------
# Lazy load: MutationObserver-based waiting (Phase 3.5a item D)
# ---------------------------------------------------------------------------

def wait_for_content_stable(page_obj, timeout_ms=8000, settle_ms=500):
    """
    Wait for page content to stabilize using a MutationObserver.
    Watches .guide-body (or body) for new child nodes. Resolves when
    no new mutations fire for settle_ms. Falls back to timeout.
    """
    try:
        page_obj.evaluate(f"""
            () => new Promise((resolve) => {{
                const target = document.querySelector('.guide-body')
                    || document.querySelector('main')
                    || document.body;
                let timer = null;
                const observer = new MutationObserver(() => {{
                    if (timer) clearTimeout(timer);
                    timer = setTimeout(() => {{
                        observer.disconnect();
                        resolve('settled');
                    }}, {settle_ms});
                }});
                observer.observe(target, {{ childList: true, subtree: true }});
                // Start the settle timer immediately in case no mutations fire
                timer = setTimeout(() => {{
                    observer.disconnect();
                    resolve('timeout-no-mutations');
                }}, {settle_ms});
                // Hard timeout
                setTimeout(() => {{
                    observer.disconnect();
                    resolve('hard-timeout');
                }}, {timeout_ms});
            }})
        """)
    except Exception:
        # Fallback to fixed sleep if MutationObserver fails
        time.sleep(timeout_ms / 1000)


def scroll_and_wait(page_obj):
    """
    Scroll to trigger lazy-loaded content, then wait for DOM to stabilize
    via MutationObserver instead of fixed sleeps.
    """
    # Scroll down in steps to trigger intersection observers
    for _ in range(5):
        page_obj.evaluate("window.scrollBy(0, 600)")
        time.sleep(0.15)
    # Scroll back to top
    page_obj.evaluate("window.scrollTo(0, 0)")
    # Wait for content to stabilize after lazy loads
    wait_for_content_stable(page_obj, timeout_ms=6000, settle_ms=800)


# ---------------------------------------------------------------------------
# Hero talent click with verification + retry (Phase 3.5a item E)
# ---------------------------------------------------------------------------

def click_hero_talent(page_obj, hero_name, url, max_retries=2):
    """
    Click a hero talent button with verification.
    After clicking, verifies data-active='true' is set on the target button.
    Retries with page reload on failure.
    Returns True if successfully activated, False otherwise.
    """
    hn_js = json.dumps(hero_name)

    for attempt in range(max_retries + 1):
        if attempt > 0:
            print(f"    Retry {attempt}/{max_retries} for hero talent: {hero_name}")
            page_obj.goto(url, wait_until="domcontentloaded", timeout=45000)
            time.sleep(3)
            scroll_and_wait(page_obj)

        # Check if already active
        already_active = page_obj.evaluate(
            "(() => {"
            "  const btns = Array.from(document.querySelectorAll('button'));"
            "  const target = btns.find(b => {"
            "    const t = b.innerText.trim();"
            "    const half = Math.floor(t.length / 2);"
            "    if (t.length > 4 && t.length % 2 === 0 && t.slice(0,half)===t.slice(half)) return false;"
            f"    return t === {hn_js};"
            "  });"
            "  if (!target) return null;"
            "  return target.dataset.active === 'true' || target.dataset.checked === 'true' || target.getAttribute('aria-pressed') === 'true';"
            "})()"
        )

        if already_active is None:
            # Button not found — try case-insensitive match
            found_ci = page_obj.evaluate(
                "(() => {"
                "  const btns = Array.from(document.querySelectorAll('button'));"
                f"  const needle = {hn_js}.toLowerCase();"
                "  const target = btns.find(b => {"
                "    const t = b.innerText.trim().toLowerCase();"
                "    const half = Math.floor(t.length / 2);"
                "    if (t.length > 4 && t.length % 2 === 0 && t.slice(0,half)===t.slice(half)) return false;"
                "    return t === needle;"
                "  });"
                "  if (target) { target.click(); return true; }"
                "  return false;"
                "})()"
            )
            if found_ci:
                print(f"    Clicked via case-insensitive match")
                time.sleep(1)
            else:
                print(f"    Button not found (attempt {attempt + 1})")
                continue

        elif already_active:
            print(f"    Already active — reading current state")
            return True
        else:
            # Click it
            clicked = page_obj.evaluate(
                "(() => {"
                "  const btns = Array.from(document.querySelectorAll('button'));"
                "  const target = btns.find(b => {"
                "    const t = b.innerText.trim();"
                "    const half = Math.floor(t.length / 2);"
                "    if (t.length > 4 && t.length % 2 === 0 && t.slice(0,half)===t.slice(half)) return false;"
                f"    return t === {hn_js};"
                "  });"
                "  if (target) { target.click(); return true; }"
                "  return false;"
                "})()"
            )
            if not clicked:
                print(f"    Click failed (attempt {attempt + 1})")
                continue

        # Wait for placeholder to disappear
        for _ in range(10):
            time.sleep(0.5)
            still_placeholder = page_obj.evaluate(
                "document.body.innerText.includes('Please select a Hero Talent')"
            )
            if not still_placeholder:
                break
        time.sleep(0.5)

        # VERIFY: check that the button is now active
        is_now_active = page_obj.evaluate(
            "(() => {"
            "  const btns = Array.from(document.querySelectorAll('button'));"
            f"  const needle = {hn_js}.toLowerCase();"
            "  const target = btns.find(b => {"
            "    const t = b.innerText.trim().toLowerCase();"
            "    const half = Math.floor(t.length / 2);"
            "    if (t.length > 4 && t.length % 2 === 0 && t.slice(0,half)===t.slice(half)) return false;"
            "    return t === needle;"
            "  });"
            "  if (!target) return null;"
            "  return target.dataset.active === 'true' || target.dataset.checked === 'true' || target.getAttribute('aria-pressed') === 'true';"
            "})()"
        )

        if is_now_active:
            print(f"    Verified active: {hero_name}")
            return True
        else:
            # Check if placeholder is gone (some pages don't use data-active)
            still_ph = page_obj.evaluate(
                "document.body.innerText.includes('Please select a Hero Talent')"
            )
            if not still_ph:
                print(f"    No data-active attribute, but placeholder gone — accepting")
                return True
            print(f"    Verification failed (attempt {attempt + 1})")

    print(f"    FAILED after {max_retries + 1} attempts: {hero_name}")
    return False


# ---------------------------------------------------------------------------
# Extraction strategy: click through ALL combinations
# ---------------------------------------------------------------------------

def extract_page_complete(page_obj, cls, spec, page_name, url=None):
    """
    Discovery-based extraction:
    1. Discover all interactive elements (hero switches, tab groups, talent toggles)
    2. Log the discovered structure
    3. Click through every combination and capture content
    4. Post-process: strip noise and deduplicate
    5. Return structured results

    Handles the fact that:
    - Hero switches may be above or inside content tabs
    - Tab groups may appear/disappear after clicking hero switches
    - Talent toggles may appear/disappear after clicking tabs
    - The number and names of everything varies per spec
    """
    disc = PageDiscovery(page_obj)
    results = {
        "spec": f"{cls}/{spec}",
        "page": page_name,
        "url": build_url(cls, spec, page_name),
        "discovered_structure": {},
        "content": {},
    }

    # Phase 1: Initial discovery
    hero_switches = disc.discover_hero_switches()
    tab_groups = disc.discover_tab_groups()
    talent_toggles = disc.discover_toggle_buttons()

    # Log discovered structure
    results["discovered_structure"] = {
        "hero_switches": [s["name"] for s in hero_switches],
        "tab_groups": [[t["name"] for t in g] for g in tab_groups],
        "talent_toggles": [t["name"] for t in talent_toggles],
    }

    print(f"  Discovered:")
    print(f"    Hero switches: {[s['name'] for s in hero_switches]}")
    print(f"    Tab groups ({len(tab_groups)}):")
    for i, g in enumerate(tab_groups):
        print(f"      Group {i}: {[t['name'] for t in g]}")
    print(f"    Talent toggles: {[t['name'] for t in talent_toggles]}")

    # Phase 2: Click through combinations
    # Strategy: for each hero switch, click it, then re-discover tabs
    # (because tabs may change after hero switch). Then click through each tab group.

    # Use names only — re-discover elements fresh before each click (stale ref protection)
    hero_names = [h["name"] for h in hero_switches] if hero_switches else [None]

    for hero_name in hero_names:
        # Key for content dict: use "default" instead of None/null
        content_key = hero_name if hero_name else "default"

        if hero_name:
            print(f"\n  === Hero Talent: {hero_name} ===")
            try:
                # Reload the page for each hero talent iteration.
                # Wowhead's JS replaces hero switch buttons with duplicated-text
                # artifacts after tab clicks, making them unclickable. A fresh
                # page load restores the original DOM reliably.
                page_obj.goto(url, wait_until="domcontentloaded", timeout=45000)
                time.sleep(3)
                scroll_and_wait(page_obj)

                if not click_hero_talent(page_obj, hero_name, url):
                    print(f"    SKIP: could not activate hero talent {hero_name}")
                    continue
            except Exception as e:
                print(f"    ERROR clicking hero switch: {e}")
                continue
        else:
            print(f"\n  === No hero switches found, extracting directly ===")

        results["content"][content_key] = {}

        # For talents pages: extract all talent-calc/blizzard/ href codes visible after
        # the hero switch — these are the base64 SimC talent strings.
        if page_name == "talents":
            talent_codes = disc.get_talent_links()
            if talent_codes:
                results["content"][content_key]["talent_codes"] = talent_codes
                print(f"    Talent codes found: {len(talent_codes)}")
                for code in talent_codes[:3]:
                    print(f"      {code[:60]}...")
            else:
                print(f"    No talent-calc/blizzard/ links found for this hero state")

        # Re-discover after hero switch (tabs may have changed)
        tab_groups_now = disc.discover_tab_groups()
        talent_toggles_now = disc.discover_toggle_buttons()

        if not tab_groups_now:
            # No tabs at all — just grab the page content
            print(f"    No tab groups found, capturing full page")
            raw_text = disc.get_page_content_snapshot()
            results["content"][content_key]["full_page"] = postprocess_content(raw_text)
            continue

        # Click through each tab in each group
        # Tab groups are ordered by DOM position (top to bottom)
        # Typically: Group 0 = main content tabs (ST/AoE/Opener)
        #            Group 1+ = sub-tabs within a section (cooldowns, advanced tips)

        for gi, group in enumerate(tab_groups_now):
            group_key = f"tab_group_{gi}"
            tab_names_in_group = [t["name"] for t in group]
            results["content"][content_key][group_key] = {
                "tab_names": tab_names_in_group,
                "tabs": {},
            }

            for tab_name in tab_names_in_group:
                print(f"    Tab Group {gi} -> [{tab_name}]")

                try:
                    # JS-based click by role=tab + exact text — immune to stale handles
                    tn_js = json.dumps(tab_name)
                    tab_js = (
                        "(() => {"
                        "  const tabs = Array.from(document.querySelectorAll('[role=\"tab\"]'));"
                        f"  const target = tabs.find(t => t.innerText.trim() === {tn_js});"
                        "  if (target) { target.click(); return true; }"
                        "  return false;"
                        "})()"
                    )
                    clicked = page_obj.evaluate(tab_js)
                    if not clicked:
                        print(f"      SKIP: tab not found via JS")
                        results["content"][content_key][group_key]["tabs"][tab_name] = "[TAB NOT FOUND]"
                        continue
                    # Wait for content to stabilize after tab switch
                    wait_for_content_stable(page_obj, timeout_ms=4000, settle_ms=500)
                except Exception as e:
                    print(f"      ERROR clicking tab: {e}")
                    results["content"][content_key][group_key]["tabs"][tab_name] = f"[CLICK FAILED: {e}]"
                    continue

                # After clicking a main tab, check for talent toggles that appeared
                talent_toggles_in_panel = disc.discover_toggle_buttons()
                new_toggles = [t for t in talent_toggles_in_panel
                               if t["name"] not in [tt["name"] for tt in talent_toggles_now]]

                if new_toggles:
                    print(f"      Found {len(new_toggles)} talent toggles: {[t['name'] for t in new_toggles]}")

                # Capture content with current state — apply post-processing
                panel_text = disc.get_visible_panel_text()
                if not panel_text:
                    panel_text = disc.get_page_content_snapshot()

                panel_text = postprocess_content(panel_text)
                tab_result = {"content": panel_text}

                # If there are talent toggles visible, click each one and capture
                if new_toggles:
                    tab_result["talent_variants"] = {}
                    for toggle in new_toggles:
                        toggle_name = toggle["name"]
                        print(f"      Talent toggle: [{toggle_name}]")
                        try:
                            toggle["element"].click()
                            time.sleep(1.0)
                            variant_text = disc.get_visible_panel_text()
                            if not variant_text:
                                variant_text = disc.get_page_content_snapshot()
                            tab_result["talent_variants"][toggle_name] = postprocess_content(variant_text)
                        except Exception as e:
                            tab_result["talent_variants"][toggle_name] = f"[CLICK FAILED: {e}]"

                # Also check for NEW sub-tab groups that appeared after clicking this tab
                sub_groups = disc.discover_tab_groups()
                new_sub_groups = [g for g in sub_groups
                                  if [t["name"] for t in g] != [t["name"] for t in group]
                                  and len(g) > 0]

                if new_sub_groups:
                    # There are sub-tab groups we haven't iterated yet
                    # They'll be caught in the outer loop since we enumerate all groups
                    pass

                results["content"][content_key][group_key]["tabs"][tab_name] = tab_result

    return results


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_output(data):
    """Convert extraction results to readable markdown."""
    lines = []
    spec = data["spec"]
    page = data["page"]
    url = data["url"]

    lines.append(f"# {spec} — {page.title()} (Browser Extracted)")
    lines.append(f"Source: {url}")
    lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    # Structure summary
    struct = data["discovered_structure"]
    lines.append("## Discovered Page Structure")
    lines.append(f"Hero Talent Switches: {struct['hero_switches'] or 'None found'}")
    for i, group in enumerate(struct["tab_groups"]):
        lines.append(f"Tab Group {i}: {group}")
    if struct["talent_toggles"]:
        lines.append(f"Talent Toggles: {struct['talent_toggles']}")
    lines.append("")

    # Content per hero talent / tab combination
    for hero_name, hero_data in data["content"].items():
        if hero_name and hero_name != "default":
            section_label = f"Hero Talent: {hero_name}"
        else:
            section_label = "Default (no hero switch)"
        lines.append(f"## {section_label}")
        lines.append("")

        if isinstance(hero_data, str):
            lines.append(hero_data)
            lines.append("")
            continue

        for group_key, group_data in hero_data.items():
            if group_key == "full_page":
                lines.append("### Full Page Content")
                lines.append(group_data)
                lines.append("")
                continue

            # Talent codes block — emit as a SimC-ready section
            if group_key == "talent_codes":
                lines.append("### Talent Export Codes (SimC `talents=` strings)")
                lines.append("")
                for i, code in enumerate(group_data, 1):
                    lines.append(f"Build {i}: `{code}`")
                lines.append("")
                continue

            if not isinstance(group_data, dict):
                lines.append(f"### {group_key}")
                lines.append(str(group_data))
                lines.append("")
                continue

            tab_names = group_data.get("tab_names", [])
            lines.append(f"### {group_key} — Tabs: {tab_names}")
            lines.append("")

            for tab_name, tab_data in group_data.get("tabs", {}).items():
                lines.append(f"#### {tab_name}")

                if isinstance(tab_data, str):
                    lines.append(tab_data)
                elif isinstance(tab_data, dict):
                    content = tab_data.get("content", "")
                    lines.append(content)

                    variants = tab_data.get("talent_variants", {})
                    if variants:
                        lines.append("")
                        lines.append(f"**Talent Toggle Variants ({len(variants)}):**")
                        for variant_name, variant_text in variants.items():
                            lines.append(f"\n##### Variant: {variant_name}")
                            lines.append(variant_text)
                lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def run_extraction(cls, spec, pages, wowhead_dir):
    """Run browser extraction for one spec across specified pages."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: playwright not installed.")
        print("Run: pip install playwright && playwright install chromium")
        sys.exit(1)

    out_dir = Path(wowhead_dir) / cls / spec / "extracted"
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900},
        )
        page_obj = context.new_page()

        for page_name in pages:
            url = build_url(cls, spec, page_name)
            print(f"\n{'='*70}")
            print(f"Extracting: {cls}/{spec} — {page_name}")
            print(f"URL: {url}")
            print(f"{'='*70}")

            try:
                page_obj.goto(url, wait_until="domcontentloaded", timeout=45000)
                time.sleep(3)  # Brief wait for initial JS hydration

                # Dismiss cookie banners / overlays
                for selector in ['button:has-text("Accept")', 'button:has-text("Consent")',
                                  '.modal-close', '.overlay-close',
                                  'button:has-text("I Accept")', 'button:has-text("Got it")']:
                    try:
                        btn = page_obj.query_selector(selector)
                        if btn and btn.is_visible():
                            btn.click()
                            time.sleep(0.5)
                    except Exception:
                        pass

                # Scroll to trigger lazy content + wait for DOM stability
                scroll_and_wait(page_obj)

                # Run discovery-based extraction
                data = extract_page_complete(page_obj, cls, spec, page_name, url=url)

                # --- Validation pass (Phase 3.5a item G) ---
                warnings = validate_extraction(data, cls, spec, page_name)
                if warnings:
                    print(f"\n  ⚠ VALIDATION WARNINGS ({len(warnings)}):")
                    for w in warnings:
                        print(f"    - {w}")

                # Format and write markdown
                output = format_output(data)
                out_file = out_dir / f"{page_name}.md"
                out_file.write_text(output, encoding="utf-8")
                print(f"\n  Written: {out_file} ({len(output)} bytes)")

                # Save raw JSON for programmatic consumption
                json_file = out_dir / f"{page_name}.json"
                serializable = json.loads(json.dumps(data, default=str))
                json_file.write_text(json.dumps(serializable, indent=2, ensure_ascii=False),
                                     encoding="utf-8")
                print(f"  Written: {json_file}")

                # Write validation warnings to a separate file if any
                if warnings:
                    warn_file = out_dir / f"{page_name}_warnings.txt"
                    warn_file.write_text(
                        f"Spec: {cls}/{spec}\nPage: {page_name}\nURL: {url}\n"
                        f"Warnings ({len(warnings)}):\n" +
                        "\n".join(f"  - {w}" for w in warnings) + "\n"
                    )
                    print(f"  Written: {warn_file}")

            except Exception as e:
                print(f"  ERROR extracting {page_name}: {e}")
                import traceback
                traceback.print_exc()
                err_file = out_dir / f"{page_name}_error.txt"
                err_file.write_text(f"URL: {url}\nError: {e}\n{traceback.format_exc()}")

        browser.close()


def main():
    parser = argparse.ArgumentParser(description="Extract Wowhead tabbed content via browser (discovery-based)")
    parser.add_argument("cls", nargs="?", help="Class name (e.g., warlock, warrior)")
    parser.add_argument("spec", nargs="?", help="Spec name (e.g., affliction, fury)")
    parser.add_argument("--pages", default="rotation,talents,bis,consumables,tier",
                        help="Comma-separated pages to extract (default: all)")
    parser.add_argument("--all", action="store_true", help="Extract all specs")
    parser.add_argument("--dps-only", action="store_true", help="Skip tank specs")
    parser.add_argument("--dir", default=None,
                        help="Wowhead directory (default: auto-detect)")

    args = parser.parse_args()

    # Auto-detect wowhead dir
    wowhead_dir = args.dir
    if not wowhead_dir:
        script_dir = Path(__file__).parent
        if (script_dir / "generate_links.sh").exists():
            wowhead_dir = str(script_dir)
        else:
            wowhead_dir = str(Path.home() / "simc" / "wowhead")

    pages = [p.strip() for p in args.pages.split(",")]

    if args.all:
        for spec_key in ALL_SPECS:
            cls, spec = spec_key.split("/")
            if args.dps_only and get_role(spec) == "tank":
                print(f"Skipping tank spec: {cls}/{spec}")
                continue
            run_extraction(cls, spec, pages, wowhead_dir)
    elif args.cls and args.spec:
        run_extraction(args.cls, args.spec, pages, wowhead_dir)
    else:
        parser.print_help()
        print("\nExamples:")
        print("  python3 extract_wowhead_tabs.py warlock affliction --pages rotation")
        print("  python3 extract_wowhead_tabs.py warrior fury --pages rotation,talents,bis")
        print("  python3 extract_wowhead_tabs.py --all --dps-only --pages rotation")
        sys.exit(1)


if __name__ == "__main__":
    main()

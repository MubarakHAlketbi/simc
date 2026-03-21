#!/usr/bin/env python3
"""
Wowhead Tabbed Content Extractor — Discovery-Based
====================================================
Extracts ALL content hidden behind JS tabs on Wowhead guide pages.
Does NOT hardcode tab names or positions — discovers them dynamically.

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

Outputs: wowhead/<class>/<spec>/extracted/<page>.md

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
# Extraction strategy: click through ALL combinations
# ---------------------------------------------------------------------------

def extract_page_complete(page_obj, cls, spec, page_name, url=None):
    """
    Discovery-based extraction:
    1. Discover all interactive elements (hero switches, tab groups, talent toggles)
    2. Log the discovered structure
    3. Click through every combination and capture content
    4. Return structured results

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
        if hero_name:
            print(f"\n  === Hero Talent: {hero_name} ===")
            try:
                # Reload the page for each hero talent iteration.
                # Wowhead's JS replaces hero switch buttons with duplicated-text
                # artifacts after tab clicks, making them unclickable. A fresh
                # page load restores the original DOM reliably.
                page_obj.goto(url, wait_until="domcontentloaded", timeout=45000)
                time.sleep(5)
                # Scroll to load lazy content
                for _ in range(5):
                    page_obj.evaluate("window.scrollBy(0, 600)")
                    time.sleep(0.2)
                page_obj.evaluate("window.scrollTo(0, 0)")
                time.sleep(0.5)

                hn_js = json.dumps(hero_name)
                js_code = (
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
                clicked = page_obj.evaluate(js_code)
                if not clicked:
                    print(f"    SKIP: button not found via JS")
                    continue
                time.sleep(2)
            except Exception as e:
                print(f"    ERROR clicking hero switch: {e}")
                continue
        else:
            print(f"\n  === No hero switches found, extracting directly ===")

        results["content"][hero_name] = {}

        # Re-discover after hero switch (tabs may have changed)
        tab_groups_now = disc.discover_tab_groups()
        talent_toggles_now = disc.discover_toggle_buttons()

        if not tab_groups_now:
            # No tabs at all — just grab the page content
            print(f"    No tab groups found, capturing full page")
            results["content"][hero_name]["full_page"] = disc.get_page_content_snapshot()
            continue

        # Click through each tab in each group
        # Tab groups are ordered by DOM position (top to bottom)
        # Typically: Group 0 = main content tabs (ST/AoE/Opener)
        #            Group 1+ = sub-tabs within a section (cooldowns, advanced tips)

        for gi, group in enumerate(tab_groups_now):
            group_key = f"tab_group_{gi}"
            tab_names_in_group = [t["name"] for t in group]
            results["content"][hero_name][group_key] = {
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
                        results["content"][hero_name][group_key]["tabs"][tab_name] = "[TAB NOT FOUND]"
                        continue
                    time.sleep(1.0)
                except Exception as e:
                    print(f"      ERROR clicking tab: {e}")
                    results["content"][hero_name][group_key]["tabs"][tab_name] = f"[CLICK FAILED: {e}]"
                    continue

                # After clicking a main tab, check for talent toggles that appeared
                talent_toggles_in_panel = disc.discover_toggle_buttons()
                new_toggles = [t for t in talent_toggles_in_panel
                               if t["name"] not in [tt["name"] for tt in talent_toggles_now]]

                if new_toggles:
                    print(f"      Found {len(new_toggles)} talent toggles: {[t['name'] for t in new_toggles]}")

                # Capture content with current state
                panel_text = disc.get_visible_panel_text()
                if not panel_text:
                    panel_text = disc.get_page_content_snapshot()

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
                            tab_result["talent_variants"][toggle_name] = variant_text
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

                results["content"][hero_name][group_key]["tabs"][tab_name] = tab_result

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
                time.sleep(5)  # Wait for JS hydration (ads/trackers keep networkidle busy)

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

                # Scroll down to trigger lazy-loaded content
                for _ in range(5):
                    page_obj.evaluate("window.scrollBy(0, 600)")
                    time.sleep(0.3)
                # Scroll back to top
                page_obj.evaluate("window.scrollTo(0, 0)")
                time.sleep(1)

                # Run discovery-based extraction
                data = extract_page_complete(page_obj, cls, spec, page_name, url=url)

                # Format and write
                output = format_output(data)
                out_file = out_dir / f"{page_name}.md"
                out_file.write_text(output, encoding="utf-8")
                print(f"\n  Written: {out_file} ({len(output)} bytes)")

                # Also save raw JSON for programmatic consumption
                json_file = out_dir / f"{page_name}.json"
                # Strip non-serializable elements
                serializable = json.loads(json.dumps(data, default=str))
                json_file.write_text(json.dumps(serializable, indent=2, ensure_ascii=False),
                                     encoding="utf-8")
                print(f"  Written: {json_file}")

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

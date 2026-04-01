#!/usr/bin/env python3
"""
Extract per-spec data from simulationcraft.org raid report.

The page is JS-rendered — uses Playwright to get the live DOM, then
parses the rendered HTML into structured per-spec files.

Output layout:
  reference/simulationcraft_org/
    index.md                        -- DPS rankings table
    {class}/
      {spec_variant}/
        summary.md                  -- DPS, race, level, stats
        abilities.md                -- per-ability DPS breakdown
        apl.md                      -- action priority lists
        buffs.md                    -- buff uptime / procs
        talents.md                  -- talent string + gear

Usage:
  python3 scripts/extract_simc_org_report.py [URL]
  Default URL: https://simulationcraft.org/reports/MID1_Raid.html
"""

import sys
import re
import time
import asyncio
from pathlib import Path
from html.parser import HTMLParser

URL = sys.argv[1] if len(sys.argv) > 1 else "https://simulationcraft.org/reports/MID1_Raid.html"
OUT_BASE = Path(__file__).parent.parent / "reference" / "simulationcraft_org"

KNOWN_CLASSES = [
    "death_knight", "demon_hunter", "druid", "evoker",
    "hunter", "mage", "monk", "paladin", "priest",
    "rogue", "shaman", "warlock", "warrior",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def parse_profile_name(name: str):
    slug = re.sub(r"^MID1_", "", name).lower()
    slug = re.sub(r"[''`]", "", slug)
    for cls in KNOWN_CLASSES:
        if slug.startswith(cls + "_") or slug == cls:
            spec = slug[len(cls):].lstrip("_") or "base"
            return cls, spec
    return None


class _StripHTML(HTMLParser):
    """Convert HTML to readable plain text."""
    def __init__(self):
        super().__init__()
        self._buf = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip = True
        elif tag in ("br", "p", "h1", "h2", "h3", "h4", "li", "tr"):
            self._buf.append("\n")
        elif tag in ("td", "th"):
            self._buf.append("\t")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = False
        elif tag == "table":
            self._buf.append("\n")

    def handle_data(self, data):
        if not self._skip:
            self._buf.append(data)

    def handle_entityref(self, name):
        entities = {"nbsp": " ", "amp": "&", "lt": "<", "gt": ">", "quot": '"'}
        if not self._skip:
            self._buf.append(entities.get(name, ""))

    def result(self):
        text = "".join(self._buf)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def strip_html(html: str) -> str:
    p = _StripHTML()
    p.feed(html)
    return p.result()


def clean_table(text: str) -> str:
    """Remove blank lines and tidy up tab-separated table output."""
    lines = [l.rstrip() for l in text.splitlines() if l.strip()]
    return "\n".join(lines)


def find_player_section(section_html: str, css_class: str) -> str:
    """
    Extract content of <div class="player-section {css_class}">
    Returns the inner HTML of the first toggle-content div inside it.
    """
    # Match the player-section div opening
    pattern = re.compile(
        r'class="player-section[^"]*\b' + re.escape(css_class) + r'\b[^"]*"',
        re.IGNORECASE,
    )
    m = pattern.search(section_html)
    if not m:
        return ""
    # Find the toggle-content div that follows
    tail = section_html[m.end():]
    # skip to first toggle-content
    tc = re.search(r'<div[^>]*class="toggle-content[^"]*"[^>]*>(.*)',
                   tail[:200000], re.DOTALL | re.IGNORECASE)
    if not tc:
        return ""
    # Extract balanced content up to matching </div>
    # Simple approach: grab up to 200KB and return it — tables are self-contained
    return tc.group(1)[:150000]


def extract_table_from(html: str, nth: int = 0) -> str:
    """Extract the nth <table> from html and convert to text."""
    tables = list(re.finditer(r'<table[^>]*>(.*?)</table>', html, re.DOTALL | re.IGNORECASE))
    if nth >= len(tables):
        return ""
    return clean_table(strip_html(tables[nth].group(0)))


def extract_apl_table(section_html: str) -> str:
    """
    APL lives in <div class="player-section action-priority-list">.
    It's a <table> with columns: # | count | actions.listname
    We want the list name headers + action lines.
    """
    content = find_player_section(section_html, "action-priority-list")
    if not content:
        return ""

    lines_out = []
    # Find all th that contain "actions." — these are sub-list headers
    # Find all td rows — col 0=index, col 1=count, col 2=action text
    current_list = ""
    for row in re.finditer(r'<tr[^>]*>(.*?)</tr>', content, re.DOTALL | re.IGNORECASE):
        row_html = row.group(1)
        # Check if it's a header row (contains "actions.")
        th = re.search(r'<th[^>]*>(.*?)</th>', row_html, re.DOTALL | re.IGNORECASE)
        if th:
            header_text = strip_html(th.group(1))
            if "actions." in header_text.lower():
                # Extract just the list name part before <small>
                list_name = re.split(r'\s', header_text.split("actions.")[-1])[0]
                current_list = f"actions.{list_name}"
                lines_out.append(f"\n# {current_list}")
            continue

        # Data row — col 2 is the action
        tds = re.findall(r'<td[^>]*>(.*?)</td>', row_html, re.DOTALL | re.IGNORECASE)
        if len(tds) >= 3:
            action = strip_html(tds[2]).strip()
            if action and not action.startswith("#"):
                lines_out.append(action)

    return "\n".join(lines_out).strip()


# ---------------------------------------------------------------------------
# Playwright fetch
# ---------------------------------------------------------------------------
async def fetch_rendered_html(url: str) -> str:
    from playwright.async_api import async_playwright
    print(f"[browser] loading {url} ...")
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle", timeout=120000)
        await page.wait_for_selector("h2", timeout=30000)
        html = await page.content()
        await browser.close()
    print(f"[browser] got {len(html):,} bytes")
    return html


# ---------------------------------------------------------------------------
# Section splitting
# ---------------------------------------------------------------------------
def split_sections(html: str) -> list[tuple[str, str]]:
    no_scripts = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    pattern = re.compile(
        r'<h2[^>]*id="player\d+toggle"[^>]*>(.*?)</h2>',
        re.DOTALL | re.IGNORECASE,
    )
    matches = list(pattern.finditer(no_scripts))
    sections = []
    for i, m in enumerate(matches):
        raw = strip_html(m.group(1))
        name = re.split(r'\s*:\s*', raw)[0].strip().replace("\xa0", "").strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(no_scripts)
        sections.append((name, no_scripts[start:end]))
    return sections


# ---------------------------------------------------------------------------
# Data extractors
# ---------------------------------------------------------------------------
def extract_dps_line(section: str) -> dict:
    m = re.search(
        r'([\d,]+)\s*dps(?:,\s*([\d,]+)\s*dtps)?'
        r'(?:,\s*([\d,]+)\s*hps)?(?:\s*\(([\d,]+)\s*aps\))?',
        section[:600], re.IGNORECASE,
    )
    if not m:
        return {}
    return {k: v.replace(",", "") for k, v in zip(
        ("dps", "dtps", "hps", "aps"), m.groups()) if v}


def extract_params(section: str) -> dict:
    m = re.search(r'<ul class="params">(.*?)</ul>', section, re.DOTALL | re.IGNORECASE)
    if not m:
        return {}
    params = {}
    for line in strip_html(m.group(1)).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            params[k.strip().lower()] = v.strip()
    return params


def extract_talent_string(section: str) -> str:
    # Talent string is in the Profile section as: talents=XXXXX
    profile = find_player_section(section, "profile")
    m = re.search(r'\btalents=([A-Za-z0-9+/=]{20,})', profile) if profile else None
    if m:
        return m.group(1)
    # Fallback: search whole section for base64-like blob
    m2 = re.search(r'\btalents=([A-Za-z0-9+/=]{20,})', section)
    return m2.group(1) if m2 else ""


def extract_profile_text(section: str) -> str:
    """Extract the raw .simc profile text from the Profile section."""
    profile = find_player_section(section, "profile")
    if not profile:
        return ""
    # Strip HTML tags and decode entities
    text = re.sub(r'<[^>]+>', ' ', profile)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
    text = re.sub(r'\s+', '\n', text)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    # Keep only simc-like lines
    simc_prefixes = (
        "actions", "spec=", "level=", "talents=", "race=", "role=",
        "position=", "potion=", "flask=", "food=", "augmentation=",
        "temporary_enchant=", "#",
    ) + tuple(cls + "=" for cls in KNOWN_CLASSES)
    simc_lines = []
    for line in lines:
        if any(line.startswith(p) for p in simc_prefixes):
            simc_lines.append(line)
    return "\n".join(simc_lines)


def extract_abilities(section: str) -> str:
    """
    The Abilities section is an h3 "Abilities" followed by a table.
    We want just the top summary rows (not the per-ability detail stats).
    """
    # Find h3 "Abilities" then the first table
    m = re.search(r'<h3[^>]*>Abilities</h3>(.*?)<table[^>]*>(.*?)</table>',
                  section, re.DOTALL | re.IGNORECASE)
    if not m:
        return ""
    table_html = "<table>" + m.group(2) + "</table>"
    text = clean_table(strip_html(table_html))
    # Keep only meaningful rows — stop before "Stats Details:" drill-down
    lines = text.splitlines()
    out = []
    for line in lines:
        if line.strip().startswith("Stats Details:"):
            break
        out.append(line)
    return "\n".join(out)


def extract_buffs(section: str) -> str:
    """Buffs section table."""
    content = find_player_section(section, "buffs")
    return extract_table_from(content, 0) if content else ""


def extract_procs(section: str) -> str:
    """Procs/uptimes section table."""
    content = find_player_section(section, "procs")
    return extract_table_from(content, 0) if content else ""


def extract_gear_section(section: str) -> str:
    content = find_player_section(section, "gear")
    return clean_table(strip_html(content[:30000])) if content else ""


def extract_stats_section(section: str) -> str:
    content = find_player_section(section, "stats")
    return clean_table(strip_html(content[:10000])) if content else ""


# ---------------------------------------------------------------------------
# Write files
# ---------------------------------------------------------------------------
def write_spec(cls: str, spec: str, name: str, section: str) -> dict:
    out = OUT_BASE / cls / spec
    out.mkdir(parents=True, exist_ok=True)

    dps_info    = extract_dps_line(section)
    params      = extract_params(section)
    talent      = extract_talent_string(section)
    profile_txt = extract_profile_text(section)
    abilities   = extract_abilities(section)
    buffs       = extract_buffs(section)
    procs       = extract_procs(section)
    apl         = extract_apl_table(section)
    gear        = extract_gear_section(section)
    stats       = extract_stats_section(section)

    # --- summary.md ---
    lines = [
        f"# {name}", "",
        "## Simulation Info",
        "- Source: https://simulationcraft.org/reports/MID1_Raid.html",
        "- Build: 12.0.1.66709 Live  |  Hotfix: 2026-03-31",
        "- Fight style: Patchwerk  |  Iterations: 7500  |  Length: 240-360s", "",
        "## DPS Summary",
    ]
    for key, label in [("dps","DPS"), ("dtps","DTPS (tank dmg taken)"),
                       ("hps","HPS"), ("aps","APS (absorb)")]:
        if dps_info.get(key):
            lines.append(f"- {label}: {int(dps_info[key]):,}")
    if params:
        lines += ["", "## Character Info"]
        for k, v in params.items():
            lines.append(f"- {k.title()}: {v}")
    if talent:
        lines += ["", "## Talent String", "```", talent, "```"]
    if stats:
        lines += ["", "## Stats", "```", stats, "```"]
    (out / "summary.md").write_text("\n".join(lines) + "\n")

    # --- abilities.md ---
    if abilities:
        (out / "abilities.md").write_text(
            f"# {name} — Ability DPS Breakdown\n\n"
            "Columns: Spell | DPS | DPS% | Executes | Interval | Total Time | DPE | DPET | Type | Count | Hit | Crit | Avg | Crit% | Up%\n\n"
            f"```\n{abilities}\n```\n"
        )

    # --- buffs.md ---
    buf_out = ""
    if buffs:
        buf_out += f"## Buffs\n```\n{buffs}\n```\n\n"
    if procs:
        buf_out += f"## Procs & Uptimes\n```\n{procs}\n```\n"
    if buf_out:
        (out / "buffs.md").write_text(f"# {name} — Buffs & Procs\n\n{buf_out}")

    # --- apl.md ---
    if apl:
        (out / "apl.md").write_text(
            f"# {name} — Action Priority List\n\n"
            "Source: upstream SimC report (reference only — our APL may differ)\n\n"
            f"```\n{apl}\n```\n"
        )

    # --- talents.md ---
    t_lines = [f"# {name} — Talents & Gear", ""]
    if talent:
        t_lines += ["## Talent Export String", "```", talent, "```", ""]
    if gear:
        t_lines += ["## Gear", "```", gear, "```"]
    if talent or gear:
        (out / "talents.md").write_text("\n".join(t_lines) + "\n")

    # --- profile.simc --- (raw upstream profile — reference only)
    if profile_txt:
        (out / "profile.simc").write_text(
            f"# Upstream SimC reference profile — {name}\n"
            f"# Source: {URL}\n"
            f"# DO NOT use this to update our optimized profiles.\n\n"
            + profile_txt + "\n"
        )

    return dps_info


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    OUT_BASE.mkdir(parents=True, exist_ok=True)
    html = asyncio.run(fetch_rendered_html(URL))

    print("[parse] splitting sections...")
    sections = split_sections(html)
    print(f"[parse] found {len(sections)} player sections")

    results, skipped = [], []
    for name, sec in sections:
        parsed = parse_profile_name(name)
        if parsed is None:
            skipped.append(name)
            continue
        cls, spec = parsed
        dps_info = write_spec(cls, spec, name, sec)
        dps_val = int(dps_info.get("dps", 0))
        files = list((OUT_BASE / cls / spec).iterdir())
        print(f"  [ok] {cls}/{spec:<35} DPS={dps_val:>7,}  files={len(files)}")
        results.append((name, cls, spec, dps_info))

    if skipped:
        print(f"[skip] {skipped}")

    # --- index.md ---
    index_lines = [
        "# SimulationCraft.org MID1 Raid Report",
        "",
        "Source: https://simulationcraft.org/reports/MID1_Raid.html",
        "Build: 12.0.1.66709 Live | Fight: Patchwerk | Iterations: 7500",
        f"Extracted: {time.strftime('%Y-%m-%d')}",
        "",
        "## DPS Rankings",
        "",
        "| Rank | Profile | Class | DPS | DTPS | HPS |",
        "|------|---------|-------|-----|------|-----|",
    ]
    for rank, (name, cls, spec, s) in enumerate(
        sorted(results, key=lambda r: int(r[3].get("dps") or 0), reverse=True), 1
    ):
        dps  = f"{int(s['dps']):,}"  if s.get("dps")  else "-"
        dtps = f"{int(s['dtps']):,}" if s.get("dtps") else "-"
        hps  = f"{int(s['hps']):,}"  if s.get("hps")  else "-"
        index_lines.append(
            f"| {rank} | [{name}]({cls}/{spec}/summary.md) | {cls} | {dps} | {dtps} | {hps} |"
        )

    (OUT_BASE / "index.md").write_text("\n".join(index_lines) + "\n")
    print(f"\n[done] {len(results)} specs -> {OUT_BASE}")
    print(f"[done] index: {OUT_BASE / 'index.md'}")


if __name__ == "__main__":
    main()

# Talent Data Extraction — Technical Reference

**Author:** Hermes Agent
**Date:** 2026-03-16
**Purpose:** Reproducible methodology for extracting Wowhead Midnight talent data and comparing it against SimC source code.

---

## Overview

Talent data for all 33 DPS/tank specs was extracted from the Wowhead Midnight talent calculator and the Apex Talents guide, then diffed against SimC class module source. The full results are in `task_dossiers/talent_audit_wowhead_2026-03-16.md`.

---

## 1. Wowhead Talent Calculator

### URL Format

```
https://www.wowhead.com/talent-calc/{class}/{spec}/{hero}
```

Examples:
```
https://www.wowhead.com/talent-calc/death-knight/blood/deathbringer
https://www.wowhead.com/talent-calc/monk/mistweaver/conduit-of-the-celestials
https://www.wowhead.com/talent-calc/warlock/affliction/hellcaller
```

Class and spec slugs are lowercase hyphenated. The hero slug is the Hero Talent tree name, also lowercase hyphenated. When multiple hero trees exist for a spec, any valid one works — the class and spec tree content is identical regardless of hero choice.

### Why Direct HTTP Fetching Fails

The talent calculator is a React SPA. A plain HTTP GET returns an HTML shell with no talent data — the tree is rendered client-side from JavaScript. Tools like `urllib` or `requests` will receive an empty content area.

### Extraction Tool: Firecrawl

Firecrawl executes JavaScript before returning HTML, giving us the fully-rendered DOM including all talent nodes.

**Install:**
```bash
pip install firecrawl-py
```

**Authenticate:**
```bash
export FIRECRAWL_API_KEY=your_key_here
```

**Basic usage:**
```python
from firecrawl import Firecrawl

app = Firecrawl(api_key=os.environ["FIRECRAWL_API_KEY"])
result = app.scrape(url=url, formats=["html"])
html = result.html  # fully rendered HTML, ~200-350KB per page
```

Request the `"html"` format, not `"markdown"` or `"rawHtml"`. The `html` format is the post-JS-execution DOM. `rawHtml` is the pre-render shell. `markdown` is a Firecrawl summary that loses spell ID attributes.

---

## 2. DOM Structure

### Locating the Talent Tree

All talent nodes for a spec live inside a single container div with a `data-class-spec` attribute:

```html
<div class="dragonflight-talent-trees" data-class-spec="death-knight-blood">
  ...all class tree and spec tree nodes...
</div>
```

The attribute value is `{class}-{spec}` in lowercase hyphenated form, matching the URL slugs:

| URL | data-class-spec |
|-----|-----------------|
| `/talent-calc/death-knight/blood/...` | `death-knight-blood` |
| `/talent-calc/monk/windwalker/...` | `monk-windwalker` |
| `/talent-calc/warlock/affliction/...` | `warlock-affliction` |

The hero talent section is a separate div and is not included in `data-class-spec` — it only covers the class tree and spec tree.

### Talent Node Structure

Each talent node is an anchor tag with:
- `href` pointing to the Wowhead spell page (contains the spell ID)
- `aria-label` containing the talent name
- A child div with class `dragonflight-talent-tree-talent-name` also containing the name
- A child div with class `dragonflight-talent-tree-talent-rank` with `current/max` rank (e.g. `0/2`)

Example node HTML:
```html
<a
  data-wh-icon-size="medium"
  data-wh-touch-lightbox="true"
  href="https://www.wowhead.com/spell=48792/icebound-fortitude"
  aria-label="Icebound Fortitude"
  data-available="1"
>
  <div class="dragonflight-talent-tree-talent-name">Icebound Fortitude</div>
  <div class="dragonflight-talent-tree-talent-boundary">
    <div class="dragonflight-talent-tree-talent-inner">
      <div class="dragonflight-talent-tree-talent-rank">0/1</div>
    </div>
  </div>
</a>
```

Choice nodes (two alternatives on one node) contain two such anchor tags side by side within a shared wrapper.

### Spell ID Extraction

The spell ID is embedded directly in the `href`:

```
https://www.wowhead.com/spell=48792/icebound-fortitude
                               ^^^^^
                             spell ID
```

Regex to extract from the section:
```python
re.compile(
    r'href=["\']https://www\.wowhead\.com/(?:beta/)?spell=(\d+)/([a-z0-9\-]+)[^"\']*["\']'
    r'[^>]*?aria-label=["\']([^"\']+)["\']',
    re.DOTALL
)
```

Note the `(?:beta/)?` — some Midnight spell pages use `/beta/spell=` prefix, others just `/spell=`.

---

## 3. Extraction Script

The full extraction was done in batches of 11 specs in parallel (3 parallel subagents) to stay within time limits. Each batch used this core logic:

```python
def parse_talent_nodes(html, spec_key):
    # 1. Find the data-class-spec container
    pattern = re.compile(
        r'data-class-spec=["\']' + re.escape(spec_key) + r'["\']',
        re.IGNORECASE
    )
    m = pattern.search(html)
    if not m:
        return []

    # 2. Slice the relevant section (400KB is safe, trees are ~100-150KB)
    section = html[m.start(): m.start() + 400000]

    # 3. Extract all talent nodes via aria-label + spell href
    seen = set()
    talents = []
    node_re = re.compile(
        r'href=["\']https://www\.wowhead\.com/(?:beta/)?spell=(\d+)/([a-z0-9\-]+)[^"\']*["\']'
        r'[^>]*?aria-label=["\']([^"\']+)["\']',
        re.DOTALL
    )
    for m in node_re.finditer(section[:300000]):
        sid, slug, label = m.group(1), m.group(2), m.group(3).strip()
        if (sid, label) not in seen:
            seen.add((sid, label))
            talents.append({"spell_id": sid, "slug": slug, "name": label})

    return talents
```

Output per spec: a list of `{spell_id, slug, name}` dicts representing every talent node in the class tree + spec tree.

### Batch Structure

Three parallel subagent runs, each processing 11 specs:

| Batch | Specs | Output |
|-------|-------|--------|
| 0 | Blood DK → Augmentation Evoker | `/tmp/talent_audit/batch_0.json` |
| 1 | BM Hunter → Shadow Priest | `/tmp/talent_audit/batch_1.json` |
| 2 | Assassination Rogue → Prot Warrior | `/tmp/talent_audit/batch_2.json` |

Raw HTML per spec saved to `/tmp/talent_audit/{class}_{spec}.html` for debugging.

---

## 4. Apex Talents Guide

The Apex Talents overview page is a static guide (not a JS SPA), so it can be fetched with Firecrawl's `markdown` format or directly via the `web_extract` tool.

**URL:**
```
https://www.wowhead.com/guide/midnight/apex-talents-overview
```

**Fetch:**
```python
result = app.scrape(url=url, formats=["markdown"])
md = result.markdown  # ~44KB
```

The guide contains a table per class with columns: Spec, Apex Talent (name + spell link), Description (all three node descriptions inline as HTML).

**Spell ID extraction from guide:**
```python
spell_links = re.findall(
    r'https://www\.wowhead\.com/beta/spell=(\d+)/([a-z0-9\-]+)',
    content
)
```

**Coefficient extraction:**
```python
coefficients = re.findall(
    r'\(([0-9.]+%? of (?:Attack Power|Spell Power)[^\)]*)\)',
    content
)
```

The guide yielded 54 spell references covering all 33 DPS/tank specs' Apex Talent nodes plus their sub-spells (e.g. Necrotic Coil, Graveyard, Solar Bolt, etc.).

---

## 5. SimC Code Comparison

### What to search for

Each Wowhead talent name was checked against SimC source using three strategies in order:

1. **Direct spell ID** — the numeric ID appears as a literal in the code (most reliable):
   ```python
   re.search(r'\b' + spell_id + r'\b', code)
   ```

2. **Slug match** — the hyphenated URL slug converted to underscores:
   ```python
   slug.replace("-", "_") in code   # e.g. "icebound_fortitude"
   ```

3. **Name string match** — the full talent name lowercased anywhere in source:
   ```python
   talent_name.lower() in code.lower()
   ```

A talent is considered "present" if any of the three match.

### Files searched per spec

Primary file is the main class module. Additional files are searched for classes with subdirectory layouts:

| Class | Primary | Additional |
|-------|---------|------------|
| DK | `sc_death_knight.cpp` | — |
| DH | `sc_demon_hunter.cpp` | — |
| Druid | `sc_druid.cpp` | — |
| Evoker | `sc_evoker.cpp` | — |
| Hunter | `sc_hunter.cpp` | — |
| Mage | `sc_mage.cpp` | — |
| Monk | `monk/sc_monk.cpp` | `monk/sc_monk.hpp` |
| Paladin (Prot) | `paladin/sc_paladin_protection.cpp` | `paladin/sc_paladin.cpp`, `paladin/sc_paladin.hpp` |
| Paladin (Ret) | `paladin/sc_paladin_retribution.cpp` | `paladin/sc_paladin.hpp` |
| Priest (Shadow) | `priest/sc_priest_shadow.cpp` | `priest/sc_priest.hpp`, `priest/sc_priest.cpp` |
| Rogue | `sc_rogue.cpp` | — |
| Shaman | `sc_shaman.cpp` | — |
| Warlock | `warlock/sc_warlock_init.cpp` | `warlock/sc_warlock.hpp`, `warlock/sc_warlock_actions.cpp` |
| Warrior | `sc_warrior.cpp` | — |

All files live under `engine/class_modules/`.

### Known false negatives

The string-match approach can produce false negatives for:
- Talents with very short or common names (e.g. "Banish" matches many things)
- Talents whose SimC name differs from the Wowhead display name (e.g. a talent called "Improved Mortal Coil" in Wowhead may be `mortal_coil_2` in SimC)
- Pure utility talents intentionally omitted from SimC (CC, movement, heals)

When a talent shows as missing, always fetch the Wowhead spell page and manually inspect the SimC file before assuming it needs implementation.

---

## 6. Reproducing the Audit

To re-run the full audit from scratch:

```bash
# 1. Fetch all specs (run in parallel as 3 separate processes or subagents)
export FIRECRAWL_API_KEY=your_key
python3 /tmp/fetch_batch.py 0   # specs 0-10
python3 /tmp/fetch_batch.py 1   # specs 11-21
python3 /tmp/fetch_batch.py 2   # specs 22-32

# 2. Run the diff against SimC source
python3 /tmp/compare_talents.py

# 3. Review output
cat /tmp/talent_audit/diff_report.json
```

Scripts are saved at:
- `/tmp/fetch_batch.py` — fetches and parses Wowhead HTML per batch
- `/tmp/compare_talents.py` — loads batch JSON, diffs against SimC, prints report
- `/tmp/inspect_talent_dom.py` — one-off DOM inspector used to discover structure

Raw data (HTML + JSON) is in `/tmp/talent_audit/`. Note: `/tmp` is ephemeral — re-fetch if the machine restarts.

---

## 7. Adding a New Spec

When a new spec is added to the game or needs to be audited:

1. Find the correct URL:
   ```
   https://www.wowhead.com/talent-calc/{class}/{spec}/{any-valid-hero}
   ```

2. Fetch with Firecrawl:
   ```python
   result = app.scrape(url=url, formats=["html"])
   html = result.html
   ```

3. Parse using `parse_talent_nodes(html, f"{class}-{spec}")`

4. Add the spec and its SimC file path to the `SIMC_FILES` dict in `compare_talents.py`

5. Re-run `compare_talents.py` and review the output

---

## 8. Caveats

- Firecrawl costs API credits per page fetch (~1 credit per page). Full 33-spec audit costs ~33 credits.
- The talent calculator pages are ~200-350KB each after JS execution.
- Wowhead sometimes uses `/beta/spell=` and sometimes `/spell=` in hrefs on the same page — the regex handles both.
- Some aria-labels are truncated at apostrophes or special characters (e.g. "Hunter" instead of "Hunter's Avoidance"). Cross-reference with the slug when the name looks wrong.
- The Demonology Warlock Apex Talent (spell 1264137) has incomplete data in the guide as of 2026-03-16 — the guide comment section confirms this is a known Wowhead error.

---

*Last updated: 2026-03-16*

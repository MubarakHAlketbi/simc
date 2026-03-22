# Wowhead Extraction Pipeline — Audit & Improvement Plan

Last updated: 2026-03-22 (v2 — expanded with full 33-spec audit + parser + consumer analysis)

---

## Summary Verdict

The pipeline is browser inner_text() scraping with zero post-processing, zero semantic
parsing, and zero validation. The data is NOT reliably accurate for direct APL use without
significant cleanup. Additionally, the downstream parser (gen_apl_diff.py) fails on 17 of
33 specs due to format assumptions, and 6 specs have missing hero talent sections.

---

## Architecture Overview

- **Producer:** `wowhead/extract_wowhead_tabs.py` (784 lines, Playwright/Chromium headless)
- **Consumers:**
  - `wowhead/gen_apl_diff.py` — reads rotation.md (never .json)
  - `wowhead/update_talents_from_extracted.py` — reads talents.md (never .json)
  - Manual agent reference via AGENTS.md directives
- **Output:** .md (human-readable) + .json (structured) per page per spec
- **Key fact:** .json files are currently unused by any downstream consumer

### How the extractor works

- Discovers `[role="tablist"]` for tab groups, `<button>` text-matched against
  ALL_HERO_TALENT_NAMES for hero switches, heuristic CSS-class for toggle buttons
- Clicks via `page.evaluate()` injected JS (immune to stale element handles)
- Extracts content via `element.inner_text()` on visible `[role="tabpanel"]` — no
  BeautifulSoup, no regex, no semantic parsing
- Full page reload between hero talent iterations (prevents "SlayerSlayer" DOM artifact)
- Lazy load: 5x `window.scrollBy(0, 600)` + fixed 5s sleep (no event-driven waiting)

---

## Problem 1: Comment Widget Pollution (ALL 33 specs)

Every subtab section ends with the full Wowhead forum comment widget as plain text.
Appears **28–88 times per file** across all 33 specs. Example junk injected everywhere:

```
1 - 1 of 1 / Subject / Posted / Author / Replies /
How to Play Your Class in the Battle for Azeroth 8.0 Pre-Patch
On 2018/07/21 Anshlun 75 / Please keep the following in mind when posting a comment /
You are not logged in...
```

Full pollution counts per spec:

| Spec | Pollution Count |
| :--- | ---: |
| warrior/fury | 88 |
| hunter/survival, warrior/arms, warlock/demonology | 80 |
| demon-hunter/havoc, druid/feral, rogue/assassination, rogue/subtlety | 72 |
| shaman/elemental, shaman/enhancement, monk/brewmaster, paladin/protection | 72 |
| death-knight/frost, druid/balance, mage/fire, hunter/beast-mastery | 64 |
| rogue/outlaw, warlock/affliction, warlock/destruction, warrior/protection | 64 |
| priest/shadow | 56 |
| death-knight/blood, evoker/devastation, demon-hunter/devourer | 48 |
| hunter/marksmanship | 48 |
| evoker/augmentation, demon-hunter/vengeance, mage/arcane, monk/windwalker | 40 |
| paladin/retribution | 36 |
| mage/frost | 32 |
| death-knight/unholy | 28 |

---

## Problem 2: Missing Hero Talent Sections (6 specs)

6 of 33 specs have fewer than 2 hero talent sections extracted. The extractor failed to
detect or click the second hero talent button.

| Spec | Hero Sections Found | Missing Hero Talent |
| :--- | :---: | :--- |
| paladin/retribution | 0 | BOTH hero talents missing |
| death-knight/unholy | 1 | Second hero tree not captured |
| druid/guardian | 1 | Second hero tree not captured |
| mage/arcane | 1 | Second hero tree not captured |
| monk/brewmaster | 1 | Second hero tree not captured |
| monk/windwalker | 1 | Shado-pan not captured |

**paladin/retribution is the worst case — zero hero talent sections.**

Root cause: the hero talent button was either not found (not matching ALL_HERO_TALENT_NAMES),
not visible in viewport, or the `data-active` check prevented the click. The current script
has no validation to detect or retry these failures.

---

## Problem 3: Repeated Explanatory Blocks (ALL specs)

Tab panels share a "details" sidebar that gets extracted under every tab. Example: the
Combustion explanation for Mage Fire appears verbatim 4–8 times per hero talent section.
Files are inflated 3–5x beyond their unique content.

| Spec | Line Count | Est. Unique Lines |
| :--- | ---: | ---: |
| evoker/devastation | 8,313 | ~800 (10x inflation) |
| demon-hunter/devourer | 3,204 | ~400 |
| evoker/augmentation | 2,517 | ~300 |
| mage/arcane | 1,646 | ~300 |
| mage/fire | 1,515 | ~300 |
| monk/brewmaster | 1,518 | ~300 |
| Average spec | ~1,000 | ~200–300 |

**evoker/devastation at 8,313 lines is the worst — almost certainly massive duplication.**

---

## Problem 4: APL Diff Parser Broken for 17 Specs

`gen_apl_diff.py` reads rotation.md and tries to extract priority steps. It fails on
17 of 33 specs, flagging them as NEEDS_MANUAL_REVIEW. The data IS in the .md files —
the parser just can't read it.

**Three root causes:**

### A. "Use" prefix not handled (mainly tanks)
The parser only recognizes "Cast " and "Precast " line prefixes. Many specs use "Use X":

| Spec | "Use" Lines | "Cast" Lines | Parser Result |
| :--- | ---: | ---: | :--- |
| demon-hunter/vengeance | 94 | 0 | FAIL — 0 steps extracted |
| monk/brewmaster | 31 | 2 | FAIL — only 2 of 33 steps |
| druid/guardian | ~20 | ~5 | FAIL |

### B. Inline spell name format (no Cast/Use prefix)
Some specs use indented spell names without any prefix:
```
 Rampage over 100 rage
 Bladestorm
 Raging Blow
```
Under "DURING COOLDOWNS" / "OUTSIDE COOLDOWNS" headers instead of "PRIORITY".
Warrior Fury is the primary example.

### C. Tab name mismatch
The parser expects "Single-Target Priority" or "AoE Priority" tab names. Some specs use
different names: "Single Target", "Multitarget", "Burst", "Sustained", etc.

**Full list of 17 affected specs:**

| # | Spec | Primary Failure Reason |
| :--- | :--- | :--- |
| 1 | demon-hunter/vengeance | "Use" format |
| 2 | druid/balance | Mixed format |
| 3 | druid/guardian | "Use" format |
| 4 | evoker/augmentation | Support spec format |
| 5 | hunter/beast-mastery | Format mismatch |
| 6 | hunter/marksmanship | Format mismatch |
| 7 | hunter/survival | Format mismatch |
| 8 | mage/arcane | Format mismatch |
| 9 | monk/brewmaster | "Use" format |
| 10 | monk/windwalker | Format mismatch |
| 11 | priest/shadow | Format mismatch |
| 12 | rogue/assassination | Format mismatch |
| 13 | shaman/elemental | Format mismatch |
| 14 | shaman/enhancement | Format mismatch |
| 15 | warlock/affliction | Format mismatch |
| 16 | warlock/demonology | Format mismatch |
| 17 | warrior/fury | Inline spell names (no prefix) |

---

## Problem 5: Mid-Sentence Truncation (lazy load timing)

Shaman Elemental AoE section cuts off:
```
AoE starts at 2 targets and focusses on spamming  Chain Lightning and [
```
The fixed-sleep lazy load (5x scrollBy + 5s sleep) is not reliable. Content was not fully
rendered when inner_text() was called.

---

## Problem 6: Interactive Content as Dead Stubs (Mage Fire)

Animated/interactive components render as empty text labels:
- `"Display Animated Double Pyroblast Example"`
- `"Double Pyroblast Exercise"`

Fundamental limitation of inner_text() — cannot capture interactive content.

---

## Problem 7: .json Files Unused by Downstream Consumers

Both consumers read .md only:
- `gen_apl_diff.py` → reads rotation.md
- `update_talents_from_extracted.py` → reads talents.md

The .json files have a consistent schema across all specs and pages:
```json
{
  "spec": "warlock/affliction",
  "page": "rotation",
  "url": "...",
  "discovered_structure": {
    "hero_switches": ["Hellcaller", "Soul Harvester"],
    "tab_groups": [["Single-Target Priority", "AoE Priority", ...], ...],
    "talent_toggles": []
  },
  "content": {
    "HeroName": {
      "tab_group_0": {
        "tab_names": ["Single-Target Priority", "AoE Priority"],
        "tabs": {
          "Single-Target Priority": { "content": "..." }
        }
      }
    }
  }
}
```

**Quirk:** When no hero switches exist, the content key is the literal string `"null"`
instead of JSON null. This is valid JSON but semantically wrong.

**Decision needed:** Standardize on .json as the canonical format and port consumers,
or enforce strict .md structure. JSON is the better choice — already structured, already
consistent, and immune to parsing ambiguity.

---

## Problem 8: Outlier Files

| File | Lines | Issue |
| :--- | ---: | :--- |
| evoker/devastation/rotation.md | 8,313 | 10x expected size — massive duplication |
| demon-hunter/devourer/rotation.md | 3,204 | "Devourer" is a hero talent, not a spec — may be an erroneous directory or alias for Havoc |

---

## Problem 9: Downstream Profile Data Gaps

Issues found by cross-checking extracted data against actual .simc profiles:

| Profile | Issue |
| :--- | :--- |
| MID1_Rogue_Assassination.simc | NO active `talents=` line — commented out. 6 valid codes in extracted/talents.md never applied. |
| MID1_Warlock_Affliction_Hellcaller.simc | Uses same talent hash as base Affliction profile. Should use Hellcaller-specific code. |
| MID1_Warlock_Affliction.simc | Shoulders mismatch: BiS says `mantle_of_dark_devotion`, profile has `echoing_void_mantle`. |

---

## Implementation Plan

### Phase 3.5a — Extractor Pipeline Fixes

| Priority | ID | Change | Effort | Impact |
| :---: | :--- | :--- | :--- | :--- |
| 1 | G | Validation pass after each extraction — count hero sections, check for placeholders, flag short files, detect truncation | Easy | Catches all failures at extraction time |
| 2 | A | Strip comment widget noise — anchor on "1 - 1 of 1", "You are not logged in", "Please keep the following in mind" | Easy | Eliminates BfA junk from all 33 files |
| 3 | B | Deduplicate repeated blocks — paragraph-level dedup within each hero talent section | Easy | 3–5x file size reduction |
| 4 | E | Hero talent click verification + retry — verify data-active="true" after click, retry on failure | Medium | Fixes 6 specs with missing hero talents |
| 5 | C | Target priority list container directly — extract from specific CSS selectors, not entire tabpanel | Medium | Eliminates noise at DOM level |
| 6 | D | Mutation observer for lazy load — replace fixed sleep with event-driven waiting | Medium | Fixes mid-sentence truncation |

### Phase 3.5b — Downstream Consumer Fixes

| Priority | ID | Change | Effort | Impact |
| :---: | :--- | :--- | :--- | :--- |
| 7 | H | Fix gen_apl_diff.py parser — handle "Use X", inline spell names, varied tab names | Medium | Fixes 17/33 specs from NEEDS_MANUAL_REVIEW |
| 8 | I | Fix "null" string key in JSON — use empty string or "default" when no hero switches | Easy | Prevents downstream bugs |
| 9 | J | Port consumers to .json — gen_apl_diff.py and update_talents_from_extracted.py read .json instead of .md | Medium | Structured data, no parsing ambiguity |
| 10 | K | Enforce universal .md output structure — strict section headers, consistent Cast/Use format | Medium | Only needed if staying with .md (alternative to J) |

### Phase 3.5c — Re-extraction + Profile Fixes

| Priority | ID | Change | Effort | Impact |
| :---: | :--- | :--- | :--- | :--- |
| 11 | L | Re-extract 6 specs with missing hero talents (after E is implemented) | Easy | Completes data for paladin/ret, DK/unholy, druid/guardian, mage/arcane, monk/brew+ww |
| 12 | M | Investigate demon-hunter/devourer directory — confirm if valid or erroneous | Easy | Cleanup |
| 13 | N | Investigate evoker/devastation 8313-line file — confirm duplication extent | Easy | Cleanup |
| 14 | O | Fix 3 profile data gaps (Rogue Assassination talents, Warlock Affliction Hellcaller talents, Warlock shoulders) | Easy | Profile accuracy |

---

## Execution Order

```
Phase 3.5a (extractor fixes):
  G → A → B → E → C → D
  
Phase 3.5b (consumer fixes):
  H → I → J (or K if staying with .md)

Phase 3.5c (re-extract + profiles):
  L → M → N → O

Then: re-run gen_apl_diff.py to produce updated APL_diff_report.md
Then: proceed to Phase 4 (APL optimization loop)
```

---

## Re-Extraction Commands (after pipeline improvements)

```bash
# Re-extract the 6 specs with missing hero talents
python3 wowhead/extract_wowhead_tabs.py paladin retribution --pages rotation
python3 wowhead/extract_wowhead_tabs.py death-knight unholy --pages rotation
python3 wowhead/extract_wowhead_tabs.py druid guardian --pages rotation
python3 wowhead/extract_wowhead_tabs.py mage arcane --pages rotation
python3 wowhead/extract_wowhead_tabs.py monk brewmaster --pages rotation
python3 wowhead/extract_wowhead_tabs.py monk windwalker --pages rotation

# Full re-extraction (all specs, all pages — after all fixes)
python3 wowhead/extract_wowhead_tabs.py --all --pages rotation,talents,bis,consumables,tier
```

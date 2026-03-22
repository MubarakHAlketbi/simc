# AGENTS.md - SimulationCraft Midnight Expansion Update

**Last Updated: 2026-03-22 (APL optimization pipeline + Wowhead browser extraction added)**

## Objective

Update SimulationCraft to fully support World of Warcraft's new "Midnight" expansion, ensuring accurate simulation of all new class talents, spells, abilities, gear, and game mechanics. Continuously improve APL (Action Priority List) quality for all 33 DPS/tank specs using automated optimization.

## Context

**SimulationCraft** is an open-source combat simulation engine for World of Warcraft. It models player characters, enemies, and combat mechanics to evaluate DPS, HPS, and other performance metrics. Players and theorycrafters rely on it for gear optimization, talent comparisons, and stat weight calculations.

The "Midnight" expansion introduces significant changes including:
- New talent trees and revamped class abilities
- Updated itemization and gear systems
- New combat mechanics and buff/debuff systems
- Level cap changes and new spells
- Class-specific changes and reworks

---

## Primary Data Source: Wowhead

**Wowhead (www.wowhead.com/midnight) is the canonical ground truth** for all Midnight expansion data. This includes:

- Spell IDs, tooltips, and descriptions
- Talent trees and ranks
- Item stats, set bonuses, and special effects
- Class changes and ability updates
- Rotation priorities and cooldown usage
- BiS gear recommendations
- Enchants, gems, consumables
- Tier set bonus effects

**General Procedure:**
1. Always verify data against Wowhead's Midnight database
2. Record the URL or build ID used for each piece of data
3. Note the retrieval date (format: YYYY-MM-DD) in comments
4. If Wowhead is unclear, cross-reference with official Blizzard patch notes

Example: `# Source: https://www.wowhead.com/spell=123456&expand=1 (2026-03-15)`

**Special Procedure for Trinkets and Gear with Special Effects:**

Many trinkets and gear effects use "dummy" or "token" spells to handle scaling. The item page shows a summary, but the full mechanics are defined in a separate spell page.

**Steps:**
1. On the item page, locate the spell ID linked in the "Item Effect" section.
2. Extract the item page data: base numbers, cooldown, description text.
3. Navigate to the spell page (https://www.wowhead.com/spell=SPELL_ID) for detailed mechanics.
4. If the spell page references a "Scaling Token" or "Dummy" spell, fetch that too.
5. Determine if displayed numbers are static or item-level dependent.

**Important:** Document both the item URL and the spell URL(s) in code comments.

---

## Wowhead Knowledge Base (`wowhead/` folder)

A pre-fetched, structured knowledge base lives in the `wowhead/` directory at the repo root.
It covers all 33 DPS/tank specs and was built from live Wowhead Midnight data.

### Folder Layout

```
wowhead/
  generate_links.sh          — generates info_links.md for every spec
  extract_wowhead_tabs.py    — browser extractor for JS-tabbed Wowhead pages
  gen_apl_diff.py            — APL diff analysis script (compares wowhead vs SimC APL)
  APL_diff_report.md         — Phase 2 diff results for all 33 specs
  {class}/
    {spec}/
      info_links.md          — canonical Wowhead URLs (guides + talent-calc + bis + tier)
      info_base.md           — comprehensive pre-fetched information base (2026-03-17)
      extracted/             — browser-extracted JS-tab content (2026-03-22)
        rotation.md          — full rotation content: all hero talents × all tabs
        rotation.json        — same, machine-readable
        talents.md           — all talent builds with export codes
        talents.json
        bis.md               — BiS gear by slot
        bis.json
        consumables.md       — enchants, gems, potions, food, flasks
        consumables.json
        tier.md              — tier set bonuses (2pc and 4pc effects)
        tier.json
```

Class and spec names use lowercase hyphenated slugs matching Wowhead URL conventions
(e.g. `beast-mastery`, `death-knight`).

### What `info_base.md` Contains (2026-03-17 snapshot)

Each file is a self-contained reference document with these sections:

| Section | Contents |
|---------|----------|
| **Sources** | All URLs used — guide pages and talent-calc pages |
| **Overview** | Role, playstyle identity, strengths/weaknesses |
| **Stat Priority** | Exact stat ranking per hero talent variant |
| **Core Abilities** | Key spells and resource mechanics |
| **Abilities & Talents Detail** | Full ability list with descriptions |
| **Rotation / Priority** | ST opener, priority list, AoE rotation, cooldown usage |
| **Enchants, Gems, Consumables** | Recommended enchants per slot, gems, potions, food |
| **Talent Tree — Class & Spec** | Complete table: Spell ID \| Name \| Max Rank \| Wowhead link |
| **Hero Talent Tree 1** | Complete table for first hero tree |
| **Hero Talent Tree 2** | Complete table for second hero tree |
| **SimC Implementation Notes** | Callouts for mechanically complex talents |

### What `extracted/` Contains (2026-03-22 snapshot)

The `extracted/` subdirectory contains **browser-extracted content** from JS-rendered Wowhead pages. Wowhead hides rotation priorities, talent builds, and gear behind JavaScript tabs — `web_extract` and curl cannot access this content. The browser extractor clicks through every tab combination and captures the result.

**Critical difference from `info_base.md`:**
- `info_base.md` was built with Firecrawl/web_extract — missed JS-tab content
- `extracted/rotation.md` was built with the Playwright browser extractor — has ALL tab content including per-hero-talent priority lists, AoE priorities, openers, and cooldown sub-tabs

**`extracted/rotation.md` structure:**
```
## Hero Talent: HeroName
### tab_group_0 — Tabs: [Single-Target Priority, AoE Priority, Opener, Pre-Combat Checks]
#### Single-Target Priority
Cast  Haunt.
Cast  Agony.
Cast  Wither.
...
### tab_group_1 — Tabs: [Darkglare, Dark Harvest, Malevolence]  <- cooldown sub-tabs
#### Darkglare
...
```

**`extracted/talents.md` structure:**
Contains all talent build names and export codes (base64 talent strings) that can be
directly imported into SimC profiles via the `talents=` field.

### When to Use Which Source

| Task | Use |
|------|-----|
| Look up spell IDs / talent tree | `info_base.md` → Talent Tree section |
| Get rotation priority for a spec | `extracted/rotation.md` (NOT info_base.md — it misses tab content) |
| Get talent build export codes | `extracted/talents.md` |
| Get BiS gear for a profile | `extracted/bis.md` |
| Get enchants/consumables for a profile | `extracted/consumables.md` |
| Get tier set bonus effects | `extracted/tier.md` |
| Verify a spell ID | `info_base.md` Talent Tree table |
| Get Wowhead URL for fresh fetch | `info_links.md` Sources section |

### When to Re-Fetch from Wowhead

The knowledge base reflects Wowhead data as of 2026-03-22. Re-fetch when:

1. A spell was patched after that date.
2. A talent is missing and not explained by known false negatives.
3. You need an exact damage formula not captured in the guide text.

To re-extract a single spec's rotation:
```bash
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation
```

To re-extract all specs:
```bash
python3 wowhead/extract_wowhead_tabs.py --all --pages rotation,talents,bis,consumables,tier
```

---

## Browser Extraction Tool (`wowhead/extract_wowhead_tabs.py`)

**Purpose:** Extracts content from JS-rendered Wowhead guide pages by running a real browser
(Playwright/Chromium) and clicking through all tab combinations.

**Why it exists:** Wowhead uses React/JS to render rotation priorities, talent builds, and gear
recommendations inside tab components. Plain HTTP fetches (web_extract, curl, Firecrawl) return
only a placeholder "Please select a Hero Talent" string. Only a real browser can click the tabs
and capture the rendered content.

**Discovery-based design:** The script does NOT hardcode tab names or positions. It:
1. Discovers all `[role="tab"]` groups, hero talent switch buttons, and talent toggle buttons
2. Classifies each element (hero switch vs content tab vs talent toggle)
3. Clicks through every combination, re-discovering after each click
4. Handles specs where hero switches appear above tabs (Warlock) vs inside tab panels (Warrior)
5. Handles varying tab counts (2 groups for Rogue, 3 groups for Warrior/Warlock)

**Known Wowhead quirks handled:**
- Hero talent buttons use `data-active="true"` — clicking an already-active button DESELECTS it (adds placeholder). Script checks before clicking.
- After clicking the last tab in a group, Wowhead re-renders hero switch buttons as duplicated-text artifacts (`"SlayerSlayer"`). Fix: reload the page for each hero talent iteration.
- JS-based clicking by text (not element handles) — immune to stale DOM references.

**Requirements:**
```bash
pip install playwright
playwright install chromium
```

**Usage:**
```bash
# Single spec, single page
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation

# Single spec, all pages
python3 wowhead/extract_wowhead_tabs.py warrior fury --pages rotation,talents,bis,consumables,tier

# All specs, rotation only
python3 wowhead/extract_wowhead_tabs.py --all --pages rotation

# All specs, all pages (takes ~60 min)
python3 wowhead/extract_wowhead_tabs.py --all

# All specs excluding tanks
python3 wowhead/extract_wowhead_tabs.py --all --dps-only
```

**Output:** For each spec/page: `.md` (human-readable) and `.json` (machine-readable) in
`wowhead/{class}/{spec}/extracted/`.

---

## APL Optimization Pipeline

Full specification: `APL_optimization.md`

### Overview

The APL optimization pipeline improves Action Priority Lists for all specs using:
- **Two fight styles**: Patchwerk (50% weight) + HecticAddCleave (50% weight)
- **Multi-build validation**: APL must work for ALL talent builds (up to 8 per spec)
- **Automated loop**: permutation candidates, condition sweeps, convergence at <0.1% delta
- **LLM-assisted review**: optional final step using spec's info_base.md for non-obvious synergies

### Phases

| Phase | Description | Status |
| :--- | :--- | :--- |
| Phase 1 | Browser extraction (rotation, talents, bis, consumables, tier) | COMPLETE |
| Phase 2 | APL validation — diff all specs vs Wowhead | COMPLETE — 2 fixes |
| Phase 3 | Profile updates — BiS gear + talent builds from extracted data | NEXT |
| Phase 4 | Optimization loop — composite DPS scoring | PENDING |
| Phase 5 | Trinket combinatorics — sim all BiS pairs | PENDING |

### Sim Commands

```bash
# Build the binary
cd engine && make -j$(nproc)

# 1-iteration smoke test
./engine/simc profiles/MID1/PROFILE.simc iterations=1 output=/dev/null

# Patchwerk baseline
./engine/simc input=profiles/MID1/PROFILE.simc iterations=10000 \
  fight_style=Patchwerk desired_targets=1 json2=results/SPEC_patchwerk.json

# HecticAddCleave baseline
./engine/simc input=profiles/MID1/PROFILE.simc iterations=10000 \
  fight_style=HecticAddCleave desired_targets=1 json2=results/SPEC_hecticaddcleave.json
```

### APL Rules (quick reference — full rules in APL_optimization.md)

1. One `variables` sub-list, called first
2. Trinkets always in a separate `trinkets` sub-list
3. Hero-tree routing is mandatory (`run_action_list,if=hero_tree.X`)
4. DoT refresh threshold: `dot.X.remains<=gcd` (never hard-code times)
5. Never cap resources
6. Cooldowns fire inside buff windows
7. Execute-phase branching via `variable.execute_phase`
8. Racials/externals before hero routing, aligned with primary CD
9. No redundant conditions inside gated sub-lists
10. Use `op=setif` for ternary variable assignments

---

## APL Diff Tool (`wowhead/gen_apl_diff.py`)

**Purpose:** Compares Wowhead rotation guide priorities against current SimC APL for every spec.

**How it works:**
1. Parses `extracted/rotation.md` to extract "Cast X" priority steps
2. Reads SimC APL from both profile `.simc` files and C++ generator files
3. Maps Wowhead spell names → SimC action names (300+ entry mapping table)
4. Categorizes each action: MATCH / MISSING / ORDER_DIFF / CONDITION_DIFF / EXTRA
5. Outputs `wowhead/APL_diff_report.md`

**Usage:**
```bash
python3 wowhead/gen_apl_diff.py
```

**Important caveats when reading the report:**
- MISSING flags are often false positives: engine-managed replacement actions, passive features,
  or buff procs that don't have standalone castable actions
- ORDER_DIFF is usually acceptable — SimC APLs optimize for sim accuracy, not 1:1 human guide order
- NEEDS_MANUAL_REVIEW means the parser couldn't extract steps (usually because Wowhead used a
  timeline image instead of text for the opener)
- Always verify before acting on a MISSING flag

---

## Task Dossier System

**MANDATORY:** Before implementing any task, create a complete dossier in `task_dossiers/` that consolidates all necessary information.

### Process

1. **Pick a task** from `project_progress.md`
2. **Create a dossier** in `task_dossiers/` using `TASK_DOSSIER_TEMPLATE.md`
3. **Fetch and populate** all ground truth data (Wowhead URLs, formulas, spell IDs)
4. **Complete the dossier** including target files, verification checklist, code change plan
5. **Edit code** based ONLY on the dossier contents
6. **After completion**, add dossier to git and reference it in commit

### Existing Dossiers

| File | Scope |
|------|-------|
| `rogue_general_2026-03-16.md` | Rogue Assassination/Outlaw/Subtlety general changes |
| `shaman_elemental_2026-03-16.md` | Elemental Shaman general changes + APL |
| `warlock_general_2026-03-16.md` | Warlock Affliction/Demo/Destro general changes |
| `talent_audit_wowhead_2026-03-16.md` | Full talent audit: all 33 specs vs Wowhead |

---

## Project Tracking

**`project_progress.md`** is the primary source of truth for all implementation status.

Statuses: **Implemented** | **In Beta** | **NYI** | **N/A**

**Before making changes, always consult `project_progress.md`.**
Update it immediately when a task is completed.

---

## Agent Development Workflow

**1. Session Start Protocol**
- Read `AGENTS.md` and `project_progress.md`
- For rotation/APL work: read `wowhead/{class}/{spec}/extracted/rotation.md` (NOT info_base.md)
- For talent/spell IDs: read `wowhead/{class}/{spec}/info_base.md`
- Check `task_dossiers/` for existing dossier before creating a new one

**2. Task Selection**
- Prioritize: NYI → In Beta → Implemented (for verification)
- For APL work: follow Phase 3 → 4 → 5 pipeline in project_progress.md
- Focus on one class/spec at a time

**3. Validation Checklist** (before marking "Implemented"):
- [ ] Code compiles without warnings/errors (`cd engine && make -j$(nproc)`)
- [ ] 1-iter sim passes for all affected profiles
- [ ] No regressions in unrelated specs
- [ ] Source data documented in code (Wowhead URLs and dates)
- [ ] `project_progress.md` updated

**4. APL-specific checklist** (before marking an APL change as done):
- [ ] 1-iter sim: PASS
- [ ] All actions appear in sim report (no 0-execute actions without conditions)
- [ ] DPS >= previous baseline on BOTH Patchwerk AND HecticAddCleave
- [ ] No talent build regresses >2%
- [ ] DoT uptime >= 95% for maintained DoTs
- [ ] Resource waste (overcap) < 5% of total generated

**5. GitHub Issues**
- Use for: ambiguous mechanics questions, review requests, blockers
- Tag with: `expansion:midnight`, task type, class/spec, status labels from `ISSUE_TAGS.md`
- Search existing issues before starting to avoid duplicate work
- Post summary after completing: what changed, rows updated, PR/commit links

**6. Error Handling**
- No Wowhead data: mark NYI, note "requires manual testing"
- Unclear mechanics: open GitHub Issue labeled `needs-data`
- Risky changes: separate branch, request testing

---

## Talent Data Extraction

> **MANDATORY:** Any time you need to fetch or verify talent data from Wowhead, use the
> methodology in **`talent_extraction.md`**. The Wowhead talent calculator is a React SPA —
> plain HTTP returns an empty shell. Only Firecrawl (which runs JS) returns talent tree data.

### Quick Reference

| Task | Tool |
|------|------|
| Look up spell IDs for a spec | Read `wowhead/{class}/{spec}/info_base.md` Talent Tree section |
| Get rotation priority | Read `wowhead/{class}/{spec}/extracted/rotation.md` |
| Get talent build export codes | Read `wowhead/{class}/{spec}/extracted/talents.md` |
| Fetch a spec's full talent tree (live) | Firecrawl + `talent_extraction.md` |
| Look up single spell by ID | `web_extract("https://www.wowhead.com/beta/spell=XXXXX")` |
| Re-extract rotation/BiS/consumables | `python3 wowhead/extract_wowhead_tabs.py {class} {spec} --pages rotation` |
| Re-run APL diff | `python3 wowhead/gen_apl_diff.py` |

### Talent Audit Status (2026-03-16)

Full audit completed. Coverage: ~100%. All 33 specs complete.
Full findings: `task_dossiers/talent_audit_wowhead_2026-03-16.md`

**Priority Queue for New Talent Gaps:**
1. Talents with direct numeric DPS effects (damage %, haste %, crit %)
2. Talents gating or modifying core rotational abilities
3. Resource-modifying talents (energy regen, CD reduction on damaging spells)
4. Defensive/utility — register with `// N/A for DPS` comment, no mechanic needed

### Apex Talents

All 33 DPS/tank specs have apex talents fully implemented. IDs and mechanics documented in:
- `task_dossiers/talent_audit_wowhead_2026-03-16.md`
- `project_progress.md` Section 3

---

## Codebase Navigation

**Consult `project_structure.md` before starting any implementation task.** (740 lines)
Maps issue types → source files, explains SimC architecture for Midnight development.

### Key File Locations

| What | Where |
|------|-------|
| APL generators | `engine/class_modules/apl/apl_{class}.cpp` (or `mage.cpp`, `warlock.cpp`) |
| APL generator (druid) | `engine/class_modules/apl/druid/` (`.inc` files) |
| Class modules | `engine/class_modules/sc_{class}.cpp` |
| Midnight gear | `engine/player/unique_gear_midnight.cpp` |
| MID1 profiles | `profiles/MID1/MID1_{Spec}_{HeroTree}.simc` |
| Wowhead info base | `wowhead/{class}/{spec}/info_base.md` |
| Wowhead extracted | `wowhead/{class}/{spec}/extracted/` |
| APL optimization guide | `APL_optimization.md` |
| APL diff report | `wowhead/APL_diff_report.md` |
| Extraction script | `wowhead/extract_wowhead_tabs.py` |
| Diff script | `wowhead/gen_apl_diff.py` |
| Link generator | `wowhead/generate_links.sh` |

---

## Resources

### Project Files (read before starting any task)

| File | Purpose |
|------|---------| 
| `AGENTS.md` | This file — agent workflow, tools, and reference index |
| `project_progress.md` | Master status tracker — all specs, gear, talents, APL pipeline |
| `project_structure.md` | Codebase navigation — maps tasks to source files (740 lines) |
| `APL_optimization.md` | Full APL optimization guide — structure rules, automated loop, composite scoring |
| `talent_extraction.md` | MANDATORY for any talent work — Firecrawl methodology |
| `wowhead/{class}/{spec}/info_base.md` | Pre-fetched spec knowledge base (talent IDs, stat priority) |
| `wowhead/{class}/{spec}/extracted/rotation.md` | Browser-extracted rotation priorities (use this for APL work) |
| `wowhead/{class}/{spec}/extracted/talents.md` | Talent build export codes |
| `wowhead/{class}/{spec}/extracted/bis.md` | BiS gear recommendations |
| `wowhead/{class}/{spec}/extracted/consumables.md` | Enchants, gems, potions, food |
| `wowhead/{class}/{spec}/extracted/tier.md` | Tier set bonus effects |
| `wowhead/APL_diff_report.md` | Phase 2 APL diff — 33 specs, MISSING/ORDER_DIFF/MATCH |
| `TASK_DOSSIER_TEMPLATE.md` | Template for new task dossiers |
| `ISSUE_TAGS.md` | All GitHub issue labels |
| `task_dossiers/talent_audit_wowhead_2026-03-16.md` | Full talent audit results |

### Wowhead URLs

| Resource | URL |
|----------|-----|
| Midnight home | https://www.wowhead.com/midnight |
| Talent calculator | `https://www.wowhead.com/talent-calc/{class}/{spec}/{hero}` |
| Apex Talents guide | https://www.wowhead.com/guide/midnight/apex-talents-overview |
| Spell lookup | `https://www.wowhead.com/spell=SPELL_ID` |
| Beta spell lookup | `https://www.wowhead.com/beta/spell=SPELL_ID` |
| Item lookup | `https://www.wowhead.com/item=ITEM_ID` |
| Rotation guide | `https://www.wowhead.com/guide/classes/{class}/{spec}/rotation-cooldowns-pve-{role}` |
| Talent builds | `https://www.wowhead.com/guide/classes/{class}/{spec}/talent-builds-pve-{role}` |
| BiS gear | `https://www.wowhead.com/guide/classes/{class}/{spec}/bis-gear` |
| Enchants/consumables | `https://www.wowhead.com/guide/classes/{class}/{spec}/enchants-gems-pve-{role}` |
| Tier set bonuses | `https://www.wowhead.com/guide/classes/{class}/{spec}/tier-set-bonuses` |

### Spec URL Role Mapping

- Tank specs (use `role=tank`): blood, vengeance, guardian, brewmaster, protection
- All others: use `role=dps`

---

## Notes

- **Code Formatting**: All C++ must conform to `.clang-format` (Google-based). Run `clang-format -i` before committing.
- Maintain backward compatibility where possible
- Use meaningful variable names and add comments for complex logic
- Wowhead as of 2026-03-22 is the reference; note if newer data differs
- The `extracted/` data is the authoritative source for rotation priorities — always prefer it over `info_base.md` for APL work

---

*This file guides autonomous agents working on the Midnight expansion update for SimulationCraft. Always check `project_progress.md` before starting work and update it after completing tasks.*

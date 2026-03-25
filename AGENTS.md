# AGENTS.md — SimulationCraft Midnight Agent Guide

**Last Updated: 2026-03-25**

This document is the operating manual for AI agents working on the SimulationCraft
Midnight expansion. It covers project context, tools, data sources, workflows,
and a complete file index. Read this first in every session.

---

## 1. Project Overview

**SimulationCraft** is an open-source WoW combat simulator. We are updating it for
the **Midnight** expansion — new talents, spells, gear, tier sets, and APLs for all
33 DPS/tank specs.

**Current state (2026-03-25):** ~85% to first stable release.
- 56/56 profiles compile and sim
- 4,410 spells, 0 genuine gaps
- 33/33 tier sets and apex talents implemented
- 112/112 Phase 4 baselines (Patchwerk + HecticAddCleave)
- 4/4 C++ APL generator syncs done
- Remaining: 4 .simc APL imports, Guardian Druid profile fix, optimization loop

**Primary status file:** `project_progress.md` — always read it at session start.
**Release gap analysis:** `RELEASE_GAPS.md` — prioritized list of remaining work.

---

## 2. File Index — What Lives Where

### Core Documentation (project root)

| File | Purpose | When to Read |
|------|---------|--------------|
| `AGENTS.md` | This file — agent workflow and reference index | Every session start |
| `project_progress.md` | Master status tracker — profiles, mechanics, APL, pipeline | Every session start |
| `RELEASE_GAPS.md` | Prioritized gap analysis for first stable release | When planning work |
| `NEXT_STEPS.md` | Prioritized TODO with specific fix descriptions | When picking next task |
| `APL_optimization.md` | Full APL guide — structure rules, optimization loop, sim commands | When doing APL work |
| `project_structure.md` | Codebase navigation — maps task types to source files (740 lines) | When touching code |
| `audit_notes.md` | 42-issue audit findings by severity | When investigating spec issues |
| `audit_task_list.md` | 10 batches of fixes from the audit | When checking what's been done |
| `full_spec_audit_2026-03-24.md` | Complete per-class audit reports (5000+ lines) | Deep-dive into specific spec |
| `spell_database_task.md` | Spell database methodology | If spell DB needs updating |

### Wowhead Data (the canonical source for all game data)

```
wowhead/
  extract_wowhead_tabs.py    — browser extractor (Playwright/Chromium)
  gen_apl_diff.py            — APL diff: Wowhead rotation vs SimC APL
  generate_links.sh          — generates info_links.md per spec
  APL_diff_report.md         — Phase 2 diff results for all 33 specs
  {class}/{spec}/
    extracted/               — ★ CANONICAL DATA — browser-extracted from Wowhead
      rotation.md / .json    — rotation priorities (all hero talents × all tabs)
      talents.md / .json     — talent builds with export codes
      bis.md / .json         — BiS gear by slot
      consumables.md / .json — enchants, gems, potions, food, flasks
      tier.md / .json        — tier set bonus effects (2pc + 4pc)
    info_links.md            — Wowhead URLs for this spec
    info_base.md             — ⚠️ DEPRECATED (2026-03-17, misses JS content)
```

**Rule:** Always use `extracted/` files. Never use `info_base.md` for decisions.

### Source Code

| What | Where |
|------|-------|
| Class modules | `engine/class_modules/sc_{class}.cpp` |
| APL generators (C++) | `engine/class_modules/apl/apl_{class}.cpp` |
| APL generators (warlock/mage) | `engine/class_modules/apl/warlock.cpp`, `mage.cpp` |
| APL generators (druid) | `engine/class_modules/apl/druid/*.inc` |
| APL overrides (.simc) | `ActionPriorityLists/default/{spec}.simc` |
| APL upstream reference | `ActionPriorityLists/cloned_default/{spec}.simc` |
| Enhancement shaman APL | `engine/class_modules/apl/shaman/enhancement.simc` |
| Midnight gear/trinkets | `engine/player/unique_gear_midnight.cpp` |
| Core action engine | `engine/action/action.cpp`, `engine/action/dot.cpp` |
| Player scheduling | `engine/player/player.cpp` |

### Profiles and Results

| What | Where |
|------|-------|
| MID1 profiles (56 total) | `profiles/MID1/MID1_{Class}_{Spec}[_{Variant}].simc` |
| Phase 4 baselines (112 JSONs) | `results/phase4/MID1_{name}_{patchwerk|hecticaddcleave}.json` |
| APL comparison results | `results/apl_compare/`, `results/apl_compare_all/` |
| Sim scripts | `scripts/run_apl_compare.py`, `scripts/run_apl_compare_all.py` |
| Spell database | `spell_database.db` (SQLite), reports in `spell_database_reports/` |

### Build

| What | Where |
|------|-------|
| Binary (built) | `engine/simc` (or `build/simc` after cmake build) |
| CMake build | `cmake -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON && cmake --build build -j$(nproc)` |
| Copy to engine | `cp build/simc engine/simc` |

---

## 3. Agent Workflow

### Session Start
1. Read `AGENTS.md` (this file)
2. Read `project_progress.md` for current status
3. Read `NEXT_STEPS.md` or `RELEASE_GAPS.md` to pick work
4. For spec-specific work: read `wowhead/{class}/{spec}/extracted/rotation.md`

### Before Editing Code
1. Read `project_structure.md` to find the right file
2. For APL work: read `APL_optimization.md` for rules and conventions
3. Check `audit_task_list.md` to see if the issue was already addressed

### After Completing Work
1. Verify: `./engine/simc profiles/MID1/{profile}.simc iterations=1 output=/dev/null`
2. Update `project_progress.md` with what changed
3. Commit with descriptive message: `Fix(apl): {spec} — {what changed}`

### Validation Checklist
- [ ] Code compiles: `cmake --build build -j$(nproc)`
- [ ] 1-iter smoke test passes for affected profiles
- [ ] No regressions in unrelated specs
- [ ] Source data documented (Wowhead URLs/dates in comments)
- [ ] `project_progress.md` updated

### APL-Specific Checklist
- [ ] All actions appear in sim report (no 0-execute without conditions)
- [ ] DPS >= baseline on BOTH Patchwerk AND HecticAddCleave
- [ ] No talent build regresses >2%
- [ ] DoT uptime >= 95% for maintained DoTs
- [ ] Resource waste (overcap) < 5%

---

## 4. Sim Commands Reference

```bash
# Build
cmake -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON
cmake --build build -j$(nproc)
cp build/simc engine/simc

# Smoke test (1 iteration)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=1 output=/dev/null

# Baseline sim (Patchwerk, target_error convergence)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc \
  fight_style=Patchwerk target_error=0.1 threads=16 \
  json2=results/phase4/MID1_Warrior_Fury_patchwerk.json output=/dev/null

# Baseline sim (HecticAddCleave)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc \
  fight_style=HecticAddCleave target_error=0.1 threads=16 \
  json2=results/phase4/MID1_Warrior_Fury_hecticaddcleave.json output=/dev/null

# APL comparison (all specs)
python3 scripts/run_apl_compare_all.py

# APL diff vs Wowhead
python3 wowhead/gen_apl_diff.py

# Re-extract Wowhead data for one spec
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation
```

**Sim parameters (Phase 4 baselines):**
- `target_error=0.1` (adaptive iterations, typically 8k-15k)
- `max_time=300` (5 minutes), `vary_combat_length=0.2`
- `threads=16-32` (use nproc)
- Composite DPS = 0.50 × Patchwerk + 0.50 × HecticAddCleave

---

## 5. Data Source Hierarchy

| Priority | Source | Use For |
|----------|--------|---------|
| 1 | `wowhead/{class}/{spec}/extracted/` | All game data: rotations, talents, gear, tier, consumables |
| 2 | Wowhead live (via browser) | When extracted data is stale or missing |
| 3 | DBC spell data (in-engine) | Spell coefficients, scaling, proc rates |
| 4 | `info_base.md` | Last resort for spell ID lookups only |

**Wowhead is the canonical ground truth.** Always verify against it.
The `extracted/` data is from 2026-03-22. Re-extract if a spell was patched after that date.

---

## 6. Key Architecture Notes

### APL Generation: Two Paths
1. **C++ generators** (`apl_{class}.cpp`): Compile into the engine binary. Used when no .simc override exists.
2. **.simc overrides** (`ActionPriorityLists/default/`): Loaded at runtime, override C++ APL. Used when we need faster iteration than recompiling.
3. **Profile inline APL**: `actions=` lines in profile .simc files override everything. Should be avoided (Guardian Druid stub is a known bug).

### Empowered Charges (DK Blood, Evoker)
- Channeled spells with a release spell on completion
- `last_tick()` schedules `release_spell->schedule_execute()`
- Hack: `d->current_action = release_spell` prevents double schedule_ready
- Bug fixed 2026-03-25: `player_t::interrupt()` now checks `!executing` before calling `schedule_ready()` — prevents crash when movement interrupts an empowered charge

### Fight Styles
- **Patchwerk**: Pure single-target, 300s, no movement
- **HecticAddCleave**: Adds spawn periodically (5 adds, ~5% uptime), movement events. Simulates M+/raid with adds.

---

## 7. Wowhead Extraction Tool

`wowhead/extract_wowhead_tabs.py` — browser-based extractor using Playwright/Chromium.

**Why:** Wowhead uses React/JS for rotation priorities, talent builds, and gear.
Plain HTTP returns empty shells. Only a real browser can click tabs and capture content.

**Design:** Discovery-based — doesn't hardcode tab names. Discovers `[role="tab"]` groups,
hero switches, and talent toggles. Clicks every combination. Handles Wowhead quirks
(data-active deselection, DOM re-renders, duplicate text artifacts).

```bash
# Install
pip install playwright && playwright install chromium

# Usage
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation
python3 wowhead/extract_wowhead_tabs.py --all --pages rotation,talents,bis,consumables,tier
```

---

## 8. Wowhead URLs

| Resource | URL Pattern |
|----------|-------------|
| Midnight home | `https://www.wowhead.com/midnight` |
| Rotation guide | `https://www.wowhead.com/guide/classes/{class}/{spec}/rotation-cooldowns-pve-{role}` |
| Talent builds | `https://www.wowhead.com/guide/classes/{class}/{spec}/talent-builds-pve-{role}` |
| BiS gear | `https://www.wowhead.com/guide/classes/{class}/{spec}/bis-gear` |
| Tier set bonuses | `https://www.wowhead.com/guide/classes/{class}/{spec}/tier-set-bonuses` |
| Consumables | `https://www.wowhead.com/guide/classes/{class}/{spec}/enchants-gems-pve-{role}` |
| Spell lookup | `https://www.wowhead.com/spell={ID}` |
| Item lookup | `https://www.wowhead.com/item={ID}` |

Tank specs use `role=tank`: blood, vengeance, guardian, brewmaster, protection.
All others use `role=dps`.

---

*Read `project_progress.md` next. It has the complete status of every spec, every phase,
and every known issue. Update it after completing any work.*

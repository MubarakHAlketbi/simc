# AGENTS.md — SimulationCraft Midnight Agent Guide

**Last Updated: 2026-03-25**

Read this file first every session. Then read `project_progress.md` — it is the
single source of truth for all project status, known issues, and what to do next.

---

## Project

SimulationCraft fork for WoW Midnight expansion. 33 DPS/tank specs, 56 profiles,
112 baselines. See `project_progress.md` for complete status.

## File Map

### Documentation (root)
| File | What It Is |
|------|------------|
| `project_progress.md` | **THE master doc** — status, issues, next steps, all data |
| `APL_optimization.md` | APL technical reference — structure rules, optimization loop (1197 lines) |
| `project_structure.md` | Codebase navigation — maps task types to source files (740 lines) |
| `full_spec_audit_2026-03-24.md` | Raw per-class audit data (5136 lines, reference only) |

### Wowhead Data (canonical game data source)
| Path | What |
|------|------|
| `wowhead/{class}/{spec}/extracted/rotation.md` | Rotation priorities (all hero talents × tabs) |
| `wowhead/{class}/{spec}/extracted/talents.md` | Talent builds with export codes |
| `wowhead/{class}/{spec}/extracted/bis.md` | BiS gear by slot |
| `wowhead/{class}/{spec}/extracted/tier.md` | Tier set bonus effects |
| `wowhead/{class}/{spec}/extracted/consumables.md` | Enchants, gems, potions, food |
| `wowhead/APL_diff_report.md` | APL diff results (Wowhead vs SimC, 33 specs) |
| `wowhead/extract_wowhead_tabs.py` | Browser extractor (Playwright/Chromium) |
| `wowhead/gen_apl_diff.py` | APL diff generator script |

**Rule:** Always use `extracted/` files. `info_base.md` is deprecated (misses JS content).

### Source Code
| What | Where |
|------|-------|
| Class modules | `engine/class_modules/sc_{class}.cpp` |
| APL generators | `engine/class_modules/apl/apl_{class}.cpp` |
| APL overrides (.simc) | `ActionPriorityLists/default/` |
| Upstream APL reference | `ActionPriorityLists/cloned_default/` |
| Midnight gear/trinkets | `engine/player/unique_gear_midnight.cpp` |
| MID1 profiles | `profiles/MID1/MID1_{Class}_{Spec}[_{Variant}].simc` |
| Phase 4 baselines | `results/phase4/*.json` (112 files) |

### Build
```bash
cmake -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON
cmake --build build -j$(nproc)
cp build/simc engine/simc
```

## Workflow

1. **Start:** Read this file → read `project_progress.md` "What's Next"
2. **Before code:** Read `project_structure.md` for file locations. For APL work, read `APL_optimization.md`.
3. **For spec work:** Read `wowhead/{class}/{spec}/extracted/rotation.md`
4. **After work:** Verify with `./engine/simc profiles/MID1/{profile}.simc iterations=1 output=/dev/null`
5. **Update** `project_progress.md` with what changed. Commit.

## Sim Commands

```bash
# Smoke test
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=1 output=/dev/null

# Baseline (Patchwerk)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc fight_style=Patchwerk \
  target_error=0.1 threads=16 json2=results/phase4/MID1_Warrior_Fury_patchwerk.json output=/dev/null

# Baseline (HecticAddCleave)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc fight_style=HecticAddCleave \
  target_error=0.1 threads=16 json2=results/phase4/MID1_Warrior_Fury_hecticaddcleave.json output=/dev/null

# APL diff vs Wowhead
python3 wowhead/gen_apl_diff.py

# Re-extract Wowhead data
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation
```

Composite DPS = 0.50 × Patchwerk + 0.50 × HecticAddCleave.

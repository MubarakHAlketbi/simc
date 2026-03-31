# Fork vs Upstream Review — SimulationCraft Midnight

**Date**: 2026-03-29  
**Fork**: `MubarakHAlketbi/simc` (branch: `midnight`)  
**Upstream**: `simulationcraft/simc` (branch: `midnight`)  
**Common Ancestor**: `1fb4963` — March 15, 2026 (`[Resto] Midnight APL first pass`)

---

## Executive Summary

The fork and upstream have significantly diverged since March 15. The divergence is **architectural and philosophical**, not just incremental:

- **Fork ahead by**: 331 unique commits, ~379 new data files, ~178,537 lines added
- **Upstream ahead by**: 181 commits of class fixes, bug fixes, and build updates (Build 66709)
- **No C++ engine code modifications** in the fork — all changes are data, tooling, documentation, and configuration
- **785 files changed** in both directions (symmetrical diff)

---

## 1. Quantitative Summary

| Metric | Fork | Upstream | Delta |
|--------|------|----------|-------|
| Unique commits (ahead) | 331 | — | +331 |
| Unique commits (behind) | — | 181 | -181 |
| C++ source files changed | 0 | ~60 | -60 |
| New data files (wowhead/) | ~379 | 0 | +379 |
| Total file changes | 785 | 785 | symmetrical |
| Lines added | ~178,537 | ~37,578 | +140,959 |
| Lines deleted | ~37,578 | ~178,537 | -140,959 |

---

## 2. What the Fork Added (Unique Contributions)

### A. Canonical Data Source — Wowhead Extracted Data

Complete browser-extracted dataset for all 33 specs under `wowhead/{class}/{spec}/extracted/`:

| File | Content |
|------|---------|
| `rotation.md/json` | Priority lists from Wowhead (all hero talent variants × tabs) |
| `talents.md/json` | Talent builds with export codes |
| `bis.md/json` | BiS gear by slot |
| `tier.md/json` | Tier set bonus effects |
| `consumables.md/json` | Enchants, gems, potions, food |
| `info_links.md` | Source URLs |

- **Total**: 379 files (JSON + Markdown)
- **Purpose**: Ground-truth data source for Midnight expansion (Build 12.0.1.66384)
- **Tooling**: `wowhead/extract_wowhead_tabs.py` (Playwright/Chromium browser automation)
- **Rule**: `extracted/` files are canonical; `info_base.md` is deprecated (misses JS-rendered content)

### B. Optimization Toolchain (~4,000 lines across 16 scripts)

#### Talent System (39 commits)

| Script | Purpose |
|--------|---------|
| `scripts/lib/talent_tree.py` | DBC talent tree parser + real TraitEdge.csv prerequisite edges |
| `scripts/lib/talent_codec.py` | Decode/encode base64 talent strings |
| `scripts/lib/tree_codec_bridge.py` | Bridge — connects tree + codec, high-level API |
| `scripts/lib/talent_validator.py` | Build validation (budget, prereqs, gates) + neighbor generation |
| `scripts/talent_local_search.py` | Hill-climbing optimizer with validated neighbors |
| `scripts/validate_all_profiles.py` | Validates all 56 profiles against tree constraints |

Key results:
- Real DB2 prerequisite edges from TraitEdge.csv (6,409 Type 2 edges)
- Heuristic accuracy vs real edges: 77.7% precision, 90.1% recall
- Warrior Fury talent optimization: **+3.31% DPS** (Patchwerk)
- All 56 profiles validated: 34/34/15 budget, real prerequisite edges, SimC smoke test PASS

#### APL Optimization (41 commits)

| Script | Purpose |
|--------|---------|
| `scripts/apl_optimizer.py` | Mutation operators + multi-stage evaluation |
| `scripts/lib/apl_parser.py` | .simc ↔ structured data serialization |
| `scripts/lib/apl_mutations.py` | 4 mutation operators (swap, sweep, promote, route) |
| `scripts/lib/sim_runner.py` | Parallel SimC runner, JSON parse, composite scoring |
| `scripts/optimize_all.py` | Master orchestrator |

Key results:
- Warrior Fury HecticAddCleave: **+0.44%** (rampage threshold 100→80 in thane_aoe)
- Warrior Fury Patchwerk: +0.00% (already optimal)
- Lesson learned: For well-tuned specs, DPS gains come from **talent optimization** (+3–6%), not APL changes

### C. Infrastructure & CI/CD Modernization (6 commits)

| Workflow | Status | Lines |
|----------|--------|-------|
| `build.yml` | Rewritten — profile-based testing, ccache, gcc-14 | 373 |
| `spec_test.yml` | New — standalone, 34-spec matrix | 400 |
| `main.yml` | Rewritten — combined build + ASan + spec-test | 196 |
| `generate_files.yml` | Removed (upstream's) | -74 |
| `ubuntu_test.yml` | Removed (upstream's) | -57 |
| `midnight-update.yml` | New issue template | +95 |

**Reason for rewrite**: Upstream's reusable `workflow_call` chain caused 0s parse failures on the fork. All workflows are now self-contained with ccache.

### D. Documentation (49 commits)

| File | Lines | Content |
|------|-------|---------|
| `AGENTS.md` | 309 | Master guide for autonomous agent development |
| `project_progress.md` | 163 | Single source of truth (rewritten from 655 lines) |
| `APL_optimization.md` | 310 | Technical reference — APL syntax, expressions, rules |
| `OPTIMIZATION_HOWTO.md` | — | Step-by-step manual optimization guide |
| `project_structure.md` | — | Codebase navigation map |
| `docs/archive/full_spec_audit_2026-03-24.md` | 5,136 | Raw per-class audit data |
| `docs/archive/APL_diff_report.md` | — | APL diff results |
| `docs/internal/darkmoon_investigation.md` | — | Darkmoon trinket investigation (Issue #81) |

### E. Profile & APL Work (42 commits)

| Batch | Description | Status |
|-------|-------------|--------|
| 1 | Fresh baselines — 112 JSONs (56 PW + 56 HAC) | DONE |
| 2 | APL diff re-run + triage | DONE — 0 real gaps |
| 3 | APL optimization — warrior_fury tested | PW +0.00%, HAC +0.44% |
| 4 | Talent local search — warrior_fury tested | PW +3.31% |
| 5–7 | Re-baseline, trinket combos, final docs | PENDING |

- **Reference APLs**: `ActionPriorityLists/cloned_default/` — complete set of 33 upstream reference APLs for 3-way comparison
- **Default APL modifications**: 20 specs updated based on optimization and audit findings

### F. Bug Fixes (60 commits)

- Guardian Druid profile fixed (commit `6534f10`): removed `assisted_combat` stub, fixed 5 APL `.inc` errors (`ravage→maul`, `thrash_bear→thrash`, `berserk_bear→berserk`, moonfire precombat, invalid variables). DPS **3k→10.6k**
- Warlock APL `drain_life` ordering corrected
- Talent neighbor generator strict point budget enforcement
- Hero tree variant filtering fix (includes internal nodes regardless of `id_spec`)
- All 42 audit issues resolved (6 CRITICAL, 11 HIGH, 18 MEDIUM, 7 LOW)

---

## 3. What Upstream Has That the Fork Is Missing (181 commits)

### A. Game Data Updates

| Commit | Description |
|--------|-------------|
| `83580bc` | `[live] Game data update (Build 66709) (#11300)` |
| `7bf25b1` | `[live] Game data update (Build 66709) (#11299)` |
| `1a604ec` | `[DBC] update for 12.0.5.66529` |

Multiple DBC updates: spell data hotfixes, ItemExtendedCost format fixes, field signedness corrections.

### B. Class-Specific Fixes

#### Balance Druid (4 commits)
- `2137add` — Star cascade procs on impact and doesn't proc off procs
- `6573452` — Star cascade triggers Harmony of the Heavens
- `f126471` — MID1 4pc procs on Surge impact & Starfall aura
- `071e7b7` — Star cascade can proc Hail of Stars
- `90299f5` — Add uptimes for Atmospheric Exposure & Stellar Amplification

#### Paladin (5 commits)
- `6cb6ed9` — Prevent segfault when target list is shorter than `n_targets()`
- `7c107ed` — Prevent segfault when target list is empty
- `cd7cd74` — Apply UR-Judgment via `target_list`
- `82b41c7` — Add a 300ms delay to Glory of the Vanguard
- `c8e2fd7` — Recalculate `target_da_mul` and `result_amount` before Hammer of Light

#### Devourer
- `b2e7ff7` — Void Ray soul gen does not scale with targets

#### Monk
- `a3f6bcc` — Convert Empowered Tiger Lightning to an assessor to avoid event manager stuck condition (#11303)

#### Enhancement Shaman
- `3eac49e` — Implement Enhancement 12.0 4PC mastery bug (halves the value)

#### Assassination Rogue
- `a608ce5` — Improved Garrote snapshotting (#11301)

#### Priest
- `434b787` — Add Shadow Word: Death to rotation in execute

#### Evoker
- `9bec245` — Fix default consumable
- `61e2383` — Add `evoker.patchwerk_in_dungeon`

#### Guardian Druid
- `b212050` — Profile for Midnight tier 1 (#11264)

#### Mage
- `bda2438` — PTR Pulse update
- `9bf981e` — Updated consumables (#11302)

#### Elemental Shaman
- `eed13c1` — Final fix for pf (#11295)

### C. Code Quality & Build Improvements

- `330f000` — Create nix flake for compiling and developing (#11231)
- `114e995` — Remove unnecessary `player_t*` argument from `buff_t::extend_duration`
- `eec0732` — Fix fallback buffs being used to decorate some HTML items

### D. Profile Generation System

Multiple "Update Generated Files" commits — automated profile generation from canonical C++ APL sources. Affected specs include all classes with recent APL changes.

---

## 4. Architectural Differences

| Dimension | Fork | Upstream |
|-----------|------|----------|
| **Data Source** | Wowhead browser extraction (JS tab content) | DBC/casc extraction + C++ code generation |
| **Data Storage** | Markdown + JSON files (human-readable) | Generated C++ code + binary DBC data |
| **Game Build** | 12.0.1.66384 | 12.0.5.66709 |
| **APL Strategy** | Upstream reference + local optimization tooling | C++ generated defaults + occasional .simc overrides |
| **Profile Format** | MID1 profiles (56) + baselines (112 JSONs) | Auto-generated profiles via `generate_profiles.sh` |
| **Validation** | Explicit talent validator with real DB2 edges | Implicit through compilation |
| **CI/CD** | Custom flat workflows (profile-based testing) | Reusable workflow chain |
| **Documentation** | Extensive (AGENTS.md, progress tracking, optimization guides) | Minimal (CONTRIBUTING.md only) |

---

## 5. File-Level Differences

### ActionPriorityLists/

| Path | Fork Status | Upstream Status |
|------|-------------|-----------------|
| `cloned_default/*.simc` (33 files) | **ADDED** — reference APLs for comparison | Not present |
| `default/deathknight_blood.simc` | Modified | Modified (different changes) |
| `default/deathknight_frost.simc` | Modified | Modified |
| `default/deathknight_unholy.simc` | Modified | Modified |
| `default/druid_balance.simc` | Modified | Modified |
| `default/druid_feral.simc` | Modified | Modified |
| `default/druid_guardian.simc` | Modified | Modified |
| `default/druid_restoration.simc` | Modified | Modified |
| `default/evoker_augmentation.simc` | Modified | Modified |
| `default/evoker_devastation.simc` | Modified | Modified |
| `default/hunter_beast_mastery.simc` | Modified | Modified |
| `default/hunter_marksmanship.simc` | Modified | Modified |
| `default/hunter_survival.simc` | Modified | Modified |
| `default/mage_arcane.simc` | Modified | Modified |
| `default/mage_fire.simc` | Modified | Modified |
| `default/mage_frost.simc` | Modified | Modified |
| `default/monk_windwalker.simc` | Modified | Modified |
| `default/paladin_retribution.simc` | Modified | Modified |
| `default/priest_shadow.simc` | Modified | Modified |
| `default/rogue_assassination.simc` | Modified | Modified |
| `default/warlock_affliction.simc` | Modified | Modified |

### Wowhead Data (fork-only)

| Path | Files |
|------|-------|
| `wowhead/{class}/{spec}/extracted/` | ~330 data files (all 33 specs × ~10 files each) |
| `wowhead/{class}/{spec}/info_links.md` | 33 link files |
| `wowhead/extract_wowhead_tabs.py` | Browser extraction script |
| `wowhead/gen_apl_diff.py` | APL diff generator |
| `wowhead/update_talents_from_extracted.py` | Talent updater |
| `wowhead/audit_report.json` | Audit results |
| `wowhead/name_audit_report.json` | Name audit results |

### Scripts (fork-only)

| Path | Purpose |
|------|---------|
| `scripts/optimize_all.py` | Master orchestrator |
| `scripts/apl_optimizer.py` | APL optimization loop |
| `scripts/talent_build_compare.py` | Wowhead talent build comparison |
| `scripts/talent_local_search.py` | Hill-climbing talent optimizer |
| `scripts/validate_all_profiles.py` | Profile validation |
| `scripts/lib/sim_runner.py` | SimC runner |
| `scripts/lib/apl_parser.py` | APL parser/serializer |
| `scripts/lib/apl_mutations.py` | Mutation operators |
| `scripts/lib/talent_tree.py` | DBC talent tree parser |
| `scripts/lib/talent_codec.py` | Talent string codec |
| `scripts/lib/tree_codec_bridge.py` | Tree + codec bridge |
| `scripts/lib/talent_validator.py` | Build validation + neighbor generation |

### Documentation (fork-only)

| Path | Lines |
|------|-------|
| `AGENTS.md` | 309 |
| `project_progress.md` | 163 |
| `APL_optimization.md` | 310 |
| `OPTIMIZATION_HOWTO.md` | — |
| `project_structure.md` | — |
| `docs/archive/full_spec_audit_2026-03-24.md` | 5,136 |
| `docs/archive/APL_diff_report.md` | — |
| `docs/internal/darkmoon_investigation.md` | — |

### CI/CD Differences

| Workflow | Fork | Upstream |
|----------|------|----------|
| `.github/workflows/build.yml` | 373 lines (rewritten, ccache, gcc-14) | Different structure |
| `.github/workflows/spec_test.yml` | 400 lines (standalone 34-spec matrix) | Not present |
| `.github/workflows/main.yml` | 196 lines (combined) | Different structure |
| `.github/workflows/generate_files.yml` | Removed | Present (74 lines) |
| `.github/workflows/ubuntu_test.yml` | Removed | Present (57 lines) |
| `.github/ISSUE_TEMPLATE/midnight-update.yml` | Added (95 lines) | Not present |
| `.gitignore` | Modified (+39 lines) | Original |

---

## 6. Risks

### High Priority

1. **Build Divergence** — Fork is on Build 12.0.1.66384, upstream is on 66709 (12.0.5). This means:
   - Missing ~2 months of balance changes, new spells, changed mechanics
   - Simulation results may be invalid for current Midnight beta
   - Class fixes upstream (Balance star cascade, Paladin judgment scaling, etc.) are not present

2. **Missing Upstream Fixes** — At least 181 commits including:
   - Critical segfault fixes (Paladin target list handling)
   - Scaling corrections (Devourer Void Ray)
   - Event manager stuck condition fix (Monk Empowered Tiger Lightning)
   - Tier set implementation updates (Enhancement 4PC mastery bug)

3. **APL Staleness** — 20 default APLs modified in the fork, but upstream has also modified many of the same files. The fork's optimizations may be based on stale spell data.

### Medium Priority

4. **No C++ Code Changes** — While this avoids merge conflicts, it also means upstream's engine-level bug fixes (buff API changes, assessor refactors) are absent.

5. **Wowhead Data Freshness** — Extracted data is from a specific point in time and may not reflect latest Beta balance changes.

6. **ActionPriorityList Conflicts** — Both fork and upstream modified the same 20+ default APL files. Merging will require per-file reconciliation.

---

## 7. Recommendations

### Immediate (Before Next Optimization Cycle)

1. **Rebase onto latest upstream** (Critical):
   ```bash
   cd ~/simc
   git checkout midnight
   git fetch upstream midnight
   git rebase upstream/midnight
   ```
   - Brings in Build 66709 game data + all 181 upstream commits
   - Expect conflicts in `ActionPriorityLists/default/` (both sides modified)
   - Strategy: Keep fork's `wowhead/`, `scripts/`, `docs/` (upstream doesn't have them); merge upstream APL changes carefully

2. **Update Wowhead data** — Re-run `extract_wowhead_tabs.py` to capture Build 66709 changes

3. **Re-run 3-way APL comparison** — At 10k iterations, compare upstream vs fork vs C++ default for all 33 specs

4. **Re-validate all profiles** — Run `validate_all_profiles.py` + 1-iteration smoke test for all 56 profiles after rebase

### Strategic

5. **Document merge strategy** — Add rebase procedure and conflict resolution steps to `OPTIMIZATION_HOWTO.md`

6. **Set up upstream monitoring** — Weekly check for new upstream commits to avoid massive rebases

7. **Consider contributing back**:
   - Talent validator with real TraitEdge.csv edges
   - APL optimization results
   - Guardian Druid profile fix
   - Would reduce divergence and benefit the upstream community

---

## 8. Top 10 Baseline Results (for reference)

### Patchwerk

| Profile | DPS |
|---------|----:|
| Rogue Subtlety | 124,620 |
| Shaman Elemental | 116,547 |
| Evoker Devastation | 115,502 |
| Evoker Devastation FS | 115,386 |

### Optimization Results (Warrior Fury)

| Method | Patchwerk | HecticAddCleave |
|--------|-----------|-----------------|
| APL Optimization | +0.00% | +0.44% |
| Talent Local Search | +3.31% | pending |
| Manual APL Reordering | -1.52% (regressed) | -0.86% (regressed) |

**Key lesson**: For well-tuned specs, DPS gains come from talent optimization (+3–6%), not APL changes. Manual intuition-based APL reordering regresses DPS.

---

*Generated 2026-03-29 from analysis of both repositories.*

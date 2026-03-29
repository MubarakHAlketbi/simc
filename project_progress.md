# SimulationCraft — Midnight Expansion (MID1) Progress

Last updated: 2026-03-28

## Status

| Metric | Value |
|--------|-------|
| Profiles | 56/56 PASS (compile + 1-iter sim) |
| Baselines | 112/112 FRESH (2026-03-28, target_error=0.1) |
| Spells | 4,410 scraped, 0 genuine DPS gaps |
| Tier sets | 33/33 implemented |
| Apex talents | 33/33 implemented (3 spell IDs each) |
| APL audit | 35/42 resolved (batch 9 deferred — tier DBC verification) |
| APL diff (Phase 4b+4c) | 0 real gaps (58 false positives triaged) |
| Talent builds | 29/33 profiles updated from Wowhead comparison |
| Optimization tooling | ALL BUILT — 14 scripts, ~3,500 lines |
| Engine bugs | All resolved |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |

## What's Next

**Design:** Each spec produces TWO independent optimal builds — one for Patchwerk (ST raid), one for HecticAddCleave (M+/AoE). Full task list: `task_list.md`

| Batch | Description | Status |
|-------|-------------|--------|
| 1 | Fresh baselines (56 PW + 56 HAC) | ✅ DONE |
| 2 | APL diff re-run + triage | ✅ DONE — 0 real gaps |
| 3 | APL optimization — warrior_fury tested | ✅ PW +0.00%, HAC +0.44% — full 33-spec run PENDING |
| 4 | Talent local search — warrior_fury tested | ✅ PW +1.52%, HAC +0.65% — full 33-spec run PENDING |
| 5 | Re-baseline + cross-validation | PENDING |
| 6 | Trinket combinatorics (Phase 5) | PENDING |
| 7 | Tier set DBC verification + final docs | PENDING |

---

## Warrior Fury Test Results (2026-03-28)

First spec fully optimized (talent + APL) with the new pipeline:

### Talent Local Search

| Style | Baseline | Optimized | Gain | Best Seed | Key Swap |
|-------|----------|-----------|------|-----------|----------|
| Patchwerk | 86,904 | 88,178 | +1.52% | Mountain Thane #3 | → Stance Mastery |
| HecticAddCleave | 209,221 | 210,582 | +0.65% | Mountain Thane #6 | → Stance Mastery, Fast Footwork |

Builds differ between PW and HAC (8 PW-only nodes, 5 HAC-only nodes). Key finding: Stance Mastery universally undervalued by Wowhead. Convergence in 1-2 hill-climb passes — this is the ceiling for single-node mutations.

### APL Optimization

| Style | Result |
|-------|--------|
| Patchwerk | +0.00% — already optimal (converged immediately) |
| HecticAddCleave | +0.44% — rampage threshold 100→80 in thane_aoe |

Manual APL changes tested (execute repositioning, rend/wrecking_throw additions) — all regressed (-1.52% PW, -0.86% HAC). Existing profile APL is battle-tested from upstream import.

---

## Baselines (2026-03-28)

### Top 10 Patchwerk

| Profile | DPS |
|---------|----:|
| Rogue Subtlety | 124,620 |
| Shaman Elemental | 116,547 |
| Evoker Devastation | 115,502 |
| Evoker Devastation FS | 115,386 |
| Mage Frost Frostfire | 113,229 |
| Monk WW Conduit | 112,753 |
| Monk Windwalker | 110,350 |
| DK Unholy San'layn | 110,059 |
| DH Devourer | 108,891 |
| DH Devourer Void-Scarred | 107,059 |

### Top 10 HecticAddCleave

| Profile | DPS |
|---------|----:|
| Warlock Demonology | 472,187 |
| Warlock Demo SH | 470,024 |
| Rogue Subtlety | 290,018 |
| Monk Windwalker | 231,023 |
| Warrior Arms | 229,257 |
| DK Unholy | 228,679 |
| Mage Arcane | 227,071 |
| Mage Fire | 225,852 |
| Mage Fire Frostfire | 225,551 |
| Monk WW Conduit | 215,848 |

Full report: `python3 scripts/optimize_all.py --report`

---

## Pipeline Phases

| Phase | Status |
|-------|--------|
| 1. Wowhead extraction (33 specs × 5 pages) | ✅ DONE |
| 2. APL diff vs Wowhead | ✅ DONE |
| 3. Profile updates (gear, consumables, talents) | ✅ DONE |
| 3.5. Extractor pipeline fixes + visual audit | ✅ DONE |
| 3.6. 3-way upstream APL comparison (198 sims, 10k iter) | ✅ DONE |
| 4-pre. Fix 8 APL issues from comparison | ✅ DONE |
| 4a. Complete all 112 baselines | ✅ DONE |
| 4b. Re-run APL diff with fixed pipeline | ✅ DONE — 0 real gaps |
| 4c. Triage all MISSING items | ✅ DONE — 58 false positives |
| 4d-talent. Wowhead build comparison (262 builds) | ✅ DONE — 29/33 improved |
| 4d-apl. APL optimization (per fight style) | TESTED on Fury — full run pending |
| 4d-talent2. Talent local search (seed + hill-climb) | TESTED on Fury — full run pending |
| 5. Trinket combinatorics | NOT STARTED |

---

## Optimization Tooling

14 scripts, ~3,500 lines — all implemented and tested:

| Script | Purpose | Status |
|--------|---------|--------|
| `scripts/lib/sim_runner.py` | SimC runner, JSON parse, per-fight-style scoring | DONE (307 lines) |
| `scripts/lib/apl_parser.py` | Parse/serialize .simc APL | DONE (278 lines) |
| `scripts/lib/apl_mutations.py` | Mutation operators: swap, sweep, route | DONE (262 lines) |
| `scripts/lib/talent_tree.py` | DBC talent tree parser → Python DAG | DONE (598 lines) |
| `scripts/lib/talent_codec.py` | Base64 talent string encode/decode | DONE (491 lines) |
| `scripts/lib/tree_codec_bridge.py` | Bridge: tree + codec high-level API | DONE (239 lines) |
| `scripts/lib/talent_neighbor.py` | Constraint-aware neighbor generation | DONE (290 lines) |
| `scripts/apl_optimizer.py` | APL optimization loop (per fight style) | DONE (288 lines) |
| `scripts/talent_local_search.py` | Talent seed + neighborhood hill-climb | DONE (310 lines) |
| `scripts/talent_build_compare.py` | Wowhead build comparison (per-style) | DONE (397 lines) |
| `scripts/optimize_all.py` | Master orchestrator (--report, --apl, --talent) | DONE (145 lines) |

Deprecated (kept in repo, removed from pipeline):
- `scripts/lib/node_classifier.py` — wrong regex, wrong abstraction
- `scripts/lib/talent_permute.py` — generates 0 combos with correct budgets

Design doc: `optimization_action_plan.md`

---

## Known Issues

### Open

- **Darkmoon Deck stacking** — Issue #81, blocked on beta data. See `darkmoon_investigation.md`.
- **Tier set DBC verification** — 7 specs need sim confirmation of auto-parsed bonuses.
- **61 TODO/FIXME in sc_mage.cpp** — code quality debt, zero DPS impact.
- **DK Unholy** — control_undead + unholy_endurance NYI (utility/CC, zero DPS).

### Resolved

- DK Blood HAC crash — `player_t::interrupt()` race condition. Fixed.
- Guardian Druid APL — full rewrite (3k → 10.6k DPS). Fixed 2026-03-27.
- 5 missing tier sets. Fixed 2026-03-24.
- 8 APL desync issues. Fixed 2026-03-25.
- Wowhead extraction pipeline — all bugs resolved.
- Talent neighbor budget bug — strict budgets enforced (no headroom). Fixed 2026-03-28.

---

## Reference Files

| File | What |
|------|------|
| `AGENTS.md` | Agent guide — file map, sim commands, domain knowledge, pitfalls |
| `task_list.md` | Remaining work — 7 batches with dependencies and commands |
| `APL_optimization.md` | APL syntax reference, rules, common mistakes |
| `optimization_action_plan.md` | Optimization design — talent local search + APL mutation |
| `darkmoon_investigation.md` | Darkmoon trinket stacking investigation (Issue #81) |
| `project_structure.md` | Codebase navigation — maps task types to source files |
| `docs/fury_apl_optimization_plan.md` | Warrior Fury deep APL analysis and test results |
| `docs/archive/` | Historical audit data, APL diff reports |

# SimulationCraft — Midnight Expansion (MID1) Progress

Last updated: 2026-03-29

## Status

| Metric | Value |
|--------|-------|
| Profiles | 56/56 PASS (compile + 1-iter sim + talent validation) |
| Talent validation | 56/56 PASS (budget, prereqs, req_points gates) |
| Baselines | 112/112 FRESH (2026-03-28, target_error=0.1) |
| Tier sets | 33/33 implemented |
| Apex talents | 33/33 implemented (3 spell IDs each) |
| APL audit | 42/42 resolved (batch 9 proven by baselines) |
| Talent builds | 29/33 profiles updated from Wowhead comparison |
| Optimization tooling | ALL BUILT — 16 scripts, ~4,000 lines |
| Engine bugs | All resolved |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |

## What's Next

Each spec produces TWO independent optimal builds — one for Patchwerk (ST raid), one for HecticAddCleave (M+/AoE).

| Batch | Description | Status |
|-------|-------------|--------|
| 1 | Fresh baselines (56 PW + 56 HAC) | DONE |
| 2 | APL diff re-run + triage | DONE — 0 real gaps |
| 3 | APL optimization — warrior_fury tested | PW +0.00%, HAC +0.44% — full run PENDING |
| 4 | Talent local search — warrior_fury tested | PW +2.79%, HAC pending — full run PENDING |
| 5 | Re-baseline + cross-validation | PENDING |
| 6 | Trinket combinatorics (Phase 5) | PENDING |
| 7 | Final docs + cleanup | PENDING |

---

## Talent Validator (2026-03-29)

Real DB2 prerequisite edges replaced the heuristic edge builder:

| Data | Source | Count |
|------|--------|-------|
| TraitEdge.csv | DB2 data, build 12.0.1.66384 | 7,116 edges total |
| Type 2 edges | Class/spec/hero prerequisites | 6,409 |
| Type 0 edges | Professions/dragonriding (ignored) | 776 |
| Heuristic accuracy | Old system vs real edges (warrior_fury) | 77.7% precision, 90.1% recall |

Validation checks per build:
1. **Point budget**: 34 class + 34 spec purchased (hero auto-granted)
2. **Rank validity**: 1..max_ranks per node
3. **req_points gates**: enough points spent in sub-tree to unlock tier
4. **Prerequisite edges**: at least 1 parent selected (OR logic)

Neighbor generator produces ~200+ valid mutations per spec for hill-climbing.

### Granted Class Talents per Spec

| Grants | Specs |
|--------|-------|
| 0 | Warlock (Soul Leech undocumented, hardcoded) |
| 1 | DH, DK, Hunter, Mage, Rogue, Shaman |
| 2 | Evoker, Monk, Priest, Warrior |
| 3 | Druid, Paladin |

### Hero Tree Filtering Fix

Hero trees are shared between 2 specs. Internal nodes may be tagged with only one spec's id_spec, but both can use them. SimC's parser confirms this (player.cpp ~line 2929). Fixed by:
- Including ALL nodes from available hero sub-trees regardless of id_spec
- Discovering sub-tree availability via selection nodes (fixes Evoker Aug + Chronowarden)

---

## Warrior Fury Test Results (2026-03-28–29)

### Talent Local Search (2026-03-29, with real edge validator)

| Style | Baseline | Optimized | Gain | Key Swap |
|-------|----------|-----------|------|----------|
| Patchwerk | 86,897 | 89,777 | +3.31% | -Reckless Abandon +Wrath and Fury, -Pain and Gain +Stance Mastery |

All builds validated: 34/34/15 budget, real prerequisite edges, SimC smoke test PASS.

### APL Optimization (2026-03-28)

| Style | Result |
|-------|--------|
| Patchwerk | +0.00% — already optimal |
| HecticAddCleave | +0.44% — rampage threshold 100→80 in thane_aoe |

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
| 1. Wowhead extraction (33 specs × 5 pages) | DONE |
| 2. APL diff vs Wowhead | DONE |
| 3. Profile updates (gear, consumables, talents) | DONE |
| 3.5. Extractor pipeline fixes + visual audit | DONE |
| 3.6. 3-way upstream APL comparison (198 sims, 10k iter) | DONE |
| 4a. Complete all 112 baselines | DONE |
| 4b. Re-run APL diff with fixed pipeline | DONE — 0 real gaps |
| 4c. Triage all MISSING items | DONE — 58 false positives |
| 4d-talent. Wowhead build comparison (262 builds) | DONE — 29/33 improved |
| 4d-apl. APL optimization (per fight style) | TESTED on Fury — full run pending |
| 4d-talent2. Talent local search (real edges + validator) | TESTED on Fury — full run pending |
| 5. Trinket combinatorics | NOT STARTED |

---

## Known Issues

### Open

- **Darkmoon Deck sigil stacking** — Issue #81, blocked on beta/live data. Basic trinkets work (14 refs in unique_gear_midnight.cpp). Issue is about Blood/Rot/Hunt/Void + sigil embellishment interaction. See `darkmoon_investigation.md`. Zero impact on optimization pipeline.
- **DH Vengeance Aldrachi Reaver** — underspent TWW-era build (31/34 class, 30/34 spec, hero=12). Structurally valid, 7 talent points unused. Will be fixed by talent local search.
- **61 TODO/FIXME in sc_mage.cpp** — code quality debt, zero DPS impact.

### Resolved

- Tier set DBC verification — 33/33 work, 80 DBC entries, 112 non-zero baselines prove all active. Resolved 2026-03-29.
- Warlock Demo Soul Harvester hero=28 — both hero trees active, runs fine, structurally valid. Not a bug.
- Wowhead over-budget builds — Prot Paladin Templar 1/3 have 35 class pts. Used valid alternates. Resolved 2026-03-29.
- Talent validator with real DB2 edges (6,409 edges from TraitEdge.csv). Fixed 2026-03-29.
- Hero tree spec filtering — internal nodes wrongly excluded for shared hero trees. Fixed 2026-03-29.
- 4 broken talent strings (Mage Frost, Prot Paladin — wrong class nodes). Fixed 2026-03-29.
- DK Blood HAC crash — `player_t::interrupt()` race condition. Fixed.
- Guardian Druid APL — full rewrite (3k → 10.6k DPS). Fixed 2026-03-27.
- 5 missing tier sets. Fixed 2026-03-24.
- 8 APL desync issues. Fixed 2026-03-25.
- APL audit batch 9 (tier DBC verification) — deferred items proven working by baselines.

---

## Reference Files

| File | What |
|------|------|
| `AGENTS.md` | Agent guide — file map, sim commands, domain knowledge, pitfalls |
| `APL_optimization.md` | APL syntax reference, rules, common mistakes |
| `optimization_action_plan.md` | Optimization design — talent local search + APL mutation |
| `darkmoon_investigation.md` | Darkmoon trinket stacking investigation (Issue #81) |
| `project_structure.md` | Codebase navigation — maps task types to source files |
| `docs/archive/` | Historical audit data, APL diff reports |

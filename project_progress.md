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
| APL diff (Phase 4b) | 0 real gaps (58 false positives triaged 2026-03-28) |
| Talent builds | 29/33 profiles updated from Wowhead comparison |
| Engine bugs | All resolved (DK Blood HAC crash, Guardian Druid APL) |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |

## What's Next

**Design:** Each spec produces TWO independent optimal builds — one for Patchwerk (ST raid), one for HecticAddCleave (M+/AoE). Full task list: `task_list.md`

| Batch | Description | Status |
|-------|-------------|--------|
| 1 | Fresh baselines (56 PW + 56 HAC) | ✅ DONE |
| 2 | APL diff re-run + triage | ✅ DONE — 0 real gaps |
| 3 | APL optimization — 33 specs × 2 fight styles | PENDING |
| 4 | Talent permutation — pivot sweep + tuning per style | PENDING |
| 5 | Re-baseline + cross-validation | PENDING |
| 6 | Trinket combinatorics (Phase 5) | PENDING |
| 7 | Tier set DBC verification + final docs | PENDING |

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
| 2. APL diff vs Wowhead | ✅ DONE — 2 fixes applied |
| 3. Profile updates (gear, consumables, talents) | ✅ DONE |
| 3.5. Extractor pipeline fixes + visual audit | ✅ DONE |
| 3.6. 3-way upstream APL comparison (198 sims, 10k iter) | ✅ DONE — 4 upstream wins, 1 ours, 27 ties |
| 4-pre. Fix 8 APL issues from comparison | ✅ DONE |
| 4a. Complete all 112 baselines | ✅ DONE |
| 4b. Re-run APL diff with fixed pipeline | ✅ DONE — 0 real gaps |
| 4c. Triage all MISSING items | ✅ DONE — all 58 false positives |
| 4d-talent. Wowhead build comparison (262 builds) | ✅ DONE — 29/33 improved |
| 4d-apl. APL optimization engine | IN PROGRESS — tool built, full run pending |
| 4d-talent2. Talent permutation engine | ✅ DONE — tooling built |
| 5. Trinket combinatorics | NOT STARTED |

---

## Optimization Tooling

All scripts implemented and tested (~2,500 lines across 11 files):

| Script | Purpose |
|--------|---------|
| `scripts/lib/sim_runner.py` | Run sims, parse JSON, per-fight-style + composite scoring |
| `scripts/lib/apl_parser.py` | Parse/serialize .simc APL ↔ structured data |
| `scripts/lib/apl_mutations.py` | Mutation operators: swap, sweep, promote, route |
| `scripts/lib/talent_tree.py` | DBC talent tree parser (trait_data.inc → Python DAG) |
| `scripts/lib/talent_codec.py` | Base64 talent string encode/decode (33/33 round-trip) |
| `scripts/lib/tree_codec_bridge.py` | Bridge: tree + codec high-level API |
| `scripts/lib/node_classifier.py` | DPS/GATING/UTILITY classification from APL + code |
| `scripts/lib/talent_permute.py` | Pivot sweep + tuning hill-climb |
| `scripts/apl_optimizer.py` | APL optimization loop (per fight style) |
| `scripts/talent_build_compare.py` | Wowhead build comparison (per-style ranking) |
| `scripts/optimize_all.py` | Master orchestrator (--report, --apl, --all, --fight-style) |

Design doc: `optimization_action_plan.md`

---

## Known Issues

### Open

- **Darkmoon Deck stacking** — Issue #81, blocked on beta data. Trinket + Sigil interaction unknown. See `darkmoon_investigation.md`.
- **Tier set DBC verification** — 7 specs (Mage ×3, Paladin ×2, Warlock Dest, WW Monk) need sim confirmation that auto-parsed bonuses apply correctly.
- **61 TODO/FIXME in sc_mage.cpp** — code quality debt, zero DPS impact.
- **DK Unholy** — control_undead + unholy_endurance NYI (utility/CC, zero DPS).

### Resolved

- DK Blood HAC crash — `player_t::interrupt()` schedule_ready race. Fixed.
- Guardian Druid APL — full rewrite (3k → 10.6k DPS). Fixed 2026-03-27.
- 5 missing tier sets (DH Havoc, Evoker Aug, Priest Shadow, Enh Shaman, WW Monk). Fixed 2026-03-24.
- 8 APL desync issues (4 upstream imports + 4 C++ generator syncs). Fixed 2026-03-25.
- Wowhead extraction pipeline — 3 extractor bugs, 17 parser fixes. All resolved.

---

## Profiles

56/56 PASS — 52 base + 4 hero-tree variants (Balance Keeper/Elune, Aug Chronowarden, Assa Deathstalker).

All profiles in `profiles/MID1/`. Baselines in `results/phase4/`.

---

## Build

```
cmake -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON
cmake --build build -j$(nproc)
cp build/simc engine/simc
```

gcc-14 (Debian 14.2.0-19), RelWithDebInfo. CI: gcc-14 + clang-18 ASan/UBSan.

---

## Reference Files

| File | What |
|------|------|
| `AGENTS.md` | Agent guide — file map, sim commands, domain knowledge, pitfalls |
| `task_list.md` | Remaining work — 7 batches with dependencies and commands |
| `APL_optimization.md` | APL syntax reference, rules, common mistakes |
| `optimization_action_plan.md` | Optimization system design — 7 milestones |
| `darkmoon_investigation.md` | Darkmoon trinket stacking investigation (Issue #81) |
| `project_structure.md` | Codebase navigation — maps task types to source files |
| `docs/archive/` | Historical audit data, APL diff reports |

# SimulationCraft — Midnight Expansion (MID1) Progress

Last updated: 2026-03-31

## Status

| Metric | Value |
|--------|-------|
| Profiles | 60/60 PASS (compile + 1-iter sim + talent validation) |
| Talent validation | 60/60 PASS (budget, prereqs, req_points gates) |
| Baselines | 112/112 (2026-03-28) — **STALE, needs re-run post upstream sync** |
| Tier sets | 33/33 exist in C++ — **behavioral correctness not yet verified** |
| Apex talents | 33/33 implemented (3 spell IDs each) |
| APL audit | 42/42 resolved |
| Talent builds | 29/33 profiles updated from Wowhead comparison |
| Tooling | 16 scripts, ~4,000 lines (optimization + validation + extraction) |
| Upstream sync | **181 commits behind** — BLOCKING |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |

---

## What's Next

Priority order reflects our full maintenance scope — not just optimization.

| # | Task | Type | Status |
|---|------|------|--------|
| **1** | **Upstream sync** — rebase onto latest upstream (181 commits), rebuild, re-validate | Engine | **BLOCKING** |
| **2** | **Review upstream C++ fixes** — understand each class module change, verify with our profiles | Engine | PENDING |
| **3** | **Engine correctness audit** — multi-target sweeps, tier set value verification, proc rate checks for all 33 specs | Testing | PENDING |
| 4 | Re-extract Wowhead data if build number changed | Data | PENDING |
| 5 | Re-baseline all specs (fresh 112 baselines post-sync) | Testing | PENDING |
| 6 | Bug hunting — scan class modules for TODO/FIXME/NYI, compare proc chains against tooltips | Engine | PENDING |
| 7 | Talent + APL optimization (per spec, both fight styles) | Optimization | IN PROGRESS |
| 8 | Trinket combinatorics | Optimization | PENDING |
| 9 | Final docs + cleanup + contribute back upstream | Maintenance | PENDING |

### Upstream Fixes We're Missing (181 commits)

These are engine-level fixes we should have caught or contributed ourselves:

| Spec | Fix | Commits | Impact |
|------|-----|---------|--------|
| Balance Druid | Star Cascade proc chain (4 bugs: impact procs, Harmony of Heavens, 4pc, Hail of Stars) | 4 | DPS accuracy |
| Paladin | 2 segfault fixes (empty/short target lists) + UR-Judgment + Glory delay + HoL recalc | 5 | Crash + DPS |
| Enhancement Shaman | 4PC mastery bug (halves the value!) | 1 | **DPS wildly wrong** |
| Monk | Empowered Tiger Lightning event manager stuck condition | 1 | Silent corruption |
| Devourer | Void Ray soul gen doesn't scale with targets | 1 | AoE DPS wrong |
| Assassination Rogue | Improved Garrote snapshotting | 1 | DPS accuracy |
| Priest | Shadow Word: Death in execute rotation | 1 | APL gap |
| Evoker | Default consumable fix | 1 | Profile |
| All | DBC data updates (Build 66384 → 66709) | 3+ | All specs affected |

### Optimization Progress (Batch 7)

All results below are **provisional** — based on pre-sync engine, will need re-validation.

| Spec | PW DPS | HAC DPS | Key HAC talent swaps | _HAC.simc | Commit |
|------|--------|---------|---------------------|-----------|--------|
| DK Unholy | 107,884 | 236,310 | different build | YES | 1ea57c2 |
| DK Frost | REVERTED | REVERTED | gate-invalid, needs re-opt | NO | reverted |
| DK Blood | DONE | SKIP(tank) | — | SKIP | 242530d |
| DH Havoc | REVERTED | REVERTED | gate-invalid, needs re-opt | NO | reverted |
| DH Vengeance | REVERTED | REVERTED | gate-invalid, needs re-opt | NO | reverted |
| DH Devourer | 112,082 | 206,038 | +Eradicate, +Pursuit, Scythe choice swap | YES | e4d8552 |
| Warrior Prot | 67,574 | 121,997 | +Barbaric Training, +Snap Induction, +Massacre | YES | e50fd77 |
| Warrior Fury | +3.31%(PW) | +0.44%(HAC) | — | PENDING | test only |
| *27 other specs* | PENDING | PENDING | — | PENDING | — |

---

## Completed Work

### Data Extraction & Auditing (Phases 1-4)

| Phase | Status |
|-------|--------|
| Wowhead extraction (33 specs × 5 pages) | DONE |
| APL diff vs Wowhead | DONE |
| Profile updates (gear, consumables, talents) | DONE |
| Extractor pipeline fixes + visual audit | DONE |
| 3-way upstream APL comparison (198 sims, 10k iter) | DONE |
| 112 baselines (56 PW + 56 HAC) | DONE — needs re-run |
| APL diff re-run with fixed pipeline | DONE — 0 real gaps |
| Triage all MISSING items | DONE — 58 false positives |
| Wowhead build comparison (262 builds) | DONE — 29/33 improved |
| APL optimization (Fury test) | PW +0.00%, HAC +0.44% |
| Talent local search (Fury test) | PW +3.31% |

### Talent Validator (2026-03-29)

Real DB2 prerequisite edges (6,409 Type 2 from TraitEdge.csv) replaced heuristic edges.
Validation checks: point budget, rank validity, req_points gates (purchased-only),
prerequisite edges (OR logic). req_points gate bug fixed 2026-03-30.
Neighbor generator produces ~200+ valid mutations per spec for hill-climbing.

### Baselines (2026-03-28) — STALE

| Top 5 Patchwerk | DPS | Top 5 HecticAddCleave | DPS |
|-----------------|----:|----------------------|----:|
| Rogue Subtlety | 124,620 | Warlock Demonology | 472,187 |
| Shaman Elemental | 116,547 | Warlock Demo SH | 470,024 |
| Evoker Devastation | 115,502 | Rogue Subtlety | 290,018 |
| Evoker Devastation FS | 115,386 | Monk Windwalker | 231,023 |
| Mage Frost Frostfire | 113,229 | Warrior Arms | 229,257 |

Full report: `python3 scripts/optimize_all.py --report`

---

## Known Issues

### Open

- **181 upstream commits behind** — BLOCKING. Includes crash fixes, scaling corrections,
  proc chain rewrites, tier set math errors, DBC updates. See table above.
- **Darkmoon Deck sigil stacking** — Issue #81, blocked on beta/live data.
  See `docs/internal/darkmoon_investigation.md`.
- **DH Vengeance Aldrachi Reaver** — underspent build (31/34 class, 30/34 spec).
  Will be fixed by talent local search after upstream sync.
- **Tier set behavioral correctness** — existence verified (33/33), but numeric values
  and proc mechanics not yet cross-checked against tooltips. Enh 4PC mastery halving
  proves this matters.
- **61 TODO/FIXME in sc_mage.cpp** — code quality debt.

### Resolved

- req_points gate validator bug — fixed 2026-03-30 (purchased-only counting)
- Hero tree spec filtering — fixed 2026-03-29
- 4 broken talent strings — fixed 2026-03-29
- DK Blood HAC crash — fixed (player_t::interrupt race condition)
- Guardian Druid APL — full rewrite, 3k → 10.6k DPS (2026-03-27)
- 5 missing tier sets — fixed 2026-03-24
- 8 APL desync issues — fixed 2026-03-25

---

## Reference Files

| File | What |
|------|------|
| `AGENTS.md` | Agent guide — mission, workflow, domain knowledge, pitfalls |
| `FORK_VS_UPSTREAM_REVIEW.md` | Fork vs upstream divergence analysis + post-mortem |
| `APL_optimization.md` | APL syntax reference, rules, common mistakes |
| `optimization_action_plan.md` | Optimization design — talent local search + APL mutation |
| `OPTIMIZATION_HOWTO.md` | Step-by-step manual guide — exact commands to optimize any spec |
| `project_structure.md` | Codebase navigation — maps task types to source files |
| `docs/internal/darkmoon_investigation.md` | Darkmoon trinket stacking investigation (Issue #81) |
| `docs/archive/` | Historical audit data, APL diff reports |

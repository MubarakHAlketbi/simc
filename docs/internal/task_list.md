# Task List — SimC Midnight Remaining Work

Updated: 2026-03-28

## Design Principle

Each spec has TWO independent optimal builds:
- **Patchwerk** (single-target raid boss)
- **HecticAddCleave** (M+/AoE/target switching)

Tank specs (Blood, Guardian, Brewmaster, Protection x2, Vengeance) skip HAC if it produces 0 DPS.

---

## Batch 1 — Fresh Baselines ✅ DONE
112 JSONs (56 PW + 56 HAC) at target_error=0.1. All 56 profiles.

## Batch 2 — APL Diff Re-run ✅ DONE
0 real gaps. 58 MISSING items all false positives.

## Batch 3 — APL Optimization
**Status:** Warrior Fury tested (PW +0.00%, HAC +0.44%). Full 33-spec run pending.
**Estimate:** ~2-6h compute, 0 code

| # | Task | Command |
|---|------|---------|
| 3.1 | Run all specs PW | `python3 scripts/apl_optimizer.py --all --fight-style Patchwerk --max-iter 5 --threads 16` |
| 3.2 | Run all specs HAC | Same with `--fight-style HecticAddCleave` |
| 3.3 | Review + apply improvements >0.3% | Update .simc profiles + sync C++ generators |
| 3.4 | Smoke test all 56 profiles | `iterations=1` loop |

## Batch 4 — Talent Local Search
**Status:** Warrior Fury tested (PW +1.52%, HAC +0.65%). Full 33-spec run pending.
**Estimate:** ~5h compute, 0 code (all tooling built)

Architecture: Wowhead builds (seeds) → screen per style → single-node neighborhood → hill-climb → confirm. Budget-strict (no headroom). Converges in 1-2 passes.

| # | Task | Command |
|---|------|---------|
| 4.1 | Run all specs PW | `python3 scripts/talent_local_search.py --all --fight-style Patchwerk --threads 16` |
| 4.2 | Run all specs HAC | Same with `--fight-style HecticAddCleave` |
| 4.3 | Update profiles with winning talent strings (>0.5% gain) | Manual edit |
| 4.4 | Create _M+ variant profiles where HAC best ≠ PW best | New .simc files |

## Batch 5 — Re-baseline + Validation
**Depends on:** Batches 3+4. **Estimate:** ~1h compute

| # | Task |
|---|------|
| 5.1 | Re-run all PW + HAC baselines |
| 5.2 | Generate final report |
| 5.3 | Verify no spec regressed vs Batch 1 |
| 5.4 | Smoke test all profiles |

## Batch 6 — Trinket Combinatorics (Phase 5)
**Depends on:** Batch 5. **Estimate:** ~6h (2h code + 4h compute)

| # | Task |
|---|------|
| 6.1 | Build trinket pair list from wowhead/*/extracted/bis.md |
| 6.2 | Sim all pairs per spec per fight style |
| 6.3 | Update profiles with BiS trinkets |

## Batch 7 — Tier Set Verification + Final Docs
**Estimate:** ~2h

| # | Task |
|---|------|
| 7.1 | Verify 7 tier set DBC auto-parse values |
| 7.2 | Fix any issues |
| 7.3 | Final doc updates + commit |

---

## Dependency Graph

```
Batch 1 ✅ → Batch 2 ✅ → Batch 3 (APL) ──→ Batch 4 (talent) ──→ Batch 5 (re-baseline)
                                                                          |
                                                                          v
                                                                    Batch 6 (trinkets)
                                                                          |
                                                                          v
                                                                    Batch 7 (final)
```

## Time Estimates

| Batch | Code | Compute | Status |
|-------|------|---------|--------|
| 1. Baselines | — | 0.5h | ✅ |
| 2. APL Diff | — | 0.2h | ✅ |
| 3. APL Optimization | — | 2-6h | Fury tested |
| 4. Talent Local Search | — | 5h | Fury tested |
| 5. Re-baseline | — | 1h | — |
| 6. Trinket Combos | 2h | 4h | — |
| 7. Final Docs | 1h | 0.5h | — |
| **TOTAL** | **3h** | **13-17h** | |

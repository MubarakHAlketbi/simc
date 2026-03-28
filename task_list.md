# Task List — SimC Midnight Remaining Work

Generated: 2026-03-28

## Design Principle

Each spec has TWO independent optimal builds:
- **Patchwerk** (single-target raid boss)
- **HecticAddCleave** (M+/AoE/target switching)

Optimization, baselines, and results are always per-fight-style.
Tank specs (Blood, Guardian, Brewmaster, Protection x2, Vengeance) skip HAC if it produces 0 DPS.

---

## Batch 1 — Fresh Baselines (blocks everything) ✅ COMPLETE 2026-03-28
**Estimate: ~30 min compute, 0 code**
**Why first:** 29/56 profiles have new talent strings. All downstream optimization needs current numbers.

| # | Task | Command | Output |
|---|------|---------|--------|
| 1.1 | Re-run all 56 PW baselines at target_error=0.1 | `for f in profiles/MID1/*.simc; do ./engine/simc $f fight_style=Patchwerk target_error=0.1 threads=16 json2=results/phase4/$(basename $f .simc)_patchwerk.json output=/dev/null; done` | 56 JSONs |
| 1.2 | Re-run all 56 HAC baselines at target_error=0.1 | Same with `fight_style=HecticAddCleave` | 56 JSONs |
| 1.3 | Generate fresh baseline report | `python3 scripts/optimize_all.py --report` | PW + HAC rankings |
| 1.4 | Update project_progress.md with new baseline numbers | Manual | Updated doc |

**Exit criteria:** 112 fresh JSONs, report shows all 56 profiles, no errors.

---

## Batch 2 — APL Diff Re-run (Phase 4b) ✅ COMPLETE 2026-03-28
**Estimate: ~10 min, 0 code**
**Result:** 0 real gaps. All 58 MISSING items are false positives (parser artifacts, engine-managed replacements, guide text). No APL changes needed.

| # | Task | Command | Output |
|---|------|---------|--------|
| 2.1 | Re-run gen_apl_diff.py | `python3 wowhead/gen_apl_diff.py` | Updated diff report |
| 2.2 | Triage HIGH-priority diffs | Read report, separate real gaps from false positives | Triage notes |
| 2.3 | Fix any real APL gaps found | Code edits to apl_*.cpp or .simc overrides | Fixes committed |
| 2.4 | Smoke test any changed profiles | `./engine/simc profiles/MID1/CHANGED.simc iterations=1 output=/dev/null` | All pass |

**Exit criteria:** Phase 4b COMPLETE, Phase 4c triaged, no HIGH gaps remaining.

---

## Batch 3 — APL Optimization (Phase 4d-apl)
**Estimate: ~2-6h compute (33 specs × 2 fight styles), 0 code**
**Why now:** All baselines fresh, APL gaps closed. This is the main optimization run.

| # | Task | Command | Output |
|---|------|---------|--------|
| 3.1 | Run APL optimizer — all specs, Patchwerk | `python3 scripts/apl_optimizer.py --all --fight-style Patchwerk --max-iter 5 --threads 16` | 33 × apl_optimization_pw.json |
| 3.2 | Run APL optimizer — all specs, HecticAddCleave | `python3 scripts/apl_optimizer.py --all --fight-style HecticAddCleave --max-iter 5 --threads 16` | 33 × apl_optimization_hac.json |
| 3.3 | Review results — accept improvements >0.3% | Read results/optimization/*/apl_optimization_{pw,hac}.json | List of accepted APLs |
| 3.4 | Apply accepted APL overrides to .simc files | Copy optimized_apl_{pw,hac}.simc content into ActionPriorityLists/default/ | Updated APLs |
| 3.5 | Sync accepted .simc APL improvements back to C++ generators | Edit apl_*.cpp to match | C++ synced |
| 3.6 | Smoke test all 56 profiles | Loop `iterations=1` over all profiles | 56/56 pass |

**Exit criteria:** Per-style APL optimization complete. optimized_apl_pw.simc and optimized_apl_hac.simc saved for every spec with >0.3% gain.

---

## Batch 4 — Talent Local Search (Seed + Neighborhood Hill-Climb)
**Estimate: ~5h compute, ~4.5h code**
**Why now:** APLs optimized. Wowhead builds cover strategic axes. Local search finds SimC-specific micro-gains.
**Depends on:** Batch 3 (optimized APLs are the evaluation harness)

**Architecture:** Wowhead builds (seeds) → screen per style → single-node neighborhood → hill-climb → confirm.
Old classify-then-permute approach ABANDONED (wrong regex, wrong abstraction). See `optimization_action_plan.md`.

| # | Task | File | Output |
|---|------|------|--------|
| 4.1 | Implement constraint validation + neighbor generator | `scripts/lib/talent_neighbor.py` (~250 lines) | New file |
| 4.2 | Implement seed screening + hill-climb local search | `scripts/talent_local_search.py` (~250 lines) | New file |
| 4.3 | Rewrite talent_optimizer.py — wire seeds → local search | `scripts/talent_optimizer.py` | Rewritten |
| 4.4 | Add --talent flag to optimize_all.py | `scripts/optimize_all.py` | Updated |
| 4.5 | Test on warrior_fury (both styles) | CLI | Validate pipeline |
| 4.6 | Full 33-spec run — PW | `python3 scripts/optimize_all.py --talent --all --fight-style Patchwerk` | 33 × talent_local_search_pw.json |
| 4.7 | Full 33-spec run — HAC | Same with HecticAddCleave | 33 × talent_local_search_hac.json |
| 4.8 | Update profiles with winning talent strings | If >0.5% gain, update talents= in .simc | Updated profiles |
| 4.9 | Create _M+ variant profiles where HAC best ≠ PW best | New .simc files with HAC-optimal talents | New profile files |

**Exit criteria:** best_build_pw.txt and best_build_hac.txt per spec. Each ≥ best Wowhead build for that style. Profiles updated. _M+ variants created where styles diverge.

---

## Batch 5 — Re-baseline + Validation
**Estimate: ~1h compute, 0 code**
**Why now:** Both APLs and talents optimized. Need fresh numbers and cross-validation.
**Depends on:** Batches 3+4

| # | Task | Command | Output |
|---|------|---------|--------|
| 5.1 | Re-run all PW baselines (updated profiles) | Same as 1.1 | 56+ JSONs |
| 5.2 | Re-run all HAC baselines (updated profiles) | Same as 1.2 | 56+ JSONs |
| 5.3 | Generate final baseline report | `python3 scripts/optimize_all.py --report` | Per-style rankings |
| 5.4 | Cross-validate: best PW APL on HAC (informational) | Sim each spec's PW-optimized APL on HAC | Gap analysis |
| 5.5 | Cross-validate: best HAC APL on PW (informational) | Sim each spec's HAC-optimized APL on PW | Gap analysis |
| 5.6 | Verify no spec lost DPS vs Batch 1 baselines | Compare before/after per style | Regression check |
| 5.7 | Smoke test all profiles (old + new _M+ variants) | `iterations=1` over all | All pass |

**Exit criteria:** All profiles baselined. No regressions. Cross-validation data for reporting.

---

## Batch 6 — Trinket Combinatorics (Phase 5)
**Estimate: ~4h compute, ~2h code**
**Why now:** Profiles are final (talents + APLs optimized). Now find BiS trinket pairs.
**Depends on:** Batch 5

| # | Task | Command | Output |
|---|------|---------|--------|
| 6.1 | Build trinket pair list from wowhead/*/extracted/bis.md | Script to parse trinket options per spec | trinket_pairs.json per spec |
| 6.2 | Sim all pairs — PW (per spec) | 5000 iter per pair, Patchwerk | trinket_results_pw.json |
| 6.3 | Sim all pairs — HAC (per spec) | 5000 iter per pair, HecticAddCleave | trinket_results_hac.json |
| 6.4 | Rank trinket pairs per fight style | Best PW pair, best HAC pair per spec | trinket_summary.md |
| 6.5 | Update profiles with BiS trinkets (PW profiles) | Edit trinket slots in .simc | Updated profiles |
| 6.6 | Update _M+ profiles with BiS trinkets (HAC profiles) | Edit trinket slots in _M+.simc | Updated _M+ profiles |
| 6.7 | Final baselines with optimized trinkets | Re-run PW + HAC baselines | Final numbers |

**Exit criteria:** BiS trinket pairs identified per spec per fight style. Profiles updated.

---

## Batch 7 — Tier Set Verification + Docs (Batch 9 + M7)
**Estimate: ~2h, mostly verification**
**Why now:** Everything else is done. Low-risk cleanup and verification.

| # | Task | Command | Output |
|---|------|---------|--------|
| 7.1 | Verify 7 tier set DBC auto-parse values | Sim each spec with/without tier set, check bonus applies | Verification results |
| 7.2 | Fix any tier sets that aren't auto-parsing correctly | Code edits to unique_gear_midnight.cpp | Fixes committed |
| 7.3 | Update project_progress.md — all phases complete | Manual edit | Final status doc |
| 7.4 | Update AGENTS.md with final numbers | Manual edit | Updated guide |
| 7.5 | Generate final summary report | `python3 scripts/optimize_all.py --report` | Published results |
| 7.6 | Commit all work, push to midnight branch | `git add -A && git commit && git push` | Clean repo |

**Exit criteria:** All phases complete. Docs current. Repo clean.

---

## Dependency Graph

```
Batch 1 (baselines)
  |
  v
Batch 2 (APL diff) ──> Batch 3 (APL optimization)
                              |
                              v
                        Batch 4 (talent permutation)
                              |
                              v
                        Batch 5 (re-baseline + validation)
                              |
                              v
                        Batch 6 (trinket combinatorics)
                              |
                              v
                        Batch 7 (verification + docs)
```

## Time Estimates

| Batch | Code | Compute | Total |
|-------|------|---------|-------|
| 1. Baselines | 0h | 0.5h | 0.5h ✅ |
| 2. APL Diff | 0h | 0.2h | 0.2h ✅ |
| 3. APL Optimization | 0h | 2-6h | 2-6h |
| 4. Talent Local Search | 4.5h | 5h | 9.5h |
| 5. Re-baseline | 0h | 1h | 1h |
| 6. Trinket Combos | 2h | 4h | 6h |
| 7. Verification + Docs | 1h | 0.5h | 1.5h |
| **TOTAL** | **7.5h** | **13-17h** | **20-25h** |

Compute is parallelizable — with 2x parallel specs, compute drops ~50%.
Batches 3 and 4 are the big batches; can run overnight.

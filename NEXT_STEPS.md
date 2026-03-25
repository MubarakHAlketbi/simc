# Next Steps — SimulationCraft Midnight Expansion

**Updated:** 2026-03-25
**Status:** Spell database confirms 0 missing DPS spells. Focus shifts to APL quality.

---

## Priority 1: Fix 8 APL Issues from Upstream Comparison (Phase 4-pre)

The 3-way sim study (198 sims, 10k iter) found 8 specs with measurable DPS gaps.
These are the highest-impact changes we can make right now.

### A. Import upstream .simc APL (4 specs, upstream beats ours)

| # | Spec | Gap | Key Fixes |
|---|------|-----|-----------|
| 1 | Rogue Assassination | +2.2% | Import bleed spreading override, simplify Vanish to `!cooldown.deathmark.ready`, remove time_to_die guards, remove rupture potion gate |
| 2 | Rogue Subtlety | +1.9% | Remove energy>60 build gate, change shd_cp to `combo_points>=6`, remove Secret Tech outside-Dance fallback, Shadowstrike `targets<=2`, simplify Shadow Dance conditions |
| 3 | Warrior Arms | +1.3% | Sweeping Strikes `>5` (not >10), Demolish `stack>=5` (not =10), remove CS gate from Bladestorm, add `executioners_precision.stack=2` to MS |
| 4 | Monk Brewmaster | +0.8% | Celestial Brew threshold `0.3` with `charges_fractional>1.9` (not 0.95) |

Files: `ActionPriorityLists/default/` .simc files for each spec

### B. Sync C++ APL generators to .simc (4 specs, C++ badly lagging)

| # | Spec | Gap | Key Fixes |
|---|------|-----|-----------|
| 1 | Warlock Affliction | -7.7% | Remove drain_life filler, use drain_soul unconditionally |
| 2 | Warrior Fury | -6.7% | Reorder: Odyn's > Recklessness, Execute unconditional + above Crushing Blow, remove bloodthirst enrage line |
| 3 | Shaman Enhancement | -5.0% | Add `buff.hot_hand.up` guard to lava_lash, add frost_shock filler |
| 4 | Monk Brewmaster | -4.4% | Reorder BK below Keg Smash and RJW |

Files: `engine/class_modules/apl/apl_{class}.cpp` for each spec

---

## Priority 2: Complete Phase 4 Baselines (Phase 4a)

| Task | Details |
|------|---------|
| Run 4 missing HecticAddCleave sims | DK Blood x2, Evoker Dev x2 |
| Re-run baselines for 5 changed profiles | Druid Bal x3, Evoker Aug x2 (talent strings changed) |

---

## Priority 3: APL Optimization Loop (Phase 4d)

After Priorities 1-2 are done, run the full optimization loop per `APL_optimization.md`:

1. **Coverage audit** — verify all registered spells appear in APL
2. **Variable extraction** — consolidate repeated sub-expressions
3. **Permutation candidates** — adjacent action swaps, condition tightening/loosening
4. **Sim each candidate** — accept only when composite improves, neither style regresses >1%
5. **Condition sweep** — numeric thresholds ±20% in 5% steps
6. **Multi-build validation** — APL works for ALL talent builds (no build >2% regression)
7. **Convergence** — iterate until delta < 0.1%

---

## Priority 4: Trinket Combinatorics (Phase 5)

For each spec, sim all BiS trinket pairs from `extracted/bis.md`:
- Generate C(N,2) combinations per spec
- Sim both Patchwerk + HecticAddCleave
- Update profiles with best pair
- Re-run Phase 4d if trinket changes rotation priorities

---

## Priority 5: Deferred Audit Items

| Batch | Task | Priority |
|-------|------|----------|
| 9 | Tier set DBC auto-parse verification (7 specs) | MEDIUM |
| 10 | Low cleanup: destro 4pc value, DK Blood fillers, DK Frost ERW, druid APB trinket, paladin judgment | LOW |

---

## Completed (for reference)

- [x] Spell database: 4,410 spells, 0 genuine gaps (2026-03-25)
- [x] 65 obsolete .md files cleaned up (2026-03-25)
- [x] 3-way APL comparison: 198 sims at 10k iter, all 33 specs (2026-03-24)
- [x] Audit batches 1-8: 35/42 issues resolved (2026-03-24)
- [x] Phase 3: profiles, consumables, gear, talents updated (2026-03-22)
- [x] Phase 2: APL diff validation, 2 fixes (2026-03-22)
- [x] Phase 1: Browser extraction, 33 specs × 5 pages (2026-03-22)
- [x] All 56 profiles pass 1-iter sim (2026-03-22)
- [x] All 33 apex talents verified (2026-03-17)

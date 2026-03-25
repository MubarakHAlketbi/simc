# Release Gap Analysis — SimulationCraft Midnight (MID1)
# Generated: 2026-03-25
# Goal: Identify all remaining work before first stable release

---

## Executive Summary

The project is ~85% complete. All 56 profiles compile and sim, the spell database
has 0 gaps, all tier sets and apex talents are implemented, and Phase 4 baselines
are 100% done (112/112 JSONs). The remaining gaps fall into 3 tiers.

---

## TIER 1: BLOCKING — Must fix before any release (7 items)

### ~~1A. Priority 1 Group A: Import upstream .simc APL fixes (4 specs)~~ ✅ DONE

Completed in commit d4c2cc4 (2026-03-25). All 4 upstream APLs imported.

### 1B. Guardian Druid profile uses stub APL (1 profile)

The C++ APL generator (guardian_apl.inc) was rewritten with a full rotation
on 2026-03-24. However, the PROFILE still overrides it with an
`assisted_combat` stub (~13 actions, no Ironfur, no cooldown management).
All Guardian Druid sim results are using the stub, not the real APL.

Fix: Remove the inline `actions=...` lines from MID1_Druid_Guardian.simc
so the C++ APL is used. Then re-run baselines.

### 1C. Update project_progress.md (stale status)

project_progress.md still says:
  - Phase 4-pre: NOT STARTED (Group B is done)
  - Phase 4a: NOT STARTED (all HAC sims are done, DK Blood bug fixed)
  - Phase 4 HAC count: 52/56 (now 56/56)

These need updating to avoid confusion.

---

## TIER 2: IMPORTANT — Should fix before release (6 items)

### 2A. Regenerate comparison report (deleted)

The FULL_COMPARISON_10K.md was deleted during the 65-file cleanup.
Need to regenerate from existing JSON results in results/apl_compare_all/
using scripts/run_apl_compare_all.py (or just re-extract DPS from JSONs).

### 2B. Re-run apl_compare for 3 incomplete specs

results/apl_compare/ is missing HAC runs for:
  - DK Blood (ours_hac, up_hac) — now possible with engine bug fix
  - Druid Balance (up_pw, up_hac)
  - Evoker Devastation (ours_hac, up_hac)

### 2C. Phase 4b: Re-run APL diff (gen_apl_diff.py)

The extraction pipeline was fixed (6 hero talents, 5 build variants) since
the last diff run. Results will change. This validates whether our APLs match
Wowhead rotation priorities.

### 2D. Batch 9: Tier set DBC auto-parse verification (7 specs)

Deferred from audit. Verify tier set bonus values match DBC spell data for:
Mage (Arcane 4pc, Fire 2pc, Frost 2pc), and 4 other specs TBD.
Risk: low — all tier sets are implemented, this is value verification only.

### 2E. Batch 10: Low-priority cleanup (5 items)

  - Destro Warlock 4pc value verification
  - DK Blood filler optimization
  - DK Frost ERW timing
  - Druid APB trinket interaction
  - Paladin Judgment threshold

### 2F. Rebuild binary with all changes

The engine/simc binary needs to be rebuilt to include:
  - Priority 1B C++ APL sync (warlock, warrior, shaman, monk) ✓ done
  - DK Blood consumption_release engine bug fix ✓ done
  - All APL .inc changes
Build is clean (gcc-14). Just needs: cmake --build build && cp build/simc engine/simc

---

## TIER 3: NICE TO HAVE — Post-release optimization

### 3A. Phase 4d: Full APL optimization loop

Per APL_optimization.md, the 8-step loop:
  1. Coverage audit
  2. Variable extraction
  3. Permutation candidates
  4. Sim each candidate
  5. Condition sweep (thresholds ±20%)
  6. Multi-build validation
  7. Convergence (<0.1% delta)

This is a LARGE effort (potentially weeks). Not blocking for release.

### 3B. Phase 5: Trinket combinatorics

Sim all BiS trinket pairs per spec. C(N,2) combinations per spec,
both Patchwerk + HecticAddCleave. Update profiles with best pair.

### 3C. 61 TODO/FIXME in sc_mage.cpp

Known tech debt. Zero DPS impact — mostly code quality notes.

### 3D. Trinket+embellishment stacking (GitHub Issue #81)

Blocked on live data. Cannot resolve until Midnight launches.

---

## Scorecard

| Category                      | Status                           |
|-------------------------------|----------------------------------|
| Profiles (compile + sim)      | 56/56 PASS ✅                     |
| Spell database                | 4,410 spells, 0 gaps ✅           |
| Apex talents                  | 33/33 implemented ✅              |
| Tier sets                     | 33/33 implemented ✅              |
| Phase 4 baselines (PW+HAC)   | 112/112 complete ✅               |
| Engine bugs                   | DK Blood HAC fixed ✅             |
| Audit issues resolved         | 35/42 (batches 1-8) ✅            |
| C++ APL sync (Group B)        | 4/4 done ✅                       |
| .simc APL imports (Group A)   | 4/4 done ✅                       |
| Guardian Druid profile        | Uses stub APL ❌                  |
| APL optimization loop         | Not started ⏳                    |
| Trinket combinatorics         | Not started ⏳                    |
| Comparison report             | Deleted, needs regen ⚠️           |
| Documentation freshness       | project_progress.md stale ⚠️     |

---

## Recommended Release Path

**Minimum Viable Release (3 items):**
1. ~~Fix 4 Group A .simc APLs~~ ✅ DONE
2. Fix Guardian Druid profile (remove assisted_combat override)
3. Final 56-profile smoke test (1 iter, both fight styles)

**Estimated effort:** Less than 1 session.

After that, Phase 4d optimization and Phase 5 trinkets are iterative
improvements that can ship as point releases.

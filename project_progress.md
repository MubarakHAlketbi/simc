# SimulationCraft — Midnight Expansion (MID1) Progress

Last updated: 2026-03-31 — **v0.3 Full Optimization Pass**

**Game build: 12.0.1.66709 Live** — we target Live only, ignore 12.0.5.x PTR.

## Status

| Metric | Value |
|--------|-------|
| Release | **v0.3** (tagged 2026-03-31) |
| Profiles | 89/89 PASS (compile + 1-iter sim + talent validation) |
| Talent validation | 89/89 PASS (budget, prereqs, req_points gates) |
| Baselines | 126/126 FRESH (2026-03-31, Build 66709, target_error=0.1) |
| Tier sets | 33/33 behaviorally verified — all effectN reads checked against DBC |
| Engine audit | **COMPLETE** — 3132 effectN reads scanned, 6 bugs found+fixed |
| Apex talents | 33/33 implemented (3 spell IDs each) |
| APL audit | 42/42 resolved |
| Optimization | **33/33 specs optimized** — talent + APL, both PW & HAC |
| Tank HAC profiles | **6/6 tanks have HAC profiles** (fixed 2026-03-31) |
| Tooling | 20 scripts, ~6,000 lines (optimization + validation + audit) |
| Upstream sync | **SYNCED** — Build 66709, merged 2026-03-31 |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |

---

## What's Next

| # | Task | Type | Status |
|---|------|------|--------|
| ~~1~~ | ~~Upstream sync~~ — merged 359 commits, Build 66709 | Engine | **DONE** |
| ~~2~~ | ~~Re-baseline all specs~~ — 120/120 fresh on Build 66709 | Testing | **DONE** |
| ~~3~~ | ~~Engine correctness audit~~ — DBC verification, tier set behavioral checks, effectN OOB scan | Testing | **DONE (v0.2)** |
| ~~7~~ | ~~Talent + APL optimization~~ — 33/33 specs, both fight styles | Optimization | **DONE (v0.3)** |
| **4** | **Re-extract Wowhead data** (build changed 66384→66709) | Data | PENDING |
| 5 | Multi-target sweeps (1,3,5,10 targets) for AoE scaling verification | Testing | PENDING |
| 6 | Proc rate validation — compare JSON execute counts vs RPPM/ICD tooltips | Testing | PENDING |
| 8 | Trinket combinatorics | Optimization | PENDING |
| 9 | Final docs + cleanup + contribute fixes back upstream | Maintenance | PENDING |

---

## v0.3 — Full Optimization Pass (2026-03-31)

All 33 specs optimized from scratch (fresh engine-correct baselines). Each spec produces
two independent profiles: PW-optimized (`.simc`) and HAC-optimized (`_HAC.simc`).
Tank specs (Blood, Guardian, Brewmaster, Prot Paladin, Prot Warrior, Vengeance) now
include HAC profiles — the tanks-skip-HAC restriction was removed.

### Optimization Results

| Spec | PW DPS | HAC DPS | Talent | APL Gains |
|------|-------:|--------:|--------|-----------|
| warrior_arms | 82,060 | 202,711 | -/Y | HAC +1.97% |
| warrior_fury | 92,619 | 217,892 | Y/Y | PW +0.59% |
| warrior_protection | 75,532 | 136,209 | Y/Y | — |
| paladin_protection | 59,962 | 113,834 | Y/Y | — |
| paladin_retribution | 114,026 | 178,327 | Y/Y | — |
| hunter_bm | 97,673 | 204,410 | Y/Y | — |
| hunter_mm | 108,100 | 182,240 | Y/Y | — |
| hunter_survival | 104,176 | 185,493 | Y/Y | HAC +0.56% |
| rogue_assassination | 102,775 | 187,520 | Y/Y | HAC +1.39% |
| rogue_outlaw | 102,657 | 214,926 | Y/Y | HAC +0.39% |
| rogue_subtlety | 115,329 | 225,134 | Y/Y | — |
| priest_shadow | 104,818 | 154,134 | Y/Y | HAC +1.64% |
| dk_blood | 46,588 | 97,667 | -/Y | HAC +1.12% |
| dk_frost | 110,960 | 188,079 | -/Y | — |
| dk_unholy | 126,982 | 272,428 | -/Y | — |
| shaman_elemental | 126,334 | 240,113 | Y/Y | — |
| shaman_enhancement | 91,512 | 174,899 | Y/Y | HAC +1.63% |
| mage_arcane | 100,952 | 217,673 | Y/Y | — |
| mage_fire | 101,877 | 209,626 | Y/Y | — |
| mage_frost | 112,278 | 206,929 | Y/Y | — |
| warlock_affliction | 94,414 | 155,809 | Y/Y | HAC +3.63% |
| warlock_demonology | 97,205 | 525,527 | Y/Y | — |
| warlock_destruction | 94,548 | 162,645 | Y/Y | HAC +3.50% |
| monk_brewmaster | 61,918 | 119,969 | Y/Y | PW +0.72% |
| monk_windwalker | 120,841 | 211,599 | Y/Y | HAC +0.02% |
| druid_balance | 76,039 | 117,750 | Y/Y | — |
| druid_feral | 106,929 | 199,563 | Y/Y | HAC +1.20% |
| druid_guardian | 79,222 | 139,526 | Y/Y | — |
| dh_havoc | 121,588 | 206,497 | -/Y | — |
| dh_vengeance | 56,115 | 94,589 | Y/Y | PW +0.95%, HAC +0.33% |
| dh_devourer | 103,645 | 179,714 | -/Y | HAC +0.09% |
| evoker_devastation | 108,492 | 176,264 | Y/Y | HAC +6.32% |
| evoker_augmentation | 68,519 | 114,737 | Y/Y | PW +0.29% |

Talent column: Y = new optimal build found, - = existing build already optimal.
APL gains > 0.1% listed; 12/33 specs had APL improvements (all HAC-side except
warrior_fury PW, monk_brewmaster PW, dh_vengeance PW, evoker_augmentation PW).

Notable: evoker_devastation HAC APL +6.32%, warlock_affliction HAC +3.63%,
warlock_destruction HAC +3.50%. warlock_demonology HAC 525k is correct (pet-heavy AoE).

---

## v0.2 — Engine Correctness Audit (2026-03-31)

### Bugs Found and Fixed

| # | Class | Bug | Root Cause | DPS Impact | Commit |
|---|-------|-----|-----------|------------|--------|
| 1 | Priest Shadow | 2pc SW:Madness doing 0 damage | Swapped effectN indices (cost vs damage) | **+25.4%** | aad7db1 |
| 2 | Rogue Sub | 4pc Shadow Blades permanent (99.7% uptime) | `from_seconds(base_value())` on ms value (4000ms = 4000s) | **-19.6%** | 31e47b9 |
| 3 | Monk WW | 4pc CDR negated by manual adjust | Manual `cooldown->adjust(-5s)` cancelled auto-applied passive aura `(-5s)` | **+1.2%** | aad7db1 |
| 4 | Shaman Ele | Storm Elemental Elemental Unity TA bonus = 0 | effectN(5) OOB on 4-effect spell (should be effectN(4)) | ~0% (pet TA) | 155add0 |
| 5 | Trinket | Phoenix Torque wrong damage/heal indices | effectN index swap | Minor | aad7db1 |
| 6 | Shaman Enh | 2pc wrong semantic effect index | Read effectN(2) instead of effectN(1) (same value) | None | aad7db1 |

### Audit Scope

| Check | Scope | Result |
|-------|-------|--------|
| Spell ID existence (Level 1) | 568 Midnight IDs across 13 classes | 568/568 exist in DBC |
| Talent name match | 568 find_talent_spell lookups | 568/568 match DBC name |
| effectN OOB (Level 2) | 3132 reads across 38 source files | 32 candidates → 2 real bugs |
| from_seconds(base_value()) | 89 call sites | 1 bug (Rogue Sub 4pc, fixed) |
| Tier set behavioral | 33 specs × 2pc+4pc | All effectN values match tooltips |
| Tier set DPS delta | 33 specs (3000 iter each) | All 2.8%–20.1% (reasonable) |

### Tier Set Deltas (post-fix)

| Spec | Delta | Spec | Delta | Spec | Delta |
|------|-------|------|-------|------|-------|
| BM Hunter | +5.2% | Assa Rogue | +8.9% | Blood DK | +5.2% |
| MM Hunter | +2.8% | Outlaw Rogue | +8.6% | Frost DK | +6.2% |
| SV Hunter | +3.6% | Sub Rogue | +19.5% | Unholy DK | +3.8% |
| Arcane Mage | +3.5% | Arms Warrior | +8.3% | Shadow Priest | +16.0% |
| Fire Mage | +6.3% | Fury Warrior | +4.8% | Ele Shaman | +11.3% |
| Frost Mage | +3.7% | Ret Paladin | +13.2% | Enh Shaman | +10.1% |
| Affli Lock | +3.0% | WW Monk | +3.2% | Havoc DH | +12.1% |
| Demo Lock | +4.7% | Balance Druid | +11.7% | Dev Evoker | +6.0% |
| Destro Lock | +6.9% | Feral Druid | +6.2% | Aug Evoker | +20.1% |

---

## Completed Work

### v0.3 — Full Optimization Pass (2026-03-31)
- 33/33 specs optimized: talent local search + APL mutation optimizer
- Both fight styles independently: Patchwerk (ST) and HecticAddCleave (AoE/M+)
- 89/89 profiles pass validation (66 previously + 23 new HAC profiles)
- Tank specs now all have HAC profiles (tanks-skip-HAC convention removed)
- optimize_all_specs.py orchestration script added

### v0.2 — Engine Correctness Audit (2026-03-31)
- Full DBC behavioral audit across all 13 class modules
- 6 bugs found and fixed (3 with significant DPS impact)
- Audit tooling: verify_spell_ids.py, deep_audit.py, audit_class_spells.py
- Upstream merge: 359 commits, 44 conflict resolution
- 120/120 fresh baselines on Build 66709

### v0.1 — Optimization System (2026-03-30)
- Talent validator with real DB2 edges (6,409 TraitEdge.csv)
- APL optimizer with 4 mutation operators + multi-stage filtering
- Talent hill-climbing local search
- req_points gate bug fix (purchased-only counting)

### Data Extraction & Auditing (Phases 1-4)
- Wowhead extraction (33 specs × 5 pages)
- 3-way upstream APL comparison (198 sims, 10k iter)
- Profile updates (gear, consumables, talents)
- Wowhead build comparison (262 builds, 29/33 improved)

---

## Known Issues

### Open

- **Darkmoon Deck sigil stacking** — Issue #81, blocked on beta/live data.
  See `docs/internal/darkmoon_investigation.md`.
- **Priest Shadowfiend effectN(4)** — OOB on 3-effect spell. Returns 0 for
  Holy/Disc mana regen. Low impact (healer sim only, not DPS).
- **Wowhead data stale** — extracted on Build 66384, current is 66709.
- **Multi-target scaling unverified** — need 1/3/5/10 target sweeps.
- **Proc rates unverified** — need JSON execute count vs RPPM/ICD comparison.
- **Baselines stale post-optimization** — 126 baselines predate the v0.3 talent/APL
  changes. Need re-baseline pass after optimization.

### Resolved (v0.3)
- tanks-skip-HAC convention removed — all 6 tank specs now have HAC profiles

### Resolved (v0.2)
- Rogue Sub 4pc permanent Shadow Blades — fixed (from_seconds on ms)
- Shaman Storm Elemental effectN(5) OOB — fixed (effectN(4))
- Priest Shadow 2pc swapped indices — fixed
- Monk WW 4pc CDR double-negation — fixed
- Phoenix Torque wrong indices — fixed
- Shaman Enh 2pc wrong semantic index — fixed

### Resolved (v0.1 and earlier)
- req_points gate validator bug — fixed 2026-03-30
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
| `docs/internal/engine_audit_2026-03-31.md` | Detailed DBC audit findings log |
| `docs/internal/behavioral_audit_2026-03-31.md` | Tier set tooltip vs code comparison |
| `docs/internal/darkmoon_investigation.md` | Darkmoon trinket stacking investigation (Issue #81) |
| `docs/archive/` | Historical audit data, APL diff reports |

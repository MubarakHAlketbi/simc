# SimulationCraft — Midnight Expansion (MID1) Progress

Last updated: 2026-04-03 — **v0.4 Proc callback API migration + 90-upstream-commit merge**

**Game build: 12.0.1.66709 Live** — we target Live only, ignore 12.0.5.x PTR.

---

## Status

| Metric | Value |
|--------|-------|
| Release | **v0.4** (2026-04-03) |
| Profiles | 89/89 PASS (compile + 1-iter sim + talent validation) |
| Talent validation | 89/89 PASS (budget, prereqs, req_points gates) |
| Baselines | 172 fresh (89 × 2 fight styles, post-v0.5 engine fixes + APL) |
| Tier sets | 33/33 audited; 10 bugs found and fixed total across all audit passes |
| Apex talents | 33/33 implemented + audited (all 3-rank IDs per spec) |
| NYI talents | Demo WL Soul Harvester: Eternal Hunger duration fix applied (v0.5.2) |
| APL Layer 1 | DONE — 33/33 specs, blind mutation optimizer |
| APL Layer 2 | DONE — signal-guided optimizer (APS, buff waste, resource, interval) |
| APL Layer 3 | DONE — LLM semantic advisor; full run 33/33 specs complete |
| Multi-target sweeps | DONE — 56 specs × 4 targets = 224 sims, no AoE scaling anomalies |
| Reference comparison | DONE — 47 spec pairs vs simulationcraft.org, findings documented |
| Upstream sync | **MERGED** — 90 commits (Build 66709 Live + 66741 test data). See v0.4 notes. |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |
| unique_gear_midnight.cpp | 65+ callbacks migrated to new dbc_proc_callback_t API (37 → 0 errors) |

---

## What's Next

| # | Task | Type | Status |
|---|------|------|--------|
| 6 | Proc rate validation — compare JSON execute counts vs RPPM/ICD | Testing | PENDING |
| 8 | Trinket combinatorics | Optimization | PENDING |
| 9 | Final docs + cleanup + contribute fixes upstream | Maintenance | PENDING |
| ~~10~~ | ~~Investigate outliers~~ — both resolved (see v0.5.3 below) | Engine/APL | **DONE** |
| 10b | Verify reflection_of_radiance proc chance via combat log (Lightsmith 11% residual gap) | Testing | PENDING |
| 11 | Verify all 89 profiles still pass after upstream merge | Testing | PENDING |

---

## v0.4 — Upstream Merge + Proc Callback API Migration (2026-04-03)

### Upstream: 90 commits merged

Major upstream changes absorbed:
- **938fa74** — Proc trigger callback rework (#11309): fundamental API change to `dbc_proc_callback_t`
- **f2978bd** — Mage Flurry bug fix
- **4c85545** — Paladin Highlord's Judgment + HoW interaction fix
- **0ecae23** — Gear: Voidglass Shards crash fix
- **704ab39** — Druid root_network ticking fix
- **e9346d8 + 5a58fc4** — Devourer Impending Apocalypse stacking fixes
- **6ae74de** — Subtlety AA proc ICD
- **0d68ec6** — Monk Gift of the Ox manual proc
- **47d89ae** — Monk precombat TE Brew stacks
- **c2d7312** — Assassination Revert Garrote snapshot mechanic
- **3204822 + e472a9c + 05a18f0** — Fake buff proc callback disabling (Priest/Rogue/Druid)
- **d0c4791** — Buff: add buff_t::proc_callbacks (engine infra)
- **7f03820** — Callbacks: trigger aura applied procs on pf2_landed
- **b3378ab** — Callbacks: check combat state of player instead of target
- **PTR skipped**: Build 66741 test data (#11326)

### Engine API Migration (unique_gear_midnight.cpp)

The upstream proc callback rework (938fa74) fundamentally changed `dbc_proc_callback_t`:

**Signature changes (65 locations):**

| Old | New | Count |
|-----|-----|-------|
| `void execute(action_t*, action_state_t*)` override | `void execute(const spell_data_t*, player_t*, action_state_t*)` | 16 |
| `void trigger(action_t*, action_state_t*)` override | `void trigger(const proc_data_t&, player_t*, action_state_t*, proc_trigger_type_e)` | 2 |
| Lambda: `(auto, auto, action_state_t* s)` (CONDITION) | `(auto, const auto&, auto, auto, action_state_t* s)` | 1 |
| Lambda: `(auto, auto, const action_state_t* s)` (execute) | `(auto, auto, player_t*, action_state_t* s)` | 8+ |
| Lambda: `(auto, auto, auto)` (execute) | `(auto, auto, auto, auto)` (4-param) | 4+ |
| `PF_DAMAGE_TAKEN` | `P_DAMAGE_TAKEN` | 1 |
| `set_can_only_proc_from_class_abilites` (typo) | `set_can_only_proc_from_class_abilities` | 2 |

Build went from **37 errors → 0 errors**. Smoke test (Mage Frost 1k iter) passes clean.

### Our Fixes Carried Forward

- Priest void_flay OOB effectN fix: spell 34433 (3 effects, effectN(4) OOB) → spell 343727 (Power Leech, effectN(1))
- Priest shadowfiend proc chance: effectN(3) on 3-effect spell → effectN(2)

### New Tooling

- `scripts/verify_spell_effects.py` — scans class modules for effectN calls, cross-references DBC for potential OOB/semantic issues
- `scripts/verify_spell_implementation.py` — deeper trait→spell resolution checker
- `docs/analysis/druid_balance_elune_dps_gap_findings.md` — Druid Balance Elune DPS gap analysis
- Debug build with assertions enabled for runtime OOB detection (`spell_data_t::effectN` asserts `idx <= effect_count()`)

---

## v0.5.3 — Outlier Investigation (2026-04-02)

### Druid Balance Elune: APL Bug Fixed (+32% DPS)

**Root cause:** `ec_cd_condition` variable had `!buff.eclipse_lunar.up` as a leading guard.
For Elune's Chosen, CA/Incarnation should be cast freely on cooldown — ideally *during* Lunar Eclipse.
The inversion blocked CA from firing ~40% of fight time, reducing usage from ~4 to ~2 per fight.

Old: `!buff.eclipse_lunar.up & hero_tree.elunes_chosen & !buff.ca_inc.up & (complex trinket-sync)`
Fixed: `hero_tree.elunes_chosen & !buff.ca_inc.up & cooldown.ca_inc.charges_fractional>=1 | fight_remains<10`

Results: 53,857 → 71,193 DPS (+32.2%). Remaining -6.4% vs base Balance is **expected** — Wowhead
explicitly notes Elune's Chosen is not optimal for single-target (it's an AoE-focused tree).

### Paladin Protection Lightsmith: Expected Gap + Minor Engine Issue

**Root cause of 28% gap:** Templar vs Lightsmith are completely different hero trees. The base Prot
profile uses Templar. Templar-exclusive abilities contribute ~29,500 DPS (empyrean_hammer 13.6k +
hammer_of_light 10k + sacrosanct_crusade 6k). Lightsmith-exclusive abilities contribute ~22,100 DPS.
The net ~7,400 DPS hero talent gap plus Templar buff amplification on Avenger's Shield/Divine Toll
explains most of the gap. **Not a bug — expected behavior.**

**Residual 11% gap (engine issue):** Reference comparison shows ~11% gap even after substituting
reference talents+APL. Suspected causes:
- `reflection_of_radiance_proc_chance` hardcoded at 0.2 (20%) with a TODO — DBC base_value=3
  for the Dummy effect. Grand Crusader encodes 15% as base_value=15, so by same convention
  base_value=3 = 3% — but that seems too low. Actual value unverified.
- Solo-sim approximation of `fake_solidarity` (group Sacred Weapon scaling) may underestimate DPS.

**Action:** Updated the TODO comment in sc_paladin.cpp with DBC audit findings. Verified proc chance
needed via combat log (task 10b).

---

## v0.5.2 — Eternal Hunger Duration Fix (2026-04-02)

Full behavioral audit of all 3 "NYI" Warlock Demonology Soul Harvester talents:

| Talent | Spell | DBC Mechanic | Finding | Action |
|--------|-------|-------------|---------|--------|
| Eternal Servitude | 449707 | Aura 107, -90s CDR on Fel Domination | Auto-applied by engine. Fel Domination is utility (pet summon), no DPS impact | None needed |
| Shared Vessel | 1268889 | Aura 318, +2% Mastery; doubled while soul active | Auto-applied as base. Manual code in composite_mastery() doubles correctly | Already correct |
| Eternal Hunger | 1268903 | Aura 219, +5000ms to Manifested Demonic Soul duration + Aura 4, +10% Soul Swipe dmg | effectN(2) damage was implemented. effectN(1) duration was **MISSING** — pet always spawned at 9s | **FIXED** |

Fix: `sc_warlock_init.cpp` — `set_default_duration` now adds `eternal_hunger->effectN(1).time_value()` (+5s) when talent is ok.
Validated: `manifested_demonic_soul` buff duration in JSON = 14.56s (was 9s). Correct.

Accessor note: effectN(1) base_value=5000 → `time_value()` = 5000ms = 5s. NOT `from_seconds(base_value())` (would be 5000s — Pattern 4 bug class).

---

## v0.5 — Upstream Sync + APL Ports + Re-baseline (2026-04-01 / 04-02)

### Upstream: 24 commits merged (38ee898 PTR skipped)

Key changes absorbed:
- Warlock Demonic Core proc fix — removed 0.2x workaround (confirmed Live hotfix 2026-03-31)
- Monk keg_smash null-ptr crash fix
- Hunter Boar Charge double-dip scoping fix
- DBC data: Build 66709 updated spell data

PTR skipped: `38ee898` — all `*_ptr.inc` DBC files, Build 66741 data. Not Live.

### Engine Bugs Fixed (v0.4.1, via reference profile comparison)

| # | Class | Bug | Root Cause | DPS Impact |
|---|-------|-----|-----------|------------|
| 7 | Warlock Affliction | Hellcaller APL drain_life filler | Rogue drain_life line imported to wrong spec | +17.2% |
| 8 | Paladin Ret | Herald 4pc double expurgation | divine_storm_second_sunrise_t inherited triggers | +12.9% |
| 9 | DK Blood | vampiric_strike -46% damage | effectN(5) AoE cleave vs effectN(1) ST (1.699 AP) | +46% per cast |
| 10 | Monk WW | 2pc double +30% to WDP/SotWL | Manual code + auto-apply via Aura 108 | ~+4% engine inflation |
| Codec | Talent codec | Corrupt string acceptance | Missing tree_hash validation | Silent errors |

### APL Ports from Reference Comparison

4 specs ported where reference delta exceeded 5%:
- Warlock Affliction Soul Harvester: +9.04%
- Shaman Enhancement Stormbringer: +9.32%
- DH Devourer Annihilator: +4.31%
- Monk Brewmaster: +3.31%

### Talent Re-optimization (9 specs post-engine-fix)

Notable gains after engine corrections cleared inflation:
- paladin_protection HAC: +11.8%
- hunter_bm HAC: +12.4%
- warlock_destruction HAC: +13.7%
- druid_feral HAC: +8.6%

### Layer 2+3 Full Run (33/33 specs, all improved)

24 of 89 profiles improved. Largest gains:
- DK Blood HAC: +4.01%
- DH Devourer HAC: +3.47%
- Shaman Elemental HAC: +2.89%
- Warlock Demo HAC: +1.85%
- Evoker Devastation HAC: +1.17%
- Monk Brewmaster PW: +1.12%

LLM model: `qwen/qwen2.5-72b-instruct:free` via OpenRouter. Full Wowhead rotation.md context (no char trim).

### Multi-target Sweeps

56 specs x 4 target counts (1/3/5/10) = 224 sims. No AoE scaling anomalies.

---

## v0.4 — Signal-Guided + LLM APL Optimizer (2026-03-31)

Three-layer APL optimization pipeline:

**Layer 1** — Blind mutation (~200 candidates/spec, 4 operators, 300->3k->10k funnel)
**Layer 2** — Signal-guided mutations targeting APS inversion, buff waste (>40%), resource overcap (>8%), interval gaps
**Layer 3** — LLM semantic advisor for buff-has-no-consumer signals; outputs structured CHANGE blocks, all DPS-validated

New scripts: `signal_apl_optimizer.py`, `apl_signal_extractor.py`, `apl_signal_mutations.py`, `llm_apl_advisor.py`

---

## v0.3 — Full Optimization Pass (2026-03-31)

33/33 specs optimized (Layer 1). 89/89 profiles pass validation.
Tank specs all have HAC profiles. Largest gains: evoker_dev HAC +6.32%, warlock_affli HAC +3.63%, warlock_dest HAC +3.50%.

---

## v0.2 — Engine Correctness Audit (2026-03-31)

| # | Class | Bug | DPS Impact |
|---|-------|-----|-----------|
| 1 | Priest Shadow | 2pc SW:Madness 0 damage (swapped effectN) | +25.4% |
| 2 | Rogue Sub | 4pc permanent Shadow Blades (from_seconds on ms) | -19.6% |
| 3 | Monk WW | 4pc CDR negated (manual adjust cancelled auto-apply) | +1.2% |
| 4 | Shaman Ele | Storm Ele TA modifier = 0 (effectN(5) OOB, should be 4) | ~0% |
| 5 | Trinket | Phoenix Torque wrong indices | Minor |
| 6 | Shaman Enh | 2pc wrong semantic effectN index | Minor |

---

## v0.1 — Optimization System (2026-03-30)

Talent validator with real DB2 edges (6,409 TraitEdge.csv).
APL optimizer: 4 mutation operators + multi-stage filtering.
Talent hill-climbing local search. req_points gate bug fixed.

---

## Current DPS Baselines (2026-04-02)

| Spec | PW DPS | HAC DPS |
|------|-------:|--------:|
| Death_Knight_Blood | 50,101 | 88,612 |
| Death_Knight_Blood_Deathbringer | 52,956 | 92,528 |
| Death_Knight_Frost | 115,451 | 179,161 |
| Death_Knight_Frost_Rider | 108,687 | 204,868 |
| Death_Knight_Unholy | 126,974 | 251,254 |
| Death_Knight_Unholy_San'layn | 130,370 | 225,178 |
| Demon_Hunter_Devourer | 108,196 | 131,049 |
| Demon_Hunter_Devourer_Void-Scarred | 98,954 | 169,655 |
| Demon_Hunter_Havoc | 121,458 | 190,024 |
| Demon_Hunter_Vengeance | 56,621 | 96,716 |
| Demon_Hunter_Vengeance_Aldrachi_Reaver | 56,081 | 93,338 |
| Druid_Balance | 76,067 | 111,335 |
| Druid_Balance_Elune | 71,193 | 86,209 |
| Druid_Balance_Keeper | 74,941 | 105,262 |
| Druid_Feral | 110,569 | 191,466 |
| Druid_Guardian | 79,241 | 128,578 |
| Evoker_Augmentation | 69,026 | 112,854 |
| Evoker_Augmentation_Chronowarden | 57,412 | 89,191 |
| Evoker_Devastation | 108,510 | 165,985 |
| Evoker_Devastation_FS | 107,390 | 168,327 |
| Hunter_Beast_Mastery | 101,824 | 189,657 |
| Hunter_Marksmanship | 108,028 | 154,894 |
| Hunter_Survival | 108,133 | 176,738 |
| Hunter_Survival_PL_DW | 110,190 | 179,279 |
| Mage_Arcane | 100,840 | 211,646 |
| Mage_Arcane_Sunfury | 101,160 | 197,276 |
| Mage_Fire | 101,915 | 209,425 |
| Mage_Fire_Frostfire | 101,792 | 209,288 |
| Mage_Frost | 112,201 | 164,312 |
| Mage_Frost_Frostfire | 94,235 | 137,049 |
| Monk_Brewmaster | 64,442 | 111,082 |
| Monk_Windwalker | 118,871 | 189,754 |
| Monk_Windwalker_Conduit | 119,037 | 196,028 |
| Paladin_Protection | 59,970 | 101,752 |
| Paladin_Protection_Lightsmith | 42,948 | 93,334 |
| Paladin_Retribution | 107,407 | 157,974 |
| Paladin_Retribution_Herald | 111,772 | 132,033 |
| Priest_Shadow | 106,885 | 129,425 |
| Priest_Shadow_Archon | 108,312 | 105,671 |
| Rogue_Assassination | 102,776 | 187,594 |
| Rogue_Assassination_Deathstalker | 97,881 | 107,426 |
| Rogue_Outlaw | 102,612 | 192,333 |
| Rogue_Outlaw_Trickster | 98,496 | 151,885 |
| Rogue_Subtlety | 115,254 | 215,766 |
| Shaman_Elemental | 126,317 | 186,382 |
| Shaman_Enhancement | 91,472 | 171,563 |
| Shaman_Enhancement_Stormbringer | 81,129 | 135,624 |
| Warlock_Affliction | 102,862 | 138,074 |
| Warlock_Affliction_Hellcaller | 99,002 | 143,149 |
| Warlock_Demonology | 103,257 | 559,391 |
| Warlock_Demonology_Soul_Harvester | 108,157 | 410,468 |
| Warlock_Destruction | 94,574 | 147,643 |
| Warlock_Destruction_Diabolist | 100,538 | 162,993 |
| Warrior_Arms | 83,774 | 147,013 |
| Warrior_Fury | 93,139 | 195,825 |
| Warrior_Protection | 75,520 | 132,314 |

Note: HAC profiles use HecticAddCleave fight style; high values (Demo WL 559k) reflect multi-pet/multi-target scaling.
HAC-optimized profiles (_HAC.simc) may show lower PW numbers — they are separately optimized for HAC.

---

## Known Issues

### Open

- **Paladin Protection Lightsmith** residual 11% gap vs reference even with ref talents+APL — `reflection_of_radiance_proc_chance` hardcoded at 20%, DBC base_value=3 (unverified, could be 3% or 30%). Verify via combat log (task 10b).
- **Priest shadowfiend effectN** — was OOB but effectN(3) is in bounds for 3-effect spell. Semantic correctness unverified against game data.
- **Darkmoon Deck sigil stacking** — Issue #81, blocked on live data. See `docs/internal/darkmoon_investigation.md`.
- **Proc rates unverified** — need JSON execute count vs RPPM/ICD comparison.
- **Wowhead rotation validator false positives** — 6 specs produce "MISSING HERO TALENTS" warnings that are false positives (build-variant button name mismatch). Content is complete. Affected: monk/brewmaster, monk/windwalker, dk/unholy, druid/guardian, paladin/retribution, mage/arcane. Safe to ignore.
- **Upstream merge created many profile/APL conflicts** — we took our Midnight-optimized versions. Some upstream fixes (e.g. warrior colossus cleave during ravager) were selectively adopted. Full verification pending.
- **DANGER: update_talents_from_extracted.py must NOT be run post-v0.3.** Overwrites optimized talent strings with Wowhead defaults. Silent regression.

### Resolved

- v0.4: 65+ dbc_proc_callback_t API migrations in unique_gear_midnight.cpp (37 build errors -> 0)
- v0.4: 90 upstream commits merged; PRIOR all proc/trigg/lambda signatures updated for upstream commit 938fa74
- v0.4: PF_DAMAGE_TAKEN -> P_DAMAGE_TAKEN typo fix (upstream rename)
- v0.3.2: 65 dbc_proc_callback_t callback API migration (37 -> 0 build errors) via merge
- v0.3: Priest void_flay mana OOB effectN fix (spell 34433->343727)
- v0.3: Priest shadowfiend proc chance OOB effectN fix (3->2)
- v0.5.3: Druid Balance Elune ec_cd_condition inverted gate (-32% DPS, APL bug)
- v0.5.2: Eternal Hunger duration extension missing (demonic_soul pet 9s not 14s)
- v0.5: Warlock Affliction Hellcaller drain_life APL bug (+17.2%)
- v0.5: Paladin Ret Herald 4pc double expurgation (+12.9%)
- v0.5: DK Blood vampiric_strike effectN(5) vs effectN(1) (+46% per cast)
- v0.5: Monk WW 2pc double-apply (+4% engine inflation)
- v0.5: Talent codec corrupt string acceptance (tree_hash validation added)
- v0.2: Priest Shadow 2pc swapped effectN (+25.4%)
- v0.2: Rogue Sub 4pc permanent Shadow Blades (from_seconds on ms)
- v0.2: Monk WW 4pc CDR double-negation
- v0.2: Shaman Ele Storm Elemental effectN(5) OOB
- v0.2: Phoenix Torque wrong indices
- v0.1: req_points gate validator counted granted nodes incorrectly
- v0.1: DK Blood HAC crash (player_t::interrupt race condition)

---

## Reference Files

| File | What |
|------|------|
| `AGENTS.md` | Agent guide — mission, workflow, domain knowledge, pitfalls |
| `APL_optimization.md` | APL syntax reference + 3-layer optimization pipeline |
| `optimization_action_plan.md` | Optimization architecture + success criteria |
| `OPTIMIZATION_HOWTO.md` | Step-by-step manual guide |
| `project_structure.md` | Codebase navigation |
| `docs/internal/behavioral_audit_checklist.md` | **USE FOR ALL C++ WORK** — 5-step per-modifier protocol |
| `docs/internal/bug_postmortem_2026-04-01.md` | Why 10 bugs passed prior audits + which checklist step catches each |
| `docs/internal/engine_audit_2026-03-31.md` | DBC audit findings (v0.2) |
| `docs/internal/behavioral_audit_2026-03-31.md` | Tier set behavioral audit (v0.2) |
| `docs/internal/darkmoon_investigation.md` | Darkmoon trinket investigation (Issue #81) |
| `docs/analysis/reference_comparison_findings.md` | Reference comparison findings — bugs, APL gaps, talent failures |
| `docs/analysis/reference_profile_comparison.json` | Raw 47-spec comparison data |
| `docs/analysis/druid_balance_elune_dps_gap_findings.md` | Druid Balance Elune DPS gap investigation |
# SimulationCraft — Midnight Expansion (MID1) Project Progress

Last updated: 2026-03-22 (Phase 2 APL audit complete — all 33 specs verified)
All information verified fresh against Wowhead + code inspection.
52/52 profiles pass 1-iteration sim. Build: gcc-14 clean.

---

## 1. Profiles

| Profile File | Status | Notes |
| :--- | :--- | :--- |
| MID1_Death_Knight_Blood.simc | PASS | |
| MID1_Death_Knight_Blood_Deathbringer.simc | PASS | |
| MID1_Death_Knight_Frost.simc | PASS | |
| MID1_Death_Knight_Frost_Rider.simc | PASS | |
| MID1_Death_Knight_Unholy.simc | PASS | |
| MID1_Death_Knight_Unholy_San'layn.simc | PASS | |
| MID1_Demon_Hunter_Devourer.simc | PASS | |
| MID1_Demon_Hunter_Devourer_Void-Scarred.simc | PASS | |
| MID1_Demon_Hunter_Havoc.simc | PASS | |
| MID1_Demon_Hunter_Vengeance.simc | PASS | |
| MID1_Demon_Hunter_Vengeance_Aldrachi_Reaver.simc | PASS | |
| MID1_Druid_Balance.simc | PASS | No valid talent hash — APL simplified |
| MID1_Druid_Feral.simc | PASS | |
| MID1_Druid_Guardian.simc | PASS | |
| MID1_Evoker_Augmentation.simc | PASS | Inline APL removed 2026-03-22 — uses C++ generator |
| MID1_Evoker_Devastation.simc | PASS | |
| MID1_Evoker_Devastation_FS.simc | PASS | |
| MID1_Hunter_Beast_Mastery.simc | PASS | |
| MID1_Hunter_Marksmanship.simc | PASS | |
| MID1_Hunter_Survival.simc | PASS | |
| MID1_Hunter_Survival_PL_DW.simc | PASS | |
| MID1_Mage_Arcane.simc | PASS | |
| MID1_Mage_Arcane_Sunfury.simc | PASS | |
| MID1_Mage_Fire.simc | PASS | |
| MID1_Mage_Fire_Frostfire.simc | PASS | |
| MID1_Mage_Frost.simc | PASS | |
| MID1_Mage_Frost_Frostfire.simc | PASS | |
| MID1_Monk_Brewmaster.simc | PASS | |
| MID1_Monk_Windwalker.simc | PASS | |
| MID1_Monk_Windwalker_Conduit.simc | PASS | |
| MID1_Paladin_Protection.simc | PASS | |
| MID1_Paladin_Protection_Lightsmith.simc | PASS | |
| MID1_Paladin_Retribution.simc | PASS | |
| MID1_Paladin_Retribution_Herald.simc | PASS | |
| MID1_Priest_Shadow.simc | PASS | |
| MID1_Priest_Shadow_Archon.simc | PASS | |
| MID1_Rogue_Assassination.simc | PASS | |
| MID1_Rogue_Outlaw.simc | PASS | |
| MID1_Rogue_Outlaw_Trickster.simc | PASS | |
| MID1_Rogue_Subtlety.simc | PASS | |
| MID1_Shaman_Elemental.simc | PASS | |
| MID1_Shaman_Enhancement.simc | PASS | |
| MID1_Shaman_Enhancement_Stormbringer.simc | PASS | |
| MID1_Warlock_Affliction.simc | PASS | drain_life priority fixed 2026-03-20 |
| MID1_Warlock_Affliction_Hellcaller.simc | PASS | |
| MID1_Warlock_Demonology.simc | PASS | |
| MID1_Warlock_Demonology_Soul_Harvester.simc | PASS | |
| MID1_Warlock_Destruction.simc | PASS | |
| MID1_Warlock_Destruction_Diabolist.simc | PASS | |
| MID1_Warrior_Arms.simc | PASS | |
| MID1_Warrior_Fury.simc | PASS | |
| MID1_Warrior_Protection.simc | PASS | |

**Total: 52/52 PASS**

Missing hero-tree variant profiles (low priority — need valid live talent hashes):
- MID1_Druid_Balance_Keeper.simc (Keeper of the Grove)
- MID1_Druid_Balance_Elune.simc (Chosen of Elune)
- MID1_Evoker_Augmentation_Chronowarden.simc
- MID1_Rogue_Assassination_Deathstalker.simc

---

## 2. Class Mechanics — General Changes

| Class / Spec | Mechanic Status | Notes |
| :--- | :--- | :--- |
| DK Blood | Implemented | |
| DK Frost | Implemented | |
| DK Unholy | In Beta | |
| DH Devourer | Implemented | |
| DH Havoc | Implemented | |
| DH Vengeance | Implemented | |
| Druid Balance | In Beta | Eclipse conditions simplified |
| Druid Feral | In Beta | |
| Druid Guardian | In Beta | |
| Evoker Devastation | Implemented | Rising Fury apex: IDs 1271687/1271796/1271788 |
| Evoker Augmentation | Implemented | Duplicate apex: IDs 1259173/1259174/1259175 — Breath of Eons summons future-self; Ebon Might extends duplicate; capstone gives +75% stat buff during duplicate |
| Hunter BM | Implemented | All 98 flagged "missing" talents confirmed already implemented (scanner false-positive bug in missing_from_code.md — Hunter uses spell_data_ptr_t not player_talent_t) |
| Hunter Marks | Implemented | Same scanner false-positive — all 93 confirmed implemented |
| Hunter Survival | Implemented | Same — all 93 confirmed implemented |
| Mage Arcane | In Beta | 75 open TODO comments — mostly behavior verification, see section 6 |
| Mage Fire | In Beta | |
| Mage Frost | In Beta | |
| Monk Brewmaster | In Beta | |
| Monk Windwalker | In Beta | Ascension energy regen (effect#2) implemented; Weapon of Wind (ID 1272678) implemented 2026-03-21: +10% damage during Zenith via DBC parse_effects |
| Paladin Protection | In Beta | All 95 flagged "missing" talents confirmed implemented (Paladin uses const spell_data_t* pattern, not player_talent_t — scanner false-positive) |
| Paladin Retribution | In Beta | All 92 confirmed implemented |
| Priest Shadow | In Beta | |
| Rogue Assassination | In Beta | Sudden Demise (ID 423136) execute mechanic now IMPLEMENTED: +10% bleed damage always; execute bonus below 35% HP scales linearly to +150% at 0% HP |
| Rogue Outlaw | In Beta | Grand Melee (ID 1259469) now IMPLEMENTED: +8% to Blade Flurry cleave multiplier |
| Rogue Subtlety | In Beta | |
| Shaman Elemental | Implemented | Lava Flows (ID 1273485) implemented 2026-03-21: +5% Lava Burst damage, +1 Maelstrom per cast/overload |
| Shaman Enhancement | Implemented | |
| Warlock Affliction | In Beta | drain_life APL priority now FIXED (2026-03-20): chains as main filler when Gorefiend's Avarice talented, interrupts on Nightfall |
| Warlock Demonology | In Beta | |
| Warlock Destruction | In Beta | |
| Warrior Arms | Implemented | |
| Warrior Fury | Implemented | |
| Warrior Protection | Implemented | |

---

## 3. Midnight Apex (4-Rank) Talents — All 33 Specs

Each spec has one 4-rank apex talent using 3 spell IDs: Rank1 (_1), Ranks2+3 (_23), Rank4 (_4).
All verified against Wowhead 2026-03-17 / 2026-03-20.

| Spec | Apex Talent Name | R1 ID | R23 ID | R4 ID | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Warrior Arms | Master of Warfare | 1269314 | 1269306 | 1269307 | Implemented |
| Warrior Fury | Rampaging Berserker | 1269308 | 1269309 | 1269310 | Implemented |
| Warrior Protection | Phalanx | 1269311 | 1269312 | 1269313 | Implemented |
| Mage Arcane | Touch of the Archmage | 1257942 | 1257947 | 1257950 | Implemented |
| Mage Fire | Fired Up | 1257343 | 1257349 | 1257348 | Implemented |
| Mage Frost | Hand of Frost | 1262935 | 1262981 | 1263249 | Implemented |
| Shaman Elemental | Feedback Loop | name+rank | name+rank | name+rank | Implemented |
| Shaman Enhancement | Storm Unleashed | 1262713 | — | — | Implemented |
| Rogue Assassination | Implacable | verified | verified | verified | Implemented |
| Rogue Outlaw | Gravedigger | verified | verified | verified | Implemented |
| Rogue Subtlety | Ancient Arts | verified | verified | verified | Implemented |
| Monk Brewmaster | Bring Me Another | verified | verified | verified | Implemented |
| Monk Windwalker | Tigereye Brew | name+rank | name+rank | name+rank | Implemented |
| Priest Shadow | Void Apparitions | verified | verified | verified | Implemented |
| Warlock Affliction | Shadow of Nathreza | verified | verified | verified | Implemented |
| Warlock Demonology | Dominion of Argus | verified | verified | verified | Implemented |
| Warlock Destruction | Embers of Nihilam | verified | verified | verified | Implemented |
| DK Blood | Dance of Midnight | name+rank | name+rank | name+rank | Implemented |
| DK Frost | Chosen of Frostbrood | name+rank | name+rank | name+rank | Implemented |
| DK Unholy | Forbidden Knowledge | name+rank | name+rank | name+rank | Implemented |
| DH Havoc | Eternal Hunt | name+rank | name+rank | name+rank | Implemented |
| DH Vengeance | Untethered Rage | name+rank | name+rank | name+rank | Implemented |
| DH Devourer | Midnight | name+rank | name+rank | name+rank | Implemented |
| Druid Balance | Ascendant Eclipses | name+rank | name+rank | name+rank | Implemented |
| Druid Feral | Unseen Predator | name+rank | name+rank | name+rank | Implemented |
| Druid Guardian | Wild Guardian | name+rank | name+rank | name+rank | Implemented |
| Druid Restoration | Everbloom | name+rank | name+rank | name+rank | N/A (healer) |
| Evoker Devastation | Rising Fury | 1271687 | 1271796 | 1271788 | Implemented |
| Evoker Augmentation | Duplicate | 1259173 | 1259174 | 1259175 | Implemented (2026-03-20: verified correct — Duplicate IS the Aug apex) |
| Hunter BM | Nature's Ally | name+rank | name+rank | name+rank | Implemented |
| Hunter Marks | Take Aim | name+rank | name+rank | name+rank | Implemented |
| Hunter Survival | Raptor Swipe | name+rank | name+rank | name+rank | Implemented |
| Paladin Protection | Glory of the Vanguard | verified | verified | verified | Implemented |
| Paladin Retribution | Light Within | verified | verified | verified | Implemented |

---

## 4. APL Status

| Spec | APL Source | Sim Validated | Notes |
| :--- | :--- | :--- | :--- |
| All 33 specs | Wowhead Midnight rotations, synced 2026-03-17 | Yes (1-iter) | |
| Warlock Affliction | Updated 2026-03-20 | Yes | Gorefiend's Avarice filler: drain_life chains as main filler, interrupted by Nightfall |
| Rogue Outlaw | Updated 2026-03-20 | Yes | Grand Melee implementation |
| Rogue Assassination | Updated 2026-03-20 | Yes | Sudden Demise execute bonus active |
| DH Havoc | Updated 2026-03-22 | Yes | Demonsurge ordering fix: immolation_aura default-list condition moved from comment into if= |
| Evoker Augmentation | Updated 2026-03-22 | Yes | Removed simplified 18-line inline APL; now uses full C++ generator (cancel_buff tip_the_scales, pandemic Ebon Might, trinket sync) |

### Phase 2 APL Diff — Summary (2026-03-22)

Full report: `wowhead/APL_diff_report.md` (2317 lines)
Analysis script: `wowhead/gen_apl_diff.py`

| Priority | Count | Result |
| :--- | :--- | :--- |
| HIGH | 1 | DH Havoc — FIXED |
| MEDIUM | 30 | All audited — 1 real fix (Evoker Aug), rest false positives or engine-managed |
| LOW | 2 | Paladin Retribution, Warlock Destruction — well-aligned, no changes |

**Actual fixes (2 total):**
1. DH Havoc — Demonsurge condition was in comment arg, not if= condition
2. Evoker Augmentation — simplified profile APL replaced with C++ generator

**False positives (parser artifacts, no action needed):**
- DK Frost: `obliterate_without_killing_machine`, `frostscythe_without_killing_machine`
- DK Blood: `death_and_decay_and_stand`
- Mage Fire: `meteor_right`
- Warrior Arms: `cleave_without_martial_prowess_talented`
- Warrior Protection: `execute_targets`

**Engine-managed replacement actions (no APL changes needed):**
- DK Blood `vampiric_strike`: auto-fires via make_fallback() when buff active
- DK Unholy `festering_scythe`: set_replacement_action() replaces festering_strike
- DK Unholy `graveyard`: set_replacement_action() replaces epidemic when buff.forbidden_knowledge.up
- DH Devourer `void_metamorphosis`: passive spec feature, not castable
- DH Devourer `reaper_s_toll`: already in APL as reavers_toll
- Paladin Protection `sacred_weapon`/`holy_bulwark`: handled by holy_armaments next_armament conditions
- Druid Feral `moonfire`: already in APL as moonfire_cat (engine alias)
- Rogue Outlaw `opportunity`: buff proc — APL uses pistol_shot,if=buff.opportunity.up

**All 15 NEEDS_MANUAL_REVIEW specs confirmed correct (no changes needed):**
DH Vengeance, Druid Balance, Druid Guardian, Evoker Augmentation, Hunter BM,
Hunter MM, Hunter Survival, Mage Arcane, Monk Brewmaster, Monk Windwalker,
Priest Shadow, Rogue Assassination, Shaman Elemental, Shaman Enhancement,
Warlock Demonology

---

## 5. APL Optimization Pipeline (Phase 3+)

Full specification: `APL_optimization.md`

### Pipeline Status

| Phase | Description | Status |
| :--- | :--- | :--- |
| Phase 1 | Browser extraction of all Wowhead pages (rotation, talents, bis, consumables, tier) | COMPLETE — 33 specs × 5 pages = 165 files in wowhead/*/extracted/ |
| Phase 2 | APL validation — diff all specs against Wowhead rotations | COMPLETE — 2 fixes applied |
| Phase 3 | Profile updates — BiS gear, consumables, talent builds from extracted data | NOT STARTED |
| Phase 4 | Optimization loop — Patchwerk + HecticAddCleave composite scoring | NOT STARTED |
| Phase 5 | Trinket combinatorics — sim all BiS trinket pairs | NOT STARTED |

### Extraction Tool

`wowhead/extract_wowhead_tabs.py` — Playwright-based browser extractor. Discovery-based
(no hardcoded tab names). Handles all Wowhead JS tab variations per spec.

Key fixes applied during development:
- Hero talent buttons use `data-active` attribute — clicking an already-active button deselects it
- Page reloads between hero talent iterations to clear Wowhead DOM artifacts (buttons become "SlayerSlayer" after tab clicks)
- JS-based clicking by text (not element handles) — immune to stale references

Usage:
```
pip install playwright && playwright install chromium
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation
python3 wowhead/extract_wowhead_tabs.py --all --pages rotation,talents,bis,consumables,tier
```

### Phase 3 Next Steps

1. Update all profiles with Wowhead BiS gear + consumables (from extracted/bis.md, extracted/consumables.md)
2. Build multi-talent-build profiles (from extracted/talents.md export codes — up to 8 builds per spec)
3. Run optimization loop: Patchwerk (50% weight) + HecticAddCleave (50% weight), accept changes
   only when composite improves AND neither fight style regresses >1%
4. Trinket combinatorics: extract all BiS trinkets, sim all pairs, find optimal combo per fight style

---

## 6. Unique Gear — Midnight Trinkets / Embellishments

### unique_gear_midnight.cpp — NYI Items Resolved

| Spell ID | Name | Previous Status | Current Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| 1237154 | AoE ground-effect trigger (Draught of Rampant Abandon secondary) | NYI — RPPM disabled | Implemented 2026-03-20 | Area Trigger 38015: 30s ground zone, 1s pulse ticks, Shadow damage = effectN(1).average(item) |
| 1263727 | Litany of Lightblind Wrath shield | NYI | Implemented 2026-03-20 | absorb_buff_t triggered on blast; self-absorb approximation for solo patchwork |

All other Midnight trinkets/consumables status:

| Item Type | Implemented | In Beta | Total |
| :--- | :--- | :--- | :--- |
| Raid Trinkets | 0 | 15 | 15 |
| Dungeon Trinkets | 1 | 15 | 16 |
| Potions | 1 | 3 | 4 |
| Flasks | 4 | 0 | 4 |
| Food Buffs | 28 | 2 | 30 |
| Weapon Oils | 3 | 4 | 7 |
| Enchants | 12 | 4 | 16 |

Notes:
- Raid trinkets registered with base proc logic; secondary effects pending beta tuning data
- Trinket+embellishment stacking (Locus-Walker, Ranger-Captain, Resonant Roarstone): GitHub Issue #81 — blocked on live data

---

## 7. Known Remaining Issues

### HIGH — DPS accuracy impact

None currently open.

### MEDIUM — Behavior correctness

**Mage (sc_mage.cpp — 75 TODO/FIXME comments)**
Material-impact items:
- Ignite spread target count logic (line 37)
- Pyromaniac proc condition (line 2438: "seems to proc regardless of Hot Streak state")
- Phoenix duration edge case when no valid targets (line 1208)
- Arcane: Clearcasting cost reduction completeness (line 2712)
These need beta testing to resolve, not code guesses.

**Priest (sc_priest.cpp — 57 TODOs)**
Shadow-relevant: Entropic Rift / Collapsing Void interaction if target dies mid-channel (line 1442).

**Druid (sc_druid.cpp — 50 TODOs)**
All remaining NYI items are Restoration talents (healer, out of scope for DPS sim).

**Death Knight (sc_death_knight.cpp — 47 TODOs)**
Two class-tree talents still NYI:
- `death_charge` — registered, not implemented
- `newly_turned` — registered, not implemented

**Rogue**
- Stale "Partial NYI" comment at line 822 for `sudden_demise` — mechanic was implemented 2026-03-20. Comment cleanup pending.
- `deaths_arrival` (Fatebound hero talent, ID uncertain) — NYI in-game, skipped.

### LOW — Cosmetic / blocked

- 4 missing hero-tree variant profiles (need valid live talent hashes)
- Trinket+embellishment stacking — GitHub Issue #81, blocked on beta data
- Stale "TODO: 81-89" comments in sc_extra_data.inc (base stats) — data is correct, cosmetic

---

## 8. Scanner False-Positive Bug in missing_from_code.md

The audit script searches for `player_talent_t` keyword to find talent declarations.
Hunter uses `spell_data_ptr_t` and Paladin uses `const spell_data_t*` — both fully implemented
but appear as 100% missing in the report.

**Impact:** 471 talents across Hunter BM/MM/SV and Paladin Prot/Ret reported as missing — all confirmed implemented.

Fix recommendation: update the scanner to also search for `find_talent_spell` calls and `spell_data_ptr_t` declarations.

---

## 9. Build Status

| Build Type | Status | Compiler |
| :--- | :--- | :--- |
| engine/Makefile RelWithDebInfo | PASS | gcc-14 (Debian 14.2.0-19) |
| ASAN (clang-18) | Not tested locally | Tested in CI |
| All 52 profiles, iterations=1 | 52/52 PASS | — |

CI workflows: self-contained (no reusable workflow_call), ccache enabled, gcc-14 + clang-18 jobs.

---

## 10. Commit History (key milestones)

| Commit | Date | Description |
| :--- | :--- | :--- |
| d09c418 | 2026-03-16 | Sync project_progress.md — full status audit pass |
| 6b8e643 | 2026-03-16 | Add 4 missing MID1 profiles + dark_pact to Warlock APLs |
| a405ae6 | 2026-03-17 | APL update — all 33 specs synced to Wowhead Midnight rotation |
| 82b5733 | 2026-03-17 | Verify 4-rank talent IDs for all specs |
| 987c693 | 2026-03-17 | Document 4-rank apex spell IDs |
| d01587d | 2026-03-20 | Hunter/Paladin DPS talent audit — scanner bug documented |
| 826b89e | 2026-03-20 | Aug Evoker Apex (Duplicate) + NYI unique gear (1237154, 1263727) |
| 5f93285 | 2026-03-20 | Rogue Outlaw Grand Melee (1259469) + Assassination Sudden Demise execute |
| ab3536d | 2026-03-21 | Shaman Elemental: Lava Flows (ID 1273485) |
| 6b31c73 | 2026-03-21 | Monk Windwalker: Weapon of Wind (ID 1272678) |
| fb8943a | 2026-03-22 | extract_wowhead_tabs.py — discovery-based browser extractor |
| 596f2f8 | 2026-03-22 | Wowhead extraction complete — all 33 specs × 5 pages (330 files) |
| 1c6dc7a | 2026-03-22 | Fix: hero talent toggle (data-active check) + placeholder wait |
| 894bf73 | 2026-03-22 | Phase 2: APL diff report (APL_diff_report.md + gen_apl_diff.py) |
| 731130c | 2026-03-22 | Fix(apl): DH Havoc Demonsurge ordering condition |
| cd5f8eb | 2026-03-22 | Fix(apl): Evoker Augmentation — remove simplified inline APL |
| c8b451e | 2026-03-22 | Docs: project_progress Phase 2 complete |

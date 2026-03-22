# SimulationCraft — Midnight Expansion (MID1) Project Progress

Last updated: 2026-03-22 (Batches 1–7 complete — full profile overhaul, NYI implementations, Phase 3 done, Phase 4 baselines run)
All information verified fresh against Wowhead + code inspection.
56/56 profiles pass 1-iteration sim. Build: gcc-14 clean.

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
| MID1_Druid_Balance.simc | PASS | talent= updated 2026-03-22 from Wowhead extraction |
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

**Total: 56/56 PASS**

4 new hero-tree variant profiles added 2026-03-22 (now in profile table above):
| MID1_Druid_Balance_Keeper.simc | PASS | Keeper of the Grove — Wowhead Build 1 talent string |
| MID1_Druid_Balance_Elune.simc | PASS | Chosen of Elune — Wowhead Build 1 talent string |
| MID1_Evoker_Augmentation_Chronowarden.simc | PASS | Chronowarden — talent-calc direct URL |
| MID1_Rogue_Assassination_Deathstalker.simc | PASS | Deathstalker — Wowhead Build 1 talent string |

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
|| Priest Shadow | Implemented | tormenting_whispers (ID 1250492) +15% SW:Madness implemented 2026-03-22; surge_of_insanity (ID 391399) +15% Mind Flay implemented 2026-03-22; deaths_torment (ID 1240364) was already implemented |
|| Rogue Assassination | In Beta | Sudden Demise (ID 423136) execute mechanic now IMPLEMENTED: +10% bleed damage always; execute bonus below 35% HP scales linearly to +150% at 0% HP |
|| Rogue Outlaw | In Beta | Grand Melee (ID 1259469) now IMPLEMENTED: +8% to Blade Flurry cleave multiplier |
|| Rogue Subtlety | In Beta | |
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
| Phase 3 | Profile updates — BiS gear, consumables, talent builds from extracted data | COMPLETE — consumables (30 profiles), gear BiS (19 profiles fixed), talents (46/56 updated via extractor + updater script) |
| Phase 4 | Optimization loop — Patchwerk + HecticAddCleave composite scoring | IN PROGRESS — baselines complete (56×2=112 JSON files in results/phase4/); permutation loop not yet run |
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

### Phase 3 Status (2026-03-22) — COMPLETE

**Consumables (DONE):** 30 profiles corrected — flask, potion, food match Wowhead Season 1.

**Gear BiS (DONE):** 19 profiles updated with correct item IDs sourced from Wowhead:
- DK Frost x2: hate_tied_waistchain (249380)
- DK Blood x2: eye_of_midnight/loa_worshipers_band rings, light_company_guidon trinket, garfrost weapon (133486), bent_gold_belt (133492)
- Priest Shadow x2: draconic_nullcape (249370), wraps_of_watchful_wrath (251108), dream_scorched_striders (249373), bond_of_light (249369), belomelorn weapon (249283)
- Warlock Affliction x2: whisper_inscribed_sash (249376), belomelorn
- Warlock Demo x2: whisper_inscribed, eye_of_midnight/signet_of_azerothian_blessings (241140), gaze/vaelgor trinkets, belomelorn
- Warlock Destro x2: whisper_inscribed, signet_of_azerothian, belomelorn
- Evoker Dev x2: darkstrider_treads (249377), locus_walkers_ribbon (249809)
- Evoker Aug + Chronowarden: horns_of_spurned_valkyr (133506), ribbon_of_coiled_malice (249337), enforcer_grips (249998), shadow_of_empyrean (249810), heart_of_wind (250256), ceremonial_hexblade (251178)
- Paladin Prot x2 + Warrior Prot: lights_march_bracers (249326), ezzoraks_gloombind, eye_of_midnight, band_of_triumvirate (151311), gaze/heart_of_ancient_hunger trinkets, thalassian_dawnguard (249921)

**Talent Strings (DONE — extractor upgraded):**
- extract_wowhead_tabs.py upgraded with get_talent_links() — scrapes `<a href>` talent-calc/blizzard/ codes from rendered DOM
- update_talents_from_extracted.py written — auto-updates talents= lines from extracted codes
- All 33 specs re-extracted; 46/56 profiles updated with fresh Wowhead build codes; 6 already correct; 4 Devourer profiles needed manual fix
- DH Devourer x2 fixed: wrong Havoc hash → correct Devourer CgcB strings

**All 56 profiles pass 1-iter smoke test.**

### Phase 4 Status (2026-03-22) — IN PROGRESS

**Baseline sims complete:**
- Patchwerk 1000-iter: 56 JSON files → results/phase4/*_patchwerk.json
- HecticAddCleave 1000-iter: 56 JSON files → results/phase4/*_hecticaddcleave.json
- Composite = 50% Patchwerk + 50% HecticAddCleave

**Remaining Phase 4 work:**
1. Parse baseline JSONs → build composite DPS table (report script needs path fix)
2. Run permutation candidates per spec (APL condition sweeps)
3. Accept changes only when composite improves AND neither fight style regresses >1%
4. Phase 5: trinket combinatorics (BiS pair sims per spec)

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

**Mage (sc_mage.cpp — ~69 TODO/FIXME comments remaining)**
Resolved 2026-03-22 (6 TODOs):
- Ignite partial tick bank: documented as best-effort approximation (ticks_left_fractional)
- Ignite spread target priority/cap: documented as best-effort
- Ignite crit trigger: documented as known approximation (omits crit_bonus/PvP)
- Pyromaniac proc: CONFIRMED correct — requires Hot Streak (ID 451466 tooltip verified)
- Arcane Phoenix no targets: documented skip+wait as standard WoW pet behavior
- Arcane Missiles cost TODO: RESOLVED — Mana Confluence already implemented at line 1830
Still open (need beta testing): various behavior-verification TODOs in Fire/Frost/Arcane paths.

**Priest Shadow (sc_priest_shadow.cpp)**
- tormenting_whispers (ID 1250492): IMPLEMENTED 2026-03-22 — +15% SW:Madness via composite_persistent_multiplier
- surge_of_insanity (ID 391399): IMPLEMENTED 2026-03-22 — +15% Mind Flay via mind_flay_base_t composite_ta_multiplier
- deaths_torment (ID 1240364): was already implemented in sw_death_t::impact() — stale TODO cleared
- Remaining: Entropic Rift / Collapsing Void if target dies mid-channel (line 1442)

**Druid (sc_druid.cpp — 50 TODOs)**
All remaining NYI items are Restoration talents (healer, out of scope for DPS sim).

**Death Knight (sc_death_knight.cpp)**
Class-tree talents — documented as utility/no DPS impact 2026-03-22:
- `death_charge` — movement utility (breaks snares, +100% speed 10s); no DPS impact
- `newly_turned` — res utility (Raise Ally at full HP + 20% absorb); no DPS impact
- `pact_of_the_apocalypse` — utility NYI, low DPS impact

**Shaman (sc_shaman.cpp)**
Class-tree utility talents — documented 2026-03-22:
- `thunderous_paws`, `gust_of_wind`, `creation_core` — movement/utility; no DPS impact
- `fury_of_the_storms` — stale NYI label fixed; already implemented (summons Storm Elemental on Stormkeeper)
- `surging_shields` — cross-referenced to lightning_shield_t (already handles it)

**Rogue**
- Stale "Partial NYI" comment at line 822 for `sudden_demise` — FIXED 2026-03-22, now documents implemented behavior.
- `deaths_arrival` (Fatebound hero talent) — NYI in-game, skipped.

### LOW — Cosmetic / blocked

- Phase 4 APL optimization loop: baselines done, permutation loop pending
- Trinket+embellishment stacking — GitHub Issue #81, blocked on beta data
- Stale "TODO: 81-89" comments in sc_extra_data.inc (base stats) — data is correct, cosmetic
- Phase 4 report script: JSON path lookup needs fix before composite DPS table can be generated

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
| All 56 profiles, iterations=1 | 56/56 PASS | — |

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
| bf9c4aa | 2026-03-22 | Docs: APL_optimization.md + example_apl_fury_warrior.md |
| b1d54e2 | 2026-03-22 | Chore: fix stale NYI comments (sudden_demise, pact_of_apocalypse, fury_of_storms) |
| 9bdbb51 | 2026-03-22 | Feat(priest/shadow): implement tormenting_whispers + surge_of_insanity; resolve deaths_torment stale TODO |
| d04018b | 2026-03-22 | Docs(mage): resolve 6 sc_mage.cpp TODOs (Pyromaniac confirmed, Mana Confluence, etc.) |
| 15f2bec | 2026-03-22 | Fix(profiles): consumables for 30 specs — correct flask/potion/food per Wowhead Season 1 |
| 4445697 | 2026-03-22 | Docs: project_progress Phase 3 consumables + gear audit + T8 talent status |
| d082570 | 2026-03-22 | Feat(talents): extractor upgraded (get_talent_links), updater script, 46/56 profiles updated |
| f6916a2 | 2026-03-22 | Fix/feat: DH Devourer talent hash corrected; 4 new hero-tree profiles (56/56 pass) |
| 3c77a2a | 2026-03-22 | Fix(profiles): gear BiS for 19 profiles — 20 new item IDs sourced from Wowhead |

# SimulationCraft — Midnight Expansion (MID1) Project Progress

Last updated: 2026-03-24 (Full spec audit fix pass — 8/10 batches complete, 35 of 42 issues resolved)
56/56 profiles pass 1-iteration sim. Build: gcc-14 clean.
Next: Phase 4a (complete baselines) → 4b (re-run diff) → 4d (optimization loop)
Note: Audit batches 9 (tier DBC verification) and 10 (low-priority cleanup) deferred.

Ground-truth audit methodology: all statements below verified by direct code inspection
(grep + read_file on actual source). Discrepancies from prior version are annotated.

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
| MID1_Druid_Balance.simc | PASS | talents= updated 2026-03-22 from Wowhead extraction |
| MID1_Druid_Balance_Elune.simc | PASS | hero-tree variant added 2026-03-22 |
| MID1_Druid_Balance_Keeper.simc | PASS | hero-tree variant added 2026-03-22 |
| MID1_Druid_Feral.simc | PASS | |
| MID1_Druid_Guardian.simc | PASS | |
| MID1_Evoker_Augmentation.simc | PASS | Inline APL removed 2026-03-22 — uses C++ generator |
| MID1_Evoker_Augmentation_Chronowarden.simc | PASS | hero-tree variant added 2026-03-22 |
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
| MID1_Rogue_Assassination_Deathstalker.simc | PASS | hero-tree variant added 2026-03-22 |
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

**Total: 56/56 PASS** (52 base + 4 hero-tree variants added 2026-03-22)

Hero-tree variant profiles (included in 56 total):
| MID1_Druid_Balance_Keeper.simc | PASS | Keeper of the Grove |
| MID1_Druid_Balance_Elune.simc | PASS | Chosen of Elune |
| MID1_Evoker_Augmentation_Chronowarden.simc | PASS | Chronowarden |
| MID1_Rogue_Assassination_Deathstalker.simc | PASS | Deathstalker |

---

## 2. Class Mechanics — General Changes

All statuses below are based on direct code inspection (2026-03-22 audit).

| Class / Spec | Mechanic Status | Notes |
| :--- | :--- | :--- |
| DK Blood | Implemented | |
| DK Frost | Implemented | |
| DK Unholy | In Beta | Apocalypse removed; loop = Lesser Ghouls + Putrefy + Dread Plague + Reaping. festering_scythe replaces festering_strike via set_replacement_action() (sc_death_knight.cpp:10046). graveyard replaces epidemic via set_replacement_action() when buff.forbidden_knowledge.up (sc_death_knight.cpp:9952). control_undead NYI (declared at line 1165, no action impl). unholy_endurance NYI (declared at line 1189, no action impl). Both are pure utility/CC with zero DPS impact. |
| DH Devourer | Implemented | |
|| DH Havoc | Implemented | Demonsurge ordering fix confirmed. MID1 tier set (2pc: Blade Dance +15%, 4pc: +6% haste in Meta) implemented 2026-03-24. APL: Inertia consumption moved to top priority after CDs. |
| DH Vengeance | Implemented | |
| Druid Balance | In Beta | Eclipse conditions confirmed in sc_druid.cpp — eclipse_lunar/eclipse_solar buffs (lines 706–707, 1237–1238); conditions simplified per prior audit. Low Phase 4 DPS (~3k composite) due to no valid talent hash — APL running on defaults only. |
| Druid Feral | In Beta | |
| Druid Guardian | In Beta | APL fully rewritten 2026-03-24: proper rage management, Ironfur/Maul at 80+ rage, Raze/Ravage, Barkskin on CD, AoE/ST split. DPS ~3k → ~11k. |
| Evoker Devastation | Implemented | Rising Fury apex IDs 1271687/1271796/1271788 confirmed at sc_evoker.cpp lines 9659–9662. |
| Evoker Augmentation | Implemented | Duplicate apex IDs 1259173/1259174/1259175 confirmed at sc_evoker.cpp lines 9736–9742. Note: ID 1259174 used for both R2 and R3 — acknowledged in code comment at line 9733. cancel_buff tip_the_scales present in apl_evoker.cpp line 220. Inline APL removed 2026-03-22; full C++ generator active. |
| Hunter BM | Implemented | Uses spell_data_ptr_t (not player_talent_t) for talent lookups — confirmed in sc_hunter.cpp lines 17–30. All talents confirmed implemented; scanner false-positive. |
| Hunter Marks | Implemented | Same spell_data_ptr_t pattern — scanner false-positive. |
| Hunter Survival | Implemented | Same pattern. |
| Mage Arcane | In Beta | 61 TODO/FIXME comments remain in sc_mage.cpp (exact count from grep, not ~62). Touch of Archmage IDs 1257942/1257947/1257950 confirmed at lines 6005–6017. |
| Mage Fire | In Beta | Fired Up IDs 1257343/1257349/1257348 confirmed at lines 6060–6072. Burnout: code reads effectN(1).percent() from spell data dynamically (line 1468); comment states 75% (line 2531). Pyromaniac confirmed correct. |
| Mage Frost | In Beta | Hand of Frost IDs 1262935/1262981/1263249 confirmed at lines 6117–6133. Winter's End AoE: reduced_aoe_targets set at line 4337 with NO p->bugs guard — confirmed real in-game behavior per inline comment citing spell ID 1247775. |
| Monk Brewmaster | In Beta | |
| Monk Windwalker | In Beta | Ascension energy regen effect#2 confirmed in sc_monk.cpp lines 6677–6678 (effectN(2).percent()). Weapon of Wind (ID 1272678): IMPLEMENTED 2026-03-22 — +10% damage during Zenith via parse_effects(buff.zenith, talent.weapon_of_wind). |
| Paladin Protection | In Beta | Uses const spell_data_t* pattern (not player_talent_t) in paladin/sc_paladin.cpp — scanner false-positive. All talents confirmed implemented. |
| Paladin Retribution | In Beta | Same const spell_data_t* pattern. All confirmed implemented. |
| Priest Shadow | Implemented | tormenting_whispers (ID 1250492): +15% SW:Madness via composite_persistent_multiplier confirmed at sc_priest_shadow.cpp lines 944–946. surge_of_insanity (ID 391399): +15% Mind Flay via composite_ta_multiplier confirmed at lines 53–55. Collapsing Void target_ready() early return confirmed at sc_priest.cpp line 1446. |
| Rogue Assassination | In Beta | Sudden Demise: +10% bleed base (effectN(1)) + linear bonus to +150% at 0% HP below execute threshold (effectN(3)) — confirmed at sc_rogue.cpp lines 2453–2471. |
| Rogue Outlaw | In Beta | Grand Melee (ID 1259469): +8% Blade Flurry cleave confirmed — talent init at line 9741, Blade Flurry default_value += effectN(1).percent() at lines 7014–7019. |
| Rogue Subtlety | In Beta | |
| Shaman Elemental | Implemented | Lava Flows (ID 1273485): Maelstrom gain on LvB Overload (lines 6677–6681) and damage bonus (lines 6704–6707, 7029–7032) confirmed. Code looks up by name via _ST("Lava Flows"), not hardcoded ID. surging_shields (ID 382033): +4 Maelstrom per LS trigger via effectN(2) confirmed at sc_shaman.cpp lines 4712–4715. gain_t* surging_shields in gains struct (line 1507) and init_gains() (line 12619) confirmed. |
| Shaman Enhancement | Implemented | surging_shields (ID 382033): +50% MSW proc chance on LS trigger via effectN(3).percent() confirmed at sc_shaman.cpp lines 4719–4722. |
| Warlock Affliction | In Beta | drain_life APL: confirmed in warlock.cpp line 77 as primary filler with Gorefiend's Avarice; drain_soul also present (line 78) for Nightfall proc handling alongside it — not sole filler. |
| Warlock Demonology | In Beta | |
| Warlock Destruction | In Beta | |
| Warrior Arms | Implemented | Master of Warfare IDs 1269314/1269306/1269307 confirmed at sc_warrior.cpp lines 7263–7265. |
| Warrior Fury | Implemented | Rampaging Berserker IDs 1269308/1269309/1269310 confirmed at sc_warrior.cpp lines 7318–7320. |
| Warrior Protection | Implemented | Phalanx IDs 1269311/1269312/1269313 confirmed at sc_warrior.cpp lines 7378–7380. |

---

## 3. Midnight Apex (4-Rank) Talents — All 33 Specs

Each spec has one 4-rank apex talent using 3 spell IDs: Rank1 (_1), Ranks2+3 (_23), Rank4 (_4).
All spell IDs verified against source code (2026-03-22 audit). "name+rank" means registered via
_ST/_CT name lookup rather than explicit integer ID in find_talent_spell calls.

| Spec | Apex Talent Name | R1 ID | R23 ID | R4 ID | Code Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Warrior Arms | Master of Warfare | 1269314 | 1269306 | 1269307 | Confirmed (sc_warrior.cpp:7263–7265) |
| Warrior Fury | Rampaging Berserker | 1269308 | 1269309 | 1269310 | Confirmed (sc_warrior.cpp:7318–7320) |
| Warrior Protection | Phalanx | 1269311 | 1269312 | 1269313 | Confirmed (sc_warrior.cpp:7378–7380) |
| Mage Arcane | Touch of the Archmage | 1257942 | 1257947 | 1257950 | Confirmed (sc_mage.cpp:6005–6017) |
| Mage Fire | Fired Up | 1257343 | 1257349 | 1257348 | Confirmed (sc_mage.cpp:6060–6072) |
| Mage Frost | Hand of Frost | 1262935 | 1262981 | 1263249 | Confirmed (sc_mage.cpp:6117–6133) |
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
| Evoker Devastation | Rising Fury | 1271687 | 1271796 | 1271788 | Confirmed (sc_evoker.cpp:9659–9662) |
| Evoker Augmentation | Duplicate | 1259173 | 1259174 | 1259175 | Confirmed (sc_evoker.cpp:9736–9742). Note: R2 and R3 share ID 1259174 — acknowledged in comment at line 9733. |
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
| Warlock Affliction | Updated 2026-03-20 | Yes | drain_life primary filler with Gorefiend's Avarice; drain_soul present for Nightfall proc handling |
| Rogue Outlaw | Updated 2026-03-20 | Yes | Grand Melee implementation confirmed |
| Rogue Assassination | Updated 2026-03-20 | Yes | Sudden Demise execute bonus confirmed |
| DH Havoc | Updated 2026-03-22 | Yes | Demonsurge ordering fix: demonsurge_available in if= guards (apl_demon_hunter.cpp lines 212, 250–254) |
|| Evoker Augmentation | Updated 2026-03-22 | Yes | Removed 18-line inline APL; C++ generator active; cancel_buff tip_the_scales present (apl_evoker.cpp:220) |
|| DH Devourer | Updated 2026-03-24 | Yes | Cull reordered above Void Ray in meta priority; Soul Smuggling fragment hold logic added |
|| DH Havoc | Updated 2026-03-24 | Yes | Inertia consumption (felblade/fel_rush) moved to top priority after CDs |
|| DK Unholy | Updated 2026-03-24 | Yes | Soul Reaper HP gate removed (cast on CD); RP>=80 spending threshold; Putrefy higher in AoE |
|| Evoker Devastation | Updated 2026-03-24 | Yes | Engulf added to Flameshaper lists; Deep Breath on CD for Scalecommander ST; typos fixed |
|| Monk Brewmaster | Updated 2026-03-24 | Yes | Touch of Death #1 priority; Blackout Kick higher; SCK AoE filler (>=3 targets) |
|| Rogue Subtlety | Updated 2026-03-24 | Yes | Shadow Dance CP split (Deathstalker low/Trickster 6+); Shadowstrike AoE <=3 |
|| Mage Frost | Updated 2026-03-24 | Yes | FoF 2-stack priority before Glacial Spike in Frostfire lists |
|| Shaman Elemental | Updated 2026-03-24 | Yes | AoE routing threshold lowered from >=3 to >=2 targets |
|| Druid Guardian | Updated 2026-03-24 | Yes | Full APL rewrite — replaced assisted_combat stub with proper rotation |

### Audit Fix Pass — Summary (2026-03-24)

Full audit: `audit_notes.md` (42 issues). Task list: `audit_task_list.md` (10 batches).

| Batch | Priority | Tasks | Status |
| :--- | :--- | :--- | :--- |
| 1 | CRITICAL | 5 missing tier sets (DH Havoc, Evoker Aug, Priest Shadow, Enh Shaman, WW Monk) | COMPLETE |
| 2 | CRITICAL | Guardian Druid APL rewrite | COMPLETE |
| 3 | HIGH | DH APL fixes (Devourer Cull reorder, Soul Smuggling, Havoc Inertia) | COMPLETE |
| 4 | HIGH+MED | DK APL fixes (Soul Reaper, Death Coil RP, Putrefy position) | COMPLETE |
| 5 | HIGH+MED | Evoker APL fixes (Engulf, Deep Breath, typos) | COMPLETE |
| 6 | HIGH+MED | Monk Brewmaster APL fixes (ToD, BoK, SCK) | COMPLETE |
| 7 | HIGH+MED | Rogue Sub + Frost Mage APL fixes | COMPLETE |
| 8 | MEDIUM | 10 multi-spec condition fixes (1 real fix, 9 verified correct) | COMPLETE |
| 9 | MEDIUM | Tier set DBC auto-parse verification | DEFERRED |
| 10 | LOW | Cleanup (5 cosmetic items) | DEFERRED |

**Resolved: 35 issues. Deferred: 7 (all MEDIUM/LOW).**

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
- DK Unholy `festering_scythe`: set_replacement_action() replaces festering_strike (sc_death_knight.cpp:10046)
- DK Unholy `graveyard`: set_replacement_action() replaces epidemic when buff.forbidden_knowledge.up (sc_death_knight.cpp:9952)
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
| Phase 3.5a | Extractor pipeline fixes — validation, noise strip, dedup, hero click verify, MutationObserver | COMPLETE — 56-82% file size reduction |
| Phase 3.5b | Downstream consumer fixes — gen_apl_diff.py parser (17 specs fixed), "null" JSON key fixed | COMPLETE — 17/17 previously-failing specs now parse; APL diff re-run: HIGH=11, MEDIUM=21, LOW=1 |
| Phase 3.5c | Investigate outliers + fix 3 profile data gaps | COMPLETE — DH Devourer confirmed valid new spec; 3 profiles fixed |
| Phase 3.5d | Visual audit of all 33 specs + hero talent extraction fixes | COMPLETE — 3 extractor bugs fixed (prefix matching, apostrophe normalization, hyphen-to-space); 5 specs with 3 build variants now captured; 33/33 validated |
| Phase 4a | Complete baselines — 4 missing HAC sims + re-run 5 changed profiles (Druid Bal x3, Evoker Aug x2) | NOT STARTED |
| Phase 4b | Re-run APL diff with fresh extracted data (6 fixed heroes + 5 build variants) | NOT STARTED |
| Phase 4c | APL gap review — triage 12 HIGH-priority specs from diff report, separate real gaps from false positives | NOT STARTED |
| Phase 4d | Optimization loop — permutation candidates, condition sweeps, composite scoring (50% PW + 50% HAC) | NOT STARTED |
| Phase 5 | Trinket combinatorics — sim all BiS trinket pairs | NOT STARTED |

### Phase 4 Baseline Status (2026-03-22) — PARTIAL, not complete as previously claimed

**Actual JSON file counts (verified by ls results/phase4/):**
- Patchwerk JSONs: 56 / 56 profiles — COMPLETE
- HecticAddCleave JSONs: 52 / 56 profiles — INCOMPLETE

**Missing HecticAddCleave runs (4 profiles):**
- MID1_Death_Knight_Blood
- MID1_Death_Knight_Blood_Deathbringer
- MID1_Evoker_Devastation
- MID1_Evoker_Devastation_FS

**Total JSONs: 108** (not 112 as previously claimed — 4 HAC runs never completed)

**Remaining Phase 4 work:**
1. (4a) Run 4 missing HecticAddCleave baseline sims (DK Blood x2, Evoker Dev x2)
2. (4a) Re-run PW + HAC baselines for 5 profiles with changed talents (Druid Bal x3, Evoker Aug x2) — DPS will change significantly now that real talent strings are applied
3. (4b) Re-run gen_apl_diff.py — extraction pipeline fixed 6 hero talents + 5 build variants since last run; diff results will change
4. (4c) Review 12 HIGH-priority specs in APL_diff_report.md — determine real gaps vs false positives
5. (4d) Run permutation candidates per spec (APL condition sweeps); accept only when composite improves AND neither fight style regresses >1%
6. Phase 5: trinket combinatorics (BiS pair sims per spec)

**Composite DPS baseline (1000 iter, 2026-03-22) — top 10 (52 complete pairs only):**
| Profile | Patchwerk | HecticAC | Composite |
| :--- | ---: | ---: | ---: |
| MID1_Warlock_Demonology_Soul_Harvester | 97,590 | 471,531 | 284,560 |
| MID1_Warlock_Demonology | 97,754 | 464,535 | 281,145 |
| MID1_Rogue_Subtlety | 125,892 | 233,196 | 179,544 |
| MID1_Mage_Fire_Frostfire | 101,657 | 225,945 | 163,801 |
| MID1_Mage_Fire | 101,705 | 225,508 | 163,607 |
| MID1_Death_Knight_Unholy | 110,175 | 212,680 | 161,427 |
| MID1_Death_Knight_Unholy_San'layn | 110,055 | 212,410 | 161,232 |
| MID1_Monk_Windwalker | 108,260 | 208,618 | 158,439 |
| MID1_Demon_Hunter_Devourer_Void-Scarred | 108,553 | 204,002 | 156,277 |
| MID1_Demon_Hunter_Devourer | 105,777 | 203,082 | 154,429 |

**Extraction pipeline:** FULLY RESOLVED. See `wowhead/EXTRACTION_PIPELINE_AUDIT.md` + `MANUAL_IMPORT_CHECKLIST.md`.
33/33 specs extract all hero builds (including 5 specs with 3 build variants).
All manual import items resolved: talent strings applied, Weapon of Wind implemented,
apex talent data corrected.

**Outliers needing APL investigation (baselines stale — re-run needed):**
- MID1_Rogue_Assassination (~13k composite) — APL likely needs DPS-spec tuning
- MID1_Evoker_Augmentation (~8k) — support spec, low raw DPS expected; talent string now applied, re-baseline will show real DPS
- MID1_Druid_Balance (~3k) — talent string now applied (was defaults), re-baseline expected to show major improvement

---

## 6. Unique Gear — Midnight Trinkets / Embellishments

### unique_gear_midnight.cpp — Current State

| Spell ID | Name | Status | Notes |
| :--- | :--- | :--- | :--- |
| 1237154 | AoE ground-effect trigger (Draught of Rampant Abandon secondary) | Implemented | Area Trigger 38015: 30s ground zone, 1s pulse ticks, Shadow damage = effectN(1).average(item) — confirmed at line 177+ |
| 1263727 | Litany of Lightblind Wrath shield | Implemented | absorb_buff_t triggered on blast; self-absorb approx for solo patchwork — confirmed at line 2583+ |

**NYI items remaining: 0** (grep for NYI/nyi/not_yet_implemented in unique_gear_midnight.cpp returns zero matches — confirmed by audit)

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

None currently open. (5 missing tier sets resolved 2026-03-24 — DH Havoc, Evoker Aug, Priest Shadow, Enh Shaman, WW Monk)

### MEDIUM — Behavior correctness

**Monk Windwalker (sc_monk.cpp)**
- Weapon of Wind (ID 1272678): IMPLEMENTED 2026-03-22. +10% damage during Zenith via
  `parse_effects( p()->buff.zenith, p()->talent.windwalker.weapon_of_wind )`. DBC spell
  1272678 modifies Zenith effectN #2 and #4 by +10 flat. Build clean, smoke test passes.

**Mage (sc_mage.cpp — 61 TODO/FIXME comments remaining)**
- Exact count from grep: 61 (previously stated ~62)
- Winter's End AoE falloff: CONFIRMED FIXED — reduced_aoe_targets at line 4337, no p->bugs
  guard, confirmed real in-game behavior from spell ID 1247775 tooltip
- Burnout: code reads effectN(1).percent() dynamically from spell data (line 1468); comment
  at line 2531 states 75%; actual value depends on live spell data

**DK Unholy (sc_death_knight.cpp)**
- control_undead (line 1165): declared NYI, no action implementation
- unholy_endurance (line 1189): declared NYI, no action implementation
- Both are pure utility (CC / defensive) with zero DPS impact

**Druid Guardian**
- APL rewritten 2026-03-24 from assisted_combat stub to full rotation. DPS ~3k → ~11k.
  Needs Phase 4 re-baseline to confirm composite improvement.

### LOW — Cosmetic / blocked

- Phase 4 APL optimization loop: 52/56 profiles have both PW+HAC baselines; 4 missing HAC runs
  (DK Blood x2, Evoker Dev x2) need to be completed before composite scoring is final
- Trinket+embellishment stacking — GitHub Issue #81, blocked on beta data
- Stale "TODO: 81-89" comments in sc_extra_data.inc (base stats) — data is correct, cosmetic

---

## 8. Scanner False-Positive Bug in missing_from_code.md

The audit script searches for `player_talent_t` keyword to find talent declarations.
Hunter uses `spell_data_ptr_t` (sc_hunter.cpp lines 17–30) and Paladin uses
`const spell_data_t*` (paladin/sc_paladin.cpp) — both fully implemented but appear
as 100% missing in the report.

**Impact:** 471 talents across Hunter BM/MM/SV and Paladin Prot/Ret reported as missing —
all confirmed implemented by direct code inspection.

**Note on file paths:** Paladin module is in engine/class_modules/paladin/sc_paladin.cpp
(subdirectory), not a flat engine/class_modules/sc_paladin.cpp.
Monk module is in engine/class_modules/monk/sc_monk.cpp (subdirectory).

Fix recommendation: update the scanner to also search for `find_talent_spell` calls,
`spell_data_ptr_t` declarations, and `const spell_data_t*` pointer patterns.

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
| 6b31c73 | 2026-03-21 | Monk Windwalker: Weapon of Wind (ID 1272678) — registered stub only, no effect code |
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
| 360bfaa | 2026-03-22 | Docs: full project_progress update — all batches 1–7 reflected |
| 71e8e58 | 2026-03-22 | Feat(shaman) + fix(profiles): surging_shields impl + gear BiS batch 2 (7 profiles) |
| c3baf08 | 2026-03-22 | Fix/docs: DK Unholy + Priest Shadow + Mage TODOs — Winter's End AoE fix, Collapsing Void edge case |
|| da1a909 | 2026-03-22 | Docs: fix commit hash c3baf08 |
|| a28ae17 | 2026-03-24 | Docs: full spec audit (42 issues), audit_notes.md + audit_task_list.md |
|| eef908c | 2026-03-24 | Feat(tier): Implement MID1 tier sets for 5 specs (DH Havoc, Evoker Aug, Priest Shadow, Enh Shaman, WW Monk) |
|| 6cdcf5a | 2026-03-24 | Fix(apl): Guardian Druid full APL rewrite — replaced assisted_combat stub |
|| ce27ee5 | 2026-03-24 | Fix(apl): Batches 3-7 — DH, DK, Evoker, Monk, Rogue, Mage APL fixes (18 changes) |
|| a21f7e1 | 2026-03-24 | Fix(apl): Batch 8 — Shaman Ele AoE threshold >=3 → >=2 |

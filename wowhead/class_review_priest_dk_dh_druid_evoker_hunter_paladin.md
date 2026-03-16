# Class Code Audit Report — Priest (Shadow), Death Knight, Demon Hunter, Druid, Evoker, Hunter, Paladin
*Generated: 2026-03-17 — Midnight SimulationCraft Project*

---

## PRIEST (SHADOW)
Files: `engine/class_modules/priest/sc_priest.hpp`, `sc_priest.cpp`, `sc_priest_shadow.cpp`

### Renames Fixed
- `shackle_undead` lookup string was `"Shackle Undead"` → changed to `"Shackle Horror"` (info_base.md ID 9484). The talent was renamed in Midnight. Field name in code kept as `shackle_undead` (refactor out of scope).

### Truncated info_base.md Names Annotated
- `238100 | Angel` — truncated; full name is "Angel's Mercy". Code `angels_mercy = CT("Angel's Mercy")` is correct. Added clarifying comment.
- `373450 | Light` — truncated; full name is "Light's Inspiration". Code `lights_inspiration = CT("Light's Inspiration")` is correct. Added clarifying comment.

### Missing From Code (info_base.md → Code)
| Spell ID | Name | Status | Action |
|----------|------|--------|--------|
| 1240364 | Death | DPS-relevant Midnight Shadow talent | // TODO: implement — added comment in sc_priest_shadow.cpp |
| 373273/373280/373310/377349 | Idol of Yogg-Saron / Idol of N / Idol of Y / Idol of C | All 4 present in code (idol_of_yoggsaron, idol_of_nzoth, idol_of_yshaarj, idol_of_cthun) | OK |
| 1264096 | Void Apparitions | Present as void_apparitions_1/2/3 apex nodes | OK — audit false positive |

### Missing From Code (code-only)
- `deaths_torment` — not in info_base table; likely renamed or absorbed. NOTE already present in code context.
- `invoked_nightmares`, `misery`, `intangibility`, `mental_fortitude` — utility/passive nodes not listed in info_base table, acceptable.

---

## DEATH KNIGHT
File: `engine/class_modules/sc_death_knight.cpp`

### Overall Coverage
Good coverage. All class, blood, frost, unholy, deathbringer, san'layn, and rider talents present.

### Notes Added
- `horsemens_aid` — added `// NOTE: not in info_base.md talent table (minor utility node)`
- `pact_of_the_apocalypse` — added `// NYI — NOTE: not in info_base.md talent table`
- `fury_of_the_horsemen` — added `// NOTE: not in info_base.md talent table`
- `a_feast_of_souls` — added `// NOTE: not in info_base.md talent table`

### Verified IDs
- `deaths_echo` code field: lookup `"Death's Echo"` matches info_base `356367 | Death | deaths-echo` (slug is truncated but spell name is correct).
- All class-tree talents (icebound_fortitude, death_strike, raise_dead, etc.) match info_base.
- `march_of_darkness`, `deaths_reach`, `wraith_walk` — present in code, confirmed in info_base.
- Blood spec: `boiling_point`, `lifeblood`, `deadly_reach`, `plague_infusion`, `bloody_reflection`, `blood_mist`, `consumption`, `sanguinary_burst` — all present and ID-verified.
- Unholy: `raise_abomination` (ID in info_base: 1242608), `clawing_shadows`, `putrefy`, `doomed_bidding`, `grave_mastery` — confirmed present.
- `dance_of_midnight_1/2/3` apex — info_base has single `Dance of Midnight (1264506)` — code splits into 3 ranks, acceptable.

---

## DEMON HUNTER
File: `engine/class_modules/sc_demon_hunter.cpp`

### Overall Coverage
Good coverage across all four specs: class, havoc, vengeance, devourer, aldrachi_reaver, annihilator, scarred.

### Verified Present (key items)
- `netherwalk` — confirmed still in Havoc info_base (ID 196555 implied). Code has `// No Implementation`.
- `desperate_instincts`, `deflecting_dance`, `mortal_dance` — confirmed in Havoc info_base. Code has `// No Implementation`.
- `master_of_the_glaive`, `champion_of_the_glaive` — confirmed in info_base (IDs 389763, 429211).
- `chaotic_transformation`, `relentless_onslaught`, `soulscar`, `inner_demon` — confirmed in info_base.
- `screaming_brutality` (1220506), `a_fire_inside` (427775), `glaive_tempest` (1244557) — in info_base.
- `eternal_hunt_1/2/3` apex — info_base has `1270898 | Eternal Hunt`. Multi-rank split OK.

### No structural issues found
All major DPS talents are present and annotated.

---

## DRUID
File: `engine/class_modules/sc_druid.cpp`

### Overall Coverage
Excellent — 324 talent entries covering class, balance, feral, guardian, restoration, and all four hero trees.

### Verified Key Items
- Class tree: `grievous_wounds` (474526), `ursocs_spirit` (449182), `lycaras_teachings` (378988), `lycaras_inspiration` (1232897), `wellhoned_instincts` (377847), `perfectlyhoned_instincts` (1213597) — all present.
- Balance: `eclipse` (1239669), `total_eclipse` (1240206), `meteor_storm`, `elunes_challenge` (1240283), `hail_of_stars` (469004) — all present.
- Feral: `panthers_guile` (1280316), `blood_spattered` (1244532), `lacerating_claws` (1244632), `frantic_frenzy` (1243807), `chomp` (1244258) — all present.
- Guardian: `harnessed_rage` (1253035), `waking_nightmare` (1253461), `sundering_roar` (1253799), `natural_resilience` (1278789), `memory_of_ysera` (1250906), `killing_blow` (1252994) — all present.
- Guardian apex: `wild_guardian_1/2/3` — info_base has `1269617 | Wild Guardian`. Multi-rank OK.

### No structural issues found

---

## EVOKER
File: `engine/class_modules/sc_evoker.cpp`

### Overall Coverage
Good coverage across class, devastation, augmentation, and hero trees (chronowarden, flameshaper, scalecommander).

### Midnight Class Tree Additions (already annotated in code)
- `regenerative_magic` (387787), `walloping_blow` (387341), `strike_from_above` (1267206), `potent_mana` (418101), `improved_defy_fate` (1268881), `nozdormu_adept` (431715) — all confirmed in info_base.

### Verified Key IDs
- `azure_sweep` (1265867), `shattering_stars` (1265802), `strafing_run` (1266151) — confirmed in info_base.
- `azure_celerity` (1219723), `star_salvo` (1265826) — confirmed in info_base.

### No structural issues found

---

## HUNTER
File: `engine/class_modules/sc_hunter.cpp`

### Notes Added
- `huntmasters_call` — info_base lists as `"Huntmaster"` (ID 459730). SimC uses `"Huntmaster's Call"` which is the correct full spell name. Added clarifying comment.
- `wild_instincts` — not in BM info_base.md talent table. Added `// NOTE: not in info_base.md BM talent table`.
- `bloody_frenzy` — not in BM info_base.md talent table. Added `// NOTE: not in info_base.md BM talent table`.
- `natures_ally_1/2/3` — info_base lists single `"Nature's Ally"` (ID 1273043). Code correctly splits into multi-rank. Added clarifying comment.

### Verified Present (key BM items)
- `barbed_shot`, `bestial_wrath`, `cobra_shot`, `beast_cleave`, `war_orders`, `wild_thrash`, `laceration`, `kill_cleave`, `training_expert`, `the_beast_within`, `thrill_of_the_hunt`, `pack_tactics`, `barbed_scales`, `serpentine_strikes`, `dire_frenzy`, `frenzy` — all in info_base.
- `bloodshed` (1272099), `wildspeaker` (1232739), `piercing_fangs` (392053) — confirmed in info_base.

### Survival: Key Talents Verified
- `boomstick` (1261193), `strike_as_one` (1251717), `raptor_swipe` (1259003) — in info_base.
- `mongoose_fury` (1252708), `shellshock` (1252931), `wildfire_imbuement` (1252943) — in info_base.
- `flankers_advantage` in code = `"Flanker's Advantage"` — info_base shows `459964 | Flanker` (truncated). Correct.
- `two_against_many` (1251718), `twin_fangs` (1272139), `primal_surge` (1272154) — confirmed in info_base.

---

## PALADIN
File: `engine/class_modules/paladin/sc_paladin.hpp`

### Overall Coverage
Good coverage using `const spell_data_t*` pattern (not `player_talent_t`).

### Key Verified Items (Class Tree)
- `lay_on_hands` (633), `hammer_of_wrath` (1241288), `fist_of_justice` (234299), `divine_toll` (375576), `divine_purpose` present, `blessing_of_dawn` (183416), `blessing_of_dusk` (1241945), `seal_of_might` (385450), `vengeful_wrath` (1241958) — all confirmed in info_base.

### Retribution Verified
- `blade_of_justice` (184575), `divine_storm` (53385), `final_verdict` (383328), `execution_sentence` (343527), `wake_of_ashes` (255937), `empyrean_legacy` (387170), `radiant_glory` (458359), `crusade` (1253598) — confirmed in info_base.
- `zealots_fervor` in code — info_base shows `403509 | Zealot` (truncated). Correct.
- `highlords_wrath` in code — info_base shows `404512 | Highlord` (truncated). Correct.
- `consecrated_ground_ret` has `// TODO: implement or drop` — appropriate.

### Protection Verified
- `ardent_defender` (31850), `grand_crusader` (85043), `bulwark_of_order` (209389), `valiant_crusade` (1245979), `searing_sunlight` (1244070), `vision_of_sanctity` (1245354), `undying_embers` (1244019) — confirmed in info_base.
- `tyrs_enforcer` in code — info_base shows `378285 | Tyr` (truncated). Correct.
- `avengers_shield` in code (prot row 0) — confirmed present as `31935 | Avenger`.

### Herald of the Sun Hero Tree
- `dawnlight` (431377), `eternal_flame` (156322), `luminosity` (431402), `endless_gleam` (1263787), `sun_sear` (431413) — confirmed in info_base.

---

## Summary of Code Changes Made

| File | Change |
|------|--------|
| `priest/sc_priest.cpp` | Fixed `shackle_undead` lookup → `"Shackle Horror"` (Midnight rename, ID 9484) |
| `priest/sc_priest.cpp` | Added NOTE comment for `angels_mercy` ("Angel" in info_base = truncated) |
| `priest/sc_priest.cpp` | Added NOTE comment for `lights_inspiration` ("Light" in info_base = truncated) |
| `priest/sc_priest_shadow.cpp` | Added `// TODO: implement — "Death" (ID 1240364) new Midnight Shadow talent` |
| `sc_death_knight.cpp` | Added `// NOTE: not in info_base.md` for `horsemens_aid`, `pact_of_the_apocalypse`, `fury_of_the_horsemen`, `a_feast_of_souls` |
| `sc_hunter.cpp` | Added NOTE for `huntmasters_call` (Huntmaster in info_base), `wild_instincts`, `bloody_frenzy` (not in BM table), `natures_ally_1` (multi-rank split) |

---
*Generated by Hermes Agent — Midnight audit pass 2026-03-17*

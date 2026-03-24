# Monk Specs Audit Report: Wowhead Data vs SimC Implementation
Generated: 2026-03-24
Auditor: Automated Comparison

## Files Reviewed
- wowhead/monk/brewmaster/extracted/rotation.md
- wowhead/monk/brewmaster/extracted/tier.md
- wowhead/monk/brewmaster/info_base.md
- wowhead/monk/windwalker/extracted/rotation.md
- wowhead/monk/windwalker/extracted/tier.md
- wowhead/monk/windwalker/info_base.md
- engine/class_modules/apl/apl_monk.cpp
- engine/class_modules/monk/sc_monk.cpp
- engine/class_modules/monk/sc_monk.hpp

---

## BREWMASTER MONK

### Rotation Priority Comparison (Wowhead vs SimC APL)

#### Wowhead ST Priority (Shado-Pan):
1. Touch of Death (execute)
2. Blackout Kick (trigger Blackout Combo)
3. Celestial Brew / Celestial Infusion (if taking minimal damage)
4. Invoke Niuzao, the Black Ox
5. Tiger Palm (consume Blackout Combo buff)
6. Keg Smash first charge / Empty Barrel
7. Breath of Fire
8. Exploding Keg
9. Chi Burst
10. Keg Smash second charge
11. Purifying Brew (if taking minimal damage, for Special Delivery / Empty Barrels)
12. Tiger Palm (filler)

#### SimC APL Priority (default list):
1. auto_attack
2. potion
3. race_actions / item_actions
4. Black Ox Brew (conditional)
5. Celestial Brew (Aspect of Harmony spender up)
6. Keg Smash (Empty Barrel + Aspect of Harmony)
7. Breath of Fire (Wisdom of the Wall + Niuzao up)
8. Keg Smash (Wisdom of the Wall + Niuzao up)
9. Celestial Brew (Aspect of Harmony accumulator > 95% health)
10. Purifying Brew
11. Fortifying Brew
12. Chi Burst
13. Exploding Keg
14. Empty the Cellar
15. Invoke Niuzao
16. Breath of Fire (conditional: BoK cd > 1.5s, no empty barrel, keg smash charges < 1)
17. Celestial Brew (if Flurry Strikes talented)
18. Keg Smash (Flurry Strikes talented)
19. Keg Smash (Empty Barrel up)
20. Keg Smash (charges = 1)
21. Breath of Fire
22. Empty the Cellar
23. Rushing Jade Wind
24. Keg Smash
25. Blackout Kick
26. Tiger Palm (conditional energy)
27. Expel Harm

#### DIFFERENCES FOUND:

| # | Issue | Severity |
|---|-------|----------|
| B1 | **Touch of Death MISSING from SimC APL.** Wowhead lists it as #1 priority (execute). SimC Brewmaster APL has NO touch_of_death action at all. | HIGH |
| B2 | **Blackout Combo interaction NOT modeled in APL.** Wowhead emphasizes using Blackout Kick BEFORE Tiger Palm to consume the combo buff. SimC APL puts Blackout Kick near the bottom (after most other abilities) and Tiger Palm doesn't check for Blackout Combo buff. The class module does implement the buff (buff.blackout_combo), but the APL doesn't sequence BoK->TP correctly. | HIGH |
| B3 | **APL is heavily tuned for Master of Harmony (Aspect of Harmony) rather than Shado-Pan.** Many conditionals reference aspect_of_harmony_spender, aspect_of_harmony_accumulator, and wisdom_of_the_wall. Wowhead's primary guide uses Shado-Pan. The APL appears to be a single combined list that handles both hero talents via conditionals, but it doesn't match the Wowhead Shado-Pan priority closely. | MEDIUM |
| B4 | **Spinning Crane Kick MISSING from APL.** Wowhead AoE priority lists SCK as filler when no other abilities to press (and Blackout Combo is not active). SimC APL has no spinning_crane_kick action for Brewmaster. | MEDIUM |
| B5 | **Invoke Niuzao priority differs.** Wowhead places it at #4 (high priority after BoK and Celestial Brew). SimC APL places it much lower, after Chi Burst and Exploding Keg. | LOW |
| B6 | **Empty the Cellar present in APL but not explicitly in Wowhead rotation.** The APL includes empty_the_cellar actions. Wowhead mentions it in the Exploding Keg section but doesn't include it in the numbered priority. | LOW |
| B7 | **Expel Harm in APL as lowest priority filler.** Wowhead doesn't include it in the DPS rotation (it's discussed as a defensive/healing ability). Including it as a damage filler is a SimC-specific optimization. | INFO |

### Tier Set Bonuses (Brewmaster)

**Wowhead Data (Way of Ra-den's Chosen):**
- 2pc: Keg Smash damage +10%, Breath of Fire damage +10%
- 4pc: Keg Smash Energy cost reduced by 5, Keg Smash deals extra Fire damage (Extra Kick) to targets afflicted by Breath of Fire

**SimC Implementation:**
- tier.mid1.brm_2pc = sets->set(MONK_BREWMASTER, MID1, B2) — FOUND
- tier.mid1.brm_4pc = sets->set(MONK_BREWMASTER, MID1, B4) — FOUND
- tier.mid1.brm_4pc_extra_kick = find_spell(1272464) — FOUND (Extra Kick damage action)
- extra_kick_t struct implemented as background action triggered on Keg Smash impact

| # | Issue | Severity |
|---|-------|----------|
| BT1 | **Brewmaster tier set bonuses appear FULLY implemented.** 2pc damage buffs and 4pc Extra Kick + energy reduction are coded. | OK |

### Key Talent Effects (Brewmaster)

| Talent | Implemented? | Notes |
|--------|-------------|-------|
| Blackout Combo | YES | buff.blackout_combo tracked, Tiger Palm consumes it |
| Stagger / Shuffle | YES | Core mechanic, heavily modeled |
| Purifying Brew | YES | In APL and class module |
| Celestial Brew / Infusion | YES | In APL with conditionals |
| Invoke Niuzao | YES | In APL and class module |
| Exploding Keg | YES | In APL |
| Flurry Strikes (Shado-Pan) | YES | Referenced in APL conditionals |
| Breath of Fire | YES | In APL |
| Special Delivery | PARTIAL | Not directly in APL but talent effects coded |
| Bob and Weave | YES | Stagger duration extension coded |
| Charred Passions / Dragonfire Brew | YES | Implemented in class module |
| Face Palm / Counterstrike | YES | Buffs parsed in class module |

---

## WINDWALKER MONK

### Rotation Priority Comparison (Wowhead vs SimC APL)

#### Wowhead ST Priority (Shado-Pan):
1. Touch of Death
2. Whirling Dragon Punch
3. Tiger Palm (if < 4 Chi, < 2 Combo Breaker stacks, about to cap energy)
4. Fists of Fury
5. Rushing Wind Kick
6. Spinning Crane Kick (Dance of Chi-Ji < 4s remaining, not at 2 Combo Breaker stacks)
7. Rising Sun Kick
8. Tiger Palm (if not enough Chi)
9. Blackout Kick (with Combo Breaker or Zenith active)
10. Spinning Crane Kick (with Dance of Chi-Ji)
11. Blackout Kick
12. Tiger Palm

#### Wowhead ST Priority (Conduit of the Celestials):
1. Fists of Fury (if Heart of the Jade Serpent < 1s)
2. Touch of Death
3. Celestial Conduit (if no active Heart of the Jade Serpent)
4. Whirling Dragon Punch
5. Tiger Palm (if < 4 Chi, < 2 Combo Breaker, cap energy)
6. Fists of Fury
7. Rushing Wind Kick
8. SCK (Dance of Chi-Ji < 4s, not 2 Combo Breaker stacks)
9. Rising Sun Kick
10. Tiger Palm (if not enough Chi)
11. Blackout Kick (with Combo Breaker)
12. SCK (with Dance of Chi-Ji)
13. Blackout Kick
14. Tiger Palm

#### SimC APL Structure:
- Separate action lists: opener, trinket, big_coc, zenith, racials, default_st, multitarget, fallback
- Very detailed and condition-heavy
- Handles both Shado-Pan (flurry_strikes) and Conduit of the Celestials (celestial_conduit) with talent conditionals

#### DIFFERENCES FOUND:

| # | Issue | Severity |
|---|-------|----------|
| W1 | **Touch of Death positioned LOW in SimC ST APL.** Wowhead lists ToD as #1/#2 priority for both hero talent builds. SimC APL places it near line 250 in the ST list (after RSK, FoF, WDP, etc.), with conditions about Zenith and trinkets. The guide says "use it as soon as it's available" but SimC delays it to avoid using during Zenith windows. This is a deliberate SimC optimization difference. | MEDIUM |
| W2 | **Zenith usage has dedicated sub-APL in SimC but not a numbered priority in Wowhead.** Wowhead discusses Zenith in the opener and as general advice but doesn't put it in the ST priority list. SimC has an entire dedicated zenith action list with 13+ conditionals for optimal timing. This is a SimC-specific optimization layer. | MEDIUM |
| W3 | **Wowhead priority is much simpler than SimC APL.** Wowhead's ~11 step priority becomes 30+ lines in SimC with Heart of the Jade Serpent, Bloodlust, Zenith, flurry_charge, and trinket-specific conditionals. This is expected (SimC needs explicit conditions), but some Wowhead priorities may not map 1:1. | INFO |
| W4 | **Combo Strike mechanic thoroughly enforced in SimC.** Nearly every action checks `combo_strike`. Wowhead doesn't mention this in the priority list (it's covered elsewhere as "Don't Repeat Abilities"). SimC correctly enforces this. | OK |
| W5 | **Rushing Wind Kick present in both.** SimC has rushing_wind_kick in both ST and multi-target lists. Wowhead lists it at priority #5. SimC positions it after FoF/WDP in ST. Class module has full rushing_wind_kick_t implementation. | OK |
| W6 | **Flurry Charge tracking in SimC but not in Wowhead.** SimC checks buff.flurry_charge.stack=30 for FoF timing. Wowhead doesn't mention flurry charge stacks in the priority. | LOW |
| W7 | **Celestial Conduit sub-APL (big_coc) is very detailed in SimC.** Multiple conditions for Invoke Xuen, Celestial Conduit timing around Heart of the Jade Serpent, which matches Wowhead's CotC-specific advice about not overlapping HotJS buffs. | OK |

### Tier Set Bonuses (Windwalker)

**Wowhead Data (Way of Ra-den's Chosen):**
- 2pc: Strike of the Windlord and Whirling Dragon Punch damage increased by 30%
- 4pc: Cooldowns of Strike of the Windlord and Whirling Dragon Punch reduced by 5 sec

**SimC Implementation:**

| # | Issue | Severity |
|---|-------|----------|
| WT1 | **Windwalker tier set bonuses NOT FOUND in code.** The tier struct in sc_monk.hpp only has brm_2pc, brm_4pc, brm_4pc_extra_kick under mid1. There are NO ww_2pc/ww_4pc entries. The mid1 struct has no Windwalker-specific fields. | HIGH |
| WT2 | **No WINDWALKER MID1 set bonus registration.** sc_monk.cpp tier initialization (line 5657-5659) only registers MONK_BREWMASTER sets. No sets->set(MONK_WINDWALKER, MID1, ...) calls found. | HIGH |

**NOTE:** This is a CRITICAL finding. The Windwalker Monk Midnight Season 1 tier set bonuses (30% damage to SotW/WDP, 5s CDR to SotW/WDP) appear to NOT be implemented in SimC at all. However, Wowhead notes these bonuses are "relatively benign" (3-5% gain, no rotation changes), so they may be handled by the automated set bonus parsing system rather than explicit code. A deeper check of the spell data auto-parse system would be needed to confirm.

### Key Talent Effects (Windwalker)

| Talent | Implemented? | Notes |
|--------|-------------|-------|
| Zenith | YES | Full implementation: zenith_t struct, buff, CDR on BoK, 2 charges |
| Weapon of Wind | YES | parse_effects(buff.zenith, talent.windwalker.weapon_of_wind) — implemented 2026-03-22 |
| Rushing Wind Kick | YES | Full rushing_wind_kick_t with AoE scaling |
| Fists of Fury | YES | Extensive APL and class module support |
| Rising Sun Kick | YES | Full implementation |
| Whirling Dragon Punch | YES | In APL and class module |
| Strike of the Windlord | YES | In APL and class module |
| Combo Breaker | YES | buff.combo_breaker tracked, APL checks stacks |
| Dance of Chi-Ji | YES | buff.dance_of_chiji in APL and class module |
| Flurry Strikes (Shado-Pan) | YES | buff.flurry_charge, multiple APL references |
| Heart of the Jade Serpent (CotC) | YES | Multiple buff variants tracked (unity_within, yulons_avatar) |
| Celestial Conduit | YES | Dedicated big_coc action list |
| Invoke Xuen | YES | In coc action list, cooldown tracked |
| Touch of Death | YES | touch_of_death_t with health threshold checks |
| Touch of Karma | NO (APL) | Not in SimC damage APL (defensive only, expected for DPS sim) |
| Obsidian Spiral | YES | Referenced in APL conditionals |
| Teachings of the Monastery | YES | Coded in class module |
| Tigereye Brew | YES | buff.tigereye_brew_1, tigereye_brew_3 in header |
| Shadowboxing Treads | YES | In multi-target APL |
| Crane Vortex | YES | In multi-target APL |
| Slicing Winds | YES | slicing_winds action in both ST and multi-target |

---

## SUMMARY OF CRITICAL ISSUES

### HIGH Severity
1. **[B1] Brewmaster: Touch of Death missing from APL** — Wowhead's #1 priority ability is entirely absent from the Brewmaster default APL.
2. **[B2] Brewmaster: Blackout Combo sequencing not in APL** — The key Blackout Kick -> Tiger Palm interaction that Wowhead emphasizes is not reflected in the APL ordering. Blackout Kick is near the bottom instead of being a high priority.
3. **[WT1/WT2] Windwalker: Tier set bonuses possibly not implemented** — No explicit Windwalker MID1 tier set code found. May be handled by auto-parse, but requires verification.

### MEDIUM Severity
4. **[B3] Brewmaster APL is Master of Harmony-focused** — Many conditionals are for Aspect of Harmony. Shado-Pan players following Wowhead's guide may not get optimal results.
5. **[B4] Brewmaster: Spinning Crane Kick missing from APL** — AoE filler ability not included.
6. **[W1] Windwalker: Touch of Death priority differs** — Wowhead says use ASAP, SimC delays for Zenith windows.
7. **[W2] Windwalker: Zenith optimization layer** — SimC has extensive Zenith timing logic not present in Wowhead's simple priority.

### LOW Severity
8. **[B5] Brewmaster: Invoke Niuzao priority placement differs**
9. **[W6] Windwalker: Flurry charge tracking in SimC only**

### OK (Matching/Expected)
- Brewmaster tier set bonuses: Fully implemented
- Core Windwalker rotation abilities: All present
- Combo Strike enforcement: Properly coded
- Rushing Wind Kick: Fully implemented (new for Midnight)
- Weapon of Wind: Implemented as of 2026-03-22
- Hero talent handling: Both Shado-Pan and CotC conditionals present
- Key defensive talents: Stagger, Shuffle, Purifying Brew all coded

# Druid Spec Audit Report: Wowhead vs SimC APL/Code
# Generated: 2026-03-24
# Specs Audited: Balance, Feral, Guardian

===========================================================================
## 1. BALANCE DRUID
===========================================================================

### Source Files:
- Wowhead rotation: wowhead/druid/balance/extracted/rotation.md
- Wowhead tier: wowhead/druid/balance/extracted/tier.md
- APL: engine/class_modules/apl/balance_apl.inc (107 lines)
- Class module: engine/class_modules/sc_druid.cpp

### APL Structure:
- precombat, default, kotg_st (Keeper ST), ec_st (Elune's Chosen ST), aoe
- Hero talent branching: CORRECT (line 28-30: kotg_st for keeper, ec_st for elune's chosen)

### ROTATION COMPARISON (Keeper of the Grove, Single-Target):

Wowhead Priority (lines 24-33):
  1. Apply Moonfire (pandemic)
  2. Apply Sunfire (pandemic, or before Force of Nature)
  3. Fury of Elune during Eclipse or before Force of Nature
  4. Force of Nature if not in Eclipse, next cast is Solar Eclipse or CA
  5. Celestial Alignment after Force of Nature, save charge for Convoke
  6. Convoke the Spirits if below 40 AP and Force of Nature active
  7. Enter Solar Eclipse when Starlord expires with procs or FoN overlap
  8. Starfall to consume Starweaver's Warp
  9. Starsurge for movement/AP cap/Starweaver's Weft/Touch the Cosmos
  10. Wrath to generate AP

APL kotg_st (lines 32-56):
  1. Moonfire (pandemic/refreshable) -- MATCHES
  2. Sunfire (pandemic/refreshable) -- MATCHES
  3. Fury of Elune (AP deficit check) -- MATCHES
  4. Solar Eclipse (if charges_fractional=2, prevent overcap) -- PARTIAL MATCH
  5. Celestial Alignment (kotg_cd_condition) -- MATCHES (uses harmony_of_the_grove)
  6. Incarnation (same condition) -- MATCHES
  7. Trinkets/Potion during CA -- OK
  8. Force of Nature (eclipse_down & ca_inc ready or eclipse ready) -- MATCHES
  9. Solar Eclipse (eclipse_condition) -- MATCHES
  10. Starfall (starweaver procs) -- MATCHES
  11. Starsurge (ascendant_stars, eclipse_remains, starlord) -- MATCHES
  12. Sunfire/Moonfire refresh -- MATCHES
  13. Starsurge (convoke ready + ca_inc) -- EXTRA (prep for Convoke)
  14. Convoke the Spirits (ca_inc.up & harmony) -- MATCHES
  15. Wrath (ascendant_fires) -- EXTRA detail
  16. New/Half/Full Moon -- EXTRA (Wowhead doesn't mention moon phases)
  17. Starsurge (Starweaver procs) -- MATCHES
  18. Starsurge (prevent AP cap) -- MATCHES
  19. Wild Mushroom -- EXTRA (Wowhead doesn't mention)
  20. Wrath (filler) -- MATCHES

### MISSING:
- [MINOR] Convoke below 40 AP condition (Wowhead line 29): APL checks
  ca_inc.up & harmony_of_the_grove.up (line 48), but does NOT check AP<40.
  This may cause Convoke to be cast at higher AP wasting potential AP gen.

### WRONG_ORDER:
- [LOW] Force of Nature is at position 8 in APL (after CA), but Wowhead says
  it should be at position 4 (before CA). The APL does handle the interaction
  via kotg_cd_condition requiring harmony_of_the_grove.up (which comes from
  Force of Nature), so the dependency is somewhat implicit. The earlier
  solar_eclipse line (35) acts as an overcap prevention.
  
- [LOW] APL has an extra solar_eclipse line (35) for charges_fractional=2
  that fires before Force of Nature. This is an overcap prevention not
  explicitly mentioned in Wowhead but is a valid optimization.

### MISSING_MECHANIC:
- [NONE CRITICAL] Tier set 2pc (Shooting Stars +40% damage, +2 AP outside
  Eclipse): IMPLEMENTED in sc_druid.cpp line 7969 (AP generation) and via
  spell data effects.
- [NONE CRITICAL] Tier set 4pc (30% chance exploding Shooting Star):
  IMPLEMENTED in sc_druid.cpp line 11625-11626 (shooting_stars_mid1 action).
- [OK] Control of the Dream CDR: This is a passive talent effect, handled
  in the class module not the APL.
- [OK] Solstice tracking: Present in passive_asp variable (line 22).
- [OK] Starlord tracking: Present in eclipse_condition and starsurge conditions.
- [OK] Ascendant Stars/Fires: Handled in APL lines 44,49.

### CONDITION_ISSUES:
- [MEDIUM] Wowhead says "Convoke if below 40 AP and Force of Nature active"
  (line 29). APL condition is "buff.ca_inc.up&buff.harmony_of_the_grove.up"
  (line 48). Missing the AP<40 check. This could result in AP overcapping
  during Convoke.

- [LOW] Wowhead says "Enter Solar Eclipse whenever Starlord expires" (line 30).
  APL uses "buff.starlord.stack<3" (line 16/42) which is similar but not
  exactly "expires" -- it's "not full stacks" which is more aggressive.

### OTHER:
- [INFO] APL includes Wild Mushroom (lines 55,79,103) which Wowhead rotation
  doesn't mention. This is likely a DPS gain from Fungal Growth talent.
- [INFO] APL includes New Moon/Half Moon/Full Moon cycle (lines 50-52, 74-76,
  100-102) which Wowhead doesn't discuss. These are talents that may or may
  not be taken depending on build.
- [CRITICAL] Balance is noted to have low DPS due to "talent hash issues."
  This is NOT an APL problem -- it's likely that the default talent string
  loaded by SimC doesn't match the recommended Wowhead talents. The APL
  itself appears well-constructed. The issue is upstream in profile/talent
  configuration.

### Elune's Chosen ST Comparison:

Wowhead EC Priority (lines 427-434):
  1. Moonfire (pandemic)
  2. Sunfire (pandemic)  
  3. Incarnation if not in Lunar Eclipse and Fury of Elune ready
  4. Fury of Elune on CD
  5. Enter Lunar Eclipse if >90% AP and about to overcap charges or FoE available
  6. Starsurge (Touch the Cosmos)
  7. Starsurge (prevent cap / Ascendant Eclipses)
  8. Starfire to generate AP

APL ec_st (lines 58-81):
  1. Moonfire -- MATCHES
  2. Sunfire -- MATCHES
  3. Fury of Elune -- MATCHES (position shifted)
  4. Celestial Alignment/Incarnation -- MATCHES
  5. Lunar Eclipse -- MATCHES
  6. Starfall (Starweaver procs) -- EXTRA for Starweaver build
  7. Starsurge (ascendant_stars/starlord) -- MATCHES
  8. Convoke -- PRESENT (Wowhead EC doesn't emphasize Convoke in Rattle build)
  9. Starfire (lunar_calling) -- MATCHES
  10. Wrath (fallback) -- MATCHES

### CONDITION_ISSUES (EC):
- [MEDIUM] Wowhead says "Enter Lunar Eclipse if above 90% AP" (line 431).
  APL condition (line 66): "variable.eclipse_condition" which requires
  astral_power>=60 (for non-starweaver). 60 AP is NOT 90% AP (max is 120).
  This means APL enters Eclipse earlier than Wowhead recommends for EC.

- [LOW] Wowhead EC says Incarnation "if not in Lunar Eclipse and Fury of
  Elune is off cooldown" (line 429). APL ec_cd_condition (line 18) has a
  complex trinket-based condition that doesn't explicitly check FoE cooldown.


===========================================================================
## 2. FERAL DRUID  
===========================================================================

### Source Files:
- Wowhead rotation: wowhead/druid/feral/extracted/rotation.md
- Wowhead tier: wowhead/druid/feral/extracted/tier.md
- APL: engine/class_modules/apl/feral_apl.inc (86 lines)
- Class module: engine/class_modules/sc_druid.cpp

### APL Structure:
- precombat, default, builder, finisher, aoe_builder, aoe_finisher, cooldown,
  cd_variable
- NO hero talent branching in APL (both DotC and Wildstalker use same APL)

### ROTATION COMPARISON (Druid of the Claw, Single-Target):

Wowhead Priority (lines 21-39):
  1. Ferocious Bite with Apex Predator's Craving
  2. Rip: 4+ CP, missing/pandemic, Tiger's Fury up (or TF won't be up before expires)
  3. Ferocious Bite: 5+ CP during Berserk / 4+ CP outside Berserk, Rip active
  4. Berserk + Convoke synced with Tiger's Fury
  5. If TF coming off CD in 3s and >80% energy, dump energy
  6. Tiger's Fury on CD
  7. Rake: missing/pandemic, snapshot upgrade, <2s left
  8. Moonfire: missing/pandemic, snapshot upgrade, <2s left
  9. Shred to generate CPs

APL default (lines 19-32):
  1. Prowl if not in Berserk -- OK
  2. Cat Form -- OK
  3. Auto attack -- OK
  4. Tiger's Fury -- DIFFERENT ORDER (Wowhead #6, APL #4 in default)
  5. Rake from stealth -- MATCHES opener
  6. Chomp -- EXTRA (Wowhead mentions Chomp in separate tab, not in main ST)
  7. Ferocious Bite (Apex procs) -- MATCHES #1
  8. Call cooldown list -- covers Berserk/Convoke
  9. Call finisher (4+ CP ST) / aoe_finisher (4+ CP AoE)
  10. Call builder (ST) / aoe_builder (AoE)

APL finisher (lines 82-86):
  1. Rip (refreshable, TF or remains<TF CD) -- MATCHES #2
  2. Pool resource / Ferocious Bite (ravage/saber_jaws logic) -- MATCHES #3
  3. Ferocious Bite (max_energy) -- MATCHES

APL builder (lines 43-47):
  1. Prowl (stealth for Pouncing Strikes) -- MATCHES
  2. Shadowmeld -- EXTRA (not mentioned in Wowhead)
  3. Rake (snapshot logic) -- MATCHES #7
  4. Moonfire (snapshot logic) -- MATCHES #8
  5. Shred -- MATCHES #9

### MISSING:
- [LOW] Wowhead says "If TF coming off CD within 3 seconds and >80% energy,
  dump energy" (line 29). The APL does NOT explicitly have this energy dump
  condition before Tiger's Fury. TF is just cast unconditionally on CD
  (line 23). The APL's pool_resource mechanic partially handles this.

- [LOW] Wowhead mentions specific CP thresholds: "5+ CP during Berserk,
  4+ CP outside Berserk" for Ferocious Bite (lines 26-27). The APL uses
  combo_points>=4 universally (line 28-29). During Berserk with extra CP
  generation, this is functionally similar but technically different.

### WRONG_ORDER:
- [LOW] Tiger's Fury is higher in APL priority (line 23, unconditional)
  vs Wowhead where it's listed as priority #6 after finishers. However,
  in SimC, Tiger's Fury is off-GCD so this doesn't actually conflict --
  it fires between GCDs regardless of position.

### MISSING_MECHANIC:
- [OK] Tier 2pc (Clearcasting -> 5% crit): IMPLEMENTED via flash_of_clarity
  buff (sc_druid.cpp line 11027, triggered at line 9596).
- [OK] Tier 4pc (Rake +20%, Clearcasting Shred/Swipe +15%): The Rake +20%
  is likely handled via spell data aura effects. The Clearcasting bonus to
  Shred/Swipe appears to be handled via the set bonus spell data.
  NOTE: Only B2 is explicitly visible in code searches. B4 implementation
  may be through automatic spell data parsing without explicit B4 code
  references. NEEDS VERIFICATION.
- [OK] Snapshotting: APL has persistent_multiplier checks (lines 45-46).
- [OK] Apex Predator's Craving: Handled (line 27).
- [OK] Claw Rampage / Ravage: Present in finisher/aoe_finisher (buff.ravage).
- [OK] Chomp: Implemented in class module and APL (line 26).

### CONDITION_ISSUES:
- [LOW] Wowhead AoE says "Swipe during Berserk for Claw Rampage procs"
  (line 75, DotC only). APL aoe_builder line 35 has this exact condition:
  "hero_tree.druid_of_the_claw&buff.bs_inc.up|buff.clearcasting.up". MATCHES.

- [LOW] Wowhead says Feral Frenzy "on cooldown" in AoE (line 74). APL has
  feral_frenzy at cooldown level with CP check (line 61). This means in AoE,
  Feral Frenzy may be delayed if CP is too high. Minor difference.

- [INFO] Wowhead Wildstalker AoE says "Swipe with Clearcasting procs up to
  7 targets" (line 449). APL aoe_builder (line 35) doesn't have the 7-target
  cap for Wildstalker Clearcasting Swipe. May be a minor AoE DPS difference.

### OTHER:
- [INFO] APL has complex trinket management (cd_variable list, lines 65-80)
  that Wowhead doesn't discuss. This is a SimC optimization.
- [INFO] APL references Algethar Puzzle Box (lines 14-15) which is likely
  outdated gear from a previous season.
- [OK] Frantic Frenzy is in APL (line 62) -- this is a Druid of the Claw
  cooldown, appropriately placed.
- [INFO] No explicit hero talent branching in APL for DotC vs Wildstalker.
  The APL handles both via conditional checks on hero_tree/talents.


===========================================================================
## 3. GUARDIAN DRUID
===========================================================================

### Source Files:
- Wowhead rotation: wowhead/druid/guardian/extracted/rotation.md
- Wowhead tier: wowhead/druid/guardian/extracted/tier.md
- APL: engine/class_modules/apl/guardian_apl.inc (31 lines)
- Class module: engine/class_modules/sc_druid.cpp

### APL Structure:
- precombat, default, assisted_combat, cooldowns
- CRITICAL: The APL is labeled "assisted_combat" and explicitly comments
  "This is for Blizzard automation and is not included in the game's
  Assisted Combat system." This is a PLACEHOLDER/MINIMAL APL, not a
  fully optimized rotation.

### ROTATION COMPARISON (DotC Single-Target):

Wowhead Priority (lines 20-29):
  1. Maintain Moonfire
  2. Maintain 3-5 stacks of Thrash
  3. Red Moon on cooldown
  4. Mangle on cooldown
  5. Thrash on cooldown
  6. Spend Rage: Maul (offense) / Ironfur (defense)
  7. Frenzied Regeneration if low health
  8. Moonfire with Galactic Guardian procs
  9. Barkskin/Incarnation frequently
  10. Swipe as filler

APL assisted_combat (lines 12-24):
  1. Berserk -- PRESENT (unconditional)
  2. Convoke the Spirits -- PRESENT (unconditional, then again with range check??)
  3. Thrash if >3 enemies -- PARTIALLY matches #2/#5
  4. Lunar Beam -- PRESENT (Wowhead mentions in separate tab)
  5. Convoke (range check) -- DUPLICATE?
  6. Moonfire if not ticking -- MATCHES #1
  7. Mangle -- MATCHES #4
  8. Thrash -- MATCHES #5
  9. Moonfire (Galactic Guardian) -- MATCHES #8
  10. Maul if rage>=8 -- PARTIALLY matches #6
  11. Swipe -- MATCHES #10
  12. Moonfire (ranged filler)

### MISSING:
- [CRITICAL] Red Moon: NOT in APL at all. Wowhead lists it as priority #3.
  Red Moon is a Guardian talent (confirmed in sc_druid.cpp line 1059).
  This is a significant DPS loss.

- [CRITICAL] Ironfur: NOT in APL. This is the primary defensive rage spender.
  While SimC focuses on DPS, Ironfur is missing entirely.

- [CRITICAL] Frenzied Regeneration: NOT in APL. Core defensive ability.

- [CRITICAL] Incarnation: Guardian of Ursoc: NOT in APL. Major cooldown.

- [CRITICAL] Barkskin: NOT in APL. Important defensive cooldown that Wowhead
  says should be used frequently.

- [MEDIUM] Heart of the Wild: NOT in APL. Mentioned in Wowhead as a DPS
  cooldown when used in Cat Form (casts Feral Frenzy).

- [MEDIUM] Raze: NOT in APL. Raze replaces Maul in AoE for DotC.

- [LOW] Harnessed Rage mechanic: Wowhead emphasizes staying above 80 rage
  for Maul casts (lines 36-37). APL just uses rage>=8 for Maul.

### WRONG_ORDER:
- [HIGH] Moonfire (not ticking) is at position 6 in APL but #1 in Wowhead.
  Maintaining Moonfire should be highest priority.

- [HIGH] Mangle is at position 7 in APL but #4 in Wowhead. After Thrash
  stacks are up, Mangle should be very high priority for rage generation.

- [MEDIUM] Thrash AoE-only (>3 enemies) is position 3 in APL, but Wowhead
  says maintain 3-5 stacks always (#2). The APL has a second unconditional
  Thrash at position 8 but that's too low in priority.

### MISSING_MECHANIC:
- [OK] Tier 2pc (Raze/Maul/Ravage +10%, Moonfire +10%): IMPLEMENTED via
  spell data (sc_druid.cpp has DRUID_GUARDIAN MID1 B2 references).
- [OK] Tier 4pc (Raze/Maul/Ravage 5% Galactic Guardian proc, Moonfire
  periodic -> next Raze/Maul/Ravage strikes again): IMPLEMENTED via
  celestial_might buff and repeat_action logic (sc_druid.cpp lines 5633,
  5686, 5710, 7690-7692).
- [MISSING] Galactic Guardian proc priority in 4pc context: Wowhead says
  save Ravage proc for 4pc procs. APL has no such logic.

### CONDITION_ISSUES:
- [CRITICAL] Maul condition is "rage>=8" (line 21). This is absurdly low.
  Wowhead emphasizes Harnessed Rage synergy requiring rage>=80 ideally.
  The condition should likely be rage>=80 for optimal DPS, with a fallback
  at lower rage levels to prevent capping.

- [HIGH] Berserk is unconditional (line 12). Wowhead says to use it as
  a major cooldown strategically. Should at minimum have a fight_remains
  or target count condition.

- [HIGH] Convoke appears TWICE in the APL (lines 13 and 16), once
  unconditional and once with distance check. This looks like a bug.

### OTHER:
- [CRITICAL] The Guardian APL is essentially a STUB/PLACEHOLDER. The comment
  on line 12 says "This is for Blizzard automation and is not included in
  the game's Assisted Combat system." This confirms it was not designed as
  a proper SimC APL. Guardian needs a COMPLETE APL REWRITE.

- [INFO] Lunar Beam is present (line 15), which matches Wowhead guidance.

- [INFO] The APL has no rage management logic, no defensive cooldown usage,
  and no Druid of the Claw vs Elune's Chosen branching.


===========================================================================
## SUMMARY OF CRITICAL ISSUES
===========================================================================

### BALANCE:
1. [MEDIUM] Convoke AP<40 condition missing from APL
2. [MEDIUM] EC Eclipse entry at 60 AP instead of Wowhead's 90% AP (108 AP)
3. [CRITICAL-EXTERNAL] Low DPS likely from talent hash mismatch, not APL
   The APL itself is well-constructed and comprehensive.

### FERAL:
1. [LOW] Energy dump before Tiger's Fury not explicitly coded
2. [LOW] No Feral 4pc (B4) explicit code found -- may rely on auto-parsing
3. [LOW] Algethar Puzzle Box reference is outdated
4. [LOW] Wildstalker 7-target Clearcasting Swipe cap missing
Overall: Feral APL is WELL-CONSTRUCTED and closely matches Wowhead guidance.

### GUARDIAN:
1. [CRITICAL] APL is a PLACEHOLDER, not a real rotation
2. [CRITICAL] Red Moon completely missing
3. [CRITICAL] Ironfur, Frenzied Regeneration, Incarnation, Barkskin missing
4. [CRITICAL] Raze missing
5. [CRITICAL] Heart of the Wild missing
6. [CRITICAL] No rage management logic (Harnessed Rage)
7. [CRITICAL] No hero talent branching
8. [HIGH] Maul rage threshold is 8 instead of ~80
9. [HIGH] Priority ordering doesn't match Wowhead at all
10. [HIGH] Convoke appears twice (likely bug)
Guardian needs a COMPLETE APL REWRITE to match Wowhead guidance.

### TIER SET IMPLEMENTATION STATUS:
- Balance 2pc: IMPLEMENTED (Shooting Stars damage + AP gen)
- Balance 4pc: IMPLEMENTED (exploding Shooting Star proc)
- Feral 2pc: IMPLEMENTED (flash_of_clarity crit buff)
- Feral 4pc: LIKELY IMPLEMENTED via spell data (no explicit B4 code)
- Guardian 2pc: IMPLEMENTED (damage increases via spell data)
- Guardian 4pc: IMPLEMENTED (celestial_might mechanics)

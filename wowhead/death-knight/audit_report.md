# Death Knight SimC APL vs Wowhead Rotation Audit Report
Generated: 2026-03-24

APL Source: engine/class_modules/apl/apl_death_knight.cpp
Class Module: engine/class_modules/sc_death_knight.cpp
Wowhead Data: wowhead/death-knight/{blood,frost,unholy}/extracted/

================================================================================
## BLOOD DEATH KNIGHT
================================================================================

### Deathbringer — Single Target

Wowhead Priority (lines 21-29 of rotation.md):
  1. Death Strike if healing needed or >75 RP
  2. Maintain Bone Shield >=5 (Marrowrend)
  3. Death and Decay if not buffed
  4. Reaper's Mark on CD
  5. Dancing Rune Weapon on CD
  6. Blood Boil if DRW active & no Blood Plague, or about to cap
  7. Blood Boil if Boiling Point proc
  8. Blood Boil as filler
  9. Heart Strike as filler

APL deathbringer list (lines 139-153):
  1. Death Strike if RP deficit <20 (or <26 during DRW)
  2. Death's Caress if Bone Shield missing/expiring/<5 & rune<4
  3. Marrowrend if Bone Shield missing/expiring/<5
  4. Death and Decay if not up
  5. Reaper's Mark
  6. Marrowrend if Exterminate up
  7. Blood Boil if DRW up & no Blood Plague
  8. Blood Boil if charges=2
  9. Death Strike (filler)
  10. Blood Boil if Boiling Point
  11. Consumption empower_to=1 if no DRW
  12. Blood Boil (filler)
  13. Heart Strike
  14. Consumption empower_to=1

#### WRONG_ORDER [BLOOD-DB-1]: Blood Boil Boiling Point vs charges cap
  Wowhead: Boiling Point (step 7) BEFORE charge cap prevention (step 6 "about to cap")
  APL: charges=2 (line 146) BEFORE Boiling Point (line 148), with a Death Strike between
  Impact: Minor — APL delays Boiling Point procs relative to Wowhead recommendation.

#### MISSING [BLOOD-DB-2]: Consumption not in Wowhead rotation
  APL lines 149, 152: Consumption empower_to=1 appears twice in APL
  Wowhead: Consumption is never mentioned in Deathbringer ST/AoE rotation priority
  Impact: Minor — Consumption is a talent choice; may not be default build.

#### CONDITION_ISSUES [BLOOD-DB-3]: Extra Death Strike filler at mid-priority
  APL line 147: Death Strike appears as a second, unconditional filler between
  Blood Boil charges=2 and Boiling Point.
  Wowhead: Death Strike only at top priority when healing/75+ RP.
  Impact: Moderate — APL spends more RP on Death Strike than Wowhead suggests.

#### MISSING [BLOOD-DB-4]: Death's Caress for Bone Shield not in Wowhead
  APL line 140: deaths_caress for Bone Shield maintenance
  Wowhead: Only mentions Marrowrend for Bone Shield; Death's Caress only in opener.
  Impact: Minor — Death's Caress is a ranged bone generator, situational.

#### OTHER [BLOOD-DB-5]: Marrowrend + Exterminate mechanic
  APL line 144: marrowrend,if=buff.exterminate.up
  Wowhead: Does not explicitly list "cast Marrowrend with Exterminate" in rotation.
  Wowhead line 40 mentions Exterminate in Bone Shield management section but not as
  a direct rotation step.
  Impact: Moderate — APL has specific Deathbringer mechanic not in Wowhead priority.

#### CONDITION_ISSUES [BLOOD-DB-6]: Dancing Rune Weapon conditions
  APL line 137 (high_prio_actions): DRW gated on !exterminate & !reapers_mark & !drw
  Wowhead line 25: "Cast Dancing Rune Weapon on cooldown"
  Impact: Minor — APL is more nuanced to avoid overlap; Wowhead simplifies.

---

### San'layn — Gift of the San'layn (DRW active)

Wowhead Priority (lines 237-242):
  1. Death Strike if healing needed or >75 RP
  2. Maintain Bone Shield >=5
  3. Blood Boil if DRW Blood Plague not on target
  4. Death and Decay if Crimson Scourge proc
  5. Fill with Vampiric Strike
  6. Blood Boil if out of runes

APL san_gift (lines 155-163):
  1. Heart Strike if Essence of Blood Queen expiring (<1.5s)
  2. Death Strike if RP deficit <36
  3. Blood Boil if DRW BP not ticking
  4. Any DnD if Crimson Scourge
  5. Heart Strike if EotBQ stack <7
  6. Death Strike
  7. Blood Boil if Boiling Point & no echo
  8. Heart Strike
  9. Blood Boil

#### MISSING_MECHANIC [BLOOD-SL-1]: Essence of Blood Queen tracking
  APL lines 155, 159: Tracks EotBQ remaining (<1.5s) and stacks (<7)
  Wowhead: Does not mention EotBQ stack/duration tracking in the Gift rotation.
  Wowhead only mentions EotBQ in the flavor text (line 234).
  Impact: Significant — APL has critical EotBQ maintenance logic absent from Wowhead.

#### CONDITION_ISSUES [BLOOD-SL-2]: RP threshold during Gift
  APL line 156: Death Strike at RP deficit <36 (roughly 89+ RP)
  Wowhead line 237: Death Strike at 75 RP
  Impact: Minor — APL is more conservative with RP during Gift window.

#### MISSING [BLOOD-SL-3]: No explicit Bone Shield maintenance in Gift
  Wowhead line 238: "Maintain at least 5 charges of Bone Shield" during Gift
  APL san_gift: No bone shield check at all in Gift of San'layn list
  Impact: Minor — DRW+Marrowrend auto-generates bones; may be unnecessary.

---

### San'layn — Outside DRW

Wowhead Priority (lines 244-250):
  1. Death Strike if >75 RP
  2. Maintain Bone Shield >=5 (Marrowrend)
  3. Death and Decay if not buffed / Crimson Scourge
  4. Blood Boil if Boiling Point
  5. Vampiric Strike if available
  6. Blood Boil to prevent cap
  7. Heart Strike

APL sanlayn (lines 165-177):
  1. Death Strike if RP deficit <20
  2. Death's Caress if Bone Shield issues
  3. Marrowrend if Bone Shield issues
  4. Blood Boil if no Blood Plague
  5. Any DnD if Crimson Scourge
  6. Consumption empower_to=1
  7. Blood Boil if Boiling Point & no echo
  8. Heart Strike if Vampiric Strike up
  9. Death Strike
  10. Blood Boil if charges=2
  11. Heart Strike if rune>=2
  12. Blood Boil
  13. Heart Strike

#### WRONG_ORDER [BLOOD-SL-4]: Death and Decay / Blood Plague priority
  Wowhead: DnD (step 3) before any Blood Boil
  APL: Blood Boil if no Blood Plague (line 168) BEFORE DnD (line 169)
  Impact: Minor — APL ensures plague is up before DnD, Wowhead bundles differently.

#### MISSING [BLOOD-SL-5]: Consumption in APL not in Wowhead
  APL line 170: Consumption empower_to=1
  Wowhead: Not mentioned in San'layn rotation.
  Impact: Minor — talent-dependent.

#### CONDITION_ISSUES [BLOOD-SL-6]: Extra Death Strike filler
  APL line 173: Unconditional Death Strike as mid-priority filler
  Wowhead: Only at top when healing/75+ RP.
  Impact: Same as BLOOD-DB-3.

---

### Blood Tier Set (Relentless Rider's Lament)
  2pc: Blood Boil +8% damage, 3 RP per cast (incl. Boiling Point echoes)
  4pc: Death Strike +8% damage, 10% chance for extra Blood Boil charge
  
  Code: CONFIRMED at lines 8663 (2pc RP gen), 9698 (4pc charge refund), 14937 (spell lookup)
  Wowhead: "No rotational changes" — MATCHES APL (no rotation changes for tier)
  Status: IMPLEMENTED CORRECTLY

---

### Blood Opener
  Wowhead Deathbringer Opener (lines 100-106):
    1. Death's Caress
    2. Pre-place Death and Decay
    3. Reaper's Mark
    4. Dancing Rune Weapon
    5. Blood Boil
    6. Death Strike
    7. Normal priority

  APL precombat (lines 119-120):
    1. snapshot_stats
    2. deaths_caress

#### MISSING [BLOOD-OP-1]: Opener sequence incomplete
  APL precombat only has Death's Caress. Missing: Death and Decay pre-place,
  Reaper's Mark before DRW ordering.
  Impact: Minor — SimC precombat is intentionally minimal; rotation handles the rest.


================================================================================
## FROST DEATH KNIGHT
================================================================================

### Deathbringer — Single Target

Wowhead Priority (lines 21-33):
  1. Empower Rune Weapon if 2 charges
  2. Reaper's Mark
  3. Pillar of Frost
  4. Breath of Sindragosa
  5. Frostwyrm's Fury if no active RM or Exterminate
  6. Obliterate if 2 KM stacks, or Exterminate
  7. Howling Blast with Rime
  8. Frost Strike to avoid RP waste
  9. Obliterate with KM
  10. Empower Rune Weapon to generate KM
  11. Frost Strike
  12. Obliterate without KM
  13. Howling Blast (filler)

APL cooldowns (lines 215-229) + single_target (lines 244-254):

Cooldowns:
  - Remorseless Winter (!)
  - Reaper's Mark (gated on Pillar CD)
  - Pillar of Frost
  - Breath of Sindragosa
  - Frostwyrm's Fury (complex multi-line conditions)
  - Raise Dead
  - Empower Rune Weapon (4 different condition lines)

Single Target:
  1. Obliterate if KM=2 or (KM & rune>=3)
  2. Howling Blast if Rime & Frostbound Will
  3. Frost Strike if Razorice=5 & Shattering Blade & not pooling
  4. Howling Blast if Rime
  5. Obliterate if Exterminate
  6. Howling Blast if Frostbane
  7. Frost Strike if not Shattering Blade & RP deficit <30
  8. Obliterate if KM & not rune pooling
  9. Frost Strike if not RP pooling
  10. Obliterate if not pooling & not (Obliteration+PoF)
  11. Howling Blast if no KM & Obliteration+PoF

#### MISSING [FROST-DB-1]: Remorseless Winter absent from Wowhead
  APL line 216: remorseless_winter with conditions for sending_cds
  Wowhead: NEVER mentions Remorseless Winter in any rotation priority.
  Wowhead line 39 mentions Frozen Dominion makes it "automatic passive" but
  it IS in the APL as a manually-cast ability.
  Impact: Significant — APL casts Remorseless Winter; Wowhead never tells you to.

#### CONDITION_ISSUES [FROST-DB-2]: Empower Rune Weapon conditions
  Wowhead line 21: "ERW if you have 2 charges" (simple)
  APL lines 226-229: Four complex ERW conditions involving runes, KM react,
  RP levels, cooldown alignment, breath timings.
  Wowhead line 30: "ERW to generate Killing Machine" (simple)
  Impact: Moderate — APL is far more nuanced; Wowhead oversimplifies ERW usage.

#### MISSING [FROST-DB-3]: Shattering Blade / Razorice conditions
  APL lines 246, 264: Frost Strike with Shattering Blade & Razorice=5 conditions
  Wowhead: No mention of Shattering Blade or Razorice stack tracking.
  Impact: Moderate — talent-specific optimization present in APL but not Wowhead.

#### MISSING [FROST-DB-4]: Frostbane proc handling
  APL line 249: howling_blast,if=buff.frostbane.react
  APL line 263 (AoE): howling_blast,if=buff.frostbane.react
  Wowhead: Frostbane never mentioned in rotation.
  Impact: Moderate — Rider of the Apocalypse talent; APL handles it, Wowhead doesn't.

#### WRONG_ORDER [FROST-DB-5]: Obliterate + Exterminate position
  Wowhead: Exterminate Obliterate at position 6 (after Howling Blast w/ Rime)
  APL: Exterminate at position 5 (line 248), after Rime+Frostbound but before plain Rime
  With Frostbound Will talented, the order is: KM2->Rime(FW)->Shattering->Rime->Exterminate
  Without Frostbound: KM2->Rime->Exterminate... wait, Rime is at line 247 which is before 248.
  So APL actually matches Wowhead: Rime before Exterminate.
  Impact: NONE — orders align on closer inspection.

#### CONDITION_ISSUES [FROST-DB-6]: Frostwyrm's Fury conditions
  Wowhead line 25: "FWF if no active Reaper's Mark or Exterminate"
  APL lines 220-224: Five separate FWF conditions across multiple lines, including
  chosen_of_frostbrood, breath_of_sindragosa, pillar_of_frost checks.
  APL line 220 includes: !debuff.reapers_mark_debuff.up&!buff.exterminate.up (matches)
  But also has complex Chosen of Frostbrood recall logic (line 221).
  Impact: Minor — APL is more detailed but core condition matches.

#### MISSING [FROST-DB-7]: Rune pooling for Reaper's Mark
  APL line 286: variable,name=rune_pooling — pools runes for Reaper's Mark
  Wowhead line 29: "Do not run out of runes around 45-second mark when RM coming off CD"
  APL implements this; Wowhead mentions it in text but not in priority list.
  Impact: Minor — APL implements the guidance properly.

---

### Rider of the Apocalypse — Single Target

Wowhead Priority (lines 257-268):
  1. ERW if 2 charges
  2. Pillar of Frost
  3. Breath of Sindragosa
  4. Frostwyrm's Fury (unconditional)
  5. Obliterate if 2 KM stacks
  6. Howling Blast with Rime
  7. Frost Strike to avoid RP waste
  8. Obliterate with KM
  9. ERW to generate KM
  10. Frost Strike
  11. Obliterate without KM
  12. Howling Blast

#### OTHER [FROST-ROTA-1]: No separate RoTA APL
  APL does not have separate action lists for Deathbringer vs Rider of the Apocalypse.
  Hero tree differentiation is via conditions (e.g., hero_tree.deathbringer in line 286).
  Wowhead has separate priority lists with notable differences (e.g., no Reaper's Mark
  for RoTA, unconditional FWF for RoTA).
  Impact: Low — the APL's conditional approach should cover both, but conditions
  that gate on hero_tree.deathbringer effectively exclude RoTA-specific behaviors.

#### MISSING [FROST-ROTA-2]: Wowhead has template text for RoTA
  Wowhead line 255: "{{Replace the list items below for rider-of-the-apocalypse...}}"
  This is UNFINISHED TEMPLATE TEXT in the Wowhead guide!
  Impact: Data quality issue — Wowhead RoTA ST may be placeholder/incomplete.

---

### Frost Tier Set (Relentless Rider's Lament)
  2pc: ERW grants stacking buff increasing next Obliterate/Frostscythe damage
  4pc: Reduces ERW CD; Pillar of Frost grants free ERW charge

  Code: CONFIRMED at lines 9740, 9801, 9805, 10163, 11490, 11645, 15849, 15852
  - empowered_strikes buff (2pc): line 15849
  - mid1_4pc_buff (4pc): line 15852
  - Free ERW on Pillar: line 11645
  Wowhead: "Does not require learning any rotational changes" — MATCHES
  Status: IMPLEMENTED CORRECTLY

---

### Frost AoE

Wowhead Deathbringer AoE (lines 60-72):
  Same structure as ST but Frostscythe replaces Obliterate, Glacial Advance replaces FS

APL aoe (lines 256-271):
  Properly has Frostscythe and Glacial Advance replacements.
  Also has Obliterate fallbacks for when active_enemies < frostscythe_priority.

#### CONDITION_ISSUES [FROST-AOE-1]: AoE threshold
  APL line 212: AoE list at active_enemies>=3
  Wowhead line 56: "Frostscythe and Glacial Advance at 3+ targets"
  Status: MATCHES

---

### Frost Opener

Wowhead Deathbringer Opener (lines 99-106):
  1. Empower Rune Weapon
  2. Reaper's Mark
  3. Pillar of Frost
  4. Breath of Sindragosa
  5. Obliterate
  6. Empower Rune Weapon
  7. Obliterate

#### OTHER [FROST-OP-1]: No opener sequence in APL
  APL precombat (lines 194-204): Only snapshot_stats and variable setup.
  No explicit opener sequence. Rotation handles ordering via cooldown priorities.
  Impact: Low — SimC standard practice; cooldowns list order achieves similar result.


================================================================================
## UNHOLY DEATH KNIGHT
================================================================================

### Rider of the Apocalypse — Single Target (Outside Forbidden Knowledge)

Wowhead Priority (lines 18-29):
  1. Outbreak if VP not active
  2. Army of the Dead on CD
  3. Dark Transformation on CD
  4. Putrefy if 2 charges
  5. Soul Reaper on CD
  6. Putrefy if DT has 15s+ on CD
  7. Festering Scythe if debuff missing/expiring
  8. Death Coil if Sudden Doom or >=80 RP
  9. Festering Strike if no Lesser Ghoul stacks
  10. Scourge Strike if Lesser Ghoul stacks
  11. Death Coil

APL cooldowns (lines 336-342) + single_target (lines 353-359):

Cooldowns:
  - Potion
  - Power Infusion
  - Outbreak (complex conditions)
  - Army of the Dead
  - Dark Transformation
  - Soul Reaper (with conditions)
  - Putrefy (complex conditions)

Single Target:
  1. Soul Reaper if target <=35% HP
  2. Festering Strike if festering_scythe conditions
  3. Death Coil if spending_rp
  4. Festering Strike if lesser_ghoul_ready=0
  5. Scourge Strike if lesser_ghoul_ready>=1
  6. Putrefy if no soul_reaper & DT CD >12
  7. Death Coil

#### CONDITION_ISSUES [UH-ROTA-1]: Death Coil RP threshold
  Wowhead line 26: "Death Coil if Sudden Doom or 80+ RP"
  APL line 366: spending_rp = rune<2 | forbidden_knowledge.up&rune<4 | sudden_doom.react
  APL does NOT check for 80 RP threshold! It checks rune count instead.
  Impact: Significant — APL uses rune-based spending logic, not RP-based.
  The 80 RP check from Wowhead is completely absent.

#### WRONG_ORDER [UH-ROTA-2]: Soul Reaper positioning
  Wowhead: Soul Reaper on CD at position 5 (unconditional in outside-FK list)
  APL cooldowns line 341: Soul Reaper with conditions (pestilence/infliction_of_sorrow/<=35%)
  APL single_target line 353: Soul Reaper ONLY if target <=35% HP
  Wowhead says "on cooldown" universally; APL restricts to <=35% or specific talent combos.
  Impact: Significant — APL is much more restrictive on Soul Reaper usage.

#### WRONG_ORDER [UH-ROTA-3]: Putrefy positioning
  Wowhead: Putrefy at position 4 (2 charges) and position 6 (DT>15s)
  APL cooldowns line 342: Complex Putrefy conditions (DT>15, soul_reaper>35%,
  charges=max, reaping interactions)
  APL single_target line 358: putrefy only if !soul_reaper & DT CD >12
  Impact: Moderate — APL is more conservative, checks Soul Reaper interaction.

#### CONDITION_ISSUES [UH-ROTA-4]: Outbreak placement
  Wowhead line 19: Outbreak as #1 priority in rotation
  APL: Outbreak is in cooldowns list (line 338), NOT in single_target.
  It has complex conditions (ticks_remain<3, pestilence, blightburst interactions).
  Impact: Minor — functionally similar, but Wowhead's simple "if VP not active"
  differs from APL's "ticks_remain<3" (which refreshes before it falls off).

#### MISSING_MECHANIC [UH-ROTA-5]: Forbidden Knowledge separate priorities
  Wowhead lines 30-36: Explicit separate "DURING FORBIDDEN KNOWLEDGE" priority
  with Necrotic Coil replacing Death Coil, different ordering.
  APL: No explicit FK mode. Uses spending_rp variable that checks FK buff,
  and relies on set_replacement_action (sc_death_knight.cpp line 9491) to
  auto-replace death_coil->necrotic_coil and epidemic->graveyard.
  Impact: Low — mechanically correct via code replacement, but APL priority
  ordering does not change during FK as Wowhead suggests it should.
  Specifically, Wowhead removes Outbreak/Army/DT from FK priority and puts
  Putrefy 2-charges and Soul Reaper at top. APL doesn't do this reordering.

#### MISSING [UH-ROTA-6]: Festering Scythe debuff tracking nuances
  Wowhead line 25: "if any target doesn't have its debuff, or its debuff is about to expire"
  APL line 354: festering_scythe conditions check buff.festering_scythe.up/remains
  and debuff.festering_scythe_debuff.remains<3
  Status: MATCHES (APL implements this correctly)

---

### San'layn — Single Target

Wowhead Priority (lines 208-230):
  Outside FK:
    1. Outbreak if VP not active
    2. Festering Strike before DT if <=3 Lesser Ghoul stacks
    3. Soul Reaper if target <35% HP
    4. Army of the Dead on CD
    5. Dark Transformation on CD
    6. Putrefy if 2 charges
    7. Soul Reaper on CD
    8. Putrefy if DT >15s on CD
    9. Festering Scythe if debuff issues
    10. Death Coil if Sudden Doom or 80+ RP
    11. Festering Strike if no Lesser Ghoul stacks
    12. Scourge Strike if Lesser Ghoul stacks -> becomes Vampiric Strike via buff
    13. Death Coil
  During FK:
    1. Soul Reaper if <35% HP
    2. Putrefy if 2 charges
    3. Soul Reaper on CD
    4. Festering Scythe
    5. Necrotic Coil (replaces Death Coil)
    6. Festering Strike if no LG stacks
    7. Vampiric Strike if LG stacks (replaces Scourge Strike)

#### MISSING_MECHANIC [UH-SL-1]: San'layn-specific priority not in APL
  APL has NO hero_tree.sanlayn checks in the Unholy APL at all.
  Wowhead San'layn has different priorities than RoTA:
  - "Festering Strike BEFORE Dark Transformation if <=3 Lesser Ghoul stacks"
  - "Soul Reaper if target <35% HP" at position 3 (before Army/DT)
  APL uses identical logic for both hero trees.
  Impact: Moderate — San'layn-specific optimizations are missing from APL.

#### MISSING_MECHANIC [UH-SL-2]: Vampiric Strike (Unholy San'layn)
  Wowhead line 229: "Vampiric Strike if you have Lesser Ghoul stacks" during FK
  Code: sc_death_knight.cpp line 12224-12225: scourge_strike auto-replaces with
  vampiric_strike when buff is up.
  APL: Uses scourge_strike which auto-replaces. No explicit vampiric_strike call.
  Status: HANDLED via code replacement — functionally correct.

---

### Unholy AoE

Wowhead RoTA AoE (lines 55-69):
  Outside FK:
    1. Outbreak if VP not active
    2. Army on CD
    3. Dark Transformation on CD
    4. Putrefy on CD
    5. Festering Scythe if debuff issues
    6. Epidemic
    7. Festering Strike if no LG stacks
    8. Scourge Strike if LG stacks
  During FK:
    1. Putrefy on CD
    2. Festering Scythe
    3. Graveyard (replaces Epidemic)
    4. Festering Strike if no LG stacks
    5. Scourge Strike if LG stacks

APL aoe (lines 326-334):
  1. Death and Decay if not ticking & talent.desecrate
  2. Festering Strike if festering_scythe conditions
  3. Epidemic if spending_rp & epidemic_prio
  4. Death Coil if spending_rp & !epidemic_prio
  5. Festering Strike if lesser_ghoul=0
  6. Scourge Strike if lesser_ghoul>=1
  7. Putrefy
  8. Epidemic if epidemic_prio
  9. Death Coil if !epidemic_prio

#### MISSING [UH-AOE-1]: Death and Decay not in Wowhead AoE
  APL line 326: death_and_decay if talent.desecrate
  Wowhead: Does not mention Death and Decay in Unholy AoE rotation.
  Impact: Minor — Desecrate talent may not be default, but APL handles it.

#### WRONG_ORDER [UH-AOE-2]: Putrefy position in AoE
  Wowhead: Putrefy on CD at position 4 (before Epidemic/Festering Strike)
  APL line 332: Putrefy at position 7 (after all spenders and builders!)
  Impact: Significant — Putrefy is much lower priority in APL than Wowhead.

#### CONDITION_ISSUES [UH-AOE-3]: AoE threshold
  APL line 323: AoE list at active_enemies>=4
  Wowhead: Does not specify exact AoE threshold.
  The epidemic_prio variable (line 370) kicks in at 4+ targets.
  Impact: Low — reasonable default.

#### MISSING [UH-AOE-4]: Graveyard during Forbidden Knowledge
  APL: No explicit graveyard. Epidemic auto-replaces via code (line 9952).
  Wowhead line 67: "Cast Graveyard" explicitly during FK AoE.
  Status: HANDLED via code replacement — functionally correct.

---

### Unholy Tier Set (Relentless Rider's Lament)
  2pc: Dread Plague +25%, Virulent Plague +25%
  4pc: Putrefy +20% damage, next Scourge Strike costs no Rune

  Code: CONFIRMED at lines 3690, 15045, 15924
  - blighted_buff (4pc): line 15045, 15924
  - Putrefy damage bonus: line 3690
  Wowhead: "No rotational impact" — MATCHES
  Status: IMPLEMENTED CORRECTLY

---

### Unholy Opener

Wowhead RoTA Opener (lines 91-101):
  1. Outbreak
  2. Festering Strike
  3. Festering Scythe
  4. Army of the Dead
  5. Dark Transformation
  6. On-Use Trinket
  7. Combat Potion
  8. Soul Reaper
  9. Necrotic Coil
  10. Necrotic Coil

APL precombat (lines 305-316):
  1. snapshot_stats
  2. raise_dead
  3. Variable setup only

#### MISSING [UH-OP-1]: Opener sequence not in APL
  APL has no opener sequence; only Raise Dead in precombat.
  Impact: Low — standard SimC practice; cooldowns/rotation handle ordering.

#### OTHER [UH-OP-2]: Raise Dead in precombat
  APL line 306: raise_dead in precombat
  Wowhead line 120: "Summon Timmy by casting Raise Dead" in pre-combat checks
  Status: MATCHES


================================================================================
## SUMMARY OF CRITICAL ISSUES
================================================================================

### HIGH IMPACT
1. [UH-ROTA-1] Unholy Death Coil RP threshold (80 RP) missing from APL
   - APL uses rune-based spending logic instead of RP threshold
2. [UH-ROTA-2] Unholy Soul Reaper restricted to <=35% HP in APL ST, but
   Wowhead says "on cooldown" unconditionally
3. [FROST-DB-1] Remorseless Winter in APL but completely absent from Wowhead
4. [UH-AOE-2] Unholy AoE Putrefy much lower priority in APL than Wowhead

### MODERATE IMPACT
5. [BLOOD-DB-3/SL-6] Blood extra Death Strike filler at mid-priority
6. [BLOOD-DB-5] Blood Marrowrend+Exterminate not in Wowhead
7. [BLOOD-SL-1] Blood San'layn EotBQ tracking in APL not in Wowhead
8. [UH-ROTA-5] Unholy FK mode doesn't reorder priorities in APL
9. [UH-SL-1] Unholy San'layn-specific priorities missing from APL
10. [FROST-DB-2] Frost ERW conditions far more complex in APL
11. [FROST-DB-3] Frost Shattering Blade/Razorice not in Wowhead
12. [FROST-DB-4] Frost Frostbane not in Wowhead

### LOW IMPACT / DATA QUALITY
13. [FROST-ROTA-2] Wowhead RoTA ST has UNFINISHED TEMPLATE TEXT
14. All three specs: APL precombat has minimal opener vs Wowhead's full sequence
15. Blood/Unholy: Consumption/DnD talent-specific entries differ

### TIER SETS
All three tier sets (Blood, Frost, Unholy) are CORRECTLY IMPLEMENTED in code.
No rotational changes needed per Wowhead — confirmed matching.

### NOTE ON METHODOLOGY
Several abilities use SimC's set_replacement_action mechanism where one ability
auto-replaces another when a buff is active:
- death_coil -> necrotic_coil (when forbidden_knowledge up)
- epidemic -> graveyard (when forbidden_knowledge up)
- scourge_strike -> vampiric_strike (when vampiric_strike buff up)
- heart_strike -> vampiric_strike (Blood, when buff up)
- festering_strike -> festering_scythe (when festering_scythe buff up)
- howling_blast -> frostbane (when frostbane buff up)

These are functionally correct even though the APL doesn't reference the
replacement ability names directly.

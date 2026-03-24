# Mage SimC vs Wowhead Audit Report
Generated: 2026-03-24
Patch: 12.0.1 (Midnight Season 1)
APL File: engine/class_modules/apl/mage.cpp
Class Module: engine/class_modules/sc_mage.cpp (61 TODO/FIXME comments)

---

## ARCANE MAGE

### Wowhead Summary (Spellslinger / Sunfury)
**Spellslinger Priority:**
1. Arcane Orb after Barrage with Clearcasting
2. Arcane Barrage at 4x Charges with 20 Arcane Salvo stacks
3. Presence of Mind when no Charges or better generators
4. Arcane Blast
5. Arcane Barrage if out of mana

**Sunfury:** Touch of the Magi cast late in Arcane Surge to capture Arcane Soul window.

**Tier Set (Voidbreaker's Accordance):**
- 2pc: Each Arcane Charge increases crit chance by 1.0%
- 4pc: Critical strike damage of Arcane spells increased by 10%

### APL Analysis (lines 78-158)
- Has three sub-lists: spellslinger, spellslinger_orbm, sunfury
- Cooldowns list handles Arcane Surge, Touch of the Magi, Evocation
- Spellslinger Orb Mastery build is the recommended Wowhead build

### Issues Found

#### MISSING
- [ARCANE-M1] **Frostfire Bolt (Sunfury variant):** Wowhead mentions Sunfury Arcane
  Phoenix casting Greater Pyroblast, Meteorite, etc. These pet behaviors are
  implemented in sc_mage.cpp but are not controllable via APL (expected, info only).

#### WRONG_ORDER
- [ARCANE-O1] **No significant priority ordering mismatches detected.** The APL
  spellslinger_orbm list closely follows the Wowhead priority: Orb after Barrage
  with CC, Barrage at 20 Salvo, Presence of Mind for charges, Arcane Blast filler,
  Barrage for mana management.

#### MISSING_MECHANIC
- [ARCANE-MM1] **Arcane 4pc (Crit Damage +10%):** No explicit code reference to
  MAGE_ARCANE MID1 B4 found in sc_mage.cpp. The 2pc (crit per Arcane Charge) is
  explicitly implemented at line 6428-6432. The 4pc may be auto-applied via spell
  data labels, but this should be verified. If not auto-parsed, this is a MISSING
  tier bonus implementation.

#### CONDITION_ISSUES
- [ARCANE-C1] **Sunfury Touch of the Magi timing:** Wowhead says Touch should be
  cast late in Surge window to capture Arcane Soul. APL condition (line 128):
  `buff.arcane_surge.remains<(5+gcd.remains)` for Sunfury — this correctly delays
  Touch to the end of Surge. However, the APL TODO notes suggest this needs
  "reassessment" and Orb Mastery support for Sunfury is missing.
- [ARCANE-C2] **Evocation usage:** APL uses Evocation only at <10% mana with no
  Surge/Touch active and Surge CD > 10s (line 130). Wowhead mentions Evocation as
  an "option" but doesn't provide detailed conditions. The APL's conservative
  approach may miss some edge cases. APL has a TODO: "Reassess Evo usage for all builds."

#### OTHER
- [ARCANE-X1] **APL TODO comments note:** "Add Orb Mastery support for Sunfury" and
  "Look into Charged Missiles tailored sequences for both hero trees." These are
  acknowledged gaps in the APL vs what Wowhead covers.
- [ARCANE-X2] **Arcane Pulse (M+):** Both Wowhead and APL handle Arcane Pulse at 3+
  targets consistently (variable.pulse_aoe_count=3).

---

## FIRE MAGE

### Wowhead Summary (Sunfury / Frostfire)
**Outside Combustion (Sunfury):**
1. Cast Combustion (delayed: 18s with Firestarter, 8-10s without)
2. Pyroblast with Hot Streak
3. Pyroblast with Hyperthermia
4. Fire Blast with Heating Up during Fireball cast
5. Fire Blast after Hot Streak spend if guaranteed crit (Hyperthermia)
6. Execute: Fire Blast without Heating Up during Scorch
7. Execute: Fire Blast with Heating Up
8. Scorch with Heat Shimmer after Hot Streak spend
9. Execute: Scorch below 30% HP
10. Fireball filler

**During Combustion (Sunfury):**
1. Meteor in last 8s of Combustion
2. Pyroblast/Flamestrike with Hot Streak
3. Fire Blast to generate Hot Streak
4. Scorch as filler

**Key Mechanics:** Fired Up extends Combustion, Burnout on Combustion end,
Fiery Rush speeds Fire Blast CD during Combustion, Hyperthermia after Sunfury
Combustion, Arcane Phoenix summoned.

**Tier Set:**
- 2pc: Pyroblast and Flamestrike deal 8% increased damage
- 4pc: Casting Pyroblast or Flamestrike reduces Fire Blast CD by 0.50 sec

### APL Analysis (lines 162-260)
- Separate lists for Frostfire (ff_combustion, ff_filler) and Sunfury (sf_combustion, sf_filler)
- Shared fireblast list with detailed conditions
- Combustion delay logic via variable.combustion_delay

### Issues Found

#### MISSING
- [FIRE-M1] **No significant missing abilities.** All key spells (Combustion, Pyroblast,
  Flamestrike, Fire Blast, Scorch, Meteor, Fireball, Frostfire Bolt) are present
  in the APL.

#### WRONG_ORDER
- [FIRE-O1] **Meteor timing in Combustion:** Wowhead says "Meteor in the last 8
  seconds of Combustion." APL sf_combustion (line 241): Uses Meteor with
  `talent.burnout&buff.combustion.remains<8` (end of Combustion for Burnout) or
  `!talent.burnout&buff.combustion.remains>2` (anytime during Combustion without
  Burnout). This matches Wowhead's guidance well but note the Burnout-specific
  timing is not explicitly called out in Wowhead's simplified priority.
- [FIRE-O2] **Sunfury Combustion precast:** Wowhead says cast Scorch into Combustion
  for Sunfury. APL sf_combustion (line 239): `scorch,if=buff.combustion.down&
  (target.health.pct<30|active_enemies>=4)` — only Scorches in execute or 4+
  targets. In non-execute ST, it falls through to Fireball precast (line 240).
  Wowhead suggests Scorch always for Sunfury precast, APL prefers Fireball in
  non-execute situations. This is a MINOR PRIORITY DISCREPANCY — APL may be
  more optimized than the simplified Wowhead guidance.

#### MISSING_MECHANIC
- [FIRE-MM1] **Fire 2pc (Pyroblast/Flamestrike +8% damage):** No explicit
  MAGE_FIRE MID1 B2 reference found in sc_mage.cpp. This bonus is likely
  auto-applied via spell data (damage modifier on Pyroblast/Flamestrike), but
  should be verified. If not auto-parsed, this is a missing implementation.
- [FIRE-MM2] **Fired Up proc mechanics:** sc_mage.cpp has an extensive Fired Up
  implementation with TODO comments: "Fit an equation or get more accurate numbers"
  (line 7083), "This is bugged and seems to apply its changes to the proc chance
  during Combustion even when the talent is not learned" (line 7086). These
  indicate ongoing accuracy concerns with the Fired Up probability model.

#### CONDITION_ISSUES
- [FIRE-C1] **Combustion delay timing:** Wowhead: "18 seconds with Firestarter,
  8-10 seconds without." APL (line 181): `variable,name=combustion_delay,value=
  10+(8*talent.firestarter)-(10*(expected_combat_length<60)...)` — base 10s,
  +8s for Firestarter = 18s. Matches Wowhead. Short fight adjustments reduce delay.
- [FIRE-C2] **Flamestrike AoE threshold:** Wowhead: "Sunfury replaces Pyroblast with
  Flamestrike at 4 or more targets." APL: sf_filler_flamestrike=3 (line 180),
  meaning Flamestrike at 3+ targets in filler for Sunfury. sf_combustion_flamestrike=4
  (line 179). DISCREPANCY: Wowhead says 4+ for Sunfury, APL uses 3+ for filler.
  This could be a SimC optimization vs Wowhead simplification.
- [FIRE-C3] **Burnout + Meteor timing:** Wowhead: "Meteor within 10 seconds of
  Combustion ending, shoot for <8 seconds remaining." APL: `talent.burnout&
  buff.combustion.remains<8` — matches the <8s guidance.

#### OTHER
- [FIRE-X1] **Pyroclasm handling:** APL has detailed Pyroclasm stack management
  (hold 1 stack for Combustion, spend at 2 stacks). Wowhead mentions Pyroclasm
  precast into Combustion. APL is more detailed here.
- [FIRE-X2] **Spontaneous Combustion talent:** APL has specific Fire Blast logic
  for this talent (line 209) not mentioned in Wowhead rotation guide.
- [FIRE-X3] **Frostfire hero talent:** APL has dedicated ff_combustion and ff_filler
  lists. Wowhead mentions Frostfire variant but extracted data focuses on Sunfury.

---

## FROST MAGE

### Wowhead Summary (Spellslinger / Frostfire)
**Spellslinger ST:**
1. Flurry if Brain Freeze & no Thermal Void
2. Ice Lance if Fingers of Frost at 2 stacks
3. Frozen Orb
4. Glacial Spike
5. Ice Lance if Fingers of Frost
6. Ice Lance if Freezing >= 6 stacks
7. Flurry
8. Ray of Frost
9. Frostbolt

**Frostfire ST:**
1. Flurry if Brain Freeze & no Thermal Void
2. Frozen Orb
3. Glacial Spike
4. Comet Storm
5. Ice Lance if Fingers of Frost
6. Ice Lance if Freezing >= 10 stacks
7. Flurry
8. Ray of Frost
9. Frostfire Bolt

**Key Mechanics:** Freezing/Shatter system, Ray of Frost as major CD with 2 charges
(Hand of Frost), Comet Storm replaces Ray of Frost after cast, Frostfire
Empowerment spending before Comet Storm in AoE.

**Tier Set:**
- 2pc: Flurry damage increased by 10%, Flurry has 10% chance to grant Fingers of Frost
- 4pc: Fingers of Frost increases Shatter's damage by 15%

### APL Analysis (lines 264-361)
- Four sub-lists: ff_aoe, ff_st, ss_aoe, ss_st (plus movement)
- Opener sequences in cds list with line_cd=9999 (one-time actions)
- Clean priority-based structure

### Issues Found

#### MISSING
- [FROST-M1] **Comet Storm in Spellslinger lists:** APL ss_st and ss_aoe both
  include `comet_storm,if=buff.splinterstorm.down` as the FIRST priority action.
  Wowhead's Spellslinger priority lists do NOT include Comet Storm at all for
  Spellslinger. This is a significant discrepancy — Comet Storm replaces Ray of
  Frost per Wowhead ("Comet Storm replaces Ray of Frost after you cast it"), but
  the Wowhead Spellslinger rotation doesn't list it as a separate priority. The
  APL includes it as the highest priority with a splinterstorm-down condition.
  This may be correct SimC behavior but diverges from the Wowhead guide.
- [FROST-M2] **Ice Nova and Cone of Cold:** APL ss_aoe includes Ice Nova and Cone
  of Cold at 4+ targets with cone_of_frost talent (lines 343-344). Wowhead AoE
  priorities don't mention these abilities at all.

#### WRONG_ORDER
- [FROST-O1] **Spellslinger ST: FoF 2-stack priority missing from APL.** Wowhead
  priority #2 is "Ice Lance if Fingers of Frost at 2 stacks" (before Frozen Orb).
  APL ss_st has no 2-stack FoF condition — all FoF Ice Lances are handled at
  position 4 as `ice_lance,if=buff.fingers_of_frost.react`. This means the APL
  may hold FoF at 2 stacks longer than Wowhead recommends, risking overcap.
- [FROST-O2] **Spellslinger ST: Glacial Spike vs FoF Ice Lance ordering.** Wowhead
  puts Glacial Spike (#4) ABOVE single-FoF Ice Lance (#5). APL ss_st has FoF Ice
  Lance (#4) ABOVE Glacial Spike (#5). This is a priority SWAP — APL prioritizes
  spending FoF over Glacial Spike, while Wowhead prioritizes Glacial Spike.
- [FROST-O3] **Spellslinger ST: Flurry vs Ray of Frost ordering.** Wowhead puts
  bare Flurry (#7) ABOVE Ray of Frost (#8). APL ss_st has Ray of Frost (#7) ABOVE
  bare Flurry (#8). Minor ordering swap.
- [FROST-O4] **Spellslinger AoE: Similar ordering issues** as ST — FoF 2-stack
  missing, Glacial Spike/FoF swap, plus Comet Storm at top.
- [FROST-O5] **Frostfire AoE: Blizzard (non-Freezing Rain) positioning.** Wowhead
  Frostfire AoE places regular Blizzard (#7) between Comet Storm and FoF Ice Lance.
  APL ff_aoe places it much lower (line 311) with a 4-5 target threshold condition.

#### MISSING_MECHANIC
- [FROST-MM1] **Frost 2pc Flurry +10% damage:** The Frost 2pc has two effects:
  (1) Flurry damage +10%, (2) 10% chance for FoF on Flurry. Only the FoF proc
  is explicitly coded (line 3924: `trigger_fof(...effectN(3).percent()...)`).
  The +10% Flurry damage (effectN 1/2) is not explicitly referenced — it may be
  auto-applied via spell data, but should be verified.
- [FROST-MM2] **Thermal Void mechanic:** Wowhead describes using Flurry to trigger
  Thermal Void buff (from Brain Freeze Flurries). APL checks
  `buff.thermal_void.down` as a condition. Code (line 3921-3922) correctly
  triggers Thermal Void on Brain Freeze Flurry. IMPLEMENTED but note:
  Thermal Void is a new Midnight mechanic replacing the old Icy Veins extension.
- [FROST-MM3] **Hand of Frost (Ray of Frost 2 charges):** Wowhead emphasizes
  Ray of Frost having 2 charges at level 90 via Hand of Frost, providing
  flexibility. Code at line 4929 has TODO: "This is a bit of a hack to make it
  work for both 4 and 8 in spell data." Charge system appears implemented but
  with caveats.
- [FROST-MM4] **Frostfire Empowerment spending before Comet Storm (AoE):** Wowhead
  says "prioritize spending Frostfire Empowerment first so that Comet Storm has
  more Freezing stacks to consume." APL ff_aoe Ray of Frost has condition
  `!buff.frostfire_empowerment.react` (line 315) — meaning it avoids Ray when
  you have empowerment, ensuring empowerment is spent on Ice Lance/other first.
  CORRECTLY IMPLEMENTED.

#### CONDITION_ISSUES
- [FROST-C1] **Freezing stack threshold:** Wowhead specifies 6+ stacks for
  Spellslinger, 10+ for Frostfire. APL matches: ss_st/ss_aoe use
  `debuff.freezing.react>=6`, ff_st/ff_aoe use `debuff.freezing.stack>=10`.
  Note the different operators (react vs stack) — react checks for reactable
  stacks, stack checks raw count. This may cause a minor timing difference.
- [FROST-C2] **Opener sequence:** Wowhead Spellslinger opener: Glacial Spike >
  Flurry > Frozen Orb > Ray of Frost. APL opener (lines 299-301): Flurry >
  Frozen Orb > Ray of Frost (no explicit Glacial Spike in SS opener, though
  it's in precombat). Frostfire opener in APL (lines 294-298): Flurry > GS >
  Flurry > RoF > Frozen Orb. Wowhead FF opener: GS > Flurry > Frozen Orb > RoF.
  SIGNIFICANT ORDERING DIFFERENCES in both openers.

#### OTHER
- [FROST-X1] **Summon Water Elemental:** APL precombat includes
  `summon_water_elemental` (line 277). Wowhead mentions "Use Summon Water Elemental
  (if talented)" in pre-combat. Aligned.
- [FROST-X2] **Blizzard precast for Frostfire:** APL precombat (line 278):
  `blizzard,if=talent.frostfire_bolt|active_enemies>=3`. Wowhead doesn't mention
  this Frostfire-specific optimization for ST. APL comment says "at least neutral,
  and a gain for builds that use Glacial Shatter."
- [FROST-X3] **Movement list:** APL has a dedicated movement priority (lines 330-334)
  with Blink, Freezing Rain Blizzard, Ice Nova, Cone of Cold, Ice Lance. Wowhead
  doesn't cover movement-specific priorities.
- [FROST-X4] **Old TWW set bonus reference:** TODO at line 4765: "Still seems to be
  using the old TWW set bonus GS" — may indicate leftover code from previous tier.

---

## CROSS-SPEC ISSUES

### Code Quality Concerns (61 TODO/FIXME in sc_mage.cpp)
Notable items that affect accuracy:
1. **Fired Up probability model** (lines 7083-7086): Fitted from logged data, known
   bugs with proc chance during Combustion
2. **Splinter generation** (line 7215): "Effect 2 of Splintering Sorcery? Unclear"
3. **Clearcasting triggers** (lines 7259-7289): Multiple TODO about accuracy of
   CC proc banking and guaranteed CC interactions
4. **Splitting Ice issues** (line 3965): Known issues affecting Frostbolt/Frostfire Bolt
5. **Arcane Phoenix duration** (lines 3323, 3500): "Extra random pet duration can
   sometimes result in an extra cast"
6. **Various AoE target cap verifications** (lines 1303, 1333, 3356, 4701): Multiple
   "TODO: Verify this" on reduced_aoe_targets values

### Tier Set Implementation Summary
| Spec   | Bonus | Description                        | Status           |
|--------|-------|------------------------------------|------------------|
| Arcane | 2pc   | +1% crit per Arcane Charge         | IMPLEMENTED      |
| Arcane | 4pc   | +10% Arcane spell crit damage      | NOT FOUND*       |
| Fire   | 2pc   | +8% Pyroblast/Flamestrike damage   | NOT FOUND*       |
| Fire   | 4pc   | -0.5s Fire Blast CD on Pyro/FS     | IMPLEMENTED      |
| Frost  | 2pc   | +10% Flurry dmg, 10% FoF chance    | PARTIAL**        |
| Frost  | 4pc   | +15% Shatter dmg with FoF          | IMPLEMENTED      |

*May be auto-applied via spell data labels — needs verification
**FoF proc implemented, Flurry +10% damage not explicitly found

### APL TODO Items (from mage.cpp comments)
1. "Recheck after all trinkets are implemented" (line 111)
2. "Add Orb Mastery support for Sunfury" (line 117)
3. "Look into Charged Missiles tailored sequences" (line 117)
4. "Look into simplifying [sunfury pooling logic]" (line 116)
5. "Look into delaying touch slightly for Spellslinger Surges" (line 128)
6. "Reassess Evo usage for all builds" (line 130)
7. "Add fight length sensitivity" (line 125)

---

## SEVERITY SUMMARY

### HIGH (Potential DPS Impact)
- [FROST-O1] FoF 2-stack priority missing — risk of FoF overcap
- [FROST-O2] Glacial Spike vs FoF ordering swapped vs Wowhead
- [FROST-M1] Comet Storm in Spellslinger lists not matching Wowhead
- [ARCANE-MM1] Arcane 4pc crit damage bonus — verify implementation
- [FIRE-MM1] Fire 2pc Pyroblast/Flamestrike damage — verify implementation

### MEDIUM (Accuracy Concerns)
- [FROST-C2] Opener sequence ordering differences
- [FROST-O5] Frostfire AoE Blizzard positioning
- [FIRE-C2] Sunfury Flamestrike threshold (3 vs 4 targets in filler)
- [FIRE-MM2] Fired Up probability model accuracy
- [FROST-MM1] Frost 2pc Flurry damage bonus — verify implementation

### LOW (Minor / Informational)
- [FIRE-O2] Sunfury Combustion precast (Scorch vs Fireball)
- [FROST-O3] Bare Flurry vs Ray of Frost ordering
- [FROST-M2] Ice Nova/Cone of Cold in AoE (APL optimization)
- [ARCANE-C2] Evocation usage conditions
- [FROST-C1] react vs stack operator difference for Freezing

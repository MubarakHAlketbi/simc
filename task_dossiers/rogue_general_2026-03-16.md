# Rogue Midnight Changes Dossier
# Created: 2026-03-16

## Sources
- Wowhead spell data: https://www.wowhead.com/beta/spell=1264856 through 1264861
- Wowhead Alpha Phase 6 datamine: https://www.wowhead.com/news/midnight-alpha-phase-6-datamined-class-and-spell-changes-more-tier-rallying-cry-379163
- BlazingBoost Midnight Rogue Changes: https://blazingboost.com/wow-boost/wow-midnight-rogue-changes
- Conquest Capped PvP Sets: https://conquestcapped.com/guides/wow/midnight-pvp-elite-sets-season-1/

---

## Global Rogue Class Changes (General)

### New Class Talents
| Talent | Effect |
|--------|--------|
| Toxic Stiletto | Shiv costs 20 less Energy, CD reduced by 15s, range +2 yards |
| Quick Fingers | +3% Agility (Passive) |
| Deep Cuts | Finisher damage increased by 6% |
| Danger Sense | 20% chance to partially evade incoming damage, reducing it by 20% |

### Updated Talents
- Cold Blooded Killer: Now provides predictable 10% crit chance bonus to next finisher after a generator crits

### Removed Talents
- Rushed Setup
- Shadowheart

---

## MID1 Tier Set: "Motley of the Grim Jest" (item-set=1987)
Set Name: Motley of the Grim Jest (Leather)

---

## Assassination Rogue

### Set Bonus Spell IDs
- 2pc: spell 1264856 - "Rogue Assassination 12.0 Class Set 2pc"
- 4pc: spell 1264857 - "Rogue Assassination 12.0 Class Set 4pc"

### 2pc Bonus (spell 1264856)
**Tooltip**: "Garrote's damage is increased by 30% and it also applies your weapon poisons."
- Effect #1: Modifies Damage/Healing Done +30% (PvP mult: 0.5)
  - Affects: Garrote (703), Garrote (360830)
- Effect #2: Modifies Periodic Damage/Healing Done +30% (PvP mult: 0.5)
  - Affects: same Garrote spells
- BONUS: Guarantees poison application on Garrote cast (100% rate)

### 4pc Bonus (spell 1264857)
**Tooltip**: "Garrote's Energy cost is reduced by 10. Mutilate, Ambush and Fan of Knives deal 25% increased damage to targets affected by your weapon poisons."
- Effect #1: Modifies Power Cost (Garrote) -10 (PvP mult: 0.5)
- Effect #2: Dummy value 25 (Server-side script) - 25% damage bonus to poisoned targets for Mutilate/Ambush/FoK

### Implementation Status
- 2pc: IMPLEMENTED - 30% persistent multiplier in garrote_t::composite_persistent_multiplier(), poison guarantee in composite_poison_flat_modifier()
- 4pc: IMPLEMENTED - affected_by.mid1_assassination_4pc on ambush_t, mutilate_strike_t, fan_of_knives_t; checked in composite_da_multiplier() with is_poisoned() check

---

## Outlaw Rogue

### Set Bonus Spell IDs
- 2pc: spell 1264858 - "Rogue Outlaw 12.0 Class Set 2pc"
- 4pc: spell 1264859 - "Rogue Outlaw 12.0 Class Set 4pc"

### 2pc Bonus (spell 1264858)
**Tooltip**: "Blade Rush's damage is increased by 30% and its damage to your primary target is increased by an additional 15%."
- Effect #1: Modifies Damage/Healing Done +30% (PvP mult: 0.5)
  - Affects: Blade Rush (271877), Blade Rush (271878), Blade Rush (271881), Blade Rush (271896), Blade Flurry (429951)
- Effect #2: Add Modifier - Flat (Label): Modifies Effect #2's Value = +23 (this is the per-target modifier)
  - Affects: Blade Rush (271881)
- Effect #3: Dummy value 15 (PvP mult: 0.4) - scripted primary target bonus

### 4pc Bonus (spell 1264859)
**Tooltip**: "Blade Rush's cooldown is reduced by 6 sec and it increases your damage dealt by 5% for 8 sec."
- Effect #1: Modifies Cooldown -6s (PvP mult: 0.5)
  - Affects: Blade Rush spells, Blade Flurry
- Effect #2: Proc Trigger Spell - triggers "Whirl of Blades" (spell 1275176) on Blade Rush execute

### Implementation Status
- 2pc: IMPLEMENTED - effectN(1) for 30% AoE damage, effectN(3) for +15% primary target in blade_rush_attack_t::composite_da_multiplier()
- 4pc: IMPLEMENTED - mid1_outlaw_4pc buff (Whirl of Blades, damage_buff_t) triggered in blade_rush_attack_t::execute(); CD reduction via spell data (effectN(1))

---

## Subtlety Rogue

### Set Bonus Spell IDs
- 2pc: spell 1264860 - "Rogue Subtlety 12.0 Class Set 2pc"
- 4pc: spell 1264861 - "Rogue Subtlety 12.0 Class Set 4pc"

### 2pc Bonus (spell 1264860)
**Tooltip**: "Finishing moves deal 1.5% more damage per combo point spent."
- Effect: Dummy value 15 (PvP mult: 0.5) - scripted 1.5% per CP
- Note: Per-combo-point so at 5 CPs = +7.5% total

### 4pc Bonus (spell 1264861)
**Tooltip**: "Shadow Blades has 4.0 sec increased duration and causes your attacks to deal an additional 6.0% damage as Shadow."
- Effect #1: Modifies Buff Duration +4 seconds (PvP mult: 0.5)
  - Affects: Shadow Blades (121471), Shadow Blades (279043)
- Effect #2: Modifies Effect #1's Value +6 (PvP mult: 0.5)
  - Affects: Shadow Blades (121471), Shadow Blades (279043)
  - This increases the shadow damage bonus from 20% to 26%

### Implementation Status
- 2pc: IMPLEMENTED - affected_by.mid1_subtlety_2pc on finishers; in composite_da_multiplier() with effectN(1).percent()/10.0 * CP formula
- 4pc: IMPLEMENTED - buffs.shadow_blades modified at create_buffs() with +4s duration (modify_duration) and +6% damage value (set_default_value overriding from_effect(1)+4pc effectN(2))

---

## UNVERIFIED_IMPLEMENTATION Notes

1. OUTLAW 2pc effectN(2): The spell data shows Effect #2 as "Add Modifier - Flat Label: Modifies Effect #2's Value +23" for Blade Rush spell 271881. This appears to be the per-target splash multiplier increase (23 = value added to effectN(2) of blade_rush_attack which defines AoE multiplier vs splash). We implemented as effectN(3).percent() for primary target bonus = 15%. The effectN(2) flat modifier to blade rush attack's effectN(2) is handled by the passive spell data engine and should auto-apply.

2. ASSASSINATION 4pc effectN(2): The Wowhead tooltip says the dummy effect value is 25 for the 25% damage bonus. We use effectN(2).percent() which should evaluate to 0.25 from the spell data.

3. SUBTLETY 4pc: The spell data effectN(1).base_value() for duration should return 4 (in seconds). Verified via from_seconds() usage in other rogue duration code.

4. General Class Changes (new talents: Toxic Stiletto, Quick Fingers, Deep Cuts, Danger Sense) are NOT implemented in SimulationCraft as these require full talent tree data from game client - marked as TODO pending actual game data.

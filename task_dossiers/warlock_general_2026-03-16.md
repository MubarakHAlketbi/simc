# Warlock Midnight (12.0) Changes Research Dossier
# Date: 2026-03-16
# Sources: Wowhead PTR spell data, Wowhead tier set guide, Icy Veins, Maxroll

## General Changes (Midnight Pre-Patch / 12.0)

### Affliction
- Main spender changed from Malefic Rapture back to Unstable Affliction (Legion-style)
- Unstable Affliction no longer has a per-target limit; multiple can be stacked on one target
- Seed of Corruption (via Sow the Seeds) is the primary AoE spender
- Summon Darkglare no longer extends DoTs
- Legion-style DOT-centric design returns

### Demonology
- General pet interaction tuning, Dreadstalker scaling changes
- Call Dreadstalkers remains central to the rotation

### Destruction
- Conflagrate remains core shard generation spell
- Chaos Bolt and Rain of Fire remain primary spenders

## MID1 Tier Set: "Reign of the Abyssal Immolator"
Item Set ID: 1989 (Cloth)
Token: Dreadful (Voidwoven Unraveled Nullcore)
Raids: The Voidspire / The Dreamrift

### Affliction
- 2pc (Spell ID: 1264869): Unstable Affliction and Seed of Corruption damage increased by 10%
  - Effect #1: +10% direct damage, PvP 0.5x (5%)
  - Effect #2: +10% periodic damage, PvP 0.5x (5%)
  - Affected spells: Seed of Corruption, Unstable Affliction (multiple IDs)
- 4pc (Spell ID: 1264870): Agony starts at 2 additional stacks, and its damage is increased by 20%
  - Effect #1 (Dummy): Value 2 (initial stack bonus), server-side script
  - Effect #2: +20% periodic damage to Agony (spell IDs: 980, 1261166)
  - PvP multiplier: 0.5 (10% bonus / 1 stack in PvP)

### Demonology
- 2pc (Spell ID: 1264871): Hand of Gul'dan damage increased by 15%
  - Effect #1: +15% damage to Hand of Gul'dan (spell IDs: 86040, 196282, Eye of Gul'dan 1250265)
  - PvP multiplier: 0.5 (7.5%)
- 4pc (Spell ID: 1264872): Your Dreadstalkers deal 10% increased damage and last 3 additional sec
  - Effect #1 (Mod Pet Stat %): +10% damage - PvP 0.5 (5%)
  - Effect #2 (Mod Buff Duration): +3 sec to dreadstalker duration - PvP 0.5 (1.5s)
  - Affected summoning spells: Call Dreadstalkers (104316, 193331, etc.), Call Greater Dreadstalker (1217615), Infernal Houndmaster (1251704)

### Destruction
- 2pc (Spell ID: 1264873): Chaos Bolt and Rain of Fire damage increased by 5%
  - Affected spells: Chaos Bolt (116858), Rain of Fire (42223)
  - PvP multiplier: 0.5
- 4pc (Spell ID: 1264874): Conflagrate generates 2 additional Soul Shard fragments and its damage is increased by 10%
  - Effect #1 (Mod Spell Effectiveness label 8): +2 soul shard fragments from Conflagrate (spell 245330), PvP 0.5 (1 extra)
  - Effect #2 (Mod Damage/Healing Done): +10% Conflagrate damage (spell 17962), PvP 1.0 (full PvP)

## Implementation Notes

### Existing Code (Already Implemented Before This PR)
- sc_warlock_init.cpp: tier struct already has all 6 tier set pointers assigned via sets->set()
- sc_warlock_actions.cpp: Affliction 4pc initial stacks implemented in agony_t::execute_action
- sc_warlock_pets.cpp: Demonology 4pc dreadstalker +10% damage in dreadstalker_t::composite_player_multiplier

### What Was Added In This PR
1. Affliction 2pc: parse_effects in apply_action_effects() for +10% UA/SoC damage
2. Affliction 4pc: parse_effects for +20% Agony periodic damage
3. Demonology 2pc: parse_effects in apply_action_effects() for +15% Hand of Gul'dan damage
4. Demonology 4pc: +3 sec dreadstalker duration in call_dreadstalkers_t::execute
5. Destruction 2pc: parse_effects in apply_action_effects() for +5% Chaos Bolt/Rain of Fire
6. Destruction 4pc: +2 soul shard fragments in conflagrate_t::execute + parse_effects for +10% damage

### Pet Interactions (UNVERIFIED_IMPLEMENTATION notes)
- Demonology 4pc +10% dreadstalker damage: Implemented via dreadstalker_t::composite_player_multiplier
  The +3 sec duration is implemented by adding it to the spawn duration in call_dreadstalkers_t::execute
- PET SCALING NOTE: The dreadstalker damage buff is applied on the pet's own multiplier,
  which should be correct. Whether it also scales with player spell power is unverified.

### Important Mechanic Notes
- Agony initial stacks: The 4pc value 2 (from effectN(1)) represents ADDITIONAL stacks above base/talent.
  With Sudden Onset talent (base +3 stacks), the total would be +3 from talent + +2 from 4pc = +5 initial stacks.
- Conflagrate shard gen: Base conflagrate generates fragments, the 4pc adds a flat +2.
  In SimC, soul shards use 0.1 per fragment, so +2 fragments = +0.2 soul shards per Conflagrate cast.
- The Destro 4pc +10% damage buff (Effect #2) does NOT have PvP halving (PvP multiplier: 1.0).

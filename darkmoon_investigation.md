# Darkmoon Trinket + Sigil Investigation Report

Generated: 2026-03-27

## Items Overview

There are 3 tiers of items sharing 4 effects (Blood, Rot, Hunt, Void):

### Darkmoon Deck (Trinket)

| Name | Item ID | Equip Spell ID | Effect |
|------|---------|----------------|--------|
| Darkmoon Deck: Blood | 245855 | 1245001 | Farstrider's Guile — proc increases lowest secondary stat for 15s. Allied player death grants highest secondary for 15s (5min ICD). |
| Darkmoon Deck: Rot | 245846 | 1245051 | Rotting Roots — Nature DoT every 2s for 6s, stacks up to 10x, new stacks don't refresh old ones. |
| Darkmoon Deck: Hunt | 245829 | 1245050 | Grant secondary stats for 15s based on target creature type. |
| Darkmoon Deck: Void | 245750 | 1244254 | Void Glass — grants Versatility over 15s, multiple applications overlap. |

All 4 tooltips state: *"This effect is augmented by Darkmoon Sigil: [type]."*

### Darkmoon Dominion (Upgraded Trinket)

| Name | Item ID | Equip Spell ID | Effect |
|------|---------|----------------|--------|
| Darkmoon Dominion: Blood | 246305 | 1245001 | Same as Deck: Blood |
| Darkmoon Dominion: Rot | 246306 | 1245051 | Same as Deck: Rot |
| Darkmoon Dominion: Hunt | 246304 | 1245050 | Same as Deck: Hunt |
| Darkmoon Dominion: Void | 246307 | 1244254 | Same as Deck: Void |

Dominion uses the SAME spell IDs as regular Decks. Tooltip also says "augmented by Darkmoon Sigil: [type]". Difference is item level scaling only.

### Darkmoon Sigil (Embellishment — Optional Reagent)

| Name | Item IDs | Equip Spell ID | Effect |
|------|----------|----------------|--------|
| Darkmoon Sigil: Blood | 245871, 245872 | 1245053 | Same effect text as Deck: Blood |
| Darkmoon Sigil: Rot | 245877, 245878 | 1245055 | Same effect text as Deck: Rot |
| Darkmoon Sigil: Hunt | 245875, 245876 | 1245054 | Same effect text as Deck: Hunt |
| Darkmoon Sigil: Void | 245873, 245874 | 1245052 | Same effect text as Deck: Void |

Each sigil has 2 item IDs (different crafting difficulty tiers: +5 and +15). Applied to crafted weapons/off-hands as an embellishment. Unique-Equipped: Embellished (2).

Note: Wowhead tooltip numbers scale with the item level set on the page, so the raw numbers shown may not reflect actual in-game values at max ilvl. Ignore the specific stat values shown above.

## Spell ID Map

| Effect | Trinket/Dominion Driver | Embellishment Driver | RPPM Spell | Buff/Damage Spell |
|--------|------------------------|---------------------|------------|-------------------|
| Blood | 1245001 | 1245053 | 1245012 | 1245025 (stat buff) |
| Rot | 1245051 | 1245055 | 1244332 | 1247411 (async DoT) |
| Hunt | 1245050 | 1245054 | 1252457 | 1252486/1252487/1252488/1252489 (stat buffs by creature type) |
| Void | 1244254 | 1245052 | (in trigger) | (in trigger, vers buff, overlapping) |

## Current SimC Code Behavior

File: `engine/player/unique_gear_midnight.cpp`, lines 1116-1389 (darkmoon namespace)

Registration (lines 4137-4140):
```cpp
register_special_effect( { 1245001, 1245053 }, darkmoon::blood );
register_special_effect( { 1245055, 1245051 }, darkmoon::rot );
register_special_effect( { 1245052, 1244254 }, darkmoon::void_ );
register_special_effect( { 1245050, 1245054 }, darkmoon::hunt );
```

Each handler has this dedup guard:
```cpp
bool do_setup = find_special_effect( effect.player, effect.trigger()->id() ) == nullptr;
```

This means: if the trinket callback already exists when the embellishment registers (or vice versa), it skips creating a second callback. Current behavior = **mutually exclusive** (only one proc source works).

## What to Test In-Game

For each of the 4 types (Blood/Rot/Hunt/Void), test with combat logging enabled:

### Test 1: Trinket Only
- Equip Darkmoon Deck (or Dominion) alone
- Record: proc rate, buff name, buff value, buff duration

### Test 2: Sigil Only
- Remove trinket, equip weapon with Darkmoon Sigil only
- Record: does it proc? Same buff name? Same or different values?

### Test 3: Both Equipped
- Equip trinket + weapon with matching sigil
- Record what changes compared to Test 1:
  - Does proc rate increase? (double RPPM)
  - Does buff value increase? (augmented = bigger numbers)
  - Do you get two separate buffs? (stacking)
  - Is there a new/different buff that only appears with both?
  - Does buff duration change?

### Test 4: Dominion vs Deck
- Optional: verify Dominion behaves identically to Deck (same spell IDs suggest yes)

## Possible "Augmented" Meanings

| Possibility | What it looks like in combat log |
|-------------|--------------------------------|
| A. Double proc rate | Two separate proc events from one attack, or noticeably faster proc frequency |
| B. Higher buff values | Same buff name but larger stat number than trinket alone |
| C. Longer duration | Same buff but lasts longer than 15s |
| D. Additional stacking buff | Two distinct buff names/IDs active simultaneously |
| E. New bonus mechanic | A completely new effect that only appears when both are equipped |

## Priority

Blood and Rot are most commonly used in default profiles. Test those first.
Hunt requires specific creature types (configurable via `midnight.darkmoon_hunt_race`).
Void is straightforward (vers stacking).

## GitHub Reference

Issue #81: https://github.com/MubarakHAlketbi/simc/issues/81

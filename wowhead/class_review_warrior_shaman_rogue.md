# Class Code Audit Report: Warrior, Shaman, Rogue
Generated: 2026-03-17
Auditor: Hermes Agent (Midnight code vs info_base)

---

## Summary of Audit Process

Each class module was cross-referenced against the Wowhead Midnight info_base files
for Arms, Fury, Protection (Warrior), Elemental, Enhancement (Shaman), and
Assassination, Outlaw, Subtlety (Rogue). The audit checked:
1. Talent names in code vs info_base (fuzzy mismatch report + manual verification)
2. Talents in info_base not present in code (missing/TODO)
3. Talents in code not present in info_base (utility/removed)
4. Spell ID correctness where ID-based registration is used

---

## WARRIOR (engine/class_modules/sc_warrior.cpp)

### Changes Made

#### Champion (ID:376079) — Class Talent — TODO added
- The Midnight class talent tree lists "Champion" (ID:376079) as a class talent.
- This is DISTINCT from "Champion's Spear" which is already implemented.
- Added `// TODO: NYI - Champion (ID:376079)` comment near champion's_spear registration.
- Needs verification whether this is a passive gate node or an active DPS talent.

#### Odyn's Fury — NOTE added
- Code field `odyns_fury` registers "Odyn's Fury" — info_base shows "Odyn" (ID:385059).
- Assessed as likely info_base display truncation (Wowhead sometimes truncates long names).
- Added `// NOTE` comment; no code change. Verify in-game spell name if talent lookup fails.

#### Executioner's Wrath → Executioner — NOTE added
- Code registers "Executioner's Wrath" for Fury talent field `executioners_wrath`.
- Midnight info_base lists "Executioner" (ID:1265570) for Fury.
- Added NOTE comment; the rename cannot be confirmed without live DBC data since
  the info_base may also represent a different spell (Arms has Executioner's Precision ID:386634).
- Pending in-game verification.

### Items Confirmed Correct (no change needed)

| Code Field | Registers | Status |
|---|---|---|
| `crackling_thunder` (class) | "Crackling Thunder" (ID:203201) | CORRECT — in class tree |
| `crashing_thunder` (mountain_thane) | "Crashing Thunder" | CORRECT — separate hero talent |
| `storm_bolt` (class) | "Storm Bolt" (ID:107570) | CORRECT |
| `storm_bolts` (mountain_thane) | "Storm Bolts" | CORRECT — hero tree plural variant |
| `overwhelming_rage` (class) | "Overwhelming Rage" (ID:382767) | CORRECT |
| `overwhelming_blades` (slayer) | "Overwhelming Blades" | CORRECT — Slayer hero talent |
| `dual_wield_specialization` (class, Fury) | "Dual Wield Specialization" (ID:382900) | CORRECT — spec-filtered |
| `shield_specialization` (protection) | "Shield Specialization" | CORRECT — Protection spec talent |
| `master_of_warfare_1/2/3` | ID:1269314,1269306,1269307 | CORRECT — 3-rank apex talent |
| `rampaging_berserker_1/2/3` | ID:1269308,1269309,1269310 | CORRECT — 3-rank apex talent |
| `phalanx_1/2/3` | ID:1269311,1269312,1269313 | CORRECT — 3-rank apex talent |
| `champions_spear` | "Champion's Spear" | CORRECT — distinct from "Champion" |
| `executioners_precision` (arms) | "Executioner's Precision" | CORRECT — different from Fury executioner |

### Items Kept with Notes (not in info_base / utility)

- `berserker_shout` (class) — info_base shows "Berserker Stance" (ID:386196) for Fury.
  These may be different spells with similar names; class tree utility talent.
- `thunder_blast` (mountain_thane) — correctly registered, functional hero talent.

### Still Needs Investigation

- "Slayer" (ID:444779) — the hero tree entry node. Code has `slayers_dominance` which registers
  "Slayer's Dominance" (the key talent, ID not specified). The capstone node "Slayer" (ID:444779)
  is probably just a passive tree gate and not needed in code. Verify.

---

## SHAMAN (engine/class_modules/sc_shaman.cpp)

### Changes Made

#### mystic_knowledge — FIXED (was "Mystic Calling", now "Mystic Knowledge")
- Field `mystic_knowledge` was registered with `find_talent_spell(HERO, "Mystic Calling")`.
- Midnight info_base clearly lists "Mystic Knowledge" (ID:1270450) for the Farseer hero tree.
- **Fixed**: changed registration string to "Mystic Knowledge". Source: ID:1270450.

#### call_of_the_elements — NOTE added
- Field `call_of_the_elements` registered with "Call of the Elements".
- This talent does not appear in Midnight Elemental or Enhancement info_base.
- Midnight has "Echo of the Elements" (ID:333919) in the spec talent tree instead.
- Added NOTE comment: "not in Wowhead info_base (utility or removed)".

#### ancestral_guidance — NOTE added
- Field `ancestral_guidance` registered with "Ancestral Guidance".
- Not found in Midnight spec talent tables (utility/healing ability).
- Added NOTE comment.

#### supercharge — NOTE added (Stormbringer hero talent)
- Field `supercharge` in Stormbringer hero tree registers "Supercharge".
- This talent is NOT in the Midnight Stormbringer hero talent list in info_base.
- Enhancement spec tree has "Overcharge" (ID:1251026) — possible rename.
- Added NOTE comment. Cannot safely rename due to heavy usage throughout code.
- Stormbringer hero tree in info_base: Tempest, Unlimited Power, Stormcaller, Stormwell,
  Arc Discharge, Rolling Thunder, Natural Gift, Voltaic Surge, Conductive Energy,
  Descending Skies, Awakening Storms — no "Supercharge".

### Items Confirmed Correct (no change needed)

| Code Field | Registers | Status |
|---|---|---|
| `chaining_storms` (enhancement spec) | "Chaining Storms" (ID:334308) | CORRECT — in enhancement spec tree |
| `awakening_storms` (Stormbringer hero) | "Awakening Storms" (ID:455129) | CORRECT — Stormbringer capstone |
| `elemental_blast` | "Elemental Blast" | CORRECT — Enhancement spec talent |
| `echo_of_the_elements` | "Echo of the Elements" (ID:333919) | CORRECT — Elemental spec talent |
| `elemental_assault` (enhancement) | "Elemental Assault" (ID:210853) | CORRECT — Enhancement spec talent |
| `elemental_unity` (elemental) | "Elemental Unity" (ID:462866) | CORRECT — Elemental spec |
| `stormwell` (Stormbringer hero) | "Stormwell" (ID:1264762) | CORRECT |
| `lashing_flames` (enhancement) | "Lashing Flames" (ID:334046) | CORRECT |
| `searing_flames` (elemental) | "Searing Flames" (ID:381782) | CORRECT |
| `storm_unleashed_1/2/3` | ID:1262713,1262761,1252373 | CORRECT — 3-rank DPS talent |
| `feedback_loop_1/2/3` | "Feedback Loop" rank 1/2/3 (ID:1270061) | CORRECT — 3-rank Elemental DPS |
| `everlasting_elements` (elemental) | "Everlasting Elements" (ID:462867) | CORRECT |
| `whirling_elements` (Totemic hero) | "Whirling Elements" (ID:445024) | CORRECT |
| `ancestral_influence` (Farseer hero) | "Ancestral Influence" (ID:1270446) | CORRECT — renamed from ancestral_guidance |
| `windspeaker` (Farseer hero) | "Windspeaker" (ID:1270447) | CORRECT |
| `winds_of_alakir` | "Winds of Al'Akir" (ID:382215) | CORRECT — info_base truncated to "Winds of Al" |
| `flash_of_lightning` (elemental) | "Flash of Lightning" (ID:381936) | CORRECT — Elemental spec |
| `crash_lightning` (enhancement) | "Crash Lightning" (ID:187874) | CORRECT — Enhancement spec |
| `elemental_resonance` (elemental) | "Elemental Resonance" | CORRECT — distinct from "Elemental Resistance" (utility) |
| `storm_swell` (Stormbringer hero) | "Storm Swell" (ID:455089) | CORRECT |
| `elemental_orbit` (class) | "Elemental Orbit" (ID:383010) | CORRECT |

### Utility Talents (Skipped per rules)
The following were confirmed utility-only and not implemented (correct per audit rules):
- astral_shift, brimming_with_life, chain_heal, cleanse_spirit, earthgrab_totem
- elemental_warding (defensive), hex, mana_spring, refreshing_waters
- spiritwalker (Farseer), totemic_projection, voodoo_mastery, wind_rush_totem

---

## ROGUE (engine/class_modules/sc_rogue.cpp)

### Changes Made

#### Grand Melee (ID:1259469) — TODO added
- "Grand Melee" appears in Outlaw spec talent tree (Midnight info_base ID:1259469).
- This is a DPS-relevant finisher modifier talent for Outlaw.
- Not currently in code under any name.
- Added `// TODO: NYI - Grand Melee (ID:1259469)` comment in outlaw talent struct.

### Items Confirmed Correct (no change needed)

| Code Field | Registers | Status |
|---|---|---|
| `seal_fate` (assassination) | "Seal Fate" (ID:14190) | CORRECT — assassination spec talent |
| `deal_fate` (fatebound hero) | "Deal Fate" (ID:454419) | CORRECT — Fatebound hero |
| `doomblade` (assassination) | "Doomblade" (ID:381673) | CORRECT — assassination spec |
| `gloomblade` (subtlety) | "Gloomblade" (ID:200758) | CORRECT — subtlety spec |
| `audacity` (outlaw) | "Audacity" (ID:381845) | CORRECT — outlaw spec |
| `alacrity` (class) | "Alacrity" (ID:193539) | CORRECT — class talent |
| `deeper_stratagem` (class) | "Deeper Stratagem" (ID:193531) | CORRECT — class talent |
| `secret_stratagem` (subtlety) | "Secret Stratagem" (ID:394320) | CORRECT — subtlety spec (distinct from class) |
| `deadly_poison` (assassination) | "Deadly Poison" (ID:2823) | CORRECT — assassination spec |
| `deadly_precision` (class) | "Deadly Precision" (ID:381542) | CORRECT — class talent |
| `improved_wound_poison` (class) | "Improved Wound Poison" (ID:319066) | CORRECT — class talent |
| `improved_poisons` (assassination) | "Improved Poisons" (ID:381624) | CORRECT — assassination spec |
| `deathstalkers_mark` (hero) | "Deathstalker's Mark" | CORRECT — Deathstalker hero talent |
| `cloaked_in_shadow` (subtlety) | "Cloaked in Shadow" | CORRECT — subtlety-specific variant |
| `cloak_of_shadows` (class) | "Cloak of Shadows" (ID:31224) | CORRECT — class talent |
| `implacable_1/2/3` | ID:1265385,1265386,1265387 | CORRECT — 3-rank assassination talent |
| `gravedigger_1/2/3` | ID:1265861,1265862,1265863 | CORRECT — 3-rank outlaw talent |
| `ancient_arts_1/2/3` | ID:1268932,1268936,1268939 | CORRECT — 3-rank subtlety talent |
| `regicides_reward` | "Regicide's Reward" | NOTE: info_base has "Regicide" (ID:1250325) separately — may be same talent with shortened name |
| `goremaws_bite` (subtlety) | "Goremaw's Bite" (ID:426591) | CORRECT — Subtlety spec; info_base "Goremaw" is truncated |

### Notable Notes

- `regicides_reward` (assassination) registers "Regicide's Reward" but info_base shows
  "Regicide" (ID:1250325). This could be: (a) info_base truncation of "Regicide's Reward",
  or (b) a renamed talent. Functional difference unlikely but should be verified.

- `deathstalker` (ID:457052) — the hero tree entry node. Code has `deathstalkers_mark`
  which is the key DPS talent. The entry node "Deathstalker" may be just a gate node.

### Utility Talents (Skipped)
- cloak_of_shadows (movement/defensive utility)
- cloaked_in_shadow (defensive)

---

## Build Verification

Build system (cmake/ninja) not available in this environment.
Changes are syntactically minimal (comments and one string literal fix for shaman mystic_knowledge).
The only functional change is `sc_shaman.cpp` line 11128 where "Mystic Calling" → "Mystic Knowledge"
fixes a talent lookup that was searching for a non-existent Midnight talent name.

---

## Files Modified

1. `engine/class_modules/sc_warrior.cpp` — Added TODO and NOTE comments for Champion,
   Odyn's Fury, and Executioner's Wrath/Executioner mismatch.

2. `engine/class_modules/sc_shaman.cpp` — Fixed mystic_knowledge registration ("Mystic Calling"
   → "Mystic Knowledge" ID:1270450). Added NOTE comments for call_of_the_elements,
   ancestral_guidance (utility), and supercharge hero talent name ambiguity.

3. `engine/class_modules/sc_rogue.cpp` — Added TODO for Grand Melee (ID:1259469, Outlaw).

---

## TODO Items Requiring Future Implementation

| Class | Talent | ID | Priority | Notes |
|---|---|---|---|---|
| Warrior | Champion | 376079 | Medium | Class talent; verify if DPS gate or passive |
| Rogue | Grand Melee | 1259469 | High | Outlaw DPS finisher modifier |

## Confirmed Correct Multi-Rank Talents (3-rank apex)

| Class | Field | Spell ID |
|---|---|---|
| Warrior Arms | master_of_warfare_1/2/3 | 1269314/1269306/1269307 |
| Warrior Fury | rampaging_berserker_1/2/3 | 1269308/1269309/1269310 |
| Warrior Prot | phalanx_1/2/3 | 1269311/1269312/1269313 |
| Shaman Enh | storm_unleashed_1/2/3 | 1262713/1262761/1252373 |
| Shaman Ele | feedback_loop_1/2/3 | via "Feedback Loop" rank lookup |
| Rogue Assa | implacable_1/2/3 | 1265385/1265386/1265387 |
| Rogue Out | gravedigger_1/2/3 | 1265861/1265862/1265863 |
| Rogue Sub | ancient_arts_1/2/3 | 1268932/1268936/1268939 |

---
*Generated by Hermes Agent — Midnight Audit Pass 2026-03-17*

# Shaman Elemental Midnight Implementation Dossier
**Date:** 2026-03-16
**Expansion:** Midnight (Patch 12.0.1)
**Source:** wowhead.com guides and spell database

---

## General Changes (Midnight vs TWW)

### Removed Abilities
- Icefury & Frost Shock (removed from ST rotation)
- Primordial Wave (replaced by Voltaic Blaze + Purging Flames)
- Fire Elemental, Storm Elemental (via talent pruning)
- Deeply Rooted Elements
- Liquid Magma Totem
- Surge of Power
- Magma Chamber
- Echo of the Elementals
- Erupting Lava

### New Abilities
- Voltaic Blaze (spell ID: 1259101 / talent) - replaces Primordial Wave; refreshes Flame Shock, triggers Purging Flames
- Call of Fire (talent)
- Purging Flames (talent; triggers Lava Burst echoes on targets with Flame Shock)

### Key Mechanic Changes
- Ascendance overload damage bonus: 150% -> 75% (halved, smoother damage profile)
- Master of the Elements: still core rotational buff
- Lava Burst: still always crits on targets with Flame Shock
- Stormkeeper: grants 2 charges of instant LB at 150% damage with overload on every target
- Elemental Blast: still primary Maelstrom spender (single target)
- Earth Shock: secondary Maelstrom spender
- Earthquake: AoE Maelstrom spender
- Stat Priority: Mastery > Critical Strike = Haste > Versatility

### Hero Talents
- Stormbringer: Tempest, Supercharge - lightning-focused; best for raid/M+
- Farseer: Ancestral Swiftness, Routine Communication, Call of the Ancestors (mirrors spells)

---

## MID1 Tier Set: Mantle of the Primal Core (Set ID: 1988)

### Spell IDs
| Bonus | Spell ID | Description |
|-------|----------|-------------|
| 2pc | 1264862 | Shaman Elemental 12.0 Class Set 2pc |
| 2pc buff | 1272101 | Thunderous Velocity (haste buff) |
| 4pc | 1264863 | Shaman Elemental 12.0 Class Set 4pc |

### 2pc: Thunderous Velocity (Source: wowhead.com/spell=1264862)
- **Effect:** Casting Stormkeeper grants 15% haste for 10 sec
- **Implementation:** `buff.mid1_ele_2pc` triggered in `stormkeeper_t::execute()`
- **Buff spell:** 1272101 (Thunderous Velocity, 15% haste, 10s)
- **Status:** IMPLEMENTED

### 4pc (Source: wowhead.com/spell=1264863)  
- **Effect 1:** Stormkeeper grants 1 additional stack (base 2 -> 3 stacks)
- **Effect 2:** Increases damage of Lightning Bolt and Chain Lightning by 25% during Stormkeeper
- **DBC Notes:**
  - Effect 1 (id=1276470): Add 1 to stormkeeper stacks (effectN(5) of spell 191634)
  - Effect 2 (id=1285159): +25% to Stormkeeper effectN(4) - affects LB, CL, and overloads
  - Effect 3 (id=1299825): +1 to stormkeeper stack count trigger
  - PvP multiplier: 0.5 (50% reduction in PvP)
- **Implementation:**
  - Extra stack: `sk_stacks += sets->set(SHAMAN_ELEMENTAL, MID1, B4)->effectN(3).base_value()` in stormkeeper execute
  - Damage bonus: `sets->has_set_bonus(SHAMAN_ELEMENTAL, MID1, B4)` check in `composite_da_multiplier` using `effectN(2).percent()` (25%)
  - Applies to: LB, CL, LB Overload, CL Overload (via `affected_by_stormkeeper_damage_tier`)
- **Status:** IMPLEMENTED

---

## APL (Action Priority List)

### Status: ALREADY IMPLEMENTED
The Elemental APL was already present and correct in `apl_shaman.cpp`. It includes:
- Stormkeeper as first priority (sync with Ascendance window)
- Proper MotE (Master of the Elements) consumption
- Voltaic Blaze for Purging Flames / Flame Shock refresh
- Tempest integration (Stormbringer hero talent)
- Ancestral Swiftness (Farseer hero talent)
- Both `elemental()` and `elemental_ptr()` functions implemented

### Single Target Priority (Stormbringer)
1. Stormkeeper (on CD, sync with Ascendance)
2. Ancestral Swiftness
3. Ascendance  
4. Flame Shock maintenance
5. Voltaic Blaze (Purging Flames / FS refresh)
6. Lava Burst (no MotE, won't overcap)
7. Tempest (consume MotE) / Lightning Bolt (with SK)
8. Elemental Blast / Earth Shock (spenders)
9. Lightning Bolt (filler)

### AoE Priority
1. Stormkeeper / Ascendance  
2. Voltaic Blaze (Purging Flames trigger)
3. Earthquake (4+ targets)
4. Elemental Blast (3 targets)
5. Tempest
6. Chain Lightning

---

## Code Changes Made

### engine/class_modules/sc_shaman.cpp
1. **Line ~1376:** Added comment for mid1_ele_2pc/4pc buff struct
2. **Line ~3191-3198:** Fixed `affected_by_stormkeeper_damage_tier` block to explicitly use MID1 4pc set bonus multiplier (25%) instead of DBC effectN(4).percent() which returns 0
3. **Line ~8508-8521:** Modified stormkeeper execute to:
   - Add extra stack from 4pc DBC data (effectN(3) = 1)
   - Add source comments for both 2pc and 4pc

### APL: No changes needed (already complete)
### unique_gear_midnight.cpp: No changes needed (set bonus registered via DBC)

---

## Verification
- Build: PASS (no errors, warnings are pre-existing)
- Sim test: PASS (116k DPS, no crashes)
- Stormkeeper uptime: 18.9% without 4pc -> 26.1% with 4pc (confirms +1 stack working)
- Thunderous Velocity (2pc): 22.8% uptime confirmed

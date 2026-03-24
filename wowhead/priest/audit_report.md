# Priest Shadow — SimC vs Wowhead Audit Report
Generated: 2026-03-24
Expansion: Midnight (12.0.1) Season 1

## Summary

Overall the SimC APL is well-aligned with the Wowhead rotation guide. The APL is
significantly more sophisticated than the simplified Wowhead priority, which is
expected. However, the Midnight Season 1 tier set (Blind Oath's Burden) has NO
implementation in the SimC codebase, which is a critical gap.

---

## 1. TIER SET BONUSES — CRITICAL GAP

### Wowhead Data (Blind Oath's Burden)
- 2pc: Shadow Word: Madness damage increased by 10% and Insanity cost reduced by 5.
- 4pc: Shadowy Apparitions and Void Apparitions damage increased by 40%.

### SimC Status: NOT IMPLEMENTED
- Searched all priest module files (sc_priest.cpp, sc_priest_shadow.cpp, sc_priest.hpp)
  for MID1, MIDNIGHT, blind_oath, class_set, or any Midnight tier references.
- ZERO results found. The set_bonus_type_e enum does have MID1 defined in sc_enums.hpp,
  but no priest code references it.
- The only set bonus code in priest is legacy DF4 (Dragonflight Season 4) remapping.
- Neither the 2pc cost reduction nor the 4pc apparition damage buff is coded.

### Impact
- Shadow Word: Madness costs 5 more Insanity than it should with 2pc equipped.
- Shadowy Apparitions and Void Apparitions deal 40% less damage than they should with 4pc.
- This would noticeably undervalue tier gear in simulations.

---

## 2. ROTATION PRIORITY COMPARISON

### 2a. Archon Single-Target Priority (Wowhead vs APL)

| # | Wowhead Priority | APL Implementation | Status |
|---|------------------|--------------------|--------|
| 1 | Maintain Shadow Word: Pain | main list: shadow_word_pain with refreshable checks | PRESENT (low-priority filler + invoked_nightmare check) |
| 2 | Maintain Vampiric Touch (via Tentacle Slam or hardcast) | tentacle_slam + vampiric_touch with refreshable logic | PRESENT |
| 3 | Cast Halo | cds list: halo (unconditional within cds) | PRESENT |
| 4 | Cast Voidform | cds list: voidform,if=active_dot.shadow_word_pain>=active_dot.vampiric_touch | PRESENT |
| 5 | Cast Power Infusion | cds list: power_infusion synced with Voidform | PRESENT |
| 6 | Cast Void Volley | main list: void_volley (high priority, unconditional) | PRESENT |
| 7 | Shadow Word: Madness (maintain/avoid cap) | main list: shadow_word_madness with insanity.deficit<=35 and other conditions | PRESENT |
| 8 | Cast Mind Blast | main list: mind_blast with Mind Devourer check | PRESENT |
| 9 | Mind Flay: Insanity when SWM active | main list: mind_flay_insanity (uses buff check internally) | PRESENT |
| 10 | Shadow Word: Madness during Voidform | Handled via shadow_word_madness conditions | PRESENT |
| 11 | Tentacle Slam (no upcoming adds/movement) | main list: tentacle_slam with raid_event.adds checks | PRESENT |
| 12 | Mind Flay (filler, interrupt on higher priority) | main list: mind_flay with chain=1,interrupt_immediate=1,interrupt_if=ticks>=2 | PRESENT |
| 13 | Moving: Tentacle Slam / SW:D / SW:P | Low-priority entries at bottom of main list | PRESENT |

### 2b. Voidweaver Single-Target Priority (Wowhead vs APL)

| # | Wowhead Priority | APL Implementation | Status |
|---|------------------|--------------------|--------|
| 1 | Maintain Shadow Word: Pain | Present as described above | PRESENT |
| 2 | Maintain Vampiric Touch | Present as described above | PRESENT |
| 3 | Cast Voidform | Present, synced with dots | PRESENT |
| 4 | Cast Power Infusion | Present, synced with Voidform | PRESENT |
| 5 | SW:D if target has absorb shield | NOT IN APL — Wowhead says to use SW:D on absorb shields | MISSING |
| 6 | Void Blast (if SWM active or Rift expiring) | void_blast with target_if logic, entropic_rift checks in SWM line | PRESENT |
| 7 | Shadow Word: Madness (maintain/avoid cap, extra during Rift) | buff.entropic_rift.up condition present on SWM | PRESENT |
| 8 | Cast Void Volley | void_volley unconditional | PRESENT |
| 9 | Void Torrent to activate Entropic Rift | void_torrent with dots_up check | PRESENT |
| 10 | Cast Mind Blast | mind_blast present | PRESENT |
| 11 | Shadow Word: Madness (general) | Present | PRESENT |
| 12 | Tentacle Slam | Present | PRESENT |
| 13 | Mind Flay (filler) | Present with interrupt logic | PRESENT |
| 14 | Moving fillers | Present at bottom of list | PRESENT |

### 2c. Opener Sequence

Wowhead Archon opener:
1. Precast Tentacle Slam — APL precombat has tentacle_slam. PRESENT.
2. Shadow Word: Pain — Handled by priority. IMPLICIT.
3. Halo — In cds list. PRESENT.
4. Voidform — In cds list. PRESENT.
5. Power Infusion + Potion + Trinkets — PI in cds, potion in cds, trinkets in cds. PRESENT.
6. Void Volley — In main list. PRESENT.

Wowhead Voidweaver opener adds Void Torrent and Void Blast after Void Volley.
Both are in the APL main list in appropriate priority order. PRESENT.

---

## 3. KEY ABILITY IMPLEMENTATIONS

| Ability | Implemented | Notes |
|---------|-------------|-------|
| Shadow Word: Pain | YES | DoT with tick damage |
| Vampiric Touch | YES | DoT with self-healing |
| Mind Flay | YES | Channeled filler with interrupt logic |
| Mind Flay: Insanity | YES | Archon proc-based replacement, buff check coded |
| Mind Blast | YES | With Shadowy Insight proc support |
| Shadow Word: Madness | YES | Full implementation with Insanity cost, Mind Devourer interaction |
| Shadow Word: Death | YES | Execute and filler usage |
| Voidform | YES | Buff with Void Volley integration |
| Void Volley | YES | ST + AoE damage components |
| Void Torrent | YES | Entropic Rift trigger for Voidweaver |
| Void Blast | YES | Voidweaver-specific Mind Blast replacement during Rift |
| Tentacle Slam | YES | Applies VT + damage, maddening_tentacles interaction |
| Halo | YES | Full Archon implementation with Divine Halo return, Power Surge buff |
| Power Infusion | YES | With Twins of the Sun support |
| Entropic Rift | YES | Voidweaver buff, collapsing_void extension |

---

## 4. KEY TALENT IMPLEMENTATIONS

| Talent | Implemented | Notes |
|--------|-------------|-------|
| Surge of Insanity | YES | Mind Flay damage multiplier (confirmed) |
| Tormenting Whispers | YES | SWM damage multiplier (confirmed) |
| Psychic Link | YES | Full implementation with per-spell psychic link variants |
| Mind Devourer | YES | Buff check, SWM damage bonus, decrement on use |
| Shadowy Insight | YES | Proc trigger from Mind Blast |
| Ancient Madness | YES | Stacking buff during Voidform, exponential decay factor |
| Sustained Potency | YES | Buff system with Halo interaction |
| Manifested Power | YES | Triggered from Halo |
| Power Surge | YES | Buff triggered from Halo with tick scheduling |
| Divine Halo | YES | Return spell mechanic |
| Collapsing Void | YES | Entropic Rift extension on SWM cast |
| Voidheart | YES | Buff extension during Void Torrent |
| Maddening Tentacles | YES | SWM triggered cast with damage modifier |
| Invoked Nightmare | YES | SW:P refresh priority in APL |
| Distorted Reality | YES | Referenced in APL variable dr_force_prio |
| Void Apparitions | YES | Separate spell struct inheriting shadowy_apparition_base |
| Idol of N'Zoth | YES | Execute stack system on multiple abilities |
| Inescapable Torment | YES | SW:D condition with pet active |
| Deathspeaker | YES | Health threshold modifier in APL |
| Devour Matter | YES | Force SW:D priority in APL |
| Mental Fortitude | YES | Absorb buff implementation |

---

## 5. DIFFERENCES AND ISSUES

### CRITICAL
1. **Midnight S1 Tier Set (Blind Oath's Burden) NOT IMPLEMENTED**
   - 2pc: SWM +10% damage, -5 Insanity cost — NOT CODED
   - 4pc: Shadowy/Void Apparitions +40% damage — NOT CODED
   - The MID1 enum exists but priest code never references it.

### MODERATE
2. **Voidweaver: SW:D on absorb shields not in APL**
   - Wowhead says: "Cast Shadow Word: Death if the target has an absorb shield."
   - APL has no absorb shield detection condition. SimC may lack the ability to
     detect target absorb shields, making this impractical to implement.

3. **AoE priority is identical to ST in the Wowhead guide**
   - Both Archon and Voidweaver AoE priorities on Wowhead are copy-pasted from ST.
   - The APL has a separate AoE path (active_enemies>2) that calls aoe_variables
     but then falls through to main. The AoE handling is more nuanced in the APL
     with VT target capping (max_vts), dot tracking, and Tentacle Slam holding logic.
   - This is APL being BETTER than the guide, not a gap.

### MINOR / INFORMATIONAL
4. **APL includes abilities not in Wowhead priority list**
   - shadow_word_death with Devour Matter forcing (niche talent interaction)
   - shadow_word_madness pmultiplier refresh (pandemic multiplier optimization)
   - heal_for_tof (Twist of Fate healing proc via Holy Nova)
   - flash_heal for Nexus-King's Command trinket proc
   - These are advanced optimizations beyond what a guide would cover. NOT issues.

5. **Wowhead mentions Light's Potential potion in opener**
   - APL uses lights_potential_2 for level >80 characters. ALIGNED.

6. **Shadowform pre-combat**
   - Wowhead: "Apply Shadowform" pre-combat check.
   - APL: shadowform,if=!buff.shadowform.up in precombat. ALIGNED.

7. **Power Word: Fortitude**
   - Wowhead mentions as pre-combat buff.
   - Not in APL (raid buffs typically handled externally in SimC). EXPECTED.

---

## 6. APL STRUCTURE NOTES

The APL uses a clean structure:
- precombat: Shadowform, trinket variables, Tentacle Slam precast
- default: Holding logic, AoE branch (>2 targets), run main
- aoe/aoe_variables: VT target capping, dot tracking, Tentacle Slam holding
- cds: Potion, racials, PI, Halo, Voidform, trinkets, Desperate Prayer
- main: Full priority list with sophisticated target_if and condition logic
- trinkets: Badge of Ferocity special case + general use_items
- heal_for_tof: Twist of Fate healing proc

Both shadow() and shadow_ptr() APL functions are IDENTICAL, suggesting no PTR
changes are pending.

---

## 7. RECOMMENDATIONS

1. **URGENT: Implement Midnight S1 tier set (MID1) for Shadow Priest**
   - 2pc: Add -5 Insanity cost and +10% damage modifier to Shadow Word: Madness
   - 4pc: Add +40% damage modifier to Shadowy Apparitions and Void Apparitions
   - Reference spell data for "Priest Shadow 12.0 Class Set" 2pc and 4pc

2. **CONSIDER: Add absorb shield detection for Voidweaver SW:D priority**
   - Low priority as this is a niche interaction

3. **VERIFY: Wowhead AoE priorities appear to be duplicated from ST**
   - The Wowhead extracted data shows identical ST and AoE priorities for both
     hero talents. This may be an extraction artifact or the guide genuinely
     recommends the same priority. The APL's AoE handling is more sophisticated
     regardless.

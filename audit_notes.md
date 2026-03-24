# SimulationCraft Midnight — Full Spec Audit Notes
# Date: 2026-03-24
# Methodology: For each of 33 specs, compared Wowhead extracted data (rotation.md, tier.md, info_base.md) against SimC code (APL generators + class modules)

Individual per-class reports are in wowhead/{class}/audit_report.md

---

## CRITICAL ISSUES (require immediate fix — large DPS impact)

### 1. [DH Havoc] Tier Set COMPLETELY UNIMPLEMENTED
- File: engine/class_modules/sc_demon_hunter.cpp
- The MID1 2pc (Blade Dance +15% damage) and 4pc (+6% haste in Metamorphosis) have ZERO code
- Impact: Havoc sims significantly undervalue tier gear
- Fix: Implement DEMON_HUNTER_HAVOC set bonus handlers

### 2. [Druid Guardian] APL is a PLACEHOLDER STUB
- File: engine/class_modules/apl/druid/guardian_apl.inc
- Labeled "assisted_combat" — NOT a real rotation
- Missing: Ironfur, Frenzied Regeneration, Incarnation, Barkskin, Heart of the Wild, Raze, Red Moon
- Maul threshold rage>=8 instead of ~80 (Harnessed Rage)
- No hero talent branching, no rage management
- Convoke appears twice (likely bug)
- Impact: All Guardian sim results are MEANINGLESS
- Fix: Complete APL rewrite needed

### 3. [Evoker Augmentation] Midnight S1 Tier Set NOT IMPLEMENTED
- File: engine/class_modules/sc_evoker.cpp
- Only old TWW1 tier bonuses exist. New 2pc (Eruption +15% dmg, +0.3s EM extension) and 4pc (empowers +20% dmg/CDR during EM) missing
- Impact: Aug Evoker significantly undervalued with tier gear

### 4. [Priest Shadow] Midnight S1 Tier Set NOT IMPLEMENTED
- File: engine/class_modules/sc_priest.cpp / sc_priest_shadow.cpp
- MID1 enum exists in sc_enums.hpp but zero priest code references it
- 2pc (SW:M +10% dmg, -5 Insanity cost) and 4pc (Apparitions +40% dmg) both missing
- Impact: Shadow sims undervalue tier gear significantly

### 5. [Enhancement Shaman] Midnight S1 Tier Set NOT IMPLEMENTED
- File: engine/class_modules/sc_shaman.cpp
- Only Elemental MID1 tier exists. Enhancement 2pc (+15% Stormstrike/Lava Lash damage) and 4pc (+2% Mastery per Crash Lightning stack) completely missing
- Impact: Enhancement sims undervalue tier gear

### 6. [Windwalker Monk] Tier Set Appears NOT IMPLEMENTED
- File: engine/class_modules/monk/sc_monk.cpp
- No WINDWALKER MID1 set bonus code found — only Brewmaster tier bonuses registered
- May be auto-parsed via spell data, but explicit code is missing
- Impact: Needs verification — if truly missing, WW sims undervalue tier

---

## HIGH ISSUES (significant DPS accuracy impact)

### 7. [DH Devourer] Void-Scarred In-Meta Priority Inversion
- File: engine/class_modules/apl/apl_demon_hunter.cpp
- Wowhead: Cull > Void Ray inside Void Metamorphosis
- APL: Void Ray (line 113) before Cull dispatch (lines 112/117)
- Impact: Wrong ability prioritization during metamorphosis

### 8. [DH Devourer] Soul Smuggling Not Modeled
- Soul Fragment management before form transitions has no APL logic
- This is the signature Devourer optimization

### 9. [DH Havoc] Inertia Ordering Wrong
- Wowhead: Inertia consumption is #1 priority
- APL: Buried after cooldown sub-list calls

### 10. [DK Unholy] Death Coil RP Threshold
- APL uses rune-based spending logic instead of Wowhead's 80 RP threshold
- Impact: Resource spending cadence differs

### 11. [DK Unholy] Soul Reaper Restricted to <=35% HP
- APL: soul_reaper only in execute phase (<=35% HP)
- Wowhead: Cast on cooldown unconditionally
- Impact: Major DPS loss outside execute phase

### 12. [DK Frost] Remorseless Winter Not in Wowhead
- APL casts Remorseless Winter in cooldowns
- Wowhead rotation has zero mention of it
- May be SimC optimization or Wowhead guide omission

### 13. [Evoker Devastation] Engulf Missing from Flameshaper APL
- File: engine/class_modules/apl/apl_evoker.cpp
- st_fs and aoe_fs lists contain zero Engulf references
- This is a CORE Flameshaper ability
- Impact: Flameshaper profiles significantly underperform

### 14. [Monk Brewmaster] Touch of Death Missing from APL
- Wowhead's #1 priority ability is completely absent from the APL
- Impact: Missing significant damage

### 15. [Monk Brewmaster] Blackout Combo Sequencing Not Modeled
- Wowhead emphasizes BoK -> Tiger Palm combo
- APL puts Blackout Kick near the bottom
- Impact: Key mechanic not leveraged

### 16. [Rogue Subtlety] Shadow Dance CP Threshold Wrong for Deathstalker
- APL requires 6+ CP to enter Shadow Dance for ALL hero talents
- Wowhead: Deathstalker should enter with LOW combo points (Trickster enters with 6+)
- Impact: Fundamental rotation mismatch for Deathstalker builds

### 17. [Frost Mage] Spellslinger Priority Mismatches
- Fingers of Frost 2-stack priority missing from APL
- Glacial Spike vs FoF ordering swapped vs Wowhead
- Comet Storm in Spellslinger lists but Wowhead doesn't list it for that hero talent

---

## MEDIUM ISSUES (moderate DPS impact or behavior correctness)

### 18. [DK Unholy] AoE Putrefy Priority Too Low
- APL: position 7 (last); Wowhead: position 4 (before spenders)

### 19. [DK Unholy] San'layn-specific Optimizations Absent
- No hero-talent-specific priority adjustments for San'layn

### 20. [DH Vengeance] Spirit Bomb Fragment Threshold Dynamic vs Fixed
- APL: dynamic 3-5 fragments; Wowhead: flat 6

### 21. [Druid Balance] Convoke Missing AP<40 Condition
- Wowhead says cast Convoke when AP < 40; APL has no such condition

### 22. [Druid Balance] Eclipse Entry AP Threshold Mismatch
- APL: 60 AP for Eclipse entry; Wowhead: 90% threshold

### 23. [Evoker Devastation] Deep Breath Missing for Scalecommander ST
- APL only uses Deep Breath to refresh Strafing Run, not on cooldown

### 24. [Hunter BM] Pack Leader ST Missing Killer Cobra
- Only in Dark Ranger list, not Pack Leader

### 25. [Hunter BM] Barbed Shot Pre-BW Window
- APL: ~1.5s; Wowhead: 3s recommendation

### 26. [Mage Fire] Sunfury Flamestrike Target Threshold
- APL: 3 targets; Wowhead: 4 targets

### 27. [Mage] Tier Set Bonuses Need Verification
- Arcane 4pc, Fire 2pc, Frost 2pc — no explicit code; may be auto-parsed from DBC

### 28. [Monk Brewmaster] Missing Spinning Crane Kick in AoE
- AoE filler completely absent from APL

### 29. [Paladin Retribution] Hammer of Light Conditions Oversimplified
- Missing AW/Undisputed Ruling/proc expiry logic from Wowhead

### 30. [Priest Shadow] Voidweaver SW:D on Absorb Shields Missing
- Wowhead specifically calls for SW:D on absorb shields; no APL condition for this

### 31. [Shaman Elemental] AoE Target Threshold Mismatch  
- APL: >=3 targets; Wowhead: 2 targets

### 32. [Warlock Demonology] No AoE Action Lists
- Single default list for all target counts; all other specs have separate AoE lists

### 33. [Warlock Demonology] No Hero Talent Branching
- No Diabolist vs Soul Harvester routing in APL

### 34. [Warlock Destruction] 4pc Damage Bonus Comment Mismatch
- Code comment says 10%, Wowhead says 20%; actual value from spell data

### 35. [Rogue Subtlety] Shadowstrike AoE Threshold Off
- APL: <=2 targets; Wowhead: <=3 targets

---

## LOW ISSUES (minor impact or acceptable SimC optimizations)

### 36. [DK Blood] Extra Unconditional Death Strike Fillers
- APL has mid-priority Death Strike not in Wowhead

### 37. [DK Frost] ERW Conditions More Complex Than Wowhead
- SimC has very detailed ERW gating; Wowhead is simpler (likely SimC optimization)

### 38. [Druid Feral] Outdated Algethar Puzzle Box Reference
- Stale trinket reference in APL

### 39. [Hunter MM] Volley Before Trueshot
- Intentional for Double Tap management; differs from Wowhead literal ordering

### 40. [Paladin Protection] Judgment Priority Lower Than Wowhead
- Wowhead: #2; APL: #11/#16/#20 — may be SimC optimization

### 41. [Warrior Fury] Crushing Blow Priority Higher Than Wowhead
- SimC optimization, not a bug

### 42. [Evoker] APL Typos
- "Fameshaper" and "Scalemander" in comments (should be Flameshaper, Scalecommander)

---

## WELL-IMPLEMENTED (confirmed working correctly)

### Tier Sets Confirmed Working:
- DK Blood 2pc/4pc ✓
- DK Frost 2pc/4pc ✓
- DK Unholy 2pc/4pc ✓
- Druid Balance 2pc/4pc ✓
- Druid Feral 2pc/4pc ✓ (4pc may use auto-parse)
- Shaman Elemental 2pc/4pc ✓
- Warlock Affliction 2pc/4pc ✓
- Warlock Demonology 2pc/4pc ✓
- Warlock Destruction 2pc/4pc ✓
- Warrior Arms 2pc/4pc ✓
- Warrior Fury 2pc/4pc ✓
- Warrior Protection 2pc/4pc ✓
- Paladin Protection 2pc/4pc ✓
- Paladin Retribution 4pc ✓
- Rogue Assassination 2pc/4pc ✓
- Rogue Outlaw 2pc/4pc ✓
- Rogue Subtlety 2pc/4pc ✓
- Hunter BM 2pc/4pc ✓
- Hunter MM 2pc/4pc ✓
- Hunter SV 2pc/4pc ✓
- Monk Brewmaster 2pc/4pc ✓

### Tier Sets MISSING/UNVERIFIED:
- DH Havoc 2pc/4pc ✗ (COMPLETELY MISSING)
- Evoker Augmentation 2pc/4pc ✗ (COMPLETELY MISSING)
- Priest Shadow 2pc/4pc ✗ (COMPLETELY MISSING)
- Enhancement Shaman 2pc/4pc ✗ (COMPLETELY MISSING)
- Windwalker Monk 2pc/4pc ? (NEEDS VERIFICATION)
- Mage Arcane 4pc ? (needs verification — may be DBC auto-parsed)
- Mage Fire 2pc ? (needs verification — may be DBC auto-parsed)
- Mage Frost 2pc ? (needs verification — may be DBC auto-parsed)
- Paladin Retribution 2pc ? (needs verification — may be DBC auto-parsed)
- DH Vengeance 2pc/4pc ? (not explicitly checked)
- DH Devourer 2pc/4pc ? (not explicitly checked)
- Druid Guardian 2pc/4pc ? (not explicitly checked)

### Apex Talents Confirmed:
- All 33 specs have 4-rank apex talents registered ✓

### Key Mechanics Confirmed:
- DK: ability replacement system (necrotic_coil, graveyard, vampiric_strike, festering_scythe, frostbane) ✓
- DH: Demonsurge ordering fix ✓  
- Evoker: Rising Fury, Duplicate apex ✓
- Hunter: all passive mechanics, Double Tap management ✓
- Monk: Weapon of Wind, Rushing Wind Kick, Combo Strike enforcement ✓
- Paladin: Holy Armaments next_armament system ✓
- Rogue: Sudden Demise execute, Grand Melee, Darkest Night ✓
- Shaman: Lava Flows, surging_shields ✓
- Warlock: Gorefiend's Avarice drain_life, Wither pandemic ✓
- Warrior: Master of Warfare, Rampaging Berserker, Phalanx ✓

---

## SUMMARY BY PRIORITY

| Priority | Count | Description |
| :--- | ---: | :--- |
| CRITICAL | 6 | 4 missing tier sets + Guardian stub APL + WW tier unverified |
| HIGH | 11 | APL priority inversions, missing core abilities |
| MEDIUM | 18 | Threshold mismatches, missing conditions, missing AoE lists |
| LOW | 7 | Minor optimizations, stale references, typos |
| **TOTAL** | **42** | |

### Top 5 Most Impactful Fixes:
1. Implement DH Havoc tier set (2pc+4pc)
2. Rewrite Druid Guardian APL from scratch
3. Implement Evoker Augmentation tier set (2pc+4pc)
4. Implement Priest Shadow tier set (2pc+4pc)
5. Implement Enhancement Shaman tier set (2pc+4pc)

These 5 fixes alone would dramatically improve simulation accuracy for 5 specs.

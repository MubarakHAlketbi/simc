# Behavioral Audit — Tier Set Tooltip vs C++ Code

Date: 2026-03-31
Build: 12.0.1.66709 Live
Method: Wowhead tooltip text compared against C++ implementation behavior

## Issues Found

### BUG: Shaman Enh 2pc effectN index (LOW — no DPS impact currently)
Lava Lash damage modifier reads effectN(1) which is the Stormstrike modifier.
Should read effectN(2) for Lava Lash. Both are 15% currently, so no output
difference, but code reads the WRONG semantic field.

### BUG-RISK: Monk WW 4pc CDR method (MEDIUM)
Uses per-cast cooldown->adjust(-5s) instead of passive base cooldown reduction.
The DBC spell data modifier type is "Modifies Cooldown (11)" which should be a
base CD modifier that interacts with haste differently. Current implementation
may double-dip if the passive modifier is also auto-applied by the engine.
NEEDS EMPIRICAL TEST: check if WDP/SotWL base cooldowns are already reduced.

### MEDIUM: Priest Shadow 2pc scope
DBC spell data's affected-spells class mask covers both Shadow Word: Madness AND
Devouring Plague, but our code only applies the +10% damage and -5 insanity cost
to Shadow Word: Madness. If the game also buffs Devouring Plague, we're missing
significant damage.
NEEDS EMPIRICAL TEST: sim with/without tier, check DP damage delta.

### MEDIUM: Shaman Enh 4pc mastery scaling
Code adds raw value 2 to composite_mastery() per Crash Lightning stack.
Tooltip says "+2% mastery" but mastery rating conversion may not be 1:1.
The code adds 2 to mastery RATING, not 2% mastery. Depending on the mastery
coefficient, this could grant more or less than 2% actual benefit.
NEEDS EMPIRICAL TEST: check mastery value with 1 vs 5 CL stacks.

### MINOR: Paladin Ret 4pc Empyrean Legacy interaction
When TV triggers + Empyrean Legacy procs DS simultaneously, code combines both
into a single Expurgation trigger. Game may apply two separate Expurgation
instances with pandemic behavior. Low impact.

### MINOR: DK Unholy 4pc ICD discrepancy
Tooltip says 300ms cooldown, buff spell (1271199) shows 500ms ICD on Wowhead.
Code inherits from buff spell. If game uses 300ms, we're being too conservative.

### MINOR: DK Blood 2pc RP indirection
RP gain uses auxiliary spell 1271198 instead of set bonus effectN(2) directly.
Values likely match but creates maintenance risk.

## Verified Correct (no issues)

| Spec | 2pc | 4pc |
|------|-----|-----|
| DH Havoc | CORRECT (15% BD, data-driven) | CORRECT (+6% haste Meta, data-driven) |
| DK Blood | CORRECT (8% BB + 3 RP) | CORRECT (8% DS + 10% BB reset) |
| DK Unholy | CORRECT (25% DP/VP, data-driven) | CORRECT (Blighted buff, auto-parsed) |
| Druid Guardian | CORRECT (10% Maul/MF, data-driven) | CORRECT (5% GG + Celestial Might RPPM) |
| Monk WW | CORRECT (30% WDP/SotWL) | BUG-RISK (CDR method) |
| Paladin Ret | N/A (2pc not ours) | CORRECT (TV 100% / DS 50% Expurgation) |
| Priest Shadow | MEDIUM (scope question) | CORRECT (40% apparitions) |
| Shaman Ele | CORRECT (haste buff) | CORRECT (+1 SK stack, +25% LB/CL) |
| Shaman Enh | BUG (wrong effectN) | MEDIUM (mastery scaling) |
| Warlock Demo | CORRECT (15% HoG, data-driven) | CORRECT (+10% + 3s duration) |
| Warlock Destro | CORRECT (5% CB/RoF, data-driven) | CORRECT (+2 frags + 10% damage) |

## Empirical Tests Needed

1. Monk WW 4pc: Check if WDP/SotWL base CD is already reduced by passive aura
2. Priest Shadow 2pc: Check if Devouring Plague damage changes with tier on/off
3. Shaman Enh 4pc: Check actual mastery value with varying CL stacks

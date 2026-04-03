# Druid Balance Elune DPS Gap — Root Cause Analysis

**Date:** 2026-04-02
**Investigator:** Hermes Agent

## Summary

The MID1_Druid_Balance_Elune profile showed 53,857 DPS vs the base MID1_Druid_Balance
profile at 76,067 DPS — a 29% gap that was suspiciously large for a hero-talent variant.

After investigation, **the gap was confirmed to be a bug in the APL `ec_cd_condition`
variable**, not an engine/NYI issue.

## Findings

### Actual DPS Numbers (3000-iter Patchwerk)
- Elune BEFORE fix:  53,874 DPS
- Elune AFTER fix:   71,185 DPS  (+17,311, +32.1%)
- Balance Base:      76,021 DPS
- Remaining gap:     -4,836 DPS (-6.4%) — this is EXPECTED and legitimate

### Root Cause: Inverted/Over-constrained `ec_cd_condition`

**File:** profiles/MID1/MID1_Druid_Balance_Elune.simc

**Old (broken) condition:**
```
variable,name=ec_cd_condition,value=!buff.eclipse_lunar.up & hero_tree.elunes_chosen
  & !buff.ca_inc.up & (!talent.convoke_the_spirits & hero_tree.elunes_chosen &
  (trinket.1.cooldown.duration<=100 & ... | trinket.1.cooldown.duration>=100 &
  cooldown.ca_inc.charges_fractional=1 & ...))|fight_remains<10
```

**Problem:** The leading `!buff.eclipse_lunar.up` check BLOCKS Celestial Alignment /
Incarnation from firing whenever the player is INSIDE Lunar Eclipse.

For Elune's Chosen, Lunar Eclipse uptime was ~40% and the player should ideally USE
CA/Incarnation DURING or right before Lunar Eclipse to stack buffs. The `!` inversion
means Incarnation was only being triggered when Lunar Eclipse was already DOWN — which
is the wrong window entirely.

**Result:** Only 2.0 Incarnation uses per 300s fight (instead of the correct ~4.0 uses).
This cost ~17,000 DPS (32% reduction).

**Fixed condition:**
```
variable,name=ec_cd_condition,value=hero_tree.elunes_chosen & !buff.ca_inc.up
  & cooldown.ca_inc.charges_fractional>=1 | fight_remains<10
```

This fires CA/Incarnation whenever it has a full charge available and isn't already active.

### Per-Ability DPS Comparison (before vs after fix)

| Ability             | Before Fix | After Fix | Base  | Note                          |
|---------------------|-----------|-----------|-------|-------------------------------|
| starsurge           | 16,396    | 22,670    | 3,425 | Elune spends more on SS       |
| shooting_stars      | 9,057     | 11,755    | 12,424| More SS procs with CA windows |
| starfire            | 5,388     | 6,399     | 0     | Elune uses starfire, not wrath|
| astral_smolder      | 3,132     | 6,106     | 7,057 | Better buff uptime            |
| fury_of_elune       | 2,943     | 4,061     | 1,164 | Elune-specific talent         |
| force_of_nature     | 0         | 0         | 14,276| KOTG only — expected absent   |

### Why ~6% gap Remains (Expected)
Per Wowhead guide: "Elune's Chosen is NOT the recommended build for single target."
It is designed for AoE content. The 6.4% ST gap vs KOTG is by-design.

## Engine NYI Assessment
No NYI/TODO issues found in sc_druid.cpp for Elune's Chosen. All relevant talents
(lunar_calling, the_light_of_elune, orbit_breaker, etc.) have implementations.
The single TODO found ("determine if duration increased by guardian of elune") is
in a Guardian spec context, not Balance/Elune's Chosen.

## Fix Applied
**File modified:** `profiles/MID1/MID1_Druid_Balance_Elune.simc`
- Replaced the broken `ec_cd_condition` variable with a correct simplified form.

## Validation
Post-fix 3000-iter Patchwerk run:
- DPS: 71,185 (was 53,874) — +32.1%
- Incarnation uses/fight: ~4.0 (was 2.0)
- Gap to base profile: -6.4% (was -29.1%) — now within expected range

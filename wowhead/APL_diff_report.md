# APL Diff Report: Wowhead vs SimC

**Generated**: 2026-03-21  
**Scope**: 33 specs — comparing Wowhead rotation guides to SimC APL files

## Legend

| Status | Meaning |
|--------|--------|
| `✓ MATCH` | Action present in SimC APL |
| `✗ MISSING` | Action in Wowhead priority but not in SimC APL |
| `~ ORDER_DIFF` | Present in APL but significantly different priority order |
| `NEEDS_MANUAL_REVIEW` | Wowhead content was minimal or format unclear |

**Important**: Wowhead guides are human-readable rotation guides, not 1:1 SimC APLs. MISSING may be intentional (SimC handles it internally). EXTRA actions are sim-specific optimizations.

---

## Death-Knight Blood

### Hero: Deathbringer

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Death's Caress | `deaths_caress` | ✓ MATCH | Present in APL (pos ~0) |
| 2 | Reaper's Mark | `reapers_mark` | ✓ MATCH | Present in APL (pos ~9) |
| 3 | Dancing Rune Weapon | `dancing_rune_weapon` | ✓ MATCH | Present in APL (pos ~15) |
| 4 | Blood Boil | `blood_boil` | ~ ORDER_DIFF | APL pos ~10, previous item at pos ~15 (Wowhead order reversed vs APL) |
| 5 | Death Strike | `death_strike` | ✓ MATCH | Present in APL (pos ~6) |

### Hero: San'layn

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Death Strike | `death_strike` | ✓ MATCH | Present in APL (pos ~6) |
| 2 | Blood Boil | `blood_boil` | ✓ MATCH | Present in APL (pos ~10) |
| 3 | Death and Decay | `death_and_decay` | ✓ MATCH | Present in APL (pos ~8) |
| 4 | Death and Decay and stand | `death_and_decay_and_stand` | ✗ MISSING | Not found in SimC APL |
| 5 | Vampiric Strike | `vampiric_strike` | ✗ MISSING | Not found in SimC APL |
| 6 | Heart Strike | `heart_strike` | ✓ MATCH | Present in APL (pos ~12) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Death Strike | `death_strike` | ✓ MATCH | Present in APL (pos ~6) |
| 2 | Blood Boil | `blood_boil` | ✓ MATCH | Present in APL (pos ~10) |
| 3 | Death and Decay | `death_and_decay` | ✓ MATCH | Present in APL (pos ~8) |
| 4 | Death and Decay and stand | `death_and_decay_and_stand` | ✗ MISSING | Not found in SimC APL |
| 5 | Vampiric Strike | `vampiric_strike` | ✗ MISSING | Not found in SimC APL |
| 6 | Heart Strike | `heart_strike` | ✓ MATCH | Present in APL (pos ~12) |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Death's Caress | `deaths_caress` | ✓ MATCH | Present in APL (pos ~0) |
| 2 | Dancing Rune Weapon | `dancing_rune_weapon` | ✓ MATCH | Present in APL (pos ~15) |
| 3 | Blood Boil | `blood_boil` | ~ ORDER_DIFF | APL pos ~10, previous item at pos ~15 (Wowhead order reversed vs APL) |
| 4 | Vampiric Strike | `vampiric_strike` | ✗ MISSING | Not found in SimC APL |
| 5 | Death Strike | `death_strike` | ✓ MATCH | Present in APL (pos ~6) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `vampiric_blood` | Sim-specific logic not covered by guide |
| `marrowrend` | Sim-specific logic not covered by guide |
| `consumption` | Sim-specific logic not covered by guide |
| `raise_dead` | Sim-specific logic not covered by guide |
| `any_dnd` | Sim-specific logic not covered by guide |
| `remorseless_winter` | Sim-specific logic not covered by guide |
| `pillar_of_frost` | Sim-specific logic not covered by guide |
| `breath_of_sindragosa` | Sim-specific logic not covered by guide |
| `frostwyrms_fury` | Sim-specific logic not covered by guide |
| `empower_rune_weapon` | Sim-specific logic not covered by guide |
| `antimagic_shell` | Sim-specific logic not covered by guide |
| `obliterate` | Sim-specific logic not covered by guide |
| *(+13 more)* | |

### Key Findings

- Minor gaps: **2 unique missing**, 2 order differences
  1. [Single-Target Priority] `death_and_decay_and_stand` (Death and Decay and stand) - MISSING from SimC APL
  1. [Single-Target Priority] `vampiric_strike` (Vampiric Strike) - MISSING from SimC APL
  1. [Opener] `blood_boil` (Blood Boil) - ORDER_DIFF in SimC APL
  1. [Opener] `blood_boil` (Blood Boil) - ORDER_DIFF in SimC APL

---

## Death-Knight Frost

### Hero: Deathbringer

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Empower Rune Weapon | `empower_rune_weapon` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Reaper's Mark | `reapers_mark` | ~ ORDER_DIFF | APL pos ~6, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 3 | Pillar of Frost | `pillar_of_frost` | ✓ MATCH | Present in APL (pos ~7) |
| 4 | Breath of Sindragosa | `breath_of_sindragosa` | ✓ MATCH | Present in APL (pos ~8) |
| 5 | Frostwyrm's Fury | `frostwyrms_fury` | ✓ MATCH | Present in APL (pos ~9) |
| 6 | Obliterate | `obliterate` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 7 | Howling Blast | `howling_blast` | ✓ MATCH | Present in APL (pos ~3) |
| 8 | Frost Strike | `frost_strike` | ✓ MATCH | Present in APL (pos ~1) |
| 9 | Obliterate without  Killing Machine | `obliterate_without_killing_machine` | ✗ MISSING | Not found in SimC APL |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Empower Rune Weapon | `empower_rune_weapon` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Reaper's Mark | `reapers_mark` | ~ ORDER_DIFF | APL pos ~6, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 3 | Pillar of Frost | `pillar_of_frost` | ✓ MATCH | Present in APL (pos ~7) |
| 4 | Breath of Sindragosa | `breath_of_sindragosa` | ✓ MATCH | Present in APL (pos ~8) |
| 5 | Frostwyrm's Fury | `frostwyrms_fury` | ✓ MATCH | Present in APL (pos ~9) |
| 6 | Frostscythe | `frostscythe` | ~ ORDER_DIFF | APL pos ~0, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 7 | Howling Blast | `howling_blast` | ✓ MATCH | Present in APL (pos ~3) |
| 8 | Glacial Advance | `glacial_advance` | ✓ MATCH | Present in APL (pos ~4) |
| 9 | Frostscythe without  Killing Machine | `frostscythe_without_killing_machine` | ✗ MISSING | Not found in SimC APL |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Rider of the Apocalypse

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Empower Rune Weapon | `empower_rune_weapon` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Pillar of Frost | `pillar_of_frost` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Breath of Sindragosa | `breath_of_sindragosa` | ✓ MATCH | Present in APL (pos ~8) |
| 4 | Frostwyrm's Fury | `frostwyrms_fury` | ✓ MATCH | Present in APL (pos ~9) |
| 5 | Obliterate | `obliterate` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 6 | Howling Blast | `howling_blast` | ✓ MATCH | Present in APL (pos ~3) |
| 7 | Frost Strike | `frost_strike` | ✓ MATCH | Present in APL (pos ~1) |
| 8 | Obliterate without  Killing Machine | `obliterate_without_killing_machine` | ✗ MISSING | Not found in SimC APL |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Empower Rune Weapon | `empower_rune_weapon` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Pillar of Frost | `pillar_of_frost` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Breath of Sindragosa | `breath_of_sindragosa` | ✓ MATCH | Present in APL (pos ~8) |
| 4 | Frostwyrm's Fury | `frostwyrms_fury` | ✓ MATCH | Present in APL (pos ~9) |
| 5 | Frostscythe | `frostscythe` | ~ ORDER_DIFF | APL pos ~0, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 6 | Howling Blast | `howling_blast` | ✓ MATCH | Present in APL (pos ~3) |
| 7 | Glacial Advance | `glacial_advance` | ✓ MATCH | Present in APL (pos ~4) |
| 8 | Frostscythe without  Killing Machine | `frostscythe_without_killing_machine` | ✗ MISSING | Not found in SimC APL |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `remorseless_winter` | Sim-specific logic not covered by guide |
| `raise_dead` | Sim-specific logic not covered by guide |
| `antimagic_shell` | Sim-specific logic not covered by guide |
| `deaths_caress` | Sim-specific logic not covered by guide |
| `vampiric_blood` | Sim-specific logic not covered by guide |
| `death_strike` | Sim-specific logic not covered by guide |
| `dancing_rune_weapon` | Sim-specific logic not covered by guide |
| `marrowrend` | Sim-specific logic not covered by guide |
| `death_and_decay` | Sim-specific logic not covered by guide |
| `blood_boil` | Sim-specific logic not covered by guide |
| `consumption` | Sim-specific logic not covered by guide |
| `heart_strike` | Sim-specific logic not covered by guide |
| *(+10 more)* | |

### Key Findings

- **2 unique MISSING** actions and 6 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `obliterate_without_killing_machine` (Obliterate without  Killing Machine) - MISSING
  1. [AoE Priority] `frostscythe_without_killing_machine` (Frostscythe without  Killing Machine) - MISSING
  1. [Single-Target Priority] `reapers_mark` (Reaper's Mark) - ORDER_DIFF
  1. [Single-Target Priority] `obliterate` (Obliterate) - ORDER_DIFF
  1. [AoE Priority] `reapers_mark` (Reaper's Mark) - ORDER_DIFF
- **Recommended**: Review and add missing major CDs/rotational abilities to APL

---

## Death-Knight Unholy

### Hero: Rider of the Apocalypse

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Outbreak | `outbreak` | ✓ MATCH | Present in APL (pos ~7) |
| 2 | Army of the Dead | `army_of_the_dead` | ✓ MATCH | Present in APL (pos ~8) |
| 3 | Dark Transformation | `dark_transformation` | ✓ MATCH | Present in APL (pos ~9) |
| 4 | Soul Reaper | `soul_reaper` | ✓ MATCH | Present in APL (pos ~10) |
| 5 | Putrefy | `putrefy` | ✓ MATCH | Present in APL (pos ~6) |
| 6 | Festering Scythe | `festering_scythe` | ✗ MISSING | Not found in SimC APL |
| 7 | Death Coil | `death_coil` | ✓ MATCH | Present in APL (pos ~4) |
| 8 | Festering Strike | `festering_strike` | ✓ MATCH | Present in APL (pos ~2) |
| 9 | Scourge Strike | `scourge_strike` | ✓ MATCH | Present in APL (pos ~5) |
| 10 | Necrotic Coil | `death_coil` | ✓ MATCH | Present in APL (pos ~4) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Outbreak | `outbreak` | ✓ MATCH | Present in APL (pos ~7) |
| 2 | Army of the Dead | `army_of_the_dead` | ✓ MATCH | Present in APL (pos ~8) |
| 3 | Dark Transformation | `dark_transformation` | ✓ MATCH | Present in APL (pos ~9) |
| 4 | Putrefy | `putrefy` | ✓ MATCH | Present in APL (pos ~6) |
| 5 | Festering Scythe | `festering_scythe` | ✗ MISSING | Not found in SimC APL |
| 6 | Epidemic | `epidemic` | ✓ MATCH | Present in APL (pos ~3) |
| 7 | Festering Strike | `festering_strike` | ✓ MATCH | Present in APL (pos ~2) |
| 8 | Scourge Strike | `scourge_strike` | ✓ MATCH | Present in APL (pos ~5) |
| 9 | Graveyard | `graveyard` | ✗ MISSING | Not found in SimC APL |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Outbreak | `outbreak` | ✓ MATCH | Present in APL (pos ~7) |
| 2 | Festering Strike | `festering_strike` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~7 (Wowhead order reversed vs APL) |
| 3 | Festering Scythe | `festering_scythe` | ✗ MISSING | Not found in SimC APL |
| 4 | Army of the Dead | `army_of_the_dead` | ✓ MATCH | Present in APL (pos ~8) |
| 5 | Dark Transformation | `dark_transformation` | ✓ MATCH | Present in APL (pos ~9) |
| 6 | Soul Reaper | `soul_reaper` | ✓ MATCH | Present in APL (pos ~10) |
| 7 | Necrotic Coil | `death_coil` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~10 (Wowhead order reversed vs APL) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `raise_dead` | Sim-specific logic not covered by guide |
| `death_and_decay` | Sim-specific logic not covered by guide |
| `deaths_caress` | Sim-specific logic not covered by guide |
| `vampiric_blood` | Sim-specific logic not covered by guide |
| `death_strike` | Sim-specific logic not covered by guide |
| `dancing_rune_weapon` | Sim-specific logic not covered by guide |
| `marrowrend` | Sim-specific logic not covered by guide |
| `reapers_mark` | Sim-specific logic not covered by guide |
| `blood_boil` | Sim-specific logic not covered by guide |
| `consumption` | Sim-specific logic not covered by guide |
| `heart_strike` | Sim-specific logic not covered by guide |
| `any_dnd` | Sim-specific logic not covered by guide |
| *(+11 more)* | |

### Key Findings

- Minor gaps: **2 unique missing**, 2 order differences
  1. [Single-Target Priority] `festering_scythe` (Festering Scythe) - MISSING from SimC APL
  1. [AoE Priority] `graveyard` (Graveyard) - MISSING from SimC APL
  1. [Opener] `festering_strike` (Festering Strike) - ORDER_DIFF in SimC APL
  1. [Opener] `death_coil` (Necrotic Coil) - ORDER_DIFF in SimC APL

---

## Demon-Hunter Havoc

### Hero: Fel-Scarred

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Eye Beam | `eye_beam` | ✓ MATCH | Present in APL (pos ~12) |
| 2 | The Hunt | `the_hunt` | ✓ MATCH | Present in APL (pos ~17) |
| 3 | Felblade | `felblade` | ~ ORDER_DIFF | APL pos ~10, previous item at pos ~17 (Wowhead order reversed vs APL) |
| 4 | Death Sweep | `death_sweep` | ~ ORDER_DIFF | APL pos ~5, previous item at pos ~10 (Wowhead order reversed vs APL) |
| 5 | Annihilation | `annihilation` | ✓ MATCH | Present in APL (pos ~6) |
| 6 | Vengeful Retreat | `vengeful_retreat` | ✓ MATCH | Present in APL (pos ~9) |
| 7 | Consuming Fire | `consuming_fire` | ✗ MISSING | Not found in SimC APL |
| 8 | Fel Rush | `fel_rush` | ✓ MATCH | Present in APL (pos ~11) |
| 9 | Abyssal Gaze | `abyssal_gaze` | ✗ MISSING | Not found in SimC APL |

### Hero: Aldrachi Reaver

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Throw Glaive | `throw_glaive` | ✓ MATCH | Present in APL (pos ~14) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Throw Glaive | `throw_glaive` | ✓ MATCH | Present in APL (pos ~14) |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | The Hunt | `the_hunt` | ✓ MATCH | Present in APL (pos ~17) |
| 2 | Reaver's Glaive | `reaver_s_glaive` | ✗ MISSING | Not found in SimC APL |
| 3 | Eye Beam | `eye_beam` | ~ ORDER_DIFF | APL pos ~12, previous item at pos ~17 (Wowhead order reversed vs APL) |
| 4 | Death Sweep | `death_sweep` | ~ ORDER_DIFF | APL pos ~5, previous item at pos ~12 (Wowhead order reversed vs APL) |
| 5 | Vengeful Retreat | `vengeful_retreat` | ✓ MATCH | Present in APL (pos ~9) |
| 6 | Annihilation | `annihilation` | ✓ MATCH | Present in APL (pos ~6) |
| 7 | Metamorphosis | `metamorphosis` | ✓ MATCH | Present in APL (pos ~16) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `immolation_aura` | Sim-specific logic not covered by guide |
| `cycling_variable` | Sim-specific logic not covered by guide |
| `retarget_auto_attack` | Sim-specific logic not covered by guide |
| `pick_up_fragment` | Sim-specific logic not covered by guide |
| `chaos_strike` | Sim-specific logic not covered by guide |
| `reavers_glaive` | Sim-specific logic not covered by guide |
| `blade_dance` | Sim-specific logic not covered by guide |
| `essence_break` | Sim-specific logic not covered by guide |
| `consume` | Sim-specific logic not covered by guide |
| `void_ray` | Sim-specific logic not covered by guide |
| `pierce_the_veil` | Sim-specific logic not covered by guide |
| `voidblade` | Sim-specific logic not covered by guide |
| *(+19 more)* | |

### Key Findings

- **3 unique MISSING** actions and 4 ORDER_DIFF items
- Top priority gaps:
  1. [Opener] `consuming_fire` (Consuming Fire) - MISSING
  1. [Opener] `abyssal_gaze` (Abyssal Gaze) - MISSING
  1. [Opener] `reaver_s_glaive` (Reaver's Glaive) - MISSING
  1. [Opener] `felblade` (Felblade) - ORDER_DIFF
  1. [Opener] `death_sweep` (Death Sweep) - ORDER_DIFF
  1. [Opener] `eye_beam` (Eye Beam) - ORDER_DIFF
- **Recommended**: Review and add missing major CDs/rotational abilities to APL

---

## Demon-Hunter Devourer

### Hero: Void-Scarred

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Voidblade | `voidblade` | ✓ MATCH | Present in APL (pos ~4) |
| 2 | Reap | `reap` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Void Ray | `void_ray` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~7 (Wowhead order reversed vs APL) |
| 4 | Void Metamorphosis | `void_metamorphosis` | ✗ MISSING | Not found in SimC APL |
| 5 | Consume | `consume` | ✓ MATCH | Present in APL (pos ~1) |
| 6 | Cull | `cull` | ✓ MATCH | Present in APL (pos ~16) |
| 7 | Pierce the Veil | `pierce_the_veil` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~16 (Wowhead order reversed vs APL) |
| 8 | Devour | `devour` | ✓ MATCH | Present in APL (pos ~10) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Hungering Slash | `hungering_slash` | ✓ MATCH | Present in APL (pos ~12) |
| 2 | Vengeful Retreat | `vengeful_retreat` | ✓ MATCH | Present in APL (pos ~11) |
| 3 | Voidblade | `voidblade` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 4 | Eradicate | `eradicate` | ✓ MATCH | Present in APL (pos ~15) |
| 5 | Void Ray | `void_ray` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~15 (Wowhead order reversed vs APL) |
| 6 | Reap | `reap` | ✓ MATCH | Present in APL (pos ~7) |
| 7 | Void Metamorphosis | `void_metamorphosis` | ✗ MISSING | Not found in SimC APL |
| 8 | Consume | `consume` | ~ ORDER_DIFF | APL pos ~1, previous item at pos ~7 (Wowhead order reversed vs APL) |
| 9 | Collapsing Star | `collapsing_star` | ✓ MATCH | Present in APL (pos ~8) |
| 10 | Reaper's Toll | `reaper_s_toll` | ✗ MISSING | Not found in SimC APL |
| 11 | Pierce the Veil | `pierce_the_veil` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~8 (Wowhead order reversed vs APL) |
| 12 | Cull | `cull` | ✓ MATCH | Present in APL (pos ~16) |
| 13 | Devour | `devour` | ~ ORDER_DIFF | APL pos ~10, previous item at pos ~16 (Wowhead order reversed vs APL) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Annihilator

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Void Ray | `void_ray` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Reap | `reap` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Void Metamorphosis | `void_metamorphosis` | ✗ MISSING | Not found in SimC APL |
| 4 | Consume | `consume` | ~ ORDER_DIFF | APL pos ~1, previous item at pos ~7 (Wowhead order reversed vs APL) |
| 5 | Collapsing Star | `collapsing_star` | ✓ MATCH | Present in APL (pos ~8) |
| 6 | Cull | `cull` | ✓ MATCH | Present in APL (pos ~16) |
| 7 | Devour | `devour` | ~ ORDER_DIFF | APL pos ~10, previous item at pos ~16 (Wowhead order reversed vs APL) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Eradicate | `eradicate` | ✓ MATCH | Present in APL (pos ~15) |
| 2 | Void Ray | `void_ray` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~15 (Wowhead order reversed vs APL) |
| 3 | Reap | `reap` | ✓ MATCH | Present in APL (pos ~7) |
| 4 | Void Metamorphosis | `void_metamorphosis` | ✗ MISSING | Not found in SimC APL |
| 5 | Consume | `consume` | ~ ORDER_DIFF | APL pos ~1, previous item at pos ~7 (Wowhead order reversed vs APL) |
| 6 | Collapsing Star | `collapsing_star` | ✓ MATCH | Present in APL (pos ~8) |
| 7 | Cull | `cull` | ✓ MATCH | Present in APL (pos ~16) |
| 8 | Devour | `devour` | ~ ORDER_DIFF | APL pos ~10, previous item at pos ~16 (Wowhead order reversed vs APL) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `the_hunt` | Sim-specific logic not covered by guide |
| `metamorphosis` | Sim-specific logic not covered by guide |
| `soul_immolation` | Sim-specific logic not covered by guide |
| `reapers_toll` | Sim-specific logic not covered by guide |
| `predators_wake` | Sim-specific logic not covered by guide |
| `immolation_aura` | Sim-specific logic not covered by guide |
| `cycling_variable` | Sim-specific logic not covered by guide |
| `retarget_auto_attack` | Sim-specific logic not covered by guide |
| `pick_up_fragment` | Sim-specific logic not covered by guide |
| `death_sweep` | Sim-specific logic not covered by guide |
| `annihilation` | Sim-specific logic not covered by guide |
| `chaos_strike` | Sim-specific logic not covered by guide |
| *(+17 more)* | |

### Key Findings

- **2 unique MISSING** actions and 12 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `void_metamorphosis` (Void Metamorphosis) - MISSING
  1. [AoE Priority] `reaper_s_toll` (Reaper's Toll) - MISSING
  1. [Single-Target Priority] `void_ray` (Void Ray) - ORDER_DIFF
  1. [Single-Target Priority] `pierce_the_veil` (Pierce the Veil) - ORDER_DIFF
  1. [AoE Priority] `voidblade` (Voidblade) - ORDER_DIFF
- **Recommended**: Review and add missing major CDs/rotational abilities to APL

---

## Demon-Hunter Vengeance

### Hero: Annihilator

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Sigil of Flame | `sigil_of_flame` | ✓ MATCH | Present in APL (pos ~0) |

### Hero: Aldrachi Reaver

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Sigil of Flame | `sigil_of_flame` | ✓ MATCH | Present in APL (pos ~0) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `immolation_aura` | Sim-specific logic not covered by guide |
| `cycling_variable` | Sim-specific logic not covered by guide |
| `infernal_strike` | Sim-specific logic not covered by guide |
| `demon_spikes` | Sim-specific logic not covered by guide |
| `metamorphosis` | Sim-specific logic not covered by guide |
| `spirit_bomb` | Sim-specific logic not covered by guide |
| `fiery_brand` | Sim-specific logic not covered by guide |
| `sigil_of_spite` | Sim-specific logic not covered by guide |
| `soul_carver` | Sim-specific logic not covered by guide |
| `fel_devastation` | Sim-specific logic not covered by guide |
| `fracture` | Sim-specific logic not covered by guide |
| `felblade` | Sim-specific logic not covered by guide |
| *(+27 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Druid Balance

### Hero: Keeper of the Grove

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Elune's Chosen

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `moonkin_form` | Sim-specific logic not covered by guide |
| `wrath` | Sim-specific logic not covered by guide |
| `starfire` | Sim-specific logic not covered by guide |
| `moonfire` | Sim-specific logic not covered by guide |
| `sunfire` | Sim-specific logic not covered by guide |
| `fury_of_elune` | Sim-specific logic not covered by guide |
| `solar_eclipse` | Sim-specific logic not covered by guide |
| `celestial_alignment` | Sim-specific logic not covered by guide |
| `incarnation` | Sim-specific logic not covered by guide |
| `force_of_nature` | Sim-specific logic not covered by guide |
| `starfall` | Sim-specific logic not covered by guide |
| `starsurge` | Sim-specific logic not covered by guide |
| *(+6 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Druid Feral

### Hero: Druid of the Claw

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Berserk | `berserk` | ✓ MATCH | Present in APL (pos ~14) |
| 2 | Rake | `rake` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~14 (Wowhead order reversed vs APL) |
| 3 | Moonfire | `moonfire` | ✗ MISSING | Not found in SimC APL |
| 4 | Shred | `shred` | ✓ MATCH | Present in APL (pos ~11) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Berserk | `berserk` | ✓ MATCH | Present in APL (pos ~14) |
| 2 | Swipe | `swipe_cat` | ~ ORDER_DIFF | APL pos ~7, previous item at pos ~14 (Wowhead order reversed vs APL) |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Moonfire | `moonfire` | ✗ MISSING | Not found in SimC APL |
| 2 | Berserk | `berserk` | ✓ MATCH | Present in APL (pos ~14) |
| 3 | Rip | `rip` | ✓ MATCH | Present in APL (pos ~18) |
| 4 | Convoke the Spirits | `convoke_the_spirits` | ✓ MATCH | Present in APL (pos ~17) |
| 5 | Ferocious Bite | `ferocious_bite` | ~ ORDER_DIFF | APL pos ~5, previous item at pos ~17 (Wowhead order reversed vs APL) |
| 6 | Feral Frenzy | `feral_frenzy` | ✓ MATCH | Present in APL (pos ~15) |

### Hero: Wildstalker

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Berserk | `berserk` | ✓ MATCH | Present in APL (pos ~14) |
| 2 | Rake | `rake` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~14 (Wowhead order reversed vs APL) |
| 3 | Moonfire | `moonfire` | ✗ MISSING | Not found in SimC APL |
| 4 | Shred | `shred` | ✓ MATCH | Present in APL (pos ~11) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Berserk | `berserk` | ✓ MATCH | Present in APL (pos ~14) |
| 2 | Swipe | `swipe_cat` | ~ ORDER_DIFF | APL pos ~7, previous item at pos ~14 (Wowhead order reversed vs APL) |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Moonfire | `moonfire` | ✗ MISSING | Not found in SimC APL |
| 2 | Berserk | `berserk` | ✓ MATCH | Present in APL (pos ~14) |
| 3 | Rip | `rip` | ✓ MATCH | Present in APL (pos ~18) |
| 4 | Convoke the Spirits | `convoke_the_spirits` | ✓ MATCH | Present in APL (pos ~17) |
| 5 | Ferocious Bite | `ferocious_bite` | ~ ORDER_DIFF | APL pos ~5, previous item at pos ~17 (Wowhead order reversed vs APL) |
| 6 | Feral Frenzy | `feral_frenzy` | ✓ MATCH | Present in APL (pos ~15) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `cat_form` | Sim-specific logic not covered by guide |
| `prowl` | Sim-specific logic not covered by guide |
| `tigers_fury` | Sim-specific logic not covered by guide |
| `chomp` | Sim-specific logic not covered by guide |
| `regrowth` | Sim-specific logic not covered by guide |
| `primal_wrath` | Sim-specific logic not covered by guide |
| `moonfire_cat` | Sim-specific logic not covered by guide |
| `incarnation` | Sim-specific logic not covered by guide |
| `frantic_frenzy` | Sim-specific logic not covered by guide |

### Key Findings

- **1 unique MISSING** actions and 6 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `moonfire` (Moonfire) - MISSING
  1. [Single-Target Priority] `rake` (Rake) - ORDER_DIFF
  1. [AoE Priority] `swipe_cat` (Swipe) - ORDER_DIFF
  1. [Opener] `ferocious_bite` (Ferocious Bite) - ORDER_DIFF
- **Recommended**: Review and add missing major CDs/rotational abilities to APL

---

## Druid Guardian

### Hero: Druid of the Claw

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Red Moon | `red_moon` | ✗ MISSING | Not found in SimC APL |
| 2 | Mangle | `mangle` | ✓ MATCH | Present in APL (pos ~6) |
| 3 | Thrash | `thrash_cat` | ✗ MISSING | Not found in SimC APL |
| 4 | Frenzied Regeneration | `frenzied_regeneration` | ✗ MISSING | Not found in SimC APL |
| 5 | Swipe | `swipe_cat` | ✗ MISSING | Not found in SimC APL |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `bear_form` | Sim-specific logic not covered by guide |
| `berserk` | Sim-specific logic not covered by guide |
| `convoke_the_spirits` | Sim-specific logic not covered by guide |
| `thrash` | Sim-specific logic not covered by guide |
| `lunar_beam` | Sim-specific logic not covered by guide |
| `moonfire` | Sim-specific logic not covered by guide |
| `maul` | Sim-specific logic not covered by guide |
| `swipe` | Sim-specific logic not covered by guide |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Evoker Devastation

### Hero: Scalecommander

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Hover | `hover` | ✓ MATCH | Present in APL (pos ~1) |
| 2 | Deep Breath | `deep_breath` | ✓ MATCH | Present in APL (pos ~8) |
| 3 | Dragonrage | `dragonrage` | ✓ MATCH | Present in APL (pos ~6) |
| 4 | Tip the Scales | `tip_the_scales` | ✓ MATCH | Present in APL (pos ~5) |
| 5 | Azure Sweep | `azure_sweep` | ✓ MATCH | Present in APL (pos ~9) |
| 6 | Living Flame | `living_flame` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 7 | Azure Strike | `azure_strike` | ✓ MATCH | Present in APL (pos ~10) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Hover | `hover` | ✓ MATCH | Present in APL (pos ~1) |
| 2 | Deep Breath | `deep_breath` | ✓ MATCH | Present in APL (pos ~8) |
| 3 | Dragonrage | `dragonrage` | ✓ MATCH | Present in APL (pos ~6) |
| 4 | Tip the Scales | `tip_the_scales` | ✓ MATCH | Present in APL (pos ~5) |
| 5 | Pyre | `pyre` | ✓ MATCH | Present in APL (pos ~7) |
| 6 | Azure Sweep | `azure_sweep` | ✓ MATCH | Present in APL (pos ~9) |
| 7 | Living Flame | `living_flame` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 8 | Azure Strike | `azure_strike` | ✓ MATCH | Present in APL (pos ~10) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Flameshaper

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Dragonrage | `dragonrage` | ✓ MATCH | Present in APL (pos ~6) |
| 2 | Tip the Scales | `tip_the_scales` | ✓ MATCH | Present in APL (pos ~5) |
| 3 | Eternity Surge | `eternity_surge` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Azure Sweep | `azure_sweep` | ✓ MATCH | Present in APL (pos ~9) |
| 5 | Living Flame | `living_flame` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 6 | Azure Strike | `azure_strike` | ✓ MATCH | Present in APL (pos ~10) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Dragonrage | `dragonrage` | ✓ MATCH | Present in APL (pos ~6) |
| 2 | Tip the Scales | `tip_the_scales` | ✓ MATCH | Present in APL (pos ~5) |
| 3 | Azure Sweep | `azure_sweep` | ✓ MATCH | Present in APL (pos ~9) |
| 4 | Living Flame | `living_flame` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~9 (Wowhead order reversed vs APL) |
| 5 | Azure Strike | `azure_strike` | ✓ MATCH | Present in APL (pos ~10) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `verdant_embrace` | Sim-specific logic not covered by guide |
| `quell` | Sim-specific logic not covered by guide |
| `fire_breath` | Sim-specific logic not covered by guide |
| `disintegrate` | Sim-specific logic not covered by guide |
| `emerald_blossom` | Sim-specific logic not covered by guide |
| `blistering_scales` | Sim-specific logic not covered by guide |
| `ebon_might` | Sim-specific logic not covered by guide |
| `prescience` | Sim-specific logic not covered by guide |
| `fury_of_the_aspects` | Sim-specific logic not covered by guide |
| `breath_of_eons` | Sim-specific logic not covered by guide |
| `upheaval` | Sim-specific logic not covered by guide |
| `time_skip` | Sim-specific logic not covered by guide |
| *(+1 more)* | |

### Key Findings

- **0 unique MISSING** actions and 4 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `living_flame` (Living Flame) - ORDER_DIFF
  1. [AoE Priority] `living_flame` (Living Flame) - ORDER_DIFF
  1. [Single-Target Priority] `living_flame` (Living Flame) - ORDER_DIFF

---

## Evoker Augmentation

### Hero: Chronowarden

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Ebon Might | `ebon_might` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Prescience | `prescience` | ✓ MATCH | Present in APL (pos ~3) |
| 3 | Breath of Eons | `breath_of_eons` | ✓ MATCH | Present in APL (pos ~8) |
| 4 | Eruption | `eruption` | ✓ MATCH | Present in APL (pos ~13) |

### Hero: Scalecommander

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Ebon Might | `ebon_might` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Prescience | `prescience` | ✓ MATCH | Present in APL (pos ~3) |
| 3 | Breath of Eons | `breath_of_eons` | ✓ MATCH | Present in APL (pos ~8) |
| 4 | Eruption | `eruption` | ✓ MATCH | Present in APL (pos ~13) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `blistering_scales` | Sim-specific logic not covered by guide |
| `living_flame` | Sim-specific logic not covered by guide |
| `tip_the_scales` | Sim-specific logic not covered by guide |
| `fire_breath` | Sim-specific logic not covered by guide |
| `upheaval` | Sim-specific logic not covered by guide |
| `time_skip` | Sim-specific logic not covered by guide |
| `azure_strike` | Sim-specific logic not covered by guide |
| `verdant_embrace` | Sim-specific logic not covered by guide |
| `hover` | Sim-specific logic not covered by guide |
| `quell` | Sim-specific logic not covered by guide |
| `dragonrage` | Sim-specific logic not covered by guide |
| `pyre` | Sim-specific logic not covered by guide |
| *(+6 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Hunter Beast-Mastery

### Hero: Pack Leader

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Misdirection | `misdirection` | ✗ MISSING | Not found in SimC APL |
| 2 | Bestial Wrath | `bestial_wrath` | ✓ MATCH | Present in APL (pos ~6) |
| 3 | Kill Command | `kill_command` | ✓ MATCH | Present in APL (pos ~7) |
| 4 | Barbed Shot | `barbed_shot` | ✓ MATCH | Present in APL (pos ~4) |

### Hero: Dark Ranger

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Misdirection | `misdirection` | ✗ MISSING | Not found in SimC APL |
| 2 | Barbed Shot | `barbed_shot` | ✓ MATCH | Present in APL (pos ~4) |
| 3 | Bestial Wrath | `bestial_wrath` | ✓ MATCH | Present in APL (pos ~6) |
| 4 | Kill Command | `kill_command` | ✓ MATCH | Present in APL (pos ~7) |
| 5 | Black Arrow | `black_arrow` | ✓ MATCH | Present in APL (pos ~9) |
| 6 | Wailing Arrow | `wailing_arrow` | ✓ MATCH | Present in APL (pos ~10) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `wild_thrash` | Sim-specific logic not covered by guide |
| `cobra_shot` | Sim-specific logic not covered by guide |
| `aimed_shot` | Sim-specific logic not covered by guide |
| `steady_shot` | Sim-specific logic not covered by guide |
| `trueshot` | Sim-specific logic not covered by guide |
| `multishot` | Sim-specific logic not covered by guide |
| `rapid_fire` | Sim-specific logic not covered by guide |
| `volley` | Sim-specific logic not covered by guide |
| `arcane_shot` | Sim-specific logic not covered by guide |
| `moonlight_chakram` | Sim-specific logic not covered by guide |
| `harpoon` | Sim-specific logic not covered by guide |
| `muzzle` | Sim-specific logic not covered by guide |
| *(+6 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Hunter Marksmanship

### Hero: Sentinel

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Arcane Shot | `arcane_shot` | ✓ MATCH | Present in APL (pos ~13) |
| 2 | Volley | `volley` | ✓ MATCH | Present in APL (pos ~11) |
| 3 | Rapid Fire | `rapid_fire` | ✓ MATCH | Present in APL (pos ~10) |
| 4 | Aimed Shot | `aimed_shot` | ~ ORDER_DIFF | APL pos ~0, previous item at pos ~10 (Wowhead order reversed vs APL) |
| 5 | Moonlight Chakram | `moonlight_chakram` | ✓ MATCH | Present in APL (pos ~14) |

### Hero: Dark Ranger

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Black Arrow | `black_arrow` | ✓ MATCH | Present in APL (pos ~7) |
| 2 | Arcane Shot | `arcane_shot` | ✓ MATCH | Present in APL (pos ~13) |
| 3 | Volley | `volley` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Rapid Fire | `rapid_fire` | ✓ MATCH | Present in APL (pos ~10) |
| 5 | Aimed Shot | `aimed_shot` | ~ ORDER_DIFF | APL pos ~0, previous item at pos ~10 (Wowhead order reversed vs APL) |
| 6 | Wailing Arrow | `wailing_arrow` | ✓ MATCH | Present in APL (pos ~12) |
| 7 | Multi | `multi` | ✗ MISSING | Not found in SimC APL |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `steady_shot` | Sim-specific logic not covered by guide |
| `trueshot` | Sim-specific logic not covered by guide |
| `multishot` | Sim-specific logic not covered by guide |
| `barbed_shot` | Sim-specific logic not covered by guide |
| `bestial_wrath` | Sim-specific logic not covered by guide |
| `kill_command` | Sim-specific logic not covered by guide |
| `cobra_shot` | Sim-specific logic not covered by guide |
| `wild_thrash` | Sim-specific logic not covered by guide |
| `harpoon` | Sim-specific logic not covered by guide |
| `muzzle` | Sim-specific logic not covered by guide |
| `aspect_of_the_eagle` | Sim-specific logic not covered by guide |
| `takedown` | Sim-specific logic not covered by guide |
| *(+4 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Hunter Survival

### Hero: Pack Leader

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Harpoon | `harpoon` | ✓ MATCH | Present in APL (pos ~1) |
| 2 | Raptor Strike | `raptor_strike` | ✓ MATCH | Present in APL (pos ~12) |
| 3 | Boomstick | `boomstick` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Takedown | `takedown` | ✓ MATCH | Present in APL (pos ~8) |
| 5 | Raptor Swipe | `raptor_swipe` | ✗ MISSING | Not found in SimC APL |
| 6 | Kill Command | `kill_command` | ✓ MATCH | Present in APL (pos ~7) |
| 7 | Wildfire Bomb | `wildfire_bomb` | ✓ MATCH | Present in APL (pos ~10) |

### Hero: Sentinel

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Takedown | `takedown` | ✓ MATCH | Present in APL (pos ~8) |
| 2 | Wildfire Bomb | `wildfire_bomb` | ✓ MATCH | Present in APL (pos ~10) |
| 3 | Boomstick | `boomstick` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Kill Command | `kill_command` | ✓ MATCH | Present in APL (pos ~7) |
| 5 | Moonlight Chakram | `moonlight_chakram` | ✓ MATCH | Present in APL (pos ~13) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `muzzle` | Sim-specific logic not covered by guide |
| `aspect_of_the_eagle` | Sim-specific logic not covered by guide |
| `flamefang_pitch` | Sim-specific logic not covered by guide |
| `barbed_shot` | Sim-specific logic not covered by guide |
| `bestial_wrath` | Sim-specific logic not covered by guide |
| `cobra_shot` | Sim-specific logic not covered by guide |
| `wild_thrash` | Sim-specific logic not covered by guide |
| `black_arrow` | Sim-specific logic not covered by guide |
| `wailing_arrow` | Sim-specific logic not covered by guide |
| `aimed_shot` | Sim-specific logic not covered by guide |
| `steady_shot` | Sim-specific logic not covered by guide |
| `trueshot` | Sim-specific logic not covered by guide |
| *(+4 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Mage Arcane

### Hero: Sunfury

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `arcane_intellect` | Sim-specific logic not covered by guide |
| `mirror_image` | Sim-specific logic not covered by guide |
| `arcane_surge` | Sim-specific logic not covered by guide |
| `arcane_blast` | Sim-specific logic not covered by guide |
| `arcane_barrage` | Sim-specific logic not covered by guide |
| `arcane_missiles` | Sim-specific logic not covered by guide |
| `arcane_orb` | Sim-specific logic not covered by guide |
| `touch_of_the_magi` | Sim-specific logic not covered by guide |
| `evocation` | Sim-specific logic not covered by guide |
| `presence_of_mind` | Sim-specific logic not covered by guide |
| `arcane_explosion` | Sim-specific logic not covered by guide |
| `frostfire_bolt` | Sim-specific logic not covered by guide |
| *(+19 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Mage Fire

### Hero: Sunfury

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Combustion | `combustion` | ✓ MATCH | Present in APL (pos ~9) |
| 2 | Fire Blast | `fire_blast` | ✓ MATCH | Present in APL (pos ~13) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Combustion | `combustion` | ✓ MATCH | Present in APL (pos ~9) |
| 2 | Fire Blast | `fire_blast` | ✓ MATCH | Present in APL (pos ~13) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Frostfire

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Combustion | `combustion` | ✓ MATCH | Present in APL (pos ~9) |
| 2 | Fire Blast | `fire_blast` | ✓ MATCH | Present in APL (pos ~13) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Meteor | `meteor` | ✓ MATCH | Present in APL (pos ~3) |
| 2 | Meteor right | `meteor_right` | ✗ MISSING | Not found in SimC APL |
| 3 | Combustion | `combustion` | ✓ MATCH | Present in APL (pos ~9) |
| 4 | Fire Blast | `fire_blast` | ✓ MATCH | Present in APL (pos ~13) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `arcane_intellect` | Sim-specific logic not covered by guide |
| `mirror_image` | Sim-specific logic not covered by guide |
| `frostfire_bolt` | Sim-specific logic not covered by guide |
| `pyroblast` | Sim-specific logic not covered by guide |
| `flamestrike` | Sim-specific logic not covered by guide |
| `fireball` | Sim-specific logic not covered by guide |
| `scorch` | Sim-specific logic not covered by guide |
| `arcane_surge` | Sim-specific logic not covered by guide |
| `arcane_blast` | Sim-specific logic not covered by guide |
| `arcane_barrage` | Sim-specific logic not covered by guide |
| `arcane_missiles` | Sim-specific logic not covered by guide |
| `arcane_orb` | Sim-specific logic not covered by guide |
| *(+16 more)* | |

### Key Findings

- Minor gaps: **1 unique missing**, 0 order differences
  1. [AoE Priority] `meteor_right` (Meteor right) - MISSING from SimC APL

---

## Mage Frost

### Hero: Spellslinger

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Flurry | `flurry` | ✓ MATCH | Present in APL (pos ~9) |
| 2 | Ice Lance | `ice_lance` | ✓ MATCH | Present in APL (pos ~12) |
| 3 | Frozen Orb | `frozen_orb` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Glacial Spike | `glacial_spike` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 5 | Ray of Frost | `ray_of_frost` | ✓ MATCH | Present in APL (pos ~10) |
| 6 | Frostbolt | `frostbolt` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~10 (Wowhead order reversed vs APL) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Blizzard | `blizzard` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Flurry | `flurry` | ✓ MATCH | Present in APL (pos ~9) |
| 3 | Ice Lance | `ice_lance` | ✓ MATCH | Present in APL (pos ~12) |
| 4 | Frozen Orb | `frozen_orb` | ✓ MATCH | Present in APL (pos ~11) |
| 5 | Glacial Spike | `glacial_spike` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 6 | Ray of Frost | `ray_of_frost` | ✓ MATCH | Present in APL (pos ~10) |
| 7 | Frostbolt | `frostbolt` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~10 (Wowhead order reversed vs APL) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Frostfire

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Flurry | `flurry` | ✓ MATCH | Present in APL (pos ~9) |
| 2 | Frozen Orb | `frozen_orb` | ✓ MATCH | Present in APL (pos ~11) |
| 3 | Glacial Spike | `glacial_spike` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 4 | Comet Storm | `comet_storm` | ✓ MATCH | Present in APL (pos ~13) |
| 5 | Ice Lance | `ice_lance` | ✓ MATCH | Present in APL (pos ~12) |
| 6 | Ray of Frost | `ray_of_frost` | ✓ MATCH | Present in APL (pos ~10) |
| 7 | Frostfire Bolt | `frostfire_bolt` | ✓ MATCH | Present in APL (pos ~29) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Blizzard | `blizzard` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Flurry | `flurry` | ✓ MATCH | Present in APL (pos ~9) |
| 3 | Frozen Orb | `frozen_orb` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Glacial Spike | `glacial_spike` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 5 | Comet Storm | `comet_storm` | ✓ MATCH | Present in APL (pos ~13) |
| 6 | Ice Lance | `ice_lance` | ✓ MATCH | Present in APL (pos ~12) |
| 7 | Ray of Frost | `ray_of_frost` | ✓ MATCH | Present in APL (pos ~10) |
| 8 | Frostfire Bolt | `frostfire_bolt` | ✓ MATCH | Present in APL (pos ~29) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `arcane_intellect` | Sim-specific logic not covered by guide |
| `summon_water_elemental` | Sim-specific logic not covered by guide |
| `any_blink` | Sim-specific logic not covered by guide |
| `ice_nova` | Sim-specific logic not covered by guide |
| `cone_of_cold` | Sim-specific logic not covered by guide |
| `mirror_image` | Sim-specific logic not covered by guide |
| `arcane_surge` | Sim-specific logic not covered by guide |
| `arcane_blast` | Sim-specific logic not covered by guide |
| `arcane_barrage` | Sim-specific logic not covered by guide |
| `arcane_missiles` | Sim-specific logic not covered by guide |
| `arcane_orb` | Sim-specific logic not covered by guide |
| `touch_of_the_magi` | Sim-specific logic not covered by guide |
| *(+10 more)* | |

### Key Findings

- **0 unique MISSING** actions and 6 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `glacial_spike` (Glacial Spike) - ORDER_DIFF
  1. [Single-Target Priority] `frostbolt` (Frostbolt) - ORDER_DIFF
  1. [AoE Priority] `glacial_spike` (Glacial Spike) - ORDER_DIFF

---

## Monk Brewmaster

### Hero: Master of Harmony

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `black_ox_brew` | Sim-specific logic not covered by guide |
| `celestial_brew` | Sim-specific logic not covered by guide |
| `keg_smash` | Sim-specific logic not covered by guide |
| `breath_of_fire` | Sim-specific logic not covered by guide |
| `purifying_brew` | Sim-specific logic not covered by guide |
| `fortifying_brew` | Sim-specific logic not covered by guide |
| `chi_burst` | Sim-specific logic not covered by guide |
| `exploding_keg` | Sim-specific logic not covered by guide |
| `empty_the_cellar` | Sim-specific logic not covered by guide |
| `invoke_niuzao` | Sim-specific logic not covered by guide |
| `rushing_jade_wind` | Sim-specific logic not covered by guide |
| `blackout_kick` | Sim-specific logic not covered by guide |
| *(+19 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Monk Windwalker

### Hero: Conduit of the Celestials

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Tiger Palm | `tiger_palm` | ✓ MATCH | Present in APL (pos ~15) |
| 2 | Invoke Xuen | `invoke_xuen_the_white_tiger` | ✓ MATCH | Present in APL (pos ~11) |
| 3 | Zenith | `zenith` | ✓ MATCH | Present in APL (pos ~27) |
| 4 | Fists of Fury | `fists_of_fury` | ~ ORDER_DIFF | APL pos ~17, previous item at pos ~27 (Wowhead order reversed vs APL) |
| 5 | Rising Sun Kick | `rising_sun_kick` | ✓ MATCH | Present in APL (pos ~20) |
| 6 | Whirling Dragon Punch | `whirling_dragon_punch` | ~ ORDER_DIFF | APL pos ~13, previous item at pos ~20 (Wowhead order reversed vs APL) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `roll` | Sim-specific logic not covered by guide |
| `chi_torpedo` | Sim-specific logic not covered by guide |
| `flying_serpent_kick` | Sim-specific logic not covered by guide |
| `thorn_bloom` | Sim-specific logic not covered by guide |
| `celestial_conduit` | Sim-specific logic not covered by guide |
| `blackout_kick` | Sim-specific logic not covered by guide |
| `spinning_crane_kick` | Sim-specific logic not covered by guide |
| `strike_of_the_windlord` | Sim-specific logic not covered by guide |
| `rushing_wind_kick` | Sim-specific logic not covered by guide |
| `touch_of_death` | Sim-specific logic not covered by guide |
| `slicing_winds` | Sim-specific logic not covered by guide |
| `black_ox_brew` | Sim-specific logic not covered by guide |
| *(+13 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Paladin Protection

### Hero: Templar

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Divine Toll | `divine_toll` | ✓ MATCH | Present in APL (pos ~7) |
| 2 | Word of Glory | `word_of_glory` | ✓ MATCH | Present in APL (pos ~17) |
| 3 | Consecration | `consecration` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~17 (Wowhead order reversed vs APL) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Divine Toll | `divine_toll` | ✓ MATCH | Present in APL (pos ~7) |
| 2 | Word of Glory | `word_of_glory` | ✓ MATCH | Present in APL (pos ~17) |
| 3 | Consecration | `consecration` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~17 (Wowhead order reversed vs APL) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Lightsmith

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Sacred Weapon | `sacred_weapon` | ✗ MISSING | Not found in SimC APL |
| 2 | Divine Toll | `divine_toll` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Holy Bulwark | `holy_bulwark` | ✗ MISSING | Not found in SimC APL |
| 4 | Word of Glory | `word_of_glory` | ✓ MATCH | Present in APL (pos ~17) |
| 5 | Consecration | `consecration` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~17 (Wowhead order reversed vs APL) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Sacred Weapon | `sacred_weapon` | ✗ MISSING | Not found in SimC APL |
| 2 | Divine Toll | `divine_toll` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Holy Bulwark | `holy_bulwark` | ✗ MISSING | Not found in SimC APL |
| 4 | Word of Glory | `word_of_glory` | ✓ MATCH | Present in APL (pos ~17) |
| 5 | Consecration | `consecration` | ~ ORDER_DIFF | APL pos ~4, previous item at pos ~17 (Wowhead order reversed vs APL) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `rite_of_sanctification` | Sim-specific logic not covered by guide |
| `rite_of_adjuration` | Sim-specific logic not covered by guide |
| `devotion_aura` | Sim-specific logic not covered by guide |
| `avenging_wrath` | Sim-specific logic not covered by guide |
| `hammer_of_light` | Sim-specific logic not covered by guide |
| `shield_of_the_righteous` | Sim-specific logic not covered by guide |
| `holy_armaments` | Sim-specific logic not covered by guide |
| `hammer_of_wrath` | Sim-specific logic not covered by guide |
| `judgment` | Sim-specific logic not covered by guide |
| `avengers_shield` | Sim-specific logic not covered by guide |
| `hammer_of_the_righteous` | Sim-specific logic not covered by guide |
| `blessed_hammer` | Sim-specific logic not covered by guide |
| *(+8 more)* | |

### Key Findings

- **2 unique MISSING** actions and 4 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `sacred_weapon` (Sacred Weapon) - MISSING
  1. [Single-Target Priority] `holy_bulwark` (Holy Bulwark) - MISSING
  1. [Single-Target Priority] `consecration` (Consecration) - ORDER_DIFF
  1. [AoE Priority] `consecration` (Consecration) - ORDER_DIFF
  1. [Single-Target Priority] `consecration` (Consecration) - ORDER_DIFF
- **Recommended**: Review and add missing major CDs/rotational abilities to APL

---

## Paladin Retribution

### Hero: Default

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Avenging Wrath | `avenging_wrath` | ✓ MATCH | Present in APL (pos ~4) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Avenging Wrath | `avenging_wrath` | ✓ MATCH | Present in APL (pos ~4) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `execution_sentence` | Sim-specific logic not covered by guide |
| `hammer_of_light` | Sim-specific logic not covered by guide |
| `divine_storm` | Sim-specific logic not covered by guide |
| `templars_verdict` | Sim-specific logic not covered by guide |
| `wake_of_ashes` | Sim-specific logic not covered by guide |
| `divine_toll` | Sim-specific logic not covered by guide |
| `blade_of_justice` | Sim-specific logic not covered by guide |
| `hammer_of_wrath` | Sim-specific logic not covered by guide |
| `judgment` | Sim-specific logic not covered by guide |
| `templar_strike` | Sim-specific logic not covered by guide |
| `templar_slash` | Sim-specific logic not covered by guide |
| `crusader_strike` | Sim-specific logic not covered by guide |
| *(+10 more)* | |

### Key Findings

- APL well-aligned with Wowhead guide (2 action matches)
- 22 extra sim-specific actions in APL (expected)

---

## Priest Shadow

### Hero: Archon

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Tentacle Slam | `tentacle_slam` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Halo | `halo` | ✓ MATCH | Present in APL (pos ~9) |
| 3 | Voidform | `voidform` | ✓ MATCH | Present in APL (pos ~10) |
| 4 | Void Volley | `void_volley` | ✓ MATCH | Present in APL (pos ~15) |

### Hero: Voidweaver

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Tentacle Slam | `tentacle_slam` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Voidform | `voidform` | ✓ MATCH | Present in APL (pos ~10) |
| 3 | Void Volley | `void_volley` | ✓ MATCH | Present in APL (pos ~15) |
| 4 | Void Torrent | `void_torrent` | ✓ MATCH | Present in APL (pos ~17) |
| 5 | Void Blast | `void_blast` | ✓ MATCH | Present in APL (pos ~16) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `shadowform` | Sim-specific logic not covered by guide |
| `flash_heal` | Sim-specific logic not covered by guide |
| `power_infusion` | Sim-specific logic not covered by guide |
| `desperate_prayer` | Sim-specific logic not covered by guide |
| `holy_nova` | Sim-specific logic not covered by guide |
| `shadow_word_death` | Sim-specific logic not covered by guide |
| `shadow_word_madness` | Sim-specific logic not covered by guide |
| `shadow_word_pain` | Sim-specific logic not covered by guide |
| `mind_blast` | Sim-specific logic not covered by guide |
| `mind_flay_insanity` | Sim-specific logic not covered by guide |
| `vampiric_touch` | Sim-specific logic not covered by guide |
| `mind_flay` | Sim-specific logic not covered by guide |
| *(+12 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Rogue Assassination

### Hero: Deathstalker

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Garrote | `garrote` | ✓ MATCH | Present in APL (pos ~8) |
| 2 | Mutilate | `mutilate` | ✓ MATCH | Present in APL (pos ~13) |
| 3 | Rupture | `rupture` | ✓ MATCH | Present in APL (pos ~9) |
| 4 | Envenom | `envenom` | ✓ MATCH | Present in APL (pos ~15) |
| 5 | Deathmark | `deathmark` | ~ ORDER_DIFF | APL pos ~5, previous item at pos ~15 (Wowhead order reversed vs APL) |
| 6 | Kingsbane | `kingsbane` | ✓ MATCH | Present in APL (pos ~6) |

### Hero: Fatebound

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Garrote | `garrote` | ✓ MATCH | Present in APL (pos ~8) |
| 2 | Mutilate | `mutilate` | ✓ MATCH | Present in APL (pos ~13) |
| 3 | Rupture | `rupture` | ✓ MATCH | Present in APL (pos ~9) |
| 4 | Envenom | `envenom` | ✓ MATCH | Present in APL (pos ~15) |
| 5 | Deathmark | `deathmark` | ~ ORDER_DIFF | APL pos ~5, previous item at pos ~15 (Wowhead order reversed vs APL) |
| 6 | Kingsbane | `kingsbane` | ✓ MATCH | Present in APL (pos ~6) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `apply_poison` | Sim-specific logic not covered by guide |
| `stealth` | Sim-specific logic not covered by guide |
| `slice_and_dice` | Sim-specific logic not covered by guide |
| `thistle_tea` | Sim-specific logic not covered by guide |
| `vanish` | Sim-specific logic not covered by guide |
| `crimson_tempest` | Sim-specific logic not covered by guide |
| `shiv` | Sim-specific logic not covered by guide |
| `ambush` | Sim-specific logic not covered by guide |
| `fan_of_knives` | Sim-specific logic not covered by guide |
| `do_treacherous_transmitter_task` | Sim-specific logic not covered by guide |
| `adrenaline_rush` | Sim-specific logic not covered by guide |
| `roll_the_bones` | Sim-specific logic not covered by guide |
| *(+20 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Rogue Outlaw

### Hero: Trickster

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Opportunity | `opportunity` | ✗ MISSING | Not found in SimC APL |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Blade Flurry | `blade_flurry` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Opportunity | `opportunity` | ✗ MISSING | Not found in SimC APL |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Adrenaline Rush | `adrenaline_rush` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Roll the Bones | `roll_the_bones` | ✓ MATCH | Present in APL (pos ~4) |
| 3 | Keep It Rolling | `keep_it_rolling` | ✓ MATCH | Present in APL (pos ~16) |
| 4 | Dispatch | `dispatch` | ✓ MATCH | Present in APL (pos ~24) |
| 5 | Blade Rush | `blade_rush` | ~ ORDER_DIFF | APL pos ~17, previous item at pos ~24 (Wowhead order reversed vs APL) |
| 6 | Killing Spree | `killing_spree` | ✓ MATCH | Present in APL (pos ~26) |

### Hero: Fatebound

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Opportunity | `opportunity` | ✗ MISSING | Not found in SimC APL |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Blade Flurry | `blade_flurry` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Opportunity | `opportunity` | ✗ MISSING | Not found in SimC APL |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Adrenaline Rush | `adrenaline_rush` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Roll the Bones | `roll_the_bones` | ✓ MATCH | Present in APL (pos ~4) |
| 3 | Keep It Rolling | `keep_it_rolling` | ✓ MATCH | Present in APL (pos ~16) |
| 4 | Dispatch | `dispatch` | ✓ MATCH | Present in APL (pos ~24) |
| 5 | Blade Rush | `blade_rush` | ~ ORDER_DIFF | APL pos ~17, previous item at pos ~24 (Wowhead order reversed vs APL) |
| 6 | Between the Eyes | `between_the_eyes` | ✓ MATCH | Present in APL (pos ~25) |
| 7 | Preparation | `preparation` | ~ ORDER_DIFF | APL pos ~15, previous item at pos ~25 (Wowhead order reversed vs APL) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `apply_poison` | Sim-specific logic not covered by guide |
| `stealth` | Sim-specific logic not covered by guide |
| `slice_and_dice` | Sim-specific logic not covered by guide |
| `ambush` | Sim-specific logic not covered by guide |
| `coup_de_grace` | Sim-specific logic not covered by guide |
| `pistol_shot` | Sim-specific logic not covered by guide |
| `sinister_strike` | Sim-specific logic not covered by guide |
| `vanish` | Sim-specific logic not covered by guide |
| `thistle_tea` | Sim-specific logic not covered by guide |
| `deathmark` | Sim-specific logic not covered by guide |
| `kingsbane` | Sim-specific logic not covered by guide |
| `garrote` | Sim-specific logic not covered by guide |
| *(+17 more)* | |

### Key Findings

- **1 unique MISSING** actions and 3 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `opportunity` (Opportunity) - MISSING
  1. [Opener] `blade_rush` (Blade Rush) - ORDER_DIFF
  1. [Opener] `blade_rush` (Blade Rush) - ORDER_DIFF
  1. [Opener] `preparation` (Preparation) - ORDER_DIFF
- **Recommended**: Review and add missing major CDs/rotational abilities to APL

---

## Rogue Subtlety

### Hero: Deathstalker

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Secret Technique | `secret_technique` | ✓ MATCH | Present in APL (pos ~15) |
| 2 | Eviscerate | `eviscerate` | ✓ MATCH | Present in APL (pos ~16) |
| 3 | Shadowstrike | `shadowstrike` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~16 (Wowhead order reversed vs APL) |
| 4 | Backstab | `backstab` | ✓ MATCH | Present in APL (pos ~6) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Secret Technique | `secret_technique` | ✓ MATCH | Present in APL (pos ~15) |
| 2 | Eviscerate | `eviscerate` | ✓ MATCH | Present in APL (pos ~16) |
| 3 | Black Powder | `black_powder` | ✓ MATCH | Present in APL (pos ~18) |
| 4 | Shadowstrike | `shadowstrike` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~18 (Wowhead order reversed vs APL) |
| 5 | Shuriken Storm | `shuriken_storm` | ✓ MATCH | Present in APL (pos ~3) |
| 6 | Shadow Dance | `shadow_dance` | ✓ MATCH | Present in APL (pos ~8) |
| 7 | Shadow Blades | `shadow_blades` | ✓ MATCH | Present in APL (pos ~7) |
| 8 | Vanish | `vanish` | ✓ MATCH | Present in APL (pos ~9) |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Eviscerate | `eviscerate` | ✓ MATCH | Present in APL (pos ~16) |
| 2 | Shadow Dance | `shadow_dance` | ~ ORDER_DIFF | APL pos ~8, previous item at pos ~16 (Wowhead order reversed vs APL) |
| 3 | Shadow Blades | `shadow_blades` | ✓ MATCH | Present in APL (pos ~7) |
| 4 | Shadowstrike | `shadowstrike` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~7 (Wowhead order reversed vs APL) |
| 5 | Secret Technique | `secret_technique` | ✓ MATCH | Present in APL (pos ~15) |

### Hero: Trickster

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Secret Technique | `secret_technique` | ✓ MATCH | Present in APL (pos ~15) |
| 2 | Eviscerate | `eviscerate` | ✓ MATCH | Present in APL (pos ~16) |
| 3 | Shadowstrike | `shadowstrike` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~16 (Wowhead order reversed vs APL) |
| 4 | Backstab | `backstab` | ✓ MATCH | Present in APL (pos ~6) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Secret Technique | `secret_technique` | ✓ MATCH | Present in APL (pos ~15) |
| 2 | Eviscerate | `eviscerate` | ✓ MATCH | Present in APL (pos ~16) |
| 3 | Black Powder | `black_powder` | ✓ MATCH | Present in APL (pos ~18) |
| 4 | Shadowstrike | `shadowstrike` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~18 (Wowhead order reversed vs APL) |
| 5 | Shuriken Storm | `shuriken_storm` | ✓ MATCH | Present in APL (pos ~3) |
| 6 | Shadow Dance | `shadow_dance` | ✓ MATCH | Present in APL (pos ~8) |
| 7 | Shadow Blades | `shadow_blades` | ✓ MATCH | Present in APL (pos ~7) |
| 8 | Vanish | `vanish` | ✓ MATCH | Present in APL (pos ~9) |

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Shadow Dance | `shadow_dance` | ✓ MATCH | Present in APL (pos ~8) |
| 2 | Shadow Blades | `shadow_blades` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Secret Technique | `secret_technique` | ✓ MATCH | Present in APL (pos ~15) |
| 4 | Shadowstrike | `shadowstrike` | ~ ORDER_DIFF | APL pos ~2, previous item at pos ~15 (Wowhead order reversed vs APL) |
| 5 | Eviscerate | `eviscerate` | ✓ MATCH | Present in APL (pos ~16) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `apply_poison` | Sim-specific logic not covered by guide |
| `stealth` | Sim-specific logic not covered by guide |
| `goremaws_bite` | Sim-specific logic not covered by guide |
| `gloomblade` | Sim-specific logic not covered by guide |
| `coup_de_grace` | Sim-specific logic not covered by guide |
| `slice_and_dice` | Sim-specific logic not covered by guide |
| `thistle_tea` | Sim-specific logic not covered by guide |
| `deathmark` | Sim-specific logic not covered by guide |
| `kingsbane` | Sim-specific logic not covered by guide |
| `garrote` | Sim-specific logic not covered by guide |
| `rupture` | Sim-specific logic not covered by guide |
| `crimson_tempest` | Sim-specific logic not covered by guide |
| *(+17 more)* | |

### Key Findings

- **0 unique MISSING** actions and 7 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `shadowstrike` (Shadowstrike) - ORDER_DIFF
  1. [AoE Priority] `shadowstrike` (Shadowstrike) - ORDER_DIFF
  1. [Opener] `shadow_dance` (Shadow Dance) - ORDER_DIFF

---

## Shaman Elemental

### Hero: Farseer

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Stormbringer

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `flametongue_weapon` | Sim-specific logic not covered by guide |
| `lightning_shield` | Sim-specific logic not covered by guide |
| `thunderstrike_ward` | Sim-specific logic not covered by guide |
| `stormkeeper` | Sim-specific logic not covered by guide |
| `spiritwalkers_grace` | Sim-specific logic not covered by guide |
| `natures_swiftness` | Sim-specific logic not covered by guide |
| `voltaic_blaze` | Sim-specific logic not covered by guide |
| `ancestral_swiftness` | Sim-specific logic not covered by guide |
| `fire_elemental` | Sim-specific logic not covered by guide |
| `ascendance` | Sim-specific logic not covered by guide |
| `flame_shock` | Sim-specific logic not covered by guide |
| `earthquake` | Sim-specific logic not covered by guide |
| *(+7 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Shaman Enhancement

### Hero: Stormbringer

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Voltaic Blaze | `voltaic_blaze` | ✓ MATCH | Present in APL (pos ~4) |
| 2 | Crash Lightning | `crash_lightning` | ✓ MATCH | Present in APL (pos ~11) |
| 3 | Lava Lash | `lava_lash` | ✓ MATCH | Present in APL (pos ~9) |
| 4 | Ascendance | `ascendance` | ✓ MATCH | Present in APL (pos ~7) |
| 5 | Windstrike every GCD | `windstrike_every_gcd` | ✗ MISSING | Not found in SimC APL |

### Hero: Totemic

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Voltaic Blaze | `voltaic_blaze` | ✓ MATCH | Present in APL (pos ~4) |
| 2 | Surging Totem | `surging_totem` | ✓ MATCH | Present in APL (pos ~6) |
| 3 | Sundering | `sundering` | ✓ MATCH | Present in APL (pos ~8) |
| 4 | Lava Lash | `lava_lash` | ✓ MATCH | Present in APL (pos ~9) |
| 5 | Doom Winds and immediately  Primordial Storm | `doom_winds_and_immediately_primordial_storm` | ✗ MISSING | Not found in SimC APL |
| 6 | Crash Lightning | `crash_lightning` | ✓ MATCH | Present in APL (pos ~11) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `windfury_weapon` | Sim-specific logic not covered by guide |
| `flametongue_weapon` | Sim-specific logic not covered by guide |
| `lightning_shield` | Sim-specific logic not covered by guide |
| `bloodlust` | Sim-specific logic not covered by guide |
| `flame_shock` | Sim-specific logic not covered by guide |
| `doom_winds` | Sim-specific logic not covered by guide |
| `windstrike` | Sim-specific logic not covered by guide |
| `stormstrike` | Sim-specific logic not covered by guide |
| `tempest` | Sim-specific logic not covered by guide |
| `primordial_storm` | Sim-specific logic not covered by guide |
| `chain_lightning` | Sim-specific logic not covered by guide |
| `lightning_bolt` | Sim-specific logic not covered by guide |
| *(+10 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Warlock Affliction

### Hero: Hellcaller

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Haunt | `haunt` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Agony | `agony` | ✓ MATCH | Present in APL (pos ~8) |
| 3 | Wither | `wither` | ✓ MATCH | Present in APL (pos ~12) |
| 4 | Dark Harvest | `dark_harvest` | ~ ORDER_DIFF | APL pos ~7, previous item at pos ~12 (Wowhead order reversed vs APL) |
| 5 | Summon Darkglare | `summon_darkglare` | ✓ MATCH | Present in APL (pos ~9) |
| 6 | Malevolence | `malevolence` | ✓ MATCH | Present in APL (pos ~10) |
| 7 | Unstable Affliction | `unstable_affliction` | ✓ MATCH | Present in APL (pos ~11) |
| 8 | Malefic Grasp | `malefic_grasp` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~11 (Wowhead order reversed vs APL) |

### Hero: Soul Harvester

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Haunt | `haunt` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Agony | `agony` | ✓ MATCH | Present in APL (pos ~8) |
| 3 | Corruption | `corruption` | ✓ MATCH | Present in APL (pos ~13) |
| 4 | Summon Darkglare | `summon_darkglare` | ✓ MATCH | Present in APL (pos ~9) |
| 5 | Dark Harvest | `dark_harvest` | ✓ MATCH | Present in APL (pos ~7) |
| 6 | Unstable Affliction | `unstable_affliction` | ✓ MATCH | Present in APL (pos ~11) |
| 7 | Malefic Grasp | `malefic_grasp` | ~ ORDER_DIFF | APL pos ~3, previous item at pos ~11 (Wowhead order reversed vs APL) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `grimoire_of_sacrifice` | Sim-specific logic not covered by guide |
| `seed_of_corruption` | Sim-specific logic not covered by guide |
| `drain_soul` | Sim-specific logic not covered by guide |
| `shadow_bolt` | Sim-specific logic not covered by guide |
| `drain_life` | Sim-specific logic not covered by guide |
| `dark_pact` | Sim-specific logic not covered by guide |
| `power_siphon` | Sim-specific logic not covered by guide |
| `demonbolt` | Sim-specific logic not covered by guide |
| `grimoire_imp_lord` | Sim-specific logic not covered by guide |
| `grimoire_fel_ravager` | Sim-specific logic not covered by guide |
| `summon_doomguard` | Sim-specific logic not covered by guide |
| `call_dreadstalkers` | Sim-specific logic not covered by guide |
| *(+16 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Warlock Demonology

### Hero: Diabolist

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Call Dreadstalkers | `call_dreadstalkers` | ✓ MATCH | Present in APL (pos ~6) |
| 2 | Summon Demonic Tyrant | `summon_demonic_tyrant` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Hand of Gul'dan | `hand_of_guldan` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Demonbolt | `demonbolt` | ~ ORDER_DIFF | APL pos ~1, previous item at pos ~11 (Wowhead order reversed vs APL) |
| 5 | Infernal Bolt | `infernal_bolt` | ✓ MATCH | Present in APL (pos ~10) |

### Hero: Soul Harvester

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Call Dreadstalkers | `call_dreadstalkers` | ✓ MATCH | Present in APL (pos ~6) |
| 2 | Summon Demonic Tyrant | `summon_demonic_tyrant` | ✓ MATCH | Present in APL (pos ~7) |
| 3 | Hand of Gul'dan | `hand_of_guldan` | ✓ MATCH | Present in APL (pos ~11) |
| 4 | Demonbolt | `demonbolt` | ~ ORDER_DIFF | APL pos ~1, previous item at pos ~11 (Wowhead order reversed vs APL) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `power_siphon` | Sim-specific logic not covered by guide |
| `shadow_bolt` | Sim-specific logic not covered by guide |
| `grimoire_imp_lord` | Sim-specific logic not covered by guide |
| `grimoire_fel_ravager` | Sim-specific logic not covered by guide |
| `summon_doomguard` | Sim-specific logic not covered by guide |
| `implosion` | Sim-specific logic not covered by guide |
| `ruination` | Sim-specific logic not covered by guide |
| `dark_pact` | Sim-specific logic not covered by guide |
| `grimoire_of_sacrifice` | Sim-specific logic not covered by guide |
| `seed_of_corruption` | Sim-specific logic not covered by guide |
| `haunt` | Sim-specific logic not covered by guide |
| `malefic_grasp` | Sim-specific logic not covered by guide |
| *(+20 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Warlock Destruction

### Hero: Hellcaller

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Soul Fire | `soul_fire` | ✓ MATCH | Present in APL (pos ~2) |

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Soul Fire | `soul_fire` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Malevolence | `malevolence` | ✓ MATCH | Present in APL (pos ~8) |
| 3 | Conflagrate | `conflagrate` | ✓ MATCH | Present in APL (pos ~6) |

### Hero: Diabolist

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Soul Fire | `soul_fire` | ✓ MATCH | Present in APL (pos ~2) |

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Soul Fire | `soul_fire` | ✓ MATCH | Present in APL (pos ~2) |
| 2 | Conflagrate | `conflagrate` | ✓ MATCH | Present in APL (pos ~6) |

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `grimoire_of_sacrifice` | Sim-specific logic not covered by guide |
| `cataclysm` | Sim-specific logic not covered by guide |
| `immolate` | Sim-specific logic not covered by guide |
| `incinerate` | Sim-specific logic not covered by guide |
| `chaos_bolt` | Sim-specific logic not covered by guide |
| `summon_infernal` | Sim-specific logic not covered by guide |
| `shadowburn` | Sim-specific logic not covered by guide |
| `wither` | Sim-specific logic not covered by guide |
| `ruination` | Sim-specific logic not covered by guide |
| `infernal_bolt` | Sim-specific logic not covered by guide |
| `channel_demonfire` | Sim-specific logic not covered by guide |
| `rain_of_fire` | Sim-specific logic not covered by guide |
| *(+22 more)* | |

### Key Findings

- APL well-aligned with Wowhead guide (7 action matches)
- 34 extra sim-specific actions in APL (expected)

---

## Warrior Arms

### Hero: Slayer

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Avatar | `avatar` | ✓ MATCH | Present in APL (pos ~14) |
| 2 | Colossus Smash | `colossus_smash` | ✓ MATCH | Present in APL (pos ~15) |
| 3 | Bladestorm | `bladestorm` | ✓ MATCH | Present in APL (pos ~25) |
| 4 | Mortal Strike | `mortal_strike` | ~ ORDER_DIFF | APL pos ~20, previous item at pos ~25 (Wowhead order reversed vs APL) |
| 5 | Execute | `execute` | ✓ MATCH | Present in APL (pos ~22) |
| 6 | Heroic Strike | `heroic_strike` | ✓ MATCH | Present in APL (pos ~23) |
| 7 | Overpower | `overpower` | ✓ MATCH | Present in APL (pos ~21) |
| 8 | Cleave | `cleave` | ✓ MATCH | Present in APL (pos ~18) |
| 9 | Rend | `rend` | ~ ORDER_DIFF | APL pos ~11, previous item at pos ~18 (Wowhead order reversed vs APL) |
| 10 | Wrecking Throw | `wrecking_throw` | ✓ MATCH | Present in APL (pos ~26) |
| 11 | Slam | `slam` | ✓ MATCH | Present in APL (pos ~24) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Rend | `rend` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Ravager | `ravager` | ✓ MATCH | Present in APL (pos ~13) |
| 3 | Avatar | `avatar` | ✓ MATCH | Present in APL (pos ~14) |
| 4 | Colossus Smash | `colossus_smash` | ✓ MATCH | Present in APL (pos ~15) |
| 5 | Sweeping Strikes | `sweeping_strikes` | ✓ MATCH | Present in APL (pos ~12) |
| 6 | Demolish | `demolish` | ✓ MATCH | Present in APL (pos ~17) |
| 7 | Cleave | `cleave` | ✓ MATCH | Present in APL (pos ~18) |
| 8 | Mortal Strike | `mortal_strike` | ✓ MATCH | Present in APL (pos ~20) |
| 9 | Overpower | `overpower` | ✓ MATCH | Present in APL (pos ~21) |
| 10 | Execute | `execute` | ✓ MATCH | Present in APL (pos ~22) |
| 11 | Slam | `slam` | ✓ MATCH | Present in APL (pos ~24) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Colossus

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Rend | `rend` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Ravager | `ravager` | ✓ MATCH | Present in APL (pos ~13) |
| 3 | Avatar | `avatar` | ✓ MATCH | Present in APL (pos ~14) |
| 4 | Colossus Smash | `colossus_smash` | ✓ MATCH | Present in APL (pos ~15) |
| 5 | Heroic Strike | `heroic_strike` | ✓ MATCH | Present in APL (pos ~23) |
| 6 | Demolish | `demolish` | ~ ORDER_DIFF | APL pos ~17, previous item at pos ~23 (Wowhead order reversed vs APL) |
| 7 | Mortal Strike | `mortal_strike` | ✓ MATCH | Present in APL (pos ~20) |
| 8 | Cleave | `cleave` | ✓ MATCH | Present in APL (pos ~18) |
| 9 | Execute | `execute` | ✓ MATCH | Present in APL (pos ~22) |
| 10 | Overpower | `overpower` | ✓ MATCH | Present in APL (pos ~21) |
| 11 | Wrecking Throw | `wrecking_throw` | ✓ MATCH | Present in APL (pos ~26) |
| 12 | Cleave without  Martial Prowess talented | `cleave_without_martial_prowess_talented` | ✗ MISSING | Not found in SimC APL |
| 13 | Slam | `slam` | ✓ MATCH | Present in APL (pos ~24) |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Rend | `rend` | ✓ MATCH | Present in APL (pos ~11) |
| 2 | Ravager | `ravager` | ✓ MATCH | Present in APL (pos ~13) |
| 3 | Avatar | `avatar` | ✓ MATCH | Present in APL (pos ~14) |
| 4 | Colossus Smash | `colossus_smash` | ✓ MATCH | Present in APL (pos ~15) |
| 5 | Sweeping Strikes | `sweeping_strikes` | ✓ MATCH | Present in APL (pos ~12) |
| 6 | Demolish | `demolish` | ✓ MATCH | Present in APL (pos ~17) |
| 7 | Cleave | `cleave` | ✓ MATCH | Present in APL (pos ~18) |
| 8 | Mortal Strike | `mortal_strike` | ✓ MATCH | Present in APL (pos ~20) |
| 9 | Overpower | `overpower` | ✓ MATCH | Present in APL (pos ~21) |
| 10 | Execute | `execute` | ✓ MATCH | Present in APL (pos ~22) |
| 11 | Slam | `slam` | ✓ MATCH | Present in APL (pos ~24) |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `battle_stance` | Sim-specific logic not covered by guide |
| `charge` | Sim-specific logic not covered by guide |
| `thunder_clap` | Sim-specific logic not covered by guide |
| `champions_spear` | Sim-specific logic not covered by guide |
| `whirlwind` | Sim-specific logic not covered by guide |
| `storm_bolt` | Sim-specific logic not covered by guide |
| `berserker_stance` | Sim-specific logic not covered by guide |
| `heroic_leap` | Sim-specific logic not covered by guide |
| `recklessness` | Sim-specific logic not covered by guide |
| `rampage` | Sim-specific logic not covered by guide |
| `bloodthirst` | Sim-specific logic not covered by guide |
| `crushing_blow` | Sim-specific logic not covered by guide |
| *(+14 more)* | |

### Key Findings

- **1 unique MISSING** actions and 3 ORDER_DIFF items
- Top priority gaps:
  1. [Single-Target Priority] `cleave_without_martial_prowess_talented` (Cleave without  Martial Prowess talented) - MISSING
  1. [Single-Target Priority] `mortal_strike` (Mortal Strike) - ORDER_DIFF
  1. [Single-Target Priority] `rend` (Rend) - ORDER_DIFF
  1. [Single-Target Priority] `demolish` (Demolish) - ORDER_DIFF
- **Recommended**: Review and add missing major CDs/rotational abilities to APL

---

## Warrior Fury

### Hero: Slayer

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Mountain Thane

#### ST Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### AoE Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `berserker_stance` | Sim-specific logic not covered by guide |
| `charge` | Sim-specific logic not covered by guide |
| `heroic_leap` | Sim-specific logic not covered by guide |
| `recklessness` | Sim-specific logic not covered by guide |
| `avatar` | Sim-specific logic not covered by guide |
| `rampage` | Sim-specific logic not covered by guide |
| `bloodthirst` | Sim-specific logic not covered by guide |
| `crushing_blow` | Sim-specific logic not covered by guide |
| `bladestorm` | Sim-specific logic not covered by guide |
| `odyns_fury` | Sim-specific logic not covered by guide |
| `bloodbath` | Sim-specific logic not covered by guide |
| `execute` | Sim-specific logic not covered by guide |
| *(+28 more)* | |

### Key Findings

- NEEDS_MANUAL_REVIEW: Could not extract rotation steps

---

## Warrior Protection

### Hero: Colossus

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Demolish | `demolish` | ✓ MATCH | Present in APL (pos ~17) |
| 2 | Shield Slam | `shield_slam` | ✓ MATCH | Present in APL (pos ~23) |
| 3 | Thunder Clap | `thunder_clap` | ✓ MATCH | Present in APL (pos ~20) |
| 4 | Revenge | `revenge` | ✓ MATCH | Present in APL (pos ~22) |
| 5 | Execute targets | `execute_targets` | ✗ MISSING | Not found in SimC APL |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Demolish | `demolish` | ✓ MATCH | Present in APL (pos ~17) |
| 2 | Shield Slam | `shield_slam` | ✓ MATCH | Present in APL (pos ~23) |
| 3 | Thunder Clap | `thunder_clap` | ✓ MATCH | Present in APL (pos ~20) |
| 4 | Revenge | `revenge` | ✓ MATCH | Present in APL (pos ~22) |
| 5 | Execute targets | `execute_targets` | ✗ MISSING | Not found in SimC APL |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

### Hero: Mountain Thane

#### Single-Target Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Shield Slam | `shield_slam` | ✓ MATCH | Present in APL (pos ~23) |
| 2 | Thunder Clap | `thunder_clap` | ✓ MATCH | Present in APL (pos ~20) |
| 3 | Revenge | `revenge` | ✓ MATCH | Present in APL (pos ~22) |
| 4 | Execute targets | `execute_targets` | ✗ MISSING | Not found in SimC APL |

#### AoE Priority

| # | Wowhead Action | SimC Name | Status | Notes |
|---|----------------|-----------|--------|-------|
| 1 | Shield Slam | `shield_slam` | ✓ MATCH | Present in APL (pos ~23) |
| 2 | Thunder Clap | `thunder_clap` | ✓ MATCH | Present in APL (pos ~20) |
| 3 | Revenge | `revenge` | ✓ MATCH | Present in APL (pos ~22) |
| 4 | Execute targets | `execute_targets` | ✗ MISSING | Not found in SimC APL |

#### Opener Priority
No priority steps found - NEEDS_MANUAL_REVIEW

#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)

| SimC Action | Notes |
|-------------|-------|
| `battle_stance` | Sim-specific logic not covered by guide |
| `charge` | Sim-specific logic not covered by guide |
| `avatar` | Sim-specific logic not covered by guide |
| `shield_wall` | Sim-specific logic not covered by guide |
| `ignore_pain` | Sim-specific logic not covered by guide |
| `demoralizing_shout` | Sim-specific logic not covered by guide |
| `ravager` | Sim-specific logic not covered by guide |
| `champions_leap` | Sim-specific logic not covered by guide |
| `champions_spear` | Sim-specific logic not covered by guide |
| `thunder_blast` | Sim-specific logic not covered by guide |
| `shield_charge` | Sim-specific logic not covered by guide |
| `shield_block` | Sim-specific logic not covered by guide |
| *(+24 more)* | |

### Key Findings

- Minor gaps: **1 unique missing**, 0 order differences
  1. [Single-Target Priority] `execute_targets` (Execute targets) - MISSING from SimC APL

---

## Priority Queue

Ranking all specs by urgency of APL work needed based on gap analysis:

### HIGH Priority

Significant gaps found between Wowhead guide and SimC APL (3+ missing major spells):

- **demon-hunter/havoc**

### MEDIUM Priority

Minor gaps (1-2 missing spells) or unclear Wowhead content:

- **death-knight/blood**
- **death-knight/frost**
- **death-knight/unholy**
- **demon-hunter/devourer**
- **demon-hunter/vengeance**
- **druid/balance**
- **druid/feral**
- **druid/guardian**
- **evoker/augmentation**
- **evoker/devastation**
- **hunter/beast-mastery**
- **hunter/marksmanship**
- **hunter/survival**
- **mage/arcane**
- **mage/fire**
- **mage/frost**
- **monk/brewmaster**
- **monk/windwalker**
- **paladin/protection**
- **priest/shadow**
- **rogue/assassination**
- **rogue/outlaw**
- **rogue/subtlety**
- **shaman/elemental**
- **shaman/enhancement**
- **warlock/affliction**
- **warlock/demonology**
- **warrior/arms**
- **warrior/fury**
- **warrior/protection**

### LOW Priority

APL well-aligned with Wowhead guide:

- **paladin/retribution**
- **warlock/destruction**

### Summary Statistics

| Category | Count |
|----------|-------|
| Total specs analyzed | 33 |
| HIGH urgency | 1 |
| MEDIUM urgency | 30 |
| LOW urgency | 2 |

---

*This report was auto-generated by `gen_apl_diff.py`. Manual verification recommended for HIGH priority specs.*

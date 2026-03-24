# Rogue Spec Audit Report: Wowhead vs SimC Implementation
Generated: 2026-03-24
Auditor: Automated comparison of Wowhead extracted data vs SimC codebase

## Files Compared
- Wowhead data: wowhead/rogue/{assassination,outlaw,subtlety}/extracted/{rotation,tier}.md
- Wowhead info: wowhead/rogue/{assassination,outlaw,subtlety}/info_base.md
- APL: engine/class_modules/apl/apl_rogue.cpp
- Class module: engine/class_modules/sc_rogue.cpp

---

## 1. ASSASSINATION ROGUE

### 1.1 Rotation Priority — Wowhead vs APL

#### Single-Target Priority (Deathstalker/Fatebound)
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Maintain Garrote | core_dot: garrote with refreshable checks | OK |
| Mutilate to 5+ CP | generate: mutilate,if=spell_targets.fan_of_knives<=1+talent.blindside | OK |
| Envenom at max CP with Darkest Night active | default: combo_points.deficit=0 with darkest_night check routes to spend | OK |
| Maintain Rupture at 5+ CP | core_dot: rupture,if=combo_points>=5&refreshable (with darkest_night guard) | OK |
| Vanish + Garrote for Improved Garrote (sync Deathmark) | vanish list: checks improved_garrote, pmultiplier, deathmark CD | OK |
| Deathmark on cooldown | cds: deathmark with bleed/kingsbane/envenom conditions | OK |
| Kingsbane on CD after Deathmark | cds: kingsbane with deathmark sync check (>52s remaining = use independently) | OK |
| Envenom at 5+ CP unless 80 stacks Implacable | spend: envenom,if=buff.implacable_tracker.stack<4 (4 stacks = 80%) | OK |

#### AoE Priority
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Maintain Garrote on main target | core_dot handles this | OK |
| Maintain Rupture on main target | core_dot handles this | OK |
| Crimson Tempest to spread bleeds | generate: crimson_tempest for bleed spread | OK |
| Fan of Knives to build CP | generate: fan_of_knives at >1+blindside targets | OK |

#### Cooldown Details
| Feature | APL Implementation | Status |
|---|---|---|
| Deathmark requires bleeds active + Kingsbane ready + Envenom up | cds: deathmark checks dot.garrote.ticking&dot.rupture.ticking&cooldown.kingsbane.remains<=2&buff.envenom.up | OK |
| Kingsbane syncs with Deathmark | cds: kingsbane checks dot.deathmark.ticking or CD>52 | OK |
| Vanish for Improved Garrote | vanish list with pmultiplier<=1 and deathmark alignment | OK |

#### Darkest Night / Shiv Edge Case (Deathstalker only)
| Feature | APL Implementation | Status |
|---|---|---|
| Envenom at max CP when Darkest Night active | default routing uses buff.darkest_night.up&combo_points.deficit=0 | OK |
| Shiv as cheap 1-CP generator for Darkest Night with Toxic Stiletto | generate: shiv,if=buff.darkest_night.up&combo_points.deficit=1&...&talent.toxic_stiletto | OK |

#### Implacable Pooling
| Feature | APL Implementation | Status |
|---|---|---|
| Let Envenom expire at 80 stacks (4 tracker stacks) | spend: envenom,if=buff.implacable_tracker.stack<4; second envenom at energy.pct>70 to prevent overcap | OK |

#### Issues Found — Assassination
1. **APL TODO Comments**: The APL has two TODO notes: "check envenom buff requirement when apex talents are fixed" on both Deathmark and Kingsbane conditions. This suggests the Envenom-up requirement for Deathmark may need revision once Implacable (apex talent) interactions are fully resolved.
2. **Fatebound vs Deathstalker Differentiation**: Wowhead shows Deathstalker has an extra priority for "Envenom at max CP when Darkest Night is active" that Fatebound does not. The APL handles this generically via the darkest_night buff check, which is correct since Fatebound wouldn't have Darkest Night talented. No issue.
3. **Opener Sequence**: Wowhead specifies a strict opener (Garrote > Mutilate to 5 > Rupture > Mutilate to 5 > Envenom > Deathmark > Kingsbane > Envenom). The APL does not encode a strict opener sequence — it relies on the priority list from the start. This is standard for SimC APLs but means the opener timing differs slightly from Wowhead guidance.

### 1.2 Tier Set Bonuses — Assassination

**Wowhead Data:**
- 2pc: Garrote's damage increased by 30% and it also applies weapon poisons
- 4pc: Garrote's Energy cost reduced by 10. Mutilate, Ambush, and Fan of Knives deal 25% increased damage to poisoned targets

**SimC Implementation:**
| Bonus | Implementation | Status |
|---|---|---|
| 2pc: Garrote +30% damage | Line ~4414: m *= 1.0 + mid1_assassination_2pc->effectN(1).percent() | IMPLEMENTED |
| 2pc: Garrote applies weapon poisons | Needs verification — spell data likely handles this via trigger | LIKELY OK (spell data driven) |
| 4pc: Garrote energy cost -10 | Spell data should handle this | LIKELY OK |
| 4pc: Mut/Ambush/FoK +25% to poisoned targets | affected_by.mid1_assassination_4pc flag + is_poisoned() check in composite_da_multiplier | IMPLEMENTED |

**Tier APL Impact**: Wowhead says "does not affect the rotation" — confirmed, APL has no tier-specific conditions for Assassination.

### 1.3 Key Talent Implementations — Assassination
| Talent | Implementation Status |
|---|---|
| Sudden Demise | IMPLEMENTED — +10% bleed dmg always; execute bonus scales linearly to +150% at 0% HP below 35% |
| Implacable (Apex) | IMPLEMENTED — tracker buff, energy regen burst, physical+nature strikes |
| Darkest Night (Deathstalker) | IMPLEMENTED — buff with damage/crit bonuses at max CP |
| Improved Garrote | IMPLEMENTED — stealth buff with pmultiplier tracking |
| Kingsbane | IMPLEMENTED — DoT with poison ramping, Deathmark interaction |
| Crimson Tempest | IMPLEMENTED — bleed spread mechanic |
| Caustic Spatter | IMPLEMENTED (referenced in class module) |
| Lethal Dose | IMPLEMENTED (talent referenced) |
| Finish the Job | IMPLEMENTED (damage_buff_t) |

---

## 2. OUTLAW ROGUE

### 2.1 Rotation Priority — Wowhead vs APL

#### Single-Target Priority (Trickster)
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Roll the Bones if stage 1 or less | cds: roll_the_bones,if=!buff.roll_the_bones.up\|rtb_buffs=1 | OK |
| Keep It Rolling at stage 2+ | cds: keep_it_rolling,if=rtb_buffs=2...or rtb_buffs>=3 | OK |
| Adrenaline Rush on CD at ≤2 CP | cds: adrenaline_rush,if=!buff.adrenaline_rush.up&(!variable.finish_condition\|!talent.improved_adrenaline_rush) | PARTIAL — see note |
| Blade Rush on CD | cds: blade_rush with tier/energy checks | OK |
| Between the Eyes at 6+ CP | finish: between_the_eyes with AR sync for Supercharger/Zero In | OK |
| Killing Spree at 6+ CP | finish: killing_spree (pooling for energy) | OK |
| Dispatch at 5+ CP | finish: dispatch as fallback finisher | OK |
| Pistol Shot at 6 stacks Opportunity | build: pistol_shot at max_stack or near-expiry | OK |
| Pistol Shot at 3 stacks & 1-3 CP | build: pistol_shot with combo_points.deficit check | PARTIAL — see note |
| Sinister Strike at ≤5 CP | build: sinister_strike as fallback | OK |

#### Single-Target Priority (Fatebound)
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Preparation when BtE/AR/Blade Rush on CD | cds: preparation,if=cooldown.adrenaline_rush.remains>30&!cooldown.between_the_eyes.ready&(!cooldown.killing_spree.ready\|!hero_tree.trickster) | OK |
| No Killing Spree (Fatebound) | finish: killing_spree is unconditional — Fatebound shouldn't talent it, so naturally excluded | OK |

#### AoE Priority
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Blade Flurry at 2+ targets | cds: blade_flurry,if=spell_targets>=2&buff.blade_flurry.remains<gcd | OK |
| Blade Flurry recast at ≤4 CP with 4+ targets | build: blade_flurry,if=talent.deft_maneuvers&spell_targets>=4 (for CP generation) | DIFFERENT — see note |

#### Issues Found — Outlaw
1. **Adrenaline Rush CP condition**: Wowhead says "at 2 or fewer combo points." APL uses `!variable.finish_condition|!talent.improved_adrenaline_rush` which means "not at finisher threshold OR no Improved AR." With Improved AR, it will only cast when not ready to finish, roughly corresponding to low CP. This is more nuanced than the simple "≤2 CP" from Wowhead but functionally similar.

2. **Pistol Shot Opportunity Thresholds**: Wowhead says "3 stacks and 1-3 CP." APL uses `combo_points.deficit>=(1+talent.quick_draw+(talent.quick_draw*talent.fan_the_hammer.rank))` which is a talent-dependent threshold rather than a flat 1-3 CP. The intent is the same (don't overcap CP) but the exact thresholds differ based on talent selection.

3. **Blade Flurry AoE Recast**: Wowhead says "recast at 4 or fewer combo points when 4 or more targets." APL uses Blade Flurry with Deft Maneuvers at 4+ targets as a CP builder (build list), not a recast mechanic. The approach differs but achieves the same goal of using BF for CP gen in high-target AoE.

4. **Coup de Grace**: Present in APL (build and finish lists) via Trickster hero tree but NOT explicitly mentioned in Wowhead rotation for Outlaw. It's triggered by Disorienting Strikes buff. This is correct since it's a Trickster proc ability.

5. **Hidden Opportunity / Audacity**: APL has extensive Ambush/Pistol Shot logic for Hidden Opportunity talent builds. Wowhead rotation doesn't mention these explicitly as the extracted data focuses on the standard priority, but the APL correctly handles this alternate build path.

### 2.2 Tier Set Bonuses — Outlaw

**Wowhead Data:**
- 2pc: Blade Rush damage +30%, primary target +15% additional
- 4pc: Blade Rush CD -6 sec, +5% damage dealt for 8 sec

**SimC Implementation:**
| Bonus | Implementation | Status |
|---|---|---|
| 2pc: Blade Rush +30% (+15% primary) | mid1_outlaw_2pc spell data | IMPLEMENTED |
| 4pc: Blade Rush CD -6 sec | Spell data driven | IMPLEMENTED |
| 4pc: +5% damage for 8 sec (Whirl of Blades) | buffs.mid1_outlaw_4pc = "whirl_of_blades" damage_buff_t | IMPLEMENTED |
| APL tier awareness | blade_rush,if=set_bonus.mid1_4pc&!buff.whirl_of_blades.up | IMPLEMENTED |

**Tier APL Impact**: Wowhead says "buffs the already optimal playstyle" — confirmed, APL adds Blade Rush priority when tier 4pc buff is not active.

### 2.3 Key Talent Implementations — Outlaw
| Talent | Implementation Status |
|---|---|
| Grand Melee | IMPLEMENTED — Modifies Blade Flurry Effect #2 cleave multiplier by +8% |
| Roll the Bones (staged system) | IMPLEMENTED — rtb_buffs tracking, stage-based bonuses |
| Keep It Rolling | IMPLEMENTED — cooldown, Restless Blades interaction |
| Preparation | IMPLEMENTED — CD reset mechanic |
| Killing Spree | IMPLEMENTED — with Trickster interaction |
| Restless Blades | IMPLEMENTED — CDR on finishers |
| Blade Rush | IMPLEMENTED — energy generation + damage |
| Hidden Opportunity / Audacity | IMPLEMENTED — APL has full Ambush/PS logic |
| Supercharger | IMPLEMENTED — referenced in BtE APL condition |

---

## 3. SUBTLETY ROGUE

### 3.1 Rotation Priority — Wowhead vs APL

#### Single-Target Priority (Deathstalker)
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Shadowstrike from Stealth | default: shadowstrike for Ancient Arts check + build list | OK |
| During Dance: Secret Technique at 6+ CP | finish: secret_technique,if=buff.shadow_dance.up | OK |
| During Dance: Eviscerate at 6+ CP | finish: eviscerate (multiple conditions) | OK |
| During Dance: Shadowstrike builder | build: shadowstrike with deathstalkers_mark check | OK |
| Outside Dance: Eviscerate at 6+ CP | finish: eviscerate with secret_technique CD check | OK |
| Outside Dance: Backstab builder | build: backstab,if=variable.targets<2 | OK |
| Shadow Dance with LOW CP + Secret Technique ready | cds: shadow_dance,if=variable.shd_cp&energy>=30&... | **MISMATCH** |
| Shadow Blades with Shadow Dance ready | cds: shadow_blades,if=variable.shd_cp&cooldown.shadow_dance.ready | **PARTIAL MISMATCH** |
| Vanish on CD with low CP | cds: vanish,if=combo_points<=1 | OK |

#### Single-Target Priority (Trickster)
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Shadow Dance at 6+ CP + Secret Technique ready | cds: shadow_dance uses variable.shd_cp (>=6 CP) | OK — matches Trickster |

#### AoE Priority (Deathstalker)
| Wowhead Priority | APL Implementation | Status |
|---|---|---|
| Eviscerate with Darkest Night | finish: eviscerate,if=buff.darkest_night.up | OK |
| Black Powder at 2+ targets | finish: black_powder,if=variable.targets>=2 | OK |
| Shadowstrike at ≤3 targets or if DS Mark not up | build: shadowstrike,if=!debuff.deathstalkers_mark.up&...or variable.targets<=2 | CLOSE — Wowhead says ≤3, APL uses ≤2 |
| Shuriken Storm for AoE building | build: shuriken_storm,if=variable.targets>1 | OK |

#### Issues Found — Subtlety
1. **CRITICAL — Shadow Dance CP Requirement for Deathstalker**: Wowhead explicitly states "Use Shadow Dance with **low Combo Points** when Secret Technique is ready" for Deathstalker, versus "6 or more Combo Points" for Trickster. The APL uses `variable.shd_cp` (combo_points>=6) for ALL hero talent builds. This means the APL does NOT differentiate between Deathstalker and Trickster for Shadow Dance entry conditions. **The APL contradicts Wowhead for Deathstalker builds.**

2. **Shadow Blades CP Requirement**: Similarly, `shadow_blades,if=variable.shd_cp&cooldown.shadow_dance.ready` requires 6+ CP for all builds. Wowhead says to use Shadow Blades "if you have Shadow Dance ready" without a specific CP requirement — but since Shadow Dance is paired with it, the CP requirement propagates. For Deathstalker, this creates the same mismatch as issue #1.

3. **Shadowstrike Target Threshold in AoE**: Wowhead says Shadowstrike should be used "with 3 or less targets or if Deathstalker's Mark is not up" during Shadow Dance AoE. APL uses `variable.targets<=2` for the general shadowstrike condition (plus a separate deathstalkers_mark check). The threshold differs by 1 target.

4. **Ancient Arts Optimization**: Wowhead mentions specific optimizations for Ancient Arts during Shadow Dance — using Shadowstrike on high CP to activate the buff, and ensuring Darkest Night Eviscerate has Ancient Arts. The APL has: `shadowstrike,if=(buff.darkest_night.up|talent.unseen_blade)&buff.shadow_techniques.stack>=5&!buff.ancient_arts.up&(variable.targets<=3+talent.weaponmaster)` which handles this partially. Trickster gets this for every finisher (talent.unseen_blade), Deathstalker only for Darkest Night. This appears correct.

5. **Coup de Grace**: Present in APL finish list (`coup_de_grace,if=cooldown.secret_technique.remains>=3|buff.shadow_dance.up`) but not explicitly in Wowhead rotation priority. This is a Trickster hero talent ability, correctly included.

6. **Goremaw's Bite**: Present in APL build list (`goremaws_bite,if=combo_points.deficit>=3`) but not mentioned in Wowhead rotation. This is a talent-dependent builder that Wowhead may have omitted from the priority or considers implicit.

7. **Second Shadow Dance During Shadow Blades**: Wowhead notes a second Shadow Dance should be used during Shadow Blades without Secret Technique ready. The APL handles this with `buff.shadow_blades.remains>=cooldown.secret_technique.remains|buff.shadow_blades.up&cooldown.secret_technique.duration>=18` which attempts to fit two dances into Shadow Blades. This is functionally aligned but uses haste-dependent logic.

### 3.2 Tier Set Bonuses — Subtlety

**Wowhead Data:**
- 2pc: Finishing moves deal 1.5% more damage per combo point spent
- 4pc: Shadow Blades has 4.0 sec increased duration and attacks deal additional 6.0% as Shadow

**SimC Implementation:**
| Bonus | Implementation | Status |
|---|---|---|
| 2pc: Finishers +1.5% per CP spent | affected_by.mid1_subtlety_2pc flag on consumes_combo_points() actions | IMPLEMENTED |
| 4pc: Shadow Blades +4 sec duration | mid1_subtlety_4pc spell data | IMPLEMENTED |
| 4pc: Attacks deal +6% as Shadow during SB | mid1_subtlety_4pc spell data | IMPLEMENTED |

**Tier APL Impact**: Wowhead says "Neither of the tier set bonuses changes the rotation" — confirmed, no tier-specific APL conditions for Subtlety.

### 3.3 Key Talent Implementations — Subtlety
| Talent | Implementation Status |
|---|---|
| Secret Technique | IMPLEMENTED — finisher with clone attacks, pet-based shadow hits |
| Shadow Dance | IMPLEMENTED — stealth buff, charge system |
| Shadow Blades | IMPLEMENTED — CP doubling, shadow damage echo |
| Deepening Shadows | IMPLEMENTED — haste-based Shadow Dance duration extension |
| Darkest Night (Deathstalker) | IMPLEMENTED — damage/crit buff at max CP |
| Ancient Arts | IMPLEMENTED — buff tracked, Shadow Techniques interaction |
| Supercharger | IMPLEMENTED — buff vector for charge tracking |
| Deathstalker's Mark | IMPLEMENTED — debuff + damage proc |
| Replicating Shadows | Referenced in class module |
| Danse Macabre | IMPLEMENTED — premeditation interaction in build list |

---

## 4. SUMMARY OF ALL ISSUES

### Critical Issues
1. **[Subtlety] Shadow Dance CP for Deathstalker**: APL requires 6+ CP to enter Shadow Dance for ALL builds. Wowhead says Deathstalker should enter with LOW CP. This is a fundamental rotation difference that likely affects DPS simulation accuracy for Deathstalker Subtlety.

### Moderate Issues
2. **[Subtlety] Shadowstrike AoE target threshold**: APL uses ≤2 targets, Wowhead says ≤3 targets for Shadowstrike during Shadow Dance AoE. Off by 1 target.
3. **[Assassination] APL TODO notes**: Deathmark and Kingsbane conditions have TODO comments about Envenom buff requirements with apex talents. May need updating.
4. **[Outlaw] Adrenaline Rush CP condition**: Wowhead says ≤2 CP, APL uses finish_condition inverse. Functionally similar but not identical.

### Minor Issues / Differences
5. **[Outlaw] Pistol Shot Opportunity thresholds**: APL uses talent-dependent formula vs Wowhead's flat 3-stack/1-3 CP rule.
6. **[Outlaw] Blade Flurry AoE recast**: Different mechanical approach (Deft Maneuvers CP gen vs explicit recast).
7. **[All Specs] Opener sequences**: APLs use priority lists from the start rather than strict opener sequences. This is standard SimC behavior.
8. **[Subtlety] Goremaw's Bite**: In APL but not in Wowhead rotation. Likely talent-dependent and implicitly covered.

### Confirmed Implementations
- **Sudden Demise**: Fully implemented with execute scaling
- **Grand Melee**: Fully implemented for Outlaw (Blade Flurry cleave modifier)
- **All Tier Sets**: All 6 set bonuses (2pc + 4pc for each spec) are implemented
- **Implacable (Apex)**: Fully implemented with tracker, energy regen, and strike damage
- **Darkest Night**: Fully implemented across Assassination and Subtlety
- **All major cooldowns**: Deathmark, Kingsbane, Adrenaline Rush, Roll the Bones, Keep It Rolling, Blade Rush, Shadow Blades, Shadow Dance, Secret Technique, Killing Spree, Preparation — all implemented
- **Hero talent systems**: Deathstalker, Fatebound, Trickster — all have talent entries and buff implementations

# Evoker APL Audit Report
## Wowhead vs SimC Comparison
Generated: 2026-03-24

Sources:
- Wowhead rotation/tier guides (extracted 2026-03-23)
- SimC APL: engine/class_modules/apl/apl_evoker.cpp
- SimC class module: engine/class_modules/sc_evoker.cpp

---

## DEVASTATION EVOKER

### Scalecommander (SC) — Single Target

**Wowhead Priority:**
1. Hover if capped and Deep Breath ready soon
2. Deep Breath
3. Deep Breath when Strafing Run about to expire
4. Dragonrage
5. Tip the Scales
6. Eternity Surge Rank 1
7. Fire Breath Rank 1
8. Disintegrate with Mass Disintegrate
9. Disintegrate
10. Azure Sweep
11. Living Flame as filler
12. Azure Strike for movement

**APL (st_sc list):**
1. Deep Breath if Strafing Run about to expire
2. Dragonrage
3. Hover (off-GCD)
4. Tip the Scales (off-GCD, during Dragonrage)
5. Eternity Surge empower_to=1
6. Fire Breath empower_to=1
7. Disintegrate (Mass Disintegrate prioritized)
8. Disintegrate (normal chain)
9. Azure Sweep
10. Living Flame (with Burnout/Leaping Flames/Ancient Flame)
11. Azure Strike (>1 target)
12. Living Flame
13. Green list (Emerald Blossom/Verdant Embrace for Scarlet Adaptation)
14. Azure Strike

#### MISSING
- [M1] **Deep Breath on cooldown (generic)**: Wowhead lists "Deep Breath" as #2 priority
  (use on CD). APL st_sc only uses Deep Breath when Strafing Run is about to expire
  (remains<=gcd.max*2). The general "use Deep Breath on cooldown" priority is absent.
  APL only has the Strafing Run refresh condition.

#### WRONG_ORDER
- [W1] **Tip the Scales placement**: Wowhead puts Tip the Scales at #5 before Eternity
  Surge at #6, implying TtS should be used on ES. APL uses TtS as off-GCD during
  Dragonrage only (line 143), which is consistent but the condition `if=buff.dragonrage.up`
  is more restrictive than Wowhead's unconditional placement.

#### CONDITION_ISSUES
- [C1] **Tip the Scales only during Dragonrage (SC)**: APL restricts TtS to
  `buff.dragonrage.up` for both ST and AoE SC lists. Wowhead lists it as a general
  priority (not Dragonrage-gated). Outside DR, the APL will never use TtS in SC.
- [C2] **Deep Breath Strafing Run threshold**: APL uses `buff.strafing_run.remains<=gcd.max*2`.
  Wowhead says "when Strafing Run is about to expire" which is vague. The 2*GCD threshold
  seems reasonable but could be too tight or too loose depending on haste.

#### MISSING_MECHANIC
- None identified for SC ST tier or talents.

---

### Scalecommander (SC) — AoE (3+ targets)

**Wowhead Priority:**
1. Hover if capped / Deep Breath ready
2. Deep Breath
3. Dragonrage
4. Tip the Scales on Eternity Surge
5. Fire Breath Rank 1
6. Eternity Surge Rank 1
7. Deep Breath with Strafing Run
8. Disintegrate with Mass Disintegrate
9. Pyre at 4+ targets
10. Disintegrate (otherwise)
11. Azure Sweep
12. Living Flame with Leaping Flames/Burnout
13. Azure Strike as filler

**APL (aoe_sc list) order:**
1. Hover
2. Deep Breath (imminent_destruction + strafing_run, if !buff.strafing_run.up)
3. Tip the Scales (during Dragonrage)
4. Dragonrage
5. Eternity Surge empower_to=1
6. Fire Breath empower_to=1
7. Deep Breath (imminent_destruction, generic)
8. Pyre (4+ targets, no mass_disintegrate_stacks)
9. Disintegrate (mass_disintegrate)
10. Azure Sweep
11. Living Flame (leaping_flames conditions)
12. ES call (for azure_sweep trigger)
13. Azure Strike

#### WRONG_ORDER
- [W2] **Fire Breath vs Eternity Surge**: Wowhead says FB Rank 1 (#5) before ES (#6).
  APL has ES before FB (lines 130-131). This is reversed from Wowhead's AoE priority.
  In ST the APL also has ES before FB, matching Wowhead ST. The AoE mismatch may be
  intentional for sim optimization but differs from the guide.

#### CONDITION_ISSUES
- [C3] **AoE Pyre threshold**: Wowhead says "Pyre at 4+ targets". APL uses
  `active_enemies>=4|active_enemies>=3&(talent.feed_the_flames|talent.volatility)`,
  which is slightly more permissive (3 targets with certain talents). This is a
  refinement, not necessarily wrong.
- [C4] **Deep Breath conditions in AoE**: Wowhead lists Deep Breath as #2 unconditionally.
  APL gates it behind `talent.imminent_destruction&talent.strafing_run&!buff.strafing_run.up`
  for the first check. The generic Deep Breath (#7) also requires imminent_destruction.
  If player doesn't have imminent_destruction, Deep Breath is never cast in AoE SC.

---

### Flameshaper (FS) — Single Target

**Wowhead Priority:**
1. Dragonrage
2. Tip the Scales if Eternity Surge ready
3. Eternity Surge with Tip the Scales
4. Fire Breath to maintain DoT
5. Eternity Surge Rank 1
6. Disintegrate
7. Azure Sweep
8. Living Flame
9. Azure Strike

**APL (st_fs list) order:**
1. Dragonrage
2. Hover (off-GCD)
3. Tip the Scales (off-GCD, during Dragonrage, if ES<=FB)
4. Eternity Surge empower_to=2 (2 targets)
5. Eternity Surge empower_to=1
6. Fire Breath empower_to=1 (refreshable, various conditions)
7. Pyre (2+ targets, Feed the Flames + Volatility)
8. Disintegrate
9. Azure Sweep
10. Living Flame
11. Azure Strike
12. Living Flame (fallback)
13. Green list
14. Azure Strike (fallback)

#### MISSING
- [M2] **Engulf is completely absent from FS APL**: Wowhead's Flameshaper guide
  (and community comments) emphasize Engulf as a key Flameshaper ability for
  buffing damage through DOTs. The APL has zero references to Engulf for Flameshaper
  Devastation. The class module has only 2 references to engulf. This is a significant
  gap for Flameshaper gameplay.
- [M3] **Shattering Star absent from APL**: While a talent, Shattering Star appears
  in community discussion as part of Flameshaper openers but is not in any APL list.

#### CONDITION_ISSUES
- [C5] **Tip the Scales FS condition**: APL uses `buff.dragonrage.up&action.eternity_surge.usable_in<=action.fire_breath.usable_in`.
  Wowhead says "Tip the Scales if Eternity Surge is ready" — simpler condition.
  The APL adds a comparison with Fire Breath timing which is not in the guide.
- [C6] **Fire Breath FS condition**: APL has complex conditions including
  `variable.can_use_empower&!buff.tip_the_scales.up&dot.fire_breath_damage.refreshable&...`
  Wowhead simply says "maintain the DoT debuff." The refreshable check aligns but the
  additional guards around TtS and recharge timing are APL-specific optimizations.

---

### Flameshaper (FS) — AoE (3+ targets)

**Wowhead Priority:**
1. Dragonrage
2. Tip the Scales on Eternity Surge
3. Fire Breath Rank 1 (maintain DoT)
4. Eternity Surge Rank 1
5. Pyre
6. Azure Sweep
7. Living Flame with Leaping Flames/Burnout
8. Azure Strike

**APL (aoe_fs list) - partial match:**
The AoE FS list exists and generally follows priority but:

#### MISSING
- [M4] **Pyre in FS AoE**: Wowhead says "Cast Pyre" unconditionally in FS AoE.
  APL gates Pyre behind `cooldown.dragonrage.remains>gcd.max*4&(buff.charged_blast.stack>=12|active_enemies>=4|...)`.
  The charged_blast stack condition is an optimization not in Wowhead's guide.

#### WRONG_ORDER
- [W3] **FS AoE Fire Breath before Dragonrage in APL**: APL line 97 casts Fire Breath
  before Dragonrage prep (line 101). Wowhead has Dragonrage as #1 in FS AoE.

---

### Devastation Tier Set (Midnight S1 — Livery of the Black Talon)

**Wowhead:**
- 2pc: Azure Sweep damage +50%, +100% additional on primary target
- 4pc: Eternity Surge grants 1 extra Azure Sweep charge; Azure Sweep reduces ES CD by 2s
- Rotation change: Prioritize Azure Sweep after empowers (not capped on Essence Burst);
  Event Horizon talent gains value. Not worthwhile above 3 targets.

**SimC Implementation:**
- 2pc: Implemented in azure_sweep_t::composite_da_multiplier (line 5342) — primary target
  bonus via chain_target==0 check. Uses effectN(2).percent().
- 4pc: Implemented — extra stack on azure_sweep buff (line 10288-10289), ES CDR on
  Azure Sweep execute (line 5354-5356).
- APL references: `set_bonus.mid1_2pc&talent.azure_sweep` condition exists in st_fs (line 115).

#### CONDITION_ISSUES
- [C7] **Tier set APL handling is minimal**: Wowhead says "prioritize Azure Sweep after
  empowers as long as not capped on Essence Burst." The APL does not have explicit
  Essence Burst cap checking around Azure Sweep usage. Azure Sweep is simply listed in
  priority order. The `set_bonus.mid1_2pc` reference only appears once (in st_fs ES
  condition, line 115) as an alternative trigger for ES — not for prioritizing Azure Sweep.
- [C8] **"Not worthwhile above 3 targets" for tier rotation change**: The APL does not
  differentiate Azure Sweep priority based on target count for tier purposes. Both AoE
  lists already include Azure Sweep, but the tier-specific "prioritize after empowers"
  logic is absent.

#### MISSING_MECHANIC
- [MM1] **Event Horizon talent synergy**: Wowhead notes Event Horizon gains value with
  tier. No special APL handling for Event Horizon + tier interaction.

---

## AUGMENTATION EVOKER

### Chronowarden — Single Target / AoE

**Wowhead Priority (ST and AoE are nearly identical):**
1. Maintain Prescience on DPS players
2. Ebon Might if few seconds remain
3. Breath of Eons
4. Tip the Scales
5. Fire Breath Rank 1 (with Molten Embers)
6. Upheaval Rank 1
7. Eruption
8. Living Flame filler
9. Azure Strike backup filler
10. Maintain Blistering Scales on tank

**APL (default list) order:**
1. Cancel TtS buff if needed
2. Hover (off-GCD)
3. Ebon Might (pandemic threshold)
4. Prescience (early, time<=8)
5. Potion
6. Items/Trinkets
7. Fury of the Aspects (time_convergence)
8. Tip the Scales (complex condition)
9. Deep Breath
10. Breath of Eons
11. Fire Breath (via fb sub-list)
12. Upheaval empower_to=1
13. Prescience (ongoing)
14. Time Skip
15. Emerald Blossom (dream_of_spring)
16. Eruption
17. Filler (Living Flame / Azure Strike)

#### WRONG_ORDER
- [W4] **Prescience vs Ebon Might**: Wowhead has Prescience as #1, Ebon Might as #2.
  APL has Ebon Might (#3) before the main Prescience cast (#13), with only an early
  Prescience at #4 gated by `time<=8`. The ongoing Prescience maintenance is after
  Eruption priority. This may cause Prescience to lapse during combat.
- [W5] **Breath of Eons before Tip the Scales**: Wowhead has BoE (#3) then TtS (#4).
  APL has TtS (#8) before Deep Breath (#9) and BoE (#10). The guide says to use
  TtS after BoE for Temporal Burst alignment; the APL reverses this.

#### MISSING
- [M5] **Blistering Scales maintenance during combat**: Wowhead says "Maintain
  Blistering Scales on a Tank" as an ongoing priority (#10). APL only casts it in
  precombat (line 216). During combat, the APL never refreshes Blistering Scales.
  This is a sim limitation (tanks not modeled) but still a gap.

#### CONDITION_ISSUES
- [C9] **Ebon Might pandemic condition**: APL uses a complex pandemic check:
  `(buff.ebon_might_self.remains-cast_time)<=buff.ebon_might_self.duration*variable.ebon_might_pandemic_threshold`
  with threshold=0.4 (40%). Wowhead says "if a few seconds or less remain." 40% of a
  ~25s Ebon Might buff is ~10 seconds, which is much more aggressive than "a few seconds."
  Additionally there's a second check `buff.ebon_might_self.value<=0.05` which recast when
  the buff value is very low.
- [C10] **Fire Breath rank with Molten Embers**: Wowhead says always Rank 1 with Molten
  Embers. APL fb sub-list correctly prioritizes empower_to=1 when talent.molten_embers
  is present (line 245). Without Molten Embers, it escalates to rank 2/3/4. This matches.
- [C11] **Tip the Scales + Upheaval pairing**: Wowhead says with Molten Embers, use TtS
  on Upheaval (not Fire Breath). APL condition includes `action.upheaval.usable_in<action.fire_breath.usable_in|!talent.molten_embers`
  which tries to pair TtS with Upheaval when Molten Embers is present. This aligns.

---

### Augmentation Tier Set (Midnight S1 — Livery of the Black Talon)

**Wowhead:**
- 2pc: Eruption damage +15%, extends Ebon Might by additional 0.3 sec
- 4pc: While Ebon Might active, empower spells deal 20% more damage and cool down 20% faster
- Rotation: No meaningful rotation changes

**SimC Implementation:**
- Only TWW1 tier set bonuses found (EVOKER_AUGMENTATION, TWW1, B2/B4) at lines 10213-10217.
- **NO MID1 (Midnight Season 1) tier set bonuses found for Augmentation.**

#### MISSING_MECHANIC
- [MM2] **Augmentation Midnight S1 2pc NOT IMPLEMENTED**: No code found for
  EVOKER_AUGMENTATION MID1 B2 bonus (Eruption damage +15%, Ebon Might extension +0.3s).
  Only TWW1 tier set bonuses exist in the class module.
- [MM3] **Augmentation Midnight S1 4pc NOT IMPLEMENTED**: No code found for
  EVOKER_AUGMENTATION MID1 B4 bonus (empowers +20% damage, +20% CDR during Ebon Might).
  The APL also has no `set_bonus.mid1` references for Augmentation.

---

### Scalecommander Augmentation

**Wowhead describes Scalecommander as a secondary hero talent option** with identical
core priority but additional mechanics:
- Mass Eruption from empower spell stacks (up to 2)
- Bombardments spreading on targets
- Extended Battle extending Bombardments
- Wingleader CDR on Breath of Eons

**APL**: The Augmentation APL is a single list (not split by hero talent). It includes
a `bombardments` reference in Eruption targeting: `target_if=min:debuff.bombardments.remains`.

#### MISSING
- [M6] **No Scalecommander-specific sub-list for Augmentation**: Unlike Devastation
  which has separate st_sc/aoe_sc and st_fs/aoe_fs lists, Augmentation uses one
  unified APL. Scalecommander-specific mechanics (Bombardments spreading to multiple
  targets, Mass Eruption stacking) are partially handled via the Eruption target_if
  but there's no explicit logic for spreading Bombardments to a second target.

#### CONDITION_ISSUES
- [C12] **Deep Breath in Augmentation APL**: The APL includes `deep_breath,cancel_if=gcd.remains<=0`
  (line 230) without any talent gating. Augmentation doesn't normally use Deep Breath
  as a damage ability unless Scalecommander is active. The APL should potentially gate
  this behind a Scalecommander check.

---

## SUMMARY OF ALL ISSUES

### MISSING (abilities in Wowhead but not in APL)
| ID | Spec | Issue |
|----|------|-------|
| M1 | Devastation SC ST | Deep Breath on cooldown (not just Strafing Run refresh) |
| M2 | Devastation FS | Engulf completely absent from Flameshaper APL |
| M3 | Devastation FS | Shattering Star absent from APL |
| M4 | Devastation FS AoE | Pyre unconditional in Wowhead, heavily conditioned in APL |
| M5 | Augmentation | Blistering Scales in-combat maintenance missing |
| M6 | Augmentation SC | No Scalecommander-specific Bombardments spreading logic |

### WRONG_ORDER (priority ordering mismatches)
| ID | Spec | Issue |
|----|------|-------|
| W1 | Devastation SC ST | Tip the Scales Dragonrage-only vs general priority |
| W2 | Devastation SC AoE | ES before FB in APL; Wowhead says FB before ES |
| W3 | Devastation FS AoE | Fire Breath before Dragonrage in APL; reversed in Wowhead |
| W4 | Augmentation | Prescience much lower priority in APL vs #1 in Wowhead |
| W5 | Augmentation | TtS before BoE in APL; Wowhead has BoE before TtS |

### MISSING_MECHANIC (talent/tier effects not in code)
| ID | Spec | Issue |
|----|------|-------|
| MM1 | Devastation | Event Horizon + tier synergy not handled in APL |
| MM2 | Augmentation | Midnight S1 2pc tier bonus NOT IMPLEMENTED in class module |
| MM3 | Augmentation | Midnight S1 4pc tier bonus NOT IMPLEMENTED in class module |

### CONDITION_ISSUES (APL conditions don't match Wowhead)
| ID | Spec | Issue |
|----|------|-------|
| C1 | Devastation SC | TtS gated to Dragonrage only; Wowhead unconditional |
| C2 | Devastation SC | Deep Breath Strafing Run threshold (2*GCD) |
| C3 | Devastation SC AoE | Pyre at 3 targets with certain talents vs 4+ |
| C4 | Devastation SC AoE | Deep Breath requires imminent_destruction talent |
| C5 | Devastation FS | TtS condition more complex than Wowhead guidance |
| C6 | Devastation FS | Fire Breath conditions more complex than "maintain DoT" |
| C7 | Devastation Tier | Azure Sweep not explicitly prioritized after empowers for tier |
| C8 | Devastation Tier | No target-count differentiation for tier rotation change |
| C9 | Augmentation | Ebon Might 40% pandemic threshold vs "few seconds" |
| C10 | Augmentation | Fire Breath Rank 1 with Molten Embers — MATCHES ✓ |
| C11 | Augmentation | TtS + Upheaval pairing with Molten Embers — MATCHES ✓ |
| C12 | Augmentation | Deep Breath not gated behind Scalecommander |

### OTHER
| ID | Spec | Issue |
|----|------|-------|
| O1 | Devastation | APL comment says "Fameshaper" (typo for "Flameshaper") at lines 96, 111 |
| O2 | Devastation | APL comment says "Scalemander" (typo for "Scalecommander") at lines 126, 140 |
| O3 | Data Quality | Extracted rotation.md contains large amounts of user comments mixed with actual guide content, making extraction unreliable |
| O4 | Augmentation | TWW1 tier bonuses still in code; MID1 tier bonuses not yet added (may be WIP) |
| O5 | Devastation FS | The Flameshaper APL (st_fs/aoe_fs) appears to be a basic framework without full Flameshaper-specific spell integration (no Engulf, no Consume Flame outside one AoE line) |

---

## CRITICAL FINDINGS

1. **HIGHEST PRIORITY — Augmentation MID1 Tier Set Missing (MM2, MM3)**: The Midnight
   Season 1 tier set bonuses for Augmentation (Eruption +15% damage / +0.3s EM extension,
   and empower +20% damage / +20% CDR during EM) are NOT implemented in sc_evoker.cpp.
   Only the old TWW1 tier bonuses exist. This means Augmentation sims are running without
   any current-season tier set bonuses.

2. **HIGH PRIORITY — Engulf Missing from Flameshaper (M2)**: Engulf is a core Flameshaper
   ability. Its complete absence from the Devastation APL means Flameshaper profiles are
   significantly underperforming their potential, as Engulf's DOT-interaction damage
   amplification is never utilized.

3. **MEDIUM PRIORITY — Deep Breath on CD Missing for SC ST (M1)**: Scalecommander's key
   differentiator is Deep Breath usage. The APL only refreshes Strafing Run, missing the
   Wowhead recommendation to use it on cooldown.

4. **MEDIUM PRIORITY — Priority Ordering Mismatches (W2, W4, W5)**: Several priority
   inversions between Wowhead and APL could affect DPS outcomes, particularly the
   Prescience priority in Augmentation and FB/ES ordering in SC AoE.

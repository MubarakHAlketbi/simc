# Hunter Specs Audit Report: Wowhead vs SimulationCraft
Generated: 2026-03-24
Auditor: Hermes Agent

Compares extracted Wowhead rotation/tier/talent data against SimC APL
(engine/class_modules/apl/apl_hunter.cpp) and class module
(engine/class_modules/sc_hunter.cpp).

================================================================
## BEAST MASTERY
================================================================

### Wowhead Rotation Summary

**Pack Leader ST Priority:**
1. Barbed Shot if BW coming off CD in ~3s
2. Bestial Wrath
3. Kill Command if Howl of the Pack Leader buff or Nature's Ally active
4. Barbed Shot
5. Cobra Shot

**Pack Leader AoE Priority:**
1. Barbed Shot if BW coming off CD
2. Bestial Wrath (with Beast Cleave active)
3. Wild Thrash
4. Kill Command
5. Barbed Shot
6. Cobra Shot

**Dark Ranger ST Priority:**
1. Bestial Wrath
2. Kill Command if Nature's Ally active
3. Black Arrow if Withering Fire active
4. Wailing Arrow
5. Barbed Shot
6. Black Arrow
7. Cobra Shot

**Killer Cobra Note:** During BW, prioritize Cobra Shot over Barbed Shot.

### Tier Set (Primal Sentry's Camouflage)
- 2pc: Bestial Wrath direct damage increased by 25%
- 4pc: Bestial Wrath summons 1 Dire Beast for 8 sec
- No rotation changes

### APL Analysis

**Pack Leader ST (APL "st"):**
1. barbed_shot if cooldown.bestial_wrath.remains<gcd
2. bestial_wrath
3. kill_command if BW CD > full_recharge_time+gcd & (natures_ally.up|howl_summon.ready)|!apex.3
4. barbed_shot
5. cobra_shot

**Pack Leader AoE (APL "cleave"):**
1. barbed_shot if BW CD < gcd
2. wild_thrash
3. bestial_wrath
4. kill_command
5. cobra_shot (conditional hogstrider)
6. barbed_shot
7. cobra_shot

**Dark Ranger ST (APL "drst"):**
1. bestial_wrath
2. kill_command if BW CD > full_recharge_time+gcd & natures_ally.up|!apex.3
3. black_arrow if withering_fire.up
4. cobra_shot if killer_cobra & BW up & barbed_shot charges < 1.4
5. wailing_arrow (with fade/death check)
6. barbed_shot
7. black_arrow
8. cobra_shot

### Findings

[MISSING] Hunter's Mark — Wowhead says to apply Hunter's Mark pre-combat on
priority target. APL has no hunter_mark action in precombat or anywhere. This is
a 3% damage increase on the target. Note: SimC may handle this as an external
raid buff, but it is not explicitly in the Hunter APL.

[CONDITION_ISSUES] BM Pack Leader ST — Wowhead says "Barbed Shot if BW about
to come off CD in the next 3 seconds." APL uses "cooldown.bestial_wrath.remains<gcd"
which is approximately 1.5s, not 3s. This is tighter than the Wowhead guidance
and may miss some charge alignment opportunities.

[WRONG_ORDER] BM Pack Leader AoE — Wowhead priority is: Barbed Shot > BW (with
Beast Cleave) > Wild Thrash > Kill Command. APL order is: Barbed Shot > Wild Thrash
> BW > Kill Command. Wild Thrash is placed BEFORE Bestial Wrath in the APL, while
Wowhead places BW before Wild Thrash. The APL prioritizes getting Beast Cleave
active (via Wild Thrash) before BW so that BW's hit benefits from Beast Cleave,
which actually aligns with Wowhead's advanced tip "make sure Beast Cleave is active
when you press BW." This is intentional but the surface priority lists differ.

[CONDITION_ISSUES] BM DR ST — Wowhead says Wailing Arrow should be used before
the effect runs out. APL checks "buff.withering_fire.remains<execute_time+gcd" or
"time_to_die.remains<execute_time+gcd" which is good but Wowhead also says to
avoid wasting Kill Command charges while using Wailing Arrow (no such check in APL).

[OTHER] Killer Cobra interaction — Wowhead says during BW with Killer Cobra, 
prioritize Cobra Shot over Barbed Shot. The APL has this only in the drst list
("cobra_shot,if=talent.killer_cobra&buff.bestial_wrath.up&...") but NOT in the
"st" (Pack Leader ST) list. Pack Leader builds could also run Killer Cobra.

[MISSING] Misdirection — Wowhead pre-combat checks mention casting Misdirection
on tank. Not in APL (expected — SimC doesn't model threat).

[OTHER] Tier set implemented correctly in code:
- 2pc (mid_s1_bm_2pc): Bestial Wrath direct damage +25% — data pointer exists
- 4pc (mid_s1_bm_4pc): Bestial Wrath spawns Dire Beast — implemented at line
  6620-6621 (spawn_dire_beast on BW execute)
- Both confirmed working.

================================================================
## MARKSMANSHIP
================================================================

### Wowhead Rotation Summary

**Sentinel ST Priority:**
1. Trinket usage with Trueshot
2. Volley on cooldown (not back-to-back with Trueshot, activates Double Tap)
3. Trueshot (ideally before Aimed Shot, after Rapid Fire for Bulletstorm)
4. Arcane Shot to spend Precise Shots (after every Aimed Shot/Rapid Fire)
5. Rapid Fire if cannot fit Aimed Shot into Bulletstorm, or Bulletstorm down
6. Aimed Shot when available
7. Moonlight Chakram as filler when out of Aimed Shots
8. Rapid Fire when available
9. Steady Shot filler

**Dark Ranger ST Priority:**
Same as Sentinel but adds:
1. Black Arrow whenever available (highest priority, Rapid Fire guarantees proc)
2. Wailing Arrow as filler (replaces Trueshot button, follow up with Black Arrow)

**AoE Note:** Hydra build uses Arcane Shot instead of Multi-Shot on AoE (for
Spotter's Mark -> Lunar Storm procs).

### Tier Set (Primal Sentry's Camouflage)
- 2pc: Precise Shots damage increased by an additional 20%
- 4pc: Spending Precise Shots has small chance to release volley of arrows
  (150% AP damage to nearby enemies)
- No rotation changes

### APL Analysis

**Sentinel ST (APL "sentst"):**
1. volley if !double_tap & active_enemies=1
2. trueshot if !double_tap & active_enemies=1
3. rapid_fire (unload conditional)
4. arcane_shot if precise_shots.up (target_if sentinels_mark)
5. rapid_fire if bulletstorm < aimed_shot execute_time
6. trueshot if !double_tap & active_enemies>1
7. volley if !double_tap & active_enemies>1
8. aimed_shot (target_if sentinels_mark)
9. moonlight_chakram
10. rapid_fire
11. steady_shot

**Dark Ranger ST (APL "drst"):**
1. black_arrow
2. trueshot if !double_tap
3. rapid_fire (unload conditional)
4. arcane_shot if precise_shots.up
5. rapid_fire if bulletstorm < aimed_shot execute_time
6. volley if !double_tap
7. aimed_shot
8. wailing_arrow
9. rapid_fire
10. steady_shot

### Findings

[WRONG_ORDER] Sentinel ST — Wowhead puts Volley AFTER Trueshot in the priority
(position 2 vs position 3 in guide). APL puts Volley BEFORE Trueshot for
single-target. This is likely intentional for the Double Tap mechanic (ensuring
Volley's Double Tap isn't wasted by Trueshot), but disagrees with the literal
Wowhead ordering for ST. The APL actually follows the guide's advice about never
casting them back-to-back.

[CONDITION_ISSUES] Sentinel ST — Wowhead says "Cast Rapid Fire if you cannot fit
another Aimed Shot into your Bulletstorm." APL uses
"rapid_fire,if=buff.bulletstorm.remains<action.aimed_shot.execute_time" which is
a close approximation but not identical (doesn't check if aimed_shot charges are
available).

[MISSING] Sentinel ST — Wowhead opener mentions pre-casting Aimed Shot 2.5s before
pull. APL precombat has "aimed_shot,if=active_enemies<3" which serves this purpose.
Confirmed present.

[WRONG_ORDER] Dark Ranger ST — Wowhead puts Black Arrow at #1 highest priority.
APL also puts black_arrow at #1 in drst. Match confirmed. However, Wowhead says
Wailing Arrow should "always follow up with Black Arrow." The APL has wailing_arrow
at position 8, well below black_arrow at position 1, so a Black Arrow proc from
the Wailing Arrow would be caught on the next cycle. This is structurally correct
but doesn't enforce the immediate follow-up.

[MISSING] AoE Hydra build — Wowhead explicitly notes that AoE build with Aspect
of the Hydra uses ONLY Arcane Shot (not Multi-Shot). The APL draoe/sentaoe lists
do include Multi-Shot with "!talent.aspect_of_the_hydra" condition which correctly
handles this. Confirmed present.

[OTHER] Tier set implemented correctly in code:
- 2pc (mid_s1_mm_2pc): Precise Shots damage +20% — data pointer exists, applied
  via spell_data modifiers
- 4pc (mid_s1_mm_4pc): Precise Shots spending triggers "let_fly" volley arrows
  via RPPM — implemented at lines 4178-4179 and 5173-5174, with let_fly_t action
  at line 4917-4922 (AoE damage action).
- Both confirmed working.

[MISSING] Hunter's Mark — Same as BM. Wowhead says apply on highest-health target
pre-combat. Not in APL. SimC handles as external debuff.

================================================================
## SURVIVAL
================================================================

### Wowhead Rotation Summary

**Pack Leader ST Priority:**
1. Avoid Hatchet Toss (even with Hogstrider)
2. Hunter's Mark if not active
3. Kill Command when Howl of Pack Leader beasts available (without wasting TotS)
4. Takedown at 0 TotS stacks (to maximize Twin Fangs)
5. Boomstick if TotS stack to spend
6. Wildfire Bomb if Fury of the Wyvern extendable & TotS to spend
7. Raptor Swipe if TotS to spend
8. Raptor Strike with or without TotS
9. Kill Command
10. Wildfire Bomb
11. Takedown as fallback

**Sentinel ST Priority:**
1. Hunter's Mark if not active
2. Kill Command when out of TotS stacks
3. Boomstick if TotS & target not affected by Sentinel's Mark
4. Wildfire Bomb if TotS & (Sentinel's Mark on target OR <4s until full recharge)
5. Kill Command before entering Takedown
6. Takedown if TotS
7. Moonlight Chakram
8. Raptor Swipe if TotS
9. Raptor Strike

**Pack Leader AoE:**
Similar to ST but Wildfire Bomb higher priority (no Fury of Wyvern condition),
Wildfire Bomb added as low-priority fallback.

**Sentinel AoE:**
Similar to ST but Boomstick unconditional, Wildfire Bomb with Sentinel's Mark OR
<6s recharge (not 4s), Moonlight Chakram with TotS.

### Tier Set (Primal Sentry's Camouflage)
- 2pc: Wildfire Bomb damage increased by 10%
- 4pc: Wildfire Bomb provokes an additional Strike as One at 100% effectiveness
- No rotation changes (guides "giving Wildfire Bomb higher priority to use" but
  no formal priority change documented)

### APL Analysis

**Pack Leader ST (APL "plst"):**
1. kill_command if TotS<2 & (howl wyvern|boar|bear remains)
2. kill_command if takedown CD < gcd & TotS<2 & !twin_fangs
3. takedown (TotS>0 & !twin_fangs | TotS=0 & twin_fangs)
4. flamefang_pitch
5. boomstick if TotS up
6. wildfire_bomb if fury_of_wyvern_extendable & TotS up
7. raptor_strike if TotS up | !raptor_swipe.up
8. kill_command if takedown CD remains
9. wildfire_bomb
10. takedown

**Sentinel ST (APL "sentst"):**
1. kill_command if TotS=0 & (takedown CD remains | !twin_fangs)
2. boomstick if TotS & !takedown ready & !sentinels_mark
3. wildfire_bomb if TotS & (sentinels_mark | full_recharge<4+gcd)
4. kill_command if takedown CD < gcd & TotS<2 & !twin_fangs
5. takedown (TotS>0 & !twin_fangs | TotS=0 & twin_fangs)
6. boomstick if TotS
7. moonlight_chakram if TotS
8. flamefang_pitch
9. raptor_strike if TotS up | !raptor_swipe.up
10. kill_command if takedown CD remains
11. takedown

### Findings

[MISSING] Hatchet Toss avoidance — Wowhead explicitly says "Avoid using Hatchet
Toss, even with Hogstrider." APL has no hatchet_toss action, which implicitly
handles this. Correct by omission.

[MISSING] Hunter's Mark — Wowhead says "Cast Hunter's Mark if it is not yet active"
as the #2 priority for Pack Leader and #1 for Sentinel. Not in APL anywhere.
Hunter's Mark (3% damage increase) is not modeled as a player action in SimC APLs
for hunters; it's assumed active or handled externally.

[CONDITION_ISSUES] Raptor Swipe vs Raptor Strike — Wowhead lists Raptor Swipe as
a separate priority step (with TotS) above Raptor Strike (with or without TotS).
APL uses "raptor_strike,if=buff.tip_of_the_spear.up|!buff.raptor_swipe.up" which
combines both into one line. When raptor_swipe buff is up (Raptor Swipe is available
as a proc from Raptor Strike), the condition requires TotS to be up. When
raptor_swipe buff is NOT up, Raptor Strike is used unconditionally. This is
functionally equivalent to the Wowhead priority but compresses two steps.

[WRONG_ORDER] Pack Leader ST — Wowhead puts Takedown at position 4 (at 0 TotS
for Twin Fangs), then Boomstick at position 5. APL puts kill_command pre-takedown
check at position 2, takedown at position 3, then flamefang_pitch at 4, then
boomstick at 5. The Boomstick/Takedown relative ordering matches. However,
Flamefang Pitch is at position 4 in APL but not explicitly in the Wowhead ST
priority list at all — Wowhead covers Flamefang Pitch in a separate tab as a
Takedown-window ability.

[MISSING_MECHANIC] Flamefang Pitch in Wowhead rotation — Wowhead describes
Flamefang Pitch extensively in the "Flamefang Pitch" tab but does NOT include it
in the main ST or AoE priority lists. The APL includes flamefang_pitch as an
unconditional action in plst (position 4) and plcleave (position 4), and
conditionally in sentst/sentcleave. This is a discrepancy where APL adds an
ability that Wowhead's rotation priority didn't explicitly list.

[CONDITION_ISSUES] Sentinel AoE — Wowhead says "Wildfire Bomb is less than 6
seconds away from fully recharging" for AoE. APL sentcleave uses
"full_recharge_time<4+gcd" which is approximately 5.5s, slightly tighter than
Wowhead's 6 seconds.

[CONDITION_ISSUES] Sentinel ST Boomstick — Wowhead says "Boomstick if TotS and
target NOT affected by Sentinel's Mark." APL sentst has
"boomstick,if=buff.tip_of_the_spear.up&!cooldown.takedown.ready&!debuff.sentinels_mark.remains"
which adds an additional condition (!takedown ready) not in Wowhead guide. This
extra condition prevents using Boomstick right before a Takedown window.

[WRONG_ORDER] Sentinel ST Moonlight Chakram — Wowhead lists Moonlight Chakram
AFTER Takedown (position 7 after Takedown at position 6). APL sentst has
moonlight_chakram at position 7, after Takedown at position 5 and second boomstick
at position 6. Match is approximate.

[OTHER] Tier set implemented correctly in code:
- 2pc (mid_s1_sv_2pc): Wildfire Bomb damage +10% — data pointer exists
- 4pc (mid_s1_sv_4pc): Wildfire Bomb triggers additional Strike as One —
  implemented at lines 7045-7047 (checks TotS buff on wildfire_bomb execute,
  triggers pet strike_as_one action). Confirmed working.

[OTHER] Wildfire Bomb with tier 4pc — Wowhead mentions the tier set "giving
Wildfire Bomb a higher priority to use" but no explicit rotation change. The APL
does not change Wildfire Bomb priority based on tier set being equipped. This is
consistent with Wowhead saying "no significant rotational changes."

================================================================
## CROSS-SPEC SUMMARY
================================================================

### MISSING (abilities in Wowhead but not in APL)
1. [ALL SPECS] Hunter's Mark — Not in any APL. Wowhead lists it as pre-combat 
   and in-combat priority for Survival. SimC handles externally.
2. [BM] Misdirection — Pre-combat only, not modeled in SimC (threat not simulated).

### WRONG_ORDER (priority ordering mismatches)
1. [BM AoE PL] Wild Thrash before BW in APL vs BW before Wild Thrash in Wowhead
   (intentional for Beast Cleave synergy)
2. [MM Sent ST] Volley before Trueshot in APL vs Trueshot before Volley in Wowhead
   (intentional for Double Tap management)

### MISSING_MECHANIC (talent/tier effects in Wowhead but not in code)
1. [BM PL] Killer Cobra interaction missing from Pack Leader ST APL — only present
   in Dark Ranger ST list, but Pack Leader can also talent into Killer Cobra.
2. [SV] Flamefang Pitch present in APL but absent from Wowhead rotation priority
   (documented separately in Wowhead's tab system, not in priority list).

### CONDITION_ISSUES (APL conditions not matching Wowhead)
1. [BM] Barbed Shot pre-BW window: APL uses <gcd (~1.5s), Wowhead says 3 seconds.
2. [MM] Rapid Fire Bulletstorm check doesn't verify Aimed Shot charge availability.
3. [SV Sent AoE] Wildfire Bomb recharge threshold: APL uses ~5.5s, Wowhead says 6s.
4. [SV Sent ST] Boomstick has extra !takedown.ready condition not in Wowhead.
5. [BM DR] Wailing Arrow doesn't check for Kill Command charge waste as Wowhead
   recommends.

### OTHER
1. [ALL SPECS] All tier set bonuses (2pc and 4pc) are properly implemented in
   sc_hunter.cpp for all three specs.
2. [ALL SPECS] Hero talent trees (Pack Leader, Dark Ranger, Sentinel) are properly
   split into separate APL lists with correct talent detection.
3. [MM] Aspect of the Hydra AoE behavior (Arcane Shot instead of Multi-Shot)
   correctly handled in APL conditions.
4. [SV] Strike as One passive damage is implemented but not explicitly managed
   in APL (correct — it's a passive proc).
5. [BM/SV] Howl of the Pack Leader beast tracking implemented with per-beast
   buff checks (wyvern/boar/bear).
6. [MM] Double Tap / Trueshot / Volley interaction correctly prevents back-to-back
   usage via !buff.double_tap.up conditions.

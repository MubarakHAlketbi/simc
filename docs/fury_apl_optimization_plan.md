# Warrior Fury — APL Deep Optimization Plan

Based on 10k-iter sim reports with optimized talent builds (2026-03-28).

---

## Sim Data Summary

### Patchwerk (ST) — 92,570 DPS

| Action | Damage | % | Executes | Notes |
|--------|-------:|--:|--------:|-------|
| rampage | 7,463,493 | 26.9% | 104.5 | Top damage, 100% enrage uptime confirms good rage mgmt |
| bloodthirst | 3,893,922 | 14.0% | 60.6 | Second highest, ~20/min |
| crushing_blow | 3,778,397 | 13.6% | 47.1 | Third — high value in ST |
| thunder_blast | 2,404,151 | 8.7% | 33.2 | Mountain Thane signature |
| auto_attack_mh | 2,245,473 | 8.1% | 207.5 | |
| bloodbath | 1,771,615 | 6.4% | 14.7 | |
| odyns_fury | 1,660,701 | 6.0% | 11.7 | |
| raging_blow | 1,038,536 | 3.7% | 24.4 | Low priority filler |
| rend_dot | 761,869 | 2.7% | 36.7 | Maintenance DoT |
| execute | 740,546 | 2.7% | 15.1 | Execute phase only |

Key buffs: enrage 100%, avatar 64.5%, recklessness 42.6%, bloodcraze 46.2%, frenzy 96.9%, thunder_blast 56.7%, surge_of_adrenaline 36.9%

APM: 66.8 | Rage spent: 6,494

### HecticAddCleave (AoE) — 216,045 DPS

| Action | Damage | % | Executes | Notes |
|--------|-------:|--:|--------:|-------|
| rampage | 15,661,496 | 24.4% | 104.7 | Still top, cleaves via whirlwind buff |
| thunder_blast | 11,401,908 | 17.7% | 39.4 | Huge AoE — much higher % than ST |
| thunder_clap | 8,455,258 | 13.2% | 26.1 | Major AoE action |
| bloodthirst | 6,912,207 | 10.8% | 52.5 | |
| bloodbath | 6,240,407 | 9.7% | 28.9 | Higher value in AoE |
| odyns_fury | 5,372,199 | 8.4% | 12.2 | |
| rend_dot | 2,438,974 | 3.8% | 303.2 | Massive spread via cleave |
| crushing_blow | 972,713 | 1.5% | 14.9 | Much lower in AoE vs ST |
| raging_blow | 584,329 | 0.9% | 9.7 | Barely used |

Key buffs: enrage 99.7%, avatar 69.3%, whirlwind 71.5%, recklessness 42.6%, thunder_blast 35.9%

APM: 69.9 | Rage spent: 6,511

---

## Current APL Analysis — Issues Found

### Issue 1: thane ST — Bloodthirst too low, no Bladestorm

**Current `thane` (ST) priority:**
1. recklessness
2. avatar
3. rampage (enrage refresh / rage cap)
4. bloodthirst (if not enraged)
5. crushing_blow
6. odyns_fury
7. thunder_blast (2 stacks)
8. bloodbath
9. rampage (during recklessness)
10. thunder_blast (during avatar)
11. bloodthirst ← unconditional BT is here at #11
12. rampage
13. execute
14. thunder_blast ← loose TB
15. raging_blow
16. thunder_clap
17. whirlwind

**Problem:** Bloodthirst at #11 (behind bloodbath, rampage during reck, thunder_blast during avatar) means it fires ~60 times. But bloodthirst does 14% of total damage — it should be higher. In the Slayer list, bloodthirst is at #4 (if not enraged) and #12 (unconditional). The Thane list has the same pattern but crushing_blow and thunder_blast steal priority.

**Potential fix:** Move unconditional bloodthirst above thunder_blast(avatar) to ensure rage generation stays strong. Bloodthirst generates rage AND does 14% damage.

### Issue 2: thane ST — No Bladestorm action

The Slayer ST list has:
```
bladestorm,if=(buff.enrage.up&talent.deft_experience|buff.enrage.remains>1)&(buff.recklessness.up|cooldown.recklessness.remains>30)
```

The Thane ST list has NO bladestorm. The optimized talent build includes Avatar (not Bladestorm choice), but Bladestorm is a separate talent in the Thane path and may still be available if talented. Need to verify if the talent build has bladestorm — if it does, it's missing from the APL.

### Issue 3: thane_aoe — Rampage threshold too high

**Current:** `rampage,if=buff.enrage.remains<gcd|rage>=100`

The APL optimizer already found that `rage>=80` is better (the +0.44% mutation from Batch 3). The current APL still uses 100. This should be applied.

### Issue 4: thane_aoe — Crushing Blow too low

In AoE, crushing_blow is at position #13 (after thunder_clap, execute, rampage). But in ST it's at position #5. Since crushing_blow does only 1.5% of AoE damage (vs 13.6% in ST), the low priority seems correct for AoE. However, at low target counts (2-3), it may still be valuable.

**Potential fix:** Add `crushing_blow,if=active_enemies<=3` higher in the thane_aoe list.

### Issue 5: Rend not in thane ST priority

The Slayer ST list has `rend,if=dot.rend.duration<6` at position #15. The Thane ST list has NO rend action. But the sim shows rend_dot does 2.7% of ST damage (761k). If rend is talented in the optimized build, it should be in the priority.

### Issue 6: Execute position in thane ST

Current: `execute,if=target.health.pct<20|buff.sudden_death.up` at position #13.

Execute does 2.7% damage. With sudden_death uptime at 28.8%, there are frequent procs. Execute should fire higher during sudden_death procs. The Wowhead guide puts Execute above Bloodthirst in the ST priority during cooldowns.

**Potential fix:** Add `execute,if=buff.sudden_death.up` earlier in the thane list (around position #7-8, after bloodbath).

### Issue 7: Wrecking Throw missing from thane lists

The Slayer ST list has `wrecking_throw` at position #14. Thane lists don't have it. It's a free damage action (off-GCD or very low cost).

---

## Proposed APL Changes

### For Thane ST (`actions.thane`):

```
# Current:                              # Proposed:
1. recklessness                         1. recklessness
2. avatar                               2. avatar
3. rampage (enrage/cap)                 3. rampage (enrage/cap)
4. bloodthirst (!enrage)                4. bloodthirst (!enrage)
5. crushing_blow                        5. crushing_blow
6. odyns_fury                           6. odyns_fury
7. thunder_blast (2 stacks)             7. execute (sudden_death proc)     ← NEW
8. bloodbath                            8. thunder_blast (2 stacks)
9. rampage (recklessness)               9. bloodbath
10. thunder_blast (avatar)              10. rampage (recklessness)
11. bloodthirst                         11. bloodthirst                    ← moved up from #11
12. rampage                             12. thunder_blast (avatar)
13. execute (hp<20|sudden_death)        13. rampage
14. thunder_blast                       14. execute (hp<20)                ← split from sudden_death
15. raging_blow                         15. wrecking_throw                 ← NEW
16. thunder_clap                        16. rend (if dot expiring)         ← NEW
17. whirlwind                           17. thunder_blast
                                        18. raging_blow
                                        19. thunder_clap
                                        20. whirlwind
```

### For Thane AoE (`actions.thane_aoe`):

```
# Change only:
# Line 6: rampage threshold 100 -> 80 (confirmed +0.44%)
rampage,if=buff.enrage.remains<gcd|rage>=80

# Add after bloodthirst (line 9), before thunder_blast:
crushing_blow,if=active_enemies<=3

# Add execute for sudden_death procs higher:
execute,if=buff.sudden_death.up  (move above thunder_clap)
```

---

## Testing Plan

Each change should be tested independently at 10k iterations to measure impact:

| # | Change | Test Command Suffix | Expected |
|---|--------|-------------------|----------|
| 1 | thane: execute(sudden_death) at #7 | `actions.thane=/.../execute,if=buff.sudden_death.up/...` | +0.1-0.3% |
| 2 | thane: wrecking_throw + rend added | Add at #15-16 | +0.1-0.2% |
| 3 | thane_aoe: rampage rage>=80 | Already confirmed | +0.44% |
| 4 | thane_aoe: crushing_blow for <=3 | Add conditional | +0.1% for HAC |
| 5 | All combined PW | Full proposed thane list | Target +0.5% |
| 6 | All combined HAC | Full proposed thane_aoe list | Target +0.5% |

Use the APL optimizer for automated testing: `python3 scripts/apl_optimizer.py warrior_fury`

The optimizer's mutation engine should catch threshold sweeps (#3) and position changes (#1, #2) automatically. The manual changes above inform which mutations to prioritize.

---

## Decision: Manual vs Automated

The APL optimizer already runs on warrior_fury. The PW run found +0.00% (converged). The HAC run found +0.44% (threshold sweep).

The optimizer's mutation operators are:
- Adjacent swap (M1): would catch #1 (execute position)
- Threshold sweep (M4): already caught #3 (rampage rage)
- Promotion (M5): not yet implemented but would catch #2
- Routing (M6): not applicable here

**Recommendation:** Make the manual changes above, then re-run the APL optimizer on the modified APL to see if further automated improvements emerge. The manual changes add new actions (wrecking_throw, rend, conditional crushing_blow) that the optimizer can't discover — it can only reorder/adjust existing actions.

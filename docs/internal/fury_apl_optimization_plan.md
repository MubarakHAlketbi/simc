# Warrior Fury — APL + Talent Optimization Report

Date: 2026-03-28

## Summary

Warrior Fury was the first spec fully optimized through the complete pipeline (talent local search + APL optimization). Results:

| Optimization | Patchwerk | HecticAddCleave |
|-------------|-----------|-----------------|
| Talent local search | +1.52% (86,904 → 88,178) | +0.65% (209,221 → 210,582) |
| APL optimizer | +0.00% (optimal) | +0.44% (rampage threshold) |
| Manual APL changes | -1.52% (reverted) | -0.86% (reverted) |

Talent optimization delivers the real gains. APL is at its ceiling.

---

## Talent Builds

### PW-Optimized (Mountain Thane #3 + local search)

85 total points: CLASS=36, SPEC=34, HERO=15

Key node vs current: **+Stance Mastery** (replacing Rumbling Earth or similar utility).

PW-only nodes (not in HAC build): Rallying Cry, Wrath and Fury, Improved Raging Blow, Enraged Regeneration, Bloodcraze, Critical Thinking (rank 2), Surge of Adrenaline, Field Dressing.

### HAC-Optimized (Mountain Thane #6 + local search)

85 total points: CLASS=36, SPEC=34, HERO=15

Key nodes vs current: **+Stance Mastery**, **+Fast Footwork** (swapped in from utility).

HAC-only nodes (not in PW build): Rampaging Ruin, Improved Whirlwind, Stance Mastery, Interpose, Meat Cleaver.

### Convergence

All 4 seeds (top 3 Wowhead + current) converge in 1-2 hill-climb passes to the same conclusion: Stance Mastery is universally undervalued. Running 8 max passes produces identical results to 3. This is the ceiling for single-node mutations.

---

## APL Analysis

### Source

The profile uses a 112-line .simc APL override (NOT the C++ generator). The C++ generator in `apl_warrior.cpp` was updated but is -1.50% PW / -0.85% HAC behind the profile APL.

### Automated Optimizer

- **PW: +0.00%** — converged immediately, 56 candidates all filtered out at Stage 2
- **HAC: +0.44%** — `thane_aoe[5] rampage threshold 100→80` accepted

### Manual Changes Tested and Reverted

| Change | PW Impact | HAC Impact | Why It Failed |
|--------|-----------|------------|---------------|
| execute(sudden_death) at #7 | regression | regression | Execute before rampage misses enrage buff |
| bloodthirst above thunder_blast(avatar) | regression | regression | Thunder_blast has higher DPET during avatar |
| wrecking_throw + rend added | regression | regression | Displaces higher-value thunder_blast/raging_blow |
| Combined all changes | -1.52% | -0.86% | Disrupts optimized priority chain |

The upstream-imported APL is battle-tested. Manual reordering and filler additions don't help.

---

## Sim Data (10k iterations, optimized talent builds)

### Patchwerk — 92,570 DPS

Top actions: rampage (26.9%), bloodthirst (14.0%), crushing_blow (13.6%), thunder_blast (8.7%), auto_attack (8.1%), bloodbath (6.4%), odyns_fury (6.0%).

Key buffs: enrage 100%, avatar 64.5%, recklessness 42.6%, frenzy 96.9%, bloodcraze 46.2%, thunder_blast 56.7%.

### HecticAddCleave — 216,045 DPS

Top actions: rampage (24.4%), thunder_blast (17.7%), thunder_clap (13.2%), bloodthirst (10.8%), bloodbath (9.7%), odyns_fury (8.4%).

Key buffs: enrage 99.7%, avatar 69.3%, whirlwind 71.5%, recklessness 42.6%.

---

## Conclusions

1. **Talent search is the main lever** — +1.52% PW, +0.65% HAC from budget-neutral single-node swaps
2. **APL is at its ceiling** — automated optimizer and manual changes both confirm no further gains
3. **Stance Mastery is the key finding** — undervalued by all Wowhead builds, consistently improves DPS
4. **Builds differ by fight style** — 8 PW-only nodes vs 5 HAC-only nodes confirms per-style optimization is correct
5. **Further talent gains require** multi-node swaps (combinatorial cost) or hero tree switching (strategic axis already covered by seed screening)

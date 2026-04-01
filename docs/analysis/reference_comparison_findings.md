# Lessons Learned — Reference Profile Comparison

Source: simulationcraft.org/reports/MID1_Raid.html  
Method: Same gear, same engine (ours). Only substituted their talent string (ref_T),
their APL (ref_A), or both (ref_TA). DPS delta is purely from the substituted component.  
Date: 2026-04-01

---

## Summary of Findings

### What we compared
- 47 spec pairs (our PW profile vs reference profile.simc from SimC.org)
- ref_T = our APL + their talents on our engine
- ref_A = our talents + their APL on our engine
- ref_TA = their talents + their APL on our engine
- engine_div = (our_dps - ref_reported) / ref_reported — detects engine bugs

### Outcome categories

| Category | Count |
|----------|-------|
| Our profile is best (ours wins) | 6 specs |
| Ref talents clearly better (>5%) | 9 specs — optimizer failure |
| Ref APL clearly better (>5%) | 3 specs — APL bug/gap |
| Combined talent+APL explains gap | 5 specs |
| Residual engine divergence (>10%) | 4 specs — C++ bugs |

---

## CRITICAL: APL Bugs Found

### 1. Warlock Affliction Hellcaller — +17.23% from ref APL
**This is the most important finding in the entire comparison.**

- Our DPS: 84,563
- Their APL on our engine: 99,130 (+17.23%)
- Reported: 99,300
- Talent strings: IDENTICAL (same string, talent diff = N/A)
- APL diff: ours=94 lines, ref=93 lines, shared=93, only_ours=1, only_ref=0

We have exactly 1 APL line they don't have. That 1 line is responsible for a -17%
DPS loss. This is almost certainly an incorrect action we added (wrong condition,
wrong sub-list, or conflicting with core DoT logic) that breaks the rotation.

**Action required**: Diff our Hellcaller APL against reference, identify the extra
line, sim with and without it, remove if it's the cause.

### 2. Warlock Affliction Soul Harvester — +8.74% from ref APL
- Our DPS: 94,536 → their APL: 102,795 (+8.74%)
- APL diff: ours=95, ref=93, shared=72, only_ours=23, only_ref=21
- 23 lines we have they don't, 21 they have we don't — significant structural divergence
- Their ref_TA (talents+APL) gets to 102,827 — matches reported 104,004 closely
- **Action**: Port their APL structure for Soul Harvester sub-list. Our optimizer
  was working from a flawed base — the talent optimizer found good builds but the
  APL underneath was already wrong.

### 3. Shaman Enhancement Stormbringer — APL worth +9.25%
- ref_A: +9.25% (our talents + their APL)
- ref_TA: +12.43% (both substituted) → 83,420 vs reported 91,989
- Remaining 10% gap after both subs = residual engine divergence (proc chain bug likely)
- APL diff: shared=105/108 — very close APLs, but the 3 different lines cause +9%
- **Action**: Investigate which 3 APL lines drive the gain; likely an emergency
  resource dump or buff consumer missing from ours.

---

## Talent Optimizer Failures (ref_T > ours by >5%)

These specs need re-investigation. The optimizer either got stuck in a local minimum
or the talent validator rejected valid builds.

| Spec | ref_T gain | Notes |
|------|------------|-------|
| DH Vengeance Annihilator | +20.96% | Massive. Their build: CUkAAAA...hZkZmZGD vs ours: CUkAAAA...ZmZkZmZY |
| Paladin Prot Lightsmith | +14.88% | Their build completely different. Our optimizer may have been given a bad seed. |
| Hunter Beast Mastery | +11.47% | APL is IDENTICAL (shared=59/59). Pure talent failure. Optimizer stuck. |
| DH Vengeance Aldrachi Reaver | +10.75% | Same ref talent string as Annihilator (different hero but same base) |
| DH Devourer Void-Scarred | +8.45% | Same ref build as Annihilator base tree |
| Warlock Demo Soul Harvester | +8.85% | Our string has long prefix `CoQAy0jxIDofkwJmoH7WhvESo...` — looks corrupted/non-standard |
| Warlock Dest Hellcaller | +7.34% | Different build priorities |
| Shaman Enh Stormbringer | +6.97% | Combined with APL gives +12.43% |
| Paladin Protection | +5.25% | Base talent tree, not lightsmith variant |

**Critical observation — Warlock Demo**: Our talent string starts with
`CoQAy0jxIDofkwJmoH7WhvES...` which is abnormal (non-zero bytes in positions that
should encode the class tree header). This looks like a corrupted talent string
possibly from a snapshot or wrong encoding. Reference has clean `CoQAAAAAAAAA...`.
This is likely a talent codec bug in our tree_codec_bridge.py.

**Common pattern for Vengeance and Prot Paladin**: Both specs use the SAME
reference talent string. This means the optimizer explored both from the same base
but converged to a different local minimum. The reference build is validated in-game
(it's what SimC.org uses for their profiles), so our optimizer's gate validation
may have incorrectly blocked the reference path.

---

## Our Optimizer Succeeded (ours beats ref_T by >2%)

These validate that our optimizer is working correctly on these specs:

| Spec | Our lead | Notes |
|------|----------|-------|
| Paladin Retribution Herald | +6.78% | Our build significantly better |
| Monk Brewmaster | +9.39% talents | BUT ref_A +3.32% and ref_TA +15.59% — talent optimizer won, APL has gaps |
| DK Unholy San'layn | +4.06% | Our talents better than reference |
| Evoker Devastation FS | +3.62% | Our build beats theirs |
| Mage Arcane Sunfury | +8.80% | Clear win; they use Spellslinger talents for Sunfury profile |
| Monk Windwalker Conduit | +2.24% | Our optimization working |

---

## Engine Divergence — C++ Bugs Likely

Specs where even ref_TA on our engine can't reach the reported DPS.
These gaps point to missing implementations or proc chain bugs in our C++ modules.

| Spec | Our engine | Reported | Gap | ref_TA closes gap? |
|------|-----------|----------|-----|-------------------|
| Warlock Demo | 91,072 | 120,997 | -25% | ref_TA=100,042 — still -17% gap |
| DK Blood San'layn | 46,578 | 59,890 | -22% | ref_A=47,085 — still -21% gap |
| Paladin Prot Lightsmith | 42,967 | 55,406 | -22% | ref_T=49,359 — still -11% gap |
| Hunter Beast Mastery | 97,614 | 113,980 | -14% | ref_TA=108,894 — still -4% gap |
| Warlock Dest Hellcaller | 94,553 | 109,082 | -13% | ref_TA=101,505 — still -7% gap |

**Warlock Demo** is the worst at -17% residual after full substitution. The demo
warlock engine likely has a broken proc chain — Dreadstalker/Tyrant summon timing,
Wild Imp energy gen, or Hand of Gul'dan stacking are common culprits. Priority for
C++ audit.

**DK Blood San'layn** at -22% total, -21% even with ref APL. Pure engine bug — the
Blood San'layn hero talent abilities (Vampiric Strike, Gift of the San'layn) are
likely not proc'ing correctly or scaling wrong.

**Paladin Prot Lightsmith** — even with ref talents we're -11% from reported. The
Lightsmith hero tree (Holy Bulwark, Sacred Weapon, Imbued Armor) likely has missing
or broken implementations.

---

## Specs Where Our Engine Runs HIGHER Than Reported (suspicious)

These could indicate bugs that inflate DPS (double-dipping, double-proc):

| Spec | Our DPS | Reported | Delta | Risk |
|------|---------|----------|-------|------|
| Paladin Retribution Herald | 118,498 | 104,924 | +12.9% | HIGH — suspicious |
| Monk Windwalker Conduit | 120,249 | 109,083 | +10.2% | HIGH — suspicious |
| DH Havoc Fel-Scarred | 121,441 | 114,804 | +5.8% | Medium |
| Rogue Subtlety | 115,301 | 109,256 | +5.5% | Medium |
| Monk Windwalker (base) | 120,876 | 114,446 | +5.6% | Medium |

**Paladin Ret Herald +12.9%** and **Monk WW Conduit +10.2%** are the highest risk.
These are precisely the specs our optimizer showed as winners with our talents.
If there's a double-dip bug inflating DPS, our optimizer would have found and
exploited it — which means our "good" talent builds for these specs might be
optimizing toward a bug, not real performance.

**Priority audit**: Check sc_paladin.cpp (Herald of the Sun talents — Dawnlight,
Morning Star) and sc_monk.cpp (Conduit of the Celestials — August Celestial uptime,
Chi Burst interactions) for passive aura double-apply patterns.

---

## APL Quality Summary

Most APLs are well-aligned with reference (shared >90%). The outliers are:

| Spec | Shared% | Ref_A Impact | Conclusion |
|------|---------|-------------|------------|
| Warlock Affliction Hellcaller | 99% (93/94) | +17.23% | 1 bug line |
| Warlock Affliction Soul Harvester | 76% (72/95) | +8.74% | Structural divergence |
| DH Devourer Annihilator | 51% (31/59) | +4.53% | Significant divergence |
| Monk Brewmaster | 70% (33/47) | +3.32% | Several missing lines |
| Rogue Subtlety | 75% (36/46) | +1.95% | Some useful lines missing |
| Warlock Demo | 16% (10/47) | +2.71% | Almost completely different |
| Druid Feral | 51% (36/70) | +0.19% | Different but DPS neutral |

---

## Prioritized Action List

### Immediate (bugs, high confidence)
1. **Warlock Affliction Hellcaller APL** — find and remove the 1 extra line causing -17% DPS
2. **Warlock Demo engine audit** — proc chain bug, -17% residual even with full ref substitution
3. **DK Blood San'layn engine audit** — -21% residual, hero talent procs not working
4. **Paladin Ret Herald DPS inflation** — +12.9% above reported, check for double-dip
5. **Monk WW Conduit DPS inflation** — +10.2% above reported, check for double-dip

### High Priority (talent optimizer re-runs)
6. Warlock Demo talent string corruption — fix codec, re-run optimizer
7. DH Vengeance (both variants) — re-seed optimizer with reference build, re-run
8. Paladin Protection (both variants) — re-seed optimizer with reference builds
9. Hunter Beast Mastery — APL is identical but talents underperform by 11%, optimizer stuck

### Medium Priority (APL improvements)
10. Warlock Affliction Soul Harvester APL — port ref structure for +8.74%
11. Shaman Enhancement Stormbringer APL — identify 3 diverging lines for +9.25%
12. DH Devourer Annihilator APL — port 30 diverging lines for +4.53%
13. Monk Brewmaster APL — port 14 missing lines for +3.32%

### Lower Priority (small gains, validate first)
14. DH Devourer Void-Scarred talents (+8.45%)
15. Warlock Dest Hellcaller talents (+7.34%)
16. Paladin Prot engine audit (remaining -10% gap)
17. Warlock Dest engine audit (remaining -7% gap)
18. Hunter BM engine audit (remaining -4% gap)

---

## Key Lessons for Future Optimization

1. **Talent strings can be corrupted**: Warlock Demo had non-standard bytes in
   the header. Always validate talent strings parse cleanly against DBC before
   treating optimizer output as ground truth.

2. **The optimizer can exploit bugs**: Specs running higher than reported (Ret
   Herald +12.9%, WW Conduit +10.2%) suggest our optimizer found and maximized
   a C++ bug. Verify these with upstream SimC before publishing.

3. **APL near-identity doesn't mean correctness**: Affliction Hellcaller shows
   94 vs 93 lines (99% shared) but -17% DPS. A single wrong action in the
   critical path can dominate the entire rotation. APL diff alone is not enough
   — always sim both versions.

4. **Engine divergence is the floor**: Reference talent+APL substitution reveals
   the irreducible gap caused by C++ implementation differences. For Demo Warlock,
   Prot Lightsmith, and Blood San'layn, the engine is the bottleneck — no APL
   optimization can overcome it.

5. **Reference profiles use vanilla talent strings**: Several "ref talent" strings
   are structurally simpler (fewer conditional selections, more linear trees).
   Our optimizer sometimes produces more exotic builds that work on our engine but
   may be exploiting bugs. Use reference builds as a sanity anchor, not a ceiling.

6. **Both reference and ours use the same gear**: All gaps above are pure
   talent/APL/engine differences. Gear is not a confound in this comparison.

---

*Raw data: docs/analysis/reference_profile_comparison.json*  
*Generated by scripts/compare_reference_profiles.py on 2026-04-01*

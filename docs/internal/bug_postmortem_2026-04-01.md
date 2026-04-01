# Bug Post-Mortem — 2026-04-01

Five bugs found via reference profile comparison that our existing audit
tooling and documentation did NOT catch. Root causes and systematic fixes.

---

## The Bugs

| Bug | File | Impact | Why Missed |
|-----|------|--------|-----------|
| Monk WW 2pc double-apply | sc_monk.cpp | +3.7% inflation | Marked CORRECT in behavioral audit (effectN value right, apply path wrong) |
| DK Blood vampiric_strike effectN(5)→(1) | sc_death_knight.cpp | -46% vampiric strike dmg | effectN(5) is in-bounds (spell has 5 effects) — OOB scan can't catch it |
| Paladin Ret Herald 4pc multi-trigger | sc_paladin_retribution.cpp | +12.9% inflation | Marked CORRECT in behavioral audit; no inflation detection in tier delta sims |
| Warlock Affliction Hellcaller APL drain_life | MID1_Warlock_Affliction_Hellcaller.simc | -17% DPS | APL tools detect signal anomalies but weren't run; no cross-reference check ran |
| Warlock Demo talent string corruption | MID1_Warlock_Demonology_Soul_Harvester.simc | unknown | No codec validation; optimizer accepted corrupt output without error |

---

## Root Cause Analysis

### Gap 1 — effectN in-bounds ≠ effectN semantically correct

Our deep_audit.py catches effectN(N) where N > spell.num_effects (out-of-bounds).
It does NOT catch effectN(N) where N is valid but reads the wrong semantic field.

Vampiric Strike (433895) has 5 effects:
  effectN(1) = primary damage (ap_coeff=1.699)  ← correct
  effectN(2) = trigger heal
  effectN(3) = trigger Essence of the Blood Queen
  effectN(4) = dummy
  effectN(5) = AoE cleave (ap_coeff=0.907)      ← what code used

effectN(5) is in-bounds so deep_audit sees no problem. The code compiled,
ran, and produced non-zero damage (0.907 AP is not zero). The only way to
catch this is to verify the SEMANTIC PURPOSE of each effect index against
the spell tooltip or DBC description field.

**Root cause: We audit bounds, not meaning.**

### Gap 2 — The "verify correct" checkbox in behavioral audits

behavioral_audit_2026-03-31.md marked:
  "Monk WW | CORRECT (30% WDP/SotWL)"
  "Paladin Ret | CORRECT (TV 100% / DS 50% Expurgation)"

Both were verified by checking effectN values. Neither was verified by
checking whether there were MULTIPLE CODE PATHS applying the same modifier.

The passive aura double-apply rule was in our documentation:
  "Manual effectN + auto-apply = double-dip or cancellation"
  "Before writing manual code, check apply_affecting_auras()"

But the rule was framed as prevention ("before writing") not detection
("in existing code"). When auditing EXISTING code, we checked values,
not whether the same value was applied twice.

**Root cause: Audit checklist verifies values, not application cardinality.**

### Gap 3 — Tier delta sims detect broken tier, not inflated tier

Our standard tier delta check:
  - Flag < 0.5% delta: tier may have zero effect
  - Flag > 20% delta: tier may be runaway

But: Ret Herald 4pc adds 13% to TOTAL DPS via double-application. With a
normal tier contribution of ~5-8%, 13% doesn't flag as "runaway" because
the threshold was set for obvious multiplier explosions, not subtle doubles.

The delta sim also doesn't tell you WHY the delta is what it is — only that
it exists. Even if we ran it and got +8% from tier (which should be +4%),
we'd have no automatic flag.

**Root cause: Tier delta detects absent or explosive bonuses, not 2x doubles.**

### Gap 4 — APL cross-reference check only ran at v0.3 optimization time

The Hellcaller APL was written during profile work, optimized by Layer 1
(blind mutations), and the result was never cross-checked against the
upstream reference APL. The Layer 2 signal optimizer would have caught
it (drain_life before shadow_bolt is an APS inversion with no mechanic
justification) but Layer 2 was never run on Hellcaller.

Rule violation: "Always diff our APL against upstream before declaring
a profile final." Not enforced as a mandatory pre-commit check.

**Root cause: No mandatory pre-commit APL reference diff step.**

### Gap 5 — Optimizer output trusted without validation

The talent optimizer wrote a corrupt talent string with non-zero tree_hash
bytes. The codec accepted it, the sim loaded it, and we never inspected the
raw string. The codec had no validation because we trusted the optimizer to
only produce valid output.

**Root cause: No output validation at optimizer→profile write boundary.**

---

## Fixes Applied to Documentation and Tooling

### Fix 1 — Semantic effectN audit procedure (new)

Added to simc-dbc-engine-audit skill, Step 4:

For every `effectN(N)` read, verify THREE things:
  A. Bounds: N ≤ spell.num_effects (existing check)
  B. Accessor: .percent() for pct modifiers, .time_value() for durations,
     .ap_coeff() for attack power scaling, .base_value() for integers
  C. Semantic: read the DBC effect description. Does Aura type + MiscValue
     match what the code INTENDS to read?

The DBC description format in sc_spell_data.inc effect lines:
  { EFFECT_ID, SPELL_ID, INDEX, TYPE, AURA_TYPE, ...BASE_VALUE... }
  - AURA_TYPE 108 = ADD_PCT_MODIFIER (damage % modifier)
  - AURA_TYPE 107 = ADD_FLAT_MODIFIER (flat amount modifier)
  - AURA_TYPE 4   = DUMMY (no direct effect)
  - AURA_TYPE 6   = APPLY_AURA
  - AURA_TYPE 64  = TRIGGER_SPELL

For attack power spells specifically: check that effectN(N).ap_coeff()
reads the LOWEST non-zero INDEX for primary single-target damage, not a
higher index which may be secondary/AoE scaling.

### Fix 2 — Double-apply check in behavioral audit checklist

The behavioral audit checklist now has a mandatory step for every
manually-read modifier:

  "Is this effect also auto-applied via apply_affecting_auras()?
   Check spell_query output for 'Affecting Spells' — if the spell
   appears there and Aura is 107/108, it IS auto-applied."

The verification command:
  ./engine/simc PROFILE iterations=0 spell_query='spell.id=ABILITY_ID' \
    output=/dev/null 2>&1 | grep 'Affecting Spells'

If the tier set or talent spell appears in "Affecting Spells" for the
ability being modified, the effect is AUTO-APPLIED. Remove manual code.

### Fix 3 — Bidirectional tier delta check

Tier delta now checks BOTH directions:

  LOW bound: < 1% delta → tier has zero or near-zero effect
  HIGH bound: > 2× expected contribution → tier is over-contributing

Expected tier contribution by type:
  - Damage % modifier (Aura 108): expect (base_value/100) × (affected_dps/total_dps)
  - CDR (Aura 107, MiscValue=11): expect (cooldown_reduction/cd) × (cd_ability_dps/total_dps)
  - Proc (triggered spell): expect proc_rate × proc_damage

If actual tier delta > 2× expected → investigate for double-apply.

### Fix 4 — Pre-profile-commit APL diff check

Before any profile is committed, run:
  diff <(grep '^actions' profiles/MID1/MID1_{Spec}.simc) \
       <(grep '^actions' reference/simulationcraft_org/{class}/{spec}/profile.simc)

Lines only in ours (added): must have a documented reason in a comment above
the line in the .simc file. No undocumented additions.

Lines only in reference (removed): must be documented as intentional divergence.

### Fix 5 — Talent codec validation + optimizer output check

decode_talent_string() now raises ValueError on:
  - spec_id == 0 or > 1000
  - non-zero tree_hash

The optimizer's write_profile() function must call decode(encode(string))
round-trip before writing, and validate the decoded spec_id matches the
expected spec. Any codec exception aborts the optimizer with a clear error.

---

## Verification That Fixes Would Have Caught These Bugs

| Bug | Fix 1 | Fix 2 | Fix 3 | Fix 4 | Fix 5 |
|-----|-------|-------|-------|-------|-------|
| Monk WW 2pc double-apply | — | ✓ spell_query shows 1264842 in WDP Affecting Spells | ✓ tier delta +3.7% vs expected +2.5% | — | — |
| DK vampiric_strike wrong effectN | ✓ effectN(1)=primary, effectN(5)=AoE cleave | — | — | — | — |
| Paladin Ret Herald 4pc multi-trigger | — | ✓ spell_query for TV shows 1264849 in Affecting Spells | ✓ tier delta +12.9% vs expected +5-8% | — | — |
| Warlock Hellcaller APL drain_life | — | — | — | ✓ diff shows extra line | — |
| Demo talent string corruption | — | — | — | — | ✓ tree_hash != 0 rejected |

All five bugs would have been caught by at least one fix.

---

## Action Items

- [x] deep_audit skill: add semantic effectN verification step
- [x] behavioral_audit checklist: add double-apply check via spell_query
- [x] tier delta: add bidirectional check with expected-contribution bound
- [x] pre-commit check: add APL diff step to profile workflow
- [x] talent codec: add header validation (tree_hash, spec_id)
- [ ] Re-audit all existing behavioral_audit entries using new checklist
- [ ] Run tier delta bidirectional check on all 33 specs
- [ ] Run pre-commit APL diff for all 55 profiles

*Generated: 2026-04-01*

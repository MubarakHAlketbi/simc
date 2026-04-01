# Behavioral Audit Checklist — Per-Modifier Verification Protocol

Updated: 2026-04-01
Reason: Five bugs passed prior behavioral audits due to gaps in verification procedure.
See: docs/internal/bug_postmortem_2026-04-01.md

---

## For Every Manually-Applied Modifier in C++

Run this checklist once per `effectN(N)` read, per tier set bonus, per talent multiplier.

### Step 1 — Bounds check
```
effectN(N): N <= spell.num_effects?  YES / NO
  If NO: OOB bug, fix immediately.
```

### Step 2 — Accessor type check
```
DBC Aura type for effectN(N):
  108 (ADD_PCT_MODIFIER) → must use .percent()
  107 (ADD_FLAT_MODIFIER) → must use .base_value() or .resource()
  4   (DUMMY)             → must use .average(player, level)
  11  (CDR, Spell Cooldown) → must use .time_value(), NOT from_seconds(base_value())

Code uses: ___________
Aura type: ___________
MATCH?  YES / NO
  If NO: accessor bug.
```

### Step 3 — Semantic check (NEW — catches in-bounds wrong index)
```
What does the code INTEND to read? (damage, heal, cost, duration, proc chance)
What does effectN(N) ACTUALLY describe per DBC?
  Effect description: ___________
  Aura type: ___________
  Base value / coeff: ___________

Is this the right semantic match?  YES / NO
  If NO: wrong-index bug (may be in-bounds but reading AoE cleave, cost modifier, etc.)

For ap_coeff() reads specifically:
  effectN(1) = primary single-target damage in MOST spells.
  Higher indexes may be: AoE cleave, trigger spells, resource gen.
  Verify by reading ALL effect descriptions for the spell.
```

### Step 4 — Double-apply check (NEW — catches Monk WW 2pc, Ret Herald class of bug)
```bash
./engine/simc PROFILE iterations=0 spell_query='spell.id=ABILITY_BEING_MODIFIED' \
  output=/dev/null 2>&1 | grep 'Affecting Spells'
```
```
Does the tier set or talent spell (ID: ___) appear in "Affecting Spells"?
  YES with Aura 107/108 → effect IS auto-applied. REMOVE manual code.
  YES with other Aura    → investigate whether it's auto-applied.
  NO                     → manual code is necessary (proceed).

If manual code applies the same +X% that apply_affecting_auras() also applies:
  Result is (1 + X%) × (1 + X%) instead of (1 + X%).
  For X=30%: (1.3)² = 1.69 instead of 1.30 — +30% too high.
```

### Step 5 — Bidirectional tier delta
Run AFTER implementing any new tier set or talent interaction:
```bash
./engine/simc profiles/MID1/SPEC.simc iterations=3000 threads=16 \
  json2=/tmp/tier_on.json output=/dev/null
./engine/simc profiles/MID1/SPEC.simc iterations=3000 threads=16 \
  'set_bonus=midnight_season_1_2pc=0/midnight_season_1_4pc=0' \
  json2=/tmp/tier_off.json output=/dev/null
```
```
Actual tier delta: ____%

Expected tier contribution:
  = (base_value/100) × (sum of affected ability DPS / total DPS)
  Example: 2pc +30% to WDP+SotWL where WDP+SotWL = 12% of total DPS
    → expected tier delta ≈ 0.30 × 0.12 = 3.6%

Delta < 1%:       tier may not be applying  → check implementation
Delta > 2×expected: tier may be double-applying → run double-apply check (Step 4)
Delta reasonable:   PASS
```

---

## Audit Checklist Table Template

Copy this table into the audit doc when reviewing a spec.

| Spell | effectN | Bounds | Accessor | Semantic | Double-apply | Tier delta | Result |
|-------|---------|--------|----------|----------|-------------|-----------|--------|
| Spell name | N | OK/OOB | OK/WRONG | OK/WRONG | OK/DOUBLE | expected%/actual% | PASS/FAIL |

---

## Known Patterns That Fail This Checklist

### Pattern: AoE cleave at higher effectN
Spells with AoE cleave effects often have:
  effectN(1) = primary damage (higher ap_coeff)
  effectN(2+) = secondary AoE hit (lower ap_coeff, restricted to N targets)
When code reads effectN(5) for what should be effectN(1), the result is
valid-but-wrong (lower coefficient, not an error). Only semantic check catches it.

### Pattern: Auto-apply passives
Passives with Aura 107/108 that match ability ClassFamily flags are auto-applied
by the engine at registration. Any manual code that also applies the same modifier
creates a double-apply. The ONLY reliable detection is the spell_query check.

List of confirmed auto-applies found in Midnight:
- Monk WW 2pc (1264842): auto-applies +30% to WDP and SotWL
- Monk WW 4pc (1264843): auto-applies -5s CDR to WDP and SotWL
- DK Blood 2pc (verified correct, data-driven)
- DH Havoc 2pc (verified correct, data-driven)
- Shaman Ele 2pc (verified correct, data-driven)
See behavioral_audit_2026-03-31.md for full verified list.

### Pattern: Multi-path trigger
When an action has both execute() and impact() triggering the same effect,
and impact() fires N times (one per target for AoE), the effect fires N+1 times
per cast instead of once. For AoE abilities hitting 5 targets: 6× application.
Detection: check both execute() and impact() for the same trigger call.

---

## Reference Profile Comparison (annual or post-optimization)

Run `scripts/compare_reference_profiles.py` to compare all 47 profiles against
simulationcraft.org reference builds. This is the catch-all for bugs that slip
through all above checks.

Interpret results:
- Our DPS > reference after talent+APL substitution: ENGINE INFLATION → audit that spec
- Reference APL > ours by >5%: APL bug or significant structural divergence → diff APL
- Reference talents > ours by >5%: optimizer failure or corrupted talent string
- No improvement from either substitution but large engine_div: NYI feature

Run: python3 scripts/compare_reference_profiles.py
Report: docs/analysis/reference_profile_comparison.md

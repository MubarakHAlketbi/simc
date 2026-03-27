# APL Optimization Loop — Implementation Plan

Generated: 2026-03-27

## Executive Summary

Build `scripts/apl_optimizer.py` — a fully automated, spec-agnostic APL
optimization engine that takes a SimC profile, extracts its current APL,
generates mutations, sims them, and iteratively improves composite DPS.

No existing tool does this. AutoSimC optimizes gear, not APLs. SimC upstream
relies on manual theorycrafter iteration. The CHI 2024 paper on GW2 rotation
optimization used MCTS but for a fundamentally different action model. Our
approach is a hill-climbing search with domain-specific mutation operators,
multi-stage evaluation, and strict regression guards.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   apl_optimizer.py                       │
│                                                         │
│  ┌──────────┐   ┌───────────┐   ┌────────────────────┐ │
│  │ APL      │──>│ Mutation  │──>│ SimC Runner        │ │
│  │ Parser   │   │ Generator │   │ (parallel, staged) │ │
│  └──────────┘   └───────────┘   └────────────────────┘ │
│       ▲                                │                │
│       │         ┌───────────┐          │                │
│       └─────────│ Evaluator │<─────────┘                │
│                 │ (accept/  │                           │
│                 │  reject)  │                           │
│                 └───────────┘                           │
└─────────────────────────────────────────────────────────┘
```

Four components, each independently testable:

1. **APL Parser** — reads .simc APL text into a structured representation
2. **Mutation Generator** — produces candidate APL variants
3. **SimC Runner** — executes sims in parallel, returns DPS
4. **Evaluator** — accepts/rejects candidates via composite scoring

---

## Component 1: APL Parser

### Input
The full APL text, obtained via:
```bash
./engine/simc profile.simc iterations=0 save_actions=/tmp/actions.simc
```
This dumps the engine-generated APL with all variables, sub-lists, and
conditions fully expanded. This is the ground truth of what the sim runs.

### Output: APL Data Structure
```python
@dataclass
class APLAction:
    list_name: str       # "default", "st", "aoe", "cooldowns", etc.
    action: str          # "rampage", "bloodthirst", "call_action_list"
    conditions: str      # raw if= expression, or ""
    args: dict           # name=, target_if=, op=, etc.
    line_number: int     # position within its sub-list (0-indexed)

@dataclass
class APL:
    lists: dict[str, list[APLAction]]  # list_name -> ordered actions
    variables: dict[str, str]          # variable definitions

    def to_simc(self) -> str:
        """Serialize back to .simc override text."""

    def copy(self) -> 'APL':
        """Deep copy for mutation."""
```

### Parser Logic
- Split on `actions.{list_name}+=` or `actions.{list_name}=`
- Extract action name (before first comma or end of line)
- Extract if= condition
- Extract other key=value args (target_if, op, name, etc.)
- Group by list_name, preserve ordering
- Separate variable definitions (action == "variable")

### Why save_actions, not read .simc files directly?
Because many specs use the C++ APL generator with no .simc override.
`save_actions` gives us the actual APL the engine runs regardless of source.
For specs WITH .simc overrides, it gives the same result.

---

## Component 2: Mutation Generator

### Mutation Types (6 operators)

#### M1: Adjacent Swap
Swap two adjacent actions within the same sub-list.
```
Before: rampage,if=rage>=80  |  bloodthirst
After:  bloodthirst          |  rampage,if=rage>=80
```
Only swap within the same sub-list (don't swap across st/aoe/cooldowns).
Skip swapping variable definitions and call_action_list routing entries.

#### M2: Condition Tightening
Add a condition to an unconditional action (or add an AND clause).
Use a library of common conditions:
```python
TIGHTENING_CONDITIONS = [
    "buff.bloodlust.up",
    "target.health.pct<35",       # execute phase
    "target.health.pct>=35",      # non-execute
    "active_enemies>=3",          # AoE gate
    "active_enemies<3",           # ST gate
    "cooldown.{cd}.remains>gcd",  # filler gate
    "rage>=80",                   # resource threshold (warrior)
    "energy>=50",                 # resource threshold (rogue)
    # ... spec-specific from buff/talent lists
]
```
For spec-specific conditions: extract all buff.X.up / talent.X references
from the existing APL and use them as tightening candidates.

#### M3: Condition Loosening
Remove or simplify an existing condition.
```
Before: execute,if=target.health.pct<20&buff.sudden_death.up
After:  execute,if=target.health.pct<20
```
Operations: remove one AND clause, remove entire condition, widen threshold.

#### M4: Threshold Sweep
For numeric values in conditions (stack counts, HP%, resource amounts):
sweep ±30% in 10% steps.
```
Before: rampage,if=rage>=80
Sweep:  rage>=56, rage>=64, rage>=72, rage>=80, rage>=88, rage>=96, rage>=104
```

#### M5: Action Promotion/Demotion
Move an action up or down by N positions (not just adjacent).
Useful for finding the right priority slot for an ability.
```
Before: [pos 5] execute,if=buff.sudden_death.up
After:  [pos 1] execute,if=buff.sudden_death.up
```

#### M6: Sub-list Routing Change
Modify the condition on call_action_list entries.
```
Before: call_action_list,name=aoe,if=active_enemies>=3
After:  call_action_list,name=aoe,if=active_enemies>=2
```

### Candidate Generation Strategy

Per iteration, generate candidates in this priority order:
1. M1 (adjacent swaps) — for top-10 highest DPET actions: O(10) candidates
2. M5 (promotion) — for top-5 actions by compound_amount: O(25) candidates
3. M4 (threshold sweep) — for 3 highest-impact numeric conditions: O(21) candidates
4. M6 (sub-list routing) — if spec has AoE routing: O(7) candidates
5. M2/M3 (condition changes) — for 5 unconditional + 5 most-conditioned: O(10)

Total: ~73 candidates max per iteration.

### Using Sim Data to Prioritize

After the baseline sim, parse the JSON output to rank actions by
compound_amount (total damage dealt). Focus mutations on the actions
that contribute most damage — swapping two low-damage fillers is unlikely
to matter.

```python
def rank_actions_by_impact(json_path: str) -> list[tuple[str, float]]:
    """Return [(action_name, compound_amount), ...] sorted descending."""
```

---

## Component 3: SimC Runner

### Multi-Stage Evaluation (key to performance)

**Stage 1 — Coarse filter (100 iterations)**
- Run ALL candidates at 100 iterations
- Compute composite DPS
- Keep top 20% that beat baseline (or top 10, whichever is fewer)
- Cost: 73 candidates × 2 fights × 100 iter ≈ 14,600 iterations (~15s)

**Stage 2 — Medium filter (1,000 iterations)**
- Run surviving candidates at 1,000 iterations
- Keep those that beat baseline by >0.3% composite
- Cost: ~15 candidates × 2 fights × 1,000 iter ≈ 30,000 iterations (~30s)

**Stage 3 — Confirmation (10,000 iterations)**
- Run top 3 candidates at 10,000 iterations
- Accept best if it beats baseline AND no fight style regresses >1%
- Cost: 3 candidates × 2 fights × 10,000 iter ≈ 60,000 iterations (~60s)

**Total per iteration: ~2 minutes** (vs ~25 minutes if we ran all 73 at 10k)

### Parallelism
SimC supports `threads=N`. Use threads=4 per sim, run 4 sims concurrently
= 16 cores utilized. The machine has 32 cores so this is conservative.

```python
async def run_sim(profile: str, apl_override: str, fight_style: str,
                  iterations: int, threads: int = 4) -> SimResult:
    """Write temp .simc file, run simc, parse JSON output."""

@dataclass
class SimResult:
    dps_mean: float
    dps_error: float
    action_breakdown: dict[str, float]  # name -> compound_amount
    fight_style: str
```

### Override Mechanism
For each candidate, write a temp .simc file:
```
input=profiles/MID1/MID1_{spec}.simc
# APL override follows — replaces all actions
actions.precombat=...
actions=...
actions+=/...
```
The `input=` directive loads the profile (gear, talents, consumables),
then the actions lines override the APL completely.

---

## Component 4: Evaluator

### Composite Scoring
```python
def composite_dps(pw_dps: float, hac_dps: float) -> float:
    return 0.50 * pw_dps + 0.50 * hac_dps
```

### Acceptance Criteria
```python
def should_accept(candidate: SimResult, baseline: SimResult) -> bool:
    comp_new = composite_dps(candidate.pw, candidate.hac)
    comp_old = composite_dps(baseline.pw, baseline.hac)

    # Must improve composite
    if comp_new <= comp_old:
        return False

    # Neither fight style may regress >1%
    if candidate.pw < baseline.pw * 0.99:
        return False
    if candidate.hac < baseline.hac * 0.99:
        return False

    return True
```

### Convergence
```python
def has_converged(history: list[float], max_iters: int) -> bool:
    if len(history) >= max_iters:
        return True
    if len(history) >= 2:
        delta = (history[-1] - history[-2]) / history[-2]
        if delta < 0.001:  # <0.1% improvement
            return True
    return False
```

---

## Main Loop

```python
def optimize_spec(spec: str, profile_path: str, max_iterations: int = 10):
    # Step 0: Extract current APL
    apl = extract_apl(profile_path)

    # Step 0b: Run baseline
    baseline = run_baseline(profile_path)
    history = [composite_dps(baseline.pw, baseline.hac)]

    for iteration in range(max_iterations):
        # Step 1: Generate candidates
        candidates = generate_mutations(apl, baseline.action_breakdown)

        # Step 2: Multi-stage evaluation
        winners = evaluate_staged(candidates, profile_path, baseline)

        if not winners:
            print(f"  Iteration {iteration}: no improvements found. Converged.")
            break

        # Step 3: Accept best
        best = winners[0]
        apl = best.apl
        baseline = best.result
        history.append(composite_dps(baseline.pw, baseline.hac))

        print(f"  Iteration {iteration}: +{(history[-1]-history[-2])/history[-2]*100:.2f}%"
              f" composite ({history[-1]:.0f})")

        # Step 4: Convergence check
        if has_converged(history, max_iterations):
            break

    # Step 5: Write final APL
    write_apl_override(spec, apl)
    return apl, history
```

---

## CLI Interface

```bash
# Optimize a single spec
python3 scripts/apl_optimizer.py --spec warrior_fury --max-iter 10

# Optimize all specs
python3 scripts/apl_optimizer.py --all --max-iter 5

# Optimize with custom profile
python3 scripts/apl_optimizer.py --profile profiles/MID1/MID1_Warrior_Fury.simc

# Dry run (generate candidates, don't sim)
python3 scripts/apl_optimizer.py --spec warrior_fury --dry-run

# Resume from checkpoint
python3 scripts/apl_optimizer.py --spec warrior_fury --resume
```

---

## Output Artifacts

Per spec:
- `results/optimization/{spec}/iteration_{N}.json` — per-iteration results
- `results/optimization/{spec}/candidates_{N}.json` — all candidates tested
- `results/optimization/{spec}/final_apl.simc` — winning APL override
- `results/optimization/{spec}/history.json` — composite DPS over iterations
- `results/optimization/{spec}/report.md` — human-readable summary

Global:
- `results/optimization/summary.md` — all specs, improvements found
- `results/optimization/checkpoint.json` — resumable state

---

## Spec-Specific Configuration

Some mutations need spec-aware knowledge. Store in a config dict:
```python
SPEC_CONFIG = {
    "warrior_fury": {
        "resource": "rage",
        "resource_thresholds": [60, 70, 80, 90, 100],
        "execute_threshold": "target.health.pct<35",  # massacre
        "key_cds": ["recklessness", "avatar", "bladestorm"],
        "aoe_routing_var": "active_enemies",
        "default_aoe_threshold": 3,
    },
    # ... per spec
}
```

This can be auto-generated from the APL itself on first parse — extract
resource references, find execute conditions, identify CD names, etc.

---

## Risk Mitigation

### Problem: Local Optima
Hill climbing can get stuck. Mitigations:
- Multiple mutation types explore different dimensions simultaneously
- Threshold sweeps explore continuous parameters exhaustively
- M5 (promotion) can make large jumps in priority ordering
- After convergence: re-run with shuffled candidate order as validation

### Problem: Simulation Noise
At low iterations, DPS variance is high. Mitigations:
- Multi-stage evaluation filters noise at 100 iter, confirms at 10k
- Require >0.3% improvement at stage 2 (not just positive)
- Stage 3 uses target_error=0.1 for high confidence

### Problem: Fight-Style Regression
Improving Patchwerk at the cost of HecticAddCleave (or vice versa).
Mitigations:
- Hard 1% regression cap per fight style
- Composite scoring ensures both contribute equally

### Problem: Multi-Build Regression
APL change helps one talent build but hurts another. Mitigations:
- After convergence, validate against all hero talent builds for the spec
- 2% regression cap per build per fight style

### Problem: Compute Time
33 specs × ~10 iterations × ~2 min = ~11 hours total.
Mitigations:
- Run specs in parallel (4-8 concurrent)
- Skip specs already within 0.3% of upstream (27 tied specs)
- Checkpoint/resume support for interruptions
- Focus on the 6 specs with known gaps first

---

## Implementation Order

### Phase A: Core Infrastructure (estimate: 2-3 hours)
1. APL parser + serializer (parse .simc, emit .simc)
2. SimC runner (temp file, JSON parse, parallel execution)
3. Composite scorer + acceptance logic
4. Unit tests with a simple spec (Warrior Fury)

### Phase B: Mutation Engine (estimate: 2-3 hours)
5. M1: Adjacent swap generator
6. M4: Threshold sweep generator
7. M5: Promotion/demotion generator
8. M2/M3: Condition tightening/loosening
9. M6: Sub-list routing changes
10. Action ranking from sim JSON output

### Phase C: Main Loop + Reporting (estimate: 1-2 hours)
11. Multi-stage evaluation pipeline
12. Convergence detection
13. Iteration loop with checkpoint/resume
14. Report generation (per-spec .md + global summary)

### Phase D: Full Run + Validation (estimate: variable)
15. Run on 6 priority specs (known gaps from Phase 3.6 comparison)
16. Run on remaining 27 specs
17. Multi-build validation pass
18. Write accepted APLs back to ActionPriorityLists/default/
19. Re-run full 112 baselines with optimized APLs
20. Update project_progress.md

---

## Priority Specs (run first)

From the 3-way comparison, these specs had the largest gaps:

| Spec | Known Gap | Expected Optimization |
|------|-----------|----------------------|
| Rogue Assassination | ~13k composite (low outlier) | Significant — APL likely needs major reordering |
| Druid Balance | ~3k → needs re-baseline | Re-baseline first, then optimize |
| Evoker Augmentation | ~8k (support spec) | Minor — low raw DPS expected |
| Warlock Affliction | Was -7.7% C++ lag, now fixed | Verify fix, then fine-tune |
| Warrior Fury | Was -6.7% C++ lag, now fixed | Verify fix, then fine-tune |
| Shaman Enhancement | Was -5.0% C++ lag, now fixed | Verify fix, then fine-tune |

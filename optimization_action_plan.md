# Optimization Action Plan

Updated: 2026-03-28

## Architecture

Two independent optimization loops per spec, each producing results per fight style:

```
TALENT OPTIMIZATION                    APL OPTIMIZATION
  Wowhead builds (seeds)                Extract current APL
       |                                     |
  Screen at 1k iter per style           Generate mutations (swap/sweep/route)
       |                                     |
  Local search (single-node swaps)      Multi-stage eval (100→1k→10k iter)
       |                                     |
  Hill-climb to convergence             Accept best per style
       |                                     |
  Confirm at 10k iter                   Confirm at 10k iter
```

Each spec produces TWO independent optimal talent/APL builds — one for Patchwerk, one for HecticAddCleave.

---

## Talent Optimization — Seed + Local Search

### Why Not Classify-Then-Permute

The old approach (node_classifier.py + talent_permute.py) was abandoned:

1. **Code scanner regex wrong** — matches `talent.spec.X` but C++ uses `talents.fury.X` (plural, spec-name prefix). 0 matches from 239 references.
2. **APL scanner too narrow** — only finds talents in `if=` conditions (5/106 for Fury). Core abilities never gated.
3. **Wrong abstraction** — talent optimization is DAG budget allocation, not independent node toggles.

### Current Approach

**Phase 1 — Seed Screening** (`talent_build_compare.py`):
- Sim all Wowhead builds (4-16 per spec) at 1000 iter × both fight styles
- Rank per fight style independently, pick top 3 seeds

**Phase 2 — Neighborhood Generation** (`talent_neighbor.py`):

| Mutation | Description | Count (Fury) |
|----------|-------------|-------------|
| REMOVE | Drop a selected non-granted node | 45 |
| SWAP_POINT | Remove A + add B in same sub-tree (budget-neutral) | 60 |
| SWAP_CHOICE | Switch a choice node to its other option | 9 |

Budget-strict: no ADDs beyond current point cap per sub-tree.

**Phase 3 — Hill-Climb** (`talent_local_search.py`):
- Per seed: generate neighbors → screen at 500 iter → confirm top 5 at 2000 iter → adopt best
- Repeat until <0.1% improvement (typically 1-2 passes)
- Final confirm at 10k iter

### Constraints

All builds must satisfy (validated by `talent_neighbor.validate_build()`):
1. Sub-tree point budgets: CLASS=36, SPEC=34, HERO=15 for Warrior Fury (varies per spec)
2. Row gates: req_points thresholds per node
3. Edge prerequisites: at least one parent selected
4. Choice exclusivity: one option per choice node
5. Granted nodes: hero starting nodes and spec-starter class nodes always present

### Test Results — Warrior Fury

| Style | Baseline | Optimized | Gain | Passes | Key Finding |
|-------|----------|-----------|------|--------|-------------|
| Patchwerk | 86,904 | 88,178 | +1.52% | 2 | Stance Mastery replaces utility |
| HecticAddCleave | 209,221 | 210,582 | +0.65% | 2 | Stance Mastery + Fast Footwork |

Converges in 1-2 passes with ~114 neighbors per pass. This is the ceiling for single-node mutations. Builds differ between PW and HAC (8 vs 5 unique nodes).

---

## APL Optimization — Mutation + Multi-Stage

Implemented in `apl_optimizer.py`. Per fight style:

1. Extract current APL via `save_actions`
2. Generate mutations: adjacent swap, threshold sweep, routing changes
3. Three-stage funnel: 100 iter → 1000 iter → 10000 iter
4. Accept if DPS improves for that fight style

### Test Results — Warrior Fury

| Style | Result | Detail |
|-------|--------|--------|
| Patchwerk | +0.00% | Converged immediately — APL already optimal |
| HecticAddCleave | +0.44% | Rampage threshold 100→80 in thane_aoe |

Manual APL changes also tested (execute repositioning, rend/wrecking_throw additions). All regressed (-1.52% PW, -0.86% HAC). The upstream-imported APL is battle-tested and at its ceiling.

---

## Files

### Active Pipeline

| Script | Lines | Purpose |
|--------|-------|---------|
| `scripts/lib/sim_runner.py` | 307 | SimC runner, JSON parse, scoring |
| `scripts/lib/apl_parser.py` | 278 | APL parse/serialize |
| `scripts/lib/apl_mutations.py` | 262 | Mutation operators |
| `scripts/lib/talent_tree.py` | 598 | DBC tree parser |
| `scripts/lib/talent_codec.py` | 491 | Talent string codec |
| `scripts/lib/tree_codec_bridge.py` | 239 | Tree↔codec bridge |
| `scripts/lib/talent_neighbor.py` | 290 | Constraint-aware neighbors |
| `scripts/apl_optimizer.py` | 288 | APL optimization loop |
| `scripts/talent_local_search.py` | 310 | Talent seed + hill-climb |
| `scripts/talent_build_compare.py` | 397 | Wowhead build comparison |
| `scripts/optimize_all.py` | 145 | Master orchestrator |

### Deprecated (kept, not called)

| Script | Reason |
|--------|--------|
| `scripts/lib/node_classifier.py` | Wrong regex (`talent.` vs `talents.`), wrong abstraction |
| `scripts/lib/talent_permute.py` | Produces 0 combos with correct budgets |

---

## Compute Estimates

Per spec, per fight style:

| Phase | Sims | Time |
|-------|------|------|
| Seed screening (12 builds × 1k iter) | 12 | 36s |
| Neighborhood screen (114 neighbors × 500 iter) | 114 | 170s |
| Confirmation (top 5 × 2k iter) | 5 | 25s |
| Hill-climb pass 2 | ~100 | ~150s |
| Final confirm (10k iter) | 2 | 14s |
| **Total per style** | **~233** | **~6.5 min** |

All 33 specs × 2 styles: ~7 hours. With 2x parallelism: ~3.5 hours.

---

## Success Criteria

1. Every spec's PW-best talent build ≥ best Wowhead build for PW
2. Every spec's HAC-best talent build ≥ best Wowhead build for HAC
3. All talent strings budget-compliant (verified: points match Wowhead totals)
4. All generated builds pass SimC smoke test
5. Pipeline runs end-to-end: `python3 scripts/optimize_all.py --talent --apl --all`

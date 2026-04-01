# Signal-Guided APL Optimization — Design Document

**Status:** Design phase (2026-03-31)
**Scope:** Layer 2 APL optimizer using per-ability stats, resource flow, and buff uptime data
**Prerequisite:** Layer 1 (blind mutation optimizer) has converged for all 33 specs

---

## 1. Motivation

The blind optimizer (Layer 1) generates mutations randomly and scores them with DPS delta.
It converges well but has two structural weaknesses:

1. It explores the full mutation space uniformly — O(N²) for swaps, O(N*K) for thresholds.
   At convergence, most mutations regress. The signal layer instead generates ~10 targeted
   mutations with prior evidence they will help, reducing compute by ~20x.

2. It cannot generate mutations that ADD new constructs (new `if=` conditions, emergency
   dumps, new buff gating). It can only modify existing ones. The signal layer identifies
   missing structures and generates those "add" mutations.

---

## 2. Signals Available in JSON2 Output

### 2.1 Per-Ability Stats (player.stats[])

| Field | What It Tells Us |
|-------|-----------------|
| `portion_aps.mean` | DPS contributed per second of fight time (true DPET) |
| `portion_amount` | Fraction of total damage dealt |
| `num_executes.mean` | Average cast count per fight |
| `total_intervals.mean` | Actual mean time between casts (reflects priority pressure + CD) |
| `direct_results.crit.pct` | Crit rate (sanity check vs talent math) |

**portion_aps is the ground truth priority metric.** It normalizes for CD, cast time, and
hit count. If ability A has higher portion_aps than B, A is more valuable per unit of fight
time. If A is below B in the APL without a conditional dependency, that is suboptimal.

### 2.2 Dynamic Buff Data (player.buffs[])

| Field | What It Tells Us |
|-------|-----------------|
| `uptime` | % of fight the buff was active |
| `start_count` | How many times the buff started per fight |
| `refresh_count` | How many times the buff was refreshed before expiry |
| `expire_count` | How many times the buff EXPIRED without being consumed |
| `interval` | Mean time between activations |

**Expire rate = expire_count / (expire_count + refresh_count)**

A high expire rate on a PROC buff means the APL isn't consuming the buff fast enough.
The consumer ability should be promoted or have `buff.X.react` added to its condition.

### 2.3 Resource Flow (player.collected_data)

| Field | What It Tells Us |
|-------|-----------------|
| `resource_overflowed.mean` | Resource wasted by hitting the cap |
| `resource_lost.mean` | Total resource spent (denominator) |
| `combat_end_resource.mean` | Resource unspent at fight end (dead time waste) |

**Overcap rate = overflowed / (overflowed + spent) * 100**

Observed overcap rates across specs:
- warrior_fury: 0.9% — near perfect
- rogue_assassination: 12.0% — room to improve
- monk_windwalker: 43.0% — significant energy waste
- dk_frost: 22.2% — runic power waste
- shaman_enhancement: 71.2% — maelstrom waste (major)
- priest_shadow: 65.5% — insanity overcap (GCD-limited, partially expected)

---

## 3. Signal Types and Formulas

### Signal A — APS Priority Inversion

**Condition:** Ability A has higher `portion_aps` than ability B, but A appears at a
lower (less urgent) position than B in the APL, with no conditional dependency.

```
aps_delta_fraction = (A.portion_aps - B.portion_aps) / total_dps

Signal priority = aps_delta_fraction
Threshold = 0.005  (0.5% of total DPS in portion_aps gap)
```

**Mutation:** Promote A above B (non-adjacent swap, not possible in blind optimizer).

**Important caveat:** APS order inversion is not always fixable by a swap.
Some inversions are intentional — e.g., a cooldown ability B correctly fires first to set up
amplifiers, then A fires inside the window. The DPS delta test always validates the mutation.

### Signal B — Proc Buff Waste

**Condition:** A proc buff has a high expire rate, AND there exists an APL action that
references that buff in an `if=buff.X.up` or `if=buff.X.react` condition.

```
expire_rate = expire_count / (expire_count + refresh_count)

consumer_aps = portion_aps of the APL action that consumes this buff
consumer_aps_fraction = consumer_aps / total_dps

signal_priority = expire_rate * consumer_aps_fraction
Threshold = 0.002  (>0.2% of total DPS being lost to buff waste)
```

**Distinguishing proc buffs from CD buffs:**
- **CD buff** = buff name matches an APL action name directly (player activates it).
  These expire naturally; expire_rate=100% is expected. Example: recklessness, avatar.
- **Proc buff** = no matching APL action name. Created by game mechanics (procs, passive effects).
  High expire rate = APL isn't responding fast enough.

Detection: If `buff.name` appears as `if=buff.NAME.up` in any APL action, it has a consumer.
If `buff.name` also appears as a direct APL action (e.g., `actions+=recklessness`), it's a
player CD — skip the waste signal.

**Mutations generated:**
1. Promote the consumer action (move higher in its sub-list)
2. If consumer already has `buff.X.up` condition, also try adding `buff.X.react` (server-confirmed)
3. If consumer lacks `buff.X.up` condition, try adding it as an OR clause

### Signal C — Resource Overcap / Spender Starvation

**Condition:** A spender-type resource has overcap_rate above threshold.

```
overcap_rate = overflowed / (overflowed + spent) * 100
Threshold = 8.0%  (below this is unavoidable GCD pressure)
```

**Resource classification:**

| Spender (overcap = bad) | Pool (overcap may be expected) |
|-------------------------|-------------------------------|
| rage, energy, focus | mana (for non-mana-starved specs) |
| runic_power, fury (DH) | — |
| holy_power, combo_points | — |
| soul_shards, chi | — |
| maelstrom, insanity | secondary only — check end_waste too |
| astral_power | — |

For ambiguous resources (maelstrom, insanity): also check `combat_end_resource`.
If both overcap_rate > 8% AND end_waste > 1 GCD worth of resource, signal is real.

**Signal priority = min(overcap_rate / 100, 0.5)**
Scaled down relative to buff waste signals — resource signals are less precise about
what exactly to change.

**Mutations generated:**
1. **Lower spender threshold:** Find the highest-portion_aps spender of this resource.
   Try reducing its `resource >= X` threshold in if= conditions.
2. **Add emergency dump:** If no emergency dump exists (`resource >= 0.9*max`), add one.
3. **Promote spender:** Move the top spender higher in its sub-list.

### Signal D — Interval Gap (Filler Delay)

**Condition:** A high-portion_aps ability has an actual cast interval significantly
longer than its theoretical GCD pressure would allow.

This signal is the hardest to use because we don't have theoretical cooldowns in the JSON.
We approximate:

```
# Abilities with portion_aps in top 5 AND interval > 4.0s AND executes < fight_duration / 4.5
# are likely being delayed by priority pressure
delay_indicator = (interval - 3.0) / 3.0  # normalized excess wait
signal_priority = delay_indicator * (portion_aps_fraction) * 0.3  # lower confidence
Threshold = 0.003
```

**Mutation:** Promote the ability in its sub-list. Test via DPS delta.

This signal has the lowest priority and highest false-positive rate.
Only generate if no higher-priority signals exist for the same ability.

---

## 4. Signal Combination and Ranking

Multiple signals can point to the same ability. When they do, the combined priority
is higher confidence than any individual signal.

```python
# Combine overlapping signals pointing to same action
combined_signals = {}
for signal in all_signals:
    key = signal.target_action
    if key in combined_signals:
        combined_signals[key].priority += signal.priority * 0.5  # diminishing returns
        combined_signals[key].types.append(signal.type)
    else:
        combined_signals[key] = signal
```

**Highest confidence combinations:**
1. `buff_waste` + `aps_order` pointing to same consumer → very high confidence promote
2. `resource_overcap` + `aps_order` pointing to top spender → high confidence
3. `buff_waste` + `interval_gap` → medium confidence (two independent signals agree)

---

## 5. Architecture

```
Layer 1 (blind, already done)
        ↓
Layer 2 (signal-guided):
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  1. Run baseline sim → JSON                                             │
  │  2. Parse JSON → compute signals (A, B, C, D)                          │
  │  3. Rank signals by priority                                            │
  │  4. Generate signal mutations (targeted, ~10-30 candidates)            │
  │  5. Also generate blind mutations (as before, ~200 candidates)         │
  │  6. Evaluate ALL in single multi-stage funnel (300→3k→10k)             │
  │  7. Accept best improvement                                             │
  │  8. Repeat until no signal OR blind mutation improves DPS              │
  └─────────────────────────────────────────────────────────────────────────┘
```

**Order rationale:** Run signals and blind mutations in the SAME pool per iteration.
- Signals and blind compete directly → best mutation wins regardless of source
- After signal mutation is accepted, signals are recomputed from new JSON
- Cascading effects are caught (fixing buff waste can change portion_aps rankings)

**Stopping condition:** No signal mutation improves DPS AND no blind mutation improves DPS.
A spec that was already well-optimized by Layer 1 will converge immediately (0-1 iterations).

---

## 6. Implementation Plan

### Phase 1 — Extended SimResult

Extend `scripts/lib/sim_runner.py` → `SimResult`:

```python
@dataclass
class AbilityStats:
    name: str
    portion_aps: float
    portion_amount: float
    executes: float
    interval: float
    crit_pct: float

@dataclass
class BuffStats:
    name: str
    uptime: float
    start_count: float
    refresh_count: float
    expire_count: float

    @property
    def expire_rate(self):
        total = self.expire_count + self.refresh_count
        return self.expire_count / total if total > 0 else 0.0

@dataclass
class ResourceStats:
    resource: str
    spent: float
    overcap: float
    end_waste: float

    @property
    def overcap_rate(self):
        total = self.spent + self.overcap
        return self.overcap / total if total > 0 else 0.0

# Add to SimResult:
ability_stats: list[AbilityStats]     # all abilities
buff_stats: list[BuffStats]           # all dynamic buffs
resource_stats: list[ResourceStats]   # all resources
```

### Phase 2 — Signal Extractor

New file: `scripts/lib/apl_signal_extractor.py`

```python
def extract_signals(sim_result, apl_text) -> list[OptimizationSignal]:
    apl_actions = parse_apl(apl_text)
    action_order = {a.action: i for i, a in enumerate(flatten_actions(apl_actions))}
    buff_consumers = find_buff_consumers(apl_actions)   # buff_name -> action_name
    player_cds = find_player_cds(apl_actions)           # actions that the player activates
    
    signals = []
    signals += aps_order_signals(sim_result, action_order)
    signals += buff_waste_signals(sim_result, buff_consumers, player_cds)
    signals += resource_overcap_signals(sim_result)
    signals += interval_gap_signals(sim_result, action_order)
    
    return combine_signals(signals)
```

### Phase 3 — Signal Mutation Generator

New file: `scripts/lib/apl_signal_mutations.py`

Generates `(APL, description)` tuples — same format as existing blind mutations.
The key new mutation types beyond what blind optimizer has:

1. **Non-adjacent swap** — move ability from position N to position M (M << N) based on APS
2. **Buff gate add** — add `buff.X.up` condition to an action that lacks it
3. **Resource emergency dump** — add `resource >= THRESHOLD` action at end of list
4. **Buff react upgrade** — change `buff.X.up` to `buff.X.react` for critical procs

### Phase 4 — Layer 2 Runner

New file: `scripts/signal_apl_optimizer.py`

```python
def optimize_spec_with_signals(spec, fight_style, max_iter=5, threads=16):
    profile = find_profile(spec)
    baseline = run_sim(profile, fight_style, iterations=10000, threads=threads,
                       json_out=f'/tmp/{spec}_{fight_style}_baseline.json')
    
    for iteration in range(max_iter):
        apl_text = extract_apl(profile)
        signals = extract_signals(baseline, apl_text)
        
        signal_mutations = generate_signal_mutations(signals, parse_apl(apl_text))
        blind_mutations = generate_all_mutations(parse_apl(apl_text))
        
        all_candidates = signal_mutations + blind_mutations
        
        best = evaluate_staged_single(all_candidates, profile, baseline, fight_style, threads)
        
        if not best or best[2].dps_mean <= baseline.dps_mean:
            break  # converged
        
        apl, desc, result = best[0]
        apply_apl_to_profile(profile, apl)
        baseline = result
        print(f"  [{iteration+1}] {desc}: {result.dps_mean:,.0f} (+{(result.dps_mean-baseline.dps_mean)/baseline.dps_mean*100:.2f}%)")
    
    return baseline
```

---

## 7. Expected Gains by Signal Type

Based on observed data patterns:

| Signal | Expected Gain | Confidence | Specs Most Likely to Benefit |
|--------|--------------|------------|------------------------------|
| buff_waste (proc consumer promote) | 0.5–3% | High | Warlock Affli, Evoker Dev |
| aps_order (non-adjacent swap) | 0.1–1% | Medium | Any spec after talent change |
| resource_overcap (spender dump) | 0.2–2% | Medium | Shaman Enh, Monk WW, DK Frost |
| interval_gap (filler promote) | 0.1–0.5% | Low | Dense filler specs (Rogue, Mage) |

**Key insight:** Warlock Affliction HAC already got +3.63% from blind APL optimization.
Signal pass may find further gains for specs with high buff expire rates or resource waste.

---

## 8. What Signal Optimization Cannot Detect

The signal layer operates only on APL-layer behavior. It cannot fix:

- **Missing abilities** — if an ability has 0 portion_aps but SHOULD be used (e.g., not in APL at all)
- **Engine proc chain bugs** — ability A doesn't proc B because of a C++ bug
- **Snapshotting** — buff wasn't captured at cast time (engine-level)
- **Talent synergy** — wrong talent selected that makes ability weaker

These require C++ engine audit (covered by the DBC audit tooling).

---

## 9. Files to Create/Modify

| File | Action | What |
|------|--------|------|
| `scripts/lib/sim_runner.py` | Modify | Add AbilityStats, BuffStats, ResourceStats to SimResult + parse_sim_json |
| `scripts/lib/apl_signal_extractor.py` | Create | Signal computation engine |
| `scripts/lib/apl_signal_mutations.py` | Create | Signal-guided mutation generators |
| `scripts/signal_apl_optimizer.py` | Create | Layer 2 runner (per spec, per fight style) |
| `scripts/optimize_all_specs.py` | Modify | Add --signal-pass flag to run Layer 2 after Layer 1 |

Estimated: ~600 lines of Python across new/modified files.

---

## 10. Compute Estimate

Per spec, per fight style:
- Baseline sim (10k iter): ~15s
- Signal extraction: <1s
- Signal mutations generated: ~20-30 per spec
- Blind mutations generated: ~200 per spec
- Total candidates: ~220-230
- Multi-stage eval (same as Layer 1): ~7 min

All 33 specs × 2 fight styles × 1 pass: ~7.7 hours (same as Layer 1).
Most specs will converge in 0-2 iterations since Layer 1 already optimized them.
Expected wall time: ~2-4 hours.

# LLM APL Advisor — Design Document

**Status:** Design phase (2026-03-31)
**Layer:** 3 (after programmatic signal extraction, before or alongside signal mutations)
**Scope:** Use an LLM with structured sim data + APL to reason about fixes that require
semantic game-mechanic knowledge — things no formula can generate.

---

## 1. The Gap the LLM Fills

The signal extractor (Layer 2) works purely on sim output data. It can detect:
- High buff expire rates
- Resource overcap
- APS priority inversions
- Cast interval gaps

But it cannot act on what it detects when the fix requires semantic knowledge:

**Example — Warlock Affliction `manifested_demonic_soul`:**
- Signal: buff expires 96% of the time
- Problem: buff name appears NOWHERE in the APL (no consumer action, no if= condition)
- Programmatic system: cannot generate a fix — it doesn't know what action consumes this buff
- LLM knows: manifested_demonic_soul is a Soul Harvester proc that empowers drain_soul
  with an extra soul shard cost. Fix = add `drain_soul,if=buff.manifested_demonic_soul.up`

**Four categories of gap:**

1. **Missing buff consumers** — buff has high expire rate but no APL reference at all.
   Fix requires knowing WHICH action consumes this specific buff.

2. **Wrong condition logic** — APL has `buff.X.up` when the correct check should be
   `buff.X.stack>=2` or `buff.X.react` or `buff.X.remains>cast_time`. Requires
   understanding of how the buff stacks and what the mechanical threshold is.

3. **Suboptimal window usage** — high-value ability should be held for a burst window
   but isn't. The signal shows low APS for the ability, but the fix is adding
   `if=cooldown.Y.remains<X` — requires knowing Y is the amplifier for this ability.

4. **Missing emergency cases** — edge conditions not covered (e.g., "spend resources
   before a movement phase", "dump DoTs before execute", "specific synergy combos").
   These never show up as clear numeric signals.

---

## 2. What the LLM Receives (Prompt Structure)

The LLM receives a structured report for ONE spec + ONE fight style, containing:

### Section A — Sim Statistics (numerical signals)
```
ABILITY PERFORMANCE (sorted by APS contribution):
  unstable_affliction    19.4%  x88/fight   aps=17899  gap=3.4s
  agony                   7.3%  x17/fight   aps= 6697  gap=18.0s
  haunt                   5.9%  x16/fight   aps= 5406  gap=18.1s
  shadow_bolt             5.0%  x27/fight   aps= 4626  gap= 9.7s
  malefic_grasp           4.9%  x20/fight   aps= 4478  gap=13.2s
  drain_life              1.3%  x62/fight   aps= 1197  gap= 4.2s
  [zero-aps actions: dark_harvest x7.4, summon_darkglare x2.8, emberwing_heatwave x2.8]

BUFF WASTE SIGNALS:
  manifested_demonic_soul  expire=96%  uptime=14.6%  starts=3.2/fight  APL_REFERENCE=NONE
  alnsight                 expire=65%  uptime=38.2%  starts=7.3/fight  APL_REFERENCE=FOUND
  arcanoweave_insight      expire=51%  uptime=52.6%  starts=5.9/fight  APL_REFERENCE=FOUND
  might_of_the_void        expire=47%  uptime=58.7%  starts=8.1/fight  APL_REFERENCE=FOUND

RESOURCE FLOW:
  mana:         spent=927838  overcap=58384 (5.9%)  end=12528
  soul_shard:   spent=68      overcap=1 (1.5%)      end=1
```

### Section B — Current APL (full text)
The complete APL exactly as SimC runs it. The LLM can read this directly.

### Section C — Context Block (spec identity + mechanics reminder)
```
SPEC: Warlock Affliction
HERO TREE: Soul Harvester (active in this profile)
FIGHT STYLE: Patchwerk (single target, 300s)
BUILD 12.0.1.66709

KNOWN MECHANICS (from Wowhead):
  - manifested_demonic_soul: Soul Harvester proc. Triggers when drain_soul ticks.
    Buff makes the next drain_soul consume an extra soul shard for massive damage bonus.
    Consumes on cast of: drain_soul
  - soul_shard: primary resource, 0-5. Spenders: unstable_affliction (1), drain_soul (1+1 with proc)
  - nightfall: proc from corruption/agony ticks. Empowers drain_soul/shadow_bolt/malefic_grasp
  - summon_darkglare: major cooldown (2min). Darkglare copies DoTs.
```

### Section D — Programmatic Signals Summary
What the automated system already found and is already testing:
```
AUTOMATED MUTATIONS BEING TESTED:
  - Promote drain_soul above drain_life in root list (APS order signal)
  - Lower soul_shard spend threshold from 4 to 3 (resource signal)
```

---

## 3. The Prompt (Exact Thinking Instructions)

The LLM must follow a STRICT REASONING PROTOCOL, not open-ended commentary.
The prompt tells it exactly what to think about, in what order, and what output format.

```
You are analyzing a SimulationCraft APL (Action Priority List) for [SPEC].
Your job is to identify SPECIFIC, ACTIONABLE changes to the APL that would increase DPS.

Work through these steps IN ORDER:

STEP 1 — BUFF WASTE ANALYSIS
Look at the BUFF WASTE SIGNALS section. For each buff with expire_rate > 40%:
  a) If APL_REFERENCE=NONE: identify which APL action consumes this buff.
     Write the exact action name and the exact if= condition to add.
  b) If APL_REFERENCE=FOUND: find that action in the APL. Is its priority high enough?
     Is the condition complete? Does it use .react vs .up correctly?
  c) For each finding, write one specific APL line change.

STEP 2 — APS ORDER VERIFICATION
Look at ABILITY PERFORMANCE. For abilities with portion_aps > 2000:
  a) Find each ability in the APL.
  b) Is any high-APS ability blocked by a lower-APS ability with no mechanical justification?
     (A mechanical justification = the lower ability sets up a buff that amplifies the higher one)
  c) If blocked without justification, write the specific swap.

STEP 3 — RESOURCE FLOW DIAGNOSIS
Look at RESOURCE FLOW. For any resource with overcap_rate > 8%:
  a) Identify the primary spender for that resource in the APL.
  b) Is its if= condition too restrictive? Find the exact threshold.
  c) What value would you lower it to? Show the exact line change.
  d) Is there an end-of-fight or emergency dump? Should one be added?

STEP 4 — MISSING SYNERGIES
Look at zero-aps actions (executed but dealing 0 damage). These are:
  cooldowns, summons, buffs, or utility. For each:
  a) Is it properly aligned with burst windows? (should fire BEFORE damage CDs, not after)
  b) Is its if= condition correct given the rotation?

STEP 5 — OUTPUT
List ONLY the changes you are confident about. Format each as:
  CHANGE [N]:
    TYPE: [promote | add_condition | modify_condition | add_action | swap]
    TARGET_LINE: [exact current APL line, or "none" if adding new]
    NEW_LINE: [exact replacement or new APL line]
    REASON: [one sentence, citing the specific signal that motivates this]
    CONFIDENCE: [high | medium | low]

Do NOT suggest changes you cannot ground in the signal data.
Do NOT suggest changes to actions with portion_aps < 500 unless resource signal points there.
Do NOT rewrite the whole APL — targeted changes only.
Do NOT change the APL structure (sub-list organization) — change individual lines only.
```

---

## 4. LLM Output Processing

The LLM output is structured (CHANGE [N] blocks). We parse each change into a
`ProposedMutation` object with the same interface as programmatic mutations:

```python
@dataclass
class LLMMutation:
    change_type: str       # promote | add_condition | modify_condition | add_action | swap
    target_line: str       # exact APL line to match
    new_line: str          # replacement
    reason: str
    confidence: str        # high | medium | low
    source: str = "llm"    # for result tracking

    def to_apl_mutation(self, current_apl: APL) -> Optional[APL]:
        """Convert to a modified APL object, or None if target_line not found."""
        ...
```

Only `high` and `medium` confidence changes are tested.
All changes go through the SAME multi-stage DPS eval (300→3k→10k iter) as programmatic mutations.
The LLM cannot directly apply changes — it only proposes candidates.

---

## 5. When to Call the LLM

**NOT for every spec on every iteration.** The LLM is called when:

1. **Buff waste with APL_REFERENCE=NONE** — automated system is completely blind here,
   LLM is the only way to generate a fix. Call always.

2. **Overcap_rate > 15% AND no programmatic mutation improved it** — LLM may see a
   structural issue the signal mutations missed.

3. **After Layer 1 + Layer 2 converge with 0 improvement** — LLM gets one chance
   to look for things the programmatic system structurally cannot see.

4. **After talent changes** — new talents sometimes activate abilities that weren't
   in the APL. The LLM can identify these because it knows game mechanics.

**Call limit per spec per fight style:** 2 times maximum (one pre-convergence, one post).

---

## 6. Mechanics Knowledge Source

The LLM's knowledge of "which action consumes buff X" comes from:

**Primary:** The LLM's training data (WoW Wowhead, WoWDB, community guides).
  - Reliable for well-known proc interactions (manifested_demonic_soul, nightfall, etc.)
  - Unreliable for new Midnight-specific procs without wiki coverage

**Secondary:** The context block we provide (Section C above).
  - We populate this from `wowhead/{class}/{spec}/extracted/rotation.md`
  - The rotation guides explicitly name proc consumers
  - This is why Wowhead data re-extraction (task #4) matters — stale data = stale context

**Fallback:** If the LLM says "I don't know which action consumes this buff",
  we log it and skip. Do not guess.

---

## 7. Prompt Engineering Rules

These rules prevent the LLM from producing useless or harmful output:

1. **Always show the FULL APL.** LLMs hallucinate less when they can read the actual
   current state rather than reasoning from description alone.

2. **Provide signal data FIRST, APL SECOND.** The signal is the "problem statement".
   LLM should arrive at the APL knowing what it's looking for.

3. **Tell it what NOT to do.** The negative constraints (don't rewrite structure,
   don't suggest low-APS changes) prevent the most common failure mode: LLM
   proposing a "clean rewrite" that looks good but hasn't been validated.

4. **Force structured output.** Free-form commentary is useless. CHANGE [N] blocks
   are parseable. If the LLM produces narrative text, discard it.

5. **One spec at a time, never batch.** Context contamination between specs causes
   the LLM to mix up mechanics. Fresh prompt per spec.

6. **Include fight style explicitly.** A HAC (multi-target) APL has different optimal
   logic than a PW (single-target) APL. The LLM must know which it's analyzing.

---

## 8. Integration in Optimization Loop

```
Per spec, per fight style:
  1. Layer 1 (blind mutations) → converge
  2. Layer 2 (signal mutations + blind) → converge
  3. IF (buff_waste_no_reference OR overcap > 15% OR 0 improvements from 1+2):
       a. Build LLM prompt (signal data + APL + mechanics context)
       b. Call LLM → parse CHANGE blocks
       c. Convert to LLMMutation objects
       d. Test in same multi-stage eval as programmatic mutations
       e. Accept if DPS improves, reject otherwise
  4. Commit final profiles
```

The LLM suggestions go through the SAME DPS validation as everything else.
If the LLM proposes a bad change, it gets rejected. No special trust.

---

## 9. AGENTS.md Additions

Add to the APL Work section of AGENTS.md:

```
### LLM APL Advisor (Layer 3)
After programmatic optimization converges, use the LLM to find:
1. Missing buff consumers (buff with high expire rate + no APL reference)
2. Wrong condition logic (incorrect buff check type or threshold)
3. Missing synergy triggers (high-value ability not gated on its amplifier)

Call: python3 scripts/signal_apl_optimizer.py --spec X --llm-pass
The LLM proposes APL changes. All changes go through DPS validation before acceptance.
Do NOT manually apply LLM suggestions without running them through the sim.

When building LLM context, populate the "KNOWN MECHANICS" section from:
  wowhead/{class}/{spec}/extracted/rotation.md

If Wowhead data is stale (current case: 66384 vs 66709 build), note this in the
prompt. The LLM may reason about mechanics that changed between builds.
```

---

## 10. Files to Create/Modify

| File | Action | What |
|------|--------|------|
| `scripts/lib/llm_apl_advisor.py` | Create | Prompt builder + output parser |
| `scripts/signal_apl_optimizer.py` | Create | Layer 2+3 runner |
| `scripts/lib/apl_signal_extractor.py` | Create | Signal computation (covered in separate doc) |
| `docs/internal/signal_guided_apl_design.md` | Done | Programmatic signal design |
| `AGENTS.md` | Modify | Add LLM advisor to APL Work section |
| `APL_optimization.md` | Modify | Add Layer 3 section |

---

## 11. Example: Expected LLM Output for Warlock Affliction

Given the data above, a well-prompted LLM should produce:

```
CHANGE 1:
  TYPE: add_action
  TARGET_LINE: none
  NEW_LINE: actions.SH_st+=/drain_soul,if=buff.manifested_demonic_soul.react,interrupt_if=!buff.manifested_demonic_soul.up
  REASON: manifested_demonic_soul expires 96% of the time with no APL consumer;
          Soul Harvester mechanic requires drain_soul to consume this proc for bonus damage.
  CONFIDENCE: high

CHANGE 2:
  TYPE: promote
  TARGET_LINE: actions.SH_st+=/drain_soul,if=buff.nightfall.react>1
  NEW_LINE: (move above malefic_grasp line)
  REASON: drain_soul has higher portion_aps (would include manifested_soul bonus) but
          appears below malefic_grasp in the SH_st sub-list without mechanical dependency.
  CONFIDENCE: medium

CHANGE 3:
  TYPE: modify_condition
  TARGET_LINE: actions+=/drain_life,chain=1,early_chain_if=buff.nightfall.react,...
  NEW_LINE: (lower portion if manifested_demonic_soul changes make drain_life irrelevant)
  REASON: After adding manifested_demonic_soul consumer, drain_life's priority should
          be evaluated relative to the new drain_soul usage.
  CONFIDENCE: low
```

Change 1 would be tested first (high confidence). If it improves DPS, the APL
is updated and the loop re-runs. Change 3 (low confidence) might be skipped or
tested only if higher-confidence changes converge.

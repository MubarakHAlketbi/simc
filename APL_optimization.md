# APL Optimization Guide — SimulationCraft Midnight Expansion
# Class-Agnostic Structure, Rules, and Automated Improvement Loop

---

## 0. CONTEXT: APL WORK WITHIN SimC MAINTENANCE

APL development is one part of maintaining SimulationCraft. The full scope includes
upstream sync, engine fixes (C++ proc chains, scaling formulas, event sequencing),
bug hunting, feature implementation, testing, and profiles. See `AGENTS.md`.

**APL work is meaningless if the engine's damage formulas are wrong.** Before
writing or optimizing APLs, verify the engine is correct for that spec:
1. Upstream is synced — no pending engine fixes
2. Proc chains match tooltips — cross-reference sc_{class}.cpp against Wowhead
3. Tier set behavior is correct — not just "implemented" but right values
4. Scaling is sane — multi-target sweep shows reasonable per-target DPS

The APL layer can reorder actions, adjust thresholds, and change routing. It
CANNOT detect or fix engine-layer problems like broken proc chains, wrong scaling
formulas, incorrect tier set math, or crash bugs. Those require C++ code review
and engine work. See `FORK_VS_UPSTREAM_REVIEW.md` for examples of engine bugs
that our APL-focused workflow missed.

---

## 1. ANATOMY OF AN APL

An APL (Action Priority List) is an ordered list of instructions evaluated top-to-bottom
every time the actor is free to act. The first action whose condition evaluates true fires.

### 1.1 Line Syntax

  actions[.LIST_NAME][+]=ACTION[,PARAM=VALUE]*[,if=EXPR]

- actions            : the root (default) list — evaluated every GCD
- actions.precombat  : runs once before the pull, non-harmful only
- actions.SUBLIST    : named sub-lists routed into via call/run_action_list
- +=/=               : append vs. overwrite (always append after the first line)
- if=EXPR            : boolean expression; action fires only when true

### 1.2 Routing Actions

  call_action_list,name=SUBLIST[,if=EXPR]   — evaluates SUBLIST, returns on miss
  run_action_list,name=SUBLIST[,if=EXPR]    — jumps to SUBLIST permanently this GCD

Use run_action_list for mutually-exclusive hero/hero-tree branches so that only ONE
branch fires per GCD. Use call_action_list for modular blocks (trinkets, variables)
that should return control to the parent list.

### 1.3 Standard Sub-list Names (conventions used across all specs)

  precombat   : snapshot_stats, stance/form toggle, trinket variables
  variables   : computed booleans and thresholds recalculated every GCD
  trinkets    : use_item logic for both slots
  cooldowns   : major CD usage (potion, racial, external buff)
  HERONAME_st     : hero-tree single-target rotation
  HERONAME_aoe    : hero-tree multi-target rotation
  HERONAME_execute: hero-tree execute-phase rotation (if distinct)

---

## 2. EXPRESSION REFERENCE

### 2.1 Common Tokens

  talent.TALENT_NAME.ok()         talent taken (any rank)
  talent.TALENT_NAME.rank         current rank (1-4 for Midnight apex talents)
  hero_tree.HEROTREE_NAME         active hero tree
  buff.BUFF_NAME.up               buff is active
  buff.BUFF_NAME.remains          seconds remaining
  buff.BUFF_NAME.stack            current stack count
  buff.BUFF_NAME.react            buff is actually present (not predicted)
  debuff.DEBUFF_NAME.up/remains   same for target debuffs
  dot.DOT_NAME.remains            DoT seconds remaining (use <= gcd for refresh threshold)
  dot.DOT_NAME.ticking            DoT is active
  cooldown.SPELL.remains          seconds until CD is ready
  cooldown.SPELL.ready            CD is ready now (remains=0)
  rage/energy/mana/runic_power/... current resource value
  target.health.pct               target HP percentage
  target.time_to_die              predicted seconds until target dies
  active_enemies                  number of enemies in cleave/AoE range
  fight_remains                   predicted seconds left in fight
  time                            current fight time in seconds
  gcd                             current GCD duration (usually 1.5 or haste-reduced)
  gcd.remains                     time until next GCD window
  variable.VAR_NAME               value of a previously declared variable

### 2.2 Arithmetic and Boolean Operators

  +  -  *  /  %  (modulo)
  =  !=  <  >  <=  >=
  &  (AND)   |  (OR)   !  (NOT)
  ()  for grouping (always use when mixing & and |)

### 2.3 Midnight-Specific Expressions

  talent.APEX_TALENT_1.ok()       rank-1 of 4-rank apex talent
  talent.APEX_TALENT_23.rank      returns 2 or 3 when those ranks are taken
  talent.APEX_TALENT_4.ok()       capstone (rank-4) taken
  hero_tree.HEROTREE_NAME         replaces old covenant/conduit checks

### 2.4 Midnight Apex Talents — Passive vs. Active Check

  Most Midnight apex talents (4-rank, 3 spell IDs each) are PASSIVE effects
  that modify existing abilities rather than adding new buttons. Example:
    Prot Warrior Phalanx — modifies Shield Slam, no new cast.
    Shaman Lava Flows — modifies Lava Burst damage and Maelstrom gen.

  For each spec's apex talent, verify on wowhead.com/spell=ID whether it:
    a) Adds a new castable ability -> needs an APL action line
    b) Modifies an existing ability -> may need condition changes on that ability
    c) Is purely passive -> no APL changes, only C++ multiplier wiring

  When in doubt, check wowhead rotation guide for rank-specific rotation changes.

---

## 3. STRUCTURAL RULES

### Rule 1 — One variables sub-list, called first
  Compute all reusable booleans (execute_phase, st_planning, adds_remain,
  on_gcd_racials) in actions.variables. Call it at the very top of the default
  list before any action that depends on those values.

### Rule 2 — Trinkets are always a separate sub-list
  Keep trinket logic in actions.trinkets called from the default list.
  Use the standard precombat variable pattern:
    trinket_1_buffs, trinket_2_buffs, trinket_1_sync, trinket_2_sync,
    trinket_priority, damage_trinket_priority
  Sync buff-trinkets to the spec's major cooldown (e.g., avatar, recklessness,
  colossus_smash). Use %% for modulo cooldown alignment checks.

### Rule 3 — Hero-tree routing is mandatory
  Every spec has at least two hero trees (Midnight adds a third Midnight-exclusive
  option). Route them via run_action_list with hero_tree.X checks in the default
  list. Separate ST / AOE / execute sub-lists per hero tree when the rotation
  meaningfully differs. If AOE and ST share logic, merge only when confirmed by sim.

### Rule 4 — DoT refresh threshold = remaining <= gcd (or <= gcd*N for pandemic)
  Never hard-code times. Use dot.X.remains<=gcd as the default refresh threshold.
  For pandemic specs allow refreshing at <= dot.X.duration*0.3 (30% pandemic window).
  Example: rend refresh = dot.rend_dot.remains <= gcd | cooldown.colossus_smash.remains<2&dot.rend_dot.remains<=10

### Rule 5 — Never cap resources
  Spend generators before spenders when at-cap. Use rage>=100 (or class equivalent)
  as a dump trigger. For combo-point specs: spend at max stacks unless a CD window
  is within 1 GCD.

### Rule 6 — Cooldowns fire inside buff windows, not before
  Major cooldowns (avatar, recklessness, colossus_smash etc.) should be used when
  other damage amplifiers are already active or can be activated this GCD. Order:
    amplifier -> cooldown -> spender
  Exception: if the cooldown IS the amplifier, fire it first then cascade.

### Rule 7 — Execute-phase branching
  Define execute_phase in variables. For Midnight: common thresholds are
    target.health.pct < 20   (base execute)
    target.health.pct < 35   (massacre / improved execute talents)
  Use target_if=min:target.health.pct when routing to execute lists in AoE.

### Rule 8 — Racials and external buffs go in the default list, before routing
  Place berserking/blood_fury/fireblood/ancestral_call after potion, before
  run_action_list routing. Use debuff or buff conditions to align them with the
  primary cooldown window.

### Rule 9 — Conditionals must be composable and not redundant
  If an action is inside a sub-list gated by hero_tree.X, do not repeat
  hero_tree.X inside the sub-list conditions unless narrowing further.
  Avoid double-negation and always simplify: !!x => x.

### Rule 10 — Use op=setif for ternary variable assignments
  variable,name=VAR,op=setif,value=A,value_else=B,condition=EXPR
  Prefer this over two separate variable lines with inverse conditions.

---

## 4. OPTIMIZATION PRINCIPLES

### 4.1 Priority Ordering (general hierarchy, top = highest priority)

  1. Interrupt (pummel, kick) — always gate on target.debuff.casting.react
  2. Movement / charge — only at time<=0.5 or movement.distance>N
  3. Precombat resource builders (openers)
  4. Potion — align with cooldown window or fight_remains<25
  5. Major DPS cooldowns (spec's defining CD, e.g., recklessness, avatar)
  6. On-use trinkets synced to that cooldown
  7. Racials synced to that cooldown
  8. Hero-tree signature abilities (highest damage per GCD)
  9. DoT application / maintenance
  10. Combo builders / filler generators
  11. Spenders / finishers
  12. Emergency dumps (resource at-cap spenders)
  13. Weakest fillers last

### 4.2 Cooldown Alignment Score (CAS)
  For each major cooldown X, score alignment with other cooldowns:
    CAS(X) = sum over Y of: (shared_uptime(X,Y) / min(CD_X, CD_Y))
  Higher CAS = better overlap = more burst window value. If two CDs never
  naturally align (e.g., 90s vs. 40s), hold the shorter one until the longer
  fires, unless the hold cost exceeds one full cycle of the shorter CD.

### 4.3 AoE Thresholds
  For every action that is ST-only add: if=active_enemies=1 (or <=N)
  For every action that is AoE-only add: if=active_enemies>=N
  Default cleave threshold is 2+ enemies unless ability tooltip says otherwise.
  Do not use AoE spells in pure ST unless they also hit the primary target.

### 4.4 Buff Pooling (React vs. Up)
  Use buff.X.react when you must confirm the buff server-side before spending.
  Use buff.X.up when predicting availability is acceptable (e.g., procs with
  known RPPM). When in doubt use .react to avoid wasted GCDs.

### 4.5 Talent Gating
  Every action tied to a talent must be wrapped: talent.X.ok() in its condition
  or the add_action call itself. Never assume a talent is always taken.
  For 4-rank Midnight apex talents, gate per rank:
    Rank 1 effect  -> talent.APEX_1.ok()
    Rank 2-3 bonus -> talent.APEX_23.rank>=2
    Rank 4 capstone-> talent.APEX_4.ok()

---
---

## 5. Optimization Layers

Three layers of APL optimization, each building on the previous:

### Layer 1 — Blind Mutation Optimizer (DONE — all 33 specs)
Generates ~200 mutations per spec (adjacent swap, threshold sweep, promote, route),
evaluates through multi-stage funnel (300→3k→10k iter), accepts best improvement.
Script: `scripts/apl_optimizer.py`

### Layer 2 — Signal-Guided Optimizer (DESIGNED — see signal_guided_apl_design.md)
Reads per-ability APS, buff expire rates, and resource flow from sim JSON output.
Computes 4 signal types (APS inversion, buff waste, resource overcap, interval gap).
Generates ~20-30 TARGETED mutations per spec instead of 200 random ones.
Key advantage over Layer 1: can do non-adjacent promotes and add new APL constructs
(buff gates, emergency dumps) based on evidence from the sim data.
Script: `scripts/signal_apl_optimizer.py` (pending implementation)

### Layer 3 — LLM APL Advisor (DESIGNED — see llm_apl_advisor_design.md)
Closes the semantic gap that no formula can cross. Called when:
  - A buff has high expire rate AND zero APL references (no consumer found programmatically)
  - Overcap > 15% AND signal mutations didn't fix it
  - Layers 1+2 converge with 0 improvement

The LLM receives: full ability APS table, buff waste signals, resource flow, current APL,
and spec mechanic context from Wowhead rotation guides. It follows a strict reasoning
protocol (buff waste → APS order → resource → missing synergies) and outputs structured
CHANGE blocks that go through the same DPS validation funnel as programmatic mutations.
LLM suggestions that don't improve DPS are rejected. No special trust.

Key capability: "manifested_demonic_soul expires 96% of time, no APL reference" →
LLM knows this is a Soul Harvester proc consumed by drain_soul → generates the fix.
Script: `scripts/lib/llm_apl_advisor.py` (pending implementation)

---

## 5-6. Historical Pipeline & Improvement Loop

These sections documented the Wowhead data extraction pipeline (Phase 1-3)
and the automated improvement loop design. Both are now implemented:
- Pipeline status: see `project_progress.md` section 5
- Optimizer tooling: see `scripts/apl_optimizer.py` and `optimization_action_plan.md`
- Archived raw data: `docs/archive/full_spec_audit_2026-03-24.md`, `docs/archive/APL_diff_report.md`

## 7. SIM RUN COMMAND TEMPLATES

  ### Patchwerk Single-Target
  ./engine/simc                             \
    input=profiles/MID1/PROFILE.simc        \
    iterations=10000                        \
    target_error=0.1                        \
    json2=results/SPEC_patchwerk.json       \
    fight_style=Patchwerk                   \
    desired_targets=1

  ### HecticAddCleave (M+ / Add-heavy)
  ./engine/simc                             \
    input=profiles/MID1/PROFILE.simc        \
    iterations=10000                        \
    target_error=0.1                        \
    json2=results/SPEC_hecticaddcleave.json \
    fight_style=HecticAddCleave             \
    desired_targets=1

  ### Trinket Combinatorics (quick, per pair)
  ./engine/simc                             \
    input=profiles/MID1/PROFILE.simc        \
    iterations=5000                         \
    target_error=0.2                        \
    json2=results/SPEC_trinket_A_B.json     \
    fight_style=Patchwerk                   \
    trinket1=TRINKET_A,id=ITEM_ID,ilvl=XXX \
    trinket2=TRINKET_B,id=ITEM_ID,ilvl=XXX

---

## 8. COMMON MISTAKES AND HOW TO FIX THEM

  MISTAKE: DoT not refreshed before it falls off
  FIX: Add dot.X.remains<=gcd as an OR clause on the refresh action.

  MISTAKE: Major CD fires outside its burst window
  FIX: Add buff.AMPLIFIER.up or debuff.AMPLIFIER.up as a condition.

  MISTAKE: Spender fires when resource is too low to be efficient
  FIX: Add resource>=THRESHOLD condition or move the generator higher.

  MISTAKE: AoE action fires in ST, diluting priority
  FIX: Gate with if=active_enemies>=2 (or appropriate threshold).

  MISTAKE: Trinket fires with no CD or buff active
  FIX: Sync to the spec's major cooldown using buff.X.up or cooldown.X.remains<2.

  MISTAKE: Duplicate conditions across many actions
  FIX: Extract to a named variable in actions.variables.

  MISTAKE: Action for a talent that does not exist in init_spells()
  FIX: Register the talent ID, then re-verify with a 1-iteration sim.

  MISTAKE: Two adjacent actions with no conditions — order matters
  FIX: Run a swap sim. Let the higher expected DPCT action go first.

  MISTAKE: execute_phase not using the massacre/improved_execute talent check
  FIX: variable.execute_phase = (talent.massacre.enabled&target.health.pct<35)|target.health.pct<20

  MISTAKE: Hero tree sub-list missing from routing in default list
  FIX: Add run_action_list,name=HERONAME_st,if=hero_tree.HERONAME&active_enemies=1

  MISTAKE: Midnight apex talent checked with .ok() when rank 4 specific behavior needed
  FIX: Use talent.APEX_4.ok() for the capstone. Use talent.APEX_1.ok() for rank-1.

  MISTAKE: APL optimized only for one fight style without considering the other
  FIX: Optimize each fight style independently. Each spec has TWO optimal APLs:
       one for Patchwerk (ST) and one for HecticAddCleave (AoE/M+).

  MISTAKE: APL works for one talent build but breaks another
  FIX: Gate build-specific actions with talent.X.ok(). Validate all builds (Section 6.2).

---

## 9. QUICK VALIDATION CHECKLIST (before committing any APL change)

  ### Engine Correctness (verify BEFORE APL work — see AGENTS.md)
  [ ] Upstream is synced (no pending engine fixes for this class)
  [ ] C++ class module reviewed (no unresolved TODO/FIXME/NYI)
  [ ] Multi-target sweep (1,3,5,10) shows sane scaling
  [ ] Tier set on/off shows tooltip-matching DPS delta
  [ ] Proc rates in JSON match expected RPPM/ICD from tooltips

  ### APL Changes (after making changes)
  [ ] 1-iteration sim completes with no crash or assertion failure
  [ ] All actions appear in sim report (zero actions with 0 executes and no condition)
  [ ] action_dpet table has no unexpected zeros for normally-cast spells
  [ ] DPS is >= previous baseline for the fight style being optimized
  [ ] Both fight styles have independently validated optimal APLs
  [ ] No single talent build regresses more than 2%
  [ ] All talents referenced in conditions are registered in init_spells()
  [ ] No DEAD_CONDITION flags (unknown buff/debuff/talent names)
  [ ] DoT uptime % for maintained DoTs is >= 95% in the sim report
  [ ] Resource waste (overcap) is < 5% of total resource generated
  [ ] Major cooldown usage % is >= 95% of expected usage opportunities

---

## 10-15. Historical Validation & Comparison Data

These sections contained per-spec validation results and the 3-way upstream
APL comparison study (198 sims, 10k iterations, 33 specs). Key findings are
preserved in `project_progress.md` sections 4 and 7.

Archived raw data: `docs/archive/`

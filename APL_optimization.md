# APL Optimization Guide — SimulationCraft Midnight Expansion
# Class-Agnostic Structure, Rules, and Automated Improvement Loop

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

## 5. DATA PIPELINE — FROM WOWHEAD TO OPTIMIZED APL

This section defines the end-to-end pipeline for each spec.

### Phase 1 — Data Extraction (Browser-Based)

  For each spec, extract from wowhead using extract_wowhead_tabs.py:

  Pages to extract:
    1. rotation    — rotation-cooldowns-pve-{role}
       Click through: each hero talent switch x each tab (ST, AoE, Opener, Pre-Combat)
       Output: wowhead/<class>/<spec>/extracted/rotation.md

    2. talents     — talent-builds-pve-{role}
       Extract: all talent build names + export codes (base64 strings)
       Output: wowhead/<class>/<spec>/extracted/talents.md

    3. bis         — bis-gear (no role suffix)
       Extract: recommended gear per slot, trinket recommendations
       Output: wowhead/<class>/<spec>/extracted/bis.md

    4. consumables — enchants-gems-pve-{role}
       Extract: flask, potion, food, weapon buff, rune, enchants per slot
       Output: wowhead/<class>/<spec>/extracted/consumables.md

    5. tier        — tier-set-bonuses (no role suffix)
       Extract: 2pc and 4pc bonus effects, which tier pieces to equip
       Output: wowhead/<class>/<spec>/extracted/tier.md

  URL construction pattern (from generate_links.sh):
    https://www.wowhead.com/guide/classes/{class}/{spec}/{page_slug}

  Role mapping:
    Tank:  blood, vengeance, guardian, brewmaster, protection
    DPS:   everything else

  The extraction script (wowhead/extract_wowhead_tabs.py) handles all tab
  clicking and content capture. Run per-spec or --all for batch.

  CRITICAL: Wowhead hides rotation priorities, talent builds, and gear
  recommendations behind JavaScript tabs. web_extract / curl CANNOT access
  this content. The browser-based extraction is MANDATORY.

  IMPORTANT — EVERY SPEC HAS A DIFFERENT TAB LAYOUT:
    The extraction script is DISCOVERY-BASED, not hardcoded. It discovers:
    - Hero talent switch buttons (may appear ABOVE or INSIDE content tabs)
    - Content tab groups (names vary: "AoE Priority" vs "Multitarget" vs "Cleave")
    - Cooldown sub-tabs (different count per spec: 3 for warlock, 5 for warrior)
    - Advanced tips sub-tabs (different structure per spec)
    - Per-talent-point toggle buttons that adapt the displayed rotation to
      specific talent choices (these appear/disappear based on active tab)

    The script finds all [role="tab"], [role="tablist"], and button elements,
    classifies them (hero switch vs content tab vs talent toggle), then clicks
    through EVERY combination, re-discovering after each click since the page
    structure changes dynamically.

    It outputs both .md (human-readable) and .json (programmatic consumption).

### Phase 2 — Profile Construction

  For each spec, for each talent build from Phase 1:

  a. Start from the BiS gear template (extracted/bis.md)
  b. Apply the talent export code (extracted/talents.md)
  c. Apply consumables (extracted/consumables.md): flask, potion, food, enchants
  d. Apply tier set pieces as indicated by extracted/tier.md
  e. Save as: profiles/MID1/MID1_{Spec}_{HeroTree}_{BuildName}.simc

  Trinket slots are left as the "default" BiS trinket pair initially.
  Trinket combinatorics happen in Phase 5 after the APL is optimized.

### Phase 3 — Base APL Construction

  For each spec, write the initial APL from extracted rotation data:

  a. Read extracted/rotation.md — it contains ST, AoE, opener, cooldown usage
     for each hero talent variant.
  b. Translate the human-readable priority into SimC APL syntax.
  c. Cross-reference with info_base.md for spell IDs and talent names.
  d. Validate against the EXISTING C++ APL in engine/class_modules/apl/:
     - DIFF the current C++ APL vs the wowhead-derived APL.
     - Keep actions from the existing APL that are correct/equivalent.
     - Only change lines where the wowhead rotation explicitly differs.
     - This avoids regressing already-working logic.

### Phase 4 — APL Optimization Loop

  See Section 6 for the full automated loop.

### Phase 5 — Trinket Combinatorics

  After the APL is optimized, run trinket pair simulations:

  a. From extracted/bis.md, collect ALL mentioned trinkets (typically 4-8).
  b. Generate all unique pairs: C(N,2) combinations.
  c. For each pair, for each fight style (Patchwerk + HecticAddCleave):
     sim using the optimized APL and the best talent build.
  d. Rank pairs by composite DPS (see Section 6.1 for weighting).
  e. Update the canonical profile with the best trinket pair per fight style.
  f. If the trinket pair changes rotation priorities (e.g., proc-based trinket),
     re-run Phase 4 optimization loop with the new trinkets equipped.

---

## 6. AUTOMATED IMPROVEMENT LOOP

### 6.1 Fight Styles and Composite Scoring

  Two fight styles, weighted equally:
    Patchwerk        weight = 0.50   (pure ST / sustained boss damage)
    HecticAddCleave  weight = 0.50   (M+ and add-heavy raid encounters)

  Composite DPS = 0.50 * DPS_patchwerk + 0.50 * DPS_hecticaddcleave

  Acceptance rule for APL changes:
    composite_new > composite_old
    AND neither fight style regresses more than 1.0%

### 6.2 Multi-Build Validation

  Each spec has multiple talent builds (typically 4-8 from wowhead).
  The APL must work for ALL builds without catastrophic regression.

  Validation matrix per spec:
    For each talent build B:
      For each fight style F:
        Sim(B, F) -> DPS(B,F)

  A candidate APL change is accepted only if:
    1. The BEST build's composite improves (or stays within 0.1%)
    2. No build regresses more than 2.0% on any fight style
    3. The average across all builds improves

  For practical purposes during the optimization loop, use the TOP 2 builds
  (most popular / highest baseline DPS) for rapid iteration. Validate against
  ALL builds only at convergence before final commit.

### 6.3 Gear Handling During Optimization

  Use a FIXED gear template per spec (from BiS extraction).
  The gear does not change during the APL optimization loop.
  Tier set bonuses are always equipped if recommended by the tier page.

  Gear-aware variables to set in precombat:
    variable,name=has_tier_2pc,value=set_bonus.tier1.2pc
    variable,name=has_tier_4pc,value=set_bonus.tier1.4pc

  These allow the APL to branch on tier bonus availability without
  needing separate APL versions per gear set.

### 6.4 The Loop

  The loop iterates until DPS delta between iterations < 0.1%
  or MAX_ITERATIONS is reached.

  #### Step 0 — Baseline
    a. Compile the current APL from the C++ generator.
    b. Run sims on the canonical MID1 profile:
       - Patchwerk (iterations=10000, target_error=0.1)
       - HecticAddCleave (iterations=10000, target_error=0.1)
    c. Record baseline composite DPS = B.

  #### Step 1 — Coverage Audit
    For each spell registered in the spec's init_spells():
      - Check if it appears in the APL.
      - If missing and it has a non-zero DPS weight (not CC/healing/utility):
        flag as MISSING_ACTION candidate.
    For each action in the APL:
      - Check if every referenced talent, buff, or debuff exists in the C++ module.
      - Flag any unknown reference as DEAD_CONDITION.

  #### Step 2 — Variable Extraction
    Scan all conditions in the APL for repeated sub-expressions with 3+ characters.
    If a sub-expression appears in 3+ actions: extract to actions.variables.
    This reduces condition evaluation overhead and improves readability.

  #### Step 3 — Permutation Candidates
    Generate a ranked list of swap candidates:
      a. Adjacent action pairs in the same sub-list where swapping might increase DPS.
         Priority: if action A has higher expected DPCT than action B immediately above it.
      b. Condition tightening: add a condition to an unconditional filler to restrict
         it to windows where it is more valuable.
      c. Condition loosening: remove an overly-restrictive condition that causes
         the action to be skipped when it should fire.

    Candidate scoring formula (heuristic, pre-sim):
      score = (spell_coeff * avg_damage_modifier * cast_frequency) / gcd_cost

  #### Step 4 — Sim Each Candidate
    For each candidate permutation P:
      a. Apply P to a copy of the APL.
      b. Run BOTH fight styles (Patchwerk + HecticAddCleave).
      c. Calculate composite DPS.
      d. If composite(P) > current_best AND no single fight style regresses >1%:
         accept P as new baseline.
      e. If not: discard P.
    Evaluate at most 20 candidates per iteration to limit compute time.

  #### Step 5 — Condition Sweep
    For numeric thresholds in conditions (stack counts, time thresholds, HP%):
      a. Sweep the threshold ±20% in 5% steps.
      b. Run BOTH fight styles per step (5000 iterations each).
      c. Accept the value that yields the highest composite.

  #### Step 6 — Multi-Build Validation
    Run the updated APL against ALL talent builds (not just the top 2):
      For each build: sim Patchwerk + HecticAddCleave.
    Check: no build regresses >2% on any fight style.
    If any build regresses: investigate and add talent-gated conditions.

  #### Step 7 — Convergence Check
    If composite_new - composite_prev < 0.1% AND no flags remain:
      -> DONE. Write final APL back to the C++ generator and commit.
    Else:
      -> Increment iteration counter. If counter < MAX_ITERATIONS: go to Step 1.
      -> If counter >= MAX_ITERATIONS: report remaining candidates for manual review.

  #### Step 7a — MAX_ITERATIONS recommendation
    Set MAX_ITERATIONS = 10 for routine passes.
    Set MAX_ITERATIONS = 25 for new spec APLs being written from scratch.

  #### Step 8 — LLM-Assisted Review (Optional, per-spec)
    After the automated loop converges, apply LLM reasoning:
      a. Feed the final APL + the spec's info_base.md to the LLM.
      b. Ask: "Are there talent interactions or priority orderings that the
         automated loop may have missed?"
      c. LLM proposes candidates -> sim them as in Step 4.
      d. Accept only if composite improves. Do NOT accept LLM suggestions
         that are purely theoretical without sim validation.

    This step is ONLY useful when the info_base.md contains mechanic details
    that create non-obvious synergies (e.g., two talents that interact in ways
    the simple swap/sweep loop cannot discover).

---

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

  MISTAKE: APL optimized only for Patchwerk, underperforms on HecticAddCleave
  FIX: Always validate both fight styles. Use composite scoring (Section 6.1).

  MISTAKE: APL works for one talent build but breaks another
  FIX: Gate build-specific actions with talent.X.ok(). Validate all builds (Section 6.2).

---

## 9. QUICK VALIDATION CHECKLIST (before committing any APL change)

  [ ] 1-iteration sim completes with no crash or assertion failure
  [ ] All actions appear in sim report (zero actions with 0 executes and no condition)
  [ ] action_dpet table has no unexpected zeros for normally-cast spells
  [ ] DPS is >= previous baseline on BOTH fight styles (Patchwerk + HecticAddCleave)
  [ ] No single talent build regresses more than 2%
  [ ] All talents referenced in conditions are registered in init_spells()
  [ ] No DEAD_CONDITION flags (unknown buff/debuff/talent names)
  [ ] DoT uptime % for maintained DoTs is >= 95% in the sim report
  [ ] Resource waste (overcap) is < 5% of total resource generated
  [ ] Major cooldown usage % is >= 95% of expected usage opportunities

---

## 10. EXISTING APL VALIDATION (before rewriting)

  Before writing a new APL from wowhead data, ALWAYS diff against the existing
  C++ APL generator for that spec:

  Location: engine/class_modules/apl/apl_{classname}.cpp

  Steps:
    1. Generate the current APL from the C++ code (run 1-iter sim, check output).
    2. Compare each action line against the wowhead rotation priorities.
    3. Categorize differences:
       a. MATCH      — existing APL already implements the wowhead priority correctly.
       b. ORDER_DIFF — same actions, different priority order -> sim both, keep winner.
       c. MISSING    — wowhead mentions an action the APL doesn't have -> add candidate.
       d. EXTRA      — APL has an action wowhead doesn't mention -> keep if sim confirms value.
       e. CONDITION  — same action, different conditions -> sim both, keep winner.
    4. Only change lines that fall into categories B, C, or E.
    5. Lines in category A stay untouched. Lines in category D stay unless sim disproves.

---

## 11. SPEC ROSTER AND URL MAPPING

  ### DPS Specs (24)
  | Class         | Spec          | Role | Hero Trees                            |
  |---------------|---------------|------|---------------------------------------|
  | death-knight  | frost         | dps  | deathbringer, rider-of-the-apocalypse |
  | death-knight  | unholy        | dps  | rider-of-the-apocalypse, sanlayn      |
  | demon-hunter  | havoc         | dps  | aldrachi-reaver, fel-scarred          |
  | demon-hunter  | devourer      | dps  | annihilator, void-scarred             |
  | druid         | balance       | dps  | elunes-chosen, keeper-of-the-grove    |
  | druid         | feral         | dps  | druid-of-the-claw, wildstalker        |
  | evoker        | devastation   | dps  | flameshaper, scalecommander           |
  | evoker        | augmentation  | dps  | chronowarden, scalecommander          |
  | hunter        | beast-mastery | dps  | dark-ranger, pack-leader              |
  | hunter        | marksmanship  | dps  | dark-ranger, sentinel                 |
  | hunter        | survival      | dps  | pack-leader, sentinel                 |
  | mage          | arcane        | dps  | spellslinger, sunfury                 |
  | mage          | fire          | dps  | frostfire, sunfury                    |
  | mage          | frost         | dps  | frostfire, spellslinger               |
  | monk          | windwalker    | dps  | conduit-of-the-celestials, shado-pan  |
  | paladin       | retribution   | dps  | herald-of-the-sun, templar            |
  | priest        | shadow        | dps  | archon, voidweaver                    |
  | rogue         | assassination | dps  | deathstalker, fatebound               |
  | rogue         | outlaw        | dps  | fatebound, trickster                  |
  | rogue         | subtlety      | dps  | deathstalker, trickster               |
  | shaman        | elemental     | dps  | farseer, stormbringer                 |
  | shaman        | enhancement   | dps  | stormbringer, totemic                 |
  | warlock       | affliction    | dps  | hellcaller, soul-harvester            |
  | warlock       | demonology    | dps  | diabolist, soul-harvester             |
  | warlock       | destruction   | dps  | diabolist, hellcaller                 |
  | warrior       | arms          | dps  | colossus, slayer                      |
  | warrior       | fury          | dps  | mountain-thane, slayer                |

  ### Tank Specs (6)
  | Class         | Spec          | Role | Hero Trees                            |
  |---------------|---------------|------|---------------------------------------|
  | death-knight  | blood         | tank | deathbringer, sanlayn                 |
  | demon-hunter  | vengeance     | tank | aldrachi-reaver, annihilator          |
  | druid         | guardian      | tank | druid-of-the-claw, elunes-chosen      |
  | monk          | brewmaster    | tank | master-of-harmony, shado-pan          |
  | paladin       | protection    | tank | lightsmith, templar                   |
  | warrior       | protection    | tank | colossus, mountain-thane              |

  URL patterns:
    Guides:    https://www.wowhead.com/guide/classes/{class}/{spec}/{page}-pve-{role}
    BiS Gear:  https://www.wowhead.com/guide/classes/{class}/{spec}/bis-gear
    Tier Sets: https://www.wowhead.com/guide/classes/{class}/{spec}/tier-set-bonuses
    Talents:   https://www.wowhead.com/talent-calc/{class}/{spec}/{hero-tree}

---

## 12. FILE LOCATIONS

  APL C++ generators       : engine/class_modules/apl/apl_CLASSNAME.cpp
  MID1 profiles            : profiles/MID1/MID1_SPECNAME_HERONAME.simc
  Example APL output       : example_apl_SPECNAME.md  (generated, do not hand-edit)
  Wowhead info base        : wowhead/CLASS/SPEC/info_base.md
  Wowhead info links       : wowhead/CLASS/SPEC/info_links.md
  Browser-extracted data   : wowhead/CLASS/SPEC/extracted/{rotation,talents,bis,consumables,tier}.md
  Tab extractor script     : wowhead/extract_wowhead_tabs.py
  Link generator script    : wowhead/generate_links.sh
  This document            : APL_optimization.md
  Progress tracker         : project_progress.md

---

## 13. IMPLEMENTATION CHECKLIST

  [ ] simc binary is compiled and accessible at engine/simc (or in PATH)
  [ ] playwright installed for browser extraction (pip install playwright && playwright install chromium)
  [ ] extract_wowhead_tabs.py tested on at least one spec
  [ ] Canonical MID1 profiles exist for each spec being optimized
  [ ] A sim runner script accepts: profile, APL override, iterations, output=json
  [ ] A diff tool compares two APL strings and produces a human-readable delta
  [ ] A parser reads simc JSON output and extracts: mean_dps, dps_error, action_dpet
  [ ] Candidate generator reads the C++ APL file and produces permutations
  [ ] Accept/reject logic uses composite scoring (Section 6.1)
  [ ] Multi-build validation runs across all talent builds (Section 6.2)
  [ ] Loop controller tracks iteration state and writes accepted APL back to .cpp

---

## 14. EXAMPLE IMPROVEMENT ITERATION (Arms Warrior reference)

  Baseline: actions.colossus_st has demolish unconditionally after colossus_smash.
  Problem: demolish fires even at 0 colossal_might stacks — low value.
  Observation from action_dpet: demolish DPET drops 18% when stacks<5.
  Fix: add if=buff.colossal_might.stack>=5|talent.master_of_warfare.rank=4
  Validation:
    Patchwerk:        +1.3% DPS
    HecticAddCleave:  +0.9% DPS
    Composite:        +1.1%
    No talent build regresses. ACCEPTED.

  Next: sweeping_strikes condition check in colossus_st:
  Old: sweeping_strikes,if=active_enemies=2&cooldown.colossus_smash.remains&buff.sweeping_strikes.down
  Problem: fires mid-CS window, wasting the window for direct damage.
  Fix: add |!talent.broad_strokes to always keep SS up without broad_strokes.
  Validation:
    Patchwerk:        +0.0% (ST, no change expected)
    HecticAddCleave:  +0.4%
    Composite:        +0.2%
    ACCEPTED.

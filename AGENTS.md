# AGENTS.md — SimulationCraft Midnight Agent Guide

**Last Updated: 2026-03-31**

Read this file first every session. Then read `project_progress.md` — it is the
single source of truth for all project status, known issues, and what to do next.

---

## Mission

We maintain a SimulationCraft fork for the WoW Midnight expansion. That means
the FULL scope of software maintenance:

- **Upstream sync** — merge engine fixes, DBC updates, class module patches
- **C++ engine work** — fix bugs, implement new mechanics, wire proc chains
- **Feature implementation** — new spells, trinkets, tier sets, apex talents
- **Bug hunting** — find and fix crashes, scaling errors, proc chain bugs, event issues
- **APL development** — write, fix, and improve action priority lists
- **Profile management** — gear, talents, consumables, fight style variants
- **Testing** — correctness testing, not just smoke tests. Multi-target sweeps,
  tier set verification, proc rate validation, regression detection
- **Optimization** — talent builds and APL tuning (ONE activity among many)
- **Documentation** — keep docs current, track progress, record lessons
- **Contribution** — push fixes and improvements back upstream

**We are maintainers, not just optimizers.** Our previous workflow focused
exclusively on data extraction + APL/talent optimization while treating the C++
engine as an untouchable black box. This caused us to miss 181 upstream commits
including crash fixes, proc chain rewrites, scaling corrections, and tier set
math errors. See `FORK_VS_UPSTREAM_REVIEW.md` for the full post-mortem.

---

## Session Start Checklist

Every session, in order:

```
1. Read this file + project_progress.md
2. Check upstream:
     git fetch upstream midnight
     git log --oneline HEAD..upstream/midnight | head -30
3. If upstream has new commits:
   a. Review them — categorize as engine fix / DBC update / APL change / profile
   b. Rebase:  git rebase upstream/midnight
   c. Rebuild: cmake --build build -j$(nproc) && cp build/simc engine/simc
   d. Re-validate: python3 scripts/validate_all_profiles.py
   e. If engine fixes affect specific specs, re-baseline those specs
4. Check project_progress.md "What's Next" for current priorities
5. Pick work based on priority: bugs > engine fixes > features > APL/profiles > optimization
```

---

## Work Categories (priority order)

### 1. Upstream Sync & Engine Fixes (highest priority)
Upstream SimC is actively developed. Engine-level fixes (proc chains, scaling
formulas, crash fixes, event sequencing) affect simulation CORRECTNESS. No
amount of APL optimization matters if the underlying math is wrong.

**How:** `git fetch upstream midnight`, review commits, rebase, rebuild, test.
When upstream fixes a class module, read the diff, understand what changed, and
verify it works with our profiles.

### 2. Bug Hunting & Fixing
Actively look for bugs in the engine — don't wait for upstream to find them.

**Categories of bugs to look for:**
- **Proc chain errors** — spell X should trigger Y but doesn't (or does when it shouldn't)
- **Scaling bugs** — damage/healing/resource scales incorrectly with targets, stats, or buffs
- **Crash/safety** — segfaults, null pointers, event manager stuck conditions
- **Tier set math** — set bonus applies wrong multiplier or triggers wrong mechanic
- **Snapshotting** — buffs not captured correctly at cast time
- **Timing** — missing delays, wrong event scheduling, race conditions

**Detection methods:**
- C++ code review (`grep TODO|FIXME|HACK|NYI` in class modules)
- Multi-target sweep (sim at 1,3,5,10 targets — catches AoE scaling bugs)
- Tier set delta (sim with/without tier — catches wrong math)
- Proc rate check (compare JSON execute counts vs expected RPPM/ICD from tooltips)
- Cross-reference Wowhead spell tooltips against C++ implementation
- Compare sim DPS against in-game data or community benchmarks when available

### 3. Feature Implementation
New spells, trinkets, mechanics, and interactions that aren't yet in the sim.

**How:** Check `unique_gear_midnight.cpp` for NYI items, check class modules
for TODO comments, cross-reference Wowhead patch notes against implemented features.

### 4. APL & Profile Work
Write and maintain action priority lists and character profiles.

**How:** Use Wowhead extracted data as reference, compare upstream APLs,
run optimization tooling. Each spec has TWO profiles — Patchwerk and HAC.

### 5. Optimization (lowest priority — only when engine is correct)
Talent hill-climbing and APL mutation optimization.

**Only run optimization when:**
- Upstream is synced (no pending engine fixes)
- Engine correctness is verified for the spec
- Baselines are fresh (post-sync)

---

## File Map

### Documentation (root)
| File | What It Is |
|------|------------|
| `project_progress.md` | **THE master doc** — status, issues, next steps, all data |
| `APL_optimization.md` | APL technical reference — syntax, expressions, rules, common mistakes |
| `project_structure.md` | Codebase navigation — maps task types to source files |
| `optimization_action_plan.md` | Optimization design — talent local search + APL optimizer |
| `OPTIMIZATION_HOWTO.md` | Step-by-step manual guide — exact commands to optimize any spec |
| `FORK_VS_UPSTREAM_REVIEW.md` | Fork vs upstream divergence analysis + post-mortem |
| `docs/internal/darkmoon_investigation.md` | Darkmoon trinket investigation — blocked on beta data (Issue #81) |

### Archived (historical reference only)
| File | What |
|------|------|
| `docs/archive/full_spec_audit_2026-03-24.md` | Raw per-class audit data (5136 lines) |
| `docs/archive/APL_diff_report.md` | APL diff results — regenerable with `wowhead/gen_apl_diff.py` |

### Tooling (`scripts/`)
| Script | What |
|--------|------|
| `scripts/optimize_all.py` | Master orchestrator — `--report`, `--apl --all`, `--spec X` |
| `scripts/apl_optimizer.py` | APL optimization loop — mutation + multi-stage evaluation |
| `scripts/talent_build_compare.py` | Wowhead talent build comparison (all 33 specs) |
| `scripts/talent_local_search.py` | Hill-climbing talent optimizer with validated neighbors |
| `scripts/validate_all_profiles.py` | Validate all profiles against tree constraints |
| `scripts/lib/sim_runner.py` | SimC runner — parallel sims, JSON parse, composite scoring |
| `scripts/lib/apl_parser.py` | APL parser/serializer — .simc ↔ structured data |
| `scripts/lib/apl_mutations.py` | 4 mutation operators — swap, sweep, promote, route |
| `scripts/lib/talent_tree.py` | DBC talent tree parser + real TraitEdge.csv prerequisite edges |
| `scripts/lib/talent_codec.py` | Talent string codec — decode/encode base64 talent strings |
| `scripts/lib/tree_codec_bridge.py` | Bridge — connects tree + codec, high-level API |
| `scripts/lib/talent_validator.py` | Build validation (budget, prereqs, gates) + neighbor generation |

### Wowhead Data (reference game data)
| Path | What |
|------|------|
| `wowhead/{class}/{spec}/extracted/rotation.md` | Rotation priorities (all hero talents × tabs) |
| `wowhead/{class}/{spec}/extracted/talents.md` | Talent builds with export codes |
| `wowhead/{class}/{spec}/extracted/bis.md` | BiS gear by slot |
| `wowhead/{class}/{spec}/extracted/tier.md` | Tier set bonus effects |
| `wowhead/{class}/{spec}/extracted/consumables.md` | Enchants, gems, potions, food |
| `wowhead/extract_wowhead_tabs.py` | Browser extractor (Playwright/Chromium) |
| `wowhead/gen_apl_diff.py` | APL diff generator script |

**Rule:** Always use `extracted/` files. `info_base.md` is deprecated (misses JS content).

### Source Code
| What | Where |
|------|-------|
| Class modules | `engine/class_modules/sc_{class}.cpp` |
| APL generators | `engine/class_modules/apl/apl_{class}.cpp` |
| APL overrides (.simc) | `ActionPriorityLists/default/` |
| Upstream APL reference | `ActionPriorityLists/cloned_default/` |
| Midnight gear/trinkets | `engine/player/unique_gear_midnight.cpp` |
| MID1 profiles (PW) | `profiles/MID1/MID1_{Class}_{Spec}[_{Variant}].simc` |
| MID1 profiles (HAC) | `profiles/MID1/MID1_{Class}_{Spec}[_{Variant}]_HAC.simc` |
| Phase 4 baselines | `results/phase4/*.json` (112 files) |
| DBC talent data | `engine/dbc/generated/trait_data.inc` (3420 entries) |
| Talent prerequisite edges | `engine/dbc/generated/TraitEdge.csv` (6409 Type 2 edges) |
| Talent gate conditions | `engine/dbc/generated/TraitCond.csv`, `TraitNodeGroup*.csv` |
| Talent node DB2 data | `engine/dbc/generated/TraitNode.csv`, `TraitNodeXTraitNodeEntry.csv` |
| Talent string parse/encode | `engine/player/player.cpp` lines 2675-3030 |

### Build
```bash
cmake -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON
cmake --build build -j$(nproc)
cp build/simc engine/simc
```

---

## Common Commands

```bash
# Upstream sync
git fetch upstream midnight
git log --oneline HEAD..upstream/midnight | head -30
git rebase upstream/midnight
cmake --build build -j$(nproc) && cp build/simc engine/simc

# Smoke test (1 iter, catches parse errors)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=1 output=/dev/null

# Baseline (Patchwerk)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc fight_style=Patchwerk \
  target_error=0.1 threads=16 json2=results/phase4/MID1_Warrior_Fury_patchwerk.json output=/dev/null

# Baseline (HecticAddCleave)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc fight_style=HecticAddCleave \
  target_error=0.1 threads=16 json2=results/phase4/MID1_Warrior_Fury_hecticaddcleave.json output=/dev/null

# Multi-target sweep (catches AoE scaling bugs)
for N in 1 3 5 10; do
  ./engine/simc profiles/MID1/${SPEC}.simc fight_style=Patchwerk \
    desired_targets=$N iterations=1000 threads=16 \
    json2=/tmp/${SPEC}_${N}t.json output=/dev/null
done

# Tier set delta (catches wrong math)
./engine/simc profiles/MID1/${SPEC}.simc iterations=3000 threads=16 \
  json2=/tmp/tier_on.json output=/dev/null
./engine/simc profiles/MID1/${SPEC}.simc iterations=3000 threads=16 \
  set_bonus=tier33_2pc=0 set_bonus=tier33_4pc=0 \
  json2=/tmp/tier_off.json output=/dev/null

# Extract engine-generated APL
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=0 \
  save_actions=/tmp/actions.simc output=/dev/null

# Baseline report
python3 scripts/optimize_all.py --report

# Talent optimization (single spec)
python3 scripts/talent_local_search.py --spec warrior_fury --fight-style Patchwerk --max-iter 3

# APL optimization (single spec)
python3 scripts/apl_optimizer.py --spec warrior_fury --max-iter 5

# Validate all profiles
python3 scripts/validate_all_profiles.py

# Re-extract Wowhead data
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation

# Check class module for known issues
grep -n 'TODO\|FIXME\|HACK\|NYI' engine/class_modules/sc_warrior.cpp
```

**Optimization model:** Each spec has TWO independent optimal talent/APL builds:
one for Patchwerk (single-target raid) and one for HecticAddCleave (M+/AoE).
Composite DPS (0.50 × PW + 0.50 × HAC) is reported for reference only — it is
NOT used for optimization decisions. Always optimize each fight style separately.

---

## Domain Knowledge — SimC Internals

### Midnight Point Budgets (Level 90)
- **Class tree**: 34 purchasable points + granted nodes (free, don't cost points)
- **Spec tree**: 34 purchasable points
- **Hero tree**: 15 nodes auto-granted (one hero tree chosen via selection node)

### Talent Gate System (req_points)
The game uses a **currency-based gate system**, not a simple "total ranks" check:
- Each tree has 2-3 gates at specific `req_points` thresholds (e.g., Warrior class: 8, 23)
- Gates require `SpentAmountRequired` of a specific `TraitCurrencyID` to be spent
- **Only PURCHASED nodes consume currency** — granted nodes cost 0
- Currency 2801 = class talent points, Currency 2800 = spec talent points
- Gate check: `purchased_ranks_in_nodes_with_req_points_less_than_gate >= gate`
- DB2 chain: TraitNodeGroup → TraitNodeGroupXTraitCond → TraitCond
- Hero tree nodes are exempt from gate checks (auto-granted package)

### Granted Class Talents per Spec
Not every spec has 1 free talent — it varies:

| Grants | Specs |
|--------|-------|
| 0 | Warlock (all 3 — Soul Leech granted via undocumented DBC mechanism, hardcoded in validator) |
| 1 | DH, DK, Hunter, Mage, Rogue, Shaman (18 specs) |
| 2 | Evoker, Monk, Priest, Warrior (13 specs) |
| 3 | Druid, Paladin (10 specs) |

Granted nodes are detected by `id_spec_starter` containing the spec ID, PLUS hero tree
starting nodes (row=1), PLUS undocumented grants (Warlock Soul Leech node 71933).

### Hero Tree Sharing
Hero trees are shared between 2 specs per class. Critical facts:
- Internal hero nodes may be tagged with only ONE spec's `id_spec`, but BOTH specs can use them.
  Example: Scalecommander nodes are all tagged `spec=[1467]` (Devastation) but Augmentation uses them too.
- SimC's parser confirms: "hero talents don't seem to require a matching id_spec_set" (player.cpp ~line 2929).
- Each hero tree has 2 different row-1 starting nodes (one per spec), rest shared.
- Some hero trees are only discoverable via **selection nodes** (tree_index=4), not starting nodes.
  Example: Evoker Aug + Chronowarden — no Aug-tagged starting node exists, but selection node 99825
  references subtree 38 (Chronowarden) with spec=[1473] (Aug).
- The talent tree builder uses a 2-pass approach: first discover available sub-trees from both
  hero starting nodes AND selection nodes, then include ALL nodes from those sub-trees.

### Talent Prerequisite Edges
- **TraitEdge.csv**: 6,409 real Type 2 edges from DB2 `TraitEdge` table (build 12.0.1.66384).
- **Type 2** = class/spec/hero talent prerequisites. **Type 0** = professions/dragonriding (ignored).
- Direction: `LeftTraitNodeID` (parent) → `RightTraitNodeID` (child). Child requires at least 1 parent selected (OR logic).
- 40 nodes have NO edges: 33 row-11 apex talents + row-1 roots. These use `req_points` gates only.
- Old heuristic (row-adjacency, col-distance ≤ 1) had 77.7% precision, 90.1% recall — replaced with real edges.
- Source: DB2 `TraitEdge` table via wago.tools. For PTR builds, re-download from `https://wago.tools/db2/TraitEdge/csv`.

### Midnight 4-Rank Apex Talents
Every spec has ONE new 4-rank talent using 3 spell IDs:
- Rank 1 = spell ID A (base effect)
- Rank 2-3 = spell ID B (same ID, different numeric value per rank)
- Rank 4 = spell ID C (capstone effect)

In C++ these need 3 `player_talent_t` fields: `talent_rank_1(ID_A)`, `talent_rank_23(ID_B)`,
`talent_rank_4(ID_C)`. All 33 specs have this pattern. IDs are in the 1240000+ range.

### Talent String Encoding
SimC talent strings are base64-encoded bitstreams. Critical facts:
- **Node ordering**: iterate ALL nodes for the class by ascending `id_node` (not spec-filtered).
  Warrior has 208 total nodes across all 3 specs — the bitstream includes ALL of them.
- **Bit layout**: version(8) + spec_id(16) + tree_hash(128, zero-filled) + per-node bits
- **Per node**: selected(1b) → purchased(1b) → [partial(1b) + rank(6b) if partial] → [choice(1b) + index(2b) if choice]
- **Node types**: NORMAL=0, TIERED=1, CHOICE=2, SELECTION=3 (NOT 4 — there is no type 4)
- **Granted nodes**: `purchased=0` (not purchased). A node is granted if:
  - Hero tree starting node (row=1 in the hero sub-tree), OR
  - Class talent where `id_spec_starter` contains the spec ID
  - Some class talents (e.g. Warlock Soul Leech) are granted via undocumented DBC mechanisms
- **Round-trip safety**: Always pass `purchased_flags` from decode through to encode. This preserves
  the original purchased bits and handles edge cases where `is_granted()` logic differs from DBC data.

### DBC trait_data.inc Format
Each line: `{ tree_index, id_class, id_trait_node_entry, id_node, max_ranks, req_points,
id_trait_definition, id_spell, id_replace_spell, id_override_spell, row, col, selection_index,
"name", {id_spec[4]}, {id_spec_starter[4]}, id_sub_tree, node_type }`

- `tree_index`: 1=CLASS, 2=SPEC, 3=HERO, 4=SELECTION
- `id_class`: 1=Warrior, 2=Paladin, 3=Hunter, 4=Rogue, 5=Priest, 6=DK, 7=Shaman, 8=Mage,
  9=Warlock, 10=Monk, 11=Druid, 12=DH, 13=Evoker
- Nodes with same `id_node` but different `id_trait_node_entry` are choice/tiered options

### APL Action Name Gotchas
Some action names in APL text differ from what you'd expect:
- `ravage` is NOT castable — use `maul,if=buff.ravage.up` (auto-fires ravage on buff)
- `thrash_bear` → use `thrash` (proxy action, engine routes to bear form)
- `berserk_bear` → use `berserk` (spec-routed)
- `festering_scythe` → `set_replacement_action()` replaces `festering_strike`
- `graveyard` → replaces `epidemic` when `buff.forbidden_knowledge.up`
- `vampiric_strike` → auto-fires via `make_fallback()` when buff active
- Moonfire cannot appear in precombat (harmful spell without cast time)
- Variables referencing nonexistent talents (e.g. `berserk_persistence`) cause init errors

### C++ APL Generator Locations (non-obvious)
Most specs: `engine/class_modules/apl/apl_{class}.cpp`
Exceptions:
- Enhancement Shaman: `sc_shaman.cpp` (`init_action_list_enhancement`), NOT `apl_shaman.cpp`
- Brewmaster Monk: `apl_monk.cpp` inside `namespace brewmaster::default_apl()`
- Each hero tree variant has its own sub-list — fix ALL of them, not just one

### C++ Engine Patterns (for bug hunting and feature work)
- **Proc callbacks**: `register_callback()` in `create_actions()` or `init_special_effects()`
  — verify every proc trigger against Wowhead tooltip
- **Scaling**: `base_dd_min/max`, `spell_power_mod.direct`, `attack_power_mod.direct`
  — verify coefficients match DBC data
- **Buff/debuff wiring**: `make_buff()`, `set_default_value_from_effect_type()`
  — `set_default_value()` AFTER `set_default_value_from_effect_type()` causes assertion;
  use `default_value += X` directly
- **Target list safety**: Always check `target_list().size()` before indexing
- **Event scheduling**: `make_event()` timing must match in-game delays (e.g., 300ms delay
  on Glory of the Vanguard)
- **Assessor pattern**: Use assessors instead of event chains when the event manager can
  get stuck (Monk Empowered Tiger Lightning fix)
- Hunter uses `spell_data_ptr_t` (not `player_talent_t`) — scanner false-positive
- Paladin uses `const spell_data_t*` — scanner false-positive

### JSON Result Structure
```
sim -> players[0] -> collected_data -> dps -> mean    (per-player DPS)
sim -> players[0] -> stats[N] -> compound_amount      (per-action total damage)
sim -> players[0] -> stats[N] -> num_executes -> mean  (per-action cast count)
```
Use `players[0]` for single-actor sims, NOT `sim.statistics.raid_dps`.

---

## Pitfalls & Hard-Won Lessons

### Upstream Sync (CRITICAL — learned 2026-03-31)
- **Never let upstream drift more than 1-2 weeks.** We accumulated 181 upstream commits
  over 2 weeks and missed: 4 Balance proc chain fixes, 2 Paladin segfaults, Enh 4PC mastery
  halving, Monk event stuck, Void Ray scaling, Garrote snapshotting, DBC data updates.
- **Engine fixes > everything else.** We spent 331 commits on data/APL/optimization while
  upstream fixed crashes, scaling bugs, and proc chain errors. Our optimization results
  were precise measurements of incorrect simulations.
- **Check upstream EVERY SESSION** — `git fetch upstream midnight && git log HEAD..upstream/midnight`
- **Rebuild after rebase** — DBC changes require full rebuild + re-validate
- **Re-baseline affected specs** after merging engine fixes
- **"Non-zero DPS" ≠ "correct DPS"** — the Enh 4PC mastery bug produced plausible numbers
  while halving mastery.
- **"Implemented" ≠ "correct"** — our tier set audit checked existence, not behavioral correctness.
  A tier set can reference the right DBC entry but apply the wrong multiplier.

### Engine & C++ Work
- **The engine is not a black box.** Proc chains, scaling formulas, event sequencing, and
  target handling are all in C++. You MUST read and modify class modules to maintain SimC.
- **Proc chain bugs are invisible to APL optimization.** The APL optimizer can reorder actions
  and adjust thresholds. It cannot detect that Star Cascade fails to trigger Harmony of the
  Heavens. Only C++ code review catches this.
- **Scaling bugs are invisible to single-target baselines.** Void Ray soul gen scaling with
  targets is only detectable via multi-target sweeps. Always test at multiple target counts.
- **Crash bugs hide in edge cases.** Paladin segfaults from empty target lists only trigger
  in specific AoE scenarios. Test beyond Patchwerk + HAC.
- **Assessor vs event pattern** — if an event chain can cause the event manager to get stuck,
  convert to an assessor (Monk ETL fix pattern).

### Talent Tree
- **Heuristic edges are wrong** — row-adjacency/col-distance heuristic had 39 false edges and
  15 missed edges for warrior_fury alone (77.7% precision). Always use real TraitEdge.csv edges.
- **Hero tree nodes ignore spec filtering** — internal hero nodes may be tagged with only one spec's
  id_spec, but both specs in the pair can use them. SimC itself doesn't enforce this.
- **Selection nodes discover hero trees** — some hero trees have no spec-matching starting node
  (e.g., Evoker Aug + Chronowarden). Must check selection nodes (tree_index=4).
- **Spec name ambiguity** — `spec=frost` matches both `dk_frost` and `mage_frost`. Always use
  class context.
- **Wowhead builds can be over-budget** — always validate exports before using them.
- **Granted node counts vary widely** — druids/paladins have 3, warlocks have 0 in DBC.
- **req_points gates count PURCHASED points only** — granted nodes cost 0 currency, don't count.
  **This was a critical bug fixed 2026-03-30.**

### Simulation
- **10k iterations minimum** for comparison validity. At 1k, noise gives ±0.5% false positives.
- **"Identical .simc files" ≠ identical DPS** — the C++ APL generator can differ from .simc files.
- **C++ and .simc APLs drift apart** — sync the C++ generator after .simc improvements.
- **Tank specs in HecticAddCleave** — may produce 0 DPS or crash. PW-only for tanks.
- **DK Blood HAC crash** — FIXED. `consumption_release` race condition in `player_t::interrupt()`.
- **Druid Balance upstream APL = 0 DPS** — incompatible with Midnight. Verify before declaring "better".
- **Talent builds dominate APL optimization** — +3-6% from talents vs +0-1% from APL tuning.
- **Manual APL reordering regresses DPS** — upstream APLs are battle-tested. Use automated
  threshold sweeps, not intuition-based reordering.

### Multi-Stage Evaluation
Running all candidates at 10k iterations is too slow.
Multi-stage filtering (used by both APL optimizer and talent local search):
- Stage 1: 300 iter on all candidates → keep top 20%
- Stage 2: 3,000 iter on survivors → keep improvements over baseline
- Stage 3: 10,000 iter on top 3 → confirm

### Profile Convention
Each spec produces TWO optimal builds:
1. Best Patchwerk talent/APL → `MID1_{Class}_{Spec}.simc`
2. Best HecticAddCleave talent/APL → `MID1_{Class}_{Spec}_HAC.simc`

Tank specs (Blood, Guardian, Brewmaster, Protection) skip HAC — PW profile only.
Variant profiles (hero talent alternatives) follow the same `_HAC` suffix rule.
See `OPTIMIZATION_HOWTO.md` § "Profile File Convention" for full naming rules.

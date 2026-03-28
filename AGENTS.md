# AGENTS.md — SimulationCraft Midnight Agent Guide

**Last Updated: 2026-03-28**

Read this file first every session. Then read `project_progress.md` — it is the
single source of truth for all project status, known issues, and what to do next.

---

## Project

SimulationCraft fork for WoW Midnight expansion (build 12.0.1.66384).
33 DPS/tank specs, 56 profiles, 112 baselines.
See `project_progress.md` for complete status.

## File Map

### Documentation (root)
| File | What It Is |
|------|------------|
| `project_progress.md` | **THE master doc** — status, issues, next steps, all data |
| `APL_optimization.md` | APL technical reference — syntax, expressions, rules, common mistakes |
| `project_structure.md` | Codebase navigation — maps task types to source files |
| `optimization_action_plan.md` | Optimization design — 7 milestones, talent engine + APL optimizer |
| `darkmoon_investigation.md` | Darkmoon trinket investigation — blocked on beta data (Issue #81) |

### Archived (historical reference only)
| File | What |
|------|------|
| `docs/archive/full_spec_audit_2026-03-24.md` | Raw per-class audit data (5136 lines) |
| `docs/archive/APL_diff_report.md` | APL diff results — regenerable with `wowhead/gen_apl_diff.py` |

### Optimization Tooling (`scripts/`)
| Script | What |
|--------|------|
| `scripts/optimize_all.py` | Master orchestrator — `--report`, `--apl --all`, `--spec X` |
| `scripts/apl_optimizer.py` | APL optimization loop — mutation + multi-stage evaluation |
| `scripts/talent_build_compare.py` | Wowhead talent build comparison (all 33 specs) |
| `scripts/lib/sim_runner.py` | SimC runner — parallel sims, JSON parse, composite scoring |
| `scripts/lib/apl_parser.py` | APL parser/serializer — .simc ↔ structured data |
| `scripts/lib/apl_mutations.py` | 4 mutation operators — swap, sweep, promote, route |
| `scripts/lib/talent_tree.py` | DBC talent tree parser — builds DAG for any spec (3420 entries) |
| `scripts/lib/talent_codec.py` | Talent string codec — decode/encode base64 talent strings |
| `scripts/lib/tree_codec_bridge.py` | Bridge — connects tree + codec, high-level API |
| `scripts/lib/node_classifier.py` | Node classifier — DPS/GATING/UTILITY from APL + code |
| `scripts/lib/talent_permute.py` | Talent permutation — pivot sweep + tuning hill-climb |

### Wowhead Data (canonical game data source)
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
| MID1 profiles | `profiles/MID1/MID1_{Class}_{Spec}[_{Variant}].simc` |
| Phase 4 baselines | `results/phase4/*.json` (112 files) |
| DBC talent data | `engine/dbc/generated/trait_data.inc` (3420 entries) |
| Talent string parse/encode | `engine/player/player.cpp` lines 2675-3030 |

### Build
```bash
cmake -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON
cmake --build build -j$(nproc)
cp build/simc engine/simc
```

---

## Workflow

1. **Start:** Read this file → read `project_progress.md` "What's Next"
2. **Before code:** Read `project_structure.md` for file locations. For APL work, read `APL_optimization.md`.
3. **For spec work:** Read `wowhead/{class}/{spec}/extracted/rotation.md`
4. **After work:** Verify with `./engine/simc profiles/MID1/{profile}.simc iterations=1 output=/dev/null`
5. **Update** `project_progress.md` with what changed. Commit.

---

## Sim Commands

```bash
# Smoke test (1 iteration, catches parse errors)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=1 output=/dev/null

# Baseline (Patchwerk — single target, stand still)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc fight_style=Patchwerk \
  target_error=0.1 threads=16 json2=results/phase4/MID1_Warrior_Fury_patchwerk.json output=/dev/null

# Baseline (HecticAddCleave — target switching, adds spawn)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc fight_style=HecticAddCleave \
  target_error=0.1 threads=16 json2=results/phase4/MID1_Warrior_Fury_hecticaddcleave.json output=/dev/null

# Baseline report (all specs, sorted by composite DPS)
python3 scripts/optimize_all.py --report

# Extract the engine-generated APL (works for all specs regardless of .simc override)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=0 save_actions=/tmp/actions.simc output=/dev/null

# APL optimization (single spec)
python3 scripts/apl_optimizer.py --spec warrior_fury --max-iter 5

# APL optimization (all specs)
python3 scripts/optimize_all.py --apl --all

# Re-extract Wowhead data
python3 wowhead/extract_wowhead_tabs.py warlock affliction --pages rotation
```

Composite DPS = 0.50 × Patchwerk + 0.50 × HecticAddCleave.

---

## Domain Knowledge — SimC Internals

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

### Buff/Talent Implementation Patterns
- Hunter uses `spell_data_ptr_t` (not `player_talent_t`) — scanner false-positive
- Paladin uses `const spell_data_t*` — scanner false-positive
- `set_default_value()` after `set_default_value_from_effect_type()` → assertion failure.
  Use `default_value += X` directly instead.

### JSON Result Structure
```
sim -> players[0] -> collected_data -> dps -> mean    (per-player DPS)
sim -> players[0] -> stats[N] -> compound_amount      (per-action total damage)
sim -> players[0] -> stats[N] -> num_executes -> mean  (per-action cast count)
```
Use `players[0]` for single-actor sims, NOT `sim.statistics.raid_dps`.

---

## Pitfalls & Hard-Won Lessons

### Simulation
- **10k iterations minimum** for APL comparison validity. At 1k, noise gives ±0.5% false positives.
- **"Identical .simc files" ≠ identical DPS** — the C++ APL generator can differ from both .simc
  files. Always compare 3 variants: upstream .simc, our .simc, C++ default (no override).
- **C++ and .simc APLs drift apart** — after any .simc improvement, sync the C++ generator too.
  Otherwise players using the engine default don't benefit.
- **Tank specs in HecticAddCleave** — may produce 0 DPS or crash. Use Patchwerk-only for tanks,
  or use composite with awareness that HAC may be meaningless.
- **DK Blood HAC crash** — FIXED. `consumption_release` empowered charge race condition.
  `engine/player/player.cpp:7546`: added `!executing` guard in `interrupt()`.
- **Druid Balance upstream APL = 0 DPS** — incompatible with Midnight. Always verify upstream
  APL actually runs before declaring it "better".
- **Talent builds dominate APL optimization** — Wowhead comparison found 29/33 specs had better
  builds. Gaps up to +554% (Guardian). Always compare talent builds BEFORE optimizing APL.

### Multi-Stage APL Evaluation
Running all ~73 candidates at 10k iterations is too slow (~25 min/iteration).
Multi-stage filtering cuts to ~2 min/iteration:
- Stage 1: 100 iter on all candidates → keep top 20%
- Stage 2: 1,000 iter on survivors → keep >0.3% gains
- Stage 3: 10,000 iter on top 3 → confirm with 1% regression cap per fight style

### Acceptance Criteria
A candidate APL/build is accepted only if:
1. Composite DPS improves
2. Neither Patchwerk nor HecticAddCleave regresses more than 1%

### Common Upstream Superiority Patterns
1. Resource gating that idles GCDs (Subtlety `energy>60`)
2. Overly conservative thresholds (Brewmaster `celestial_brew` at 0.95 vs 0.3)
3. Missing AoE DoT spreading (Assassination CT bleed spreading)
4. Holding CDs too long for perfect alignment (Arms `demolish stack=10` vs `>=5`)

### Common Improvement Patterns
1. Current-season trinket references
2. Nightfall/proc capping prevention
3. More aggressive interrupt thresholds
4. Talent-specific dynamic AoE thresholds

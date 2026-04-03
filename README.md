# SimulationCraft — Midnight Fork

> Automated, agent-maintained fork of SimulationCraft focused on the **WoW Midnight** expansion (build 12.0.1.66709 Live).

This fork is based on [simulationcraft/simc](https://github.com/simulationcraft/simc) and targets the `midnight` branch. It is periodically synced with upstream and maintained by an autonomous Hermes agent that merges new commits, fixes bugs, optimizes APLs and talents, and runs validation pipelines — all without manual intervention.

## Origin & Acknowledgments

This work would not exist without the upstream SimulationCraft team. Everything in this fork builds on their C++ engine, class modules, talent system, DBC data pipeline, profile framework, APL infrastructure, and testing tooling. The upstream project has decades of accumulated domain knowledge about WoW combat mechanics — spell interactions, proc chains, snapshotting, scaling formulas, and fight-style simulation.

We treat [simulationcraft/simc](https://github.com/simulationcraft/simc) as the **single source of truth** for engine code. When we merge upstream, we keep their engine changes and resolve conflicts by preferring their upstream fixes. Our additions live on top of their foundation. All class module modifications, bug fixes, and engine improvements in this fork are diffs against their codebase.

**If you want to use the most stable and authoritative SimC: use upstream directly.** This fork is a specialized Midnight-focused layer for a narrower use case.

## What This Fork Adds

### 1. Engine Bug Fixes

We proactively audit the C++ code for correctness issues that upstream may not have caught yet. Found and fixed:

- **DK Blood vampiric_strike**: was reading `effectN(5)` (secondary AoE cleave coefficient) instead of `effectN(1)` (primary damage) — ~46% damage deficit per cast
- **Priest Shadow 2pc**: swapped effectN indices — Shadow Word: Madness dealt 0 damage
- **Rogue Subtlety 4pc**: `from_seconds()` applied to a millisecond value, making Shadow Blades permanent
- **Monk WW 4pc**: cooldown reduction was double-negated, canceling itself out
- **Monk WW 2pc**: +30% bonus double-applied (manual code + auto-apply via Aura 108) — ~4% DPS inflation
- **Paladin Ret Herald 4pc**: double-expurgation through inherited trigger callbacks
- **Shaman Elemental Storm Elemental pet**: wrong effectN index for talent modifier
- **Upstream proc callback API migration**: 65 locations migrated after upstream commit 938fa74 changed `dbc_proc_callback_t` signatures

Every fix is validated against DBC data and tested at 10,000+ iterations.

### 2. Midnight Tier Set & Talent Implementations

Complete implementation of all 33 spec tier sets (MID1) plus Midnight-exclusive 4-rank apex talents:

| Class | Apex Talent | Pattern |
|-------|------------|---------|
| Balance Druid | Ascendant Eclipses | Instant casts + eclipse DoT + guaranteed Solar/Lunar bolts |
| Feral Druid | Unseen Predator | Ferocious Bite proc chain + damage bonus + Tiger's Fury synergy |
| Guardian Druid | Wild Guardian | Berserk echo casts + mastery + Dream Guide |
| Restoration Druid | Everbloom | AoE heal bloom + HoT capstone |
| All 33 specs | Spec-specific apex | Each follows the 3-spell-ID rank pattern |

All NYI (Not Yet Implemented) talents have been audited and either implemented or annotated with justification (e.g., "N/A for DPS — movement utility only").

### 3. APL & Profile Optimization

This fork produces **optimized action priority lists and talent builds** for every spec using a 3-layer pipeline:

- **Layer 1** — Blind mutation optimizer: swaps APL actions, sweeps thresholds, promotes high-value casts (~200 candidates/spec, evaluated through a 300→3,000→10,000 iteration funnel)
- **Layer 2** — Signal-guided mutations: parses sim output for APS inversions, buff waste, resource overcap, and interval gaps, then generates targeted fixes
- **Layer 3** — LLM semantic advisor: when automated signals detect a buff with no consumer in the APL, an LLM (Qwen via OpenRouter) receives full Wowhead context and proposes structured changes — all DPS-validated before acceptance

**Each spec gets two profiles:**

| File | Description |
|------|-------------|
| `MID1_{Class}_{Spec}.simc` | Optimized for Patchwerk (single-target) |
| `MID1_{Class}_{Spec}_HAC.simc` | Optimized for Hectic Add Cleave (multi-target, movement) |

All 89 profiles (33 base specs + 16 hero talent variants × 2 fight styles) pass compilation, talent validation, and 1-iter smoke tests.

### 4. Midnight Trinket Implementations

Implemented 23+ Midnight trinkets in `unique_gear_midnight.cpp` with proper DBC-driven values:

- The Eternal Egg, Rotting Globule, Solar Core Igniter, Bark of the Guardian Tree
- Desecrated Chalice (stack-based trigger), Holy Retributor's Order
- Umbric's Channeling Focus, Repurposed Volatile Manacell
- Gloom-Spattered Dreadscale, Drum of Renewed Bonds, Permafrost Reservoir
- Shard of VoidStalker's Bracers, Voidclaw Gauntlets, and many more

All use `dbc_proc_callback_t` with the updated signature and read coefficients from DBC data.

### 5. Tooling & Automation Infrastructure

A comprehensive testing and optimization framework built as a complement to the SimC engine:

| Script | Purpose |
|--------|---------|
| `talent_validator.py` | Validates talent builds against real TraitEdge.csv prerequisite edges — budget, gates, hero trees |
| `talent_local_search.py` | Hill-climbing talent optimizer with validated neighbor generation |
| `apl_optimizer.py` | APL mutation engine with 4 operators: swap, sweep, promote, route |
| `signal_apl_optimizer.py` | Signal-guided + LLM Layer 2+3 pipeline |
| `verify_spell_effects.py` | Scans class modules for effectN out-of-bounds and semantic issues |
| `verify_spell_implementation.py` | Validates spell implementations against DBC data |
| `deep_audit.py` | Variable-to-spell tracing + comprehensive effectN audit |
| `compare_reference_profiles.py` | Substitutes reference talents/APLs on our engine to isolate engine inflation or deflation |
| `validate_all_profiles.py` | Full profile validation against tree constraints |
| `dump_llm_prompts.py` | Reviews LLM advisor prompts for debugging |

These tools live in this fork to support the autonomous agent workflow. They do not modify upstream code.

### 6. 33 New Midnight Profiles

This fork added all missing Midnight base and hero variant profiles and HAC variants that upstream did not have at the time of branching. Every profile includes:
- Updated gear, talents, consumables for Midnight S1
- Optimized APLs through the 3-layer pipeline
- Both Patchwerk and HecticAddCleave variants (including tanks)

## Automated Agent Workflow

This fork is maintained by a **Hermes agent** — an autonomous CLI assistant that:

1. **Merges upstream** — fetches, reviews, and rebases upstream `midnight` commits; migrates our changes to match new upstream signatures
2. **Validates** — runs compile checks, 1-iter smoke tests, and profile validation after every merge
3. **Audits** — periodically runs spell audits, tier set behavioral audits, and effectN scans
4. **Optimizes** — runs full talent + APL optimization passes across all 33 specs
5. **Validates DPS** — compares against simulationcraft.org reference profiles using the substitute methodology (reference talents + reference APLs on our engine)
6. **Documents** — updates progress, records post-mortems, and maintains internal checklists

All changes are made through this automated pipeline with data-driven gates — no intuition-based modifications reach the profiles. If a change doesn't pass DPS validation at 10,000 iterations, it is rejected.

## Sync Policy

- We merge from upstream `midnight` regularly and test every merge
- PTR-specific commits (12.0.5.x builds) are skipped — we target 12.0.1.66709 Live only
- When upstream fixes a class module, we read the diff, understand the change, verify it works with our profiles, and adopt it
- Our optimization data (talents, APLs, profiles) is kept separate from engine changes

## How to Build

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc)
cp build/simc engine/simc
```

Or with networking disabled:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DSC_NO_NETWORKING=ON
cmake --build build -j$(nproc)
```

## How to Simulate

```bash
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=10000
```

For multi-target and Hectic Add Cleave:

```bash
./engine/simc profiles/MID1/MID1_Warrior_Fury_HAC.simc iterations=10000 fight_style=HecticAddCleave
```

## Upstream

- **Main Repo**: [simulationcraft/simc](https://github.com/simulationcraft/simc)
- **Our upstream branch**: [simulationcraft/simc → midnight](https://github.com/simulationcraft/simc/tree/midnight)
- **SimC Website**: [simulationcraft.org](https://www.simulationcraft.org/)
- **SimC Discord**: [SimCMinMax](https://discord.gg/tFR2uvK)

## License

This fork inherits the same license as upstream SimulationCraft. See [LICENSE](LICENSE) for details.

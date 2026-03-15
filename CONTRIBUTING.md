# Contributing to Midnight Expansion Update

**Based on upstream SimulationCraft practices, adapted for the Midnight expansion update.**

---

## Overview

This fork (`MubarakHAlketbi/simc`) is focused exclusively on updating SimulationCraft for the **Midnight expansion** (Patch 12.0.x). The work is being conducted primarily by autonomous AI agents following the protocols documented in `AGENTS.md`.

While we don't actively solicit external contributions, this document outlines the established practices so that any future contributors can align with upstream conventions and our specific workflow.

---

## Core Principles (From Upstream)

The original SimulationCraft community operates on a philosophy of radical ownership:

- **"Just check it in. Don't ask for permission."** If the code needs to change for functional or artistic reasons, commit it. Maintainers will review and revert/modify if needed.
- **Initiative over permission.** Developers are expected to identify needs and address them without waiting for assignment.
- **Laid-back collaboration.** There is little strict responsibility; help wherever needed.
- **Pull requests welcome.** PRs are the primary mechanism for code review and integration without requiring direct repository permissions.

We retain these principles but have formalized them for autonomous agent execution.

---

## Our Adapted Workflow

### 1. Read the Guides (in order)

Before doing any work, read these files **completely**:

1. **`AGENTS.md`** - The authoritative protocol for Midnight development. Defines data sources, validation checklist, task selection, and communication channels.
2. **`project_structure.md`** - The 740-line codebase map. ALWAYS consult this to locate the correct files for any issue type.
3. **`project_progress.md`** - The master tracker of implementation status. Shows what's done, in beta, or NYI (Not Yet Implemented).

These three files contain everything needed to work efficiently.

### 2. Ground Truth: Wowhead

All game data must be sourced from **Wowhead's Midnight database**:
https://www.wowhead.com/midnight

- Record the **full URL** and **retrieval date (YYYY-MM-DD)** in code comments
- For trinkets/items with special effects, follow the **two-step extraction**: item page → linked spell ID → spell page → scaling token spell
- If Wowhead is ambiguous, cross-reference with official Blizzard patch notes

Never use old data or guess at mechanics.

### 3. Task Selection

The source of truth is **`project_progress.md`**. Tasks are prioritized:

1. **NYI** → Implement (highest priority)
2. **In Beta** → Test/refine
3. **Implemented** → Verify (regression checks)

When picking a task:
- Choose an NYI row with no blocking dependencies
- Reference the specific row number (e.g., "Row 45: Druid Balance general changes")
- Update the status immediately after completing the task and commit

### 4. File Location Protocol

**NEVER guess or manually search for files.** Use `project_structure.md` mapping:

- **New class ability/spell** → `engine/class_modules/sc_<class>.cpp` (or split directory)
- **Midnight trinket/unique item** → `engine/player/unique_gear_midnight.cpp`
- **Talent adjustments** → Class module where the talent's effect is applied
- **APL changes** → `engine/class_modules/apl/apl_<class>.cpp`
- **Set bonuses** → DBC auto-loaded; complex logic in `unique_gear_midnight.cpp`
- **Consumables (food/flasks)** → `unique_gear_midnight.cpp` (namespace `consumables`)
- **Profiles** → `profiles/MID1/MID1_<Class>_<Spec>.simc`
- **Spell/item data corrections** → Regenerate via `dbc_extract3/dbc_extract.py`

The structure guide includes a quick reference table and detailed examples.

### 5. Implementation Pattern

For **Midnight-specific code**, follow these conventions:

- **Trinket registration** in `unique_gear_midnight.cpp`:
  ```cpp
  register_special_effect( SPELL_ID, []( special_effect_t& effect ) {
      effect.custom_buff = new buff_t( ... );
      effect.proc_chance_ = 15;
      // ...
  } );
  ```
- **Version guards** if necessary:
  ```cpp
  if ( !player->dbc || player->dbc->wow_version() < midnight_version )
      return;
  ```
- **Source citations** mandatory: `// Source: https://www.wowhead.com/spell=123456&expand=1 (2026-03-15)`

### 6. Build System

If you add a **new source file** (`.cpp` or `.hpp`):

1. Add it to `source_files/cmake_engine.txt` (canonical list)
2. Also update `source_files/QT_engine.pri` and `source_files/VS_engine.props` if present
3. Run a clean build to ensure all build systems pick it up

Never skip this step.

---

## Testing & Validation

Before marking anything **"Implemented"** in `project_progress.md`, run the **Validation Checklist** (from `AGENTS.md`):

- [ ] Code compiles without warnings/errors
- [ ] Simulation runs without crashes
- [ ] Profile loads and simulates at least 1 iteration
- [ ] Results are reasonable (no zero DPS, no absurd values)
- [ ] Talents/abilities interact correctly (check logs)
- [ ] Set bonuses trigger and stack properly
- [ ] No regressions in existing specs (quick sanity check)
- [ ] Source data documented in code (Wowhead URLs and dates)

Tests are located in `tests/`. Run them with:
```bash
python3 tests/run.py
```

---

## Pull Request Process

If you are a collaborator with push access, you may commit directly. However, for substantial changes or if you're unsure:

1. Create a **feature branch** from `midnight`
2. Make your changes
3. Open a **Pull Request** against `upstream/midnight`
4. Request review from maintainers or post in GitHub Discussions
5. Address feedback, then merge

**Pull request description must include:**
- What was changed
- Which rows in `project_progress.md` were updated
- Links to Wowhead data sources
- Any testing performed

---

## Communication

- **GitHub Discussions** - Use the `midnight-update`, `agent-dev`, `needs-review`, `needs-clarification` labels
- **Discord** - `SimCMinMax` (https://discord.gg/tFR2uvK) - #simulationcraft for class-specific questions
- **Issues** - Reference issue numbers in commit messages: `Fixes #123`

---

## Upstream Alignment

We aim to stay compatible with upstream SimulationCraft practices:

- Follow existing **code style** (mixed snake_case/camelCase; match surrounding code)
- Use the same **naming conventions**: `class_t`, `sc_<class>.cpp`, `apl_<class>.cpp`
- Keep **data separate from logic**: DBC-generated `.inc` files are not hand-edited; we add logic in `.cpp` files
- Respect the **registration pattern** for special effects
- **Never edit** files in `ActionPriorityLists/default/` or `profiles/` directly—they are auto-generated

If you discover a better pattern, document it in `project_structure.md` for future agents.

---

## Resources

- **`AGENTS.md`** - Our primary development protocol
- **`project_structure.md`** - Codebase navigation guide (740 lines)
- **`project_progress.md`** - Task tracker
- **Wowhead Midnight** - https://www.wowhead.com/midnight
- **Upstream Coding Guidelines** - https://github.com/simulationcraft/simulationcraft/wiki/CodingGuidelines
- **How to Build** - https://github.com/simulationcraft/simulationcraft/wiki/HowToBuild
- **Developer Corner** - https://github.com/simulationcraft/simulationcraft/wiki/Participate

---

## Summary

1. Read `AGENTS.md` and `project_structure.md`
2. Pick an NYI task from `project_progress.md`
3. Use `project_structure.md` to find the correct file
4. Verify data from Wowhead (with URLs/dates)
5. Implement, test, validate
6. Update `project_progress.md` and commit
7. Open PR or continue to next task

---

*Adapted from upstream SimulationCraft CONTRIBUTING.md. Last updated: March 15, 2026.*

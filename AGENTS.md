# AGENTS.md - SimulationCraft Midnight Expansion Update

**Last Updated: March 15, 2026**

## Objective

Update SimulationCraft to fully support World of Warcraft's new "Midnight" expansion, ensuring accurate simulation of all new class talents, spells, abilities, gear, and game mechanics.

## Context

**SimulationCraft** is an open-source combat simulation engine for World of Warcraft. It models player characters, enemies, and combat mechanics to evaluate DPS, HPS, and other performance metrics. Players and theorycrafters rely on it for gear optimization, talent comparisons, and stat weight calculations.

The "Midnight" expansion introduces significant changes including:
- New talent trees and revamped class abilities
- Updated itemization and gear systems
- New combat mechanics and buff/debuff systems
- Level cap changes and new spells
- Class-specific changes and reworks

## Primary Data Source: Wowhead

**Wowhead (www.wowhead.com/midnight) is the canonical ground truth** for all Midnight expansion data. This includes:

- Spell IDs, tooltips, and descriptions
- Talent trees and ranks
- Item stats, set bonuses, and special effects
- Class changes and ability updates

**General Procedure:**
1. Always verify data against Wowhead's Midnight database
2. Record the URL or build ID used for each piece of data
3. Note the retrieval date (format: YYYY-MM-DD) in comments
4. If Wowhead is unclear, cross-reference with official Blizzard patch notes

Example: `# Source: https://www.wowhead.com/spell=123456&expand=1 (2026-03-15)`

**Special Procedure for Trinkets and Gear with Special Effects:**

Many trinkets and gear effects use "dummy" or "token" spells to handle scaling. The item page shows a summary, but the full mechanics (including damage formulas and scaling coefficients) are defined in a separate spell page.

**Steps:**
1. On the item page, locate the spell ID linked in the "Item Effect" section (usually displayed as a spell icon or tooltip).
2. Extract the item page data: base numbers, cooldown, description text.
3. Navigate to the spell page (https://www.wowhead.com/spell=SPELL_ID) to get the detailed mechanics.
4. If the spell page references another "Scaling Token" or "Dummy" spell, fetch that as well — it often contains the actual scaling multipliers (e.g., "+30% per additional enemy").
5. Determine if the displayed numbers are static or item-level dependent. If the item has multiple item levels (e.g., normal/heroic), treat the number as item-level specific and derive a coefficient or formula for SimC's item level scaling.

**Important:** Document both the item URL and the spell URL(s) in your code comments.

## Task Dossier System

**MANDATORY:** Before implementing any task, create a complete `task_dossier.md` that consolidates all necessary information. This dossier becomes the single source of truth for that task.

### Why?
- Prevents repeated web fetches that can cause misconfiguration
- Ensures all data is documented and verified upfront
- Provides a stable reference for code editing
- Creates an audit trail for future maintenance

### Process

1. **Pick a task** from `project_progress.md` (reference row number)
2. **Create a dossier** in `task_dossiers/` using `TASK_DOSSIER_TEMPLATE.md`
   - Rename with descriptive name: `druid_balance_general_2026-03-15.md`
3. **Fetch and populate** all ground truth data:
   - Wowhead URLs for spells/items/talents
   - Extract formulas, coefficients, descriptions
   - For trinkets: follow item → spell → scaling token chain
4. **Complete the dossier** including:
   - Target file(s) from `project_structure.md`
   - Verification checklist
   - Code change plan (draft logic)
5. **Edit code** based ONLY on the dossier contents
6. **After completion**, add dossier to git and reference it in commit

### Dossier Contents

The template includes sections for:
- Metadata (task reference, type, target files)
- Spell/Item/Talent/Set details with full Wowhead citations
- Profile requirements for testing
- Implementation notes and interactions
- Verification checklist
- Code change plan (draft before coding)
- Post-implementation info

### Rule

**Never start coding without a completed dossier.** If new information emerges during implementation, update the dossier first, then adjust code.

All dossiers should be committed to the repository in `task_dossiers/` for future reference and to avoid re-fetching the same data.

## Project Tracking (Main Source)

**`project_progress.md`** is the *primary source of truth* for tracking implementation status across all classes, specs, gear, and consumables. It contains detailed tables with the following statuses:

- **Implemented**: Feature/class/generic changes fully implemented
- **In Beta**: Implementation exists but needs testing/refinement
- **NYI**: Not Yet Implemented
- **N/A**: Not applicable (e.g., healer specs in some contexts)

**Key columns tracked:**
- Class general changes
- APL (Action Priority List) readiness
- MID1 tier set bonuses (2-set and 4-set)
- Trinkets, consumables, enchants, food, gear effects, etc.

**Before making changes, always consult `project_progress.md`** to understand what needs work and what is already done. Update this file immediately when a task is completed by changing the status and adding a brief note.

## Solo Agent Development System

This project is developed by autonomous agents. The following workflow ensures continuity across sessions:

**1. Self-Contained Tasks**
- Each task should be independently actionable by an agent
- Include in the task description: what to implement, where to modify, expected behavior
- Reference specific rows in `project_progress.md` (e.g., "Update DK: Unholy general changes (row 10)")

**2. State Persistence**
- All progress recorded in `project_progress.md`
- Commit changes with clear messages: "[Midnight] Update DK Unholy - General Changes"
- Include source URLs/dates in comments within code changes

**3. Task Selection Protocol**
An agent should:
- Read `AGENTS.md` and `project_progress.md` at start
- Prioritize: NYI → In Beta → Implemented (for verification)
- Focus on one class/spec or gear category at a time
- Prefer tasks with clear dependencies met (e.g., finish core class before set bonuses)

**4. Validation Checklist** (run before marking anything "Implemented"):
- [ ] Code compiles without warnings/errors
- [ ] Simulation runs without crashes
- [ ] Profile loads and can simulate at least 1 iteration
- [ ] Results are reasonable (no zero DPS, no absurdly high values)
- [ ] Talents/abilities properly interact (tested via simulated logs if possible)
- [ ] Set bonuses correctly trigger and stack
- [ ] No regressions in existing specs (quick sanity checks)
- [ ] Source data documented in code (Wowhead URLs and dates)

**5. Communication: GitHub Issues**
- Use the repository's GitHub Issues for:
  - Questions about ambiguous mechanics
  - Requests for review before marking "Implemented"
  - Sharing partial implementations for collaboration
  - Reporting blockers or missing data
- Tag issues with the appropriate labels from `ISSUE_TAGS.md`:
  - Always: `expansion:midnight`
  - Task type: `type:general-changes`, `type:apl`, `type:set-2pc`, `type:set-4pc`, `type:trinket`, `type:consumable`, `type:talent`
  - Class/Spec: `class:<class>`, `spec:<spec>` (if applicable)
  - Status: `status:nyi`, `status:in-progress`, `status:in-beta`, `status:implemented`, `status:blocked`
  - Flags: `needs-review`, `needs-data`, `priority:high/medium/low`
- Before starting a task, search existing issues to avoid duplicate work
- After completing a task, post a summary with:
  - What was changed
  - Rows updated in `project_progress.md`
  - Links to PRs or commits

**6. Error Handling & Edge Cases**
- If Wowhead lacks data: mark as NYI and note "requires manual testing" in table
- If mechanics are unclear: open a GitHub Issue, label as `needs-data` and add detailed questions
- If code changes are risky: create a separate branch and request testing from maintainers

**Status:**
- All classes listed as NYI moved to In Beta or Implemented
- All gear/consumables marked Implemented or verified
- `project_progress.md` accurately reflects current state
- All code changes include source verification (Wowhead URLs)
- No regression in existing Midnight-eligible specs

## GitHub Issues Integration

The project uses GitHub Issues to track individual implementation tasks. The relationship with `project_progress.md` is:

1. **Issues reference specific rows** in `project_progress.md` (tracked via the "project_progress.md Reference" field in the issue template).
2. **Each issue corresponds to one work item** (e.g., "Row 10: DK Unholy general changes" or "Rows 65-70: Raid trinkets").
3. **When an issue is closed as completed**, the agent **must update the corresponding row(s)** in `project_progress.md` to reflect the new status (Implemented, In Beta, etc.).
4. **The issue's labels** (especially `status:*`) should match the status in `project_progress.md`.
5. For traceability, the issue number should be noted in the commit message and optionally in the `project_progress.md` notes column.

This bidirectional linkage ensures the high-level dashboard stays current and provides a complete audit trail.

## Codebase Navigation Reference

**ALWAYS consult `project_structure.md` before starting any implementation task.** This comprehensive guide (740 lines) maps:

- Issue types to specific files (e.g., "Midnight trinket" → `engine/player/unique_gear_midnight.cpp`)
- Class modules, APL locations, and data pipelines
- Build system requirements and conventions
- Common patterns and registration mechanisms

This prevents repeated exploration and conserves tokens. The file includes a quick reference table and detailed explanations of the SimulationCraft architecture tailored for Midnight development.

**Core Principle:** Before touching any code, locate the appropriate target file using `project_structure.md`. If the mapping is unclear, update the document as you discover patterns.

## Key Tasks

1. **Data Updates**
   - Add new spells, talents, and abilities to `spell_data.cpp` / spell database
   - Update existing spell coefficients, damage formulas, and scaling
   - Add new items, gear, and set bonuses
   - Update level and progression data

2. **Class Module Updates**
   - Each class module (e.g., `mage.cpp`, `warrior.cpp`) needs updates for new abilities
   - Implement new talent trees and talent interactions
   - Update rotation logic for changed mechanics
   - Add support for new resource systems if applicable

3. **Mechanics & Systems**
   - Update combat log parsing if event IDs changed
   - Implement new buff/debuff tracking systems
   - Adjust proc calculations and random mechanics
   - Update stat scaling formulas

4. **Testing & Validation**
   - Create baseline profiles for each specialization
   - Run regression tests against known benchmarks (if available)
   - Validate talent simulations produce expected results
   - Ensure no crashes or memory errors with new data

5. **Documentation**
   - Update README with Midnight-specific notes
   - Document new simulation options or flags
   - Update changelog

## Notes

- **Code Formatting**: All C++ code must conform to the project's `.clang-format` style (Google-based with project-specific tweaks). Before committing, run `clang-format -i` on modified files or use `run-clang-format` if available. See `.clang-format` in the repository root for full configuration.
- Maintain backward compatibility where possible
- Use meaningful variable names and add comments for complex logic
- Test thoroughly before submitting changes
- Coordinate via GitHub Issues for major architectural changes
- Wowhead as of build date 2026-03-15 is the reference; note if newer data differs

## Resources

- **Wowhead Midnight Database**: https://www.wowhead.com/midnight
- **Blizzard Patch Notes**: Official patch notes for Midnight expansion
- **SimulationCraft GitHub**: GitHub Issues for tracking tasks
- **Class Discord Communities**: For nuanced mechanics (if accessible)
- **project_structure.md**: ⭐ Essential codebase navigation guide - consult before any task
- **ISSUE_TAGS.md**: Complete reference for GitHub issue tagging system (type, class, spec, status)
- **Label Setup**: Before using issues, create all required labels on GitHub as defined in `ISSUE_TAGS.md` (use `gh label create <name> --color <hex> --description "<desc>"`).

---
*This file guides autonomous agents working on the Midnight expansion update for SimulationCraft. Always check `project_progress.md` before starting work and update it after completing tasks. Use GitHub Issues for coordination.*
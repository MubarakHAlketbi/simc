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

**Procedure:**
1. Always verify data against Wowhead's Midnight database
2. Record the URL or build ID used for each piece of data
3. Note the retrieval date (format: YYYY-MM-DD) in comments
4. If Wowhead is unclear, cross-reference with official Blizzard patch notes

Example: `# Source: https://www.wowhead.com/spell=123456&expand=1 (2026-03-15)`

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

**5. Communication: GitHub Discussions**
- Use the repository's GitHub Discussions for:
  - Questions about ambiguous mechanics
  - Requests for review before marking "Implemented"
  - Sharing partial implementations for collaboration
  - Reporting blockers or missing data
- Tag discussions with labels: `midnight-update`, `agent-dev`, `needs-review`
- Before starting a task, search existing discussions to avoid duplicate work
- After completing a task, post a summary with:
  - What was changed
  - Rows updated in `project_progress.md`
  - Links to PRs or commits

**6. Error Handling & Edge Cases**
- If Wowhead lacks data: mark as NYI and note "requires manual testing" in table
- If mechanics are unclear: open a GitHub Discussion, label as `needs-clarification`
- If code changes are risky: create a separate branch and request testing from maintainers

**7. Success Criteria**
- All classes listed as NYI moved to In Beta or Implemented
- All gear/consumables marked Implemented or verified
- `project_progress.md` accurately reflects current state
- All code changes include source verification (Wowhead URLs)
- No regression in existing Midnight-eligible specs

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

- Follow existing code style and patterns in the codebase
- Maintain backward compatibility where possible
- Use meaningful variable names and add comments for complex logic
- Test thoroughly before submitting changes
- Coordinate via GitHub Discussions for major architectural changes
- Wowhead as of build date 2026-03-15 is the reference; note if newer data differs

## Resources

- **Wowhead Midnight Database**: https://www.wowhead.com/midnight
- **Blizzard Patch Notes**: Official patch notes for Midnight expansion
- **SimulationCraft GitHub**: Repository issues and discussions
- **Class Discord Communities**: For nuanced mechanics (if accessible)

---
*This file guides autonomous agents working on the Midnight expansion update for SimulationCraft. Always check `project_progress.md` before starting work and update it after completing tasks. Use GitHub Discussions for coordination.*
# AGENTS.md - SimulationCraft Midnight Expansion Update

**Last Updated: March 16, 2026**

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

**MANDATORY:** Before implementing any task, create a complete dossier in `task_dossiers/` that consolidates all necessary information. This dossier becomes the single source of truth for that task.

### Why?
- Prevents repeated web fetches that can cause misconfiguration
- Ensures all data is documented and verified upfront
- Provides a stable reference for code editing
- Creates an audit trail for future maintenance

### Process

1. **Pick a task** from `project_progress.md` (reference row number)
2. **Create a dossier** in `task_dossiers/` using `TASK_DOSSIER_TEMPLATE.md`
   - Name it descriptively: `druid_balance_general_2026-03-15.md`
3. **Fetch and populate** all ground truth data:
   - Wowhead URLs for spells/items/talents
   - Extract formulas, coefficients, descriptions
   - For trinkets: follow item → spell → scaling token chain
   - For talent audits: use the methodology in `talent_extraction.md`
4. **Complete the dossier** including:
   - Target file(s) from `project_structure.md`
   - Verification checklist
   - Code change plan (draft logic)
5. **Edit code** based ONLY on the dossier contents
6. **After completion**, add dossier to git and reference it in commit

### Dossier Contents

The template (`TASK_DOSSIER_TEMPLATE.md`) includes sections for:
- Metadata (task reference, type, target files, Wowhead build date)
- Spell/Item/Talent/Set details with full Wowhead citations
- Profile requirements for testing
- Implementation notes and interactions
- Verification checklist
- Code change plan (draft before coding)
- Post-implementation info (commit message, files modified, rows updated)

### Dossier Types and Naming

| Task Type | Example filename |
|-----------|-----------------|
| Class general changes | `dk_unholy_general_2026-03-16.md` |
| APL work | `warrior_arms_apl_2026-03-16.md` |
| Tier set bonuses | `mage_mid1_sets_2026-03-16.md` |
| Trinket/gear | `trinket_void_reaper_libram_2026-03-16.md` |
| Talent audit (full sweep) | `talent_audit_wowhead_2026-03-16.md` |
| Talent implementation | `warlock_class_tree_2026-03-16.md` |

### Existing Dossiers

The following dossiers are already committed in `task_dossiers/` and must not be re-created:

| File | Scope |
|------|-------|
| `rogue_general_2026-03-16.md` | Rogue Assassination/Outlaw/Subtlety general changes |
| `shaman_elemental_2026-03-16.md` | Elemental Shaman general changes + APL |
| `warlock_general_2026-03-16.md` | Warlock Affliction/Demo/Destro general changes |
| `talent_audit_wowhead_2026-03-16.md` | Full talent audit: all 33 specs vs Wowhead — 94.7% coverage, missing talent classifications, priority queue |

Before starting any talent-related task, **read `talent_audit_wowhead_2026-03-16.md` first** — it contains the complete list of missing talents per spec, spell IDs, DPS-relevance classification, and implementation priority order.

### Rule

**Never start coding without a completed dossier.** If new information emerges during implementation, update the dossier first, then adjust code.

All dossiers must be committed to `task_dossiers/` so future agents can reference them without re-fetching Wowhead.

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
- For talent work: also read `talent_extraction.md` and `task_dossiers/talent_audit_wowhead_2026-03-16.md`
- Check `task_dossiers/` for an existing dossier covering the task before creating a new one
- Prioritize: NYI → In Beta → Implemented (for verification)
- For talent gaps: follow the priority queue in the Talent Data Extraction section above
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

## Talent Data Extraction

When working on talent-related tasks — whether implementing missing talents, auditing spec trees, or verifying Apex Talent mechanics — use the methodology documented in **`talent_extraction.md`**.

### What talent_extraction.md covers

- **Wowhead talent calculator URL format:** `https://www.wowhead.com/talent-calc/{class}/{spec}/{hero}`
- **Why plain HTTP fails** (React SPA) and how to use Firecrawl to get the rendered DOM
- **DOM structure:** the `data-class-spec="{class}-{spec}"` container and how talent nodes are structured
- **Extraction regex** for pulling spell IDs, names, and ranks from the HTML
- **Batch extraction scripts** at `/tmp/fetch_batch.py` and `/tmp/compare_talents.py`
- **Apex Talents guide** URL and extraction approach
- **SimC comparison methodology** (3-tier: spell ID → slug → name string)
- **Which SimC files to search** per class
- **Known false negatives** and how to handle them
- **Step-by-step instructions** for auditing a new spec or re-running the full audit

### Talent Audit Status (2026-03-16)

A full audit of all 33 DPS/tank specs has been completed and documented. Results:

- **Coverage: 94.7%** (2,644 / 2,792 Wowhead talents found in SimC)
- **Complete (0 missing):** DH (all 3), Druid (all 3), Hunter (all 3), Mage (all 3), Paladin (2), Rogue (all 3), Warrior (all 3), Shadow Priest
- **Needs work:** Warlock all specs (31 missing — class tree), Shaman (15 missing — class tree), Evoker Augmentation (6 missing)
- **Minor gaps:** DK all specs (3), Monk (2), Subtlety Rogue (1), Devastation Evoker (4)

Full findings and implementation priority queue: `task_dossiers/talent_audit_wowhead_2026-03-16.md`

### Priority Queue for Remaining Talent Work

Before picking up any talent implementation task, check this order:

1. **Warlock class tree DPS passives** — Gorefiend's Avarice (1270701), Pact of Nathrezim (1270690), Oppressive Darkness (1270255), Pact of Gluttony (386689), Teachings of the Black Harvest (385881), Fel Synergy (389367), Infernal Beneficiary (1265810), Dark Pact (108416), Empowered Drain Life (1271689)
2. **Shaman Elemental Orbit** (383010) — new Midnight DPS proc talent, affects both Elemental and Enhancement
3. **Evoker:** Strike from Above (1267206), Nozdormu Adept (431715), Improved Defy Fate (1268881)
4. **Subtlety Rogue:** Improved Find Weakness (382512) — verify armor pen modifier
5. **DK class tree:** Blood Bond (1267028), Death Notes (1266819), Death Defiance (1266818) — verify DPS impact first

### Apex Talents

All Apex Talent nodes for all 33 DPS/tank specs are **already present in SimC**. Apex Talent spell IDs and full mechanics are documented in:
- `task_dossiers/talent_audit_wowhead_2026-03-16.md` (Apex Talent table with all 54 spell refs)
- `talent_extraction.md` (how to re-fetch from the guide if data needs refreshing)

The Apex Talent guide URL: `https://www.wowhead.com/guide/midnight/apex-talents-overview`

---

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

### Project Files (read these before starting any task)

| File | Purpose |
|------|---------|
| `AGENTS.md` | This file — agent workflow, rules, and reference index |
| `project_progress.md` | ⭐ Master status tracker — all specs, gear, talents, Apex Talents |
| `project_structure.md` | ⭐ Codebase navigation — maps tasks to source files (740 lines) |
| `talent_extraction.md` | ⭐ How to extract talent data from Wowhead talent calculator and diff against SimC |
| `TASK_DOSSIER_TEMPLATE.md` | Template for creating new task dossiers |
| `ISSUE_TAGS.md` | All GitHub issue labels with colors and descriptions |
| `task_dossiers/talent_audit_wowhead_2026-03-16.md` | Full talent audit results — 33 specs, missing talents, priority queue |

### Wowhead URLs

| Resource | URL |
|----------|-----|
| Midnight home | https://www.wowhead.com/midnight |
| Talent calculator | `https://www.wowhead.com/talent-calc/{class}/{spec}/{hero}` |
| Apex Talents guide | https://www.wowhead.com/guide/midnight/apex-talents-overview |
| Spell lookup | `https://www.wowhead.com/spell=SPELL_ID` |
| Beta spell lookup | `https://www.wowhead.com/beta/spell=SPELL_ID` |
| Item lookup | `https://www.wowhead.com/item=ITEM_ID` |

### External

- **Blizzard Patch Notes**: Official patch notes for Midnight expansion
- **SimulationCraft GitHub**: GitHub Issues for tracking tasks
- **Class Discord Communities**: For nuanced mechanics (if accessible)

### Label Setup

Before using GitHub Issues, create all required labels as defined in `ISSUE_TAGS.md`:
```bash
gh label create <name> --color <hex> --description "<desc>"
```

---
*This file guides autonomous agents working on the Midnight expansion update for SimulationCraft. Always check `project_progress.md` before starting work and update it after completing tasks. Use GitHub Issues for coordination.*
# Issue Tags Organization

**For Midnight Expansion Development**

This document defines the tagging system used to categorize GitHub issues in the `MubarakHAlketbi/simc` repository.

---

## Tag Prefixes

All tags follow a `prefix:value` format for consistency and machine-readability.

### 1. `expansion:midnight`

All tasks related to the Midnight expansion.

- **Applies to:** Every issue
- **Color:** `#1d76db`

### 2. Task Types (`type:`)

What kind of work is needed?

| Label | Description | When to Use |
|-------|-------------|-------------|
| `type:general-changes` | General class/spec updates (new abilities, mechanics changes) | New spells, core class changes |
| `type:apl` | Default Action Priority List rotation | APL logic updates |
| `type:set-2pc` | 2-piece tier set bonus (MID1 2-set) | Set bonus implementation |
| `type:set-4pc` | 4-piece tier set bonus (MID1 4-set) | Set bonus implementation |
| `type:trinket` | Trinket special effect (raid or dungeon) | Trinket procs, unique effects |
| `type:consumable` | Food, flasks, potions, oils, enchants | Non-gear consumables |
| `type:talent` | Talent adjustments or new talent interactions | Talent-specific changes |

### 3. Classes (`class:`)

Which class is affected?

| Label | Class |
|-------|-------|
| `class:death-knight` | Death Knight |
| `class:demon-hunter` | Demon Hunter |
| `class:druid` | Druid |
| `class:evoker` | Evoker |
| `class:hunter` | Hunter |
| `class:mage` | Mage |
| `class:monk` | Monk |
| `class:paladin` | Paladin |
| `class:priest` | Priest |
| `class:rogue` | Rogue |
| `class:shaman` | Shaman |
| `class:warrior` | Warrior |
| `class:warlock` | Warlock |

### 4. Specializations (`spec:`)

Which specialization? (Used together with `class:`)

**Note:** Some spec names are shared across classes (e.g., `restoration`, `holy`). This is fine; combine with `class:` for clarity.

Common specs:
- Death Knight: `blood`, `frost`, `unholy`
- Demon Hunter: `havoc`, `vengeance`
- Druid: `balance`, `feral`, `guardian`, `restoration`
- Evoker: `devastation`, `preservation`, `augmentation`
- Hunter: `beast-mastery`, `marksmanship`, `survival`
- Mage: `arcane`, `fire`, `frost`
- Monk: `brewmaster`, `windwalker`, `mistweaver`
- Paladin: `holy`, `protection`, `retribution`
- Priest: `discipline`, `holy`, `shadow`
- Rogue: `assassination`, `outlaw`, `subtlety`
- Shaman: `elemental`, `enhancement`, `restoration`
- Warrior: `arms`, `fury`, `protection`
- Warlock: `affliction`, `demonology`, `destruction`

### 5. Status (`status:`)

Implementation progress.

| Label | Meaning |
|-------|---------|
| `status:nyi` | Not Yet Implemented (default for all created issues) |
| `status:in-progress` | Currently being worked on by an agent |
| `status:in-beta` | Implemented, needs testing/refinement |
| `status:implemented` | Complete and verified |
| `status:blocked` | Blocked (missing data, external dependency) |

### 6. Flags

Additional qualifiers.

| Label | Meaning |
|-------|---------|
| `needs-review` | Requires human review before merging |
| `needs-data` | Missing or uncertain game data from Wowhead |
| `priority:high` | High priority (critical path) |
| `priority:medium` | Medium priority |
| `priority:low` | Low priority / cleanup |

---

## Labeling Logic

When creating or triaging issues, apply labels in this order:

1. **Always:** `expansion:midnight`
2. **Determine type** from issue body's "Task Type" field → appropriate `type:...`
3. **Extract class/spec** from "Class / Spec / Item" field if it represents a playable class/spec:
   - If the first part is a known class (e.g., "Rogue", "Mage", "Death Knight"), apply `class:<class>` and `spec:<spec>`
   - If it's a gear slot or item category (e.g., "Weapon", "Enchants", "Raid Trinkets"), skip class/spec labels
4. **Set initial status:** `status:nyi`
5. **Add flag:** `needs-data` (since data sources are TBD until researched)

---

## Examples

### Class Ability
Title: `MIDNIGHT: General Changes - Mage Frost`
Labels: `expansion:midnight`, `type:general-changes`, `class:mage`, `spec:frost`, `status:nyi`, `needs-data`

### Set Bonus
Title: `MIDNIGHT: Set Bonus 4-set - Priest Shadow`
Labels: `expansion:midnight`, `type:set-4pc`, `class:priest`, `spec:shadow`, `status:nyi`, `needs-data`

### Trinket
Title: `MIDNIGHT: Raid Trinket - Gloom-Spattered Dreadscale`
Labels: `expansion:midnight`, `type:trinket`, `status:nyi`, `needs-data` (no class/spec)

### Consumable
Title: `MIDNIGHT: Potions - Potion of Recklessness`
Labels: `expansion:midnight`, `type:consumable`, `status:nyi`, `needs-data`

---

## Automation

New issues created from the issue template will be automatically labeled by the agent script during onboarding. See `apply_midnight_labels_final.py` for the tagging logic.

---

*Last updated: March 15, 2026*

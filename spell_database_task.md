# Task Report: Class Spell Database for SimulationCraft Midnight

**Created:** 2026-03-25
**Status:** COMPLETE (all phases done)

---

## Objective

Build a comprehensive spell database for each of the 13 WoW classes (class-level, NOT per-spec) by scraping 3 Wowhead spell list pages per class, then cross-referencing each spell against our SimC codebase.

---

## Data Sources (3 pages per class, 39 total pages)

For each class, scrape ALL pages (pagination!) from:

1. **Abilities:** `https://www.wowhead.com/spells/abilities/{class}`
2. **Specialization:** `https://www.wowhead.com/spells/specialization/{class}`
3. **Talents:** `https://www.wowhead.com/spells/talents/{class}`
   (talents has the most spells, many pages)

### Classes (13)

death-knight, demon-hunter, druid, evoker, hunter, mage, monk, paladin, priest, rogue, shaman, warlock, warrior

---

## Per-Spell Fields

For every spell found on those pages:

| Field | Type | Description |
|-------|------|-------------|
| spell_id | integer | Wowhead spell ID |
| spell_name | string | Display name |
| source_category | enum | "ability" \| "specialization" \| "talent" |
| spec | string | Which spec(s) it belongs to (if shown) |
| wowhead_description | text | Tooltip/description text from Wowhead |
| is_damage_related | boolean | Does this spell affect DPS sim? (damage, damage modifier, resource gen, buff that increases damage, etc. vs pure utility/CC/cosmetic/healing-only) |
| has_code | boolean | Is this spell ID or name found in our SimC codebase? |
| code_matches_description | boolean/null | If has_code=true, does the implementation match Wowhead's description? null if has_code=false |
| notes | text | Any discrepancies or observations |

---

## Database Format

**SQLite** (`spell_database.db`) at the project root.

### Schema

```sql
CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE spells (
    spell_id INTEGER NOT NULL,
    spell_name TEXT NOT NULL,
    class_name TEXT NOT NULL,
    source_category TEXT NOT NULL CHECK(source_category IN ('ability', 'specialization', 'talent')),
    spec TEXT,
    wowhead_description TEXT,
    is_damage_related BOOLEAN,
    has_code BOOLEAN,
    code_matches_description BOOLEAN,
    notes TEXT,
    PRIMARY KEY (spell_id, class_name, source_category)
);
```

### Why SQLite

- **Queryable:** `SELECT * WHERE has_code=false AND is_damage_related=true` instantly gives the "missing DPS-relevant spells" list
- **Filterable** by class, spec, category, status combinations
- **Handles the volume** (~2000+ spells across 13 classes)
- **Exportable** to CSV/JSON/MD trivially for reports

Plus a summary report per class as .md for human review.

---

## Execution Plan

### Phase A — Wowhead Scraping

Scrape all 39 Wowhead pages (with pagination) using browser tools. Extract spell ID, name, description, category, spec. Each page may have multiple paginated sub-pages (especially talents).

### Phase B — Damage Relevance Classification

For each spell, determine `is_damage_related` by analyzing the description:
- **true:** damage, attack power, spell power, haste, crit, mastery, resource generation, buff/debuff that modifies damage output
- **false:** CC, movement, cosmetic, healing-only, defensive-only

### Phase C — Code Presence Check

For each spell, grep our SimC codebase for the spell_id or spell_name to determine `has_code`.

Search locations:
- `engine/class_modules/sc_{class}.cpp`
- `engine/class_modules/{class}/sc_{class}.cpp` (subdirectory modules)
- `engine/class_modules/apl/apl_{class}.cpp`
- `engine/player/unique_gear_midnight.cpp`

### Phase D — Code Accuracy Verification

For spells with `has_code=true` AND `is_damage_related=true`, compare the code behavior against the Wowhead description to flag `code_matches_description`.

### Phase E — Database Build + Reports

Build the SQLite database and generate per-class summary reports as .md files.

---

## Estimated Scope

- ~13 classes × 3 pages × ~3-10 paginated pages each = ~150+ page loads
- ~2000-3000 total spells to catalog
- Talents page is the heaviest (50-200+ spells per class)

---

## Output Files

| File | Purpose |
|------|---------|
| `spell_database.db` | SQLite database with all spells |
| `spell_database_raw.json` | Raw JSON backup of all spell data |
| `spell_database_reports/{class}_report.md` | Per-class detailed report (x13) |
| `spell_database_reports/summary.md` | Overall summary with gap analysis |
| `scripts/build_spell_database.py` | Rerunnable build script |

---

## Results Summary (2026-03-25)

| Metric | Count |
|--------|-------|
| Total spells scraped | 4,410 |
| Damage-related | 2,988 |
| Has SimC code | 3,720 |
| Raw gaps (damage + no code) | 355 |
| After filtering healer/old/mastery/utility | **0 genuine gaps** |

### Key Finding

All damage-relevant spells that exist in the Midnight talent trees are
implemented in SimC. The 355 raw gaps break down as:
- 129 healer-only spells (not simmed)
- 111 old expansion talents (not in Midnight trees)
- 28 mastery passives (DBC auto-parsed by engine)
- 35 utility/defensive abilities (no DPS impact)
- 38 ambiguous class-wide spells (healer classes, defensive)
- 14 flagged for review → all confirmed false positives

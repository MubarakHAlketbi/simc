# SimulationCraft Project Structure Guide
## For Midnight Expansion Development

---

## Overview

SimulationCraft is a combat simulator for World of Warcraft. The codebase is organized into modular components with clear separation between data, simulation engine, class implementations, and user-facing profiles.

**Key Architecture Pattern**: Data-driven design where spell/item data is extracted from game client DBC files and compiled into the binary, while class-specific logic (spell mechanics, APL) is implemented in C++.

---

## Top-Level Directory Structure

```
./
├── engine/              # Core simulation engine and class implementations
├── profiles/            # Player profile definitions (.simc files)
├── ActionPriorityLists/ # Auto-generated default APL files (for reference)
├── dbc_extract3/        # DBC extraction tool from WoW client files
├── SpellDataDump/       # Raw spell data dumps from simc binary (used for generation)
├── source_files/        # Build system file lists (CMake, qmake, Visual Studio)
├── cli/                 # Command-line interface (minimal)
├── gui/                 # Qt-based GUI (if applicable)
├── qt/                  # Qt project files
├── tests/               # Automated test suite (Python-based)
├── util_scripts/        # Utility scripts for code formatting, etc.
├── cmake/               # Custom CMake modules
├── vs/                  # Visual Studio support files
├── WinReleaseScripts/   # Windows release packaging
├── doc/                 # Documentation
├── logos/               # Logo files
├── casc_extract/        # Blizzard CASC extraction tool
└── [Build files]        # CMakeLists.txt, .pro files, .sln files
```

---

## Core Engine (`engine/`)

The engine directory contains the heart of the simulator.

### Build Configuration

- **`engine/CMakeLists.txt`** - Build rules for the engine library; includes `../source_files/cmake_engine.txt` for source file list
- **`engine/Makefile`** - Alternative build system for Unix-like systems
- **`engine/simulationcraft.hpp`** - Main header file that includes most engine headers

### Core Systems

#### Actions and Spells (`engine/action/`)

```
action/
├── action.cpp/hpp           # Base action class (all spells/abilities derive from this)
├── attack.cpp/hpp           # Melee/ranged attack actions
├── spell.cpp/hpp            # Spell actions (magical damage/healing)
├── heal.cpp/hpp             # Healing actions
├── dot.cpp/hpp              # Damage-over-time effects
├── absorb.cpp/hpp           # Absorption shields
├── sequence.cpp/hpp         # Sequential action execution
├── parse_effects.cpp/hpp    # Parses spell effect data from DBC
├── variable.cpp/hpp         # Action variables for APL
├── dbc_proc_callback.cpp/hpp # Proc callbacks from DBC
└── ...                      # Other specialized action types
```

#### Buffs (`engine/buff/`)

- **`buff.cpp/hpp`** - Buff/debuff implementation with stacks, duration, refresh mechanics

#### Player and Character (`engine/player/`)

```
player/
├── player.cpp/hpp                 # Main player_t class (core character logic)
├── player_stat_cache.cpp/hpp      # Cached stat calculations
├── set_bonus.cpp/hpp              # Tier/trinket set bonus handling
├── unique_gear*.cpp/hpp           # Expansion-specific unique item effects:
│   ├── unique_gear_bfa.cpp        # Battle for Azeroth
│   ├── unique_gear_dragonflight.cpp
│   ├── unique_gear_legion.cpp
│   ├── unique_gear_midnight.cpp   # ⭐ MIDNIGHT EXPANSION - MAIN TARGET
│   ├── unique_gear_shadowlands.cpp
│   └── unique_gear_thewarwithin.cpp
├── azerite_data.cpp/hpp          # Azerite traits (BFA)
├── consumable.cpp/hpp            # Food, flasks, potions
├── talent.cpp/hpp                # Talent wrapper class
├── action_priority_list.cpp/hpp  # APL execution engine
├── pet.cpp/hpp                   # Pet implementation
├── pet_spawner_impl.hpp          # Pet spawner definitions
├── darkmoon_deck.cpp/hpp         # Darkmoon deck trinkets
├── ground_aoe.cpp/hpp            # Ground-based AoE effects
└── ...                           # Other player subsystems
```

#### Items (`engine/item/`)

```
item/
├── item.cpp/hpp           # Item_t class (equipment representation)
├── special_effect.cpp/hpp # Special item effects (procs, on-use)
├── enchants.cpp/hpp       # Enchantment definitions
└── ...                    # Other item-related code
```

#### DBC Data (`engine/dbc/`)

This is the data loading layer that reads from compiled DBC info.

```
dbc/
├── spell_data.cpp/hpp       # Spell data structures and query functions
├── sc_spell_data.cpp        # Loads spell data from sc_spell_data.inc
├── sc_item_data.cpp         # Loads item data from sc_item_data.inc
├── sc_const_data.cpp        # Loads constants (races, classes, etc.)
├── sc_extra_data.inc        # Extra data (base stats, scaling) - auto-generated
├── sc_extra_data_ptr.inc    # PTR version
├── trait_data.cpp/hpp       # Talent/trait data structures
├── specialization_spell.cpp/hpp # Specialization spell handling
├── class_spells.cpp/hpp     # Class-specific spell categorization
├── item_database.hpp        # Global item database access
├── item_data.cpp/hpp        # Item data from DBC
├── item_effect.cpp/hpp      # Item effect handling
├── item_set_bonus.cpp/hpp   # Set bonus definitions from DBC
├── gem_data.cpp/hpp         # Gem definitions
├── permanent_enchant.cpp/hpp # Enchant definitions
├── racial_spells.cpp/hpp    # Racial ability definitions
├── mastery_spells.cpp/hpp   # Mastery definitions
├── rank_spells.cpp/hpp      # Rank-based spell handling
├── real_ppm_data.cpp/hpp   # Real PPM proc rates
├── wow_version.cpp/hpp      # WoW version detection
└── generated/               # Auto-generated .inc files from dbc_extract.py
    ├── sc_spell_data.inc        # ~28MB - ALL spell data
    ├── sc_spell_data_ptr.inc
    ├── item_data.inc            # ~25MB - ALL item data
    ├── item_data_ptr.inc
    ├── trait_data.inc           # Talent/trait definitions (3,420 entries)
    ├── TraitEdge.csv            # Real prerequisite edges from DB2 (7,116 edges)
    ├── spelltext_data.inc       # Spell names, descriptions
    ├── item_bonus.inc           # Item bonus mappings
    ├── item_set_bonus.inc       # Set bonus definitions
    ├── ...                      # Many other data files
```

The `generated/` directory contains massive auto-generated C++ arrays from the DBC extraction process. These are compiled directly into the binary.

#### Class Modules (`engine/class_modules/`)

Each class has a main implementation file and possibly an APL subdirectory.

##### Main Class Files (Large monolithic implementations)

- **`sc_death_knight.cpp`** - Death Knight (Blood, Frost, Unholy)
- **`sc_demon_hunter.cpp`** - Demon Hunter (Havoc, Vengeance)
- **`sc_druid.cpp`** - Druid (Balance, Feral, Guardian, Restoration)
- **`sc_evoker.cpp`** - Evoker (Devastation, Preservation, Augmentation)
- **`sc_hunter.cpp`** - Hunter (Beast Mastery, Marksmanship, Survival)
- **`sc_mage.cpp`** - Mage (Arcane, Fire, Frost)
- **`sc_rogue.cpp`** - Rogue (Assassination, Outlaw, Subtlety)
- **`sc_shaman.cpp`** - Shaman (Elemental, Enhancement, Restoration)
- **`sc_warrior.cpp`** - Warrior (Arms, Fury, Protection)
- **`sc_enemy.cpp`** - Enemy AI/combat routines

##### Split Class Directories

Some classes are split across multiple files in subdirectories:

- **`monk/`**
  - `sc_monk.cpp`, `sc_monk.hpp`
  - `sc_monk_pets.cpp` (pet definitions)
  - `sc_stagger.cpp` (Stagger mechanic)
- **`paladin/`**
  - `sc_paladin.cpp`
  - `sc_paladin_holy.cpp`
  - `sc_paladin_protection.cpp`
  - `sc_paladin_retribution.cpp`
- **`priest/`**
  - `sc_priest.cpp`
  - `sc_priest_discipline.cpp`
  - `sc_priest_holy.cpp`
  - `sc_priest_shadow.cpp`
  - `sc_priest_pets.cpp` (Shadowfiend, etc.)
- **`warlock/`**
  - `sc_warlock.cpp`
  - `sc_warlock_actions.cpp`
  - `sc_warlock_init.cpp` (initialization)
  - `sc_warlock_pets.cpp` (pet definitions)

##### Class Header

- **`class_module.hpp`** - Common base class and utilities for all class modules

#### Action Priority Lists (`engine/class_modules/apl/`)

These C++ files define the default APL logic that gets compiled into the binary and later exported to text format.

```
apl/
├── apl_death_knight.cpp/hpp
├── apl_demon_hunter.cpp/hpp
├── apl_evoker.cpp/hpp
├── apl_hunter.cpp/hpp
├── apl_warrior.cpp/hpp
├── apl_rogue.cpp/hpp
├── apl_shaman.cpp/hpp
├── mage.cpp/hpp          # Mage APL
├── warlock.cpp/hpp       # Warlock APL
├── monk/                  # Monk APL (split)
├── hunter/                # Hunter APL variations
├── rogue/                 # Rogue APL variations
├── shaman/                # Shaman APL variations
├── demon_hunter/          # DH APL (already split)
├── *.inc                  # Generated APL fragments for specializations
│   ├── balance_apl.inc
│   ├── feral_apl.inc
│   ├── guardian_apl.inc
│   ├── restoration_druid_apl.inc
│   └── retribution_apl.inc
└── ConvertAPL.py          # Converts C++ APL to text format
```

The APL system uses a domain-specific language embedded in C++ via action priority list objects.

#### Other Engine Subsystems

```
engine/
├── sim/                  # Simulation core (event queue, iterations, etc.)
│   ├── sim.cpp/hpp      # Main simulation loop
│   ├── event.cpp/hpp    # Event system
│   ├── option.cpp/hpp   # Simulation options
│   ├── cooldown.cpp/hpp # Cooldown tracking
│   └── ...
├── report/               # Reporting and output generation
│   ├── reports.cpp/hpp
│   ├── json/             # JSON output
│   └── ...
├── interfaces/           # HTTP, BCP API, JavaScript interfaces
├── util/                 # Utilities (string, math, IO, RNG, etc.)
└── lib/                  # Third-party libraries (fmt, rapidjson, rapidxml, etc.)
```

---

## Spell Data Flow

### 1. Extraction Phase

**Tool**: `dbc_extract3/dbc_extract.py`

```bash
# Extract all spell data from WoW DBC files
./dbc_extract3/dbc_extract.py -b <build_number> -t spell -p /path/to/dbc > sc_spell_data.inc
```

This generates the massive `engine/dbc/generated/*.inc` files.

### 2. Data Compilation

The `.inc` files are included by C++ source files (e.g., `sc_spell_data.cpp`) via `#include` directives. They contain statically initialized arrays that the binary links directly.

### 3. Runtime Access

- `spell_data_t` structures provide queryable access to spell properties (damage, coefficient, mana cost, etc.)
- `dbc::find_spell(spell_id)` returns spell data
- Class modules call `player->find_spell(spell_id)` to get spell data for abilities

---

## Item and Trinket System

### Data Sources

1. **DBC Item Data**: `SpellDataDump/nonclass.txt` contains all non-class spells (items, enchants, set bonuses, etc.). Used to generate `item_data.inc`, `item_bonus.inc`, `item_set_bonus.inc`.

2. **Special Effects**: Complex trinket/item procs are implemented manually in:
   - **`engine/player/unique_gear_<expansion>.cpp`** for expansion-specific unique effects
   - **`engine/item/special_effect.cpp`** for the special effect infrastructure

### Where to Add New Trinket/Item Effects

**For Midnight expansion items**:
- Add registration code in `engine/player/unique_gear_midnight.cpp`
- The file uses `register_special_effect(spell_id, callback)` to hook custom behavior
- Also handles: food, flasks, gems, enchants, set bonuses specific to Midnight

**Example pattern**:
```cpp
// In unique_gear_midnight.cpp
void register_special_effects()
{
  // Register a trinket with custom behavior
  register_special_effect( SPELL_ID, []( special_effect_t& effect )
  {
    // Custom initialization: proc rate, buff, damage formula, etc.
    effect.proc_chance_ = 15;
    effect.custom_buff = new buff_t( ... );
  } );
}
```

### Set Bonuses

- Set bonuses from DBC are auto-parsed but may need manual overrides in `unique_gear_midnight.cpp` if they require special logic.
- The `set_bonus.cpp/hpp` implements the generic set bonus tracker.

---

## Talent System

### Data Flow

1. **DBC Extraction**: Talent definitions come from `Trait.dbc` (and related tables). Generated into `generated/trait_data.inc` (3,420 entries).
2. **Prerequisite Edges**: `engine/dbc/generated/TraitEdge.csv` — 6,409 real Type 2 edges from DB2 `TraitEdge` table (build 12.0.1.66384). Replaces old heuristic edge builder.
3. **Access**: `trait_data_t` structures define talent nodes, spells, requirements.
4. **Selection**: Player talents are selected via `player->talents` and `player_talent_t` wrapper.

### Talent Validation & Optimization Tooling

| Script | Purpose |
|--------|---------|
| `scripts/lib/talent_tree.py` | DBC tree parser + real TraitEdge.csv edges |
| `scripts/lib/talent_codec.py` | Base64 talent string encode/decode |
| `scripts/lib/tree_codec_bridge.py` | Tree↔codec bridge, high-level API |
| `scripts/lib/talent_validator.py` | Build validation (budget, prereqs, gates) + neighbor generation |
| `scripts/talent_local_search.py` | Hill-climbing talent optimizer |
| `scripts/talent_build_compare.py` | Wowhead build comparison |
| `scripts/validate_all_profiles.py` | Validate all 56 profiles against tree constraints |

### Midnight Point Budgets

- **Class tree**: 34 purchasable points + granted nodes (0-3 depending on spec)
- **Spec tree**: 34 purchasable points
- **Hero tree**: 15 nodes auto-granted (one hero tree chosen via selection node)
- Hero trees are shared between 2 specs; internal nodes may be tagged with only one spec's id_spec but both can use them

### Where to Modify Talent Logic

- **Base talent mechanics**: `engine/player/talent.cpp/hpp` (rarely needs changes)
- **Class-specific talent effects**: Inside the class implementation file (`sc_<class>.cpp` or subdirectory files)
  - Talents typically modify spell damage, add effects, or change behavior
  - Often implemented by overriding spell effect calculations or adding buffs

**Example**: A talent that increases damage of a specific spell would be handled in the class's `create_action()` or in a specific spell's `calculate` method, checking `player->talents->talent_rank( "Talent Name" )`.

---

## Action Priority Lists (APL)

### Generation Process

1. **C++ Implementation**: APL logic is written in C++ in `engine/class_modules/apl/apl_<class>.cpp`. These files contain functions that build an `action_priority_list_t` object programmatically.

2. **Export to Text**: The `ConvertAPL.py` script (or build process) generates human-readable `.simc` files:
   - **`ActionPriorityLists/default/*.simc`** - Auto-generated for each spec
   - These are **NOT** to be manually edited (per README.md)
   - They are provided for reference and can be used directly in simulations

### Custom APL

Users write their own APL in profile files or via the Advanced APL box in Raidbots. The simulator parses and executes this at runtime. The default APL files serve as examples.

### Where to Change Default APL

Modify the C++ source in `engine/class_modules/apl/apl_<class>.cpp`. The APL functions typically look like:

```cpp
void apl_<class>( action_priority_list_t* apl )
{
  apl->add_action( "spell_name" );
  apl->add_action( "spell_name", "if=condition" );
  // ...
}
```

---

## Profiles (`profiles/`)

### Organization

```
profiles/
├── generators/           # Profile generation scripts (e.g., for Pre-Raid)
├── PreRaids/             # Pre-raid gear profiles
├── MID1/                 # ⭐ MIDNIGHT EXPANSION PROFILES
│   ├── MID1_<Class>_<Spec>.simc
│   └── ...
├── tests/                # Test profiles
└── CI.simc               # Continuous Integration profile list
```

Profiles contain:
- Race, class, specialization
- Talent selections
- Gear with enchants/gems
- Consumables
- APL override (optional)

### Adding New Profiles

Create new `.simc` files in the appropriate expansion directory following the naming convention: `<expansion>_<Class>_<Spec>_<Variant>.simc`.

---

## Build System

### CMake (Primary)

- **`CMakeLists.txt`** (root) - Main project configuration
  - Adds `engine` subdirectory
  - Adds `qt` subdirectory if `BUILD_GUI=ON`
  - Adds `tests` subdirectory if `BUILD_TESTING=ON`
  - Creates `simc` executable linking `engine`

- **`engine/CMakeLists.txt`** - Defines `engine` library
  - Includes source list from `source_files/cmake_engine.txt`
  - Sets compiler options, dependencies (Threads, CURL, etc.)

- **`source_files/cmake_engine.txt`** - Explicit list of all `.cpp` and `.hpp` files
  - This is the **canonical source list**; new files must be added here
  - Headers listed first, then implementation files

- **`cmake/`** - Custom CMake modules (e.g., `package.cmake`)

### qmake (Alternative)

- **`simulationcraft.pro`** - qmake project file
- **`simulationcraft.pri`** - Common includes
- **`source_files/QT_engine.pri`** - Source list for qmake
- Similar structure for GUI: `simulationcraft-qt.pro`

### Visual Studio

- **`simc_vs20XX.sln`** - Solution files for VS 2017, 2019, 2022, 2026
- **`source_files/VS_engine.props`** - Source file lists for VS

### Makefile

- **`engine/Makefile`** - Direct make build (invokes `make -f engine_main_make`)

---

## Data Generation Pipeline

### Step 1: Extract DBC Files

Use `dbc_extract3/dbc_extract.py` with a World of Warcraft client's DBC files:

```bash
# Extract spells
python3 dbc_extract3/dbc_extract.py -b 12345 -t spell -p ./dbc > engine/dbc/generated/sc_spell_data.inc

# Extract items
python3 dbc_extract3/dbc_extract.py -b 12345 -t item -p ./dbc > engine/dbc/generated/item_data.inc

# Extract traits/talents
python3 dbc_extract3/dbc_extract.py -b 12345 -t trait -p ./dbc > engine/dbc/generated/trait_data.inc

# ... and others
```

Configuration files in `dbc_extract3/` specify build numbers for live/PTR (e.g., `live.conf`, `ptr.conf`).

### Step 2: Generate Spell Data Dumps (Optional)

Run the built simulator to output queries:

```bash
./engine/simc display_build="0" spell_query="spell.class=mage" > SpellDataDump/mage.txt
./engine/simc display_build="0" spell_query="spell" > SpellDataDump/allspells.txt
./engine/simc display_build="0" spell_query="spell.class=none" > SpellDataDump/nonclass.txt
```

These dumps are used for analysis, not compilation.

### Step 3: Generate Default APL Text

After building, run:

```bash
# Usually part of build process or:
./generate_profiles.sh
```

This creates/updates:
- `ActionPriorityLists/default/*.simc` (auto-generated)
- May also update `profiles/` directory

---

## Important Configuration and Constants

### Game Version Detection

- **`engine/dbc/wow_version.cpp/hpp`** - Detects build number and data version
- Build number determines which data variant (live vs PTR) to load
- Midnight expansion likely uses build numbers in the 10.x or 11.x range (verify)

### Enumerations

- **`engine/sc_enums.hpp`** - Master list of enums (classes, specs, resources, races, etc.)
  - `class_e`: WARRIOR, MAGE, etc.
  - `specialization_e`: Specific specs (e.g., MAGE_ARCANE)
  - `spell_e`: Enumerated spell IDs (auto-generated from data?)
  - `action_e`: Action types
  - Many more

These enums are used throughout the codebase.

### Scaling and Formulas

- **`engine/dbc/generated/sc_scale_data.inc`** - Scaling coefficients (spell damage, health, etc. by level)
- **`engine/dbc/generated/sc_specialization_data.inc`** - Spec-specific multipliers
- **`engine/player/rating.cpp/hpp`** - Rating-to-stat conversions

---

## Testing

- **`tests/`** directory contains Python test framework
  - `run.py` - Main test runner
  - `helper.py` - Test utilities
  - Tests execute simc with various inputs and compare results to expected values
- Run with: `python3 tests/run.py` (from build dir or after install)
- CI runs tests automatically on push

---

## Mapping: Issue Types to Files

### "Add/Update a class ability (spell)"

1. **Spell data** already exists in DBC → already in `generated/sc_spell_data.inc`
2. **Implement the action** in the class file:
   - If new ability: Add method in `engine/class_modules/sc_<class>.cpp` (or appropriate sub-file)
   - Derive from `spell_t` or `special_action_t`
   - Define constructor, `impact()`, `calculate()`, etc.
3. **Add to APL** (if default behavior should change):
   - Modify `engine/class_modules/apl/apl_<class>.cpp`
4. **Re-generate APL text**: Run generate script
5. **Verify**: Test profile uses the ability correctly

### "Fix spell damage/healing coefficient"

1. Check spell data parsing in `engine/action/parse_effects.cpp` (general) or class-specific `create_<spell>()` methods
2. Adjust formula in the spell's action class `calculate_damage()` or similar
3. May involve `spell_data_t` effect queries: `spell->effectN( X ).average()`, `spell->effectN( X ).coef()`

### "Add new trinket or unique item effect"

**Midnight expansion items go in**: `engine/player/unique_gear_midnight.cpp`

1. Find the spell ID from `SpellDataDump/nonclass.txt` or in-game
2. In `register_special_effects()`, add:
   ```cpp
   register_special_effect( <spell_id>, []( special_effect_t& effect )
   {
     // Setup: proc rate, buff, triggers, damage, etc.
     effect.custom_buff = new buff_t( ... );
     effect.trigger_action = create_action<...>();
   } );
   ```
3. Implement custom buff/action classes as needed (can be lambdas or separate classes)
4. May also need to adjust `set_bonus` handling in same file

### "Update set bonuses (tier, trinket sets)"

- DBC set bonuses auto-loaded; complex logic in `engine/player/set_bonus.cpp`
- For Midnight-specific unique set bonuses: add/modify in `unique_gear_midnight.cpp`
  - Look for `register_set_bonus()` calls or similar patterns

### "Adjust talent behavior"

1. Locate talent effect in class implementation:
   - Talent definition comes from DBC (in `trait_data.inc`)
   - Effect is usually a spell or modifier
2. Find where the talent's spell is used in class actions
3. Add conditional checks: `if ( p->talents->talent_rank( "Talent Name" ) )`
4. Modify calculations accordingly

Example: Talent that increases Fireball damage:
```cpp
double fireball_t::calculate_damage( ...
{
  double dmg = ...;
  if ( p->talents->talent_pyromania.ok() )  // using talent wrapper
    dmg *= 1.25;
  return dmg;
}
```

### "Add new consumable (food/flask/potion)"

- **Food/flasks**: `unique_gear_midnight.cpp` in `namespace consumables`
- **Potions**: Similar, often in `unique_gear_midnight.cpp` or `engine/item/enchants.cpp`
- Use existing patterns: `selector_food()`, `primary_food()`, `potion_stat()`, etc.

### "Fix stat scaling or ratings**

- **Rating conversions**: `engine/player/rating.cpp` (`rating_t` class)
- **Secondary stat formulas**: `engine/player/player_stat_cache.cpp` (e.g., `calculate_haste()`, `calculate_crit()`)
- **Primary stats**: `engine/player/player.cpp` (`calculate_base_*()` methods)

### "Update default APL for a spec**

Edit `engine/class_modules/apl/apl_<class>.cpp`. Find the APL-building function for that class (often `apl_<class>( action_priority_list_t* )` or similar). Add/remove actions or conditions.

**Then run** the APL generation to update the text files:
```bash
# Build simc first, then:
./generate_profiles.sh
# or manually:
./engine/simc ... generate_apl=1
```

### "Fix simulation core (event queue, iteration, etc.)"

- **Event system**: `engine/sim/event.cpp/hpp`, `engine/sim/event_manager.cpp/hpp`
- **Main loop**: `engine/sim/sim.cpp/hpp`
- **Options**: `engine/sim/option.cpp/hpp`

### "Add new race or class"

1. Add race/class enums to `engine/sc_enums.hpp`
2. Add base stats in `engine/dbc/generated/sc_extra_data.inc` (manual table updates)
3. Add racial spells in `engine/dbc/generated/racial_spells.inc` (from DBC extraction)
4. If new class: create new `sc_<class>.cpp` file
5. Update class mask definitions

### "Fix parsing of spell effects from DBC**

- **`engine/action/parse_effects.cpp`** - General spell effect parsing (power costs, damage multipliers)
- **`engine/dbc/spell_data.cpp`** - Spell data query functions

---

## Important Conventions

### Naming

- **Files**: `sc_<class>.cpp` for main class, `apl_<class>.cpp` for APL
- **Class names**: `<class>_t` (e.g., `mage_t`, `spell_t`)
- **Functions**: snake_case or camelCase (mixed; follow existing style)
- **Namespaces**: `namespace <class>` (lowercase) or `unique_gear::<expansion>`

### Data Inclusion

- **Headers**: `.hpp` files containing class declarations
- **Implementation**: `.cpp` files containing definitions
- **Large data arrays**: `.inc` files (included via `#include "file.inc"`)

### Expansion-Specific Code

- Midnight-specific: `unique_gear_midnight.cpp/hpp`, files in `profiles/MID1/`
- Guard with version checks if necessary:
  ```cpp
  if ( !player->dbc || player->dbc->wow_version() < midnight_version )
    return;
  ```

### Registration Pattern

Many systems use a registration function called during initialization:

```cpp
// In unique_gear_midnight.cpp
static void register_midnight_special_effects()
{
  register_special_effect( SPELL_ID, init_callback );
}
// Called from unique_gear::midnight::register_special_effects()
```

### Spell ID References

Spell IDs are typically defined as constants:
- In `engine/sc_enums.hpp` as `spell_e` enum values (may be auto-generated)
- Or just use raw numbers (less common now)
- Use `find_spell( <id> )` to get `spell_data_t*`

---

## Quick Reference Table

| Component | Primary Location(s) | Purpose |
|-----------|-------------------|---------|
| Class abilities | `engine/class_modules/sc_<class>.cpp` | Implement spell actions, buffs, resources |
| Class APL (default) | `engine/class_modules/apl/apl_<class>.cpp` | Default action priority list generation |
| Spell data | `engine/dbc/generated/sc_spell_data.inc` | Raw spell properties (auto-generated) |
| Item data | `engine/dbc/generated/item_data.inc` | Raw item properties |
| Talent data | `engine/dbc/generated/trait_data.inc` | Talent tree definitions (3,420 entries) |
| Talent edges | `engine/dbc/generated/TraitEdge.csv` | Real prerequisite edges (6,409 Type 2) |
| Trinket/unique item logic | `engine/player/unique_gear_<expansion>.cpp` | Custom item procs/special effects |
| Set bonuses | `engine/player/set_bonus.cpp` + `unique_gear_<exp>.cpp` | Tier/class set handling |
| Base stats/scaling | `engine/dbc/generated/sc_extra_data.inc` | Base stats by level/class |
| Buffs/debuffs | `engine/buff/buff.cpp` | Buff implementation |
| Action mechanics | `engine/action/*.cpp` | Spell/attack/heal base classes |
| Profiles | `profiles/<expansion>/*.simc` | Ready-to-run character definitions |
| Default APL text | `ActionPriorityLists/default/*.simc` | Auto-generated APL output |
| Build system | `CMakeLists.txt`, `source_files/*.txt` | Compilation rules |
| DBC extraction | `dbc_extract3/dbc_extract.py` | Convert WoW DBC to .inc files |

---

## Midnight Expansion Specific

**Midnight** is the current working expansion. Key files:

- `engine/player/unique_gear_midnight.cpp` - **Central file for new item effects**
  - Version check: `wowv_t version_min = { 12 };` (build 12 is likely Midnight)
  - Register consumables, gems, enchants, trinkets, set bonuses
- `profiles/MID1/` - Production-ready profiles for all specs
- `ActionPriorityLists/default/` contains APL with `MID1_` prefix generated from C++ code
- Ensure `wow_version()` checks align with Midnight build numbers in `dbc/wow_version.cpp`

---

## Summary Workflow for Common Tasks

1. **New spell for existing class**
   - Confirm spell ID in `SpellDataDump/allspells.txt`
   - Implement action in `sc_<class>.cpp`
   - Add to APL if default usage needed (`apl_<class>.cpp`)
   - Test with profile

2. **New trinket for Midnight**
   - Get spell ID from game/dumps
   - Add registration in `unique_gear_midnight.cpp`
   - Implement custom buff/action if complex
   - Test with profile equipping the trinket

3. **Talent adjustment**
   - Find talent in DBC trait data or existing code
   - Modify class code where talent effect is applied
   - Update APL if necessary

4. **Data update (spells/items changed by patch)**
   - Re-run `dbc_extract3/dbc_extract.py` with new client DBC
   - Regenerate `.inc` files
   - May need to adjust class code for changed formulas
   - Regenerate profiles/APL

5. **Build changes**
   - Add new `.cpp/.hpp` to `source_files/cmake_engine.txt` (and other build systems)
   - Ensure CMakeLists.txt includes the directory if new subdirectory

---

## Additional Resources

- **`AGENTS.md`** - Notes for AI agents working on the codebase
- **`CONTRIBUTING.md`** - Contribution guidelines
- **`README.md`** - Project overview and build instructions
- **`project_progress.md`** - Current development status and tasks
- **`OPTIMIZATION_HOWTO.md`** - Step-by-step manual guide to optimize any spec (talents + APL)
- **`APL_optimization.md`** - APL syntax reference, expression tokens, rules, common mistakes
- **`optimization_action_plan.md`** - Optimization architecture, data sources, compute estimates

---

*Last updated: March 29, 2026*  
*SimulationCraft codebase analysis for Midnight expansion development*

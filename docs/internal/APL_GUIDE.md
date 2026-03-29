# SimulationCraft Action Priority List (APL) Guide
## Midnight Expansion Edition

**Last Updated:** 2026-03-17
**Applies to:** SimulationCraft Midnight branch (12.0.1)

---

## Table of Contents

1. [What Is an APL?](#1-what-is-an-apl)
2. [APL File Locations](#2-apl-file-locations)
3. [APL Syntax: The .simc Format](#3-apl-syntax-the-simc-format)
4. [Conditions Reference](#4-conditions-reference)
5. [Action Modifiers](#5-action-modifiers)
6. [Variables](#6-variables)
7. [Call Action List](#7-call-action-list)
8. [Building APLs in C++](#8-building-apls-in-c)
9. [Walkthrough: Affliction Warlock APL](#9-walkthrough-affliction-warlock-apl)
10. [Common Patterns](#10-common-patterns)
11. [Testing APL Changes](#11-testing-apl-changes)
12. [Midnight-Specific APL Notes](#12-midnight-specific-apl-notes)

---

## 1. What Is an APL?

An **Action Priority List** is SimulationCraft's rotation system. It is a sequential list of
combat actions (spells, abilities, item uses) each with an optional condition. On every GCD
the simulator evaluates the list top-to-bottom and executes the **first action whose condition
is true** and whose spell is ready (off cooldown, resources available, target in range).

APLs determine the DPS output of a simulation. A well-written APL closely mirrors expert
player rotation guides. A poor APL results in artificially low DPS.

**Key properties:**
- Evaluated every GCD (and off-GCD window if applicable)
- Pure priority system — no state machine, no decision tree
- Conditions are arithmetic/logical expressions evaluated in real-time against sim state
- All spell names, buff names, cooldown names use snake_case versions of the in-game name

---

## 2. APL File Locations

APLs live in two places:

### C++ Source (authoritative)
```
engine/class_modules/apl/
  apl_death_knight.cpp / .hpp
  apl_demon_hunter.cpp / .hpp
  apl_evoker.cpp / .hpp
  apl_hunter.cpp / .hpp
  apl_monk.cpp         (no .hpp)
  apl_paladin.cpp / .hpp
  apl_priest.cpp / .hpp
  apl_rogue.cpp / .hpp
  apl_shaman.cpp / .hpp
  apl_warrior.cpp / .hpp
  mage.cpp / .hpp
  warlock.cpp / .hpp
```

Each file contains one function per spec (e.g. `warlock_apl::affliction(player_t* p)`).
The function is called during `player_t::init_action_list()` in the class module.

### .simc Profile Format (exported / user-editable)
When you run a sim or export from SimC, actions appear in .simc files:
```
profiles/MID1/MID1_Warlock_Affliction_Hellcaller.simc
```
These are the same APL but in text form. SimC auto-generates these at the top of profile
files with the comment `# This default action priority list is automatically created...`

The C++ source and .simc format are **equivalent** — changes to one can be expressed as the
other. The C++ version is compiled into the binary; the .simc format can override it at runtime.

---

## 3. APL Syntax: The .simc Format

### Basic structure

```
# Precombat list (runs once before combat)
actions.precombat=snapshot_stats
actions.precombat+=/summon_pet
actions.precombat+=/haunt,if=active_enemies<2

# Main combat list (evaluated every GCD)
actions=call_action_list,name=variables
actions+=/call_action_list,name=cooldowns
actions+=/agony,if=!ticking|refreshable
actions+=/corruption,if=!ticking|refreshable
actions+=/shadow_bolt
```

**Rules:**
- First line for a list: `actions.NAME=ACTION`
- Subsequent lines: `actions.NAME+=/ACTION`
- `actions=` and `actions+=/` are shorthand for `actions.default=`
- Comments start with `#`
- No semicolons — one action per line

### Action syntax

```
action_name[,modifier=value[,modifier=value...]]
```

Everything after the action name is a comma-separated modifier list.

```
# Simple unconditional action
shadow_bolt

# Action with condition
agony,if=!ticking|refreshable

# Action with multiple modifiers
drain_soul,chain=1,early_chain_if=buff.nightfall.react,interrupt_if=tick_time>0.5
```

### Named sublists

```
# Define a named sublist
actions.ogcd=potion,if=...
actions.ogcd+=/berserking,if=...

# Call it from default
actions+=/call_action_list,name=ogcd
```

---

## 4. Conditions Reference

All conditions go in `if=EXPR`. Expressions use standard arithmetic (`+`, `-`, `*`, `/`),
comparison (`=`, `!=`, `<`, `>`, `<=`, `>=`), and logical (`&` = AND, `|` = OR, `!` = NOT).
Parentheses group sub-expressions.

### 4.1 Buff Conditions

```
buff.NAME.up              # buff is active (1 if yes, 0 if no)
buff.NAME.down            # buff is NOT active
buff.NAME.react           # stacks of buff available to consume
buff.NAME.stack           # current stack count
buff.NAME.max_stack       # maximum stacks
buff.NAME.remains         # seconds remaining on buff
buff.NAME.duration        # full duration of buff
buff.NAME.refreshable     # buff can be refreshed (within pandemic window)
```

Examples:
```
buff.recklessness.up
buff.nightfall.react>1
buff.bloodlust.up|buff.heroism.up
buff.power_infusion.remains>10
```

### 4.2 Cooldown Conditions

```
cooldown.NAME.ready       # off cooldown (equiv: cooldown.NAME.remains=0)
cooldown.NAME.remains     # seconds until off cooldown
cooldown.NAME.charges     # current charges available
cooldown.NAME.max_charges # maximum charges
cooldown.NAME.charges_fractional  # charges including partial recharge
cooldown.NAME.recharge_time       # time until next charge
```

Examples:
```
cooldown.summon_darkglare.ready
cooldown.dark_harvest.remains<3
cooldown.sinful_brand.charges>=1
```

### 4.3 DoT / Debuff Conditions

```
dot.NAME.ticking          # dot is on target
dot.NAME.remains          # seconds remaining
dot.NAME.duration         # full duration
dot.NAME.refreshable      # within pandemic window (can reapply without loss)
dot.NAME.stack            # stacks (for stackable dots)
dot.NAME.pmultiplier      # persistent damage multiplier when dot was applied
```

Examples:
```
dot.corruption.ticking
!dot.agony.ticking|dot.agony.refreshable
dot.shadow_word_pain.remains<3
```

### 4.4 Resource Conditions

```
soul_shard              # current soul shards (Warlock)
soul_shard.deficit      # max_shards - current
energy                  # current energy (Rogue/Druid/Monk)
energy.deficit          # max_energy - current
energy.regen            # regen rate (per second)
energy.time_to_max      # seconds to reach cap
rage                    # current rage (Warrior)
runic_power             # current runic power (DK)
mana                    # current mana
mana.pct                # mana as percent of max
holy_power              # current holy power (Paladin)
chi                     # current chi (Monk)
combo_points            # current combo points (Rogue/Feral Druid)
fury                    # current fury (Demon Hunter)
pain                    # current pain (Vengeance DH)
maelstrom               # current maelstrom (Shaman)
astral_power            # current astral power (Balance Druid)
insanity                # current insanity (Shadow Priest)
```

Examples:
```
soul_shard<3
energy>=50
combo_points>=5
rage>60
holy_power=5
insanity<=50
```

### 4.5 Target Conditions

```
target.health.pct         # target health as percentage
target.health.pct<=20     # execute threshold check
active_enemies            # number of enemies in combat
target.time_to_die        # estimated seconds until target dies
target.distance           # distance to target in yards
target.debuff.NAME.up     # debuff on current target
```

Examples:
```
target.health.pct<20
active_enemies>=3
target.time_to_die>5
```

### 4.6 Player State Conditions

```
health.pct                # player health as percentage
time                      # seconds elapsed since combat start
fight_remains             # estimated seconds until end of fight
time_to_die               # alias for fight_remains
in_combat                 # 1 if in combat
movement.distance         # distance currently moving
moving                    # 1 if moving
cast_time                 # current action cast time
execute_time              # cast_time or gcd, whichever is longer
gcd                       # current GCD duration
tick_time                 # tick time of current channel
```

Examples:
```
fight_remains<15
health.pct<35
time>5
```

### 4.7 Talent Conditions

```
talent.NAME.enabled       # talent is selected (also: talent.NAME)
talent.NAME.rank          # rank of the talent (for multi-rank talents)
```

Examples:
```
talent.grimoire_of_sacrifice.enabled
talent.malefic_grasp
talent.phalanx.rank>=2
```

### 4.8 Spec / Hero Tree Conditions

```
spec.NAME                 # current specialization
hero_tree.NAME            # current hero talent tree
```

Examples:
```
hero_tree.soul_harvester
hero_tree.hellcaller
spec.fury
```

### 4.9 Set Bonus Conditions

```
set_bonus.NAME_2pc        # 2-piece set bonus active
set_bonus.NAME_4pc        # 4-piece set bonus active
```

Examples:
```
set_bonus.mid1_4pc
```

### 4.10 Pet Conditions

```
pet.NAME.active           # pet is active
pet.NAME.remains          # seconds until pet expires
```

Examples:
```
pet.darkglare.active
pet.darkglare.remains>gcd
```

### 4.11 Trinket Conditions

```
trinket.1.has_use_buff              # slot 1 trinket has a use-on-buff effect
trinket.2.has_cooldown              # slot 2 trinket has a cooldown
trinket.1.is.NAME                   # item in slot 1 is NAME
trinket.1.proc.any_dps.up          # trinket 1 DPS proc is active
trinket.1.proc.any_dps.remains     # seconds remaining on proc
trinket.1.cooldown.ready           # trinket 1 on-use ready
trinket.1.cooldown.remains         # seconds until trinket 1 on-use ready
```

Examples:
```
trinket.1.has_use_buff
!trinket.1.is.treacherous_transmitter
trinket.2.cooldown.remains<2
```

### 4.12 Action/Spell Conditions

```
action.NAME.casting       # action is currently being cast
action.NAME.in_flight     # action is in the air (travel time)
variable.NAME             # previously set variable value
prev.NAME                 # previous action used was NAME
prev_gcd.1.NAME           # 1 GCD ago the action was NAME
```

---

## 5. Action Modifiers

These are comma-separated key=value pairs after an action name.

| Modifier | Type | Description |
|----------|------|-------------|
| `if=EXPR` | condition | Execute only when expression is true |
| `target_if=max:EXPR` or `target_if=min:EXPR` | targeting | Execute on target that maximizes/minimizes expression |
| `chain=1` | bool | For channels: re-evaluate next tick instead of waiting for full cast |
| `early_chain_if=EXPR` | condition | With chain=1: break chain early when expr is true |
| `interrupt_if=EXPR` | condition | Interrupt channel when expr becomes true |
| `interrupt=1` | bool | Always interrupt when something better is ready |
| `interrupt_global=1` | bool | Interrupt even if next action has a cast time |
| `moving=1` | bool | Only execute while moving |
| `line_cd=N` | float | Minimum seconds between uses of this action line |
| `cycle_targets=1` | bool | Cycle through all targets |
| `max_cycle_targets=N` | int | Maximum targets to cycle through |
| `use_off_gcd=1` | bool | Execute as off-GCD action (doesn't consume GCD) |
| `use_while_casting=1` | bool | Queue while casting |
| `wait_on_ready=N` | float | Wait up to N seconds for this action instead of moving on |
| `sec=N` | float | Time offset for the action |

Examples:
```
# Use trinket on specific condition
use_item,name=trinket_name,if=cooldown.NAME.ready

# Interrupt a channel if a proc occurs
drain_soul,interrupt_if=tick_time>0.5

# Chain channeling with early exit
drain_soul,chain=1,early_chain_if=buff.nightfall.react,interrupt_if=tick_time>0.5

# Target with lowest health for execute
execute,target_if=min:target.health.pct

# Off-GCD with condition
potion,if=!flask&fight_remains<30,use_off_gcd=1
```

---

## 6. Variables

Variables store computed values that would be expensive or verbose to repeat inline.
They are recalculated each time the variable action is evaluated in the list.

```
variable,name=VAR_NAME,op=OPERATION,value=EXPR[,value_else=EXPR][,condition=EXPR]
```

### Operations

| op | Effect |
|----|--------|
| `set` | VAR = value |
| `setif` | VAR = value if condition, else value_else |
| `add` | VAR += value |
| `sub` | VAR -= value |
| `mul` | VAR *= value |
| `div` | VAR /= value |
| `min` | VAR = min(VAR, value) |
| `max` | VAR = max(VAR, value) |
| `floor` | VAR = floor(VAR) |
| `ceil` | VAR = ceil(VAR) |
| `reset` | VAR = default (0) |

### Usage

```
# In precombat: initialize
precombat->add_action("variable,name=trinket_1_buffs,value=trinket.1.has_use_buff");

# In variables sublist: update each GCD
variables->add_action("variable,name=hold_cooldowns,"
                      "op=setif,"
                      "value=1,"
                      "value_else=0,"
                      "condition=cooldown.X.remains<fight_remains*0.9");

# Reference the variable in other conditions
some_action->add_action("cooldown_ability,if=!variable.hold_cooldowns");
```

Variables defined in `precombat` persist into combat. Variables updated in a `variables`
sublist (called first in default) refresh each GCD.

---

## 7. Call Action List

APLs branch into sublists for readability and conditional routing:

```
# Execute: run the sublist, then continue here when it returns
call_action_list,name=SUBLIST[,if=EXPR]

# Execute: run the sublist and stop — don't return to default list
run_action_list,name=SUBLIST[,if=EXPR]
```

`call_action_list` returns control to the calling list after the sublist is exhausted.
`run_action_list` does **not** return — it consumes the GCD completely.

Typical structure:
```
default:
  call_action_list,name=variables      # always recalculate vars
  call_action_list,name=ogcd           # check off-GCD abilities
  call_action_list,name=cooldowns      # major cooldowns
  call_action_list,name=aoe,if=active_enemies>=3
  call_action_list,name=st             # single target rotation
  shadow_bolt                          # filler if nothing else fires
```

---

## 8. Building APLs in C++

### Core pattern

In the APL `.cpp` file:

```cpp
void affliction( player_t* p )
{
  // 1. Get (or create) named action priority lists
  action_priority_list_t* default_  = p->get_action_priority_list( "default" );
  action_priority_list_t* precombat = p->get_action_priority_list( "precombat" );
  action_priority_list_t* ogcd      = p->get_action_priority_list( "ogcd" );
  action_priority_list_t* variables = p->get_action_priority_list( "variables" );

  // 2. Populate precombat list
  precombat->add_action( "snapshot_stats" );
  precombat->add_action( "summon_pet" );
  precombat->add_action( "haunt,if=active_enemies<2" );

  // 3. Populate default (combat) list
  default_->add_action( "call_action_list,name=variables" );
  default_->add_action( "call_action_list,name=ogcd" );
  default_->add_action( "agony,if=!ticking|refreshable" );
  default_->add_action( "corruption,if=!ticking|refreshable" );
  default_->add_action( "shadow_bolt" );

  // 4. Populate off-GCD list
  ogcd->add_action( "potion,if=fight_remains<30" );
  ogcd->add_action( "berserking,if=buff.bloodlust.down" );
}
```

### add_action signature

```cpp
// No comment
list->add_action( "action_name,modifier=value" );

// With comment (shown in HTML report output)
list->add_action( "action_name,if=...", "This is why we do this" );

// Talent-gated: only adds action if the talent is taken
// (handled via if=talent.NAME in the condition, not a special method)
list->add_action( "drain_soul,if=talent.drain_soul" );
```

### Helper functions

```cpp
// potion/flask/food/rune helpers at top of file return level-appropriate item names
std::string potion( const player_t* p )
{
  if ( p->true_level >= 90 ) return "lights_potential_2";
  return ( p->true_level >= 80 ) ? "tempered_potion_3" : "disabled";
}

// Use in APL:
precombat->add_action( "potion" );  // resolved at runtime via p->potion()
```

### Calling the APL function

In the class module (e.g. `sc_warlock.cpp`):
```cpp
void warlock_t::init_action_list()
{
  // ...
  switch ( specialization() )
  {
    case WARLOCK_AFFLICTION:  warlock_apl::affliction( this ); break;
    case WARLOCK_DEMONOLOGY:  warlock_apl::demonology( this ); break;
    case WARLOCK_DESTRUCTION: warlock_apl::destruction( this ); break;
    default: break;
  }
}
```

### Exporting to .simc format

After a sim run with `save=profile.simc`, SimC outputs the APL in .simc format.
The C++ APL is also auto-exported into profile files with the marker:
```
//affliction_apl_start
...
//affliction_apl_end
```
These markers are used to regenerate `profiles/MID1/` from the C++ source.

---

## 9. Walkthrough: Affliction Warlock APL

This walks through `engine/class_modules/apl/warlock.cpp` for Affliction.

### Step 1 — Setup

```cpp
action_priority_list_t* default_      = p->get_action_priority_list( "default" );
action_priority_list_t* precombat     = p->get_action_priority_list( "precombat" );
action_priority_list_t* end_of_fight  = p->get_action_priority_list( "end_of_fight" );
action_priority_list_t* items         = p->get_action_priority_list( "items" );
action_priority_list_t* ogcd          = p->get_action_priority_list( "ogcd" );
action_priority_list_t* variables     = p->get_action_priority_list( "variables" );
action_priority_list_t* soul_harvester= p->get_action_priority_list( "soul_harvester" );
action_priority_list_t* hellcaller    = p->get_action_priority_list( "hellcaller" );
// ... SH_st, SH_cleave, SH_aoe, HC_st, HC_cleave, HC_aoe ...
```

Thirteen named sublists for the two hero tree paths × three target-count scenarios.

### Step 2 — Precombat

```cpp
precombat->add_action( "summon_pet" );
precombat->add_action( "grimoire_of_sacrifice,if=talent.grimoire_of_sacrifice.enabled" );
precombat->add_action( "snapshot_stats" );
precombat->add_action( "seed_of_corruption,if=(hero_tree.soul_harvester&active_enemies>1)|active_enemies>2" );
precombat->add_action( "haunt,if=active_enemies<2|(hero_tree.hellcaller&active_enemies<3)" );
```

- Summon pet before combat
- Optionally sacrifice pet (Grimoire of Sacrifice talent)
- `snapshot_stats` locks raid buff state for the simulation
- Pre-apply Seed of Corruption in AoE scenarios
- Pre-cast Haunt for single target (starts with Haunt debuff on pull)

### Step 3 — Default list routing

```cpp
default_->add_action( "call_action_list,name=variables" );   // recalc all vars
default_->add_action( "call_action_list,name=end_of_fight" ); // execute phase
default_->add_action( "call_action_list,name=ogcd" );         // off-GCD abilities
default_->add_action( "call_action_list,name=items" );         // trinkets
default_->add_action( "call_action_list,name=soul_harvester,if=hero_tree.soul_harvester" );
default_->add_action( "call_action_list,name=hellcaller,if=hero_tree.hellcaller" );
// Fallback filler actions if no sublist action fired:
default_->add_action( "malefic_grasp,chain=1,early_chain_if=buff.nightfall.react,if=pet.darkglare.active" );
default_->add_action( "drain_soul,chain=1,early_chain_if=buff.nightfall.react,interrupt_if=tick_time>0.5" );
default_->add_action( "shadow_bolt" );  // ultimate filler
```

### Step 4 — Hero tree dispatch

```cpp
soul_harvester->add_action( "call_action_list,name=SH_st,if=active_enemies=1" );
soul_harvester->add_action( "call_action_list,name=SH_cleave,if=active_enemies=2" );
soul_harvester->add_action( "call_action_list,name=SH_aoe,if=active_enemies>2" );

hellcaller->add_action( "call_action_list,name=HC_st,if=active_enemies=1" );
hellcaller->add_action( "call_action_list,name=HC_cleave,if=active_enemies=2" );
hellcaller->add_action( "call_action_list,name=HC_aoe,if=active_enemies>2" );
```

Each hero tree routes to ST/Cleave/AoE variants of its rotation.

### Step 5 — Single target rotation (Soul Harvester)

```cpp
SH_st->add_action( "haunt,if=buff.nightfall.react<2" );
SH_st->add_action( "agony,if=!ticking|refreshable" );
SH_st->add_action( "corruption,if=!ticking|refreshable" );
SH_st->add_action( "summon_darkglare,if=soul_shard<3|cooldown.dark_harvest.remains" );
SH_st->add_action( "dark_harvest,if=soul_shard<3&execute_time<(dot.agony.remains<?dot.corruption.remains)&buff.cascading_calamity.remains" );
SH_st->add_action( "drain_soul,if=buff.nightfall.react>1" );
SH_st->add_action( "agony,...(refresh conditions)" );
SH_st->add_action( "unstable_affliction,...(maintain UA stacks)" );
// ... more actions ...
SH_st->add_action( "drain_life,if=talent.gorefiends_avarice&soul_shard<5" );
SH_st->add_action( "drain_soul" );  // filler channel
```

**Reading the logic:**
1. Keep Haunt up (unless proc stacks are building)
2. Always keep DoTs ticking (agony, corruption) — refresh within pandemic window
3. Use Summon Darkglare on cooldown when resources aren't too high
4. Dark Harvest as a burst window extender
5. Consume Nightfall procs with Drain Soul
6. Maintain Unstable Affliction stacks
7. Drain Life filler with Gorefiend's Avarice talented (halved channel)
8. Drain Soul as universal filler

---

## 10. Common Patterns

### Trinket Usage Pattern

```cpp
// In precombat variables:
precombat->add_action( "variable,name=trinket_1_buffs,value=trinket.1.has_use_buff" );
precombat->add_action( "variable,name=trinket_2_buffs,value=trinket.2.has_use_buff" );

// In items sublist:
items->add_action(
  "use_item,slot=trinket1,if=variable.trinket_1_buffs&"
  "(buff.MAJOR_COOLDOWN.up|cooldown.MAJOR_COOLDOWN.remains>20)"
);
items->add_action( "use_item,slot=trinket2,if=variable.trinket_2_buffs&..." );
// Fallback: use if nothing else is happening
items->add_action( "use_item,slot=trinket1" );
items->add_action( "use_item,slot=trinket2" );
```

### Cooldown Pooling

```cpp
// Hold cooldown if fight ends before you could use it twice:
action->add_action(
  "major_cooldown,if=fight_remains>cooldown.major_cooldown.duration*0.75"
);

// Sync cooldown to another cooldown:
action->add_action(
  "secondary_cd,if=cooldown.primary_cd.remains<5|cooldown.primary_cd.up"
);
```

### AoE / ST Switching

```cpp
// Pattern 1: Enemy count routing
default_->add_action( "call_action_list,name=aoe,if=active_enemies>=3" );
default_->add_action( "call_action_list,name=st,if=active_enemies<3" );

// Pattern 2: Inline AoE conditions on individual actions
list->add_action( "whirlwind,if=active_enemies>=3" );
list->add_action( "mortal_strike,if=active_enemies<3" );
```

### Channel Interruption

```cpp
// Interrupt a channel if something better procs
list->add_action(
  "drain_soul,"
  "chain=1,"
  "early_chain_if=buff.nightfall.react,"  // break into new cast on proc
  "interrupt_if=tick_time>0.5"            // safety: don't interrupt in mid-tick
);
```

### Execute Phase

```cpp
action_priority_list_t* eof = p->get_action_priority_list( "end_of_fight" );
eof->add_action( "pool_resource,for_next=1" );
eof->add_action( "some_expensive_spell,if=fight_remains<cast_time+1" );
// Call first in default:
default_->add_action( "call_action_list,name=end_of_fight,if=fight_remains<5" );
```

### Racial Actions

```cpp
// Get all available racial abilities for the character
std::vector<std::string> racial_actions = p->get_racial_actions();

// Add them to the off-GCD list
for ( const auto& ra : racial_actions )
  ogcd->add_action( ra + ",if=..." );
```

---

## 11. Testing APL Changes

### Command-line syntax

```bash
# Run a specific profile with custom APL
engine/simc profiles/MID1/MID1_Warlock_Affliction_Hellcaller.simc \
  iterations=100 \
  output=result.txt

# Override a single action in the APL (appends to default list):
engine/simc <profile> \
  "actions+=/shadowbolt,if=..." \
  iterations=10

# Completely replace the APL with an inline one:
engine/simc warlock= spec=affliction level=90 \
  load_default_gear=1 load_default_talents=1 \
  "actions=agony" \
  "actions+=/corruption" \
  "actions+=/shadow_bolt" \
  iterations=1

# Run all MID1 profiles (1 iteration each for smoke test)
for f in profiles/MID1/*.simc; do
  echo -n "$(basename $f): "
  engine/simc "$f" iterations=1 output=/dev/null html=/dev/null json=/dev/null \
    cleanup_threads=1 2>&1 | grep -oE 'DPS: [0-9.]+' | head -1
done
```

### Comparing two APLs

```bash
# Baseline
engine/simc <profile> iterations=1000 output=baseline.txt

# Modified profile
engine/simc <profile_modified> iterations=1000 output=modified.txt

# Diff DPS
grep "DPS" baseline.txt modified.txt
```

### Quick CI-style validation (1 iteration, all profiles)

```bash
PASS=0; FAIL=0
for f in profiles/MID1/*.simc; do
  name=$(basename "$f" .simc)
  if engine/simc "$f" iterations=1 output=/dev/null html=/dev/null \
     json=/dev/null cleanup_threads=1 >/dev/null 2>&1; then
    PASS=$((PASS+1)); echo "PASS: $name"
  else
    FAIL=$((FAIL+1)); echo "FAIL: $name"
  fi
done
echo "Results: $PASS PASS / $FAIL FAIL"
```

### In-sim APL debugging

```bash
# Log every action decision
engine/simc <profile> iterations=1 debug=1 output=debug.txt

# Print APL to stdout before sim
engine/simc <profile> iterations=0 print_styles=1
```

---

## 12. Midnight-Specific APL Notes

### New condition types

**Hero tree routing** (new in Midnight):
```
hero_tree.HERO_TREE_NAME    # e.g. hero_tree.soul_harvester, hero_tree.hellcaller
```

**4-rank talent rank checks**:
```
talent.TALENT_NAME.rank>=2  # check if talent rank 2+ is taken
talent.phalanx.rank=4       # specifically rank 4 (capstone)
```

**Dark Pact (all Warlocks)**:
```
# Defensive; use when below 50% health
dark_pact,if=health.pct<50&buff.dark_pact.down,use_off_gcd=1
```

### Consumables for Midnight (level 90)

```
potion:             lights_potential_2
flask:              flask_of_the_magisters_2
food:               blooming_feast
augmentation:       void_touched
temporary_enchant:  main_hand:thalassian_phoenix_oil_2
```

### Gorefiend's Avarice (Warlock class talent)

This talent halves Drain Life's channel duration (Rank 1: tick_time * 0.5). APLs should
prioritize Drain Life more aggressively when this talent is active:

```
drain_life,if=talent.gorefiends_avarice&soul_shard<5
```

Currently a TODO — APLs treat Drain Life as standard filler regardless of this talent.

### Known APL limitations (2026-03-17)

| Spec | Issue |
|------|-------|
| Warlock (all) | drain_life priority not adjusted for gorefiends_avarice |
| Balance Druid | Simplified APL — no valid talent hash, lower DPS than optimal |
| Aug Evoker | Simplified APL — simplified talent set |
| Assassination Rogue | Simplified APL — base rotation only |

---

## Appendix: Quick Reference Card

```
# Boolean operators
&   AND
|   OR
!   NOT
()  grouping

# Arithmetic
+  -  *  /  <? (min of) >? (max of)

# Comparison
=  !=  <  >  <=  >=

# Common shortcuts
!dot.X.ticking               = dot is NOT active
!ticking|refreshable         = apply/reapply DoT idiom
soul_shard<3                 = resource below threshold
fight_remains<cooldown.X.duration  = don't use if can't use twice
buff.X.react                 = stacks available (proc-based buff)
cooldown.X.ready             = off cooldown

# Named list calls
call_action_list,name=X      = branch to X, then return
run_action_list,name=X       = branch to X, don't return

# Variables
variable,name=X,op=set,value=Y       = X = Y
variable,name=X,op=setif,value=Y,value_else=Z,condition=C = X = C?Y:Z
```

---

*Generated for the SimulationCraft Midnight (12.0.1) fork.*
*See `engine/class_modules/apl/` for all class APL implementations.*

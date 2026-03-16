# Task Dossier: Warlock Class Tree + Misc Talent Mechanics Implementation

## Task Metadata

- **Issue/Row Reference:** Warlock rows 201-203, Rogue row 196, Evoker rows 175-176
- **Task Type:** Gameplay Mechanics — talent effect wiring
- **Target Files:**
  - `engine/class_modules/warlock/sc_warlock_actions.cpp` (primary)
  - `engine/class_modules/warlock/sc_warlock.cpp` (composite_leech)
  - `engine/class_modules/warlock/sc_warlock.hpp` (declarations)
  - `engine/class_modules/sc_rogue.cpp` (improved_find_weakness)
  - `engine/class_modules/sc_evoker.cpp` (walloping_blow)
- **Status:** Declarations registered → Mechanics NYI
- **Wowhead Build Date:** 2026-03-16
- **Preceded By:** commit 099b0aa (talent registration)
- **Dossier Version:** 1.0 — 2026-03-16

---

## Background

Commit 099b0aa registered all 31 Warlock class tree talents, 2 Shaman talents, 6 Evoker talents,
and 1 Rogue talent as `player_talent_t` declarations with `find_talent_spell()` init calls.
However, the talent values are not yet wired into any gameplay calculation.
This dossier covers the DPS-relevant talents that require mechanical implementation.

---

## Spell Data Summary (Wowhead, 2026-03-16)

### Warlock

| Spell ID | Name | Effect | DPS Impact |
|----------|------|--------|------------|
| 1270701 | Gorefiend's Avarice | Drain Life channels 100% faster (tick_time * 0.5) and restores health 100% faster | HIGH — halves Drain Life channel duration, doubles tick frequency |
| 1271689 | Empowered Drain Life | Increases Drain Life damage coefficient | HIGH — direct damage multiplier on tick |
| 1265810 | Infernal Beneficiary | Drain Life heals primary demon at 400% effectiveness | LOW — pet healing, not direct DPS |
| 1270690 | Pact of the Nathrezim | +2% Leech | LOW — passive leech grant |
| 108416  | Dark Pact | Sacrifice 20% current HP → 200% absorb shield for 20s, 1min CD | MEDIUM — defensive, affects survivability/rotation |
| 385881  | Teachings of the Black Harvest | Modifies pet abilities per spec: Imp singe magic → 4% dmg reduction; Felhunter spell lock enhanced | LOW — utility/pet |
| 389367  | Fel Synergy | Soul Leech heals self 8% + pet 25% of absorb granted | LOW — healing utility |
| 1270255 | Oppressive Darkness | Shadowfury CD -15s, radius +2 yds | UTILITY — CC cooldown |
| 386689  | Pact of Gluttony | Healthstone multiple-use | UTILITY |

Source URLs:
- https://www.wowhead.com/beta/spell=1270701 (Gorefiend's Avarice)
- https://www.wowhead.com/beta/spell=1271689 (Empowered Drain Life)
- https://www.wowhead.com/beta/spell=1270690 (Pact of Nathrezim)
- https://www.wowhead.com/beta/spell=108416 (Dark Pact)
- https://www.wowhead.com/beta/spell=1265810 (Infernal Beneficiary)

### Rogue Subtlety

| Spell ID | Name | Effect | DPS Impact |
|----------|------|--------|------------|
| 382512 | Improved Find Weakness | Amplifies Find Weakness armor pen % beyond baseline | HIGH — increases armor ignore during Find Weakness uptime |

Source: https://www.wowhead.com/beta/spell=382512

### Evoker

| Spell ID | Name | Effect | DPS Impact |
|----------|------|--------|------------|
| 387341 | Walloping Blow | Adds bonus damage to melee hit (% or flat) | MEDIUM — melee modifier |
| 431715 | Nozdormu Adept | Prescience CD -2s, +1% crit chance (Devast+Aug) | MEDIUM — Prescience uptime + crit |

Source: https://www.wowhead.com/beta/spell=387341, https://www.wowhead.com/beta/spell=431715

---

## Code Patterns (from codebase research, 2026-03-16)

### Pattern A — Channel tick speed modifier (drain_life_t)

Reference: `sc_warlock_actions.cpp` lines 2052–2119 (`drain_soul_state_t`)

```cpp
// 1. Add a custom action_state_t struct before drain_life_t
struct drain_life_state_t : public action_state_t
{
  double tick_time_multiplier;

  drain_life_state_t( action_t* action, player_t* target )
    : action_state_t( action, target ), tick_time_multiplier( 1.0 ) {}

  void initialize() override
  {
    action_state_t::initialize();
    tick_time_multiplier = 1.0;
  }

  void copy_state( const action_state_t* s ) override
  {
    action_state_t::copy_state( s );
    tick_time_multiplier = debug_cast<const drain_life_state_t*>( s )->tick_time_multiplier;
  }
};

// 2. Inside drain_life_t, override:
action_state_t* new_state() override
{ return new drain_life_state_t( this, target ); }

void snapshot_state( action_state_t* s, result_amount_type rt ) override
{
  auto* dl = debug_cast<drain_life_state_t*>( s );
  dl->tick_time_multiplier = 1.0;
  if ( p()->talents.gorefiends_avarice.ok() )
    dl->tick_time_multiplier *= 0.5;  // "100% faster" = 0.5x tick time
  warlock_spell_t::snapshot_state( s, rt );
}

double tick_time_pct_multiplier( const action_state_t* s ) const override
{
  auto m = warlock_spell_t::tick_time_pct_multiplier( s );
  m *= debug_cast<const drain_life_state_t*>( s )->tick_time_multiplier;
  return m;
}
```

NOTE: "100% faster channel" in WoW typically means 2x tick rate = tick_time * 0.5.
Confirm with effectN(1) from spell data at runtime.

### Pattern B — Damage coefficient multiplier on drain_life_t (Empowered Drain Life)

Reference: `sc_warlock_actions.cpp` line 2180 (`drain_soul_t::composite_ta_multiplier`)

```cpp
// Inside drain_life_t:
double composite_ta_multiplier( const action_state_t* s ) const override
{
  double m = warlock_spell_t::composite_ta_multiplier( s );
  if ( p()->talents.empowered_drain_life.ok() )
    m *= 1.0 + p()->talents.empowered_drain_life->effectN( 1 ).percent();
  return m;
}
```

Alternative: use `parse_effects( talents.empowered_drain_life )` in
`warlock_t::apply_affecting_auras()` in `sc_warlock.cpp` (lines ~917–993) if
the spell data has a proper game-side link to Drain Life's damage effect.

### Pattern C — Leech passive (Pact of the Nathrezim)

Reference: `sc_hunter.cpp` lines 8589–8596 (predators_thirst)

```cpp
// In sc_warlock.cpp, add to warlock_t class methods:
double warlock_t::composite_leech() const
{
  double l = player_t::composite_leech();
  if ( talents.pact_of_the_nathrezim.ok() )
    l += talents.pact_of_the_nathrezim->effectN( 1 ).percent();  // +2% leech
  return l;
}
// Also add CACHE_LEECH invalidation via buff or invalidate() in init_rng or init.
```

Declare in `sc_warlock.hpp`:
```cpp
double composite_leech() const override;
```

### Pattern D — Absorb shield with HP sacrifice (Dark Pact)

Reference: `sc_warrior.cpp` lines 2349–2426 (ignore_pain), `sc_death_knight.cpp` lines 6201–6247

```cpp
// In sc_warlock_actions.cpp:
struct dark_pact_t : public warlock_spell_t
{
  propagate_const<absorb_buff_t*> shield;

  dark_pact_t( warlock_t* p, util::string_view options_str )
    : warlock_spell_t( "dark_pact", p, p->talents.dark_pact, options_str ),
      shield( nullptr )
  {
    harmful   = false;
    may_miss  = false;
    target    = p;
    use_off_gcd = true;  // Dark Pact is 0 GCD
  }

  void init_finished() override
  {
    warlock_spell_t::init_finished();
    shield = make_buff<absorb_buff_t>( p(), "dark_pact_shield",
               p()->find_spell( 108416 ) )
               ->set_absorb_source( p()->get_stats( "dark_pact" ) );
  }

  void execute() override
  {
    warlock_spell_t::execute();
    // Sacrifice 20% of current HP (effectN(1) should be 0.20)
    double hp_cost = p()->resources.current[ RESOURCE_HEALTH ]
                     * p()->talents.dark_pact->effectN( 1 ).percent();
    p()->resource_loss( RESOURCE_HEALTH, hp_cost, nullptr, this );
    // Grant absorb = 200% of sacrificed HP (effectN(2) should be 2.00)
    double absorb_amount = hp_cost * p()->talents.dark_pact->effectN( 2 ).percent();
    shield->trigger( 1, absorb_amount );
  }
};
```

Register in `create_action()` in `sc_warlock.cpp`:
```cpp
if ( name == "dark_pact" ) return new actions::dark_pact_t( this, options_str );
```

### Pattern E — Armor penetration amplifier (Improved Find Weakness)

Reference: `sc_rogue.cpp` lines 8787–8794 (`composite_player_target_armor`)

Current implementation:
```cpp
double rogue_t::composite_player_target_armor( player_t* target ) const
{
  double a = player_t::composite_player_target_armor( target );
  a *= 1.0 - buffs.find_weakness->value();
  return a;
}
```

Modified to include improved_find_weakness:
```cpp
double rogue_t::composite_player_target_armor( player_t* target ) const
{
  double a = player_t::composite_player_target_armor( target );
  if ( buffs.find_weakness->check() )
  {
    double pen = buffs.find_weakness->value();
    if ( talent.subtlety.improved_find_weakness.ok() )
      pen += talent.subtlety.improved_find_weakness->effectN( 1 ).percent();
    a *= 1.0 - pen;
  }
  return a;
}
```

NOTE: Verify `effectN(1)` is the right effect index for the additional armor pen %.
Could also be implemented as a buff value modifier on find_weakness buff creation.

### Pattern F — Melee hit % modifier (Walloping Blow)

Reference: Generic `composite_da_multiplier()` pattern in sc_evoker.cpp

The `walloping_blow` spell data effectN(1) needs to be checked at runtime.
It's likely a % bonus to melee physical hits (tail swipe / wing buffet type spells).

```cpp
// In the relevant evoker melee action(s), add to composite_da_multiplier:
double composite_da_multiplier( const action_state_t* s ) const override
{
  double m = base_t::composite_da_multiplier( s );
  if ( p()->talent.walloping_blow.ok() )
    m *= 1.0 + p()->talent.walloping_blow->effectN( 1 ).percent();
  return m;
}
```

Apply to: `tail_swipe_t`, `wing_buffet_t`, or whichever melee actions exist.
Check which actions are tagged in the spell's "Affected Spells" list on Wowhead.

### Pattern G — Prescience CD + crit (Nozdormu Adept)

Nozdormu Adept: Prescience CD -2s, +1% crit. These are passive modifiers.
Use `parse_effects` system or explicit override:

```cpp
// In apply_affecting_auras() in sc_evoker.cpp, add:
// parse_effects( talent.nozdormu_adept );
// If parse_effects handles A_HASTE_COOLDOWNS and A_MOD_ALL_CRIT_CHANCE types.

// OR manual:
// In prescience_t::cooldown setup:
if ( p()->talent.nozdormu_adept.ok() )
  cooldown->duration -= p()->talent.nozdormu_adept->effectN( 1 ).time_value(); // -2s

// In warlock_t::composite_spell_crit_chance():
// (add to evoker_t::composite_spell_crit_chance if that exists)
double composite_spell_crit_chance() const override
{
  double c = base_t::composite_spell_crit_chance();
  if ( talent.nozdormu_adept.ok() )
    c += talent.nozdormu_adept->effectN( 2 ).percent(); // +1%
  return c;
}
```

---

## Implementation Priority and Plan

### Priority 1 — High DPS Impact

**Task 1: Gorefiend's Avarice — Drain Life channel speed**
- File: `engine/class_modules/warlock/sc_warlock_actions.cpp`
- Add `drain_life_state_t` struct above `drain_life_t`
- Override `new_state()`, `snapshot_state()`, `tick_time_pct_multiplier()` in `drain_life_t`
- The 100% faster multiplier should come from `talents.gorefiends_avarice->effectN(1)` or be hardcoded to `0.5x` if effectN is a flat flag
- Verify with build + sanity check that tick rate changes

**Task 2: Empowered Drain Life — Drain Life damage multiplier**
- File: `engine/class_modules/warlock/sc_warlock_actions.cpp`
- Add `composite_ta_multiplier()` override in `drain_life_t`
- Gate on `p()->talents.empowered_drain_life.ok()`
- Use `effectN(1).percent()` for the coefficient

**Task 3: Improved Find Weakness — Armor pen amplifier**
- File: `engine/class_modules/sc_rogue.cpp`
- Modify `rogue_t::composite_player_target_armor()` (around line 8787)
- Change `a *= 1.0 - buffs.find_weakness->value()` to check talent and add extra pen

### Priority 2 — Medium DPS Impact

**Task 4: Dark Pact — HP sacrifice absorb action**
- Files: `sc_warlock_actions.cpp` (action struct), `sc_warlock.cpp` (create_action registration)
- Create `dark_pact_t` struct using absorb_buff_t pattern
- Register in `create_action()`

**Task 5: Nozdormu Adept — Prescience CD + crit**
- File: `engine/class_modules/sc_evoker.cpp`
- Find prescience_t cooldown setup, apply CD reduction
- Override or extend `composite_spell_crit_chance()` in evoker_t

**Task 6: Walloping Blow — Melee damage modifier**
- File: `engine/class_modules/sc_evoker.cpp`
- Identify affected melee actions via Wowhead "Affected Spells"
- Add `composite_da_multiplier()` override

### Priority 3 — Low/Utility

**Task 7: Pact of the Nathrezim — +2% Leech**
- File: `sc_warlock.cpp` + `sc_warlock.hpp`
- Add `composite_leech()` override to `warlock_t`

**Task 8: Infernal Beneficiary — Drain Life heals pet**
- File: `sc_warlock_actions.cpp`
- In `drain_life_t::tick()`, trigger pet heal at 400% of heal amount
- Requires access to `p()->pets.active_pet()` or similar

---

## Verification Checklist

- [ ] Spell data effectN indices confirmed at runtime (log a sim run, inspect values)
- [ ] Drain Life tick rate doubles with Gorefiend's Avarice active
- [ ] Drain Life damage increases with Empowered Drain Life active
- [ ] Dark Pact action available in APL, triggers HP loss + absorb buff
- [ ] Find Weakness armor pen % higher with Improved Find Weakness talented
- [ ] Prescience cooldown 2s shorter with Nozdormu Adept
- [ ] Build compiles clean (no new errors or warnings from changes)
- [ ] No zero-DPS or crash scenarios introduced

---

## Code Patterns Reference Quick-Index

| Need | Pattern Location | Key Method |
|------|-----------------|------------|
| Channel tick speed | `sc_warlock_actions.cpp` L2052–2119 | `tick_time_pct_multiplier()` via snapshotted state |
| Channel damage multiplier | `sc_warlock_actions.cpp` L2180 | `composite_ta_multiplier()` |
| Leech passive | `sc_hunter.cpp` L8589–8596 | `composite_leech()` override |
| Absorb + HP sacrifice | `sc_warrior.cpp` L2349–2426 | `absorb_buff_t` + `resource_loss(RESOURCE_HEALTH)` |
| Armor pen amplifier | `sc_rogue.cpp` L8787–8794 | `composite_player_target_armor()` |
| Melee % modifier | generic evoker pattern | `composite_da_multiplier()` |
| CD reduction passive | prescience_t cooldown | `cooldown->duration -= effectN(N).time_value()` |
| Crit % passive | evoker_t composite | `composite_spell_crit_chance()` |

---

## Post-Implementation

**Commit message (draft):**
`[Midnight] Wire Warlock class tree mechanics — Drain Life speed/dmg, Dark Pact, Leech; Rogue IFW armor pen; Evoker Nozdormu Adept/Walloping Blow`

**Rows to update in project_progress.md after completion:**
- Warlock Affliction/Demonology/Destruction: talent rows → Implemented
- Rogue Subtlety: talent row → Implemented
- Evoker Devastation/Augmentation: talent row → Implemented

---

*Dossier version: 1.0 — 2026-03-16*

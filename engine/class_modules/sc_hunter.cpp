//==========================================================================
// Dedmonwakeen's DPS-DPM Simulator.
// Send questions to natehieter@gmail.com
// ==========================================================================

#include <memory>
#include <optional>

#include "simulationcraft.hpp"
#include "player/pet_spawner.hpp"
#include "class_modules/apl/apl_hunter.hpp"

namespace
{ // UNNAMED NAMESPACE

// helper smartpointer-like struct for spell data pointers
struct spell_data_ptr_t
{
  spell_data_ptr_t():
    data_( spell_data_t::not_found() ) {}

  spell_data_ptr_t( const spell_data_t* s ):
    data_( s ? s : spell_data_t::not_found() ) {}

  spell_data_ptr_t& operator=( const spell_data_t* s )
  {
    data_ = s ? s : spell_data_t::not_found();
    return *this;
  }

  const spell_data_t* operator->() const { return data_; }

  operator const spell_data_t*() const { return data_; }

  bool ok() const { return data_ -> ok(); }

  const spell_data_t* data_;
};

static void print_affected_by( const action_t* a, const spelleffect_data_t& effect, util::string_view label = {} )
{
  fmt::memory_buffer out;
  const spell_data_t& spell = *effect.spell();
  const auto& spell_text = a->player->dbc->spell_text( spell.id() );

  fmt::format_to( std::back_inserter(out), "{} {} is affected by {}", *a->player, *a, spell.name_cstr() );
  if ( spell_text.rank() )
    fmt::format_to( std::back_inserter(out), " (desc={})", spell_text.rank() );
  fmt::format_to( std::back_inserter(out), " (id={}) effect#{}", spell.id(), effect.spell_effect_num() + 1 );
  if ( !label.empty() )
    fmt::format_to( std::back_inserter(out), ": {}", label );

  a -> sim -> print_debug( "{}", util::string_view( out.data(), out.size() ) );
}

static bool check_affected_by( action_t* a, const spelleffect_data_t& effect )
{
  bool affected = a->data().affected_by( effect ) || a->data().affected_by_label( effect );
  if ( affected && a->sim->debug )
    print_affected_by( a, effect );
  return affected;
}

struct damage_affected_by {
  uint8_t direct = 0;
  uint8_t tick = 0;
};

static damage_affected_by parse_damage_affecting_aura( action_t* a, spell_data_ptr_t spell )
{
  damage_affected_by affected_by;
  for ( const spelleffect_data_t& effect : spell -> effects() )
  {
    if ( effect.type() != E_APPLY_AURA )
      continue;

    if ( ( effect.subtype() == A_MOD_DAMAGE_FROM_CASTER_SPELLS && a->data().affected_by( effect ) ) ||
         ( effect.subtype() == A_MOD_DAMAGE_FROM_CASTER_SPELLS_LABEL && a->data().affected_by_label( effect ) ) )
    {
      affected_by.direct = as<uint8_t>( effect.spell_effect_num() + 1 );
      affected_by.tick   = as<uint8_t>( effect.spell_effect_num() + 1 );
      print_affected_by( a, effect, "spell damage taken increase" );

      return affected_by;
    }

    if ( ( effect.subtype() == A_ADD_PCT_MODIFIER && a->data().affected_by( effect ) ) ||
         ( effect.subtype() == A_ADD_PCT_LABEL_MODIFIER && a->data().affected_by_label( effect ) ) )
    {
      if ( effect.misc_value1() == P_GENERIC )
      {
        affected_by.direct = as<uint8_t>( effect.spell_effect_num() + 1 );
        print_affected_by( a, effect, "direct damage increase" );
      }
      else if ( effect.misc_value1() == P_TICK_DAMAGE )
      {
        affected_by.tick = as<uint8_t>( effect.spell_effect_num() + 1 );
        print_affected_by( a, effect, "tick damage increase" );
      }
    }
  }
  return affected_by;
}

namespace cdwaste {

struct action_data_t
{
  simple_sample_data_with_min_max_t exec;
  simple_sample_data_with_min_max_t cumulative;
  timespan_t iter_sum;

  void update_ready( const action_t* action, timespan_t cd )
  {
    const cooldown_t* cooldown = action -> cooldown;
    sim_t* sim = action -> sim;
    if ( ( cd > 0_ms || ( cd <= 0_ms && cooldown -> duration > 0_ms ) ) &&
         cooldown -> current_charge == cooldown -> charges && cooldown -> last_charged > 0_ms &&
         cooldown -> last_charged < sim -> current_time() )
    {
      timespan_t time_ = sim -> current_time() - cooldown -> last_charged;
      if ( sim -> debug )
      {
        sim -> out_debug.print( "{} {} cooldown waste tracking waste={} exec_time={}",
                                action -> player -> name(), action -> name(),
                                time_, action -> time_to_execute );
      }
      time_ -= action -> time_to_execute;

      if ( time_ > 0_ms )
      {
        exec.add( time_.total_seconds() );
        iter_sum += time_;
      }
    }
  }
};

struct player_data_t
{
  using record_t = std::pair<std::string, std::unique_ptr<action_data_t>>;
  std::vector<record_t> data_;

  action_data_t* get( const action_t* a )
  {
    auto it = range::find( data_, a -> name_str, &record_t::first );
    if ( it != data_.cend() )
      return it -> second.get();

    data_.emplace_back( a -> name_str, std::make_unique<action_data_t>( ) );
    return data_.back().second.get();
  }

  void merge( const player_data_t& other )
  {
    for ( size_t i = 0, end = data_.size(); i < end; i++ )
    {
      data_[ i ].second -> exec.merge( other.data_[ i ].second -> exec );
      data_[ i ].second -> cumulative.merge( other.data_[ i ].second -> cumulative );
    }
  }

  void datacollection_begin()
  {
    for ( auto& rec : data_ )
      rec.second -> iter_sum = 0_ms;
  }

  void datacollection_end()
  {
    for ( auto& rec : data_ )
      rec.second -> cumulative.add( rec.second -> iter_sum.total_seconds() );
  }
};

void print_html_report( const player_t& player, const player_data_t& data, report::sc_html_stream& os )
{
  if ( data.data_.empty() )
    return;

  os << "<h3 class='toggle open'>Cooldown waste details</h3>\n"
     << "<div class='toggle-content'>\n";

  os << "<table class='sc' style='float: left;margin-right: 10px;'>\n"
     << "<tr>"
     << "<th></th>"
     << "<th colspan='3'>Seconds per Execute</th>"
     << "<th colspan='3'>Seconds per Iteration</th>"
     << "</tr>\n"
     << "<tr>"
     << "<th>Ability</th>"
     << "<th>Average</th><th>Minimum</th><th>Maximum</th>"
     << "<th>Average</th><th>Minimum</th><th>Maximum</th>"
     << "</tr>\n";

  size_t n = 0;
  for ( const auto& rec : data.data_ )
  {
    const auto& entry = rec.second -> exec;
    if ( entry.count() == 0 )
      continue;

    const auto& iter_entry = rec.second -> cumulative;
    const action_t* a = player.find_action( rec.first );

    ++n;
    fmt::print( os,
      "<tr{}>"
      "<td class='left'>{}</td>"
      "<td class='right'>{:.3f}</td><td class='right'>{:.3f}</td><td class='right'>{:.3f}</td>"
      "<td class='right'>{:.3f}</td><td class='right'>{:.3f}</td><td class='right'>{:.3f}</td>"
      "</tr>\n",
      n & 1 ? " class='odd'" : "",
      a ? report_decorators::decorated_action( *a ) : util::encode_html( rec.first ),
      entry.mean(), entry.min(), entry.max(),
      iter_entry.mean(), iter_entry.min(), iter_entry.max()
    );
  }

  os << "</table>\n"
     << "</div>\n"
     << "<div class='clear'></div>\n";
}

} // end namespace cd_waste

// ==========================================================================
// Hunter
// ==========================================================================

enum howl_of_the_pack_leader_beast
{
  WYVERN,
  BOAR,
  BEAR
};

struct maybe_bool {

  enum class value_e : uint8_t {
    None, True, False
  };

  constexpr maybe_bool() = default;

  constexpr maybe_bool& operator=( bool val ) {
    set( val );
    return *this;
  }

  constexpr void set( bool val ) {
    value_ = val ? value_e::True : value_e::False;
  }

  constexpr bool is_none() const { return value_ == value_e::None; }

  constexpr operator bool() const { return value_ == value_e::True; }

  value_e value_ = value_e::None;
};

template <typename Data, typename Base = action_state_t>
struct hunter_action_state_t : public Base, public Data
{
  static_assert( std::is_base_of_v<action_state_t, Base> );
  static_assert( std::is_default_constructible_v<Data> ); // required for initialize
  static_assert( std::is_copy_assignable_v<Data> ); // required for copy_state

  using Base::Base;

  void initialize() override
  {
    Base::initialize();
    *static_cast<Data*>( this ) = Data{};
  }

  std::ostringstream& debug_str( std::ostringstream& s ) override
  {
    Base::debug_str( s );
    if constexpr ( fmt::is_formattable<Data>::value )
      fmt::print( s, " {}", *static_cast<const Data*>( this ) );
    return s;
  }

  void copy_state( const action_state_t* o ) override
  {
    Base::copy_state( o );
    *static_cast<Data*>( this ) = *static_cast<const Data*>( debug_cast<const hunter_action_state_t*>( o ) );
  }
};

struct pet_amount_expr_t : public expr_t
{
public:
  action_t& action;
  action_t& pet_action;
  action_state_t* state;

  pet_amount_expr_t( util::string_view name, action_t& a, action_t& pet_a )
    : expr_t( name ), action( a ), pet_action( pet_a ), state( pet_a.get_state() )
  {
    state->n_targets = 1;
    state->chain_target = 0;
    state->result = RESULT_HIT;
  }

  double evaluate() override
  {
    state->target = action.target;
    pet_action.snapshot_state( state, result_amount_type::DMG_DIRECT );

    state->result_amount = pet_action.calculate_direct_amount( state );
    state->target->target_mitigation( action.get_school(), result_amount_type::DMG_DIRECT, state );

    return state->result_amount;
  }

  ~pet_amount_expr_t() override
  {
    delete state;
  }
};

struct hunter_t;

namespace pets
{
struct natures_ally_pet_t;
struct dire_critter_t;
struct dire_beast_t;
struct dark_hound_t;
struct dark_minion_t;
struct fenryr_t;
struct hati_t;
struct bear_t;
struct stable_pet_t;
struct hunter_main_pet_base_t;
struct animal_companion_t;
struct hunter_main_pet_t;
}

namespace events
{
struct tar_trap_aoe_t;
}

struct hunter_td_t: public actor_target_data_t
{
  bool damaged = false;

  struct debuffs_t
  {
    buff_t* outland_venom;

    buff_t* spotters_mark;

    buff_t* sentinels_mark;

    buff_t* headshot;
  } debuffs;

  struct dots_t
  {
    dot_t* explosive_shot;
    
    dot_t* barbed_shot;
    dot_t* laceration;

    dot_t* wildfire_bomb;

    dot_t* sanctified_armaments;

    dot_t* black_arrow;
  } dots;

  hunter_td_t( player_t* target, hunter_t* p );

  void target_demise();
};

struct hunter_t final : public player_t
{
public:

  struct pets_t
  {
    pets::hunter_main_pet_t* main = nullptr;
    pets::animal_companion_t* animal_companion = nullptr;
    spawner::pet_spawner_t<pets::natures_ally_pet_t, hunter_t> natures_ally_pet;
    spawner::pet_spawner_t<pets::dire_beast_t, hunter_t> dire_beast;
    spawner::pet_spawner_t<pets::dark_hound_t, hunter_t> dark_hound;
    spawner::pet_spawner_t<pets::dark_minion_t, hunter_t> dark_minion;
    spawner::pet_spawner_t<pets::fenryr_t, hunter_t> fenryr;
    spawner::pet_spawner_t<pets::hati_t, hunter_t> hati;
    spawner::pet_spawner_t<pets::bear_t, hunter_t> bear;

    pets_t( hunter_t* p ) : 
      natures_ally_pet( "natures_ally_pet", p ),
      dire_beast( "dire_beast", p ),
      dark_hound( "dark_hound", p ),
      dark_minion( "dark_minion", p ),
      fenryr( "fenryr", p ),
      hati( "hati", p ),
      bear( "bear", p )
    {
    }
  } pets;

  struct tier_sets_t
  {
    // Midnight Season 1 - Whatever the raid is called
    spell_data_ptr_t mid_s1_bm_2pc;
    spell_data_ptr_t mid_s1_bm_4pc;

    spell_data_ptr_t mid_s1_mm_2pc;
    spell_data_ptr_t mid_s1_mm_4pc;
    spell_data_ptr_t mid_s1_mm_4pc_damage;

    spell_data_ptr_t mid_s1_sv_2pc;
    spell_data_ptr_t mid_s1_sv_4pc;
  } tier_set;

  struct buffs_t
  {
    // Hunter Tree
    buff_t* deathblow;

    // Marksmanship Tree
    buff_t* precise_shots;
    buff_t* trick_shots;
    buff_t* lock_and_load;
    buff_t* in_the_rhythm;
    buff_t* trueshot;
    buff_t* bullseye;
    buff_t* bulletstorm;
    buff_t* volley;
    buff_t* double_tap;
    buff_t* focus_fire;

    // Beast Mastery Tree
    buff_t* barbed_shot;
    buff_t* bestial_wrath;
    buff_t* beast_cleave; 
    buff_t* huntmasters_call;
    buff_t* summon_fenryr;
    buff_t* summon_hati;
    buff_t* heart_of_the_pack;
    buff_t* natures_ally_3;
    buff_t* bloody_frenzy;

    // Survival Tree
    buff_t* tip_of_the_spear;
    buff_t* tip_of_the_spear_boomstick;
    buff_t* tip_of_the_spear_chakram;
    buff_t* mongoose_fury;
    buff_t* bloodseeker;
    buff_t* aspect_of_the_eagle;
    buff_t* wallop;
    buff_t* takedown;
    buff_t* wildfire_imbuement;
    buff_t* raptor_swipe;

    // Pet family buffs
    buff_t* endurance_training;
    buff_t* pathfinding;
    buff_t* predators_thirst;

    // Tier Set Bonuses

    // Hero Talents 

    // Pack Leader
    buff_t* howl_of_the_pack_leader_wyvern;
    buff_t* howl_of_the_pack_leader_boar;
    buff_t* howl_of_the_pack_leader_bear;
    buff_t* howl_of_the_pack_leader_cooldown;
    buff_t* wyverns_cry;
    buff_t* hogstrider;
    buff_t* stampede;
    buff_t* stampede_incoming;

    // Sentinel
    buff_t* stargazer;
    buff_t* moonlight_chakram;

    // Dark Ranger
    buff_t* withering_fire;
    buff_t* wailing_arrow;
  } buffs;

  struct cooldowns_t
  {
    cooldown_t* kill_shot;
    
    cooldown_t* aimed_shot;
    cooldown_t* rapid_fire;
    cooldown_t* trueshot;
    cooldown_t* target_acquisition;
    cooldown_t* volley;
    cooldown_t* salvo;
    
    cooldown_t* dire_beast;
    cooldown_t* kill_command;
    cooldown_t* wild_thrash;

    cooldown_t* barbed_shot;
    cooldown_t* bestial_wrath;

    cooldown_t* wildfire_bomb;
    cooldown_t* harpoon;
    cooldown_t* boomstick;
    cooldown_t* strike_as_one;
    cooldown_t* takedown;
    cooldown_t* flamefang_pitch;

    cooldown_t* black_arrow;
    cooldown_t* bleak_powder;
  } cooldowns;

  struct gains_t
  {
    gain_t* barbed_shot;
    gain_t* pack_tactics;
    gain_t* invigorating_pulse;
    gain_t* serpentine_strikes;
    gain_t* lethal_barbs;
    gain_t* disruptive_rounds;
  } gains;

  struct procs_t
  {
    proc_t* snakeskin_quiver;
    proc_t* dire_command;

    proc_t* deathblow;

    proc_t* dire_beast_spawn;
    proc_t* dark_minion_spawn;
    proc_t* dark_hound_spawn;
  } procs;

  struct rppm_t
  {
    real_ppm_t* corpsecaller;
    real_ppm_t* shadow_surge;

    real_ppm_t* let_fly;
  } rppm;

  struct accumulated_rngs_t
  {
    accumulated_rng_t* dire_command;
  } accumulated_rng;

  struct talents_t
  {
    // Hunter Tree
    spell_data_ptr_t rejuvenating_winds; //Utility talent, won't implement
    spell_data_ptr_t survival_of_the_fittest; //Utility talent, won't implement
    spell_data_ptr_t posthaste; //Utility talent, won't implement

    spell_data_ptr_t natural_mending; //Utility talent, won't implement
    spell_data_ptr_t padded_armor; //Utility talent, won't implement
    spell_data_ptr_t hunters_avoidance; //Utility talent, won't implement

    spell_data_ptr_t wilderness_medicine; //Utility talent, won't implement
    spell_data_ptr_t combat_experience;
    spell_data_ptr_t improved_aspect_of_the_cheetah; //Utility talent, won't implement
    spell_data_ptr_t concussive_shot; //Not implemented - probably not needed

    spell_data_ptr_t precision_strikes;
    spell_data_ptr_t counter_shot;
    spell_data_ptr_t muzzle;
    spell_data_ptr_t serrated_tips;

    spell_data_ptr_t tranquilizing_shot; //Not implemented - probably not needed
    spell_data_ptr_t pathfinding; //Utility talent, won't implement
    spell_data_ptr_t disruptive_rounds;
    spell_data_ptr_t improved_feign_death; //Utility talent, won't implement
    spell_data_ptr_t misdirection; //Utility talent, won't implement

    spell_data_ptr_t kodo_tranquilizer; //Utility talent, won't implement
    spell_data_ptr_t devilsaur_tranquilizer; //Utility talent, won't implement
    spell_data_ptr_t kindling_flare; //Utility talent, won't implement
    spell_data_ptr_t trigger_finger;
    spell_data_ptr_t tar_trap;
    spell_data_ptr_t scare_beast; //Utility talent, won't implement
    spell_data_ptr_t touch_of_grass; //Utility talent, won't implement
    spell_data_ptr_t camouflage; //Utility talent, won't implement
    spell_data_ptr_t no_hard_feelings; //Utility talent, won't implement

    spell_data_ptr_t improved_aspect_of_the_turtle; //Utility talent, won't implement
    spell_data_ptr_t specialized_arsenal;
    spell_data_ptr_t scouts_instincts; //Utility talent, won't implement

    spell_data_ptr_t shell_wall; //Utility talent, won't implement
    spell_data_ptr_t intimidation; //Utility talent, won't implement
    spell_data_ptr_t improved_snaring; //Utility talent, won't implement
    spell_data_ptr_t lone_survivor; //Utility talent, won't implement
    spell_data_ptr_t catlike_reflexes; //Utility talent, won't implement
    spell_data_ptr_t binding_shot; //Utility talent, won't implement
    spell_data_ptr_t trailblazer; //Utility talent, won't implement
    spell_data_ptr_t moment_of_opportunity; //Utility talent, won't implement

    spell_data_ptr_t cold_feet; //Utility talent, won't implement
    spell_data_ptr_t territorial_instincts; //Utility talent, won't implement
    spell_data_ptr_t guttural_roar; //Utility talent, won't implement
    spell_data_ptr_t born_to_be_wild; //Utility talent, won't implement
    spell_data_ptr_t keen_eyesight;
    spell_data_ptr_t tar_coated_bindings; //Utility talent, won't implement
    spell_data_ptr_t horsehair_tether; //Utility talent, won't implement
    spell_data_ptr_t improved_traps; //Utility talent, won't implement

    spell_data_ptr_t emergency_salve; //Utility talent, won't implement
    spell_data_ptr_t roar_of_sacrifice; //Utility talent, won't implement
    spell_data_ptr_t guardians_hide; //Utility talent, won't implement
    spell_data_ptr_t unnatural_causes;
    spell_data_ptr_t unnatural_causes_debuff;

    spell_data_ptr_t deathblow_buff;
    
    // Beast Mastery Tree
    spell_data_ptr_t kill_command_bm_player;
    spell_data_ptr_t kill_command_bm_pet;

    spell_data_ptr_t animal_companion;
    spell_data_ptr_t solitary_companion;
    spell_data_ptr_t barbed_shot;
    spell_data_ptr_t barbed_shot_buff;

    spell_data_ptr_t alpha_predator;
    spell_data_ptr_t dire_beast;
    spell_data_ptr_t stomp;
    spell_data_ptr_t stomp_dmg;
    spell_data_ptr_t war_orders;

    spell_data_ptr_t wild_thrash_player;
    spell_data_ptr_t wild_thrash_pet;
    spell_data_ptr_t bestial_wrath;
    spell_data_ptr_t cobra_shot;
    spell_data_ptr_t cobra_shot_data;

    spell_data_ptr_t beast_cleave;
    spell_data_ptr_t scent_of_blood;
    spell_data_ptr_t thundering_hooves;
    spell_data_ptr_t go_for_the_throat;

    spell_data_ptr_t laceration;
    spell_data_ptr_t laceration_driver;
    spell_data_ptr_t laceration_bleed;
    spell_data_ptr_t kill_cleave;
    spell_data_ptr_t training_expert;
    spell_data_ptr_t the_beast_within;
    spell_data_ptr_t thrill_of_the_hunt;
    spell_data_ptr_t pack_tactics;
    spell_data_ptr_t pack_tactics_energize;
    spell_data_ptr_t barbed_scales;

    spell_data_ptr_t aspect_of_the_beast;
    spell_data_ptr_t dire_cleave;
    spell_data_ptr_t dire_command;
    spell_data_ptr_t jagged_wounds;
    spell_data_ptr_t serpentine_strikes;
    spell_data_ptr_t serpentine_strikes_energize;
    spell_data_ptr_t snakeskin_quiver;
    spell_data_ptr_t cobra_senses;

    spell_data_ptr_t dire_frenzy;
    spell_data_ptr_t frenzy;
    spell_data_ptr_t killer_instinct;

    spell_data_ptr_t brutal_companion;
    spell_data_ptr_t huntmasters_call;  // NOTE: info_base.md lists as "Huntmaster" (ID 459730) — Huntmaster's Call is correct SimC name
    spell_data_ptr_t heart_of_the_pack;
    spell_data_ptr_t heart_of_the_pack_buff;
    spell_data_ptr_t bloodshed;
    spell_data_ptr_t bloodshed_dot;
    spell_data_ptr_t savagery_bm;
    spell_data_ptr_t killer_cobra;
    spell_data_ptr_t master_handler;

    spell_data_ptr_t wildspeaker;
    spell_data_ptr_t wildspeaker_kill_command;
    spell_data_ptr_t wildspeaker_bestial_wrath;
    spell_data_ptr_t wild_instincts;   // NOTE: not in info_base.md BM talent table — Midnight-era talent not listed
    spell_data_ptr_t bloody_frenzy;    // NOTE: not in info_base.md BM talent table — Midnight-era talent not listed
    spell_data_ptr_t bloody_frenzy_buff;
    spell_data_ptr_t piercing_fangs;

    spell_data_ptr_t natures_ally_1;         // NOTE: info_base.md lists as "Nature's Ally" (ID 1273043) — multi-rank split in code
    spell_data_ptr_t natures_ally_1_summon;
    spell_data_ptr_t natures_ally_2;
    spell_data_ptr_t natures_ally_3;
    spell_data_ptr_t natures_ally_3_buff;

    // Marksmanship Tree
    spell_data_ptr_t aimed_shot;

    spell_data_ptr_t rapid_fire;
    spell_data_ptr_t rapid_fire_tick;
    spell_data_ptr_t rapid_fire_energize;
    spell_data_ptr_t precise_shots;
    spell_data_ptr_t precise_shots_buff;

    spell_data_ptr_t quick_draw; //TODO implement move speed buff?
    spell_data_ptr_t lock_and_load; // TODO how does its blp work
    spell_data_ptr_t lock_and_load_buff;

    spell_data_ptr_t surging_shots;
    spell_data_ptr_t avian_specialization;
    spell_data_ptr_t unbreakable_bond;
    spell_data_ptr_t trick_shots;
    spell_data_ptr_t trick_shots_data;
    spell_data_ptr_t trick_shots_buff;
    spell_data_ptr_t aspect_of_the_hydra;

    spell_data_ptr_t in_the_rhythm;
    spell_data_ptr_t in_the_rhythm_buff;
    spell_data_ptr_t penetrating_shots;
    spell_data_ptr_t tenacious; //Utility talent, won't implement
    spell_data_ptr_t cunning; //Utility talent, won't implement
    spell_data_ptr_t master_marksman;
    spell_data_ptr_t master_marksman_bleed;
    spell_data_ptr_t light_ammo;

    spell_data_ptr_t obsidian_arrowhead;
    spell_data_ptr_t on_target;
    spell_data_ptr_t trueshot;
    spell_data_ptr_t kill_shot;

    spell_data_ptr_t target_acquisition;
    spell_data_ptr_t critical_precision;
    spell_data_ptr_t no_scope;
    spell_data_ptr_t feathered_frenzy;
    spell_data_ptr_t lethality;
    spell_data_ptr_t headshot;
    spell_data_ptr_t headshot_debuff;
    spell_data_ptr_t deadeye;
    spell_data_ptr_t deathblow;

    spell_data_ptr_t take_aim_1;
    spell_data_ptr_t unmatched_precision;
    spell_data_ptr_t bullseye;
    spell_data_ptr_t bullseye_buff;
    spell_data_ptr_t calling_the_shots;
    spell_data_ptr_t unerring_vision; 
    spell_data_ptr_t small_game_hunter;
    spell_data_ptr_t eagles_accuracy;

    spell_data_ptr_t take_aim_2;
    spell_data_ptr_t focused_aim;
    spell_data_ptr_t bulletstorm;
    spell_data_ptr_t bulletstorm_buff;
    spell_data_ptr_t tensile_bowstring;
    spell_data_ptr_t volley;
    spell_data_ptr_t volley_data;
    spell_data_ptr_t volley_dmg;
    spell_data_ptr_t focus_fire;
    spell_data_ptr_t focus_fire_buff;

    spell_data_ptr_t take_aim_3;
    spell_data_ptr_t windrunner_quiver;
    spell_data_ptr_t incendiary_ammunition;
    spell_data_ptr_t double_tap;
    spell_data_ptr_t double_tap_buff;
    spell_data_ptr_t salvo;
    spell_data_ptr_t explosive_shot_data;
    spell_data_ptr_t explosive_shot_damage;
    spell_data_ptr_t bullet_hell;
    spell_data_ptr_t shrapnel_shot;
    spell_data_ptr_t unload;

    // Survival Tree
    spell_data_ptr_t kill_command_sv_player;
    spell_data_ptr_t kill_command_sv_pet;

    spell_data_ptr_t wildfire_bomb;
    spell_data_ptr_t wildfire_bomb_data;
    spell_data_ptr_t wildfire_bomb_dmg;
    spell_data_ptr_t wildfire_bomb_dot;
    spell_data_ptr_t raptor_strike;
    spell_data_ptr_t raptor_strike_eagle;

    spell_data_ptr_t raptor_swipe_1;
    spell_data_ptr_t raptor_swipe_2;
    spell_data_ptr_t raptor_swipe_3;
    spell_data_ptr_t raptor_swipe_spell;
    spell_data_ptr_t raptor_swipe_buff;

    spell_data_ptr_t guerrilla_tactics;
    spell_data_ptr_t tip_of_the_spear;
    spell_data_ptr_t tip_of_the_spear_buff;
    spell_data_ptr_t tip_of_the_spear_boomstick_buff;
    spell_data_ptr_t tip_of_the_spear_chakram_buff;

    spell_data_ptr_t lunge;
    spell_data_ptr_t boomstick;
    spell_data_ptr_t strike_as_one;
    spell_data_ptr_t strike_as_one_dmg;

    spell_data_ptr_t shrapnel_bomb;
    spell_data_ptr_t shrapnel_bomb_bleed;
    spell_data_ptr_t flamebreak;
    spell_data_ptr_t bloodseeker;
    spell_data_ptr_t quick_reload;
    spell_data_ptr_t flankers_advantage;
    spell_data_ptr_t two_against_many;

    spell_data_ptr_t mongoose_fury;
    spell_data_ptr_t mongoose_fury_buff;
    spell_data_ptr_t mongoose_rounds;
    spell_data_ptr_t wildfire_shells;
    spell_data_ptr_t shellshock;
    spell_data_ptr_t sic_em;
    spell_data_ptr_t sic_em_bleed;

    spell_data_ptr_t bloody_claws;
    spell_data_ptr_t wallop;
    spell_data_ptr_t wallop_buff;
    spell_data_ptr_t improved_wildfire_bomb;
    spell_data_ptr_t bonding;
    spell_data_ptr_t sweeping_spear;
    spell_data_ptr_t vulnerability;
    spell_data_ptr_t blackrock_munitions;
    spell_data_ptr_t shower_of_blood;
    spell_data_ptr_t outland_venom;
    spell_data_ptr_t outland_venom_debuff;

    spell_data_ptr_t explosives_expert;
    spell_data_ptr_t takedown;
    spell_data_ptr_t takedown_energize;
    spell_data_ptr_t takedown_dmg;
    spell_data_ptr_t takedown_pet;
    spell_data_ptr_t killer_companion;

    spell_data_ptr_t flamefang_pitch;
    spell_data_ptr_t flamefang_pitch_data;
    spell_data_ptr_t flamefang_pitch_dmg;
    spell_data_ptr_t flamefang_pitch_aoe;
    spell_data_ptr_t twin_fangs;
    spell_data_ptr_t savagery_sv;
    spell_data_ptr_t wildfire_infusion;

    spell_data_ptr_t grenade_juggler;
    spell_data_ptr_t wildfire_imbuement;
    spell_data_ptr_t wildfire_imbuement_dmg;
    spell_data_ptr_t wildfire_imbuement_buff;
    spell_data_ptr_t flanked;
    spell_data_ptr_t lethal_calibration;
    spell_data_ptr_t primal_surge;

    // Dark Ranger
    spell_data_ptr_t black_arrow;
    spell_data_ptr_t black_arrow_spell;
    spell_data_ptr_t black_arrow_dot;
    
    spell_data_ptr_t bleak_arrows;
    spell_data_ptr_t bleak_arrows_spell;
    spell_data_ptr_t soul_drinker;
    spell_data_ptr_t bleak_powder;
    spell_data_ptr_t bleak_powder_spell;
    spell_data_ptr_t corpsecaller;
    spell_data_ptr_t corpsecaller_minion_summon;
    spell_data_ptr_t corpsecaller_hound_summon;

    spell_data_ptr_t ebon_bowstring;
    spell_data_ptr_t through_the_eyes;
    spell_data_ptr_t smoke_screen; //Utility talent, won't implement
    spell_data_ptr_t dark_chains; //Utility talent, won't implement
    spell_data_ptr_t shadow_dagger; //Utility talent, won't implement
    spell_data_ptr_t wailing_dead;
    spell_data_ptr_t wailing_arrow;
    spell_data_ptr_t wailing_arrow_buff;
    spell_data_ptr_t wailing_arrow_damage;

    spell_data_ptr_t blighted_quiver;
    spell_data_ptr_t banshees_mark;
    spell_data_ptr_t the_bell_tolls;
    spell_data_ptr_t umbral_reach;
    spell_data_ptr_t pact_of_the_hollow;

    spell_data_ptr_t withering_fire;
    spell_data_ptr_t withering_fire_black_arrow;
    spell_data_ptr_t withering_fire_buff;

    // Pack Leader
    spell_data_ptr_t howl_of_the_pack_leader;
    spell_data_ptr_t howl_of_the_pack_leader_wyvern_ready_buff;
    spell_data_ptr_t howl_of_the_pack_leader_boar_ready_buff;
    spell_data_ptr_t howl_of_the_pack_leader_bear_ready_buff;
    spell_data_ptr_t howl_of_the_pack_leader_cooldown_buff;
    spell_data_ptr_t howl_of_the_pack_leader_wyvern_summon;
    spell_data_ptr_t howl_of_the_pack_leader_wyvern_buff;
    spell_data_ptr_t howl_of_the_pack_leader_boar_charge_trigger;
    spell_data_ptr_t howl_of_the_pack_leader_boar_charge_impact;
    spell_data_ptr_t howl_of_the_pack_leader_boar_charge_cleave;
    spell_data_ptr_t howl_of_the_pack_leader_bear_summon;
    spell_data_ptr_t howl_of_the_pack_leader_bear_buff;
    spell_data_ptr_t howl_of_the_pack_leader_bear_bleed;

    spell_data_ptr_t pack_mentality;
    spell_data_ptr_t dire_summons;
    spell_data_ptr_t better_together;
    spell_data_ptr_t slicked_shoes; //Utility talent, won't implement
    spell_data_ptr_t masterful_call; //Utility talent, won't implement

    spell_data_ptr_t ursine_fury;
    spell_data_ptr_t dire_beast_summon;
    spell_data_ptr_t sharpened_claws;
    spell_data_ptr_t fury_of_the_wyvern;
    spell_data_ptr_t hogstrider;
    spell_data_ptr_t hogstrider_buff;
    spell_data_ptr_t lethal_barbs;
    spell_data_ptr_t lethal_barbs_energize;

    spell_data_ptr_t no_mercy;
    spell_data_ptr_t shell_cover; //Utility talent, won't implement
    spell_data_ptr_t hoof_and_blade;
    spell_data_ptr_t wyverns_gaze;
    spell_data_ptr_t sharpened_fangs;
    
    spell_data_ptr_t stampede;
    spell_data_ptr_t stampede_incoming_buff;
    spell_data_ptr_t stampede_trigger;
    spell_data_ptr_t stampede_dmg;
    
    // Sentinel
    spell_data_ptr_t sentinel;
    spell_data_ptr_t sentinels_mark;

    spell_data_ptr_t dont_look_back; //Utility talent, won't implement
    spell_data_ptr_t moons_blessing;
    spell_data_ptr_t sanctified_armaments;
    spell_data_ptr_t sanctified_armaments_dot;
    spell_data_ptr_t moonlight_chakram;
    spell_data_ptr_t moonlight_chakram_spell;
    spell_data_ptr_t moonlight_chakram_damage;
    spell_data_ptr_t moonlight_chakram_buff;

    spell_data_ptr_t stargazer;
    spell_data_ptr_t stargazer_buff;
    spell_data_ptr_t open_fire;
    spell_data_ptr_t cant_miss_wont_miss;
    spell_data_ptr_t invigorating_pulse;
    spell_data_ptr_t twilight_requiem;
    spell_data_ptr_t twilight_requiem_damage;
    spell_data_ptr_t stalk_and_strike;

    spell_data_ptr_t arcane_talons;
    spell_data_ptr_t lunar_calling;
    spell_data_ptr_t conditioning; //Utility talent, won't implement
    spell_data_ptr_t scouts_vigil; //Utility talent, won't implement
    spell_data_ptr_t radiant_edge;

    spell_data_ptr_t lunar_storm;
    spell_data_ptr_t lunar_storm_dmg;
  } talents;

  // Specialization Spells
  struct specs_t
  {
    spell_data_ptr_t pet_damage; // 2026-02-03: Generic "Pet Damage" buff, used as a tuning knob for Dire Beasts
    spell_data_ptr_t hunter;
    spell_data_ptr_t beast_mastery_hunter;
    spell_data_ptr_t marksmanship_hunter;
    spell_data_ptr_t survival_hunter;

    spell_data_ptr_t auto_shot;
    spell_data_ptr_t freezing_trap;
    spell_data_ptr_t arcane_shot;
    spell_data_ptr_t steady_shot;
    spell_data_ptr_t steady_shot_energize;
    spell_data_ptr_t flare;
    spell_data_ptr_t call_pet;

    // SV
    spell_data_ptr_t aspect_of_the_eagle;
    spell_data_ptr_t harpoon;
    spell_data_ptr_t hatchet_toss;

    // MM
    spell_data_ptr_t multishot;
    spell_data_ptr_t spotters_mark_data;
    spell_data_ptr_t spotters_mark_debuff;
  } specs;

  struct mastery_spells_t
  {
    spell_data_ptr_t master_of_beasts; // BM
    spell_data_ptr_t sniper_training; // MM
    spell_data_ptr_t spirit_bond; // SV
    spell_data_ptr_t spirit_bond_buff;
  } mastery;

  struct {
    action_t* barbed_shot = nullptr;
    action_t* snakeskin_quiver = nullptr;
    action_t* laceration = nullptr;

    action_t* boar_charge = nullptr;

    action_t* lunar_storm = nullptr;

    action_t* stampede = nullptr;
    action_t* wild_instincts = nullptr;

    action_t* let_fly = nullptr;
  } actions;

  cdwaste::player_data_t cd_waste;

  struct {
    events::tar_trap_aoe_t* tar_trap_aoe = nullptr;
    event_t* current_volley = nullptr;
    howl_of_the_pack_leader_beast howl_of_the_pack_leader_next_beast = WYVERN;
    timespan_t fury_of_the_wyvern_extension = 0_s;
    bool fury_of_the_wyvern_extendable = false;
  } state;

  struct options_t {
    std::string summon_pet_str = "duck";
    timespan_t pet_attack_speed = 2_s;
    timespan_t pet_basic_attack_delay = 0.15_s;
    bool max_prio_damage = true;
  } options;

  hunter_t( sim_t* sim, util::string_view name, race_e r = RACE_NONE ) :
    player_t( sim, HUNTER, name, r ),
    pets( this ),
    buffs(),
    cooldowns(),
    gains(),
    procs()
  {
    cooldowns.kill_shot       = get_cooldown( "kill_shot" );

    cooldowns.aimed_shot                = get_cooldown( "aimed_shot" );
    cooldowns.rapid_fire                = get_cooldown( "rapid_fire" );
    cooldowns.trueshot                  = get_cooldown( "trueshot" );
    cooldowns.target_acquisition        = get_cooldown( "target_acquisition_icd" );
    cooldowns.volley                    = get_cooldown( "volley" );
    cooldowns.salvo                     = get_cooldown( "salvo_icd" );
    
    cooldowns.kill_command  = get_cooldown( "kill_command" );
    cooldowns.barbed_shot   = get_cooldown( "barbed_shot" );
    cooldowns.bestial_wrath = get_cooldown( "bestial_wrath" );
    cooldowns.dire_beast    = get_cooldown( "dire_beast" );
    cooldowns.wild_thrash   = get_cooldown( "wild_thrash" );

    cooldowns.wildfire_bomb       = get_cooldown( "wildfire_bomb" );
    cooldowns.harpoon             = get_cooldown( "harpoon" );
    cooldowns.boomstick           = get_cooldown( "boomstick" );
    cooldowns.strike_as_one       = get_cooldown( "strike_as_one" );
    cooldowns.takedown            = get_cooldown( "takedown" );
    cooldowns.flamefang_pitch     = get_cooldown( "flamefang_pitch" );

    cooldowns.black_arrow = get_cooldown( "black_arrow" );
    cooldowns.bleak_powder = get_cooldown( "bleak_powder_icd" );

    base_gcd = 1.5_s;

    resource_regeneration = regen_type::DYNAMIC;
    regen_caches[ CACHE_HASTE ] = true;
    regen_caches[ CACHE_ATTACK_HASTE ] = true;
  }

  // Character Definition
  void init() override;
  void init_spells() override;
  void init_base_stats() override;
  void create_actions() override;
  void create_buffs() override;
  void init_gains() override;
  void init_position() override;
  void init_procs() override;
  void init_rng() override;
  void init_scaling() override;
  void init_assessors() override;
  void init_action_list() override;
  void init_blizzard_action_list() override;
  parsed_assisted_combat_rule_t parse_assisted_combat_rule( const assisted_combat_rule_data_t& rule, const assisted_combat_step_data_t& step ) const override;
  std::vector<std::string> action_names_from_spell_id( unsigned int spell_id ) const override;
  void parse_assisted_combat_step( const assisted_combat_step_data_t& step, action_priority_list_t* assisted_combat ) override;
  void init_special_effects() override;
  void init_finished() override;
  void reset() override;
  void merge( player_t& other ) override;
  void arise() override;
  void combat_begin() override;
  bool validate_actor() override;

  void datacollection_begin() override;
  void datacollection_end() override;

  double composite_melee_crit_chance() const override;
  double composite_spell_crit_chance() const override;
  double composite_rating_multiplier( rating_e ) const override;
  double composite_melee_auto_attack_speed() const override;
  double composite_player_critical_damage_multiplier( const action_state_t*, school_e ) const override;
  double composite_player_multiplier( school_e school ) const override;
  double composite_player_target_multiplier( player_t* target, school_e school ) const override;
  double composite_player_pet_damage_multiplier( const action_state_t*, bool ) const override;
  double composite_player_target_pet_damage_multiplier( player_t* target, bool guardian ) const override;
  double composite_leech() const override;
  double matching_gear_multiplier( attribute_e attr ) const override;
  double stacking_movement_modifier() const override;
  void invalidate_cache( cache_e ) override;
  void regen( timespan_t periodicity ) override;
  double resource_gain( resource_e resource_type, double amount, gain_t* g = nullptr, action_t* a = nullptr ) override;
  void create_options() override;
  std::unique_ptr<expr_t> create_expression( util::string_view expression_str ) override;
  std::unique_ptr<expr_t> create_action_expression( action_t&, util::string_view expression_str ) override;
  action_t* create_action( util::string_view name, util::string_view options ) override;
  pet_t* create_pet( util::string_view name, util::string_view type ) override;
  void create_pets() override;
  double resource_loss( resource_e resource_type, double amount, gain_t* g = nullptr, action_t* a = nullptr ) override;
  resource_e primary_resource() const override { return RESOURCE_FOCUS; }
  role_e primary_role() const override { return ROLE_ATTACK; }
  stat_e convert_hybrid_stat( stat_e s ) const override;
  std::string create_profile( save_e ) override;
  void copy_from( player_t* source ) override;
  void moving( ) override;

  std::string default_potion() const override { return hunter_apl::potion( this ); }
  std::string default_flask() const override { return hunter_apl::flask( this ); }
  std::string default_food() const override { return hunter_apl::food( this ); }
  std::string default_rune() const override { return hunter_apl::rune( this ); }
  std::string default_temporary_enchant() const override { return hunter_apl::temporary_enchant( this ); }

  target_specific_t<hunter_td_t> target_data;

  const hunter_td_t* find_target_data( const player_t* target ) const override
  {
    return target_data[ target ];
  }

  hunter_td_t* get_target_data( player_t* target ) const override
  {
    hunter_td_t*& td = target_data[target];
    if ( !td ) td = new hunter_td_t( target, const_cast<hunter_t*>( this ) );
    return td;
  }

  std::vector<action_t*> background_actions;

  template <typename T, typename... Ts>
  T* get_background_action( util::string_view n, Ts&&... args )
  {
    auto it = range::find( background_actions, n, &action_t::name_str );
    if ( it != background_actions.cend() )
      return dynamic_cast<T*>( *it );

    auto action = new T( n, this, std::forward<Ts>( args )... );
    action -> background = true;
    background_actions.push_back( action );
    return action;
  }

  void trigger_bloodseeker_update();
  int ticking_dots( hunter_td_t* td );
  void trigger_outland_venom_update();
  void consume_trick_shots();
  void trigger_deathblow( bool activated = false );
  void trigger_lunar_storm( player_t* target );
  void consume_precise_shots();
  void trigger_eagles_mark( player_t* target, bool sentinel, bool force = false );
  bool consume_howl_of_the_pack_leader( player_t* target );
  void trigger_howl_of_the_pack_leader();
  void trigger_natures_ally_3();
  void trigger_huntmasters_call();
  void spawn_dire_beast( timespan_t base_duration, bool force_hound = false );
};

// Template for common hunter action code.
template <class Base>
struct hunter_action_t: public Base
{
private:
  using ab = Base;
public:

  bool track_cd_waste;
  maybe_bool decrements_tip_of_the_spear;
  double dire_beast_chance = 0;

  struct {
    // Hunter
    // TODO 26/4/25: possibly entirely scripted now, now that the passive mods are gone we know the target debuff 459529 should be ignored by 
    // residual bleeds but they see behavior identical to normal dots: 10% is correctly applied outside of execute but in execute range a final
    // value of about 15.23% is seen now, so using the same assumed behavior of the bleed mods originally, execute range simply applies another 4.76% mod
    damage_affected_by unnatural_causes;

    // Beast Mastery
    damage_affected_by bestial_wrath;
    damage_affected_by master_of_beasts;

    // Marksmanship
    bool trueshot_crit_damage_bonus = false;
    bool bullseye_crit_chance = false;
    damage_affected_by lone_wolf;
    damage_affected_by sniper_training;
    damage_affected_by headshot;

    // Survival
    bool outland_venom = false;
    damage_affected_by spirit_bond;
    damage_affected_by tip_of_the_spear;
    damage_affected_by mongoose_fury;
    damage_affected_by wallop;
    damage_affected_by takedown;

    // Sentinel
    damage_affected_by sentinels_mark;
    bool stargazer = false;

    // Pack Leader
    damage_affected_by wyverns_cry;

    // Dark Ranger
    damage_affected_by through_the_eyes;
  } affected_by;

  cdwaste::action_data_t* cd_waste = nullptr;

  hunter_action_t( util::string_view n, hunter_t* p, const spell_data_t* s ):
    ab( n, p, s ),
    track_cd_waste( s -> cooldown() > 0_ms || s -> charge_cooldown() > 0_ms )
  {
    ab::special = true;

    affected_by.unnatural_causes = parse_damage_affecting_aura( this, p->talents.unnatural_causes_debuff );
    
    affected_by.sniper_training = parse_damage_affecting_aura( this, p->mastery.sniper_training );
    affected_by.headshot = parse_damage_affecting_aura( this, p->talents.headshot_debuff );
    affected_by.trueshot_crit_damage_bonus = check_affected_by( this, p->talents.trueshot->effectN( 4 ) );
    affected_by.bullseye_crit_chance = check_affected_by( this, p->talents.bullseye->effectN( 1 ).trigger()->effectN( 1 ) );

    affected_by.bestial_wrath = parse_damage_affecting_aura( this, p->talents.bestial_wrath );
    affected_by.master_of_beasts = parse_damage_affecting_aura( this, p->mastery.master_of_beasts );

    affected_by.spirit_bond = parse_damage_affecting_aura( this, p->mastery.spirit_bond );
    affected_by.tip_of_the_spear = parse_damage_affecting_aura( this, p->talents.tip_of_the_spear_buff );
    affected_by.outland_venom = check_affected_by( this, p->talents.outland_venom_debuff->effectN( 1 ) );
    affected_by.mongoose_fury = parse_damage_affecting_aura( this, p->talents.mongoose_fury_buff );
    affected_by.wallop = parse_damage_affecting_aura( this, p->talents.wallop_buff );
    affected_by.takedown = parse_damage_affecting_aura( this, p->talents.takedown );

    affected_by.sentinels_mark = parse_damage_affecting_aura( this, p->talents.sentinels_mark );
    affected_by.stargazer      = check_affected_by( this, p->talents.stargazer_buff->effectN( 1 ) );

    affected_by.wyverns_cry = parse_damage_affecting_aura( this, p->talents.howl_of_the_pack_leader_wyvern_buff );

    affected_by.through_the_eyes = parse_damage_affecting_aura( this, p->talents.black_arrow_dot );
  }

  hunter_t* p()             { return static_cast<hunter_t*>( ab::player ); }
  const hunter_t* p() const { return static_cast<hunter_t*>( ab::player ); }

  hunter_td_t* td( player_t* t ) { return p() -> get_target_data( t ); }
  const hunter_td_t* td( player_t* t ) const { return p() -> get_target_data( t ); }
  const hunter_td_t* find_td( const player_t* t ) const { return p() -> find_target_data( t ); }

  void init() override
  {
    ab::init();

    if ( track_cd_waste )
      cd_waste = p() -> cd_waste.get( this );

    if ( p()->talents.tip_of_the_spear.ok() )
    {
      if ( decrements_tip_of_the_spear.is_none() )
        decrements_tip_of_the_spear = affected_by.tip_of_the_spear.direct > 0;
    }
    else
    {
      decrements_tip_of_the_spear = false;
    }

    if ( p()->talents.dire_beast.ok() )
    {
      if ( dire_beast_chance == 0 )
      {
        for ( size_t i = 1; i <= ab::data().effect_count(); i++ )
        {
          if ( ab::data().effectN( i ).subtype() == effect_subtype_t::A_PERIODIC_DAMAGE &&
            ab::data().get_school_type() == SCHOOL_PHYSICAL &&
            ( ab::data().effectN( i ).mechanic() == MECHANIC_BLEED || ab::data().mechanic() == MECHANIC_BLEED ) )
          {
            dire_beast_chance = p()->talents.dire_beast->effectN( 1 ).percent();
            break;
          }
        }
      }
    }

    if ( decrements_tip_of_the_spear )
      ab::sim->print_debug( "{} action {} set to decrement Tip of the Spear", ab::player->name(), ab::name() );

    if ( dire_beast_chance > 0 )
      ab::sim->print_debug( "{} action {} set to trigger Dire Beast with {}% chance", ab::player->name(), ab::name(), dire_beast_chance * 100 );
  }

  timespan_t gcd() const override
  {
    timespan_t g = ab::gcd();

    if ( g == 0_ms )
      return g;

    if ( g < ab::min_gcd )
      g = ab::min_gcd;

    return g;
  }

  void execute() override
  {
    ab::execute();

    if ( affected_by.wallop.direct )
      p()->buffs.wallop->expire();
  }

  void impact( action_state_t* s ) override
  {
    ab::impact( s );

    // Tip removal and effects are triggered on impact but only once
    if ( decrements_tip_of_the_spear && s->chain_target == 0 && p()->buffs.tip_of_the_spear->check() )
    {
      p()->buffs.tip_of_the_spear->decrement();
      p()->buffs.stargazer->trigger();

      // 2026-02-13: For Survival, Sentinel's Mark applies to a random target hit for AoE spells.
      //             Tipped Wildfire Bombs can also trigger an additional mark after consuming one so make an event.
      make_event( p()->sim, [ this ]() { p()->trigger_eagles_mark( get_random_valid_target(), true ); } );

      if ( p()->cooldowns.strike_as_one->up() )
      {
        auto pet = p()->pets.main;
        if ( pet )
        {
          pet->actions.strike_as_one->execute_on_target( p()->target );
          p()->cooldowns.strike_as_one->start();
        }
      }
    }
  }

  double composite_da_multiplier( const action_state_t* s ) const override
  {
    double am = ab::composite_da_multiplier( s );

    if ( affected_by.bestial_wrath.direct )
      am *= 1 + p()->buffs.bestial_wrath->check_value();

    if ( affected_by.master_of_beasts.direct )
      am *= 1 + p()->cache.mastery() * p()->mastery.master_of_beasts->effectN( affected_by.master_of_beasts.direct ).mastery_value();

    if ( affected_by.sniper_training.direct )
      am *= 1 + p()->cache.mastery() * p()->mastery.sniper_training->effectN( affected_by.sniper_training.direct ).mastery_value();

    if ( affected_by.spirit_bond.direct )
    {
      double bonus = p()->cache.mastery() * p()->mastery.spirit_bond->effectN( affected_by.spirit_bond.direct ).mastery_value();
      bonus *= 1 + p()->mastery.spirit_bond_buff->effectN( 1 ).percent();
      am *= 1 + bonus;
    }

    if ( affected_by.mongoose_fury.direct && p()->buffs.mongoose_fury->check() )
      am *= 1 + p()->buffs.mongoose_fury->stack_value();

    if ( affected_by.wallop.direct && p()->buffs.wallop->check() )
      am *= 1 + p()->buffs.wallop->value();

    if ( affected_by.takedown.direct && p()->buffs.takedown->check() )
      am *= 1 + p()->talents.takedown->effectN( affected_by.takedown.direct ).percent();

    if ( affected_by.tip_of_the_spear.direct && p()->buffs.tip_of_the_spear->check() )
      am *= 1 + p()->talents.tip_of_the_spear_buff->effectN( 1 ).percent();

    if ( affected_by.wyverns_cry.direct )
      am *= 1 + p()->buffs.wyverns_cry->check_stack_value();

    return am;
  }

  double composite_ta_multiplier( const action_state_t* s ) const override
  {
    double am = ab::composite_ta_multiplier( s );

    if ( affected_by.bestial_wrath.tick )
      am *= 1 + p()->buffs.bestial_wrath->check_value();

    if ( affected_by.master_of_beasts.tick )
      am *= 1 + p()->cache.mastery() * p()->mastery.master_of_beasts->effectN( affected_by.master_of_beasts.tick ).mastery_value();

    if ( affected_by.sniper_training.tick )
      am *= 1 + p()->cache.mastery() * p()->mastery.sniper_training->effectN( affected_by.sniper_training.tick ).mastery_value();

    if ( affected_by.spirit_bond.tick )
    {
      double bonus = p()->cache.mastery() * p()->mastery.spirit_bond->effectN( affected_by.spirit_bond.tick ).mastery_value();
      bonus *= 1 + p()->mastery.spirit_bond_buff->effectN( 3 ).percent();
      am *= 1 + bonus;
    }

    if ( affected_by.takedown.tick && p()->buffs.takedown->check() )
      am *= 1 + p()->talents.takedown->effectN( affected_by.takedown.tick ).percent();

    if ( affected_by.wyverns_cry.tick )
      am *= 1 + p()->buffs.wyverns_cry->check_stack_value();

    return am;
  }

  double composite_crit_chance() const override
  {
    double cc = ab::composite_crit_chance();

    if ( affected_by.bullseye_crit_chance )
      cc += p()->buffs.bullseye->check_stack_value();

    return cc;
  }

  double composite_crit_damage_bonus_multiplier() const override
  {
    double cm = ab::composite_crit_damage_bonus_multiplier();

    if ( affected_by.trueshot_crit_damage_bonus && p()->buffs.trueshot->check() )
      cm *= 1 + p()->talents.trueshot->effectN( 4 ).percent();

    if ( affected_by.stargazer && p()->buffs.stargazer->check() )
      cm *= 1 + p()->buffs.stargazer->stack_value();

    return cm;
  }

  double composite_target_crit_damage_bonus_multiplier( player_t* target ) const override
  {
    double cm = ab::composite_target_crit_damage_bonus_multiplier( target );

    if ( affected_by.outland_venom )
      cm *= 1 + td( target )->debuffs.outland_venom->check_stack_value();

    return cm;
  }

  double composite_target_da_multiplier( player_t* target ) const override
  {
    double da = ab::composite_target_da_multiplier( target );

    if ( affected_by.unnatural_causes.direct )
    {
      da *= 1 + p()->talents.unnatural_causes->effectN( 1 ).percent();

      if ( target->health_percentage() < p()->talents.unnatural_causes->effectN( 3 ).base_value() )
        da *= 1.0476;
    }

    if ( affected_by.sentinels_mark.direct )
      da *= 1 + td( target )->debuffs.sentinels_mark->check_value();

    if ( affected_by.headshot.direct && td( target )->debuffs.headshot->check() )
      da *= 1 + td( target )->debuffs.headshot->stack_value();

    if ( p()->specialization() == HUNTER_BEAST_MASTERY 
      && affected_by.through_the_eyes.direct 
      && td( target )->dots.black_arrow->is_ticking() )
      da *= 1 + p()->talents.black_arrow_dot->effectN( 2 ).percent();

    return da;
  }

  double composite_target_ta_multiplier( player_t* target ) const override
  {
    double ta = ab::composite_target_ta_multiplier( target );

    if ( affected_by.unnatural_causes.tick )
    {
      ta *= 1 + p()->talents.unnatural_causes->effectN( 1 ).percent();

      if ( target->health_percentage() < p()->talents.unnatural_causes->effectN( 3 ).base_value() )
        ta *= 1.0476;
    }

    if ( affected_by.headshot.tick && td( target )->debuffs.headshot->check() )
      ta *= 1 + td( target )->debuffs.headshot->stack_value();

    if ( p()->specialization() == HUNTER_BEAST_MASTERY 
      && affected_by.through_the_eyes.tick 
      && td( target )->dots.black_arrow->is_ticking() )
      ta *= 1 + p()->talents.black_arrow_dot->effectN( 2 ).percent();

    return ta;
  }

  void tick( dot_t* dot ) override
  {
    ab::tick( dot );

    if ( p()->rng().roll( dire_beast_chance ) && p()->cooldowns.dire_beast->up() )
      p()->spawn_dire_beast( p()->talents.dire_beast_summon->duration() );
      p()->cooldowns.dire_beast->start();
  }

  void update_ready( timespan_t cd ) override
  {
    if ( cd_waste )
      cd_waste -> update_ready( this, cd );

    ab::update_ready( cd );
  }

  virtual double energize_cast_regen( const action_state_t* s ) const
  {
    const int num_targets = this -> n_targets();
    size_t targets_hit = 1;
    if ( ab::energize_type == action_energize::PER_HIT && ( num_targets == -1 || num_targets > 0 ) )
    {
      size_t tl_size = this -> target_list().size();
      targets_hit = ( num_targets < 0 ) ? tl_size : std::min( tl_size, as<size_t>( num_targets ) );
    }
    return targets_hit * this -> composite_energize_amount( s );
  }

  virtual double cast_regen( const action_state_t* s ) const
  {
    const timespan_t execute_time = this -> execute_time();
    const timespan_t cast_time = std::max( execute_time, this -> gcd() );
    const double regen = p() -> resource_regen_per_second( RESOURCE_FOCUS );

    double total_regen = regen * cast_time.total_seconds();
    double total_energize = energize_cast_regen( s );

    return total_regen + floor( total_energize );
  }

  // action list expressions
  std::unique_ptr<expr_t> create_expression( util::string_view name ) override
  {
    if ( util::str_compare_ci( name, "cast_regen" ) )
    {
      // Return the focus that will be regenerated during the cast time or GCD of the target action.
      return make_fn_expr( "cast_regen",
        [ this, state = std::unique_ptr<action_state_t>( this -> get_state() ) ] {
          this -> snapshot_state( state.get(), result_amount_type::NONE );
          state -> target = this -> target;
          return this -> cast_regen( state.get() );
        } );
    }

    // fudge wildfire bomb dot name
    auto splits = util::string_split<util::string_view>( name, "." );
    if ( splits.size() == 3 && splits[ 0 ] == "dot" && splits[ 1 ] == "wildfire_bomb" )
      return ab::create_expression( fmt::format( "dot.wildfire_bomb_dot.{}", splits[ 2 ] ) );

    return ab::create_expression( name );
  }

  void add_pet_stats( pet_t* pet, std::initializer_list<util::string_view> names )
  {
    if ( ! pet )
      return;

    for ( const auto& n : names )
    {
      stats_t* s = pet -> find_stats( n );
      if ( s )
        ab::stats -> add_child( s );
    }
  }

  bool trigger_buff( buff_t *const buff, timespan_t precast_time, timespan_t duration = timespan_t::min() ) const
  {
    const bool in_combat = ab::player -> in_combat;
    const bool triggered = buff -> trigger(duration);
    if ( triggered && ab::is_precombat && !in_combat && precast_time > 0_ms )
    {
      buff -> extend_duration( ab::player, -std::min( precast_time, buff -> buff_duration() ) );
      buff -> cooldown -> adjust( -precast_time );
    }
    return triggered;
  }

  void adjust_precast_cooldown( timespan_t precast_time ) const
  {
    const bool in_combat = ab::player -> in_combat;
    if ( ab::is_precombat && !in_combat && precast_time > 0_ms )
      ab::cooldown -> adjust( -precast_time );
  }

  player_t* get_random_valid_target( std::optional<int> aoe_override = std::nullopt ) const
  {
    const int aoe = aoe_override.value_or( ab::aoe );

    switch ( aoe )
    {
      case 0: 
        return ab::target;

      case -1:
      {
        const auto tl = ab::target_list();
        if ( !tl.empty() )
          return p()->rng().range( tl );

        break;
      }

      // Capped targets
      default:
      {
        const auto tl = ab::target_list();
        if ( !tl.empty() && aoe > 0 )
        {
          const size_t cap = std::min<size_t>( aoe, tl.size() );
          const size_t t   = p()->rng().template range<size_t>( 0, cap );
          return tl[ t ];
        }
        break;
      }
    }
    return ab::target;
  }
};

struct hunter_spell_t : public hunter_action_t<spell_t>
{
  hunter_spell_t( util::string_view n, hunter_t* p, const spell_data_t* s = spell_data_t::nil() ) : hunter_action_t( n, p, s ) {}
  bool usable_moving() const override { return true; }
};

struct hunter_ranged_attack_t : public hunter_action_t<ranged_attack_t>
{
  hunter_ranged_attack_t( util::string_view n, hunter_t* p, const spell_data_t* s = spell_data_t::nil() ) : hunter_action_t( n, p, s ) {}
  bool usable_moving() const override { return true; }
};

struct hunter_melee_attack_t : public hunter_action_t<melee_attack_t>
{
  hunter_melee_attack_t( util::string_view n, hunter_t* p, const spell_data_t* s = spell_data_t::nil() ) : hunter_action_t( n, p, s ) {}

  void init() override
  {
    hunter_action_t::init();

    if ( weapon )
    {
      const weapon_e group = weapon->group();
      if ( group != WEAPON_2H && group != WEAPON_1H && group != WEAPON_SMALL )
        background = true;
    }
  }
};

namespace pets
{
// ==========================================================================
// Hunter Pet
// ==========================================================================

struct hunter_pet_t: public pet_t
{
  struct buffs_t
  {
    buff_t* beast_cleave = nullptr;
  } buffs;

  struct actions_t
  {
    action_t* beast_cleave = nullptr;
  } actions;

  hunter_pet_t( hunter_t* owner, util::string_view pet_name, pet_e pt = PET_HUNTER, bool guardian = false, bool dynamic = false ) :
    pet_t( owner -> sim, owner, pet_name, pt, guardian, dynamic )
  {
    owner_coeff.ap_from_ap = 0.15;

    main_hand_weapon.type       = WEAPON_BEAST;
    main_hand_weapon.swing_time = 2_s;
  }

  void schedule_ready( timespan_t delta_time, bool waiting ) override
  {
    if ( main_hand_attack && !main_hand_attack->execute_event )
      main_hand_attack->schedule_execute();

    pet_t::schedule_ready( delta_time, waiting );
  }

  double composite_melee_attack_power() const override
  {
    double ap = pet_t::composite_melee_attack_power();

    return ap;
  }

  void create_buffs() override
  {
    pet_t::create_buffs();

    buffs.beast_cleave =
      make_buff( this, "beast_cleave", find_spell( 118455 ) )
      -> set_default_value( o()->talents.beast_cleave.ok() ? o() -> talents.beast_cleave -> effectN( 1 ).percent() : 1.0 );
  }

  hunter_t* o()             { return static_cast<hunter_t*>( owner ); }
  const hunter_t* o() const { return static_cast<hunter_t*>( owner ); }

  void init_spells() override;
};

static std::pair<timespan_t, int> dire_beast_duration( hunter_t* p, timespan_t base_duration )
{
  // Dire beast gets a chance for an extra attack based on haste
  // rather than discrete plateaus.  At integer numbers of attacks,
  // the beast actually has a 50% chance of n-1 attacks and 50%
  // chance of n.  It (apparently) scales linearly between n-0.5
  // attacks to n+0.5 attacks.  This uses beast duration to
  // effectively alter the number of attacks as the duration itself
  // isn't important and combat log testing shows some variation in
  // attack speeds.  This is not quite perfect but more accurate
  // than plateaus.
  const timespan_t swing_time       = 2_s * p->cache.auto_attack_speed();
  double partial_attacks_per_summon = base_duration / swing_time;
  int base_attacks_per_summon       = static_cast<int>( partial_attacks_per_summon );
  partial_attacks_per_summon -= static_cast<double>( base_attacks_per_summon );

  if ( p->rng().roll( partial_attacks_per_summon ) )
    base_attacks_per_summon += 1;

  return { base_attacks_per_summon * swing_time, base_attacks_per_summon };
}

// ==========================================================================
// Dark Minion (Corpsecaller)
// ==========================================================================

struct dark_minion_t final : public hunter_pet_t
{
  struct 
  {
    action_t* shoot          = nullptr;
    action_t* blighted_arrow = nullptr;
  } actions;

  dark_minion_t( hunter_t* owner, util::string_view n = "dark_minion" ) 
    : hunter_pet_t( owner, n, PET_HUNTER, true /* GUARDIAN */, true /* dynamic */ )
  {
    resource_regeneration = regen_type::DISABLED;
    owner_coeff.ap_from_ap = 1;
  }

  void update_stats() override
  {
    // 2026-01-25: Dark Minions only seem to inherit AP and Crit from the player.
    current_pet_stats.attack_power_from_ap = owner->composite_total_attack_power_by_type( owner->default_ap_type() ) * owner_coeff.ap_from_ap;
    sim->print_debug( "{} refreshed AP from owner (ap={})", name(), composite_melee_attack_power() );

    current_pet_stats.composite_melee_crit = owner->cache.attack_crit_chance();
    current_pet_stats.composite_spell_crit = owner->cache.spell_crit_chance();
    sim->print_debug( "{} refreshed Critical Strike from owner (crit={})", name(), current_pet_stats.composite_melee_crit, owner->cache.attack_crit_chance() );

    this->adjust_dynamic_cooldowns();
  }

  void init_action_list() override
  {
    pet_t::init_action_list();

    action_priority_list_t* def = get_action_priority_list( "default" );
    def->add_action( "shoot" );
  }

  void summon( timespan_t duration = 0_ms ) override
  {
    hunter_pet_t::summon( duration );

    o()->procs.dark_minion_spawn->occur();
  }

  void arise() override
  {
    pet_t::arise();

    /* 2026-01-25: Dark Minions don't cast Shoot for ~1.25s after they spawn.
                   Further log data required for more accurate range. */
    actions.shoot->cooldown->start( owner->rng().range( 1000_ms, 1500_ms ) );
  }

  void init_spells() override;

  action_t* create_action( util::string_view name, util::string_view options_str ) override;
};

// ==========================================================================
// Dire Critter
// ==========================================================================

struct dire_critter_t : public hunter_pet_t
{
  struct buffs_t
  {
    buff_t* bestial_wrath;
    buff_t* pet_damage;
  } buffs;

  struct actions_t
  {
    action_t* kill_command = nullptr;
  } actions;

  bool triggers_heart_of_the_pack = false;

  dire_critter_t( hunter_t* owner, util::string_view n = "dire_beast" )
    : hunter_pet_t( owner, n, PET_HUNTER, true /* GUARDIAN */, true /* dynamic */ )
  {
    resource_regeneration = regen_type::DISABLED;
  }

  // Used to trigger any behaviour that needs to run after base summon() but before auto attacks start...
  // for inheriting child classes.
  virtual void additional_summon_behavior() {};

  void create_buffs() override
  {
    hunter_pet_t::create_buffs();

    buffs.bestial_wrath =
      make_buff( this, "bestial_wrath", o()->talents.wildspeaker_bestial_wrath )
        ->set_default_value_from_effect( 1 );

    buffs.pet_damage = 
      make_buff( this, "pet_damage", o()->specs.pet_damage )
        ->set_default_value_from_effect_type( A_MOD_DAMAGE_PERCENT_DONE );
  }

  void summon( timespan_t duration = 0_ms ) override
  {
    hunter_pet_t::summon( duration );

    if ( o()->talents.dire_cleave.ok() )
      hunter_pet_t::buffs.beast_cleave->trigger( o()->talents.dire_cleave->effectN( 2 ).time_value() );

    if ( o()->talents.wildspeaker.ok() && o()->buffs.bestial_wrath->check() )
      buffs.bestial_wrath->trigger( o()->buffs.bestial_wrath->remains() );

    if ( triggers_heart_of_the_pack && o()->talents.heart_of_the_pack.ok() )
      o()->buffs.heart_of_the_pack->trigger();

    buffs.pet_damage->trigger();
    
    additional_summon_behavior();

    if ( main_hand_attack )
      main_hand_attack->execute();
  }

  double composite_player_multiplier( school_e school ) const override
  {
    double m = hunter_pet_t::composite_player_multiplier( school );

    if ( o()->talents.dire_frenzy.ok() )
      m *= 1 + o()->talents.dire_frenzy->effectN( 2 ).percent();

    if ( buffs.pet_damage->check() )
      m *= 1 + buffs.pet_damage->check_value();

    if ( buffs.bestial_wrath->has_common_school( school ) )
      m *= 1 + buffs.bestial_wrath->check_value();

    return m;
  }

  void init_spells() override;
};

// ==========================================================================
// Dark Hound (Corpsecaller)
// ==========================================================================

struct dark_hound_t final : public dire_critter_t
{
  struct
  {
    action_t* shadow_thrash = nullptr;
  } actions;

  dark_hound_t( hunter_t* owner, util::string_view n = "dark_hound" ) : dire_critter_t( owner, n )
  {
    resource_regeneration  = regen_type::DISABLED;
    owner_coeff.ap_from_ap = 1.5;
    auto_attack_multiplier = 4;
    triggers_heart_of_the_pack = true;
  }

  void summon( timespan_t duration = 0_ms ) override
  {
    dire_critter_t::summon( duration );

    o()->procs.dark_hound_spawn->occur();
  }

  void init_spells() override;
};

// ==========================================================================
// Dire Beast
// ==========================================================================

struct dire_beast_t final : public dire_critter_t
{
  dire_beast_t( hunter_t* owner, util::string_view n = "dire_beast" ) : dire_critter_t( owner, n )
  {
    // 11-10-22 Dire Beast - Damage increased by 400%. (15% -> 60%)
    // 13-10-22 Dire Beast damage increased by 50%. (60% -> 90%)
    // 22-7-24 Dire Beast damage increased by 10% (90% -> 100%)
    owner_coeff.ap_from_ap = 1;
    triggers_heart_of_the_pack = true;
  }

  void summon( timespan_t duration = 0_ms ) override
  {
    dire_critter_t::summon( duration );

    o()->procs.dire_beast_spawn->occur();
  }
};

// =========================================================================
// Fenryr
// =========================================================================

struct fenryr_td_t final : public actor_target_data_t
{
public:
  struct dots_t
  {
    dot_t* ravenous_leap = nullptr;
  } dots;

  fenryr_td_t( player_t* target, fenryr_t* p );
};

struct fenryr_t final : public dire_critter_t
{
  struct actions_t
  {
    action_t* ravenous_leap = nullptr;
  } actions;

  target_specific_t<fenryr_td_t> target_data;

  fenryr_t( hunter_t* owner, util::string_view n = "fenryr" ) : dire_critter_t( owner, n )
  {
    // 9-7-25 Hati and Fenryr base damage increased to about 2x of a normal Dire Beast's damage.
    owner_coeff.ap_from_ap = 2;
  }

  void summon( timespan_t duration = 0_ms ) override
  {
    dire_critter_t::summon( duration );

    actions.ravenous_leap->execute_on_target( target );
  }

  const fenryr_td_t* find_target_data( const player_t* target ) const override
  {
    return target_data[ target ];
  }

  fenryr_td_t* get_target_data( player_t* target ) const override
  {
    fenryr_td_t*& td = target_data[target];
    if ( !td )
      td = new fenryr_td_t( target, const_cast<fenryr_t*>( this ) );
    return td;
  }

  void init_spells() override;
};

// ==========================================================================
// Hati
// ==========================================================================

struct hati_t final : public dire_critter_t
{
  hati_t( hunter_t* owner, util::string_view n = "hati" ) : dire_critter_t( owner, n )
  {
   // 9-7-25 Hati and Fenryr base damage increased to about 2x of a normal Dire Beast's damage.
    owner_coeff.ap_from_ap = 2;
  }
};

// ==========================================================================
// Bear

// Guardian Druid APL — Midnight Season 1
// Source: https://www.wowhead.com/guide/classes/druid/guardian/rotation-cooldowns-pve-tank (2026-03-23)
// Covers: Druid of the Claw + Elune's Chosen hero talent paths
// Tier set: Sprouts of the Luminous Bloom (2pc: Maul/Raze/Ravage/Moonfire +10%, 4pc: proc interactions)

action_priority_list_t* precombat = get_action_priority_list( "precombat" );
action_priority_list_t* def = get_action_priority_list( "default" );
action_priority_list_t* cooldowns = get_action_priority_list( "cooldowns" );
action_priority_list_t* st = get_action_priority_list( "st" );
action_priority_list_t* aoe = get_action_priority_list( "aoe" );

// === Precombat ===
precombat->add_action( "bear_form,if=buff.bear_form.down","Ensure Bear Form before pull." );
precombat->add_action( "heart_of_the_wild" );

// === Default ===
def->add_action( "auto_attack","Executed every time the actor is available." );
def->add_action( "call_action_list,name=cooldowns" );
def->add_action( "call_action_list,name=aoe,if=active_enemies>=3" );
def->add_action( "call_action_list,name=st" );

// === Cooldowns ===
cooldowns->add_action( "use_items" );
cooldowns->add_action( "potion,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up" );
cooldowns->add_action( "blood_fury,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up" );
cooldowns->add_action( "berserking,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up" );
cooldowns->add_action( "fireblood,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up" );
cooldowns->add_action( "ancestral_call,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up" );
cooldowns->add_action( "incarnation","Use Incarnation/Berserk on cooldown." );
cooldowns->add_action( "berserk" );
cooldowns->add_action( "convoke_the_spirits,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up|cooldown.berserk_bear.remains>30","Convoke during Berserk/Incarnation if possible, otherwise don't hold." );
cooldowns->add_action( "lunar_beam" );
cooldowns->add_action( "barkskin","Use Barkskin as frequently as possible." );
cooldowns->add_action( "bristling_fur,if=rage<40","Generate rage when low." );

// === Single Target ===
st->add_action( "ironfur,if=!buff.ironfur.up|rage>=80","Maintain Ironfur; spend rage at 80+ to avoid capping." );
st->add_action( "moonfire,if=buff.galactic_guardian.up","Galactic Guardian procs: free Moonfire, high priority." );
st->add_action( "raze,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up","Raze replaces Maul during Berserk/Incarnation." );
st->add_action( "maul,if=buff.ravage.up","Ravage (DotC proc) — maul auto-fires ravage when buff is up. High priority with 4pc." );
st->add_action( "moonfire,if=dot.moonfire.remains<=gcd","Maintain Moonfire." );
st->add_action( "mangle","Mangle on cooldown — core rage generator." );
st->add_action( "thrash,if=dot.thrash.remains<=gcd|active_enemies>=2","Maintain Thrash, and use on 2+ targets." );
st->add_action( "maul,if=rage>=80","Maul as rage dump at 80+ (Harnessed Rage/Killing Blow synergy)." );
st->add_action( "moonfire,if=buff.galactic_guardian.up" );
st->add_action( "swipe_bear","Filler." );

// === AoE (3+ targets) ===
aoe->add_action( "ironfur,if=!buff.ironfur.up|rage>=80","Maintain Ironfur; avoid rage cap." );
aoe->add_action( "moonfire,if=buff.galactic_guardian.up","Galactic Guardian proc." );
aoe->add_action( "raze,if=buff.berserk_bear.up|buff.incarnation_guardian_of_ursoc.up","Raze replaces Maul in Berserk." );
aoe->add_action( "maul,if=buff.ravage.up","Ravage proc — maul auto-fires ravage when buff is up." );
aoe->add_action( "thrash","Thrash is the primary AoE ability." );
aoe->add_action( "moonfire,if=dot.moonfire.remains<=gcd&active_enemies<=5","Maintain Moonfire on reasonable target counts." );
aoe->add_action( "mangle","Mangle on cooldown." );
aoe->add_action( "maul,if=rage>=80","Rage dump." );
aoe->add_action( "swipe_bear","AoE filler." );

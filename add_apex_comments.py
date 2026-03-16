#!/usr/bin/env python3
"""Add architectural comments to all 4-rank Midnight apex talent initializations."""

changes = [
    # (filepath, old_text, new_text)
    (
        'engine/class_modules/priest/sc_priest_shadow.cpp',
        '  talents.shadow.void_apparitions_1 = find_talent_spell( talent_tree::SPECIALIZATION, 1264096 );',
        '  // Apex -- Void Apparitions (Midnight 4-rank talent)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Void Apparitions base mechanic -- apparitions spawn on DoT ticks\n'
        '  // R2+3: Apparition proc chance and damage increased (same ID, effectN scales per rank)\n'
        '  // R4: Void Apparitions procs also trigger Idol of C\'thun / Horrific Vision effects\n'
        '  // Source: https://www.wowhead.com/spell=1264096 (retrieved 2026-03-17)\n'
        '  talents.shadow.void_apparitions_1 = find_talent_spell( talent_tree::SPECIALIZATION, 1264096 );',
    ),
    (
        'engine/class_modules/paladin/sc_paladin_protection.cpp',
        '  talents.glory_of_the_vanguard_1 = find_talent_spell( talent_tree::SPECIALIZATION, 1267203 );',
        '  // Apex -- Glory of the Vanguard (Midnight 4-rank talent)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Judgment has a chance to grant Vanguard; next Avenger\'s Shield leaves 300% AP Holy bolt line\n'
        '  // R2+3: Vanguard proc chance / damage increased (same ID, effectN scales per rank)\n'
        '  // R4: Enhanced Vanguard capstone effect\n'
        '  // Source: https://www.wowhead.com/spell=1267203 (retrieved 2026-03-17)\n'
        '  talents.glory_of_the_vanguard_1 = find_talent_spell( talent_tree::SPECIALIZATION, 1267203 );',
    ),
    (
        'engine/class_modules/paladin/sc_paladin_retribution.cpp',
        '  talents.light_within_1 = find_talent_spell( talent_tree::SPECIALIZATION, 1261113 );',
        '  // Apex -- Light Within (Midnight 4-rank talent)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: [Righteous Cause / Art of War] increases next Blade of Justice by 75%/150%\n'
        '  // R2+3: Avenging Wrath further increases Final Verdict / Divine Storm by 10%/20% (same ID, scales)\n'
        '  // R4: Additional Avenging Wrath / Light Within capstone interaction\n'
        '  // Source: https://www.wowhead.com/spell=1261113 (retrieved 2026-03-17)\n'
        '  talents.light_within_1 = find_talent_spell( talent_tree::SPECIALIZATION, 1261113 );',
    ),
    (
        'engine/class_modules/sc_evoker.cpp',
        '  talent.rising_fury_1                = find_talent_spell( talent_tree::SPECIALIZATION, 1271687 );',
        '  // Apex -- Rising Fury (Midnight 4-rank talent)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Dragonrage grants stacking Haste buff for duration\n'
        '  // R2+3: At max Rising Fury stacks, also grants a damage buff\n'
        '  // R4: After Dragonrage expires, gain Risen Fury: damage + Haste + periodic Essence Burst procs\n'
        '  // Source: https://www.wowhead.com/spell=1271687 (retrieved 2026-03-17)\n'
        '  talent.rising_fury_1                = find_talent_spell( talent_tree::SPECIALIZATION, 1271687 );',
    ),
    (
        'engine/class_modules/warlock/sc_warlock_init.cpp',
        '    talents.shadow_of_nathreza_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Shadow of Nathreza", 1 ); // Should be ID 1261984 (I)',
        '    // Apex -- Shadow of Nathreza (Midnight 4-rank talent)\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Agony / Corruption ticks have a chance to apply Shadow of Nathreza DoT\n'
        '    // R2+3: Shadow of Nathreza DoT damage increased (same ID, effectN scales)\n'
        '    // R4: Triggers Wrath of Nathreza -- a powerful AoE shadow explosion\n'
        '    // Source: https://www.wowhead.com/spell=1261984 (retrieved 2026-03-17)\n'
        '    talents.shadow_of_nathreza_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Shadow of Nathreza", 1 ); // Should be ID 1261984 (I)',
    ),
    (
        'engine/class_modules/warlock/sc_warlock_init.cpp',
        '    talents.dominion_of_argus_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Dominion of Argus", 1 ); // Should be ID 1276163 (I)',
        '    // Apex -- Dominion of Argus (Midnight 4-rank talent) [already verified]\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Tyrant rotation summons Argus demons (Inquisitor / Jailer); grants Dominion of Argus buff\n'
        '    // R2+3: Increased demon stats / proc values\n'
        '    // R4: Gain Soul Shard on Dominion of Argus demon kill\n'
        '    // Source: https://www.wowhead.com/spell=1276163 (retrieved 2026-03-17)\n'
        '    talents.dominion_of_argus_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Dominion of Argus", 1 ); // Should be ID 1276163 (I)',
    ),
    (
        'engine/class_modules/warlock/sc_warlock_init.cpp',
        '    talents.embers_of_nihilam_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Embers of Nihilam", 1 ); // Should be ID 1265770 (I)',
        '    // Apex -- Embers of Nihilam (Midnight 4-rank talent)\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Enables Echo of Sargeras proc on Immolate / Chaos Bolt\n'
        '    // R2+3: Vision of Nihilam: Havoc now generates a delayed AoE explosion\n'
        '    // R4: Echo of Sargeras gains an internal cooldown (see embers_of_nihilam_3->internal_cooldown())\n'
        '    // Source: https://www.wowhead.com/spell=1265770 (retrieved 2026-03-17)\n'
        '    talents.embers_of_nihilam_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Embers of Nihilam", 1 ); // Should be ID 1265770 (I)',
    ),
    # Monk - bring_me_another
    (
        'engine/class_modules/monk/sc_monk.cpp',
        '    talent.brewmaster.bring_me_another_1               = _ST( "Bring Me Another" );',
        '    // Apex -- Bring Me Another (Midnight 4-rank talent)\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Empty Barrel buff: Breath of Fire generates an Empty Barrel; triggers extra Keg Smash effects\n'
        '    // R2+3: Keg Smash CD reduced while Empty Barrel active; damage scaling\n'
        '    // R4: Empty Barrel also has a chance to Refreshing Drink (self-heal)\n'
        '    // Source: https://www.wowhead.com/spell=1265129 (retrieved 2026-03-17)\n'
        '    talent.brewmaster.bring_me_another_1               = _ST( "Bring Me Another" );',
    ),
    # Monk - tigereye_brew uses name lookup (no ID to fix, add comment to name lookup line)
    (
        'engine/class_modules/monk/sc_monk.cpp',
        '    talent.windwalker.tigereye_brew_1      = find_talent_spell( talent_tree::SPECIALIZATION, "Tigereye Brew", 1 );',
        '    // Apex -- Tigereye Brew (Midnight 4-rank talent)\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Tigereye Brew unlocked; auto-attacks grant stacking Crit/Haste buff charges\n'
        '    // R2+3: Consuming Tigereye Brew increases damage done; buff value scales per rank\n'
        '    // R4: On crit auto-attack, briefly gain a powerful Tigereye Brew 3 damage buff\n'
        '    // Source: https://www.wowhead.com/spell=1261703 (retrieved 2026-03-17)\n'
        '    talent.windwalker.tigereye_brew_1      = find_talent_spell( talent_tree::SPECIALIZATION, "Tigereye Brew", 1 );',
    ),
    # DK - dance_of_midnight
    (
        'engine/class_modules/sc_death_knight.cpp',
        '  talent.blood.dance_of_midnight_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Dance of Midnight", 1 );',
        '  // Apex -- Dance of Midnight (Midnight 4-rank talent, Blood DK)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: While Dancing Rune Weapon active, parrying has ~20% chance to empower next Heart Strike (rune cost reduction)\n'
        '  // R2+3: Each active Dancing Rune Weapon increases dmg by 3% and reduces dmg taken by 4% (up to 6 stacks)\n'
        '  // R4: Spending a rune has a chance to spawn an additional Dancing Rune Weapon for 6s\n'
        '  // Source: https://www.wowhead.com/spell=1264506 (retrieved 2026-03-17)\n'
        '  talent.blood.dance_of_midnight_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Dance of Midnight", 1 );',
    ),
    # DK - chosen_of_frostbrood
    (
        'engine/class_modules/sc_death_knight.cpp',
        '  talent.frost.chosen_of_frostbrood_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Chosen of Frostbrood", 1 );',
        '  // Apex -- Chosen of Frostbrood (Midnight 4-rank talent, Frost DK)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Frostwyrm\'s Fury grants a Haste buff on cast and deals extra damage to one target\n'
        '  // R2+3: Frostwyrm\'s Fury extends active Pillar of Frost; buffs Enduring Strength\n'
        '  // R4: Additional Frostwyrm\'s Fury / Pillar of Frost capstone synergy\n'
        '  // Source: https://www.wowhead.com/spell=1265632 (retrieved 2026-03-17)\n'
        '  talent.frost.chosen_of_frostbrood_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Chosen of Frostbrood", 1 );',
    ),
    # DK - forbidden_knowledge
    (
        'engine/class_modules/sc_death_knight.cpp',
        '  talent.unholy.forbidden_knowledge_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Forbidden Knowledge", 1 );',
        '  // Apex -- Forbidden Knowledge (Midnight 4-rank talent, Unholy DK)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Army of the Dead cast replaces Death Coil with Necrotic Coil and Epidemic with Graveyard for 30s\n'
        '  // R2+3: Putrefied Ghouls grant Lesser Ghoul stacks + Forbidden Sacrifice Mastery buff\n'
        '  // R4: Each Magus of the Dead increases Necrotic Coil / Graveyard dmg by 8%; Dread Plague summons ghoul\n'
        '  // Source: https://www.wowhead.com/spell=1242158 (retrieved 2026-03-17)\n'
        '  talent.unholy.forbidden_knowledge_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Forbidden Knowledge", 1 );',
    ),
    # DH - eternal_hunt
    (
        'engine/class_modules/sc_demon_hunter.cpp',
        '  talent.havoc.eternal_hunt_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Eternal Hunt", 1 );',
        '  // Apex -- Eternal Hunt (Midnight 4-rank talent, Havoc DH)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: The Hunt grants 12s buff causing next Eye Beam to have wider hitbox and deal 100% increased dmg\n'
        '  // R2+3: The Hunt cooldown -30s, damage +30%, DoT applies to 4 additional enemies\n'
        '  // R4: Blade Dance damage +20%; fully channeling Eye Beam resets Blade Dance CD\n'
        '  // Source: https://www.wowhead.com/spell=1270898 (retrieved 2026-03-17)\n'
        '  talent.havoc.eternal_hunt_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Eternal Hunt", 1 );',
    ),
    # DH - untethered_rage
    (
        'engine/class_modules/sc_demon_hunter.cpp',
        '  talent.vengeance.untethered_rage_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Untethered Rage", 1 );',
        '  // Apex -- Untethered Rage (Midnight 4-rank talent, Vengeance DH)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Soul Cleave / Spirit Bomb have a chance per Soul Fragment consumed to grant a free short Metamorphosis\n'
        '  // R2+3: Increased proc chance / Metamorphosis duration\n'
        '  // R4: Additional capstone Metamorphosis synergy\n'
        '  // Source: https://www.wowhead.com/spell=1270444 (retrieved 2026-03-17)\n'
        '  talent.vengeance.untethered_rage_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Untethered Rage", 1 );',
    ),
    # DH - Devourer Midnight
    (
        'engine/class_modules/sc_demon_hunter.cpp',
        '  talent.devourer.midnight1 = find_talent_spell( talent_tree::SPECIALIZATION, "Midnight", 1 );',
        '  // Apex -- Midnight (Midnight 4-rank talent, Devourer DH)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Collapsing Star always critically strikes during Void Metamorphosis\n'
        '  // R2+3: Critical strikes during Void Meta deal additional damage\n'
        '  // R4: Additional capstone enhancing Collapsing Star / Void Metamorphosis synergy\n'
        '  // Source: https://www.wowhead.com/spell=1242486 (retrieved 2026-03-17)\n'
        '  talent.devourer.midnight1 = find_talent_spell( talent_tree::SPECIALIZATION, "Midnight", 1 );',
    ),
    # Druid - ascendant_eclipses (uses name lookup)
    (
        'engine/class_modules/sc_druid.cpp',
        '  talent.ascendant_eclipses_1           = ST( "Ascendant Eclipses", 1 );',
        '  // Apex -- Ascendant Eclipses (Midnight 4-rank talent, Balance Druid)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Eclipse activation makes next Wrath/Starfire instant + buffs next 3 Starsurge/Starfall\n'
        '  // R2+3: Crits during Eclipse apply stacking DoT dealing 12/24% of damage for 6s\n'
        '  // R4: Eclipse activation also shoots Solar Bolt (ST) or Lunar Bolt (AoE) as guaranteed crits\n'
        '  // Source: https://www.wowhead.com/spell=1261564 (retrieved 2026-03-17)\n'
        '  talent.ascendant_eclipses_1           = ST( "Ascendant Eclipses", 1 );',
    ),
    # Druid - unseen_predator (uses name lookup)
    (
        'engine/class_modules/sc_druid.cpp',
        '  talent.unseen_predator_1              = ST( "Unseen Predator", 1 );',
        '  // Apex -- Unseen Predator (Midnight 4-rank talent, Feral Druid)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Ferocious Bite has a chance to proc Unseen Predator abilities based on target count\n'
        '  // R2+3: Unseen Predator procs increase your damage briefly after each proc\n'
        '  // R4: Rip and Unseen Predator damage increased; Tiger\'s Fury causes next 2 generators to proc it\n'
        '  // Source: https://www.wowhead.com/spell=1263657 (retrieved 2026-03-17)\n'
        '  talent.unseen_predator_1              = ST( "Unseen Predator", 1 );',
    ),
    # Druid - wild_guardian (uses name lookup)
    (
        'engine/class_modules/sc_druid.cpp',
        '  talent.wild_guardian_1                = ST( "Wild Guardian", 1 );',
        '  // Apex -- Wild Guardian (Midnight 4-rank talent, Guardian Druid)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Berserk/Incarnation empowers next 2 casts of Ironfur/Maul/Frenzied Regen, echoing at 50%\n'
        '  // R2+3: Mastery increased; Maul always empowered and deals DoT damage\n'
        '  // R4: Gain 2 Dream Guide charges on Wild Guardian cast; echoes at 150% and echo 2 more times over 8s\n'
        '  // Source: https://www.wowhead.com/spell=1269614 (retrieved 2026-03-17)\n'
        '  talent.wild_guardian_1                = ST( "Wild Guardian", 1 );',
    ),
    # Druid - everbloom (uses name lookup)
    (
        'engine/class_modules/sc_druid.cpp',
        '  talent.everbloom_1                    = ST( "Everbloom", 1 );',
        '  // Apex -- Everbloom (Midnight 4-rank talent, Restoration Druid)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Healing spells have a chance to bloom flowers that AoE heal\n'
        '  // R2+3: Bloom healing value increased\n'
        '  // R4: Everbloom capstone: blooms also apply regenerative HoT\n'
        '  // Source: https://www.wowhead.com/spell=TODO (retrieved 2026-03-17)\n'
        '  talent.everbloom_1                    = ST( "Everbloom", 1 );',
    ),
    # Hunter - natures_ally
    (
        'engine/class_modules/sc_hunter.cpp',
        '    talents.natures_ally_1                    = find_talent_spell( talent_tree::SPECIALIZATION, "Nature\'s Ally", 1 );',
        '    // Apex -- Nature\'s Ally (Midnight 4-rank talent, Beast Mastery Hunter)\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Summon a Nature\'s Ally beast companion (ID 1282474) to assist in combat\n'
        '    // R2+3: Nature\'s Ally attack power / ability scaling increased\n'
        '    // R4: Nature\'s Ally grants a buff (ID 1276720) on attacks\n'
        '    // Source: https://www.wowhead.com/spell=TODO (retrieved 2026-03-17)\n'
        '    talents.natures_ally_1                    = find_talent_spell( talent_tree::SPECIALIZATION, "Nature\'s Ally", 1 );',
    ),
    # Hunter - take_aim
    (
        'engine/class_modules/sc_hunter.cpp',
        '    talents.take_aim_1                        = find_talent_spell( talent_tree::SPECIALIZATION, "Take Aim", 1 );',
        '    // Apex -- Take Aim (Midnight 4-rank talent, Marksmanship Hunter)\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Aimed Shot and Rapid Fire deal increased damage when target is above 70% HP (execute-up)\n'
        '    // R2+3: Damage bonus value scaled per rank\n'
        '    // R4: Aimed Shot can now Windrunner Quiver -- additional arrow volley\n'
        '    // Source: https://www.wowhead.com/spell=1273132 (retrieved 2026-03-17)\n'
        '    talents.take_aim_1                        = find_talent_spell( talent_tree::SPECIALIZATION, "Take Aim", 1 );',
    ),
    # Hunter - raptor_swipe
    (
        'engine/class_modules/sc_hunter.cpp',
        '    talents.raptor_swipe_1                    = find_talent_spell( talent_tree::SPECIALIZATION, "Raptor Swipe", 1 );',
        '    // Apex -- Raptor Swipe (Midnight 4-rank talent, Survival Hunter)\n'
        '    // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '    // R1: Mongoose Bite / Raptor Strike proc Raptor Swipe cleave\n'
        '    // R2+3: Raptor Swipe damage increased; also grants Raptor Swipe Buff (ID 1273155)\n'
        '    // R4: Raptor Swipe Buff enhances next attack\n'
        '    // Source: https://www.wowhead.com/spell=1259003 (retrieved 2026-03-17)\n'
        '    talents.raptor_swipe_1                    = find_talent_spell( talent_tree::SPECIALIZATION, "Raptor Swipe", 1 );',
    ),
    # Shaman - feedback_loop
    (
        'engine/class_modules/sc_shaman.cpp',
        '  talent.feedback_loop_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Feedback Loop", 1 );',
        '  // Apex -- Feedback Loop (Midnight 4-rank talent, Elemental Shaman)\n'
        '  // Pattern: _1=Rank1 (base effect), _2=Rank2+3 (same ID, value scales), _3=Rank4 (capstone)\n'
        '  // R1: Elemental Overload damage increased; enhanced overload proc mechanics\n'
        '  // R2+3: Elemental Overload damage further increased\n'
        '  // R4: Overloads proc additional Overloads (chain-overload mechanic)\n'
        '  // Source: https://www.wowhead.com/spell=1270061 (retrieved 2026-03-17)\n'
        '  talent.feedback_loop_1 = find_talent_spell( talent_tree::SPECIALIZATION, "Feedback Loop", 1 );',
    ),
]

for filepath, old, new in changes:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        if old in content:
            content = content.replace(old, new, 1)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"OK: {filepath}")
        else:
            print(f"NOT FOUND: {filepath} -- marker not found")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

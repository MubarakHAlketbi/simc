#!/usr/bin/env python3
"""
Generate APL diff report comparing Wowhead rotation guides to SimC APLs.
Uses .md files for cleaner parsing.
"""
import json
import re
import os
from pathlib import Path

BASE = Path("/home/mubarak/simc")
WOWHEAD = BASE / "wowhead"
APL_DIR = BASE / "engine/class_modules/apl"
PROFILES = BASE / "profiles/MID1"

# Spell name mapping from Wowhead display names to SimC action names
SPELL_MAP = {
    # Death Knight - Blood
    "Death Strike": "death_strike",
    "Marrowrend": "marrowrend",
    "Blood Boil": "blood_boil",
    "Dancing Rune Weapon": "dancing_rune_weapon",
    "Heart Strike": "heart_strike",
    "Consumption": "consumption",
    "Tombstone": "tombstone",
    "Bonestorm": "bonestorm",
    "Vampiric Blood": "vampiric_blood",
    "Abomination Limb": "abomination_limb",
    "Blood Tap": "blood_tap",
    "Death and Decay": "death_and_decay",
    "Reaper's Mark": "reapers_mark",
    "Death's Caress": "deaths_caress",
    "Vampiric Strike": "vampiric_strike",
    "Bone Shield": "marrowrend",
    # Death Knight - Frost
    "Obliterate": "obliterate",
    "Howling Blast": "howling_blast",
    "Frost Strike": "frost_strike",
    "Remorseless Winter": "remorseless_winter",
    "Empower Rune Weapon": "empower_rune_weapon",
    "Pillar of Frost": "pillar_of_frost",
    "Frostwyrm's Fury": "frostwyrms_fury",
    "Glacial Advance": "glacial_advance",
    "Chains of Ice": "chains_of_ice",
    "Chill Streak": "chill_streak",
    "Horn of Winter": "horn_of_winter",
    "Soul Reaper": "soul_reaper",
    "Breath of Sindragosa": "breath_of_sindragosa",
    "Frostscythe": "frostscythe",
    # Death Knight - Unholy
    "Festering Strike": "festering_strike",
    "Scourge Strike": "scourge_strike",
    "Apocalypse": "apocalypse",
    "Army of the Dead": "army_of_the_dead",
    "Dark Transformation": "dark_transformation",
    "Death Coil": "death_coil",
    "Epidemic": "epidemic",
    "Unholy Assault": "unholy_assault",
    "Raise Dead": "raise_dead",
    "Defile": "defile",
    "Outbreak": "outbreak",
    "Necrotic Coil": "death_coil",
    "Summon Gargoyle": "summon_gargoyle",
    # Demon Hunter - Havoc
    "Immolation Aura": "immolation_aura",
    "Chaos Strike": "chaos_strike",
    "Blade Dance": "blade_dance",
    "Eye Beam": "eye_beam",
    "Metamorphosis": "metamorphosis",
    "Death Sweep": "death_sweep",
    "Annihilation": "annihilation",
    "Throw Glaive": "throw_glaive",
    "Glaive Tempest": "glaive_tempest",
    "Essence Break": "essence_break",
    "The Hunt": "the_hunt",
    "Fel Rush": "fel_rush",
    "Sigil of Flame": "sigil_of_flame",
    "Vengeful Retreat": "vengeful_retreat",
    "Demon Blades": "throw_glaive",
    # Demon Hunter - Vengeance
    "Fel Devastation": "fel_devastation",
    "Spirit Bomb": "spirit_bomb",
    "Fracture": "fracture",
    "Soul Cleave": "soul_cleave",
    "Infernal Strike": "infernal_strike",
    "Fiery Brand": "fiery_brand",
    "Demon Spikes": "demon_spikes",
    "Felblade": "felblade",
    # Druid - Balance
    "Starsurge": "starsurge",
    "Starfall": "starfall",
    "Wrath": "wrath",
    "Starfire": "starfire",
    "Sunfire": "sunfire",
    "Moonfire": "moonfire",
    "Celestial Alignment": "celestial_alignment",
    "Incarnation: Chosen of Elune": "incarnation_chosen_of_elune",
    "Incarnation": "incarnation_chosen_of_elune",
    "Force of Nature": "force_of_nature",
    "Stellar Flare": "stellar_flare",
    "Fury of Elune": "fury_of_elune",
    "New Moon": "new_moon",
    "Half Moon": "half_moon",
    "Full Moon": "full_moon",
    "Orbital Strike": "orbital_strike",
    "Wild Mushroom": "wild_mushroom",
    # Druid - Feral
    "Rip": "rip",
    "Ferocious Bite": "ferocious_bite",
    "Rake": "rake",
    "Shred": "shred",
    "Tiger's Fury": "tigers_fury",
    "Berserk": "berserk",
    "Thrash": "thrash_cat",
    "Swipe": "swipe_cat",
    "Brutal Slash": "brutal_slash",
    "Primal Wrath": "primal_wrath",
    "Convoke the Spirits": "convoke_the_spirits",
    "Feral Frenzy": "feral_frenzy",
    "Adaptive Swarm": "adaptive_swarm",
    # Druid - Guardian
    "Mangle": "mangle",
    "Ironfur": "ironfur",
    "Frenzied Regeneration": "frenzied_regeneration",
    "Maul": "maul",
    "Pulverize": "pulverize",
    "Incarnation: Guardian of Ursoc": "incarnation_guardian_of_ursoc",
    "Berserk: Bear Form": "berserk",
    "Berserk: Ravage": "berserk",
    "Ravage": "maul",
    "Raze": "maul",
    # Evoker - Devastation
    "Dragonrage": "dragonrage",
    "Fire Breath": "fire_breath",
    "Eternity Surge": "eternity_surge",
    "Pyre": "pyre",
    "Living Flame": "living_flame",
    "Disintegrate": "disintegrate",
    "Deep Breath": "deep_breath",
    "Shattering Star": "shattering_star",
    "Azure Strike": "azure_strike",
    "Firestorm": "firestorm",
    # Evoker - Augmentation
    "Ebon Might": "ebon_might",
    "Breath of Eons": "breath_of_eons",
    "Upheaval": "upheaval",
    "Prescience": "prescience",
    "Blistering Scales": "blistering_scales",
    "Eruption": "eruption",
    "Shifting Sands": "shifting_sands",
    "Tip the Scales": "tip_the_scales",
    "Spatial Paradox": "spatial_paradox",
    "Temporal Anomaly": "temporal_anomaly",
    # Hunter - Beast Mastery
    "Kill Command": "kill_command",
    "Bestial Wrath": "bestial_wrath",
    "A Murder of Crows": "a_murder_of_crows",
    "Barbed Shot": "barbed_shot",
    "Multi-Shot": "multishot",
    "Multishot": "multishot",
    "Cobra Shot": "cobra_shot",
    "Dire Beast": "dire_beast",
    "Stampede": "stampede",
    "Aspect of the Wild": "aspect_of_the_wild",
    "Call of the Wild": "call_of_the_wild",
    "Barrage": "barrage",
    "Bloodshed": "bloodshed",
    # Hunter - Marksmanship
    "Aimed Shot": "aimed_shot",
    "Rapid Fire": "rapid_fire",
    "Arcane Shot": "arcane_shot",
    "Trueshot": "trueshot",
    "Steady Shot": "steady_shot",
    "Chimaera Shot": "chimaera_shot",
    "Black Arrow": "black_arrow",
    "Volley": "volley",
    "Explosive Shot": "explosive_shot",
    "Salvo": "salvo",
    # Hunter - Survival
    "Wildfire Bomb": "wildfire_bomb",
    "Raptor Strike": "raptor_strike",
    "Flanking Strike": "flanking_strike",
    "Mongoose Bite": "mongoose_bite",
    "Coordinated Assault": "coordinated_assault",
    "Serpent Sting": "serpent_sting",
    "Carve": "carve",
    "Butchery": "butchery",
    "Spearhead": "spearhead",
    "Fury of the Eagle": "fury_of_the_eagle",
    "Kill Shot": "kill_shot",
    # Mage - Arcane
    "Arcane Blast": "arcane_blast",
    "Arcane Missiles": "arcane_missiles",
    "Arcane Barrage": "arcane_barrage",
    "Arcane Surge": "arcane_surge",
    "Arcane Orb": "arcane_orb",
    "Touch of the Magi": "touch_of_the_magi",
    "Evocation": "evocation",
    "Radiant Spark": "radiant_spark",
    "Nether Tempest": "nether_tempest",
    "Arcane Explosion": "arcane_explosion",
    "Presence of Mind": "presence_of_mind",
    "Shifting Power": "shifting_power",
    # Mage - Fire
    "Pyroblast": "pyroblast",
    "Fireball": "fireball",
    "Fire Blast": "fire_blast",
    "Phoenix Flames": "phoenix_flames",
    "Combustion": "combustion",
    "Flamestrike": "flamestrike",
    "Scorch": "scorch",
    "Dragon's Breath": "dragons_breath",
    "Living Bomb": "living_bomb",
    "Meteor": "meteor",
    "Searing Touch": "scorch",
    # Mage - Frost
    "Frostbolt": "frostbolt",
    "Ice Lance": "ice_lance",
    "Frozen Orb": "frozen_orb",
    "Blizzard": "blizzard",
    "Flurry": "flurry",
    "Icy Veins": "icy_veins",
    "Comet Storm": "comet_storm",
    "Glacial Spike": "glacial_spike",
    "Ice Nova": "ice_nova",
    "Ray of Frost": "ray_of_frost",
    "Ebonbolt": "ebonbolt",
    # Monk - Brewmaster
    "Keg Smash": "keg_smash",
    "Breath of Fire": "breath_of_fire",
    "Blackout Kick": "blackout_kick",
    "Tiger Palm": "tiger_palm",
    "Celestial Brew": "celestial_brew",
    "Purifying Brew": "purifying_brew",
    "Exploding Keg": "exploding_keg",
    "Chi Burst": "chi_burst",
    "Invoke Niuzao": "invoke_niuzao_the_black_ox",
    "Invoke Niuzao, the Black Ox": "invoke_niuzao_the_black_ox",
    "Rushing Jade Wind": "rushing_jade_wind",
    # Monk - Windwalker
    "Rising Sun Kick": "rising_sun_kick",
    "Fists of Fury": "fists_of_fury",
    "Strike of the Windlord": "strike_of_the_windlord",
    "Whirling Dragon Punch": "whirling_dragon_punch",
    "Spinning Crane Kick": "spinning_crane_kick",
    "Touch of Death": "touch_of_death",
    "Storm, Earth, and Fire": "storm_earth_and_fire",
    "Invoke Xuen": "invoke_xuen_the_white_tiger",
    "Invoke Xuen, the White Tiger": "invoke_xuen_the_white_tiger",
    "Serenity": "serenity",
    "Jadefire Stomp": "jadefire_stomp",
    # Paladin - Protection
    "Shield of the Righteous": "shield_of_the_righteous",
    "Avenger's Shield": "avengers_shield",
    "Judgment": "judgment",
    "Hammer of Wrath": "hammer_of_wrath",
    "Consecration": "consecration",
    "Guardian of Ancient Kings": "guardian_of_ancient_kings",
    "Avenging Wrath": "avenging_wrath",
    "Hammer of the Righteous": "hammer_of_the_righteous",
    "Word of Glory": "word_of_glory",
    "Blessed Hammer": "blessed_hammer",
    "Divine Toll": "divine_toll",
    "Holy Armaments": "holy_armaments",
    "Ardent Defender": "ardent_defender",
    # Paladin - Retribution
    "Templar's Verdict": "templars_verdict",
    "Divine Storm": "divine_storm",
    "Wake of Ashes": "wake_of_ashes",
    "Blade of Justice": "blade_of_justice",
    "Final Reckoning": "final_reckoning",
    "Execution Sentence": "execution_sentence",
    "Crusader Strike": "crusader_strike",
    "Templar Strikes": "crusader_strike",
    "Divine Hammer": "divine_hammer",
    "Expurgation": "blade_of_justice",
    "Holy Prism": "holy_prism",
    # Priest - Shadow
    "Void Bolt": "void_bolt",
    "Mind Blast": "mind_blast",
    "Shadow Word: Pain": "shadow_word_pain",
    "Vampiric Touch": "vampiric_touch",
    "Mind Flay": "mind_flay",
    "Void Eruption": "void_eruption",
    "Devouring Plague": "devouring_plague",
    "Shadow Crash": "shadow_crash",
    "Shadowfiend": "shadowfiend",
    "Mindbender": "mindbender",
    "Dark Ascension": "dark_ascension",
    "Void Torrent": "void_torrent",
    "Mindgames": "mindgames",
    "Inescapable Torment": "mindbender",
    "Idol of C'Thun": "void_bolt",
    "Mind Spike": "mind_spike",
    # Rogue - Assassination
    "Mutilate": "mutilate",
    "Envenom": "envenom",
    "Garrote": "garrote",
    "Rupture": "rupture",
    "Shiv": "shiv",
    "Deathmark": "deathmark",
    "Exsanguinate": "exsanguinate",
    "Fan of Knives": "fan_of_knives",
    "Kingsbane": "kingsbane",
    "Crimson Tempest": "crimson_tempest",
    "Serrated Bone Spike": "serrated_bone_spike",
    "Echoing Reprimand": "echoing_reprimand",
    "Indiscriminate Carnage": "garrote",
    # Rogue - Outlaw
    "Between the Eyes": "between_the_eyes",
    "Dispatch": "dispatch",
    "Pistol Shot": "pistol_shot",
    "Roll the Bones": "roll_the_bones",
    "Slice and Dice": "slice_and_dice",
    "Blade Flurry": "blade_flurry",
    "Blade Rush": "blade_rush",
    "Ambush": "ambush",
    "Ghostly Strike": "ghostly_strike",
    "Dreadblades": "dreadblades",
    "Keep it Rolling": "keep_it_rolling",
    "Sinister Strike": "sinister_strike",
    "Adrenaline Rush": "adrenaline_rush",
    # Rogue - Subtlety
    "Shadow Dance": "shadow_dance",
    "Backstab": "backstab",
    "Shadowstrike": "shadowstrike",
    "Eviscerate": "eviscerate",
    "Symbols of Death": "symbols_of_death",
    "Black Powder": "black_powder",
    "Secret Technique": "secret_technique",
    "Shadow Blades": "shadow_blades",
    "Shuriken Storm": "shuriken_storm",
    "Shuriken Toss": "shuriken_toss",
    "Flagellation": "flagellation",
    "Gloomblade": "gloomblade",
    "Shuriken Tornado": "shuriken_tornado",
    # Shaman - Elemental
    "Lava Burst": "lava_burst",
    "Earthquake": "earthquake",
    "Earth Shock": "earth_shock",
    "Elemental Blast": "elemental_blast",
    "Storm Elemental": "storm_elemental",
    "Fire Elemental": "fire_elemental",
    "Primordial Wave": "primordial_wave",
    "Lightning Bolt": "lightning_bolt",
    "Chain Lightning": "chain_lightning",
    "Icefury": "icefury",
    "Frost Shock": "frost_shock",
    "Stormkeeper": "stormkeeper",
    "Ascendance": "ascendance",
    "Liquid Magma Totem": "liquid_magma_totem",
    "Tempest": "lightning_bolt",
    # Shaman - Enhancement
    "Stormstrike": "stormstrike",
    "Lava Lash": "lava_lash",
    "Crash Lightning": "crash_lightning",
    "Feral Spirit": "feral_spirit",
    "Flametongue Weapon": "flametongue_weapon",
    "Windfury Weapon": "windfury_weapon",
    "Windstrike": "windstrike",
    "Doom Winds": "doom_winds",
    "Ice Strike": "ice_strike",
    "Fire Nova": "fire_nova",
    "Sundering": "sundering",
    # Warlock - Affliction
    "Haunt": "haunt",
    "Agony": "agony",
    "Wither": "wither",
    "Corruption": "corruption",
    "Unstable Affliction": "unstable_affliction",
    "Summon Darkglare": "summon_darkglare",
    "Dark Harvest": "dark_harvest",
    "Malevolence": "malevolence",
    "Malefic Grasp": "malefic_grasp",
    "Drain Soul": "drain_soul",
    "Shadow Bolt": "shadow_bolt",
    "Seed of Corruption": "seed_of_corruption",
    # Warlock - Demonology
    "Call Dreadstalkers": "call_dreadstalkers",
    "Hand of Gul'dan": "hand_of_guldan",
    "Demonbolt": "demonbolt",
    "Grimoire: Felguard": "grimoire_felguard",
    "Summon Demonic Tyrant": "summon_demonic_tyrant",
    "Bilescourge Bombers": "bilescourge_bombers",
    "Doom": "doom",
    "Power Siphon": "power_siphon",
    "Nether Portal": "nether_portal",
    "Summon Vilefiend": "summon_vilefiend",
    "Implosion": "implosion",
    "Soul Strike": "soul_strike",
    "Demonic Strength": "demonic_strength",
    # Warlock - Destruction
    "Chaos Bolt": "chaos_bolt",
    "Rain of Fire": "rain_of_fire",
    "Cataclysm": "cataclysm",
    "Havoc": "havoc",
    "Channel Demonfire": "channel_demonfire",
    "Summon Infernal": "summon_infernal",
    "Dimensional Rift": "dimensional_rift",
    "Conflagrate": "conflagrate",
    "Immolate": "immolate",
    "Incinerate": "incinerate",
    "Shadowburn": "shadowburn",
    # Warrior - Arms
    "Mortal Strike": "mortal_strike",
    "Overpower": "overpower",
    "Colossus Smash": "colossus_smash",
    "Warbreaker": "warbreaker",
    "Bladestorm": "bladestorm",
    "Execute": "execute",
    "Cleave": "cleave",
    "Slam": "slam",
    "Ravager": "ravager",
    "Avatar": "avatar",
    "Sweeping Strikes": "sweeping_strikes",
    "Skullsplitter": "skullsplitter",
    "Rend": "rend",
    "Heroic Strike": "heroic_strike",
    "Demolish": "demolish",
    "Wrecking Throw": "wrecking_throw",
    "Champion's Spear": "champions_spear",
    # Warrior - Fury
    "Rampage": "rampage",
    "Bloodthirst": "bloodthirst",
    "Raging Blow": "raging_blow",
    "Onslaught": "onslaught",
    "Whirlwind": "whirlwind",
    "Recklessness": "recklessness",
    "Crushing Blow": "crushing_blow",
    "Odyn's Fury": "odyns_fury",
    "Siegebreaker": "siegebreaker",
    "Thunderous Roar": "thunderous_roar",
    "Spear of Bastion": "spear_of_bastion",
    # Warrior - Protection
    "Shield Slam": "shield_slam",
    "Thunder Clap": "thunder_clap",
    "Revenge": "revenge",
    "Shield Block": "shield_block",
    "Demoralizing Shout": "demoralizing_shout",
    "Last Stand": "last_stand",
    "Ignore Pain": "ignore_pain",
    "Shockwave": "shockwave",
    "Spell Reflection": "spell_reflection",
    "Devastate": "devastate",
    "Thunder Blast": "thunder_blast",
}


def extract_md_priority_steps(md_content, section_name_variants):
    """
    Parse .md file and extract priority steps for a given section.
    Returns dict: {hero_name: {tab_name: [spells]}}
    """
    result = {}
    
    lines = md_content.split('\n')
    current_hero = None
    current_tab = None
    in_priority = False
    in_section = False
    priority_lines = []
    
    # Mapping of variant names to standard names
    tab_map = {}
    for variants in section_name_variants:
        for v in variants:
            tab_map[v.lower()] = variants[0]  # canonical name
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect hero talent section
        if line.startswith('## Hero Talent: '):
            current_hero = line[len('## Hero Talent: '):].strip()
            if current_hero not in result:
                result[current_hero] = {}
            current_tab = None
            in_priority = False
            in_section = False
        
        # Detect tab name (#### level)
        elif line.startswith('#### '):
            tab_name = line[5:].strip()
            canonical = tab_map.get(tab_name.lower())
            if canonical:
                current_tab = canonical
                in_section = True
                in_priority = False
                if current_hero and current_tab not in result.get(current_hero, {}):
                    if current_hero:
                        result[current_hero][current_tab] = []
            else:
                in_section = False
                current_tab = None
        
        # Detect PRIORITY block
        elif line.strip() == 'PRIORITY' and in_section and current_hero and current_tab:
            in_priority = True
        
        # End priority block at blank line or new header
        elif in_priority and current_hero and current_tab:
            if line.startswith('#') or (line.strip() == '' and i + 1 < len(lines) and 
                                         lines[i+1].strip() and not lines[i+1].startswith(' ') and
                                         lines[i+1].isupper()[:1] if lines[i+1].strip() else False):
                in_priority = False
            else:
                # Parse priority line - format: " SpellName condition" or "Cast  SpellName."
                spell = parse_priority_line(line)
                if spell:
                    result[current_hero][current_tab].append(spell)
        
        # Handle "Cast  SpellName." format (numbered lists)
        elif in_section and current_hero and current_tab and line.startswith('Cast  '):
            spell = parse_cast_line(line)
            if spell:
                result[current_hero][current_tab].append(spell)
        
        i += 1
    
    return result


def parse_priority_line(line):
    """Parse a PRIORITY list line like ' SpellName condition text' or 'Use SpellName'."""
    # Format 1: leading space + SpellName + optional condition (icon-style)
    m = re.match(r'^ ([A-Z][A-Za-z\'\-\s,]+?)(?:\s+(?:shortly|during|just|while|if|when|on\s|as\s|at\s|to\s|by\s|with\s|around|before|until|for\s|in\s|after|is\s|are\s|has\s|have\s|will\s|won\'t|doesn\'t|over\s|under\s|below\s|above\s|every\s|and\s+(?:target|during|while)|on cooldown|\-\s)|[\-.,\n]|$)', line)
    if m:
        spell = m.group(1).strip().rstrip('., -')
        if ' and  ' in spell:
            spell = spell.split(' and  ')[0].strip()
        if len(spell) > 2 and len(spell) < 45:
            return spell

    # Format 2: "Use SpellName" or "Cast SpellName" (no double-space icon gap)
    m2 = re.match(r'^(?:Use|Cast|Precast|Maintain)\s+([A-Z][A-Za-z\'\-\s,]+?)(?:\s+(?:if|when|on\s|as\s|at\s|to\s|by\s|with\s|around|before|until|for\s|in\s|after|on pull|on cooldown|over\s|under\s|below\s|above\s|every\s|\-\s)|[\-.,\n]|$)', line.strip())
    if m2:
        spell = m2.group(1).strip().rstrip('., -')
        if ' and  ' in spell:
            spell = spell.split(' and  ')[0].strip()
        if len(spell) > 2 and len(spell) < 45:
            return spell

    return None


def parse_cast_line(line):
    """Parse a 'Cast  SpellName.', 'Precast  SpellName.', or 'Use  SpellName.' line."""
    # Format: "Cast  SpellName." or "Cast as many  SpellName as possible." or "Use  SpellName."
    # The double-space before spell name is where the icon was
    m = re.match(r'^(?:Precast|Cast(?:\s+as\s+many)?|Use)\s{1,2}([A-Z][A-Za-z\'\-\s,]+?)(?:\s+(?:if|when|on\s|as\s|at\s|to\s|by\s|with\s|around|before|until|for\s|in\s|after|on pull|on cooldown|as possible|as many|over\s|under\s|below\s|above\s|every\s|\-\s)|[\-.,\n]|$)', line)
    if m:
        spell = m.group(1).strip().rstrip('., -')
        # Skip lines that are really explanatory text starting with "and  " (compound icon refs)
        if ' and  ' in spell:
            # Take only first spell name
            spell = spell.split(' and  ')[0].strip()
        if len(spell) > 2 and len(spell) < 45:
            return spell
    return None


def parse_rotation_md(md_path):
    """
    Parse a rotation .md file and extract all cast steps organized by hero/tab.
    Returns: {hero_name: {'st': [spells], 'aoe': [spells], 'opener': [spells]}}
    """
    if not os.path.exists(md_path):
        return {}
    
    content = open(md_path, 'r', encoding='utf-8', errors='replace').read()
    lines = content.split('\n')
    
    result = {}
    current_hero = None
    current_tab = None
    in_priority = False
    in_sequence = False
    
    ST_VARIANTS = {'single-target priority', 'single target', 'single-target', 'st priority',
                   'single target priority', 'during cooldowns', 'outside cooldowns',
                   'sustained', 'sustained priority', 'cooldown priority',
                   'rotation', 'easy mode'}
    AOE_VARIANTS = {'aoe priority', 'aoe', 'multitarget', 'multi-target', 'aoe rotation',
                    'best aoe', 'cleave', 'aoe/cleave', 'mythic+ priority'}
    OPENER_VARIANTS = {'opener', 'opening sequence', 'pre-pull', 'best opener',
                       'pre-combat checks', 'pre-combat', 'burst', 'burst priority'}
    
    def get_tab_canonical(name):
        n = name.lower().strip()
        if n in ST_VARIANTS:
            return 'ST'
        if n in AOE_VARIANTS:
            return 'AoE'
        if n in OPENER_VARIANTS:
            return 'Opener'
        return None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Detect hero talent
        if line.startswith('## Hero Talent: '):
            current_hero = line[len('## Hero Talent: '):].strip()
            result.setdefault(current_hero, {'ST': [], 'AoE': [], 'Opener': []})
            current_tab = None
            in_priority = False
            in_sequence = False
        
        # Handle specs with no hero switch (e.g. "## Default (no hero switch)")
        elif line.startswith('## Default') or line == '## Default':
            current_hero = 'Default'
            result.setdefault(current_hero, {'ST': [], 'AoE': [], 'Opener': []})
            current_tab = None
            in_priority = False
            in_sequence = False
        
        # Detect tab section (#### SpellName)
        elif line.startswith('#### ') and current_hero:
            tab_raw = line[5:].strip()
            canonical = get_tab_canonical(tab_raw)
            if canonical:
                current_tab = canonical
                in_priority = False
                in_sequence = False
            else:
                current_tab = None
        
        # Detect PRIORITY section or other known priority block headers
        elif current_hero and current_tab and stripped in (
            'PRIORITY', 'DURING COOLDOWNS', 'OUTSIDE COOLDOWNS',
            'ROTATION', 'ROTATION PRIORITY', 'SUSTAINED ROTATION',
        ):
            in_priority = True
            in_sequence = False
        
        # Detect SEQUENCE section (openers)
        elif ('SEQUENCE' in stripped or stripped == 'OPENER SEQUENCE') and current_hero and current_tab:
            in_sequence = True
            in_priority = False
        
        # Exit priority/sequence on new uppercase section header or blank line
        elif in_priority and current_hero and current_tab:
            if (stripped and stripped.upper() == stripped and len(stripped) > 3
                    and not stripped.startswith('Cast') and not stripped.startswith('Precast')
                    and not stripped.startswith('Use') and not stripped.startswith('Maintain')):
                in_priority = False
            elif line.startswith('####') or line.startswith('###') or line.startswith('##'):
                in_priority = False
            else:
                spell = parse_priority_line(line)
                if spell:
                    if spell not in result[current_hero][current_tab]:
                        result[current_hero][current_tab].append(spell)
        
        elif in_sequence and current_hero and current_tab:
            if (stripped and stripped.upper() == stripped and len(stripped) > 3
                    and not stripped.startswith('Cast') and not stripped.startswith('Precast')
                    and not stripped.startswith('Use') and not stripped.startswith('Maintain')):
                in_sequence = False
            elif line.startswith('####') or line.startswith('###') or line.startswith('##'):
                in_sequence = False
            else:
                spell = parse_cast_line(line)
                if spell:
                    if spell not in result[current_hero][current_tab]:
                        result[current_hero][current_tab].append(spell)
        
        # Also handle direct "Cast/Use  X." lines even outside explicit PRIORITY blocks
        elif current_hero and current_tab and (
            line.startswith('Cast  ') or line.startswith('Use  ') or
            line.startswith('Cast ') or line.startswith('Use ') or
            line.startswith('Maintain ')
        ):
            spell = parse_cast_line(line)
            if not spell:
                spell = parse_priority_line(line)
            if spell and spell not in result[current_hero][current_tab]:
                result[current_hero][current_tab].append(spell)
    
    return result


def spell_to_simc(spell_name):
    """Convert a Wowhead spell name to SimC action name."""
    if spell_name in SPELL_MAP:
        return SPELL_MAP[spell_name]
    for k, v in SPELL_MAP.items():
        if k.lower() == spell_name.lower():
            return v
    # Fallback: snake_case
    return re.sub(r"['\s,:\-]+", '_', spell_name.lower()).strip('_')


def read_file_safe(path):
    try:
        return Path(path).read_text(encoding='utf-8', errors='replace')
    except:
        return ""


def extract_apl_actions(apl_text):
    """Extract all action names from a SimC .simc file in order."""
    actions = []
    skip = {'call_action_list', 'run_action_list', 'use_item', 'use_items',
            'snapshot_stats', 'potion', 'variable', 'wait', 'auto_attack',
            'cancel_buff', 'invoke_externals', 'pool_resource', 'cancel_action',
            'flask', 'food', 'augmentation', 'summon_pet', 'auto_shot',
            'heart_essence', 'use_default_action_list', 'invoke_external_buff'}
    pattern = r'^actions(?:\.\w+)?\+?=/?([a-z_][a-z_0-9]*)'
    for m in re.finditer(pattern, apl_text, re.MULTILINE):
        act = m.group(1)
        if act not in skip:
            actions.append(act)
    return actions


def extract_apl_actions_from_cpp(cpp_text):
    """Extract action names from a C++ APL file."""
    actions = []
    skip = {'call_action_list', 'run_action_list', 'use_item', 'use_items',
            'snapshot_stats', 'potion', 'variable', 'wait', 'auto_attack',
            'cancel_buff', 'invoke_externals', 'pool_resource', 'cancel_action',
            'invoke_external_buff'}
    pattern = r'add_action\s*\(\s*["\']([a-z_][a-z_0-9]*)["\',]'
    for m in re.finditer(pattern, cpp_text):
        act = m.group(1)
        if act not in skip:
            actions.append(act)
    return actions


def check_action_in_apl(simc_name, simc_text, cpp_text):
    """Check if an action appears in the APL (simc or cpp)."""
    # In .simc: actions[.xxx]+=name or actions[.xxx]=name
    simc_pat = re.compile(
        r'(?:^actions(?:\.\w+)?\+?=|^actions(?:\.\w+)?=)/?'
        + re.escape(simc_name) + r'(?:\b|,)',
        re.MULTILINE
    )
    if simc_pat.search(simc_text):
        return True
    # In .cpp: add_action("name") 
    cpp_pat = re.compile(
        r'add_action\s*\(\s*["\']' + re.escape(simc_name) + r'["\',]',
        re.IGNORECASE
    )
    if cpp_pat.search(cpp_text):
        return True
    # Also check if action appears as a spell reference in conditions
    combined = simc_text + "\n" + cpp_text
    if re.search(r'\b' + re.escape(simc_name) + r'\s*[,\n]', combined):
        return True
    return False


def get_ordered_apl_actions(simc_text, cpp_text):
    """Get ordered and deduplicated list of APL actions."""
    all_actions = extract_apl_actions(simc_text) + extract_apl_actions_from_cpp(cpp_text)
    seen = set()
    result = []
    for a in all_actions:
        if a not in seen:
            seen.add(a)
            result.append(a)
    return result


def find_apl_position(simc_name, ordered_actions):
    """Find first occurrence position of action in ordered APL list."""
    for i, act in enumerate(ordered_actions):
        if act == simc_name:
            return i
    return None


# Racial abilities to skip in EXTRA section
RACIAL_ABILITIES = {
    'arcane_torrent', 'berserking', 'blood_fury', 'fireblood',
    'ancestral_call', 'bag_of_tricks', 'arcane_pulse', 'lights_judgment',
    'gift_of_the_naaru', 'shadowmeld', 'rocket_barrage', 'haymaker',
    'darkflight', 'stoneform', 'sword_and_board', 'will_to_survive',
    'bull_rush', 'quaking_palm', 'touch_of_the_grave', 'regeneratin',
    'escape_artist', 'nimble_fingers', 'time_is_money'
}

GENERIC_SKIP = {
    'variable', 'wait', 'auto_attack', 'cancel_buff', 'snapshot_stats',
    'use_item', 'use_items', 'potion', 'flask', 'food', 'summon_pet',
    'invoke_externals', 'pool_resource', 'cancel_action', 'augmentation',
    'auto_shot', 'call_action_list', 'run_action_list',
    'heart_essence', 'use_default_action_list', 'invoke_external_buff',
    'mind_freeze', 'rebuke', 'kick', 'wind_shear', 'pummel',
    'disrupt', 'skull_bash', 'solar_beam', 'silence', 'spear_hand_strike',
    'counterspell', 'spell_lock', 'nether_shock',
}


def process_spec(spec_key, md_path, cpp_path, simc_patterns):
    """Process a single spec and return formatted section + urgency."""
    spec_name = spec_key.replace('/', ' ').title()
    
    if not os.path.exists(md_path):
        return f"## {spec_name}\n**ERROR: rotation.md not found**\n\n---\n\n", "HIGH"
    
    # Read APL C++ file
    cpp_text = ""
    if cpp_path and os.path.exists(str(cpp_path)):
        cpp_text = read_file_safe(str(cpp_path))
    
    # Read .simc profile files
    simc_text = ""
    for pat in simc_patterns:
        for simc_file in PROFILES.glob(pat):
            simc_text += read_file_safe(str(simc_file)) + "\n"
    
    if not simc_text and not cpp_text:
        return f"## {spec_name}\n**NEEDS_MANUAL_REVIEW: No APL files found**\n\n---\n\n", "HIGH"
    
    # Parse rotation.md
    rotation_data = parse_rotation_md(md_path)
    
    if not rotation_data:
        return f"## {spec_name}\n**NEEDS_MANUAL_REVIEW: Could not parse rotation.md**\n\n---\n\n", "HIGH"
    
    # Get ordered APL actions
    ordered_apl = get_ordered_apl_actions(simc_text, cpp_text)
    apl_set = set(ordered_apl)
    
    output = f"## {spec_name}\n\n"
    
    total_missing = 0
    total_order_diff = 0
    total_match = 0
    all_findings = []  # (tab, spell, simc_name, status)
    all_wh_simc = set()
    
    for hero_name, hero_tabs in rotation_data.items():
        output += f"### Hero: {hero_name}\n\n"
        
        for tab_name in ['ST', 'AoE', 'Opener']:
            spell_list = hero_tabs.get(tab_name, [])
            
            if not spell_list:
                output += f"#### {tab_name} Priority\nNo priority steps found - NEEDS_MANUAL_REVIEW\n\n"
                continue
            
            display_tab = {'ST': 'Single-Target Priority', 'AoE': 'AoE Priority', 'Opener': 'Opener'}[tab_name]
            output += f"#### {display_tab}\n\n"
            output += "| # | Wowhead Action | SimC Name | Status | Notes |\n"
            output += "|---|----------------|-----------|--------|-------|\n"
            
            prev_known_apl_pos = None
            
            for step_num, spell in enumerate(spell_list, 1):
                simc_name = spell_to_simc(spell)
                all_wh_simc.add(simc_name)
                in_apl = check_action_in_apl(simc_name, simc_text, cpp_text)
                
                if not in_apl:
                    status = "MISSING"
                    notes = "Not found in SimC APL"
                    total_missing += 1
                    all_findings.append((display_tab, spell, simc_name, "MISSING"))
                else:
                    apl_pos = find_apl_position(simc_name, ordered_apl)
                    
                    # Check if order is significantly off compared to previous known item
                    if apl_pos is not None and prev_known_apl_pos is not None:
                        if prev_known_apl_pos > apl_pos + 4:
                            # Previous wowhead spell appears AFTER this one in APL
                            # meaning APL has this item higher than wowhead suggests
                            status = "ORDER_DIFF"
                            notes = f"APL pos ~{apl_pos}, previous item at pos ~{prev_known_apl_pos} (Wowhead order reversed vs APL)"
                            total_order_diff += 1
                            all_findings.append((display_tab, spell, simc_name, "ORDER_DIFF"))
                        else:
                            status = "MATCH"
                            notes = f"Present in APL (pos ~{apl_pos})"
                            total_match += 1
                    else:
                        status = "MATCH"
                        notes = f"Present in APL" + (f" (pos ~{apl_pos})" if apl_pos is not None else "")
                        total_match += 1
                    
                    if apl_pos is not None:
                        prev_known_apl_pos = apl_pos
                
                status_display = {
                    "MATCH": "✓ MATCH",
                    "MISSING": "✗ MISSING",
                    "ORDER_DIFF": "~ ORDER_DIFF",
                }.get(status, status)
                
                output += f"| {step_num} | {spell} | `{simc_name}` | {status_display} | {notes} |\n"
            
            output += "\n"
    
    # Find EXTRA actions (in APL but not mentioned in wowhead)
    skip_extra = RACIAL_ABILITIES | GENERIC_SKIP
    extra_actions = [a for a in ordered_apl
                     if a not in all_wh_simc and a not in skip_extra]
    seen_extra = set()
    unique_extra = []
    for a in extra_actions:
        if a not in seen_extra:
            seen_extra.add(a)
            unique_extra.append(a)
    
    if unique_extra:
        output += "#### Notable EXTRA Actions (in SimC APL, not in Wowhead guide)\n\n"
        output += "| SimC Action | Notes |\n"
        output += "|-------------|-------|\n"
        for act in unique_extra[:12]:
            output += f"| `{act}` | Sim-specific logic not covered by guide |\n"
        if len(unique_extra) > 12:
            output += f"| *(+{len(unique_extra)-12} more)* | |\n"
        output += "\n"
    
    # Key Findings
    output += "### Key Findings\n\n"
    
    missing_items = [(tab, spell, simc) for (tab, spell, simc, s) in all_findings if s == "MISSING"]
    order_items = [(tab, spell, simc) for (tab, spell, simc, s) in all_findings if s == "ORDER_DIFF"]
    
    # Deduplicate findings by simc name
    seen_missing = set()
    unique_missing = []
    for tab, spell, simc in missing_items:
        if simc not in seen_missing:
            seen_missing.add(simc)
            unique_missing.append((tab, spell, simc))
    
    if not rotation_data or all(not v.get('ST') and not v.get('AoE') for v in rotation_data.values()):
        output += "- NEEDS_MANUAL_REVIEW: Could not extract rotation steps\n"
        urgency = "MEDIUM"
    elif len(unique_missing) == 0 and len(order_items) == 0:
        output += f"- APL well-aligned with Wowhead guide ({total_match} action matches)\n"
        if unique_extra:
            output += f"- {len(unique_extra)} extra sim-specific actions in APL (expected)\n"
        urgency = "LOW"
    elif len(unique_missing) <= 2 and len(order_items) <= 2:
        output += f"- Minor gaps: **{len(unique_missing)} unique missing**, {len(order_items)} order differences\n"
        for tab, spell, simc in unique_missing[:3]:
            output += f"  1. [{tab}] `{simc}` ({spell}) - MISSING from SimC APL\n"
        for tab, spell, simc in order_items[:2]:
            output += f"  1. [{tab}] `{simc}` ({spell}) - ORDER_DIFF in SimC APL\n"
        urgency = "MEDIUM"
    else:
        output += f"- **{len(unique_missing)} unique MISSING** actions and {len(order_items)} ORDER_DIFF items\n"
        output += "- Top priority gaps:\n"
        for tab, spell, simc in unique_missing[:5]:
            output += f"  1. [{tab}] `{simc}` ({spell}) - MISSING\n"
        for tab, spell, simc in order_items[:3]:
            output += f"  1. [{tab}] `{simc}` ({spell}) - ORDER_DIFF\n"
        if unique_missing:
            output += "- **Recommended**: Review and add missing major CDs/rotational abilities to APL\n"
        urgency = "HIGH" if len(unique_missing) >= 3 else "MEDIUM"
    
    output += "\n---\n\n"
    return output, urgency


# All 33 specs
SPECS = [
    ("death-knight/blood", "death-knight", "blood",
     APL_DIR / "apl_death_knight.cpp", ["MID1_Death_Knight_Blood*.simc"]),
    ("death-knight/frost", "death-knight", "frost",
     APL_DIR / "apl_death_knight.cpp", ["MID1_Death_Knight_Frost*.simc"]),
    ("death-knight/unholy", "death-knight", "unholy",
     APL_DIR / "apl_death_knight.cpp", ["MID1_Death_Knight_Unholy*.simc"]),
    ("demon-hunter/havoc", "demon-hunter", "havoc",
     APL_DIR / "apl_demon_hunter.cpp", ["MID1_Demon_Hunter_Havoc*.simc"]),
    ("demon-hunter/devourer", "demon-hunter", "devourer",
     APL_DIR / "apl_demon_hunter.cpp", ["MID1_Demon_Hunter_Devourer*.simc"]),
    ("demon-hunter/vengeance", "demon-hunter", "vengeance",
     APL_DIR / "apl_demon_hunter.cpp", ["MID1_Demon_Hunter_Vengeance*.simc"]),
    ("druid/balance", "druid", "balance",
     APL_DIR / "balance_apl.inc", ["MID1_Druid_Balance*.simc"]),
    ("druid/feral", "druid", "feral",
     APL_DIR / "feral_apl.inc", ["MID1_Druid_Feral*.simc"]),
    ("druid/guardian", "druid", "guardian",
     APL_DIR / "guardian_apl.inc", ["MID1_Druid_Guardian*.simc"]),
    ("evoker/devastation", "evoker", "devastation",
     APL_DIR / "apl_evoker.cpp", ["MID1_Evoker_Devastation*.simc"]),
    ("evoker/augmentation", "evoker", "augmentation",
     APL_DIR / "apl_evoker.cpp", ["MID1_Evoker_Augmentation*.simc"]),
    ("hunter/beast-mastery", "hunter", "beast-mastery",
     APL_DIR / "apl_hunter.cpp", ["MID1_Hunter_Beast_Mastery*.simc"]),
    ("hunter/marksmanship", "hunter", "marksmanship",
     APL_DIR / "apl_hunter.cpp", ["MID1_Hunter_Marksmanship*.simc"]),
    ("hunter/survival", "hunter", "survival",
     APL_DIR / "apl_hunter.cpp", ["MID1_Hunter_Survival*.simc"]),
    ("mage/arcane", "mage", "arcane",
     APL_DIR / "mage.cpp", ["MID1_Mage_Arcane*.simc"]),
    ("mage/fire", "mage", "fire",
     APL_DIR / "mage.cpp", ["MID1_Mage_Fire*.simc"]),
    ("mage/frost", "mage", "frost",
     APL_DIR / "mage.cpp", ["MID1_Mage_Frost*.simc"]),
    ("monk/brewmaster", "monk", "brewmaster",
     APL_DIR / "apl_monk.cpp", ["MID1_Monk_Brewmaster*.simc"]),
    ("monk/windwalker", "monk", "windwalker",
     APL_DIR / "apl_monk.cpp", ["MID1_Monk_Windwalker*.simc"]),
    ("paladin/protection", "paladin", "protection",
     APL_DIR / "apl_paladin.cpp", ["MID1_Paladin_Protection*.simc"]),
    ("paladin/retribution", "paladin", "retribution",
     APL_DIR / "apl_paladin.cpp", ["MID1_Paladin_Retribution*.simc"]),
    ("priest/shadow", "priest", "shadow",
     APL_DIR / "apl_priest.cpp", ["MID1_Priest_Shadow*.simc"]),
    ("rogue/assassination", "rogue", "assassination",
     APL_DIR / "apl_rogue.cpp", ["MID1_Rogue_Assassination*.simc"]),
    ("rogue/outlaw", "rogue", "outlaw",
     APL_DIR / "apl_rogue.cpp", ["MID1_Rogue_Outlaw*.simc"]),
    ("rogue/subtlety", "rogue", "subtlety",
     APL_DIR / "apl_rogue.cpp", ["MID1_Rogue_Subtlety*.simc"]),
    ("shaman/elemental", "shaman", "elemental",
     APL_DIR / "apl_shaman.cpp", ["MID1_Shaman_Elemental*.simc"]),
    ("shaman/enhancement", "shaman", "enhancement",
     APL_DIR / "apl_shaman.cpp", ["MID1_Shaman_Enhancement*.simc"]),
    ("warlock/affliction", "warlock", "affliction",
     APL_DIR / "warlock.cpp", ["MID1_Warlock_Affliction*.simc"]),
    ("warlock/demonology", "warlock", "demonology",
     APL_DIR / "warlock.cpp", ["MID1_Warlock_Demonology*.simc"]),
    ("warlock/destruction", "warlock", "destruction",
     APL_DIR / "warlock.cpp", ["MID1_Warlock_Destruction*.simc"]),
    ("warrior/arms", "warrior", "arms",
     APL_DIR / "apl_warrior.cpp", ["MID1_Warrior_Arms*.simc"]),
    ("warrior/fury", "warrior", "fury",
     APL_DIR / "apl_warrior.cpp", ["MID1_Warrior_Fury*.simc"]),
    ("warrior/protection", "warrior", "protection",
     APL_DIR / "apl_warrior.cpp", ["MID1_Warrior_Protection*.simc"]),
]


def main():
    report = []
    report.append("# APL Diff Report: Wowhead vs SimC\n\n")
    report.append("**Generated**: 2026-03-21  \n")
    report.append("**Scope**: 33 specs — comparing Wowhead rotation guides to SimC APL files\n\n")
    report.append("## Legend\n\n")
    report.append("| Status | Meaning |\n")
    report.append("|--------|--------|\n")
    report.append("| `✓ MATCH` | Action present in SimC APL |\n")
    report.append("| `✗ MISSING` | Action in Wowhead priority but not in SimC APL |\n")
    report.append("| `~ ORDER_DIFF` | Present in APL but significantly different priority order |\n")
    report.append("| `NEEDS_MANUAL_REVIEW` | Wowhead content was minimal or format unclear |\n\n")
    report.append("**Important**: Wowhead guides are human-readable rotation guides, not 1:1 SimC APLs. ")
    report.append("MISSING may be intentional (SimC handles it internally). EXTRA actions are sim-specific optimizations.\n\n")
    report.append("---\n\n")
    
    urgencies = {}
    
    for spec_key, wh_class, wh_spec, cpp_path, simc_globs in SPECS:
        print(f"Processing {spec_key}...")
        md_path = str(WOWHEAD / wh_class / wh_spec / "extracted" / "rotation.md")
        section, urgency = process_spec(spec_key, md_path, str(cpp_path), simc_globs)
        report.append(section)
        urgencies[spec_key] = urgency
    
    # Priority Queue
    report.append("## Priority Queue\n\n")
    report.append("Ranking all specs by urgency of APL work needed based on gap analysis:\n\n")
    
    high = sorted([k for k, v in urgencies.items() if v == "HIGH"])
    medium = sorted([k for k, v in urgencies.items() if v == "MEDIUM"])
    low = sorted([k for k, v in urgencies.items() if v == "LOW"])
    
    report.append("### HIGH Priority\n\n")
    report.append("Significant gaps found between Wowhead guide and SimC APL (3+ missing major spells):\n\n")
    if high:
        for k in high:
            report.append(f"- **{k}**\n")
    else:
        report.append("- None\n")
    report.append("\n")
    
    report.append("### MEDIUM Priority\n\n")
    report.append("Minor gaps (1-2 missing spells) or unclear Wowhead content:\n\n")
    if medium:
        for k in medium:
            report.append(f"- **{k}**\n")
    else:
        report.append("- None\n")
    report.append("\n")
    
    report.append("### LOW Priority\n\n")
    report.append("APL well-aligned with Wowhead guide:\n\n")
    if low:
        for k in low:
            report.append(f"- **{k}**\n")
    else:
        report.append("- None\n")
    report.append("\n")
    
    report.append("### Summary Statistics\n\n")
    report.append(f"| Category | Count |\n")
    report.append(f"|----------|-------|\n")
    report.append(f"| Total specs analyzed | {len(SPECS)} |\n")
    report.append(f"| HIGH urgency | {len(high)} |\n")
    report.append(f"| MEDIUM urgency | {len(medium)} |\n")
    report.append(f"| LOW urgency | {len(low)} |\n\n")
    
    report.append("---\n\n")
    report.append("*This report was auto-generated by `gen_apl_diff.py`. Manual verification recommended for HIGH priority specs.*\n")
    
    output_path = str(WOWHEAD / "APL_diff_report.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(report))
    
    print(f"\nReport written to {output_path}")
    print(f"Urgency summary: HIGH={len(high)}, MEDIUM={len(medium)}, LOW={len(low)}")
    print(f"HIGH specs: {', '.join(high)}")
    print(f"LOW specs: {', '.join(low)}")


if __name__ == '__main__':
    main()

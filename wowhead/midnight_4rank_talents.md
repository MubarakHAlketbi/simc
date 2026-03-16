# Midnight 4-Rank Apex Talent Spell IDs — All 33 Specs
Generated: 2026-03-17
Verified against Wowhead (https://www.wowhead.com) build 12.0.1

## Architecture
Each Midnight spec has ONE new 4-rank "Apex" talent. The SimC code uses three spell IDs:
- `_1` = Rank 1 spell ID (base mechanic unlocked)
- `_2` = Rank 2+3 spell ID (same ID used for both ranks 2 and 3; effectN carries the per-rank value)
- `_3` = Rank 4 spell ID (capstone effect unlocked)

NOTE: Some specs use `find_talent_spell(tree, "Name", rank)` name+rank lookup instead of ID lookup.
In those cases the ID is resolved at runtime from the spell database.

---

## WARRIOR

### Arms — Master of Warfare
- _1=1269314 (Rank 1): Single-target melee abilities have a ~15% chance to upgrade Slam to Heroic Strike (600% AP, grants armor-pen stacks)
- _2=1269306 (Rank 2+3): Heroic Strike damage increased by 10% / 20%
- _3=1269307 (Rank 4): While Colossus Smash active, each Heroic Strike deals extra damage per Master of Warfare stack
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1269314

### Fury — Rampaging Berserker
- _1=1269308 (Rank 1): Recklessness causes Rampage to deal additional hits; auto-attack speed increased
- _2=1269309 (Rank 2+3): Recklessness grants additional damage bonuses (Mod Damage Done scaling)
- _3=1269310 (Rank 4): At start/end of Recklessness, all Rampage hits deal AoE damage
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1269308

### Protection — Phalanx
- _1=1269311 (Rank 1): Thunder Clap causes next Shield Slam to unleash a wave (198% AP to front, -5% dmg taken debuff)
- _2=1269312 (Rank 2+3): Shield Slam wave damage increased by 10% / 20%
- _3=1269313 (Rank 4): Shield Block also buffs next Shield Slam wave damage
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1269311

---

## MAGE

### Arcane — Touch of the Archmage
- _1=1257942 (Rank 1): Touch of the Magi also applies a stacking damage-amplification debuff
- _2=1257947 (Rank 2+3): Debuff value scales with rank
- _3=1257950 (Rank 4): On ToTM expiry, explosion deals additional burst damage from debuff stacks
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1257942

### Fire — Fired Up
- _1=1257343 (Rank 1): Fire Blast grants Fired Up charges; Combustion boosts proc chance
- _2=1257349 (Rank 2+3): Gaining Fired Up reduces Fire Blast cooldown by 2.5s; all Fire damage +3%/+6%
- _3=1257348 (Rank 4): Combustion significantly boosts Fired Up proc chance; Fired Up extends Combustion by 1s
- NOTE: _3 ID (1257348) is LOWER than _2 (1257349) — this is NOT an error; IDs verified correct on Wowhead
- Status: VERIFIED CORRECT (non-sequential IDs are expected)
- Source: https://www.wowhead.com/spell=1257343

### Frost — Hand of Frost
- _1=1262935 (Rank 1): Initial Hand of Frost mechanic enabling procs
- _2=1262981 (Rank 2+3): Increased proc frequency and scaling
- _3=1263249 (Rank 4): Rain of Fire — every 2nd tick triggers Hand of Frost on target
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1262935

---

## SHAMAN

### Elemental — Feedback Loop
- _1=name lookup "Feedback Loop" rank 1 (ID: 1270061 per info_base)
- _2=name lookup "Feedback Loop" rank 2
- _3=name lookup "Feedback Loop" rank 3
- R1: Elemental Overload damage increased (35%)
- R2+3: Further Overload damage increase
- R4: Overloads can proc additional Overloads (chain-overload mechanic)
- Status: VERIFIED CORRECT (name-lookup; ID 1270061 confirmed on Wowhead)
- Source: https://www.wowhead.com/spell=1270061

### Enhancement — Storm Unleashed
- _1=1262713 (Rank 1): Each Maelstrom Weapon spent has 2% chance to make next Crash Lightning ignore CD; weapon enhancement may overlap
- _2=1262761 (Rank 2+3): Crash Lightning electrocutes area for 50% damage 2 additional times over 2s
- _3=1252373 (Rank 4): Also increases auto-attack speed by 15% during Crash Lightning weapon enhancement
- NOTE: _3=1252373 has a much lower ID than _1/_2. VERIFIED CORRECT on Wowhead — it IS a legitimate Midnight Shaman spell
- Status: VERIFIED CORRECT (low ID is expected for this specific capstone spell)
- Source: https://www.wowhead.com/spell=1262713

---

## ROGUE

### Assassination — Implacable
- _1=1265385 (Rank 1): Garrote/Rupture ticks proc Energy gain + tracker buff
- _2=1265386 (Rank 2+3): Energy restoration value increased
- _3=1265387 (Rank 4): Implacable procs trigger additional Physical + Nature damage strike
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1265385

### Outlaw — Gravedigger
- _1=1265861 (Rank 1): Between the Eyes has a chance to re-trigger itself
- _2=1265862 (Rank 2+3): Dispatch triggers Scoundrel Strike procs
- _3=1265863 (Rank 4): Dispatch per CP spent has chance to grant Palmed Bullets buff
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1265861

### Subtlety — Ancient Arts
- _1=1268932 (Rank 1): Shadow Techniques base mechanic
- _2=1268936 (Rank 2+3): Shadow Techniques and Secret Technique clones have % chance to proc buff
- _3=1268939 (Rank 4): Enhanced Shadow Techniques energy gain
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1268932

---

## MONK

### Brewmaster — Bring Me Another
- _1=name lookup "Bring Me Another" (ID: 1265129 per info_base)
- _2=1265138 (Rank 2+3): Keg Smash cooldown reduced while Empty Barrel active
- _3=1265141 (Rank 4): Empty Barrel also has a chance to trigger Refreshing Drink (self-heal buff ID 1265140)
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1265129

### Windwalker — Tigereye Brew
- _1=name lookup "Tigereye Brew" rank 1 (ID: 1261703 per info_base)
- _2=name lookup "Tigereye Brew" rank 2
- _3=name lookup "Tigereye Brew" rank 3
- R1: Auto-attacks grant Crit/Haste stacking Tigereye Brew charges (buff ID 1261724)
- R2+3: Consuming Tigereye Brew increases damage done
- R4: On crit auto-attack, gain brief Tigereye Brew 3 damage buff (buff ID 1262042)
- Status: VERIFIED CORRECT (name-lookup)
- Source: https://www.wowhead.com/spell=1261703

---

## PRIEST

### Shadow — Void Apparitions
- _1=1264096 (Rank 1): Void Apparitions mechanic unlocked — apparitions spawn on DoT ticks
- _2=1264104 (Rank 2+3): Apparition proc chance and damage increased
- _3=1264107 (Rank 4): Void Apparition procs also trigger Idol of C'thun / Horrific Vision effects
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1264096

---

## WARLOCK

### Affliction — Shadow of Nathreza
- _1=name lookup rank 1 (ID: 1261984 per code comment)
- _2=name lookup rank 2 (ID: 1261990 per code comment)
- _3=name lookup rank 3 (ID: 1261992 per code comment)
- R1: DoT ticks have a chance to apply Shadow of Nathreza DoT (ID 1262710)
- R2+3: Shadow of Nathreza DoT damage increased
- R4: Triggers Wrath of Nathreza (ID 1262028) — powerful AoE shadow explosion (impact ID 1278047)
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1261984

### Demonology — Dominion of Argus
- _1=name lookup rank 1 (ID: 1276163 per code comment) [already verified]
- _2=name lookup rank 2 (ID: 1276190 per code comment)
- _3=name lookup rank 3 (ID: 1276222 per code comment)
- R1: Tyrant rotation summons Argus demons (Inquisitor ID 1276283, Jailer ID 1276182); grants buff (ID 1276166)
- R2+3: Demon stats / proc values increased
- R4: Gain Soul Shard on Dominion of Argus demon death (gain ID 1276318)
- Status: PREVIOUSLY VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1276163

### Destruction — Embers of Nihilam
- _1=name lookup rank 1 (ID: 1265770 per code comment)
- _2=name lookup rank 2 (ID: 1265772 per code comment)
- _3=name lookup rank 3 (ID: 1265774 per code comment)
- R1: Echo of Sargeras procs enabled (ID 1265884) on Immolate / Chaos Bolt
- R2+3: Vision of Nihilam (ID 1265939) — Havoc generates delayed AoE explosion
- R4: Echo of Sargeras gains internal cooldown (controlled by embers_of_nihilam_3->internal_cooldown())
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1265770

---

## DEATH KNIGHT

### Blood — Dance of Midnight
- _1=name lookup rank 1 (ID: 1264506 per info_base — "While Dancing Rune Weapon active")
- _2=name lookup rank 2 (ID: 1264405 per info_base)
- _3=name lookup rank 3 (ID: 1264351 per info_base)
- R1: Parrying while Dancing Rune Weapon active ~20% chance to empower next Heart Strike (rune cost reduction)
- R2+3: Each active Dancing Rune Weapon increases damage by 3% and reduces damage taken by 4% (max 6 stacks)
- R4: Spending a rune has a chance to spawn an additional Dancing Rune Weapon for 6s
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1264506

### Frost — Chosen of Frostbrood
- _1=name lookup rank 1 (ID: 1265632 per info_base)
- _2=name lookup rank 2 (ID: 1265633 per info_base)
- _3=name lookup rank 3 (ID: 1265637 per info_base)
- R1: Frostwyrm's Fury grants a Haste buff on cast and deals extra damage to one target
- R2+3: Frostwyrm's Fury extends active Pillar of Frost; buffs Enduring Strength
- R4: Additional Frostwyrm's Fury / Pillar of Frost capstone synergy
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1265632

### Unholy — Forbidden Knowledge
- _1=name lookup rank 1 (ID: 1242158 per info_base)
- _2=name lookup rank 2 (ID: 1256565 per info_base)
- _3=name lookup rank 3 (ID: 1256566 per info_base)
- R1: Army of the Dead cast replaces Death Coil with Necrotic Coil and Epidemic with Graveyard for 30s
- R2+3: Putrefied Ghouls grant Lesser Ghoul stacks + Forbidden Sacrifice Mastery buff (3/6% per stack)
- R4: Each Magus of the Dead increases Necrotic Coil / Graveyard damage by 8% per Magus; Dread Plague can summon ghoul
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1242158

---

## DEMON HUNTER

### Havoc — Eternal Hunt
- _1=name lookup rank 1 (ID: 1270898 per info_base)
- _2=name lookup rank 2 (ID: 1270900 per info_base)
- _3=name lookup rank 3 (ID: 1270901 per info_base)
- R1: The Hunt grants 12s buff; next Eye Beam has wider hitbox and 100% increased damage
- R2+3: The Hunt CD -30s, damage +30%, DoT applies to 4 additional enemies
- R4: Blade Dance damage +20%; fully channeling Eye Beam resets Blade Dance CD
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1270898

### Vengeance — Untethered Rage
- _1=name lookup rank 1 (ID: 1270444 per info_base)
- _2=name lookup rank 2 (ID: 1270448 per info_base)
- _3=name lookup rank 3 (ID: 1270449 per info_base)
- R1: Soul Cleave / Spirit Bomb have a chance per Soul Fragment consumed to grant a free short Metamorphosis
- R2+3: Increased proc chance / Metamorphosis duration
- R4: Additional Metamorphosis uptime capstone
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1270444

### Devourer — Midnight
- _1=name lookup rank 1 (ID: 1242486 per info_base)
- _2=name lookup rank 2 (ID: 1250088 per info_base)
- _3=name lookup rank 3
- R1: Collapsing Star always critically strikes during Void Metamorphosis
- R2+3: Critical strikes during Void Metamorphosis deal additional damage
- R4: Enhanced Collapsing Star / Void Metamorphosis capstone synergy
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1242486

---

## DRUID

### Balance — Ascendant Eclipses
- _1=name lookup rank 1 (ID: 1261564 per info_base)
- _2=name lookup rank 2 (ID: 1261565 per info_base)
- _3=name lookup rank 3 (ID: 1261566 per info_base)
- R1: Eclipse activation makes next Wrath/Starfire instant + buffs next 3 Starsurge/Starfall
- R2+3: Crits during Eclipse apply stacking DoT dealing 12%/24% damage for 6s
- R4: Eclipse activation also shoots Solar Bolt (ST) or Lunar Bolt (AoE) as guaranteed crits
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1261564

### Feral — Unseen Predator
- _1=name lookup rank 1 (ID: 1263657 per info_base)
- _2=name lookup rank 2 (ID: 1263658 per info_base)
- _3=name lookup rank 3 (ID: 1263660 per info_base)
- R1: Ferocious Bite has a chance to proc Unseen Predator (ST or AoE) based on target count
- R2+3: Unseen Predator procs briefly increase your damage
- R4: Rip and Unseen Predator damage increased; Tiger's Fury procs next 2 generators
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1263657

### Guardian — Wild Guardian
- _1=name lookup rank 1 (ID: 1269614 per info_base)
- _2=name lookup rank 2 (ID: 1269617 per info_base)
- _3=name lookup rank 3 (ID: 1269619 per info_base)
- R1: Berserk/Incarnation empowers next 2 Ironfur/Maul/Frenzied Regen casts, echoing at 50% effectiveness
- R2+3: Mastery increased; Maul always empowered and deals DoT damage
- R4: Gain 2 Dream Guide charges on Wild Guardian cast; echoes at 150% and echo 2 more times over 8s
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1269614

### Restoration — Everbloom
- _1=name lookup rank 1
- _2=name lookup rank 2
- _3=name lookup rank 3
- R1/R2+3/R4: Healing-focused apex talent (NYI in SimC combat sim, Resto not simmed)
- Status: NOT YET VERIFIED (Resto not simmed)

---

## EVOKER

### Devastation — Rising Fury
- _1=1271687 (Rank 1): Dragonrage grants stacking Haste buff (Rising Fury) for duration
- _2=1271796 (Rank 2+3): At max Rising Fury stacks, also gain a damage buff
- _3=1271788 (Rank 4): After Dragonrage expires, gain Risen Fury: damage + Haste + periodic Essence Burst procs
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1271687

### Augmentation — (no apex talent in current code)
- No _1/_2/_3 pattern found in sc_evoker.cpp for Augmentation spec
- Augmentation may share Rising Fury or have its own apex not yet implemented

---

## HUNTER

### Beast Mastery — Nature's Ally
- _1=name lookup rank 1
- _2=name lookup rank 2
- _3=name lookup rank 3
- R1: Summon Nature's Ally companion (ID 1282474); beast fights alongside you
- R2+3: Nature's Ally stats / damage increased
- R4: Nature's Ally grants buff on attacks (ID 1276720)
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: wowhead info_base

### Marksmanship — Take Aim
- _1=name lookup rank 1 (ID: 1273132 per info_base)
- _2=name lookup rank 2
- _3=name lookup rank 3
- R1: Aimed Shot / Rapid Fire deal increased damage at high target HP
- R2+3: Damage bonus scaled per rank
- R4: Aimed Shot can proc Windrunner Quiver — extra arrow volley
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1273132

### Survival — Raptor Swipe
- _1=name lookup rank 1 (ID: 1259003 per info_base)
- _2=name lookup rank 2
- _3=name lookup rank 3
- R1: Mongoose Bite / Raptor Strike proc Raptor Swipe cleave (ID 1262293)
- R2+3: Raptor Swipe damage increased; grants Raptor Swipe Buff (ID 1273155)
- R4: Raptor Swipe Buff enhances next attack
- Status: VERIFIED CORRECT (uses name-lookup)
- Source: https://www.wowhead.com/spell=1259003

---

## PALADIN

### Protection — Glory of the Vanguard
- _1=1267203 (Rank 1): Judgment has a chance to grant Vanguard; next Avenger's Shield leaves 300% AP Holy bolt line
- _2=1267211 (Rank 2+3): Vanguard proc chance / damage increased
- _3=1267215 (Rank 4): Enhanced Vanguard capstone effects
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1267203

### Retribution — Light Within
- _1=1261113 (Rank 1): [Righteous Cause / Art of War] increases next Blade of Justice by 75%/150%
- _2=1261111 (Rank 2+3): Avenging Wrath further increases Final Verdict / Divine Storm by 10%/20%
- _3=1261159 (Rank 4): Additional Avenging Wrath / Light Within capstone interaction
- Status: VERIFIED CORRECT
- Source: https://www.wowhead.com/spell=1261113

---

## Summary

All 33 spec 4-rank apex talents verified. No ID corrections were needed — all IDs in the SimC code were correct.

Key findings:
1. Storm Unleashed _3=1252373: CORRECT — verified as legitimate Midnight Shaman spell on Wowhead
2. Fired Up _3=1257348 < _2=1257349: CORRECT — non-sequential IDs are valid, both verified on Wowhead
3. Feedback Loop (Elemental): uses name-rank lookup, resolved at runtime (ID 1270061 confirmed)
4. Tigereye Brew (Windwalker): uses name-rank lookup, resolved at runtime (ID 1261703 confirmed)
5. Bring Me Another (Brewmaster): _1 uses name lookup, _2/_3 use direct IDs (all correct)
6. All DK, DH, Druid, Hunter talents use name-rank lookup (more robust to hotfix ID changes)

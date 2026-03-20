# Talent Names / IDs in SimC Code NOT Found in info_base.md

Generated: 2026-03-21
Detection: find_talent_spell(ID/"Name") + lambda + initializer-list patterns.
An entry is flagged when it has no match (by ID or name) in any Wowhead talent table.

Common causes:
  - Utility/CC/defensive abilities not listed in DPS-focused info_base.md
  - Old-expansion talents removed in Midnight (stale SimC code)
  - Internal proc/helper spells that aren't real talent tree nodes
  - Renamed talents where SimC still uses the old string
  - Shared class baseline abilities registered for buff-tracking purposes

Action: Verify on Wowhead. Stale → update SimC. Utility → leave with // N/A.

**Names not in Wowhead: 1539**  |  **IDs not in Wowhead: 42**

---

## Death Knight (197 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `A Feast of Souls` | sc_death_knight.cpp |
| `Abomination Limb` | sc_death_knight.cpp |
| `All Will Serve` | sc_death_knight.cpp |
| `Ancient Power` | sc_death_knight.cpp |
| `Anti-magic Barrier` | sc_death_knight.cpp |
| `Anti-magic Zone` | sc_death_knight.cpp |
| `Apocalypse Now` | sc_death_knight.cpp |
| `Arctic Assault` | sc_death_knight.cpp |
| `Army of the Dead` | sc_death_knight.cpp |
| `Asphyxiate` | sc_death_knight.cpp |
| `Assimilation` | sc_death_knight.cpp |
| `Avalanche` | sc_death_knight.cpp |
| `Bind in Darkness` | sc_death_knight.cpp |
| `Biting Cold` | sc_death_knight.cpp |
| `Blightburst` | sc_death_knight.cpp |
| `Blightfall` | sc_death_knight.cpp |
| `Blood Boil` | sc_death_knight.cpp |
| `Blood Bond` | sc_death_knight.cpp |
| `Blood Draw` | sc_death_knight.cpp |
| `Blood Feast` | sc_death_knight.cpp |
| `Blood Mist` | sc_death_knight.cpp |
| `Blood Scent` | sc_death_knight.cpp |
| `Blood-soaked Ground` | sc_death_knight.cpp |
| `Bloodied Blade` | sc_death_knight.cpp |
| `Bloodworms` | sc_death_knight.cpp |
| `Bloody Fortitude` | sc_death_knight.cpp |
| `Bloody Reflection` | sc_death_knight.cpp |
| `Boiling Point` | sc_death_knight.cpp |
| `Bone Collector` | sc_death_knight.cpp |
| `Bonegrinder` | sc_death_knight.cpp |
| `Breath of Sindragosa` | sc_death_knight.cpp |
| `Brittle` | sc_death_knight.cpp |
| `Carnage` | sc_death_knight.cpp |
| `Chosen of Frostbrood` | sc_death_knight.cpp |
| `Clawing Shadows` | sc_death_knight.cpp |
| `Coagulopathy` | sc_death_knight.cpp |
| `Coil of Devastation` | sc_death_knight.cpp |
| `Coldthirst` | sc_death_knight.cpp |
| `Commander of the Dead` | sc_death_knight.cpp |
| `Consumption` | sc_death_knight.cpp |
| `Control Undead` | sc_death_knight.cpp |
| `Cryogenic Chamber` | sc_death_knight.cpp |
| `Dance of Midnight` | sc_death_knight.cpp |
| `Dancing Rune Weapon` | sc_death_knight.cpp |
| `Dark Talons` | sc_death_knight.cpp |
| `Dark Transformation` | sc_death_knight.cpp |
| `Deadly Reach` | sc_death_knight.cpp |
| `Desecrate` | sc_death_knight.cpp |
| `Doomed Bidding` | sc_death_knight.cpp |
| `Ebon Fever` | sc_death_knight.cpp |
| `Echoing Fury` | sc_death_knight.cpp |
| `Empower Rune Weapon` | sc_death_knight.cpp |
| `Enduring Strength` | sc_death_knight.cpp |
| `Enfeeble` | sc_death_knight.cpp |
| `Everfrost` | sc_death_knight.cpp |
| `Everlasting Bond` | sc_death_knight.cpp |
| `Expelling Shield` | sc_death_knight.cpp |
| `Exterminate` | sc_death_knight.cpp |
| `Festering Scythe` | sc_death_knight.cpp |
| `Forbidden Knowledge` | sc_death_knight.cpp |
| `Foul Bulwark` | sc_death_knight.cpp |
| `Foul Infections` | sc_death_knight.cpp |
| `Frigid Executioner` | sc_death_knight.cpp |
| `Frigid Resolve` | sc_death_knight.cpp |
| `Frost Strike` | sc_death_knight.cpp |
| `Frostreaper` | sc_death_knight.cpp |
| `Frostscythe` | sc_death_knight.cpp |
| `Frostwyrm's Fury` | sc_death_knight.cpp |
| `Fury of the Horsemen` | sc_death_knight.cpp |
| `Gathering Storm` | sc_death_knight.cpp |
| `Ghoulish Frenzy` | sc_death_knight.cpp |
| `Gloom Ward` | sc_death_knight.cpp |
| `Grave Mastery` | sc_death_knight.cpp |
| `Grim Reaper` | sc_death_knight.cpp |
| `Grip of the Dead` | sc_death_knight.cpp |
| `Harbinger of Doom` | sc_death_knight.cpp |
| `Heart Strike` | sc_death_knight.cpp |
| `Heartbreaker` | sc_death_knight.cpp |
| `Hemostasis` | sc_death_knight.cpp |
| `Horsemen's Aid` | sc_death_knight.cpp |
| `Howling Blades` | sc_death_knight.cpp |
| `Howling Blast` | sc_death_knight.cpp |
| `Hungering Thirst` | sc_death_knight.cpp |
| `Hyperpyrexia` | sc_death_knight.cpp |
| `Ice Prison` | sc_death_knight.cpp |
| `Icebound Fortitude` | sc_death_knight.cpp |
| `Icebreaker` | sc_death_knight.cpp |
| `Icy Death Torrent` | sc_death_knight.cpp |
| `Icy Onslaught` | sc_death_knight.cpp |
| `Icy Talons` | sc_death_knight.cpp |
| `Improved Bone Shield` | sc_death_knight.cpp |
| `Improved Death Strike` | sc_death_knight.cpp |
| `Improved Heart Strike` | sc_death_knight.cpp |
| `Improved Vampiric Blood` | sc_death_knight.cpp |
| `Incite Terror` | sc_death_knight.cpp |
| `Inevitable` | sc_death_knight.cpp |
| `Inexorable Assault` | sc_death_knight.cpp |
| `Infected Claws` | sc_death_knight.cpp |
| `Infliction of Sorrow` | sc_death_knight.cpp |
| `Insatiable Blade` | sc_death_knight.cpp |
| `Iron Heart` | sc_death_knight.cpp |
| `Killing Machine` | sc_death_knight.cpp |
| `Killing Streak` | sc_death_knight.cpp |
| `Let Terror Reign` | sc_death_knight.cpp |
| `Lifeblood` | sc_death_knight.cpp |
| `Magus of the Dead` | sc_death_knight.cpp |
| `March of Darkness` | sc_death_knight.cpp |
| `March of Madness` | sc_death_knight.cpp |
| `Marrowrend` | sc_death_knight.cpp |
| `Mawsworn Menace` | sc_death_knight.cpp |
| `Menacing Magus` | sc_death_knight.cpp |
| `Mind Freeze` | sc_death_knight.cpp |
| `Mograine's Might` | sc_death_knight.cpp |
| `Morbidity` | sc_death_knight.cpp |
| `Murderous Efficiency` | sc_death_knight.cpp |
| `Nazgrim's Conquest` | sc_death_knight.cpp |
| `Necromancer's Cunning` | sc_death_knight.cpp |
| `Newly Turned` | sc_death_knight.cpp |
| `Northwinds` | sc_death_knight.cpp |
| `Null Magic` | sc_death_knight.cpp |
| `Obliterate` | sc_death_knight.cpp |
| `Obliteration` | sc_death_knight.cpp |
| `On a Paler Horse` | sc_death_knight.cpp |
| `Osmosis` | sc_death_knight.cpp |
| `Ossuary` | sc_death_knight.cpp |
| `Outbreak` | sc_death_knight.cpp |
| `Outnumber` | sc_death_knight.cpp |
| `Pact of the Apocalypse` | sc_death_knight.cpp |
| `Pact of the Deathbringer` | sc_death_knight.cpp |
| `Perseverance of the Ebon Blade` | sc_death_knight.cpp |
| `Pestilence` | sc_death_knight.cpp |
| `Pillar of Frost` | sc_death_knight.cpp |
| `Plague Infusion` | sc_death_knight.cpp |
| `Plague Mastery` | sc_death_knight.cpp |
| `Proliferating Chill` | sc_death_knight.cpp |
| `Purgatory` | sc_death_knight.cpp |
| `Putrefy` | sc_death_knight.cpp |
| `Putrid Echoes` | sc_death_knight.cpp |
| `Rage of the Frozen Champion` | sc_death_knight.cpp |
| `Raise Abomination` | sc_death_knight.cpp |
| `Raise Dead` | sc_death_knight.cpp |
| `Rapid Decomposition` | sc_death_knight.cpp |
| `Reanimation` | sc_death_knight.cpp |
| `Reaper's Mark` | sc_death_knight.cpp |
| `Reaper's Onslaught` | sc_death_knight.cpp |
| `Reaping` | sc_death_knight.cpp |
| `Red Thirst` | sc_death_knight.cpp |
| `Relish in Blood` | sc_death_knight.cpp |
| `Ride or Die!` | sc_death_knight.cpp |
| `Rider's Champion` | sc_death_knight.cpp |
| `Rune Carved Plates` | sc_death_knight.cpp |
| `Rune Mastery` | sc_death_knight.cpp |
| `Runic Attenuation` | sc_death_knight.cpp |
| `Runic Command` | sc_death_knight.cpp |
| `Runic Overflow` | sc_death_knight.cpp |
| `Runic Protection` | sc_death_knight.cpp |
| `Sanguinary Burst` | sc_death_knight.cpp |
| `Sanguine Ground` | sc_death_knight.cpp |
| `Sanguine Scent` | sc_death_knight.cpp |
| `Scourge Strike` | sc_death_knight.cpp |
| `Scourging` | sc_death_knight.cpp |
| `Scythe of Decay` | sc_death_knight.cpp |
| `Shattering Blade` | sc_death_knight.cpp |
| `Smothering Offense` | sc_death_knight.cpp |
| `Soul Reaper` | sc_death_knight.cpp |
| `Soul Rupture` | sc_death_knight.cpp |
| `Subduing Grasp` | sc_death_knight.cpp |
| `Sudden Doom` | sc_death_knight.cpp |
| `Summon Gargoyle` | sc_death_knight.cpp |
| `Superstrain` | sc_death_knight.cpp |
| `Suppression` | sc_death_knight.cpp |
| `The Blood is Life` | sc_death_knight.cpp |
| `The Long Winter` | sc_death_knight.cpp |
| `Thrill of Blood` | sc_death_knight.cpp |
| `Transfusion` | sc_death_knight.cpp |
| `Trollbane's Icy Fury` | sc_death_knight.cpp |
| `Umbilicus Eternus` | sc_death_knight.cpp |
| `Unholy Armaments` | sc_death_knight.cpp |
| `Unholy Aura` | sc_death_knight.cpp |
| `Unholy Bond` | sc_death_knight.cpp |
| `Unholy Devotion` | sc_death_knight.cpp |
| `Unholy Endurance` | sc_death_knight.cpp |
| `Unholy Momentum` | sc_death_knight.cpp |
| `Unyielding Will` | sc_death_knight.cpp |
| `Vampiric Aura` | sc_death_knight.cpp |
| `Vampiric Blood` | sc_death_knight.cpp |
| `Vampiric Speed` | sc_death_knight.cpp |
| `Vampiric Strike` | sc_death_knight.cpp |
| `Vestigial Shell` | sc_death_knight.cpp |
| `Veteran of the Third War` | sc_death_knight.cpp |
| `Visceral Strength` | sc_death_knight.cpp |
| `Voracious` | sc_death_knight.cpp |
| `Wave of Souls` | sc_death_knight.cpp |
| `Whitemane's Famine` | sc_death_knight.cpp |
| `Will of the Necropolis` | sc_death_knight.cpp |
| `Wither Away` | sc_death_knight.cpp |
| `Wraith Walk` | sc_death_knight.cpp |

## Druid (270 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Abundance` | sc_druid.cpp |
| `Aessina's Renewal` | sc_druid.cpp |
| `Aetherial Kindling` | sc_druid.cpp |
| `After the Wildfire` | sc_druid.cpp |
| `Aggravate Wounds` | sc_druid.cpp |
| `Apex Predator's Craving` | sc_druid.cpp |
| `Ashamane's Guidance` | sc_druid.cpp |
| `Astral Communion` | sc_druid.cpp |
| `Astral Influence` | sc_druid.cpp |
| `Astral Insight` | sc_druid.cpp |
| `Atmospheric Exposure` | sc_druid.cpp |
| `Balance of All Things` | sc_druid.cpp |
| `Bask in Moonlight` | sc_druid.cpp |
| `Berserk: Heart of the Lion` | sc_druid.cpp |
| `Bestial Strength` | sc_druid.cpp |
| `Blood Frenzy` | sc_druid.cpp |
| `Blood Spattered` | sc_druid.cpp |
| `Blooming Infusion` | sc_druid.cpp |
| `Bond with Nature` | sc_druid.cpp |
| `Boundless Moonlight` | sc_druid.cpp |
| `Bounteous Bloom` | sc_druid.cpp |
| `Brambles` | sc_druid.cpp |
| `Bristling Fur` | sc_druid.cpp |
| `Bursting Growth` | sc_druid.cpp |
| `Call of the Elder Druid` | sc_druid.cpp |
| `Carnivorous Instinct` | sc_druid.cpp |
| `Celestial Alignment` | sc_druid.cpp |
| `Celestial Fire` | sc_druid.cpp |
| `Cenarius' Guidance` | sc_druid.cpp |
| `Cenarius' Might` | sc_druid.cpp |
| `Chomp` | sc_druid.cpp |
| `Circle of Life and Death` | sc_druid.cpp |
| `Circle of the Heavens` | sc_druid.cpp |
| `Circle of the Wild` | sc_druid.cpp |
| `Claw Rampage` | sc_druid.cpp |
| `Coiled to Spring` | sc_druid.cpp |
| `Control of the Dream` | sc_druid.cpp |
| `Convoke the Spirits` | sc_druid.cpp |
| `Cosmic Rapidity` | sc_druid.cpp |
| `Cultivation` | sc_druid.cpp |
| `Cyclone` | sc_druid.cpp |
| `Denizen of the Dream` | sc_druid.cpp |
| `Dreadful Bleeding` | sc_druid.cpp |
| `Dreadful Wound` | sc_druid.cpp |
| `Dream Guide` | sc_druid.cpp |
| `Dream Surge` | sc_druid.cpp |
| `Dream of Cenarius` | sc_druid.cpp |
| `Dryad's Dance` | sc_druid.cpp |
| `Durability of Nature` | sc_druid.cpp |
| `Early Spring` | sc_druid.cpp |
| `Eclipse` | sc_druid.cpp |
| `Efflorescence` | sc_druid.cpp |
| `Elune's Challenge` | sc_druid.cpp |
| `Elune's Favored` | sc_druid.cpp |
| `Elune's Grace` | sc_druid.cpp |
| `Elune's Guidance` | sc_druid.cpp |
| `Embrace of the Dream` | sc_druid.cpp |
| `Empowered Shapeshifting` | sc_druid.cpp |
| `Entangling Vortex` | sc_druid.cpp |
| `Everbloom` | sc_druid.cpp |
| `Exacerbating Wounds` | sc_druid.cpp |
| `Expansiveness` | sc_druid.cpp |
| `Feline Swiftness` | sc_druid.cpp |
| `Feral Frenzy` | sc_druid.cpp |
| `Flashing Claws` | sc_druid.cpp |
| `Flourish` | sc_druid.cpp |
| `Flower Walk` | sc_druid.cpp |
| `Fluid Form` | sc_druid.cpp |
| `Force of Nature` | sc_druid.cpp |
| `Forestwalk` | sc_druid.cpp |
| `Fount of Strength` | sc_druid.cpp |
| `Frantic Frenzy` | sc_druid.cpp |
| `Frantic Momentum` | sc_druid.cpp |
| `Front of the Pack` | sc_druid.cpp |
| `Fury of Elune` | sc_druid.cpp |
| `Fury of Nature` | sc_druid.cpp |
| `Galactic Guardian` | sc_druid.cpp |
| `Gale Winds` | sc_druid.cpp |
| `Germination` | sc_druid.cpp |
| `Gift of an Ancient Guardian` | sc_druid.cpp |
| `Glistening Fur` | sc_druid.cpp |
| `Gory Fur` | sc_druid.cpp |
| `Green Thumb` | sc_druid.cpp |
| `Grievous Wounds` | sc_druid.cpp |
| `Grove Guardians` | sc_druid.cpp |
| `Grove's Inspiration` | sc_druid.cpp |
| `Guardian of Elune` | sc_druid.cpp |
| `Hail of Stars` | sc_druid.cpp |
| `Harmonious Blooming` | sc_druid.cpp |
| `Harmonious Constitution` | sc_druid.cpp |
| `Harmony of the Grove` | sc_druid.cpp |
| `Harmony of the Heavens` | sc_druid.cpp |
| `Harnessed Rage` | sc_druid.cpp |
| `Hibernate` | sc_druid.cpp |
| `Hunger for Battle` | sc_druid.cpp |
| `Hunt Beneath the Open Skies` | sc_druid.cpp |
| `Implant` | sc_druid.cpp |
| `Improved Barkskin` | sc_druid.cpp |
| `Improved Eclipse` | sc_druid.cpp |
| `Improved Ironbark` | sc_druid.cpp |
| `Improved Nature's Cure` | sc_druid.cpp |
| `Improved Regrowth` | sc_druid.cpp |
| `Improved Stampeding Roar` | sc_druid.cpp |
| `Improved Swiftmend` | sc_druid.cpp |
| `Improved Wild Growth` | sc_druid.cpp |
| `Incapacitating Roar` | sc_druid.cpp |
| `Incarnation: Avatar of Ashamane` | sc_druid.cpp |
| `Incarnation: Chosen of Elune` | sc_druid.cpp |
| `Incarnation: Guardian of Ursoc` | sc_druid.cpp |
| `Incarnation: Tree of Life` | sc_druid.cpp |
| `Incessant Tempest` | sc_druid.cpp |
| `Infected Wounds` | sc_druid.cpp |
| `Innate Resolve` | sc_druid.cpp |
| `Innervate` | sc_druid.cpp |
| `Instincts of the Claw` | sc_druid.cpp |
| `Intensity` | sc_druid.cpp |
| `Ironbark` | sc_druid.cpp |
| `Ironfur` | sc_druid.cpp |
| `Killing Blow` | sc_druid.cpp |
| `Killing Strikes` | sc_druid.cpp |
| `Lifebloom` | sc_druid.cpp |
| `Lifetreading` | sc_druid.cpp |
| `Limb from Limb` | sc_druid.cpp |
| `Lingering Healing` | sc_druid.cpp |
| `Liveliness` | sc_druid.cpp |
| `Lore of the Grove` | sc_druid.cpp |
| `Lunar Beam` | sc_druid.cpp |
| `Lunar Calling` | sc_druid.cpp |
| `Lunar Insight` | sc_druid.cpp |
| `Lunar Inspiration` | sc_druid.cpp |
| `Lunation` | sc_druid.cpp |
| `Lycara's Inspiration` | sc_druid.cpp |
| `Lycara's Teachings` | sc_druid.cpp |
| `Maim` | sc_druid.cpp |
| `Mass Entanglement` | sc_druid.cpp |
| `Master Shapeshifter` | sc_druid.cpp |
| `Matted Fur` | sc_druid.cpp |
| `Maul` | sc_druid.cpp |
| `Memory of Ysera` | sc_druid.cpp |
| `Merciless Claws` | sc_druid.cpp |
| `Mighty Bash` | sc_druid.cpp |
| `Moment of Clarity` | sc_druid.cpp |
| `Moon Guardian` | sc_druid.cpp |
| `Moondust` | sc_druid.cpp |
| `Moonkin Form` | sc_druid.cpp |
| `Moonless Night` | sc_druid.cpp |
| `New Moon` | sc_druid.cpp |
| `Nurturing Dormancy` | sc_druid.cpp |
| `Nurturing Instinct` | sc_druid.cpp |
| `Oakskin` | sc_druid.cpp |
| `Omen of Clarity` | sc_druid.cpp |
| `Orbit Breaker` | sc_druid.cpp |
| `Orbital Strike` | sc_druid.cpp |
| `Pack's Endurance` | sc_druid.cpp |
| `Panther's Guile` | sc_druid.cpp |
| `Passing Seasons` | sc_druid.cpp |
| `Patient Custodian` | sc_druid.cpp |
| `Penumbral Swell` | sc_druid.cpp |
| `Perfectly-Honed Instincts` | sc_druid.cpp |
| `Persistence` | sc_druid.cpp |
| `Photosynthesis` | sc_druid.cpp |
| `Potent Enchantments` | sc_druid.cpp |
| `Pouncing Strikes` | sc_druid.cpp |
| `Power of Goldrinn` | sc_druid.cpp |
| `Power of Nature` | sc_druid.cpp |
| `Power of the Archdruid` | sc_druid.cpp |
| `Power of the Dream` | sc_druid.cpp |
| `Predator` | sc_druid.cpp |
| `Primal Fury` | sc_druid.cpp |
| `Primal Wrath` | sc_druid.cpp |
| `Prosperity` | sc_druid.cpp |
| `Protective Growth` | sc_druid.cpp |
| `Radiant Moonlight` | sc_druid.cpp |
| `Raging Fury` | sc_druid.cpp |
| `Rake` | sc_druid.cpp |
| `Rattle the Stars` | sc_druid.cpp |
| `Ravage` | sc_druid.cpp |
| `Raze` | sc_druid.cpp |
| `Red Moon` | sc_druid.cpp |
| `Reforestation` | sc_druid.cpp |
| `Regenerative Heartwood` | sc_druid.cpp |
| `Regenesis` | sc_druid.cpp |
| `Reinforced Fur` | sc_druid.cpp |
| `Rejuvenation` | sc_druid.cpp |
| `Remove Corruption` | sc_druid.cpp |
| `Rend and Tear` | sc_druid.cpp |
| `Renewing Surge` | sc_druid.cpp |
| `Resilient Flourishing` | sc_druid.cpp |
| `Rip` | sc_druid.cpp |
| `Rip and Tear` | sc_druid.cpp |
| `Root Network` | sc_druid.cpp |
| `Ruthless Aggression` | sc_druid.cpp |
| `Saber Jaws` | sc_druid.cpp |
| `Sabertooth` | sc_druid.cpp |
| `Scintillating Moonlight` | sc_druid.cpp |
| `Sculpt the Stars` | sc_druid.cpp |
| `Shooting Stars` | sc_druid.cpp |
| `Skull Bash` | sc_druid.cpp |
| `Solar Beam` | sc_druid.cpp |
| `Solstice` | sc_druid.cpp |
| `Soothe` | sc_druid.cpp |
| `Soul of the Forest` | sc_druid.cpp |
| `Stampeding Roar` | sc_druid.cpp |
| `Star Cascade` | sc_druid.cpp |
| `Starfire` | sc_druid.cpp |
| `Starlight Conduit` | sc_druid.cpp |
| `Starlord` | sc_druid.cpp |
| `Starsurge` | sc_druid.cpp |
| `Starweaver` | sc_druid.cpp |
| `Stellar Amplification` | sc_druid.cpp |
| `Stellar Command` | sc_druid.cpp |
| `Stonebark` | sc_druid.cpp |
| `Strike for the Heart` | sc_druid.cpp |
| `Sudden Ambush` | sc_druid.cpp |
| `Sunseeker Mushroom` | sc_druid.cpp |
| `Survival Instincts` | sc_druid.cpp |
| `Swiftmend` | sc_druid.cpp |
| `Swipe` | sc_druid.cpp |
| `Sylvan Beckoning` | sc_druid.cpp |
| `Symbiotic Relationship` | sc_druid.cpp |
| `Taste for Blood` | sc_druid.cpp |
| `Tear Down the Mighty` | sc_druid.cpp |
| `The Eternal Moon` | sc_druid.cpp |
| `The Light of Elune` | sc_druid.cpp |
| `Thick Hide` | sc_druid.cpp |
| `Thriving Growth` | sc_druid.cpp |
| `Thriving Vegetation` | sc_druid.cpp |
| `Tireless Energy` | sc_druid.cpp |
| `Total Eclipse` | sc_druid.cpp |
| `Touch the Cosmos` | sc_druid.cpp |
| `Tranquil Mind` | sc_druid.cpp |
| `Tranquility` | sc_druid.cpp |
| `Treants of the Moon` | sc_druid.cpp |
| `Twin Claw` | sc_druid.cpp |
| `Twin Moonfire` | sc_druid.cpp |
| `Twin Moons` | sc_druid.cpp |
| `Twin Sprouts` | sc_druid.cpp |
| `Typhoon` | sc_druid.cpp |
| `Umbral Intensity` | sc_druid.cpp |
| `Unseen Predator` | sc_druid.cpp |
| `Unstoppable Growth` | sc_druid.cpp |
| `Untamed Savagery` | sc_druid.cpp |
| `Ursine Vigor` | sc_druid.cpp |
| `Ursoc's Endurance` | sc_druid.cpp |
| `Ursoc's Fury` | sc_druid.cpp |
| `Ursoc's Guidance` | sc_druid.cpp |
| `Ursoc's Spirit` | sc_druid.cpp |
| `Ursol's Vortex` | sc_druid.cpp |
| `Ursol's Warding` | sc_druid.cpp |
| `Veinripper` | sc_druid.cpp |
| `Verdancy` | sc_druid.cpp |
| `Verdant Heart` | sc_druid.cpp |
| `Verdant Infusion` | sc_druid.cpp |
| `Vulnerable Flesh` | sc_druid.cpp |
| `Waking Dream` | sc_druid.cpp |
| `Waking Nightmare` | sc_druid.cpp |
| `Ward of the Forest` | sc_druid.cpp |
| `Well-Honed Instincts` | sc_druid.cpp |
| `Whirling Stars` | sc_druid.cpp |
| `Wild Charge` | sc_druid.cpp |
| `Wild Growth` | sc_druid.cpp |
| `Wild Guardian` | sc_druid.cpp |
| `Wild Mushroom` | sc_druid.cpp |
| `Wild Slashes` | sc_druid.cpp |
| `Wild Surges` | sc_druid.cpp |
| `Wild Synthesis` | sc_druid.cpp |
| `Wildpower Surge` | sc_druid.cpp |
| `Wildshape Mastery` | sc_druid.cpp |
| `Wildstalker's Power` | sc_druid.cpp |
| `Ysera's Gift` | sc_druid.cpp |

## Evoker (167 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Accretion` | sc_evoker.cpp |
| `Aerial Mastery` | sc_evoker.cpp |
| `Anachronism` | sc_evoker.cpp |
| `Ancient Flame` | sc_evoker.cpp |
| `Animosity` | sc_evoker.cpp |
| `Ashes in Motion` | sc_evoker.cpp |
| `Attuned to the Dream` | sc_evoker.cpp |
| `Azure Celerity` | sc_evoker.cpp |
| `Azure Essence Burst` | sc_evoker.cpp |
| `Azure Sweep` | sc_evoker.cpp |
| `Blast Furnace` | sc_evoker.cpp |
| `Blistering Scales` | sc_evoker.cpp |
| `Bombardments` | sc_evoker.cpp |
| `Bountiful Bloom` | sc_evoker.cpp |
| `Breath of Eons` | sc_evoker.cpp |
| `Breath of Sindragosa` | sc_evoker.cpp |
| `Burning Adrenaline` | sc_evoker.cpp |
| `Catalyze` | sc_evoker.cpp |
| `Causality` | sc_evoker.cpp |
| `Celestial Alignment` | sc_evoker.cpp |
| `Chrono Flame` | sc_evoker.cpp |
| `Chronoboon` | sc_evoker.cpp |
| `Clairvoyant` | sc_evoker.cpp |
| `Command Squadron` | sc_evoker.cpp |
| `Commander of the Dead` | sc_evoker.cpp |
| `Conduit of Flame` | sc_evoker.cpp |
| `Consume Flame` | sc_evoker.cpp |
| `Coordinated Assault` | sc_evoker.cpp |
| `Dark Ascension` | sc_evoker.cpp |
| `Dark Transformation` | sc_evoker.cpp |
| `Deep Exhalation` | sc_evoker.cpp |
| `Defile` | sc_evoker.cpp |
| `Diverted Power` | sc_evoker.cpp |
| `Draconic Instincts` | sc_evoker.cpp |
| `Draconic Legacy` | sc_evoker.cpp |
| `Dragonrage` | sc_evoker.cpp |
| `Dream of Spring` | sc_evoker.cpp |
| `Ebon Might` | sc_evoker.cpp |
| `Echoing Strike` | sc_evoker.cpp |
| `Empower Rune Weapon` | sc_evoker.cpp |
| `Energy Cycles` | sc_evoker.cpp |
| `Engulfing Blaze` | sc_evoker.cpp |
| `Enkindle` | sc_evoker.cpp |
| `Enkindled` | sc_evoker.cpp |
| `Eruption` | sc_evoker.cpp |
| `Essence Attunement` | sc_evoker.cpp |
| `Essence Burst` | sc_evoker.cpp |
| `Essence Well` | sc_evoker.cpp |
| `Eternity Surge` | sc_evoker.cpp |
| `Eternity's Span` | sc_evoker.cpp |
| `Event Horizon` | sc_evoker.cpp |
| `Expanded Lungs` | sc_evoker.cpp |
| `Expunge` | sc_evoker.cpp |
| `Extended Battle` | sc_evoker.cpp |
| `Extended Flight` | sc_evoker.cpp |
| `Exuberance` | sc_evoker.cpp |
| `Eye of Infinity` | sc_evoker.cpp |
| `Fan the Flames` | sc_evoker.cpp |
| `Fate Mirror` | sc_evoker.cpp |
| `Feed the Flames` | sc_evoker.cpp |
| `Fire Torrent` | sc_evoker.cpp |
| `Font of Magic` | sc_evoker.cpp |
| `Forger of Mountains` | sc_evoker.cpp |
| `Fulminous Roar` | sc_evoker.cpp |
| `Golden Opportunity` | sc_evoker.cpp |
| `Hardened Scales` | sc_evoker.cpp |
| `Heat Wave` | sc_evoker.cpp |
| `Honed Aggression` | sc_evoker.cpp |
| `Icy Veins` | sc_evoker.cpp |
| `Imminent Destruction` | sc_evoker.cpp |
| `Imposing Presence` | sc_evoker.cpp |
| `Improved Defy Fate` | sc_evoker.cpp |
| `Incarnation: Chosen of Elune` | sc_evoker.cpp |
| `Inherent Resistance` | sc_evoker.cpp |
| `Innate Magic` | sc_evoker.cpp |
| `Instability Matrix` | sc_evoker.cpp |
| `Instinctive Arcana` | sc_evoker.cpp |
| `Interwoven Threads` | sc_evoker.cpp |
| `Iridescence` | sc_evoker.cpp |
| `Landslide` | sc_evoker.cpp |
| `Lay Waste` | sc_evoker.cpp |
| `Leaping Flames` | sc_evoker.cpp |
| `Legacy of the Lifebinder` | sc_evoker.cpp |
| `Lifecinders` | sc_evoker.cpp |
| `Lush Growth` | sc_evoker.cpp |
| `Maneuverability` | sc_evoker.cpp |
| `Mass Eruption` | sc_evoker.cpp |
| `Master of Destiny` | sc_evoker.cpp |
| `Melt Armor` | sc_evoker.cpp |
| `Menacing Presence` | sc_evoker.cpp |
| `Might of the Black Dragonflight` | sc_evoker.cpp |
| `Molten Blood` | sc_evoker.cpp |
| `Molten Embers` | sc_evoker.cpp |
| `Momentum Shift` | sc_evoker.cpp |
| `Motes of Acceleration` | sc_evoker.cpp |
| `Motes of Possibility` | sc_evoker.cpp |
| `Nimble Flyer` | sc_evoker.cpp |
| `Nozdormu Adept` | sc_evoker.cpp |
| `Obsidian Bulwark` | sc_evoker.cpp |
| `Obsidian Scales` | sc_evoker.cpp |
| `Onslaught` | sc_evoker.cpp |
| `Onyx Legacy` | sc_evoker.cpp |
| `Oppressing Roar` | sc_evoker.cpp |
| `Overawe` | sc_evoker.cpp |
| `Overclock` | sc_evoker.cpp |
| `Overlord` | sc_evoker.cpp |
| `Panacea` | sc_evoker.cpp |
| `Pillar of Frost` | sc_evoker.cpp |
| `Plot the Future` | sc_evoker.cpp |
| `Potent Mana` | sc_evoker.cpp |
| `Power Nexus` | sc_evoker.cpp |
| `Power Swell` | sc_evoker.cpp |
| `Prescience` | sc_evoker.cpp |
| `Primacy` | sc_evoker.cpp |
| `Protracted Talons` | sc_evoker.cpp |
| `Pupil of Alexstrasza` | sc_evoker.cpp |
| `Pyre` | sc_evoker.cpp |
| `Quell` | sc_evoker.cpp |
| `Reactive Hide` | sc_evoker.cpp |
| `Refined Essence` | sc_evoker.cpp |
| `Regenerative Chitin` | sc_evoker.cpp |
| `Regenerative Magic` | sc_evoker.cpp |
| `Ricocheting Pyroclast` | sc_evoker.cpp |
| `Roar of Exhilaration` | sc_evoker.cpp |
| `Ruby Embers` | sc_evoker.cpp |
| `Ruby Essence Burst` | sc_evoker.cpp |
| `Scarlet Adaptation` | sc_evoker.cpp |
| `Scintillation` | sc_evoker.cpp |
| `Serenity` | sc_evoker.cpp |
| `Shadow Dance` | sc_evoker.cpp |
| `Shape of flame` | sc_evoker.cpp |
| `Shattering Stars` | sc_evoker.cpp |
| `Slipstream` | sc_evoker.cpp |
| `Spellweaver's Dominance` | sc_evoker.cpp |
| `Star Salvo` | sc_evoker.cpp |
| `Strafing Run` | sc_evoker.cpp |
| `Strike from Above` | sc_evoker.cpp |
| `Tailwind` | sc_evoker.cpp |
| `Tectonic Locus` | sc_evoker.cpp |
| `Temporal Burst` | sc_evoker.cpp |
| `Temporality` | sc_evoker.cpp |
| `Time Convergence` | sc_evoker.cpp |
| `Time Skip` | sc_evoker.cpp |
| `Time Spiral` | sc_evoker.cpp |
| `Tip the Scales` | sc_evoker.cpp |
| `Titanic Precision` | sc_evoker.cpp |
| `Titanic Wrath` | sc_evoker.cpp |
| `Tomorrow, Today` | sc_evoker.cpp |
| `Trailblazer` | sc_evoker.cpp |
| `Twin Flame` | sc_evoker.cpp |
| `Unholy Assault` | sc_evoker.cpp |
| `Unravel` | sc_evoker.cpp |
| `Unrelenting Siege` | sc_evoker.cpp |
| `Unyielding Domain` | sc_evoker.cpp |
| `Verdant Embrace` | sc_evoker.cpp |
| `Void Eruption` | sc_evoker.cpp |
| `Volatility` | sc_evoker.cpp |
| `Volcanism` | sc_evoker.cpp |
| `Walloping Blow` | sc_evoker.cpp |
| `Wingleader` | sc_evoker.cpp |
| `upheaval` | sc_evoker.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1259173 | sc_evoker.cpp |
| 1259174 | sc_evoker.cpp |
| 1259175 | sc_evoker.cpp |
| 1271687 | sc_evoker.cpp |
| 1271788 | sc_evoker.cpp |
| 1271796 | sc_evoker.cpp |

## Hunter (250 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `A Fire Inside` | sc_demon_hunter.cpp |
| `Accelerated Blade` | sc_demon_hunter.cpp |
| `Agonizing Flames` | sc_demon_hunter.cpp |
| `Aldrachi Design` | sc_demon_hunter.cpp |
| `Aldrachi Tactics` | sc_demon_hunter.cpp |
| `Animal Companion` | sc_hunter.cpp |
| `Army Unto Oneself` | sc_demon_hunter.cpp |
| `Art of the Glaive` | sc_demon_hunter.cpp |
| `Ascending Flame` | sc_demon_hunter.cpp |
| `Aspect of the Hydra` | sc_hunter.cpp |
| `Aura of Pain` | sc_demon_hunter.cpp |
| `Avian Specialization` | sc_hunter.cpp |
| `Banshee's Mark` | sc_hunter.cpp |
| `Better Together` | sc_hunter.cpp |
| `Black Arrow` | sc_hunter.cpp |
| `Blackrock Munitions` | sc_hunter.cpp |
| `Bladecraft` | sc_demon_hunter.cpp |
| `Blazing Path` | sc_demon_hunter.cpp |
| `Bleak Arrows` | sc_hunter.cpp |
| `Bleak Powder` | sc_hunter.cpp |
| `Bloody Claws` | sc_hunter.cpp |
| `Bloody Frenzy` | sc_hunter.cpp |
| `Bouncing Glaives` | sc_demon_hunter.cpp |
| `Broken Spirit` | sc_demon_hunter.cpp |
| `Bullet Hell` | sc_hunter.cpp |
| `Burn It Out` | sc_demon_hunter.cpp |
| `Burning Alive` | sc_demon_hunter.cpp |
| `Burning Blood` | sc_demon_hunter.cpp |
| `Burning Hatred` | sc_demon_hunter.cpp |
| `Burning Wound` | sc_demon_hunter.cpp |
| `Calamitous` | sc_demon_hunter.cpp |
| `Calcified Spikes` | sc_demon_hunter.cpp |
| `Calling the Shots` | sc_hunter.cpp |
| `Can't Miss, Won't Miss` | sc_hunter.cpp |
| `Catastrophe` | sc_demon_hunter.cpp |
| `Celestial Echoes` | sc_demon_hunter.cpp |
| `Chains of Anger` | sc_demon_hunter.cpp |
| `Chaos Nova` | sc_demon_hunter.cpp |
| `Chaos Theory` | sc_demon_hunter.cpp |
| `Chaotic Disposition` | sc_demon_hunter.cpp |
| `Chaotic Transformation` | sc_demon_hunter.cpp |
| `Charred Flesh` | sc_demon_hunter.cpp |
| `Charred Warglaives` | sc_demon_hunter.cpp |
| `Collapsing Star` | sc_demon_hunter.cpp |
| `Collective Anguish` | sc_demon_hunter.cpp |
| `Consume Magic` | sc_demon_hunter.cpp |
| `Corpsecaller` | sc_hunter.cpp |
| `Critical Chaos` | sc_demon_hunter.cpp |
| `Cycle of Binding` | sc_demon_hunter.cpp |
| `Cycle of Hatred` | sc_demon_hunter.cpp |
| `Dancing with Fate` | sc_demon_hunter.cpp |
| `Dark Matter` | sc_demon_hunter.cpp |
| `Darkglare Boon` | sc_demon_hunter.cpp |
| `Darkness` | sc_demon_hunter.cpp |
| `Dash of Chaos` | sc_demon_hunter.cpp |
| `Deadeye` | sc_hunter.cpp |
| `Deflecting Dance` | sc_demon_hunter.cpp |
| `Desperate Instincts` | sc_demon_hunter.cpp |
| `Devourer's Bite` | sc_demon_hunter.cpp |
| `Devourer's Edge` | sc_demon_hunter.cpp |
| `Dire Summons` | sc_hunter.cpp |
| `Disrupting Fury` | sc_demon_hunter.cpp |
| `Don't Look Back` | sc_hunter.cpp |
| `Doomsayer` | sc_demon_hunter.cpp |
| `Down in Flames` | sc_demon_hunter.cpp |
| `Duty Eternal` | sc_demon_hunter.cpp |
| `Ebon Bowstring` | sc_hunter.cpp |
| `Emptiness` | sc_demon_hunter.cpp |
| `Entropy` | sc_demon_hunter.cpp |
| `Eradicate` | sc_demon_hunter.cpp |
| `Erratic Felheart` | sc_demon_hunter.cpp |
| `Essence Break` | sc_demon_hunter.cpp |
| `Eternal Hunt` | sc_demon_hunter.cpp |
| `Exergy` | sc_demon_hunter.cpp |
| `Eye Beam` | sc_demon_hunter.cpp |
| `Fallout` | sc_demon_hunter.cpp |
| `Feast of Souls` | sc_demon_hunter.cpp |
| `Feed the Demon` | sc_demon_hunter.cpp |
| `Fel Devastation` | sc_demon_hunter.cpp |
| `Fel Flame Fortification` | sc_demon_hunter.cpp |
| `Felblade` | sc_demon_hunter.cpp |
| `Felbound` | sc_demon_hunter.cpp |
| `Felfire Fist` | sc_demon_hunter.cpp |
| `Felfire Haste` | sc_demon_hunter.cpp |
| `Fiery Brand` | sc_demon_hunter.cpp |
| `Fiery Demise` | sc_demon_hunter.cpp |
| `First Blood` | sc_demon_hunter.cpp |
| `Frailty` | sc_demon_hunter.cpp |
| `Furious` | sc_demon_hunter.cpp |
| `Furious Gaze` | sc_demon_hunter.cpp |
| `Furious Throws` | sc_demon_hunter.cpp |
| `Fury of the Aldrachi` | sc_demon_hunter.cpp |
| `Fury of the Wyvern` | sc_hunter.cpp |
| `Glaive Tempest` | sc_demon_hunter.cpp |
| `Growing Inferno` | sc_demon_hunter.cpp |
| `Guile` | sc_demon_hunter.cpp |
| `Harness the Cosmos` | sc_demon_hunter.cpp |
| `Headshot` | sc_hunter.cpp |
| `Hogstrider` | sc_hunter.cpp |
| `Hoof and Blade` | sc_hunter.cpp |
| `Howl of the Pack Leader` | sc_hunter.cpp |
| `Hungering Slash` | sc_demon_hunter.cpp |
| `Illidari Knowledge` | sc_demon_hunter.cpp |
| `Impending Apocalypse` | sc_demon_hunter.cpp |
| `Imprison` | sc_demon_hunter.cpp |
| `Improved Chaos Strike` | sc_demon_hunter.cpp |
| `Improved Consume` | sc_demon_hunter.cpp |
| `Improved Disrupt` | sc_demon_hunter.cpp |
| `Improved Sigil of Misery` | sc_demon_hunter.cpp |
| `Incisive Blade` | sc_demon_hunter.cpp |
| `Incorruptible Spirit` | sc_demon_hunter.cpp |
| `Inertia` | sc_demon_hunter.cpp |
| `Initiative` | sc_demon_hunter.cpp |
| `Internal Struggle` | sc_demon_hunter.cpp |
| `Invigorating Pulse` | sc_hunter.cpp |
| `Isolated Prey` | sc_demon_hunter.cpp |
| `Keen Edge` | sc_demon_hunter.cpp |
| `Keen Engagement` | sc_demon_hunter.cpp |
| `Know Your Enemy` | sc_demon_hunter.cpp |
| `Last Resort` | sc_demon_hunter.cpp |
| `Live by the Glaive` | sc_demon_hunter.cpp |
| `Long Night` | sc_demon_hunter.cpp |
| `Lost in Darkness` | sc_demon_hunter.cpp |
| `Lunar Calling` | sc_hunter.cpp |
| `Lunar Storm` | sc_hunter.cpp |
| `Mass Acceleration` | sc_demon_hunter.cpp |
| `Midnight` | sc_demon_hunter.cpp |
| `Moment of Craving` | sc_demon_hunter.cpp |
| `Mongoose Rounds` | sc_hunter.cpp |
| `Moon's Blessing` | sc_hunter.cpp |
| `Moonlight Chakram` | sc_hunter.cpp |
| `Mortal Dance` | sc_demon_hunter.cpp |
| `Netherwalk` | sc_demon_hunter.cpp |
| `No Mercy` | sc_hunter.cpp |
| `Obsidian Arrowhead` | sc_hunter.cpp |
| `On Target` | sc_hunter.cpp |
| `Open Fire` | sc_hunter.cpp |
| `Otherworldly Focus` | sc_demon_hunter.cpp |
| `Pack Mentality` | sc_hunter.cpp |
| `Pact of the Hollow` | sc_hunter.cpp |
| `Painbringer` | sc_demon_hunter.cpp |
| `Path to Oblivion` | sc_demon_hunter.cpp |
| `Perfectly Balanced Glaive` | sc_demon_hunter.cpp |
| `Phase Shift` | sc_demon_hunter.cpp |
| `Pitch Black` | sc_demon_hunter.cpp |
| `Predator's Thirst` | sc_demon_hunter.cpp |
| `Preemptive Strike` | sc_demon_hunter.cpp |
| `Pursuit` | sc_demon_hunter.cpp |
| `Quickened Sigils` | sc_demon_hunter.cpp |
| `Radiant Edge` | sc_hunter.cpp |
| `Ragefire` | sc_demon_hunter.cpp |
| `Reaver's Mark` | sc_demon_hunter.cpp |
| `Relentless Onslaught` | sc_demon_hunter.cpp |
| `Remorseless` | sc_demon_hunter.cpp |
| `Retaliation` | sc_demon_hunter.cpp |
| `Revel in Pain` | sc_demon_hunter.cpp |
| `Roaring Fire` | sc_demon_hunter.cpp |
| `Rolling Torment` | sc_demon_hunter.cpp |
| `Ruinous Bulwark` | sc_demon_hunter.cpp |
| `Scars of Suffering` | sc_demon_hunter.cpp |
| `Screaming Brutality` | sc_demon_hunter.cpp |
| `Scythe's Embrace` | sc_demon_hunter.cpp |
| `Second Helping` | sc_demon_hunter.cpp |
| `Sentinel` | sc_hunter.cpp |
| `Serrated Glaive` | sc_demon_hunter.cpp |
| `Sharpened Claws` | sc_hunter.cpp |
| `Sharpened Fangs` | sc_hunter.cpp |
| `Shattered Destiny` | sc_demon_hunter.cpp |
| `Shattered Restoration` | sc_demon_hunter.cpp |
| `Shrapnel Bomb` | sc_hunter.cpp |
| `Shrapnel Shot` | sc_hunter.cpp |
| `Sic 'Em` | sc_hunter.cpp |
| `Sigil of Chains` | sc_demon_hunter.cpp |
| `Sigil of Misery` | sc_demon_hunter.cpp |
| `Sigil of Silence` | sc_demon_hunter.cpp |
| `Sigil of Spite` | sc_demon_hunter.cpp |
| `Singed Spirit` | sc_demon_hunter.cpp |
| `Singular Strikes` | sc_demon_hunter.cpp |
| `Snakeskin Quiver` | sc_hunter.cpp |
| `Solitary Companion` | sc_hunter.cpp |
| `Soul Barrier` | sc_demon_hunter.cpp |
| `Soul Carver` | sc_demon_hunter.cpp |
| `Soul Cleanse` | sc_demon_hunter.cpp |
| `Soul Drinker` | sc_hunter.cpp |
| `Soul Glutton` | sc_demon_hunter.cpp |
| `Soul Immolation` | sc_demon_hunter.cpp |
| `Soul Rending` | sc_demon_hunter.cpp |
| `Soul Sigils` | sc_demon_hunter.cpp |
| `Soul Splitter` | sc_demon_hunter.cpp |
| `Soulcrush` | sc_demon_hunter.cpp |
| `Soulforged Blades` | sc_demon_hunter.cpp |
| `Soulmonger` | sc_demon_hunter.cpp |
| `Soulscar` | sc_demon_hunter.cpp |
| `Soulshaper` | sc_demon_hunter.cpp |
| `Spontaneous Immolation` | sc_demon_hunter.cpp |
| `Stalk and Strike` | sc_hunter.cpp |
| `Stampede!` | sc_hunter.cpp |
| `Star Fragments` | sc_demon_hunter.cpp |
| `Stargazer` | sc_hunter.cpp |
| `State of Matter` | sc_demon_hunter.cpp |
| `Stoke the Flames` | sc_demon_hunter.cpp |
| `Swallowed Anger` | sc_demon_hunter.cpp |
| `Sweet Release` | sc_demon_hunter.cpp |
| `Sweet Suffering` | sc_demon_hunter.cpp |
| `Tar Trap` | sc_hunter.cpp |
| `Tempered Soul` | sc_demon_hunter.cpp |
| `Tempered Steel` | sc_demon_hunter.cpp |
| `Tenacious` | sc_hunter.cpp |
| `The Bell Tolls` | sc_hunter.cpp |
| `The Hunt` | sc_demon_hunter.cpp |
| `Thrill of the Fight` | sc_demon_hunter.cpp |
| `Trail of Ruin` | sc_demon_hunter.cpp |
| `Trick Shots` | sc_hunter.cpp |
| `Twilight Requiem` | sc_hunter.cpp |
| `Umbral Blade` | sc_demon_hunter.cpp |
| `Umbral Reach` | sc_hunter.cpp |
| `Unbound Chaos` | sc_demon_hunter.cpp |
| `Unbreakable Bond` | sc_hunter.cpp |
| `Unerring Vision` | sc_hunter.cpp |
| `Unhindered Assault` | sc_demon_hunter.cpp |
| `Unrestrained Fury` | sc_demon_hunter.cpp |
| `Untethered Rage` | sc_demon_hunter.cpp |
| `Ursine Fury` | sc_hunter.cpp |
| `Vengeful Beast` | sc_demon_hunter.cpp |
| `Vengeful Bonds` | sc_demon_hunter.cpp |
| `Vengeful Retreat` | sc_demon_hunter.cpp |
| `Void Metamorphosis` | sc_demon_hunter.cpp |
| `Void Nova` | sc_demon_hunter.cpp |
| `Void Ray` | sc_demon_hunter.cpp |
| `Void Reaver` | sc_demon_hunter.cpp |
| `Voidblade` | sc_demon_hunter.cpp |
| `Voidglare Boon` | sc_demon_hunter.cpp |
| `Voidpurge` | sc_demon_hunter.cpp |
| `Voidrage` | sc_demon_hunter.cpp |
| `Voidrush` | sc_demon_hunter.cpp |
| `Voidsurge` | sc_demon_hunter.cpp |
| `Volatile Flameblood` | sc_demon_hunter.cpp |
| `Vulnerability` | sc_demon_hunter.cpp |
| `Vulnerability` | sc_hunter.cpp |
| `Wailing Dead` | sc_hunter.cpp |
| `Wallop` | sc_hunter.cpp |
| `Warblade's Hunger` | sc_demon_hunter.cpp |
| `Waste Not` | sc_demon_hunter.cpp |
| `Wild Instincts` | sc_hunter.cpp |
| `Will of the Illidari` | sc_demon_hunter.cpp |
| `Wings of Wrath` | sc_demon_hunter.cpp |
| `Withering Fire` | sc_hunter.cpp |
| `World Killer` | sc_demon_hunter.cpp |
| `Wounded Quarry` | sc_demon_hunter.cpp |
| `Wyvern's Gaze` | sc_hunter.cpp |

## Mage (85 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Aegwynn's Technique` | sc_mage.cpp |
| `Archmage's Wrath` | sc_mage.cpp |
| `Ashes of Inspiration` | sc_mage.cpp |
| `Attuned Familiar` | sc_mage.cpp |
| `Augury Abounds` | sc_mage.cpp |
| `Blast Radius` | sc_mage.cpp |
| `Burden of Power` | sc_mage.cpp |
| `Burn It All` | sc_mage.cpp |
| `Codex of the Sunstriders` | sc_mage.cpp |
| `Cold Snap` | sc_mage.cpp |
| `Controlled Instincts` | sc_mage.cpp |
| `Dragon's Breath` | sc_mage.cpp |
| `Dualcasting Adept` | sc_mage.cpp |
| `Duality` | sc_mage.cpp |
| `Elemental Affinity` | sc_mage.cpp |
| `Elemental Conduit` | sc_mage.cpp |
| `Evocation` | sc_mage.cpp |
| `Fire's Ire` | sc_mage.cpp |
| `Force of Will` | sc_mage.cpp |
| `Freezing Cold` | sc_mage.cpp |
| `Frigid Focus` | sc_mage.cpp |
| `Frostfire Empowerment` | sc_mage.cpp |
| `Frostfire Infusion` | sc_mage.cpp |
| `Glorious Incandescence` | sc_mage.cpp |
| `Heat Sink` | sc_mage.cpp |
| `High Voltage` | sc_mage.cpp |
| `Ice Nova` | sc_mage.cpp |
| `Ice Ward` | sc_mage.cpp |
| `Imbued Warding` | sc_mage.cpp |
| `Improved Blink` | sc_mage.cpp |
| `Infused Splinters` | sc_mage.cpp |
| `Invocation: Arcane Phoenix` | sc_mage.cpp |
| `Isothermic Core` | sc_mage.cpp |
| `Lessons in Debilitation` | sc_mage.cpp |
| `Lonely Winter` | sc_mage.cpp |
| `Look Again` | sc_mage.cpp |
| `Mana Adept` | sc_mage.cpp |
| `Mana Cascade` | sc_mage.cpp |
| `Mass Polymorph` | sc_mage.cpp |
| `Meltdown` | sc_mage.cpp |
| `Memory of Al'ar` | sc_mage.cpp |
| `Merely a Setback` | sc_mage.cpp |
| `Molten Chill` | sc_mage.cpp |
| `Polished Focus` | sc_mage.cpp |
| `Presence of Mind` | sc_mage.cpp |
| `Pyrocosm` | sc_mage.cpp |
| `Reactive Barrier` | sc_mage.cpp |
| `Reflection` | sc_mage.cpp |
| `Ring of Frost` | sc_mage.cpp |
| `Rondurmancy` | sc_mage.cpp |
| `Savor the Moment` | sc_mage.cpp |
| `Severe Temperatures` | sc_mage.cpp |
| `Shifting Shards` | sc_mage.cpp |
| `Shimmer` | sc_mage.cpp |
| `Signature Spell` | sc_mage.cpp |
| `Slippery Slinging` | sc_mage.cpp |
| `Slipstream` | sc_mage.cpp |
| `Slow Burn` | sc_mage.cpp |
| `Spatial Manipulation` | sc_mage.cpp |
| `Spellfire Salvo` | sc_mage.cpp |
| `Spellfire Spheres` | sc_mage.cpp |
| `Spellfrost Teachings` | sc_mage.cpp |
| `Splintering Orbs` | sc_mage.cpp |
| `Splintering Ray` | sc_mage.cpp |
| `Splintering Sorcery` | sc_mage.cpp |
| `Splinterstorm` | sc_mage.cpp |
| `Summon Water Elemental` | sc_mage.cpp |
| `Sunfury Execution` | sc_mage.cpp |
| `Supernova` | sc_mage.cpp |
| `Temporal Realignment` | sc_mage.cpp |
| `Thermal Conditioning` | sc_mage.cpp |
| `Time Twist` | sc_mage.cpp |
| `Time Walk` | sc_mage.cpp |
| `White Out` | sc_mage.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1248829 | sc_mage.cpp |
| 1254851 | sc_mage.cpp |
| 1257348 | sc_mage.cpp |
| 1257349 | sc_mage.cpp |
| 1257947 | sc_mage.cpp |
| 1257950 | sc_mage.cpp |
| 1262981 | sc_mage.cpp |
| 1263249 | sc_mage.cpp |
| 190356 | sc_mage.cpp |
| 2120 | sc_mage.cpp |
| 431044 | sc_mage.cpp |

## Monk (93 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Against All Odds` | monk/sc_monk.cpp |
| `Airborne Rhythm` | monk/sc_monk.cpp |
| `Aspect of Harmony` | monk/sc_monk.cpp |
| `Awakening Spirit` | monk/sc_monk.cpp |
| `Balanced Stratagem` | monk/sc_monk.cpp |
| `Black Ox Brew` | monk/sc_monk.cpp |
| `Blackout Combo` | monk/sc_monk.cpp |
| `Bob and Weave` | monk/sc_monk.cpp |
| `Celerity` | monk/sc_monk.cpp |
| `Celestial Brew` | monk/sc_monk.cpp |
| `Celestial Conduit` | monk/sc_monk.cpp |
| `Celestial Infusion` | monk/sc_monk.cpp |
| `Charred Passions` | monk/sc_monk.cpp |
| `Chi Burst` | monk/sc_monk.cpp |
| `Chi Torpedo` | monk/sc_monk.cpp |
| `Chi Wave` | monk/sc_monk.cpp |
| `Chi-Ji's Swiftness` | monk/sc_monk.cpp |
| `Clarity of Purpose` | monk/sc_monk.cpp |
| `Coalescence` | monk/sc_monk.cpp |
| `Combat Stance` | monk/sc_monk.cpp |
| `Courage of the White Tiger` | monk/sc_monk.cpp |
| `Crashing Fists` | monk/sc_monk.cpp |
| `Crashing Momentum` | monk/sc_monk.cpp |
| `Cyclone's Drift` | monk/sc_monk.cpp |
| `Disable` | monk/sc_monk.cpp |
| `Dragonfire Brew` | monk/sc_monk.cpp |
| `Drinking Horn Cover` | monk/sc_monk.cpp |
| `Echo Technique` | monk/sc_monk.cpp |
| `Efficient Training` | monk/sc_monk.cpp |
| `Endless Draught` | monk/sc_monk.cpp |
| `Escape from Reality` | monk/sc_monk.cpp |
| `Expeditious Fortification` | monk/sc_monk.cpp |
| `Flowing Wisdom` | monk/sc_monk.cpp |
| `Fluidity of Motion` | monk/sc_monk.cpp |
| `Harmonic Gambit` | monk/sc_monk.cpp |
| `Harmonic Surge` | monk/sc_monk.cpp |
| `Hasty Provocation` | monk/sc_monk.cpp |
| `High Impact` | monk/sc_monk.cpp |
| `Hurricane's Vault` | monk/sc_monk.cpp |
| `Initiator's Edge` | monk/sc_monk.cpp |
| `Inner Compass` | monk/sc_monk.cpp |
| `Invoke Xuen, the White Tiger` | monk/sc_monk.cpp |
| `Ironshell Brew` | monk/sc_monk.cpp |
| `Jade Sanctuary` | monk/sc_monk.cpp |
| `Keg Volley` | monk/sc_monk.cpp |
| `Manifestation` | monk/sc_monk.cpp |
| `Mantra of Purity` | monk/sc_monk.cpp |
| `Mantra of Tenacity` | monk/sc_monk.cpp |
| `Martial Precision` | monk/sc_monk.cpp |
| `Meditative Focus` | monk/sc_monk.cpp |
| `One Versus Many` | monk/sc_monk.cpp |
| `Overwhelming Force` | monk/sc_monk.cpp |
| `Path of Jade` | monk/sc_monk.cpp |
| `Path of Resurgence` | monk/sc_monk.cpp |
| `Path of the Falling Star` | monk/sc_monk.cpp |
| `Potential Energy` | monk/sc_monk.cpp |
| `Predictive Training` | monk/sc_monk.cpp |
| `Press the Advantage` | monk/sc_monk.cpp |
| `Pride of Pandaria` | monk/sc_monk.cpp |
| `Profound Rebuttal` | monk/sc_monk.cpp |
| `Purified Spirit` | monk/sc_monk.cpp |
| `Quick Footed` | monk/sc_monk.cpp |
| `Quick Sip` | monk/sc_monk.cpp |
| `Restore Balance` | monk/sc_monk.cpp |
| `Revolving Whirl` | monk/sc_monk.cpp |
| `Ring of Peace` | monk/sc_monk.cpp |
| `Roar from the Heavens` | monk/sc_monk.cpp |
| `Rushing Jade Wind` | monk/sc_monk.cpp |
| `Sal'salabim's Strength` | monk/sc_monk.cpp |
| `Shado Over the Battlefield` | monk/sc_monk.cpp |
| `Singularly Focused Jade` | monk/sc_monk.cpp |
| `Song of Chi-Ji` | monk/sc_monk.cpp |
| `Special Delivery` | monk/sc_monk.cpp |
| `Stand Ready` | monk/sc_monk.cpp |
| `Strength of the Black Ox` | monk/sc_monk.cpp |
| `Strike of the Windlord` | monk/sc_monk.cpp |
| `Temple Training` | monk/sc_monk.cpp |
| `Training of Niuzao` | monk/sc_monk.cpp |
| `Unity Within` | monk/sc_monk.cpp |
| `Veteran's Eye` | monk/sc_monk.cpp |
| `Vigilant Watch` | monk/sc_monk.cpp |
| `Vital Flame` | monk/sc_monk.cpp |
| `Way of a Thousand Strikes` | monk/sc_monk.cpp |
| `Weapons of the Wall` | monk/sc_monk.cpp |
| `Whirling Dragon Punch` | monk/sc_monk.cpp |
| `Whirling Steel` | monk/sc_monk.cpp |
| `Wind's Reach` | monk/sc_monk.cpp |
| `Wisdom of the Wall` | monk/sc_monk.cpp |
| `Xuen's Battlegear` | monk/sc_monk.cpp |
| `Xuen's Bond` | monk/sc_monk.cpp |
| `Xuen's Guidance` | monk/sc_monk.cpp |
| `Yu'lon's Avatar` | monk/sc_monk.cpp |
| `Yu'lon's Grace` | monk/sc_monk.cpp |

## Paladin (90 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Adjudication` | paladin/sc_paladin_protection.cpp |
| `Art of War` | paladin/sc_paladin_retribution.cpp |
| `Aurora` | paladin/sc_paladin.cpp |
| `Authoritative Rebuke` | paladin/sc_paladin.cpp |
| `Awakening` | paladin/sc_paladin_holy.cpp |
| `Beacon of Faith` | paladin/sc_paladin_holy.cpp |
| `Beacon of Virtue` | paladin/sc_paladin_holy.cpp |
| `Bestow Faith` | paladin/sc_paladin_holy.cpp |
| `Blessed Assurance` | paladin/sc_paladin.cpp |
| `Blessed Hammer` | paladin/sc_paladin_protection.cpp |
| `Blessing of An'she` | paladin/sc_paladin.cpp |
| `Blessing of Freedom` | paladin/sc_paladin.cpp |
| `Blessing of Spellwarding` | paladin/sc_paladin_protection.cpp |
| `Blessing of the Forge` | paladin/sc_paladin.cpp |
| `Bonds of Fellowship` | paladin/sc_paladin.cpp |
| `Born in Sunlight` | paladin/sc_paladin.cpp |
| `Boundless Judgment` | paladin/sc_paladin_retribution.cpp |
| `Dawnlight` | paladin/sc_paladin.cpp |
| `Divine Exaction` | paladin/sc_paladin.cpp |
| `Divine Guidance` | paladin/sc_paladin.cpp |
| `Divine Hammer` | paladin/sc_paladin.cpp |
| `Divine Inspiration` | paladin/sc_paladin.cpp |
| `Divine Purpose` | paladin/sc_paladin.cpp |
| `Endless Gleam` | paladin/sc_paladin.cpp |
| `Endless Wrath` | paladin/sc_paladin.cpp |
| `Forewarning` | paladin/sc_paladin.cpp |
| `Gleaming Rays` | paladin/sc_paladin.cpp |
| `Glimmer of Light` | paladin/sc_paladin_holy.cpp |
| `Golden Path` | paladin/sc_paladin.cpp |
| `Hammer and Anvil` | paladin/sc_paladin.cpp |
| `Hammer of the Righteous` | paladin/sc_paladin_protection.cpp |
| `Hammerfall` | paladin/sc_paladin.cpp |
| `Healing Hands` | paladin/sc_paladin.cpp |
| `Healing Hands` | paladin/sc_paladin_retribution.cpp |
| `Higher Calling` | paladin/sc_paladin.cpp |
| `Holy Armaments` | paladin/sc_paladin.cpp |
| `Holy Blade` | paladin/sc_paladin_retribution.cpp |
| `Holy Prism` | paladin/sc_paladin_holy.cpp |
| `Imbued Shield` | paladin/sc_paladin_protection.cpp |
| `Improved Ardent Defender` | paladin/sc_paladin_protection.cpp |
| `Improved Blade of Justice` | paladin/sc_paladin_retribution.cpp |
| `Improved Judgment` | paladin/sc_paladin_retribution.cpp |
| `Laying Down Arms` | paladin/sc_paladin.cpp |
| `Lingering Radiance` | paladin/sc_paladin.cpp |
| `Luminosity` | paladin/sc_paladin.cpp |
| `Masterwork` | paladin/sc_paladin.cpp |
| `Morning Star` | paladin/sc_paladin.cpp |
| `Quickened Invocation` | paladin/sc_paladin.cpp |
| `Recompense` | paladin/sc_paladin.cpp |
| `Redoubt` | paladin/sc_paladin_protection.cpp |
| `Reflection of Radiance` | paladin/sc_paladin.cpp |
| `Resounding Strike` | paladin/sc_paladin.cpp |
| `Righteous Cause` | paladin/sc_paladin_retribution.cpp |
| `Rite of Adjuration` | paladin/sc_paladin.cpp |
| `Rite of Sanctification` | paladin/sc_paladin.cpp |
| `Rule of Law` | paladin/sc_paladin_holy.cpp |
| `Sacred Strength` | paladin/sc_paladin.cpp |
| `Sacrifice of the Just` | paladin/sc_paladin.cpp |
| `Sacrosanct Crusade` | paladin/sc_paladin.cpp |
| `Saved by the Light` | paladin/sc_paladin_holy.cpp |
| `Seal of the Templar` | paladin/sc_paladin.cpp |
| `Second Sunrise` | paladin/sc_paladin.cpp |
| `Selfless Healer` | paladin/sc_paladin.cpp |
| `Sentinel` | paladin/sc_paladin_protection.cpp |
| `Shake the Heavens` | paladin/sc_paladin.cpp |
| `Shared Resolve` | paladin/sc_paladin.cpp |
| `Solar Grace` | paladin/sc_paladin.cpp |
| `Solidarity` | paladin/sc_paladin.cpp |
| `Stand Against Evil` | paladin/sc_paladin.cpp |
| `Steed of Liberty` | paladin/sc_paladin.cpp |
| `Strength in Adversity` | paladin/sc_paladin_protection.cpp |
| `Sun Sear` | paladin/sc_paladin.cpp |
| `Sun's Avatar` | paladin/sc_paladin.cpp |
| `Sweeping Verdict` | paladin/sc_paladin_protection.cpp |
| `Tempered in Battle` | paladin/sc_paladin.cpp |
| `Templar Strikes` | paladin/sc_paladin_retribution.cpp |
| `Tirion's Devotion` | paladin/sc_paladin_protection.cpp |
| `Tyr's Enforcer` | paladin/sc_paladin_protection.cpp |
| `Undisputed Ruling` | paladin/sc_paladin.cpp |
| `Unrelenting Charger` | paladin/sc_paladin.cpp |
| `Valiance` | paladin/sc_paladin.cpp |
| `Walk Into Light` | paladin/sc_paladin.cpp |
| `Worthy Sacrifice` | paladin/sc_paladin.cpp |
| `Wrathful Descent` | paladin/sc_paladin.cpp |
| `Wrench Evil` | paladin/sc_paladin.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1261111 | paladin/sc_paladin.cpp |
| 1261111 | paladin/sc_paladin_retribution.cpp |
| 1261159 | paladin/sc_paladin_retribution.cpp |
| 1267211 | paladin/sc_paladin_protection.cpp |
| 1267215 | paladin/sc_paladin_protection.cpp |

## Priest (146 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Abyssal Reverie` | priest/sc_priest_discipline.cpp |
| `Afterlife` | priest/sc_priest_holy.cpp |
| `Ancient Madness` | priest/sc_priest_shadow.cpp |
| `Apotheosis` | priest/sc_priest_holy.cpp |
| `Assured Safety` | priest/sc_priest.cpp |
| `Atonement` | priest/sc_priest_discipline.cpp |
| `Benediction` | priest/sc_priest_holy.cpp |
| `Benevolence` | priest/sc_priest.cpp |
| `Blaze of Light` | priest/sc_priest_discipline.cpp |
| `Borrowed Time` | priest/sc_priest_discipline.cpp |
| `Bright Pupil` | priest/sc_priest_discipline.cpp |
| `Burning Vehemence` | priest/sc_priest_holy.cpp |
| `Castigation` | priest/sc_priest_discipline.cpp |
| `Censure` | priest/sc_priest_holy.cpp |
| `Collapsing Void` | priest/sc_priest.cpp |
| `Cosmic Ripple` | priest/sc_priest_holy.cpp |
| `Cosmic Wave` | priest/sc_priest_holy.cpp |
| `Crisis Management` | priest/sc_priest_holy.cpp |
| `Dark Energy` | priest/sc_priest.cpp |
| `Dark Indulgence` | priest/sc_priest_discipline.cpp |
| `Darkening Horizon` | priest/sc_priest.cpp |
| `Desperate Measures` | priest/sc_priest.cpp |
| `Desperate Times` | priest/sc_priest_holy.cpp |
| `Devour Matter` | priest/sc_priest.cpp |
| `Dispersing Light` | priest/sc_priest_holy.cpp |
| `Distorted Reality` | priest/sc_priest_shadow.cpp |
| `Divine Aegis` | priest/sc_priest_discipline.cpp |
| `Divine Feathers` | priest/sc_priest.cpp |
| `Divine Halo` | priest/sc_priest.cpp |
| `Divine Hymn` | priest/sc_priest_holy.cpp |
| `Divine Image` | priest/sc_priest_holy.cpp |
| `Divine Procession` | priest/sc_priest_discipline.cpp |
| `Divine Service` | priest/sc_priest_holy.cpp |
| `Divinity` | priest/sc_priest_holy.cpp |
| `Dominant Mind` | priest/sc_priest.cpp |
| `Efficient Prayers` | priest/sc_priest_holy.cpp |
| `Embrace the Shadow` | priest/sc_priest.cpp |
| `Empowered Surges` | priest/sc_priest.cpp |
| `Empyreal Blaze` | priest/sc_priest_holy.cpp |
| `Encroaching Shadows` | priest/sc_priest_discipline.cpp |
| `Enduring Luminescence` | priest/sc_priest_discipline.cpp |
| `Energy Compression` | priest/sc_priest.cpp |
| `Energy Conservation` | priest/sc_priest.cpp |
| `Energy Cycle` | priest/sc_priest.cpp |
| `Entropic Rift` | priest/sc_priest.cpp |
| `Epiphany` | priest/sc_priest_holy.cpp |
| `Eternal Barrier` | priest/sc_priest_discipline.cpp |
| `Eternal Sanctity` | priest/sc_priest_holy.cpp |
| `Evangelism` | priest/sc_priest_discipline.cpp |
| `Expiation` | priest/sc_priest_discipline.cpp |
| `Forseen Circumstances` | priest/sc_priest.cpp |
| `Gales of Song` | priest/sc_priest_holy.cpp |
| `Greater Smite` | priest/sc_priest_discipline.cpp |
| `Guardian Angel` | priest/sc_priest_holy.cpp |
| `Guardian Spirit` | priest/sc_priest_holy.cpp |
| `Guiding Light` | priest/sc_priest.cpp |
| `Halo` | priest/sc_priest.cpp |
| `Harsh Discipline` | priest/sc_priest_discipline.cpp |
| `Healing Focus` | priest/sc_priest_holy.cpp |
| `Heightened Alteration` | priest/sc_priest.cpp |
| `Holy Celerity` | priest/sc_priest_holy.cpp |
| `Holy Fire` | priest/sc_priest.cpp |
| `Holy Ray` | priest/sc_priest_discipline.cpp |
| `Holy Word: Chastise` | priest/sc_priest_holy.cpp |
| `Holy Word: Sanctify` | priest/sc_priest_holy.cpp |
| `Holy Word: Serenity` | priest/sc_priest_holy.cpp |
| `Improved Voidform` | priest/sc_priest_shadow.cpp |
| `Incessant Screams` | priest/sc_priest.cpp |
| `Indemnity` | priest/sc_priest_discipline.cpp |
| `Inner Focus` | priest/sc_priest_discipline.cpp |
| `Inner Light` | priest/sc_priest_discipline.cpp |
| `Inner Quietus` | priest/sc_priest.cpp |
| `Intangibility` | priest/sc_priest_shadow.cpp |
| `Invoked Nightmares` | priest/sc_priest_shadow.cpp |
| `Lasting Words` | priest/sc_priest_holy.cpp |
| `Lenience` | priest/sc_priest_discipline.cpp |
| `Manifested Power` | priest/sc_priest.cpp |
| `Master the Darkness` | priest/sc_priest_discipline.cpp |
| `Mental Fortitude` | priest/sc_priest_shadow.cpp |
| `Mind Control` | priest/sc_priest.cpp |
| `Mind Flay: Insanity` | priest/sc_priest.cpp |
| `Mind's Eye` | priest/sc_priest_shadow.cpp |
| `Miracle Worker` | priest/sc_priest_holy.cpp |
| `Misery` | priest/sc_priest_shadow.cpp |
| `No Escape` | priest/sc_priest.cpp |
| `Occultist` | priest/sc_priest_discipline.cpp |
| `Overwhelming Shadows` | priest/sc_priest.cpp |
| `Pain Suppression` | priest/sc_priest_discipline.cpp |
| `Pain Transformation` | priest/sc_priest_discipline.cpp |
| `Pain and Suffering` | priest/sc_priest_discipline.cpp |
| `Painful Punishment` | priest/sc_priest_discipline.cpp |
| `Perfected Form` | priest/sc_priest.cpp |
| `Petrifying Scream` | priest/sc_priest.cpp |
| `Piety` | priest/sc_priest.cpp |
| `Plea` | priest/sc_priest_discipline.cpp |
| `Power Surge` | priest/sc_priest.cpp |
| `Power Word: Barrier` | priest/sc_priest_discipline.cpp |
| `Power Word: Radiance` | priest/sc_priest_discipline.cpp |
| `Power of the Dark Side` | priest/sc_priest_discipline.cpp |
| `Prayer of Healing` | priest/sc_priest_holy.cpp |
| `Prayerful Litany` | priest/sc_priest_holy.cpp |
| `Prayers of the Virtuous` | priest/sc_priest_holy.cpp |
| `Preemptive Care` | priest/sc_priest.cpp |
| `Preventive Measures` | priest/sc_priest.cpp |
| `Prismatic Echoes` | priest/sc_priest_holy.cpp |
| `Prompt Prognosis` | priest/sc_priest.cpp |
| `Prophets Will` | priest/sc_priest.cpp |
| `Protector of the Frail` | priest/sc_priest_discipline.cpp |
| `Psychic Voice` | priest/sc_priest.cpp |
| `Purge the Wicked` | priest/sc_priest_discipline.cpp |
| `Quickened Pulse` | priest/sc_priest.cpp |
| `Radiant Plea` | priest/sc_priest_holy.cpp |
| `Realized Potential` | priest/sc_priest.cpp |
| `Renewed Faith` | priest/sc_priest_holy.cpp |
| `Restitution` | priest/sc_priest_holy.cpp |
| `Revel in Darkness` | priest/sc_priest_discipline.cpp |
| `Save the Day` | priest/sc_priest.cpp |
| `Say Your Prayers` | priest/sc_priest_holy.cpp |
| `Seraphic Crescendo` | priest/sc_priest_holy.cpp |
| `Shadow Mend` | priest/sc_priest_discipline.cpp |
| `Shadow Tap` | priest/sc_priest_discipline.cpp |
| `Sheer Terror` | priest/sc_priest.cpp |
| `Shield Discipline` | priest/sc_priest_discipline.cpp |
| `Shock Pulse` | priest/sc_priest.cpp |
| `Sustained Potency` | priest/sc_priest.cpp |
| `Touch of the Void` | priest/sc_priest.cpp |
| `Trail of Light` | priest/sc_priest_holy.cpp |
| `Twinsight` | priest/sc_priest.cpp |
| `Ultimate Penitence` | priest/sc_priest_discipline.cpp |
| `Ultimate Serenity` | priest/sc_priest_holy.cpp |
| `Uplifting Words` | priest/sc_priest_holy.cpp |
| `Voice of Harmony` | priest/sc_priest_holy.cpp |
| `Void Blast` | priest/sc_priest.cpp |
| `Void Empowerment` | priest/sc_priest.cpp |
| `Void Infusion` | priest/sc_priest.cpp |
| `Void Leech` | priest/sc_priest.cpp |
| `Void Tendrils` | priest/sc_priest.cpp |
| `Void Torrent` | priest/sc_priest.cpp |
| `Void Volley` | priest/sc_priest_shadow.cpp |
| `Voidheart` | priest/sc_priest.cpp |
| `Voidwraith` | priest/sc_priest.cpp |
| `Waste No Time` | priest/sc_priest.cpp |
| `Weal and Woe` | priest/sc_priest_discipline.cpp |
| `Word of Supremacy` | priest/sc_priest.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1264104 | priest/sc_priest_shadow.cpp |
| 1264107 | priest/sc_priest_shadow.cpp |

## Rogue (91 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Airborne Irritant` | sc_rogue.cpp |
| `Atrophic Poison` | sc_rogue.cpp |
| `Bait and Switch` | sc_rogue.cpp |
| `Blackjack` | sc_rogue.cpp |
| `Canny Strikes` | sc_rogue.cpp |
| `Cheat Death` | sc_rogue.cpp |
| `Chosen's Revelry` | sc_rogue.cpp |
| `Clear the Witnesses` | sc_rogue.cpp |
| `Clever Combatant` | sc_rogue.cpp |
| `Cloaked in Shadow` | sc_rogue.cpp |
| `Cloud Cover` | sc_rogue.cpp |
| `Combat Stamina` | sc_rogue.cpp |
| `Controlled Chaos` | sc_rogue.cpp |
| `Corrupt the Blood` | sc_rogue.cpp |
| `Coup de Grace` | sc_rogue.cpp |
| `Darkest Night` | sc_rogue.cpp |
| `Deal Fate` | sc_rogue.cpp |
| `Delivered Doom` | sc_rogue.cpp |
| `Destiny Defined` | sc_rogue.cpp |
| `Devious Distractions` | sc_rogue.cpp |
| `Disorienting Strikes` | sc_rogue.cpp |
| `Don't Be Suspicious` | sc_rogue.cpp |
| `Echoing Reprimand` | sc_rogue.cpp |
| `Edge Case` | sc_rogue.cpp |
| `Elusiveness` | sc_rogue.cpp |
| `Ephemeral Bonds` | sc_rogue.cpp |
| `Ethereal Cloak` | sc_rogue.cpp |
| `Exhilarating Execution` | sc_rogue.cpp |
| `Fade to Nothing` | sc_rogue.cpp |
| `Fate Intertwined` | sc_rogue.cpp |
| `Flashing Steel` | sc_rogue.cpp |
| `Flawless Form` | sc_rogue.cpp |
| `Flickering Steel` | sc_rogue.cpp |
| `Flickerstrike` | sc_rogue.cpp |
| `Flying Daggers` | sc_rogue.cpp |
| `Follow the Blood` | sc_rogue.cpp |
| `Forced Induction` | sc_rogue.cpp |
| `Gouge` | sc_rogue.cpp |
| `Heightened Rush` | sc_rogue.cpp |
| `Hit and Run` | sc_rogue.cpp |
| `Hoodwink` | sc_rogue.cpp |
| `Hunt Them Down` | sc_rogue.cpp |
| `Improved Ambush` | sc_rogue.cpp |
| `Inexorable March` | sc_rogue.cpp |
| `Inspiring Strike` | sc_rogue.cpp |
| `Intent to Kill` | sc_rogue.cpp |
| `Internal Bleeding` | sc_rogue.cpp |
| `Iron Wire` | sc_rogue.cpp |
| `Lingering Darkness` | sc_rogue.cpp |
| `Lucky Coin` | sc_rogue.cpp |
| `Mass Casualty` | sc_rogue.cpp |
| `Mean Streak` | sc_rogue.cpp |
| `Menacing Rush` | sc_rogue.cpp |
| `Mirrors` | sc_rogue.cpp |
| `Momentum of Despair` | sc_rogue.cpp |
| `Night Terrors` | sc_rogue.cpp |
| `Nimble Flurry` | sc_rogue.cpp |
| `Numbing Poison` | sc_rogue.cpp |
| `Overflowing Purse` | sc_rogue.cpp |
| `Planned Execution` | sc_rogue.cpp |
| `Poisoner's Drive` | sc_rogue.cpp |
| `Precise Killer` | sc_rogue.cpp |
| `Quietus Celeris` | sc_rogue.cpp |
| `Ravenholdt Mint` | sc_rogue.cpp |
| `Retractable Hook` | sc_rogue.cpp |
| `Rush to the Inevitable` | sc_rogue.cpp |
| `Secondary Poisoning` | sc_rogue.cpp |
| `Shadewalker` | sc_rogue.cpp |
| `Shot in the Dark` | sc_rogue.cpp |
| `Shroud of Night` | sc_rogue.cpp |
| `Singular Focus` | sc_rogue.cpp |
| `Smoke` | sc_rogue.cpp |
| `So Tricky` | sc_rogue.cpp |
| `Sometimes Lucky` | sc_rogue.cpp |
| `Surprising Strikes` | sc_rogue.cpp |
| `Symbolic Victory` | sc_rogue.cpp |
| `Tempted Fate` | sc_rogue.cpp |
| `Terrifying Pace` | sc_rogue.cpp |
| `Thief's Versatility` | sc_rogue.cpp |
| `Thousand Cuts` | sc_rogue.cpp |
| `Tight Spender` | sc_rogue.cpp |
| `Tricks of the Trade` | sc_rogue.cpp |
| `Unseen Blade` | sc_rogue.cpp |
| `Unshakeable Drive` | sc_rogue.cpp |
| `Warning Signs` | sc_rogue.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1265386 | sc_rogue.cpp |
| 1265387 | sc_rogue.cpp |
| 1265862 | sc_rogue.cpp |
| 1265863 | sc_rogue.cpp |
| 1268936 | sc_rogue.cpp |
| 1268939 | sc_rogue.cpp |

## Shaman (61 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Aftershock` | sc_shaman.cpp |
| `Ancestral Guidance` | sc_shaman.cpp |
| `Ancestral Influence` | sc_shaman.cpp |
| `Ancestral Swiftness` | sc_shaman.cpp |
| `Ancient Fellowship` | sc_shaman.cpp |
| `Arc Discharge` | sc_shaman.cpp |
| `Awakening Storms` | sc_shaman.cpp |
| `Call of the Ancestors` | sc_shaman.cpp |
| `Call of the Elements` | sc_shaman.cpp |
| `Conductive Energy` | sc_shaman.cpp |
| `Creation Core` | sc_shaman.cpp |
| `Deeply Rooted Elements` | sc_shaman.cpp |
| `Descending Skies` | sc_shaman.cpp |
| `Earth Shock` | sc_shaman.cpp |
| `Earthsurge` | sc_shaman.cpp |
| `Electroshock` | sc_shaman.cpp |
| `Elemental Attunement` | sc_shaman.cpp |
| `Elemental Blast` | sc_shaman.cpp |
| `Elemental Resonance` | sc_shaman.cpp |
| `Elemental Reverb` | sc_shaman.cpp |
| `First Ascendant` | sc_shaman.cpp |
| `Fury of the Storms` | sc_shaman.cpp |
| `Graceful Spirit` | sc_shaman.cpp |
| `Gust of Wind` | sc_shaman.cpp |
| `Heed My Call` | sc_shaman.cpp |
| `Herald of the Storms` | sc_shaman.cpp |
| `Imbuement Mastery` | sc_shaman.cpp |
| `Improved Lightning Bolt` | sc_shaman.cpp |
| `Latent Wisdom` | sc_shaman.cpp |
| `Lively Totems` | sc_shaman.cpp |
| `Maelstrom Supremacy` | sc_shaman.cpp |
| `Molten Wrath` | sc_shaman.cpp |
| `Mystic Knowledge` | sc_shaman.cpp |
| `Offering from Beyond` | sc_shaman.cpp |
| `Oversurge` | sc_shaman.cpp |
| `Preeminence` | sc_shaman.cpp |
| `Primal Catalyst` | sc_shaman.cpp |
| `Primordial Capacity` | sc_shaman.cpp |
| `Pulse Capacitor` | sc_shaman.cpp |
| `Rolling Thunder` | sc_shaman.cpp |
| `Routine Communication` | sc_shaman.cpp |
| `Splitstream` | sc_shaman.cpp |
| `Supportive Imbuements` | sc_shaman.cpp |
| `Surging Totem` | sc_shaman.cpp |
| `Tectonic Collapse` | sc_shaman.cpp |
| `Thunderous Paws` | sc_shaman.cpp |
| `Thundershock` | sc_shaman.cpp |
| `Thunderstorm` | sc_shaman.cpp |
| `Thunderstrike Ward` | sc_shaman.cpp |
| `Totemic Coordination` | sc_shaman.cpp |
| `Totemic Momentum` | sc_shaman.cpp |
| `Totemic Rebound` | sc_shaman.cpp |
| `Totemic Recall` | sc_shaman.cpp |
| `Unlimited Power` | sc_shaman.cpp |
| `Voltaic Surge` | sc_shaman.cpp |
| `Whirling Elements` | sc_shaman.cpp |
| `Windspeaker` | sc_shaman.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1252373 | sc_shaman.cpp |
| 1262761 | sc_shaman.cpp |
| 462620 | sc_shaman.cpp |
| 61882 | sc_shaman.cpp |

## Warlock (57 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Absolute Corruption` | warlock/sc_warlock_init.cpp |
| `Abyssal Dominion` | warlock/sc_warlock_init.cpp |
| `Alzzin's Iniquity` | warlock/sc_warlock_init.cpp |
| `Blackened Soul` | warlock/sc_warlock_init.cpp |
| `Bleakheart Tactics` | warlock/sc_warlock_init.cpp |
| `Channel Demonfire` | warlock/sc_warlock_init.cpp |
| `Cloven Souls` | warlock/sc_warlock_init.cpp |
| `Crashing Chaos` | warlock/sc_warlock_init.cpp |
| `Devil Fruit` | warlock/sc_warlock_init.cpp |
| `Diabolic Oculi` | warlock/sc_warlock_init.cpp |
| `Diabolic Ritual` | warlock/sc_warlock_init.cpp |
| `Dimensional Rift` | warlock/sc_warlock_init.cpp |
| `Drain Soul` | warlock/sc_warlock_init.cpp |
| `Eternal Hunger` | warlock/sc_warlock_init.cpp |
| `Feast of Souls` | warlock/sc_warlock_init.cpp |
| `Gloom of Nathreza` | warlock/sc_warlock_init.cpp |
| `Grimoire of Sacrifice` | warlock/sc_warlock_init.cpp |
| `Grimoire: Fel Ravager` | warlock/sc_warlock_init.cpp |
| `Grimoire: Imp Lord` | warlock/sc_warlock_init.cpp |
| `Hatefury Rituals` | warlock/sc_warlock_init.cpp |
| `Havoc` | warlock/sc_warlock_init.cpp |
| `Illhoof's Design` | warlock/sc_warlock_init.cpp |
| `Implosion` | warlock/sc_warlock_init.cpp |
| `Improved Shadow Bolt` | warlock/sc_warlock_init.cpp |
| `Internal Combustion` | warlock/sc_warlock_init.cpp |
| `Looks That Kill` | warlock/sc_warlock_init.cpp |
| `Malevolence` | warlock/sc_warlock_init.cpp |
| `Manifested Avarice` | warlock/sc_warlock_init.cpp |
| `Mark of F'harg` | warlock/sc_warlock_init.cpp |
| `Mark of Peroth'arn` | warlock/sc_warlock_init.cpp |
| `Mark of Shatug` | warlock/sc_warlock_init.cpp |
| `Mark of Xavius` | warlock/sc_warlock_init.cpp |
| `Mayhem` | warlock/sc_warlock_init.cpp |
| `Mind's Eyes` | warlock/sc_warlock_init.cpp |
| `Necrolyte Teachings` | warlock/sc_warlock_init.cpp |
| `Power Siphon` | warlock/sc_warlock_init.cpp |
| `Quietus` | warlock/sc_warlock_init.cpp |
| `Rain of Chaos` | warlock/sc_warlock_init.cpp |
| `Reverse Entropy` | warlock/sc_warlock_init.cpp |
| `Ruination` | warlock/sc_warlock_init.cpp |
| `Sataiel's Volition` | warlock/sc_warlock_init.cpp |
| `Secrets of the Coven` | warlock/sc_warlock_init.cpp |
| `Seeds of Their Demise` | warlock/sc_warlock_init.cpp |
| `Shadow of Death` | warlock/sc_warlock_init.cpp |
| `Shared Fate` | warlock/sc_warlock_init.cpp |
| `Shared Vessel` | warlock/sc_warlock_init.cpp |
| `Siphon Life` | warlock/sc_warlock_init.cpp |
| `Soul Anathema` | warlock/sc_warlock_init.cpp |
| `Soul Fire` | warlock/sc_warlock_init.cpp |
| `Summoner's Embrace` | warlock/sc_warlock_init.cpp |
| `Through the Felvine` | warlock/sc_warlock_init.cpp |
| `Touch of Rancora` | warlock/sc_warlock_init.cpp |
| `Wicked Reaping` | warlock/sc_warlock_init.cpp |
| `Xalan's Cruelty` | warlock/sc_warlock_init.cpp |
| `Xalan's Ferocity` | warlock/sc_warlock_init.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1214467 | warlock/sc_warlock_init.cpp |
| 5740 | warlock/sc_warlock_init.cpp |

## Warrior (74 entries)

**By Name:**

| Talent Name | File |
|-------------|------|
| `Arterial Bleed` | sc_warrior.cpp |
| `Berserker Shout` | sc_warrior.cpp |
| `Bladestorm` | sc_warrior.cpp |
| `Boneshaker` | sc_warrior.cpp |
| `Broad Strokes` | sc_warrior.cpp |
| `Brutal Finish` | sc_warrior.cpp |
| `Brute Force` | sc_warrior.cpp |
| `Burst of Power` | sc_warrior.cpp |
| `Capacitance` | sc_warrior.cpp |
| `Celeritous Conclusion` | sc_warrior.cpp |
| `Colossal Might` | sc_warrior.cpp |
| `Conductivity` | sc_warrior.cpp |
| `Crashing Thunder` | sc_warrior.cpp |
| `Crushing Combo` | sc_warrior.cpp |
| `Culling Cyclone` | sc_warrior.cpp |
| `Cut to the Bone` | sc_warrior.cpp |
| `Deadly Focus` | sc_warrior.cpp |
| `Decimator` | sc_warrior.cpp |
| `Defender's Aegis` | sc_warrior.cpp |
| `Demolish` | sc_warrior.cpp |
| `Dominance of the Colossus` | sc_warrior.cpp |
| `Earthquaker` | sc_warrior.cpp |
| `Efficiency` | sc_warrior.cpp |
| `Fearless` | sc_warrior.cpp |
| `Fierce Followthrough` | sc_warrior.cpp |
| `Flashing Skies` | sc_warrior.cpp |
| `Gathering Clouds` | sc_warrior.cpp |
| `Ground Current` | sc_warrior.cpp |
| `Heavy Repercussions` | sc_warrior.cpp |
| `Hunker Down` | sc_warrior.cpp |
| `Imminent Demise` | sc_warrior.cpp |
| `Impenetrable Wall` | sc_warrior.cpp |
| `Improved Sweeping Strikes` | sc_warrior.cpp |
| `Interpose` | sc_warrior.cpp |
| `Into the Fray` | sc_warrior.cpp |
| `Just Warming Up` | sc_warrior.cpp |
| `Keep Your Feet on the Ground` | sc_warrior.cpp |
| `Martial Expert` | sc_warrior.cpp |
| `Mountain of Muscle and Scars` | sc_warrior.cpp |
| `No Stranger to Pain` | sc_warrior.cpp |
| `Odyn's Fury` | sc_warrior.cpp |
| `One Against Many` | sc_warrior.cpp |
| `Overwhelming Blades` | sc_warrior.cpp |
| `Piercing Howl` | sc_warrior.cpp |
| `Powerful Enrage` | sc_warrior.cpp |
| `Powerful Momentum` | sc_warrior.cpp |
| `Practiced Strikes` | sc_warrior.cpp |
| `Precise Might` | sc_warrior.cpp |
| `Ravager` | sc_warrior.cpp |
| `Reap the Storm` | sc_warrior.cpp |
| `Relentless Pursuit` | sc_warrior.cpp |
| `Shattering Throw` | sc_warrior.cpp |
| `Show No Mercy` | sc_warrior.cpp |
| `Slayer's Dominance` | sc_warrior.cpp |
| `Slayer's Malice` | sc_warrior.cpp |
| `Snap Induction` | sc_warrior.cpp |
| `Spell Breaker` | sc_warrior.cpp |
| `Steadfast as the Peaks` | sc_warrior.cpp |
| `Strength of the Mountain` | sc_warrior.cpp |
| `Thunder Blast` | sc_warrior.cpp |
| `Tide of Battle` | sc_warrior.cpp |
| `Unhinged` | sc_warrior.cpp |
| `Unrelenting Onslaught` | sc_warrior.cpp |
| `Veteran Vitality` | sc_warrior.cpp |
| `Vicious Agility` | sc_warrior.cpp |
| `Violent Euphoria` | sc_warrior.cpp |
| `Whirling Blade` | sc_warrior.cpp |
| `Wrecking Throw` | sc_warrior.cpp |

**By ID (ID-only registration, no name in Wowhead):**

| Spell ID | File |
|----------|------|
| 1269306 | sc_warrior.cpp |
| 1269307 | sc_warrior.cpp |
| 1269309 | sc_warrior.cpp |
| 1269310 | sc_warrior.cpp |
| 1269312 | sc_warrior.cpp |
| 1269313 | sc_warrior.cpp |

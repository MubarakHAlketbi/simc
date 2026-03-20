# Evoker Augmentation — Midnight (12.0.1) Information Base
Generated: 2026-03-17
Updated: 2026-03-20 — Added Apex talent documentation

## Midnight Apex Talent: Duplicate
- Rank 1 (ID 1259173): Breath of Eons summons a future-self duplicate for 20s that casts Eruption, Fire Breath, Upheaval.
- Rank 2+3 (ID 1259174): Extending Ebon Might also extends the duplicate by 50% of the amount.
- Rank 4 (ID 1259175): While duplicate active, Ebon Might grants +75% stats; Upheaval/Eruption +25% damage.
- SimC implementation: sc_evoker.cpp talent.duplicate1/2/3 + buff.duplicate
- Source: https://www.wowhead.com/spell=1259173
Sources:
- https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps
- https://www.wowhead.com/guide/classes/evoker/augmentation/basics
- https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps
- https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps
- https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps
- https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps
- https://www.wowhead.com/talent-calc/evoker/augmentation/chronowarden
- https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander

## Overview
Guide Contents

Patch 12.0.1

4.4/5

(13 Votes)

**~~~~**
**Midnight**

- [Cheat Sheet](https://www.wowhead.com/guide/classes/evoker/augmentation/cheat-sheet)

- [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

- [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps)

- [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

- [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps)


**~~~~**
**Spec Basics**

- [Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps)

  - [Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#overview)
  - [Strengths and Weaknesses](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#strengths-and-weaknesses)
  - [Cheat Sheet](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#cheat-sheet)
  - [Patch Changes](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#patch-changes)

    - [Removed Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#removed-abilities)
    - [New Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#new-abilities)
    - [Big Changes](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#big-changes)

  - [Hero Talents](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#hero-talents)
  - [Playstyle](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#playstyle)
  - [Gearing](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#gearing)
  - [Professions](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#professions)
  - [Races](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#races)

- [Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

- [Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps)

- [Stat Priority](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps)

- [UI & Macros](https://www.wowhead.com/guide/classes/evoker/augmentation/addons-macro-ui-imports)

- [Leveling](https://www.wowhead.com/guide/classes/evoker/augmentation/dps-leveling-tips)


**~~~~**
**Guide Info**

- [Changelog](https://www.wowhead.com/guide/changelog?id=20707)


# Augmentation Evoker DPS Guide - Midnight

[By Jereico](https://www.wowhead.com/author/Jereico)
Updated:
2026/03/15

LiveJereico[Live on Twitch!](https://www.twitch.tv/jereico) Offline on TwitchFollow: Follow [Discord](https://discord.gg/vXB3GJsbFw) [Twitch](https://www.twitch.tv/jereico) [Twitter](https://twitter.com/coffeeandsteve) [YouTube](https://www.youtube.com/@Jereico)

Welcome to Wowhead's **Midnight Season 1** Augmentation Evoker guide. This guide will help you master your Augmentation Evoker in most forms of PvE content in the game, including raids and dungeons.

[Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps) [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear) [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps) [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps) [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps) [Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps) [![](https://wow.zamimg.com/images/wow/icons/large/inv_misc_groupneedmore.jpg)\\
Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

Show Table of Contents

## ~~~~Augmentation Evoker Overview

Augmentation Evoker is a **unique, support-oriented ranged DPS** specialization with two distinct goals in combat: dealing damage to enemies using the stalwart Earth magic of the Black Dragonflight and empowering allies through various Black- and Bronze-themed support abilities.

_You three shall be the examples all dracthyr will follow._

_Sarkareth, my devastator. You shall rend your foes with the powers of the Red and Blue Dragonflights._

_Viridia, my preserver. You shall heal our allies with the grace of the Green and Bronze Dragonflights._

_And Emberthal, you will wield the essence of the Black Dragonflight to augment all those around you with my power._

Augmentation Evokers have a variety of powerful tools at their disposal: from spells that launch enemies into the air, to inflicting temporal wounds on enemies, all while amplifying the power of nearby allies in the process. This specialization has a fairly simple rotation and straightforward learning curve, making it a great choice for newer players and veterans alike.

## Augmentation Evoker Strengths and Weaknesses

|     |     |     |
| --- | --- | --- |
| **Strengths** |  | **Weaknesses** |
| - Highly accessible spec, with both gameplay and rotation being easy to pick up.<br>  <br>- Potent group damage potential by buffing your own damage and that of nearby allies.<br>  <br>- Excellent survivability with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_defyfate.gif)Defy Fate](https://www.wowhead.com/spell=404195/defy-fate), as well as a variety of additional defensive options, along with bonus armor to mitigate Physical damage.<br>  <br>- Exceptional mobility through high uptime on [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover), along with the ability to control your character when falling with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_glide.gif)Glide](https://www.wowhead.com/spell=358733/glide).<br>  <br>- Has access to some of the best class utility in the game with spells like [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_flywithme.gif)Rescue](https://www.wowhead.com/spell=370665/rescue), [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timespiral.gif)Time Spiral](https://www.wowhead.com/spell=374968/time-spiral), [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_stretchtime.gif)Spatial Paradox](https://www.wowhead.com/spell=406732/spatial-paradox), and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_fontofmagic_red.gif)Cauterizing Flame](https://www.wowhead.com/spell=374251/cauterizing-flame). |  | - 25-yard maximum range as a ranged caster remains a downside.<br>  <br>- Direct damage can be respectable but is highly limited; damage output truly relies on the effectiveness of allies in group content.<br>  <br>- Generally speaking, effectiveness is lowered should one of your buff targets die in combat, especially in dungeons.<br>  <br>- Limited AoE scaling, and cannot deal meaningful priority burst or spread cleave damage aside from buffing allies. |

## ~~~~ Augmentation Evoker Cheat Sheet

![](https://wow.zamimg.com/images/logos/wh-logo-thumbnail.png)WowheadAugmentation Evoker Raid BuildRaidMythic+DelvesRaidMythic+Delves

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Evoker

Spent: 34 / 34Req Level: 88

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVJlBGQJgRFBREVFBQPVFVVUFFUEBUVFUNCFEFFVVVUBB)

1/1

1/1

1/1

1/1

0/1

2/2

1/1

2/2

1/1

1/1

0/1

0/1

1/1

0/1

1/1

2/2

1/1

0/2

0/1

0/1

2/2

1/1

2/2

0/1

0/1

1/1

0/1

1/1

0/1

1/1

1/1

0/1

0/1

1/1

1/1

0/2

1/1

0/1

1/1

0/1

1/1

1/1

1/1

0/1

1/1

1/1

Spent: 34 / 34Req Level: 88

![](https://wow.zamimg.com/images/wow/icons/medium/classicon_evoker_augmentation.jpg)

Augmentation

Spent: 34 / 34Req Level: 90

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVJlBGQJgRFBREVFBQPVFVVUFFUEBUVFUNCFEFFVVVUBB)

1/1

1/1

1/1

0/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

0/1

0/1

1/1

1/1

0/1

1/1

1/1

1/1

1/1

0/2

0/1

1/1

0/2

0/1

0/1

1/1

1/1

1/1

0/1

1/1

1/1

1/1

0/1

1/1

1/1

1/1

1/1

0/1

0/1

4/4

Spent: 34 / 34Req Level: 90

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Scalecommander

Spent: 13 / 13Req Level: 89

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVJlBGQJgRFBREVFBQPVFVVUFFUEBUVFUNCFEFFVVVUBB)

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

Spent: 13 / 13Req Level: 89

PvP Talents: PvP:

##### Key Talents

![](https://wow.zamimg.com/images/wow/TextureAtlas/live/talents-heroclass-evoker-scalecommander.webp)

Hero:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_eruption.jpg)](https://www.wowhead.com/spell=438587/mass-eruption)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_divideandconquer.jpg)](https://www.wowhead.com/spell=441212/extended-battle)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_deepbreath.jpg)](https://www.wowhead.com/spell=433871/maneuverability)

Spec:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_geomancy.jpg)](https://www.wowhead.com/spell=459120/rumbling-earth)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_plotthefuture.jpg)](https://www.wowhead.com/spell=407866/plot-the-future)[![](https://wow.zamimg.com/images/wow/icons/large/inv_enchant_optionalreagent_01.jpg)](https://www.wowhead.com/spell=412713/interwoven-threads)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_earthensky.jpg)](https://www.wowhead.com/spell=459725/molten-embers)

Class:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_flywithme.jpg)](https://www.wowhead.com/spell=370665/rescue)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_timespiral.jpg)](https://www.wowhead.com/spell=374968/time-spiral)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_hoverblack.jpg)](https://www.wowhead.com/spell=374227/zephyr)

* * *

[Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVJlBGQJgRFBREVFBQPVFVVUFFUEBUVFUNCFEFFVVVUBB) Copy Talents

[Stat Priority](https://www.wowhead.com/guide/20775) IntellectCritHasteMasteryVersatility[Weapons](https://www.wowhead.com/20777) ~~~~~~~~Best in Slot~~~~Alternatives[Trinkets](https://www.wowhead.com/20777) ~~~~~~~~Best in Slot~~~~~~~~~~~~Alternatives[Consumables](https://www.wowhead.com/20759)~~~~~~~~~~~~~~~~[Tier Set](https://www.wowhead.com/20778) ~~~~~~~~~~~~~~~~Best in Slot

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Evoker

Spent: 34 / 34Req Level: 88

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBUVQVNCEQFFVVVUBB)

1/1

1/1

1/1

1/1

0/1

1/2

1/1

2/2

1/1

1/1

0/1

1/1

0/1

1/1

0/1

2/2

1/1

0/2

0/1

0/1

2/2

1/1

2/2

0/1

0/1

1/1

0/1

1/1

0/1

1/1

1/1

0/1

0/1

1/1

1/1

0/2

1/1

0/1

1/1

0/1

1/1

1/1

1/1

1/1

1/1

1/1

Spent: 34 / 34Req Level: 88

![](https://wow.zamimg.com/images/wow/icons/medium/classicon_evoker_augmentation.jpg)

Augmentation

Spent: 34 / 34Req Level: 90

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBUVQVNCEQFFVVVUBB)

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

0/1

0/1

0/1

1/1

1/1

0/1

1/1

1/1

1/1

1/1

0/2

0/1

1/1

0/2

0/1

0/1

1/1

1/1

1/1

0/1

1/1

1/1

1/1

1/1

0/1

0/1

1/1

1/1

1/1

0/1

4/4

Spent: 34 / 34Req Level: 90

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Scalecommander

Spent: 13 / 13Req Level: 89

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBUVQVNCEQFFVVVUBB)

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

Spent: 13 / 13Req Level: 89

PvP Talents: PvP:

##### Key Talents

![](https://wow.zamimg.com/images/wow/TextureAtlas/live/talents-heroclass-evoker-scalecommander.webp)

Hero:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_eruption.jpg)](https://www.wowhead.com/spell=438587/mass-eruption)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_divideandconquer.jpg)](https://www.wowhead.com/spell=441212/extended-battle)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_deepbreath.jpg)](https://www.wowhead.com/spell=433871/maneuverability)

Spec:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_geomancy.jpg)](https://www.wowhead.com/spell=459120/rumbling-earth)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_plotthefuture.jpg)](https://www.wowhead.com/spell=407866/plot-the-future)[![](https://wow.zamimg.com/images/wow/icons/large/inv_enchant_optionalreagent_01.jpg)](https://www.wowhead.com/spell=412713/interwoven-threads)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_earthensky.jpg)](https://www.wowhead.com/spell=459725/molten-embers)

Class:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_flywithme.jpg)](https://www.wowhead.com/spell=370665/rescue)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_timespiral.jpg)](https://www.wowhead.com/spell=374968/time-spiral)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_hoverblack.jpg)](https://www.wowhead.com/spell=374227/zephyr)

* * *

[Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBUVQVNCEQFFVVVUBB) Copy Talents

[Stat Priority](https://www.wowhead.com/guide/20775) IntellectCritHasteMasteryVersatility[Weapons](https://www.wowhead.com/20777) ~~~~~~~~Best in Slot~~~~Alternatives[Trinkets](https://www.wowhead.com/20777) ~~~~~~~~Best in Slot~~~~~~~~~~~~Alternatives[Consumables](https://www.wowhead.com/20759)~~~~~~~~~~~~~~~~[Tier Set](https://www.wowhead.com/20778) ~~~~~~~~~~~~~~~~Best in Slot

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Evoker

Spent: 34 / 34Req Level: 88

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBEVFUdCEQFFVVVUBB)

1/1

1/1

1/1

1/1

0/1

1/2

1/1

2/2

1/1

1/1

0/1

1/1

0/1

1/1

0/1

2/2

1/1

0/2

0/1

0/1

2/2

1/1

2/2

0/1

0/1

1/1

0/1

1/1

0/1

1/1

1/1

0/1

0/1

1/1

1/1

0/2

1/1

0/1

1/1

0/1

1/1

1/1

1/1

1/1

1/1

1/1

Spent: 34 / 34Req Level: 88

![](https://wow.zamimg.com/images/wow/icons/medium/classicon_evoker_augmentation.jpg)

Augmentation

Spent: 34 / 34Req Level: 90

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBEVFUdCEQFFVVVUBB)

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

0/1

0/1

0/1

1/1

1/1

0/1

1/1

1/1

1/1

1/1

0/2

0/1

1/1

0/2

0/1

0/1

1/1

0/1

1/1

0/1

1/1

1/1

1/1

0/1

1/1

1/1

1/1

1/1

0/1

1/1

4/4

Spent: 34 / 34Req Level: 90

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Scalecommander

Spent: 13 / 13Req Level: 89

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBEVFUdCEQFFVVVUBB)

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

1/1

Spent: 13 / 13Req Level: 89

PvP Talents: PvP:

##### Key Talents

![](https://wow.zamimg.com/images/wow/TextureAtlas/live/talents-heroclass-evoker-scalecommander.webp)

Hero:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_eruption.jpg)](https://www.wowhead.com/spell=438587/mass-eruption)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_divideandconquer.jpg)](https://www.wowhead.com/spell=441212/extended-battle)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_deepbreath.jpg)](https://www.wowhead.com/spell=433871/maneuverability)

Spec:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_geomancy.jpg)](https://www.wowhead.com/spell=459120/rumbling-earth)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_plotthefuture.jpg)](https://www.wowhead.com/spell=407866/plot-the-future)[![](https://wow.zamimg.com/images/wow/icons/large/inv_enchant_optionalreagent_01.jpg)](https://www.wowhead.com/spell=412713/interwoven-threads)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_earthensky.jpg)](https://www.wowhead.com/spell=459725/molten-embers)

Class:

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_flywithme.jpg)](https://www.wowhead.com/spell=370665/rescue)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_timespiral.jpg)](https://www.wowhead.com/spell=374968/time-spiral)[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_hoverblack.jpg)](https://www.wowhead.com/spell=374227/zephyr)

* * *

[Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBEVFUdCEQFFVVVUBB) Copy Talents

[Stat Priority](https://www.wowhead.com/guide/20775) IntellectCritHasteMasteryVersatility[Weapons](https://www.wowhead.com/20777) ~~~~~~~~Best in Slot~~~~Alternatives[Trinkets](https://www.wowhead.com/20777) ~~~~~~~~Best in Slot~~~~~~~~~~~~Alternatives[Consumables](https://www.wowhead.com/20759)~~~~~~~~~~~~~~~~[Tier Set](https://www.wowhead.com/20778) ~~~~~~~~~~~~~~~~Best in Slot

## ~~~~ Augmentation Evoker Changes in Midnight

With Midnight, WoW's core combat systems have received substantial changes. Similar to most other specs, Augmentation has received a few key changes that impact how the spec feels to play.

### Removed Abilities

Augmentation lost the following abilities in Midnight:

- **[Renewing Blaze](https://www.wowhead.com/spell=374348)** \- This talent now adds a passive effect to [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_artifact_dragonscales.gif)Obsidian Scales](https://www.wowhead.com/spell=363916/obsidian-scales).

- **[Unravel](https://www.wowhead.com/spell=1264378)** \- This talent now adds a passive effect to [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath).


### New Abilities

Augmentation gains the following major effects through new Apex Talents:

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv12_apextalent_evoker_duplicate.gif)Duplicate](https://www.wowhead.com/spell=1259173/duplicate) (Apex Talent)

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Duplicate](https://www.wowhead.com/spell=1259174/duplicate) (Apex Talent)

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_ouroboros.gif)Duplicate](https://www.wowhead.com/spell=1259175/duplicate) (Apex Talent)


### Big Changes

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) now splits its effect across all DPS players in your raid.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) is no longer used to direct [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might), and can also be triggered by [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_motesofpossibility.gif)Motes of Possibility](https://www.wowhead.com/spell=409267/motes-of-possibility) with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterylifebinder_bronze.gif)Clairvoyant](https://www.wowhead.com/spell=1250914/clairvoyant).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Shifting Sands](https://www.wowhead.com/spell=413984/shifting-sands) still prefers the closest eligible target, but now has more eligible targets in a raid setting.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_spatialparadox.gif)Warp](https://www.wowhead.com/spell=429483/warp) can now be used while casting.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_misc_volatileair.gif)Twin Guardian](https://www.wowhead.com/spell=370888/twin-guardian) now provides a short burst of speed and cast-while-moving instead of a shield.


## Augmentation Evoker Hero Talents: Chronowarden and Scalecommander

For Hero Talents, Augmentation Evokers can choose between the Bronze time magic-themed Chronowarden and the more direct damage-oriented Scalecommander.

The Chronowarden Hero tree includes a variety of updates to the core Augmentation Evoker kit and is primarily focused around Haste and cooldown reduction, with a focus on improving the spec's major group buffs.

Conversely, Scalecommander Augmentation Evokers emphasize personal damage and have a distinct focus on the spec's main cooldown, [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=442204/breath-of-eons).

Both Hero trees have a similar playstyle and bring a similar degree of damage potential, mobility, and utility to the spec, but still excel in different situations. At the moment, the average player might find more success with Scalecommander, particularly in Mythic+ with its strong burst damage and lesser reliance on matching cooldown timings. On the other hand, Chronowarden has damage potential at the top-end but is considerably more reliant on buffing allies.

[![](https://wow.zamimg.com/images/wow/icons/medium/ability_marksmanship.jpg)Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

## ~~~~ Playing an Augmentation Evoker in Midnight Season 1

Augmentation Evoker gameplay is all about weaving together your key damaging abilities and group buffs in order to maximize the damage output of your group. For more details on how to play Augmentation, you can check out our [rotation guide](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps).

|     |     |
| --- | --- |
| |     |     |
| --- | --- |
| ~~~~ | **Keep your buffs up:** Augmentation's rotation is centered around maximizing uptime of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might). [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_sandsoftime.gif)Sands of Time](https://www.wowhead.com/spell=413525/sands-of-time) allows us to extend the duration of Ebon Might through our damaging rotation: casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at appropriate ranks on cooldown, spending resources on [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption), and filling downtime with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) (or [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike)). |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Always be casting:** Keeping high uptime on your rotational spells is key to maintaining a solid resource economy in both raids and Mythic+. Use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) effectively to cast spells on the move, and make sure to fill any "downtime" in your rotation with your filler spells, Living Flame and Azure Strike, in order to deal damage and generate [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst). |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Watch your Essence Burst:** Augmentation Evoker has a few different potential sources of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst), and the buff only stacks up to 2. Make sure to spend your Essence Burst when capped, ideally before casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) generators like [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) and Living Flame to avoid wasting resources. |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Mind your cooldowns:** It's often correct to send cooldowns as soon as they've come back up, but look for opportunities to align your major cooldowns like [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) with allies' cooldowns and big damage moments during an encounter. | |

## ~~~~ Gearing an Augmentation Evoker in Midnight Season 1

As a rough guideline, follow these general stat priorities when gearing your Augmentation Evoker:

- Chronowarden: **Intellect >> Critical Strike > Haste > Mastery > Versatility**

- Scalecommander: **Intellect >> Critical Strike > Haste > Mastery > Versatility**


Don't neglect the value of **Intellect**, as a substantial increase in item level is generally worth it compared to optimized stats. It is always recommended that you use [Raidbots](https://www.raidbots.com/simbot/topgear) to sim your own character since every character has different circumstances. Also, check out our guide to the [Great Vault](https://www.wowhead.com/guide=17592) to learn how to increase the chances of obtaining BiS gear for your Augmentation Evoker.

[![](https://wow.zamimg.com/images/wow/icons/medium/inv_chest_chain_03.jpg)Best-in-Slot Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

## ~~~~ What Professions are Best for Augmentation Evoker?

Compared to previous expansions, professions in Midnight provide minimal benefits towards the performance of your spec. This means that Augmentation Evoker players can choose any profession according to personal preference. You might consider [Leatherworking](https://www.wowhead.com/guide/midnight/professions/leatherworking-overview-trainer-locations-recipes-tools) to craft your own armor, as many profession items can be very close to your [Best in Slot gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear). On the other hand, you may opt for [Alchemy](https://www.wowhead.com/guide/midnight/professions/alchemy-overview-trainer-locations-recipes-tools) to craft consumables or [Enchanting](https://www.wowhead.com/guide/midnight/professions/enchanting-overview-trainer-locations-recipes-tools) to enchant gear without relying on the Auction House.

[![](https://wow.zamimg.com/images/wow/icons/medium/inv_inscription_80_warscroll_intellect.jpg)Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps)

[![](https://wow.zamimg.com/images/wow/icons/medium/ui_concentration.jpg)Professions in Midnight](https://www.wowhead.com/guide/professions/overview)

## ~~~~ What Race is Best for Augmentation Evoker?

Augmentation Evoker can only be Dracthyr for both Horde and Alliance.

* * *

Our Augmentation Evoker guides are always updated with the latest information from in-game experience, simulations, and logs. Make sure to check our changelog for this page by clicking on **View Changelog** in the Quick Facts column or on the book icon at the top of the page. If you are interested in more in-depth Augmentation Evoker guides for **Midnight Season 1**, make sure to browse the _Navigation Bar_ at the top of the page.

* * *

## Feedback

Thanks for reading our class guides! If you have any feedback, feel free to leave a comment in the section below, and we will reply as quickly as possible. If you'd like to talk with any of our writers directly, you can do so by joining our [Discord server](http://discord.gg/wowhead) and finding them there!

![](https://wow.zamimg.com/uploads/author-pages/author/ea925294db5fb08bebba4c014a834604ad94e4ad.jpg)

## Jereico

### World of Warcraft Evoker Class Expert

[Twitch](https://www.twitch.tv/Jereico)[Discord](https://discord.gg/vXB3GJsbFw)[YouTube](https://www.youtube.com/@Jereico)[Bluesky](https://bsky.app/profile/jereico.bsky.social)[Author Page](https://www.wowhead.com/author/Jereico)

Jereico (he, him) has written Evoker class guides and editorial content for Wowhead since 2023. He has been an avid fan of MMOs for nearly 25 years, with countless hours dedicated across classic titles like Runescape, Puzzle Pirates, Maple Story, and Guild Wars before first discovering World of Warcraft in 2007.

If you want to get in touch with Jereico, you can find him in his Community Discord, on Twitter and Bluesky, posting videos to YouTube, and occasionally streaming on Twitch.

[Get WowheadPremium$2A MonthEnjoy an ad-free experience, unlock premium features, & support the site!](https://www.wowhead.com/premium)

Comments (4)

Reset Sort« First‹ Previous**1** \- **4** of **4**Next ›Last »

[Add your comment](https://www.wowhead.com/account=signin) \|Sort: newest first, oldest first, highest rated\|Filter by patch: 11.0.210.1.5

|     |     |     |
| --- | --- | --- |
| 6<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [lrgshadow](https://www.wowhead.com/user=lrgshadow) (4,527 – **17**·21) [on 2023/07/16](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#comments:id=5650322) (Patch 10.1.5) |  |  |

Thank you very much for this. I was quite disappointed with the Augment spec when first announced. I was really hoping for a melee tank or dps spec. But thanks to your writeup and Talent tree, i gave it a shot.

Happy to say it's Much more satisfying than i thought it would be. Go Dragons!

|
| |

|     |     |     |
| --- | --- | --- |
| 6<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [Darclyghte](https://www.wowhead.com/user=Darclyghte) (10,857 – _2_· **14**·28) [on 2023/07/29](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#comments:id=5659092) (Patch 10.1.5) |  |  |

Would love to see Ebon Might scaling higher if it effects less targets. 2 at 60% more and 3 at 30% more would make player deaths in groups feel less personally punishing and give a built in upscaling to work with for arenas so they can remove the other buffs added there.

|
| |

|     |     |     |
| --- | --- | --- |
| 4<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [fxfighter0x03](https://www.wowhead.com/user=fxfighter0x03) (1,480 – **3**·7) [on 2024/08/22](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#comments:id=5925245) (Patch 11.0.2) |  |  |

The "copy talents" for M+ sets spatial paradox instead of time spiral, which is different from what's displayed on the webpage.

Actually, that node is wrong for all the tabs when you copy talents. I think it's flipped.

Last edited by [fxfighter0x03](https://www.wowhead.com/user=fxfighter0x03) on 2024/08/22 (Patch 11.0.2)

|     |     |
| --- | --- |
| 1 | [Jereico](https://www.wowhead.com/user=Jereico) <Guide Author> [on 2024/08/22](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#comments:id=5925245:reply=1704216) (Patch 11.0.2)<br>Thanks for letting me know! The intended build (at the moment) should be running Spatial Paradox, but I’ll also pass this along in case there’s an issue with the import strings. | |

|     |     |     |
| --- | --- | --- |
| 1<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [khdunderscore](https://www.wowhead.com/user=khdunderscore) (1,145 – **2**·4) [on 2023/08/19](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#comments:id=5669130) (Patch 10.1.5) |  |  |

Aerial Mastery is better off being a situational talent instead of core talent. One charge of hover is enough i replaced it with Enkindled or adjust it with a talent corresponding to the weekly affix.

|     |     |
| --- | --- |
| 0 | [khdunderscore](https://www.wowhead.com/user=khdunderscore) [on 2023/12/09](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps#comments:id=5669130:reply=1656040) (Patch 10.2.0)<br>Enkindled is a bad replacement. Better choices are Sleep Walk or Overawe depending on the weekly affix. | |

« First‹ Previous**1** \- **4** of **4**Next ›Last »

## Contribute

Add your comment

Please keep the following in mind when posting a comment:

- Your comment must be in English or it will be removed.

- Unsure how to post? Check out our [handy guide](https://www.wowhead.com/help=commenting-and-you)!

- You might want to proof-read your comments before posting them.

- Please post questions on our [forums](https://www.wowhead.com/forums) for quicker reply.


Post a Comment

You are not logged in. Please [log in](https://www.wowhead.com/account=signin) or [register an account](https://www.wowhead.com/auth/register) to add your comment.

Simply browse for your screenshot using the form below.

- Screenshots containing UI elements are generally declined on sight, the same goes for screenshots from the modelviewer or character selection screen.

- The higher the quality the better!

- Please review our [Screenshot Guidelines](https://www.wowhead.com/help=screenshot-guidelines) before submitting!


You are not logged in. Please [log in](https://www.wowhead.com/account=signin) to submit a screenshot.

Simply type the URL of the video in the form below.

URL: Supported: YouTube only

Title: Optional, up to 200 characters

Note: Your video will need to be approved before appearing on the site.

The **Wowhead Client** is a little application we use to keep our database up to date, and to provide you with some nifty extra functionality on the website!

It serves 2 main purposes:

1. It maintains a WoW addon called the **Wowhead Looter**, which collects data as you play the game!

2. It uploads the **collected data** to Wowhead in order to keep the database up-to-date!


You can also use it to keep track of your completed quests, recipes, mounts, companion pets, and titles!

So, what are you waiting for? [Download the client](https://www.wowhead.com/client) and get started.

Do you want to enable desktop notifications for WoW news?

AcceptDeclineMaybe Later

## Stat Priority
Guide Contents

Patch 12.0.1

**~~~~**
**Midnight**

- [Cheat Sheet](https://www.wowhead.com/guide/classes/evoker/augmentation/cheat-sheet)

- [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

- [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps)

- [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

- [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps)


**~~~~**
**Spec Basics**

- [Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps)

- [Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

- [Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps)

- [Stat Priority](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps)

  - [Stat Recommendations](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps#stat-recommendations)
  - [Stats Explained](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps#stats-explained)
  - [Simulations](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps#simulations)
  - [Diminishing Returns](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps#diminishing-returns)

- [UI & Macros](https://www.wowhead.com/guide/classes/evoker/augmentation/addons-macro-ui-imports)

- [Leveling](https://www.wowhead.com/guide/classes/evoker/augmentation/dps-leveling-tips)


**~~~~**
**Guide Info**

- [Changelog](https://www.wowhead.com/guide/changelog?id=20775)


# Augmentation Evoker Stat Priority - Midnight

[By Jereico](https://www.wowhead.com/author/Jereico)
Updated:
2026/02/25

LiveJereico[Live on Twitch!](https://www.twitch.tv/jereico) Offline on TwitchFollow: Follow [Discord](https://discord.gg/vXB3GJsbFw) [Twitch](https://www.twitch.tv/jereico) [Twitter](https://twitter.com/coffeeandsteve) [YouTube](https://www.youtube.com/@Jereico)

Stats are a key component of customizing your Augmentation Evoker in Midnight. Having the right distribution of stats on your gear can be critical towards optimizing your performance.

This guide details the best stat priority for your Augmentation Evoker, as well as covering how to determine Augmentation Evoker stat priorities personalized for your character in **Midnight Season 1**, as well as how to check whether an item Best-in-Slot, an upgrade, or outright bad.

It also covers Augmentation Evoker's preferred stats in-depth, accounting for nuances and synergies for niche situations that go beyond a generic priority.

[Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps) [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear) [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps) [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps) [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps) [Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps) [![](https://wow.zamimg.com/images/wow/icons/large/inv_misc_groupneedmore.jpg)\\
Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

Show Table of Contents

## ~~~~ Best Stats for Augmentation Evoker

Depending on whether you are playing a Chronowarden or Scalecommander build, your stat preferences shift slightly based on the focus of your chosen Hero Talents. **Note that these recommendations are most applicable at maximum level, and are particularly focused around group play.** While leveling, simply prioritize item level for a smooth experience. We always recommend simulating your own character using Raidbot's Top Gear function, but general stat priority guidelines are:

|     |     |
| --- | --- |
| **Chronowarden Stat Priority**<br>* * *<br>1. **Intellect**<br>   <br>2. **Critical Strike**<br>   <br>3. **Haste**<br>   <br>4. **Mastery**<br>   <br>5. **Versatility** | **Scalecommander Stat Priority**<br>* * *<br>1. **Intellect**<br>   <br>2. **Critical Strike**<br>   <br>3. **Haste**<br>   <br>4. **Mastery**<br>   <br>5. **Versatility** |

While not unlimited, gearing provides considerable freedom when customizing stats. Following the suggestions below, we've tailored recommendations of best-in-slot gear to seek during **Midnight Season 1** for Augmentation Evoker in our Gearing Guide.

[![](https://wow.zamimg.com/images/wow/icons/medium/inv_chest_chain_03.jpg)Augmentation Evoker Gearing Guide](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

## ~~~~ Stats Explained

**Intellect** is the primary stat for Augmentation Evoker, and you'll find it on most of your gear, outside of Rings, Neck, and some Trinkets. For Augmentation, not only does Intellect increase your own Spell Power and damage dealt, but importantly it increases the effectiveness of your core group buff [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might), increasing the main stat of affected allies by a portion of your Intellect.

For Secondary stats, Augmentation Evoker gains the following from each stat:

- **Critical Strike**: Chance for attacks and heals to deal double damage, as well as chance for spells affected by [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_sandsoftime.gif)Sands of Time](https://www.wowhead.com/spell=413525/sands-of-time) to provide an additional 50% [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) duration.

- **Haste**: Decreases the cast time of your spells (including Empowered spells), adds ticks to our DoT effects (such as [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath)), and reduces the Global Cooldown (GCD). Haste also modestly improves the rate at which you generate [Essence](https://www.wowhead.com/resource/essence-19). Additional Notes

These effects have a modest effect on your ability to extend Ebon Might, mainly through being able to occasionally fit additional casts of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) inside the Ebon Might window.

- **Mastery**: [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Mastery: Timewalker](https://www.wowhead.com/spell=406380/mastery-timewalker) has two powerful effects: It increases the amount of Versatility granted to nearby allies through [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Shifting Sands](https://www.wowhead.com/spell=413984/shifting-sands), and also extends the base duration of all Augmentation buffs and helpful auras. Additional Notes

Unlike Critical Strike and Haste, Mastery almost exclusively serves to increase your damage through buffing allies, and provides limited value outside of group play.

- **Versatility**: Increases personal damage and healing, while also reducing damage taken. Additional Notes

Versatility has essentially no impact to Augmentation's ability to buff other players, and its value is limited to your own personal damage output. As a result, it should be considered the weakest Secondary stat for Augmentation Evoker in group play.


## ~~~~ Sim Your Augmentation Evoker

The suggestions for stat priorities mentioned above are generic; exact values will change based on your gear. To gain a proper understanding of your optimal stats, we recommend **simming your character** using various tools available in the community, such as [SimulationCraft](https://www.wowhead.com/guide/how-to-use-simulationcraft-and-pawn-4885). You can easily sim your character and identify your stat priority with Raidbots, an online platform! Explore more about Raidbots in our [comprehensive guide](https://www.wowhead.com/guide/how-to-use-raidbots-and-run-character-simulations-6050).

#### Simulate Your Character Now

RegionEUKRTWUSUS RealmsAegwynnAerie PeakAgamagganAggramarAkamaAlexstraszaAlleriaAltar of StormsAlterac MountainsAman'ThulAndorhalAnetheronAntonidasAnub'arakAnvilmarArathorArchimondeArea 52Argent DawnArthasArygosAuchindounAzgalorAzjol-NerubAzralonAzsharaAzuremystBaelgunBalnazzarBarthilasBlack DragonflightBlackhandBlackrockBlackwater RaidersBlackwing LairBlade's EdgeBladefistBleeding HollowBlood FurnaceBloodhoofBloodscalpBonechewerBorean TundraBoulderfistBronzebeardBurning BladeBurning LegionCaelestraszCairneCenarion CircleCenariusCho'gallChromaggusCoilfangCrushridgeDaggerspineDalaranDalvengyrDark IronDarkspearDarrowmereDath'RemarDawnbringerDeathwingDemon SoulDentargDestromathDethecusDetherocDoomhammerDraenorDragonblightDragonmawDrak'TharonDrak'thulDrakaDrakkariDreadmaulDrendenDunemaulDurotanDuskwoodEarthen RingEcho IslesEitriggEldre'ThalasEluneEmerald DreamEonarEredarExecutusExodarFarstridersFeathermoonFenrisFiretreeFizzcrankFrostmaneFrostmourneFrostwolfGalakrondGallywixGarithosGaronaGarroshGhostlandsGilneasGnomereganGoldrinnGorefiendGorgonnashGreymaneGrizzly HillsGul'danGundrakGurubashiHakkarHaomarushHellscreamHydraxisHyjalIcecrownIllidanJaedenarJubei'ThosKael'thasKalecgosKargathKel'ThuzadKhadgarKhaz ModanKhaz'gorothKil'jaedenKilroggKirin TorKorgathKorialstraszKul TirasLaughing SkullLethonLightbringerLightning's BladeLightninghoofLlaneLotharMadoranMaelstromMagtheridonMaievMal'GanisMalfurionMalorneMalygosMannorothMedivhMishaMok'NathalMoon GuardMoonrunnerMug'tholMuradinNagrandNathrezimNazgrelNazjatarNemesisNer'zhulNesingwaryNordrassilNorgannonOnyxiaPerenoldeProudmooreQuel'doreiQuel'ThalasRagnarosRavencrestRavenholdtRexxarRivendareRunetotemSargerasSaurfangScarlet CrusadeScillaSen'jinSentinelsShadow CouncilShadowmoonShadowsongShandrisShattered HallsShattered HandShu'haloSilver HandSilvermoonSisters of EluneSkullcrusherSkywallSmolderthornSpinebreakerSpirestoneStaghelmSteamwheedle CartelStonemaulStormrageStormreaverStormscaleSuramarTanarisTerenasTerokkarThaurissanThe Forgotten CoastThe ScryersThe UnderbogThe Venture CoThorium BrotherhoodThrallThunderhornThunderlordTichondriusTol BaradTortheldrinTrollbaneTuralyonTwisting NetherUldamanUldumUndermineUrsinUS PS Realm 222UtherVashjVek'nilashVelenWarsongWhisperwindWildhammerWindrunnerWinterhoofWyrmrest AccordYseraYsondreZangarmarshZul'jinZuluhedSubmit

Complete the fields above to go to [Raidbots](https://www.raidbots.com/) and find out the best stats for your character right now!

## ~~~~ Diminishing Returns in Midnight

Accumulating too much of one Secondary stat from your gear leads to diminishing returns. This means that adding more of the same stat beyond certain thresholds results in reduced benefits. These thresholds are fixed and reduce the amount gained from more of that stat rating by 10% per breakpoint. Each stat has a different rating threshold where the reduction begins:

- **Critical Strike** \- Above 1380 rating

- **Haste** \- Above 1320 rating

- **Mastery** \- Above 1380 rating

- **Versatility** \- Above 1620 rating


**Example**

Let's assume you gain 1% Haste for 10 Haste Rating. When above the diminishing return breakpoint, 10 Haste Rating would give you 0.9% Haste instead, resulting in a 10% reduction from what you gained previously.

Note that this system **only counts stat rating**, meaning that percentage-based procs and effects like [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_nature_bloodlust.gif)Bloodlust](https://www.wowhead.com/spell=2825/bloodlust) aren't factored in and will always grant their full benefit.

You can learn more about stat diminishing returns in our detailed guide:

[What are Stat Diminishing Returns](https://www.wowhead.com/guide/diminishing-returns-on-secondary-stats-in-world-of-warcraft)

* * *

Our Augmentation Evoker guides are always updated with the latest information from in-game experience, simulations, and logs. Make sure to check our changelog for this page by clicking on **View Changelog** in the Quick Facts column or on the book icon at the top of the page. If you are interested in more in-depth Augmentation Evoker guides for **Midnight Season 1**, make sure to browse the _Navigation Bar_ at the top of the page.

* * *

## Feedback

Thanks for reading our class guides! If you have any feedback, feel free to leave a comment in the section below, and we will reply as quickly as possible. If you'd like to talk with any of our writers directly, you can do so by joining our [Discord server](http://discord.gg/wowhead) and finding them there!

![](https://wow.zamimg.com/uploads/author-pages/author/ea925294db5fb08bebba4c014a834604ad94e4ad.jpg)

## Jereico

### World of Warcraft Evoker Class Expert

[Twitch](https://www.twitch.tv/Jereico)[Discord](https://discord.gg/vXB3GJsbFw)[YouTube](https://www.youtube.com/@Jereico)[Bluesky](https://bsky.app/profile/jereico.bsky.social)[Author Page](https://www.wowhead.com/author/Jereico)

Jereico (he, him) has written Evoker class guides and editorial content for Wowhead since 2023. He has been an avid fan of MMOs for nearly 25 years, with countless hours dedicated across classic titles like Runescape, Puzzle Pirates, Maple Story, and Guild Wars before first discovering World of Warcraft in 2007.

If you want to get in touch with Jereico, you can find him in his Community Discord, on Twitter and Bluesky, posting videos to YouTube, and occasionally streaming on Twitch.

[Get WowheadPremium$2A MonthEnjoy an ad-free experience, unlock premium features, & support the site!](https://www.wowhead.com/premium)

Comments

Reset Sort« First‹ Previous**1** \- **0** of **0**Next ›Last »

[Add your comment](https://www.wowhead.com/account=signin) \|Sort: newest first, oldest first, highest rated\|Filter by patch:

**No comments have been posted yet.**

Please [log in](https://www.wowhead.com/account=signin) to add your comment, or [register](https://www.wowhead.com/auth/register) if you don't already have an account.

« First‹ Previous**1** \- **0** of **0**Next ›Last »

## Contribute

Add your comment

Please keep the following in mind when posting a comment:

- Your comment must be in English or it will be removed.

- Unsure how to post? Check out our [handy guide](https://www.wowhead.com/help=commenting-and-you)!

- You might want to proof-read your comments before posting them.

- Please post questions on our [forums](https://www.wowhead.com/forums) for quicker reply.


Post a Comment

You are not logged in. Please [log in](https://www.wowhead.com/account=signin) or [register an account](https://www.wowhead.com/auth/register) to add your comment.

Simply browse for your screenshot using the form below.

- Screenshots containing UI elements are generally declined on sight, the same goes for screenshots from the modelviewer or character selection screen.

- The higher the quality the better!

- Please review our [Screenshot Guidelines](https://www.wowhead.com/help=screenshot-guidelines) before submitting!


You are not logged in. Please [log in](https://www.wowhead.com/account=signin) to submit a screenshot.

Simply type the URL of the video in the form below.

URL: Supported: YouTube only

Title: Optional, up to 200 characters

Note: Your video will need to be approved before appearing on the site.

The **Wowhead Client** is a little application we use to keep our database up to date, and to provide you with some nifty extra functionality on the website!

It serves 2 main purposes:

1. It maintains a WoW addon called the **Wowhead Looter**, which collects data as you play the game!

2. It uploads the **collected data** to Wowhead in order to keep the database up-to-date!


You can also use it to keep track of your completed quests, recipes, mounts, companion pets, and titles!

So, what are you waiting for? [Download the client](https://www.wowhead.com/client) and get started.

Do you want to enable desktop notifications for WoW news?

AcceptDeclineMaybe Later

## Core Abilities
Guide Contents

Patch 12.0.1

**~~~~**
**Midnight**

- [Cheat Sheet](https://www.wowhead.com/guide/classes/evoker/augmentation/cheat-sheet)

- [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

- [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps)

- [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

- [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps)


**~~~~**
**Spec Basics**

- [Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps)

- [Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

- [Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps)

  - [Baseline Spells](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps#baseline-spells)
  - [Hero Talents](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps#hero-talents)
  - [Talents](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps#talents)

    - [Class Talents](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps#class-talents)
    - [Spec Talents](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps#spec-talents)

- [Stat Priority](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps)

- [UI & Macros](https://www.wowhead.com/guide/classes/evoker/augmentation/addons-macro-ui-imports)

- [Leveling](https://www.wowhead.com/guide/classes/evoker/augmentation/dps-leveling-tips)


**~~~~**
**Guide Info**

- [Changelog](https://www.wowhead.com/guide/changelog?id=20724)


# Augmentation Evoker Abilities and Talents Guide - Midnight

[By Jereico](https://www.wowhead.com/author/Jereico)
Updated:
2026/03/11

LiveJereico[Live on Twitch!](https://www.twitch.tv/jereico) Offline on TwitchFollow: Follow [Discord](https://discord.gg/vXB3GJsbFw) [Twitch](https://www.twitch.tv/jereico) [Twitter](https://twitter.com/coffeeandsteve) [YouTube](https://www.youtube.com/@Jereico)

Explore the depths of the Augmentation Evoker talent tree, which contains the bulk of your abilities and customization options. In this Augmentation Evoker guide, we review all the different abilities and talents in **Midnight Season 1**, including an explanation for what they do and how to use them correctly.

[Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps) [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear) [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps) [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps) [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps) [Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps) [![](https://wow.zamimg.com/images/wow/icons/large/inv_misc_groupneedmore.jpg)\\
Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

Show Table of Contents

## ~~~~ Baseline Augmentation Evoker Spells

### Offensive Abilities

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) ( **AS**): Filler ability. Claw at enemies to instantly cleave multiple targets.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) ( **LF**): Filler ability with a twist. Send a bolt of flame to damage an enemy **or** heal an ally. You can cast this on yourself as a heal.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_disintegrate.gif)Disintegrate](https://www.wowhead.com/spell=356995/disintegrate): [Essence](https://www.wowhead.com/resource/essence-19) Spender. Channel a beam on the target, dealing damage over time and slowing them. Eventually replaced by [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) for Augmentation.


### Offensive Cooldowns

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) ( **FB**): Empower your breath and release a burning cone that deals damage and applies a damage over time (DoT) effect to enemies. Empowering this ability increases the upfront damage at the cost of duration on the DoT.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_furyoftheaspects.gif)Fury of the Aspects](https://www.wowhead.com/spell=390386/fury-of-the-aspects): This is the Evoker version of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_nature_bloodlust.gif)Bloodlust](https://www.wowhead.com/spell=2825/bloodlust). It increases the Haste of all allies for a time.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_deepbreath.gif)Deep Breath](https://www.wowhead.com/spell=357210/deep-breath): Remove all roots and become immune to CC effets as you decimate enemies in your path with volcanic flame. Generally replaced by [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) for Augmentation.


### Defensive/Healing Cooldowns

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom): AoE Healing on a short cooldown. Place a bulb that blossoms into a heal for injured allies.


### Utility Abilities

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover): Movement ability. Launch yourself in a direction and gain the ability to cast while moving for a time. If used without directional input, you hover in place, and this effect can be used while casting other spells.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blessingofthebronze.gif)Blessing of the Bronze](https://www.wowhead.com/spell=364342/blessing-of-the-bronze): Raid buff. This spell decreases the cooldown of your allies movement ability. The affected ability [depends on the class](https://www.wowhead.com/news/new-evoker-raid-buff-in-dragonflight-blessing-of-the-bronze-327698). For Evoker, it gives [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) a shorter cooldown.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_return.gif)Return](https://www.wowhead.com/spell=361227/return): Bring an ally back to life. Only available outside of combat.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_tailswipe.gif)Tail Swipe](https://www.wowhead.com/spell=368970/tail-swipe): Evoker-specific Racial ability. Swing your tail and knock enemies around you into the air.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_wingbuffet.gif)Wing Buffet](https://www.wowhead.com/spell=357214/wing-buffet): Dracthyr Racial ability. Flap your wings to knock away enemies in front of you.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_glide.gif)Glide](https://www.wowhead.com/spell=358733/glide): Dracthyr Racial ability. Slow your falling speed and gain control of your momentum.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_soar.gif)Soar](https://www.wowhead.com/spell=381322/soar): Dracthyr Racial ability. Take to the skies and gain Dragonriding controls.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_visage.gif)Visage](https://www.wowhead.com/spell=372014/visage): Dracthyr Racial ability. Assume your Visage form, significantly increasing your out of combat health regeneration and showing off your transmog.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_hunter_aspectoftheviper.gif)Sense Power](https://www.wowhead.com/spell=361021/sense-power): Augmentation-specific ability. Toggle this ability to add a buff indicator to friendly unit frames when your allies are using their major cooldowns.


### Passive Abilities

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Mastery: Timewalker](https://www.wowhead.com/spell=406380/mastery-timewalker): Casting an Empower spell temporarily grants increased Versatility to a nearby ally, preferring damage dealers. Mastery also increases the duration of all of your helpful buffs and auras.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_dragonriding_yearningforthesky01.gif)Close as Clutchmates](https://www.wowhead.com/spell=396043/close-as-clutchmates): Two of your main group buffs, [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons), are more effective outside of raid. This exists to balance the fact that group content usually includes a Tank and Healer, and also helps with solo content.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_nourishingsands.gif)Nourishing Sands](https://www.wowhead.com/spell=406041/nourishing-sands): Dealing a killing blow on an enemy target resets the cooldown and increases the potency of your next [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_sandsoftime.gif)Sands of Time](https://www.wowhead.com/spell=413525/sands-of-time): Certain Augmentation spells increase the active duration of your group buff, [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might). This effect can critically strike, further increasing the duration extended.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_misc_orb_05.gif)Energizing Flame](https://www.wowhead.com/spell=400006/energizing-flame): Casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) as an offensive ability refunds a portion of its Mana cost.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_misc_scales_dragonblue03.gif)Tempered Scales](https://www.wowhead.com/spell=396571/tempered-scales): Your scales increases your armor by 75%. This makes Evokers take less physical damage.


## Augmentation Evoker Hero Talents

### Chronowarden Augmentation Evoker Talents

**Key Talent**

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_chronowardenevoker_chronoflame.gif)Chrono Flame](https://www.wowhead.com/spell=431442/chrono-flame): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) now repeats a portion of your damage and healing dealt to the target within the last 5 seconds.


**Capstone Talent**

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Afterimage](https://www.wowhead.com/spell=431875/afterimage): Empower spells will also send a [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_chronowardenevoker_chronoflame.gif)Chrono Flame](https://www.wowhead.com/spell=431442/chrono-flame) at each enemy hit, up to 3.


**Passives**

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_spatialparadox.gif)Warp](https://www.wowhead.com/spell=429483/warp): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) now behaves similar to [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_arcane_blink.gif)Blink](https://www.wowhead.com/spell=1953/blink) and has a shorter cooldown.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst5.gif)Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) is now a damage cooldown that increases your Haste, Movement Speed, and Cooldown Recovery Rate.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_aspectsfavorbronze.gif)Nozdormu Adept](https://www.wowhead.com/spell=431715/nozdormu-adept): Buff that echoes a portion of an ally's damage or healing for a short time when you cast an Empower spell during [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst5.gif)Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Chronoboon](https://www.wowhead.com/spell=1260484/chronoboon): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales)' cooldown is reduced by 30 sec.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_innatemagic4.gif)Energy Cycles](https://www.wowhead.com/spell=1260568/energy-cycles): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst5.gif)Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst) grants [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) every 6 sec.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_holy_borrowedtime.gif)Overclock](https://www.wowhead.com/spell=1260647/overclock): [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_chronowardenevoker_chronoflame.gif)Chrono Flame](https://www.wowhead.com/spell=431442/chrono-flame) maximum damage and healing is increased.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_giftoftheaspects.gif)Reverberations](https://www.wowhead.com/spell=431615/reverberations): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) deals additional damage over time.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_misc_pocketwatch_01.gif)Primacy](https://www.wowhead.com/spell=431657/primacy): Active [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) damage over time effects provide you with additional Haste.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/achievement_faction_goldenlotus.gif)Golden Opportunity](https://www.wowhead.com/spell=432004/golden-opportunity): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) has a chance to give your next [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) a longer duration.


**Choice Nodes**

- Choice Node 1:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_return.gif)Temporality](https://www.wowhead.com/spell=431873/temporality): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_spatialparadox.gif)Warp](https://www.wowhead.com/spell=429483/warp) reduces damage taken for a short time.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/item_timemote_icon.gif)Motes of Acceleration](https://www.wowhead.com/spell=432008/motes-of-acceleration): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_spatialparadox.gif)Warp](https://www.wowhead.com/spell=429483/warp) drops motes that increase allies' movement speed when they walk through the motes.


- Choice Node 2:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_holy_borrowedtime.gif)Double-time](https://www.wowhead.com/spell=431874/double-time): [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) can now critically strike, granting additional stats.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_plotthefuture.gif)Time Convergence](https://www.wowhead.com/spell=431984/time-convergence): Your non-defensive cooldowns increase your Intellect for a short time, extended by casting [Essence](https://www.wowhead.com/resource/essence-19) spells.


- Choice Node 3:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_defyfate.gif)Master of Destiny](https://www.wowhead.com/spell=431840/master-of-destiny): [Essence](https://www.wowhead.com/resource/essence-19) spells extend the duration of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_aspectsfavorbronze.gif)Nozdormu Adept](https://www.wowhead.com/spell=431715/nozdormu-adept).

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_dragonriding_bronzerewind01.gif)Instability Matrix](https://www.wowhead.com/spell=431484/instability-matrix): Reduces the cooldown of your Empower spells.


### Scalecommander Augmentation Evoker Talents

**Key Talent**

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Mass Eruption](https://www.wowhead.com/spell=438587/mass-eruption): Empower spells cause your next [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) to also strike additional targets, or slightly increase [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) damage on fewer targets.


**Capstone Talent**

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_deepbreath.gif)Maneuverability](https://www.wowhead.com/spell=433871/maneuverability): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=442204/breath-of-eons) can now be actively steered to some extent, instead of using the targeting reticle. Also applies a DoT to enemies hit.


**Passives**

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blackattunementalt.gif)Might of the Black Dragonflight](https://www.wowhead.com/spell=441705/might-of-the-black-dragonflight): Your Black spells deal more damage.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_10_gearupgrade_drakesshadowflameenhancedcrest.gif)Melt Armor](https://www.wowhead.com/spell=441176/melt-armor): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=442204/breath-of-eons) causes enemies to take more damage from your [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments) and [Essence](https://www.wowhead.com/resource/essence-19) abilities.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Mass Eruption](https://www.wowhead.com/spell=438587/mass-eruption) marks your primary target, causing allies' attacks against that target to have a chance to deal additional damage, split among nearby enemies.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_soar.gif)Wingleader](https://www.wowhead.com/spell=441206/wingleader): [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments) slightly reduces the cooldown of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=442204/breath-of-eons) for each target hit.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_fire_soulburn.gif)Onslaught](https://www.wowhead.com/spell=441245/onslaught): Gain a stack of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_fire_soulburn.gif)Burnout](https://www.wowhead.com/spell=375801/burnout) when you enter combat.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_siege_engineer_superheated.gif)Unrelenting Siege](https://www.wowhead.com/spell=441246/unrelenting-siege): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike), [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame), and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) deal additional damage the longer you are in combat.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_dragonriding_dynamicflight01.gif)Command Squadron](https://www.wowhead.com/spell=1260745/command-squadron): While flying in [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=442204/breath-of-eons), two Dracthyr Commandos cast up to 4 [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_pyre.gif)Pyre](https://www.wowhead.com/spell=1236970/pyre) s each at enemy targets.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_10_dungeonjewelry_dragon_trinket_1arcanemagical_blue.gif)Concentrated Power](https://www.wowhead.com/spell=1261448/concentrated-power): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Mass Eruption](https://www.wowhead.com/spell=438587/mass-eruption) hits one additional target.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburststacks.gif)Refined Essence](https://www.wowhead.com/spell=1261452/refined-essence): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) deals 15% more damage.


**Choice Nodes**

- Choice Node 1:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_10_skinning_scales_black.gif)Hardened Scales](https://www.wowhead.com/spell=441180/hardened-scales): [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_artifact_dragonscales.gif)Obsidian Scales](https://www.wowhead.com/spell=363916/obsidian-scales) is now stronger.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_wingbuffet.gif)Menacing Presence](https://www.wowhead.com/spell=441181/menacing-presence): Knocking enemies up or backwards reduces their damage done to you.


- Choice Node 2:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_divideandconquer.gif)Extended Battle](https://www.wowhead.com/spell=441212/extended-battle): Essence abilities extend the duration of active [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments).

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_powerswell.gif)Diverted Power](https://www.wowhead.com/spell=441219/diverted-power): [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments) have a chance to activate [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst).


- Choice Node 3:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Nimble Flyer](https://www.wowhead.com/spell=441253/nimble-flyer): You take reduced damage from area of effect attacks while [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) is active.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_dragonriding_barrelroll01.gif)Slipstream](https://www.wowhead.com/spell=441257/slipstream): Casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=442204/breath-of-eons) resets the cooldown of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover).


## ~~~~ Augmentation Evoker Talents

### Evoker Class Talents

#### Row 1 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_earthen_pillar.gif)Landslide](https://www.wowhead.com/spell=358385/landslide): Sends out a path of stone that roots enemies. Damage can break this effect.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_artifact_dragonscales.gif)Obsidian Scales](https://www.wowhead.com/spell=363916/obsidian-scales): Defensive cooldown that reduces your damage taken for a short time.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_fontofmagic_green.gif)Expunge](https://www.wowhead.com/spell=365585/expunge): Removes a Poison debuff from an ally.


#### Row 2 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_frost_frostblast.gif)Natural Convergence](https://www.wowhead.com/spell=369913/natural-convergence): Passively makes [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_disintegrate.gif)Disintegrate](https://www.wowhead.com/spell=356995/disintegrate) channel faster and reduces the cast time of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_wingbuffet.gif)Heavy Wingbeats](https://www.wowhead.com/spell=368838/heavy-wingbeats): Reduces the cooldown of your racial ability, [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_wingbuffet.gif)Wing Buffet](https://www.wowhead.com/spell=357214/wing-buffet).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_rescue.gif)Verdant Embrace](https://www.wowhead.com/spell=360995/verdant-embrace) ( **VE**): Healing and mobility cooldown. Fly to an ally and heal them, or heal yourself instantly.


#### Row 3 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_earthen_pillar.gif)Forger of Mountains](https://www.wowhead.com/spell=375528/forger-of-mountains): Cooldown reduction and buff for [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_earthen_pillar.gif)Landslide](https://www.wowhead.com/spell=358385/landslide) that makes it harder to break.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_innatemagic4.gif)Innate Magic](https://www.wowhead.com/spell=375520/innate-magic): [Essence](https://www.wowhead.com/resource/essence-19) recharges slightly faster.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_shield_1h_revenantfire_d_01.gif)Obsidian Bulwark](https://www.wowhead.com/spell=375406/obsidian-bulwark): [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_artifact_dragonscales.gif)Obsidian Scales](https://www.wowhead.com/spell=363916/obsidian-scales) gains an additional charge.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Enkindled](https://www.wowhead.com/spell=375554/enkindled): Increases the healing and damage of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_bijou_red.gif)Scarlet Adaptation](https://www.wowhead.com/spell=372469/scarlet-adaptation): Passively stores effective healing to increase the damage of your next [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame).


#### Row 4 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_holy_spellwarding.gif)Inner Radiance](https://www.wowhead.com/spell=386405/inner-radiance): The healing effectiveness of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom) are increased when used on yourself.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_recall.gif)Recall](https://www.wowhead.com/spell=371806/recall): Allows you to return to where you were when you used [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_deepbreath.gif)Deep Breath](https://www.wowhead.com/spell=357210/deep-breath), provided you use it within 3 seconds of landing. This ability incurs a global cooldown.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_tailswipe.gif)Clobbering Sweep](https://www.wowhead.com/spell=375443/clobbering-sweep): Reduces the cooldown of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_tailswipe.gif)Tail Swipe](https://www.wowhead.com/spell=368970/tail-swipe).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_skyreach_wind.gif)Tailwind](https://www.wowhead.com/spell=375556/tailwind): Increases your speed for a brief time when using [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_fontofmagic_red.gif)Cauterizing Flame](https://www.wowhead.com/spell=374251/cauterizing-flame) ( **Caut**): Removes all Bleed, Poison, Curse, and Disease effects from an ally and heal them.


#### Row 5 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_elemental_mote_fire01.gif)Ancient Flame](https://www.wowhead.com/spell=369990/ancient-flame): Healing with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom) or [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_rescue.gif)Verdant Embrace](https://www.wowhead.com/spell=360995/verdant-embrace) speeds up your next [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) cast.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_arcane_studentofmagic.gif)Instinctive Arcana](https://www.wowhead.com/spell=376164/instinctive-arcana): A passive increase to all magic damage you deal.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) ( **Tip**): Cooldown that causes your next [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) or [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) to be instant and fully Empowered.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_rogue_imrovedrecuperate.gif)Attuned to the Dream](https://www.wowhead.com/spell=376930/attuned-to-the-dream): Increases your healing done and the healing you take.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_xavius_dreamsimulacrum.gif)Sleep Walk](https://www.wowhead.com/spell=360806/sleep-walk): Crowd Control (CC) effect. Disorient an enemy, causing them to walk towards you. Damage can break this effect.


#### Row 6 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Protracted Talons](https://www.wowhead.com/spell=369909/protracted-talons): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) damages one additional enemy.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_misc_rubysanctum1.gif)Inherent Resistance](https://www.wowhead.com/spell=375544/inherent-resistance): Passive magic damage reduction.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_helm_mail_dracthyrquest_b_02.gif)Draconic Legacy](https://www.wowhead.com/spell=376166/draconic-legacy): Passive increase to your Stamina.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Extended Flight](https://www.wowhead.com/spell=375517/extended-flight): Increases the duration of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Bountiful Bloom](https://www.wowhead.com/spell=370886/bountiful-bloom): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom) heals additional targets.


#### Row 7 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_frost_manarecharge.gif)Regenerative Magic](https://www.wowhead.com/spell=387787/regenerative-magic): Provides a small amount of Leech.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Blast Furnace](https://www.wowhead.com/spell=375510/blast-furnace): Increases the duration of the DoT from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover2.gif)Exuberance](https://www.wowhead.com/spell=375542/exuberance): Provides a passive increase to movement speed while your Health is high.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterylifebinder_red.gif)Renewing Blaze](https://www.wowhead.com/spell=374348/renewing-blaze): Damage mitigated by [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_artifact_dragonscales.gif)Obsidian Scales](https://www.wowhead.com/spell=363916/obsidian-scales) is healed back over time. Each damage event creates a healing over time (HoT) effect that heals every 2 seconds, over 8 seconds. Multiple instances of damage over the duration will extend the HoT.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_misc_monsterscales_06.gif)Walloping Blow](https://www.wowhead.com/spell=387341/walloping-blow): Increases the effect of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_wingbuffet.gif)Wing Buffet](https://www.wowhead.com/spell=357214/wing-buffet) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_tailswipe.gif)Tail Swipe](https://www.wowhead.com/spell=368970/tail-swipe) and adds a slow.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_druid_protectionofthegrove.gif)Panacea](https://www.wowhead.com/spell=387761/panacea): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_rescue.gif)Verdant Embrace](https://www.wowhead.com/spell=360995/verdant-embrace) instantly heal you when cast.


#### Row 8 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timedilation.gif)Stretch Time](https://www.wowhead.com/spell=410352/stretch-time): Stagger all damage taken while flying with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) active.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_unravel.gif)Unravel](https://www.wowhead.com/spell=1264378/unravel): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath)'s initial hit deals additional damage to absorption shields. This cannot do damage to a target's health.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_oppressingroar.gif)Oppressing Roar](https://www.wowhead.com/spell=372048/oppressing-roar): Apply a debuff to targets in a cone in front of you that increases the duration of CC effects for a short time. This effect persists for the full duration and is not removed by other forms of CC.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_fire_incinerate.gif)Foci of Life](https://www.wowhead.com/spell=375574/foci-of-life): Speeds up the healing of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterylifebinder_red.gif)Renewing Blaze](https://www.wowhead.com/spell=374348/renewing-blaze)'s HoT.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_flywithme.gif)Rescue](https://www.wowhead.com/spell=370665/rescue): Grab an ally within 30 yards, then travel with them up to 30 yards from your initial location. This can be used to move someone up to 60 yards if used at max range. The ally being rescued is able to cast while you taxi them.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_staff_2h_bloodelf_c_01.gif)Lush Growth](https://www.wowhead.com/spell=375561/lush-growth): Increases effectiveness of Green spells.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blue_01.gif)Source of Magic](https://www.wowhead.com/spell=369459/source-of-magic): Place a buff on an friendly Healer that returns a small amount of Mana each time you Empower a spell. The mana returned depends on the Empowerment level.


#### Row 9 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_glide.gif)Strike from Above](https://www.wowhead.com/spell=1267206/strike-from-above): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_glide.gif)Glide](https://www.wowhead.com/spell=358733/glide) speed and height increased.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_pupilofalexstraza.gif)Leaping Flames](https://www.wowhead.com/spell=369939/leaping-flames): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) causes [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) to hit additional targets. If there are no enemies to hit, [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) will instead heal allies. The amount of targets added depends on Empowerment level.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_oppressingroar2.gif)Overawe](https://www.wowhead.com/spell=374346/overawe): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_oppressingroar.gif)Oppressing Roar](https://www.wowhead.com/spell=372048/oppressing-roar) removes Enrage effects and gains cooldown reduction per enrage removed.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_aerialmastery.gif)Aerial Mastery](https://www.wowhead.com/spell=365933/aerial-mastery): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) gains an additional charge.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_misc_volatileair.gif)Twin Guardian](https://www.wowhead.com/spell=370888/twin-guardian): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_flywithme.gif)Rescue](https://www.wowhead.com/spell=370665/rescue) grants additional movement speed and allows spells to be cast while moving for you and your ally for a short duration.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_magic_managain.gif)Potent Mana](https://www.wowhead.com/spell=418101/potent-mana): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blue_01.gif)Source of Magic](https://www.wowhead.com/spell=369459/source-of-magic) also increases target's damage and healing.


#### Row 10 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_terroroftheskies.gif)Terror of the Skies](https://www.wowhead.com/spell=371032/terror-of-the-skies): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_deepbreath.gif)Deep Breath](https://www.wowhead.com/spell=357210/deep-breath) briefly stuns enemies.

- Choice node:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timespiral.gif)Time Spiral](https://www.wowhead.com/spell=374968/time-spiral): Grant allies a free use of their movement ability for a brief time, even if it is on cooldown. For Evokers, this can be used to gain another use of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover). This affects the same spells as [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blessingofthebronze.gif)Blessing of the Bronze](https://www.wowhead.com/spell=364342/blessing-of-the-bronze).

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_stretchtime.gif)Spatial Paradox](https://www.wowhead.com/spell=406732/spatial-paradox): Allows both a targeted Healer and the Evoker to cast while moving and also increases their range for a short duration. Chooses the nearest Healer within 60 yards if you do not have one targeted.


- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hoverblack.gif)Zephyr](https://www.wowhead.com/spell=374227/zephyr): When activated, this ability increases the movement speed of you and your 4 nearest allies for a short duration. It also reduces the damage that all of you take from AoE attacks.


### Augmentation Specialization Talents

#### Apex Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv12_apextalent_evoker_duplicate.gif)Duplicate](https://www.wowhead.com/spell=1259173/duplicate): Casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) summons a copy of yourself that lasts for 20 sec and casts [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption), [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath), and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Duplicate](https://www.wowhead.com/spell=1259174/duplicate): Any time you extend [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might), your active [![](https://wow.zamimg.com/images/wow/icons/tiny/inv12_apextalent_evoker_duplicate.gif)Duplicate](https://www.wowhead.com/spell=1259173/duplicate) is also extended by up to the same amount.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_ouroboros.gif)Duplicate](https://www.wowhead.com/spell=1259175/duplicate): While your [![](https://wow.zamimg.com/images/wow/icons/tiny/inv12_apextalent_evoker_duplicate.gif)Duplicate](https://www.wowhead.com/spell=1259173/duplicate) is active, [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) grants 100% additional stats to allies, and you deal extra damage with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval).


#### Row 1 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) ( **EM**): Augmentation’s main group buff. Increases your damage, as well as the Primary stat of nearby allies.


#### Row 2 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption): Causes the ground beneath your target to erupt, dealing damage split between them and nearby enemies. Replaces [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_disintegrate.gif)Disintegrate](https://www.wowhead.com/spell=356995/disintegrate).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=396187/essence-burst) ( **EB**): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) have a chance to give you [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst), making your next [Essence](https://www.wowhead.com/resource/essence-19) ability free.


#### Row 3 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_quell.gif)Quell](https://www.wowhead.com/spell=351338/quell): A ranged interrupt on a 20 sec cooldown.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_rhyolith_volcano.gif)Ricocheting Pyroclast](https://www.wowhead.com/spell=406659/ricocheting-pyroclast): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) now deals additional damage for each enemy struck, up to 5.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburststacks.gif)Essence Attunement](https://www.wowhead.com/spell=375722/essence-attunement): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) can now stack up to 2 times.

- Choice node:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_pupilofalexstraza.gif)Pupil of Alexstrasza](https://www.wowhead.com/spell=407814/pupil-of-alexstrasza): When cast at an enemy, [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) will hit one additional enemy near the original target if a second target exists.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_echoingstrike.gif)Echoing Strike](https://www.wowhead.com/spell=410784/echoing-strike): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) has a small chance to cast again, based on the number of enemies hit. This effect can repeat.


#### Row 4 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval): Deals damage to enemies in the target radius and launches them into the air. Empowering this spell significantly increases the area of effect radius.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) ( **BoE/Eons**): Fly overhead, amplifying damage taken by enemies hit for ten seconds. Also grants additional [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) duration. Replaces [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_deepbreath.gif)Deep Breath](https://www.wowhead.com/spell=357210/deep-breath).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_defyfate.gif)Defy Fate](https://www.wowhead.com/spell=404195/defy-fate): Powerful cheat death effect that also heals nearby allies on activation.


#### Row 5 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_fire_immolation.gif)Ignition Rush](https://www.wowhead.com/spell=408775/ignition-rush) ( **IR**): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) reduces the cast time of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_powernexus.gif)Power Nexus](https://www.wowhead.com/spell=369908/power-nexus): Increases your maximum [Essence](https://www.wowhead.com/resource/essence-19).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_fire_volcano.gif)Volcanism](https://www.wowhead.com/spell=406904/volcanism): Reduces the [Essence](https://www.wowhead.com/resource/essence-19) cost for [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption).

- Choice node:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_shadow_lastingafflictions.gif)Perilous Fate](https://www.wowhead.com/spell=410253/perilous-fate): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) reduces enemy attack speed and movement speed for 10 seconds.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_bronze_01.gif)Chrono Ward](https://www.wowhead.com/spell=409676/chrono-ward): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) provides a modest absorption shield to allies who deal damage during its active window.


- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_bestowweyrnstone.gif)Bestow Weyrnstone](https://www.wowhead.com/spell=408233/bestow-weyrnstone): Conjure an on-use item for you and a friendly target, which can be activated to teleport to the other’s location anywhere within a large radius.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timelessness.gif)Timelessness](https://www.wowhead.com/spell=412710/timelessness): Reduces the threat generated by one ally for 30 mins.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Improved Defy Fate](https://www.wowhead.com/spell=1268881/improved-defy-fate): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_defyfate.gif)Defy Fate](https://www.wowhead.com/spell=404195/defy-fate) provides additional healing and has a reduced cooldown.


#### Row 6 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales): Provides a friendly target with passive armor, as well as charges of explosive scales that detonate upon receiving melee attacks, dealing damage in a small area.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_draconicattunements.gif)Draconic Attunements](https://www.wowhead.com/spell=403208/draconic-attunements): Choose one of two active auras applying to nearby allies, one increasing maximum Health, and the other providing bonus movement speed.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience): Temporarily grants an ally increased Critical Strike chance.


#### Row 7 Talents

- Choice node:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_shaman_stormearthfire.gif)Unyielding Domain](https://www.wowhead.com/spell=412733/unyielding-domain): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) cannot be interrupted and has an increased chance to critically strike.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/6bf_explosive_shard.gif)Tectonic Locus](https://www.wowhead.com/spell=408002/tectonic-locus): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) deals increased damage to the primary target and launches them higher in the air.


- Choice node:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_tradeskill_skinning_prismaticscale.gif)Regenerative Chitin](https://www.wowhead.com/spell=406907/regenerative-chitin): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) no longer loses charges and deals additional damage.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_shaman_spewlava.gif)Molten Blood](https://www.wowhead.com/spell=410643/molten-blood): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) provides the target with a modest absorption shield, which is more potent the lower the Health of the target.


- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_priest_voidshift.gif)Momentum Shift](https://www.wowhead.com/spell=408004/momentum-shift): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) temporarily grants you increased Intellect. This effect can stack up to 2 times.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_aspectsfavor.gif)Aspects' Favor](https://www.wowhead.com/spell=407243/aspects-favor): Casting [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_artifact_dragonscales.gif)Obsidian Scales](https://www.wowhead.com/spell=363916/obsidian-scales) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) temporarily enhances the effect of their respective, related [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_draconicattunements.gif)Draconic Attunements](https://www.wowhead.com/spell=403208/draconic-attunements).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/classicon_evoker.gif)Arcane Reach](https://www.wowhead.com/spell=454983/arcane-reach): Increased your range on spells targeting friendly players.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/trade_archaeology_highbornesoulmirror.gif)Fate Mirror](https://www.wowhead.com/spell=412774/fate-mirror): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) grants the target a chance to echo a portion of their damage dealt.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_10_herb_seed_magiccolor5.gif)Symbiotic Bloom](https://www.wowhead.com/spell=410685/symbiotic-bloom): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom) temporarily increases friendly targets’ healing received.


#### Row 8 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_reactivehide.gif)Reactive Hide](https://www.wowhead.com/spell=409329/reactive-hide): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) deals increasing damage on subsequent explosions, stacking up to 10 times.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_fontofmagic.gif)Font of Magic](https://www.wowhead.com/spell=408083/font-of-magic): Empower spells can be additionally Empowered and reach maximum Empower level faster.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_innatemagic2.gif)Hoarded Power](https://www.wowhead.com/spell=375796/hoarded-power): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) has a chance to not be consumed.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_motesofpossibility.gif)Motes of Possibility](https://www.wowhead.com/spell=409267/motes-of-possibility) ( **Motes**): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) has a chance to spawn a mote which grants a random Augmentation buff when walked through.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst6.gif)Anachronism](https://www.wowhead.com/spell=407869/anachronism): Casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) has a chance to grant [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst).

- Choice node:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_reversion_green.gif)Prolong Life](https://www.wowhead.com/spell=410687/prolong-life): Effects that extend [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) also extend [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_10_herb_seed_magiccolor5.gif)Symbiotic Bloom](https://www.wowhead.com/spell=410685/symbiotic-bloom).

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterylifebinder.gif)Dream of Spring](https://www.wowhead.com/spell=414969/dream-of-spring): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_emeraldblossom.gif)Emerald Blossom](https://www.wowhead.com/spell=355913/emerald-blossom) now costs [Essence](https://www.wowhead.com/resource/essence-19) but has no cooldown. It also heals for more and extends the duration of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might).


#### Row 9 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_accretion.gif)Accretion](https://www.wowhead.com/spell=407876/accretion): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) reduces the remaining cooldown of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_burningbladeshaman_blazing_radiance.gif)Imminent Destruction](https://www.wowhead.com/spell=459537/imminent-destruction): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=442204/breath-of-eons) reduces the cost and increases the damage of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) for a short duration.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip): Channel to reduce the remaining cooldown of all your spells.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterylifebinder_bronze.gif)Clairvoyant](https://www.wowhead.com/spell=1250914/clairvoyant): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_motesofpossibility.gif)Motes of Possibility](https://www.wowhead.com/spell=409267/motes-of-possibility) can now grant [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) and has a higher chance to activate.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_infernosblessing.gif)Inferno's Blessing](https://www.wowhead.com/spell=410261/infernos-blessing) ( **IB**): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) causes you and allies affected by [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) to deal additional damage with damaging attacks and spells.


#### Row 10 Talents

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_geomancy.gif)Rumbling Earth](https://www.wowhead.com/spell=459120/rumbling-earth): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) repeats a portion of its damage twice.

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_plotthefuture.gif)Plot the Future](https://www.wowhead.com/spell=407866/plot-the-future): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) grants you [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_furyoftheaspects.gif)Fury of the Aspects](https://www.wowhead.com/spell=390386/fury-of-the-aspects) for a short period without causing [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_nature_sleep.gif)Exhaustion](https://www.wowhead.com/spell=57723/exhaustion).

- Choice node:

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_rewind2.gif)Tomorrow, Today](https://www.wowhead.com/spell=412723/tomorrow-today): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip) channels for slightly longer.

  - [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_enchant_optionalreagent_01.gif)Interwoven Threads](https://www.wowhead.com/spell=412713/interwoven-threads): All your cooldowns are slightly reduced.


- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_overlord.gif)Overlord](https://www.wowhead.com/spell=410260/overlord): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) casts [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) at targets struck and spawn [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_motesofpossibility.gif)Motes of Possibility](https://www.wowhead.com/spell=409267/motes-of-possibility).

- [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_earthensky.gif)Molten Embers](https://www.wowhead.com/spell=459725/molten-embers) ( **ME**): [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) causes affected enemies to take increased damage from your Black spells.


* * *

## Feedback

Thanks for reading our class guides! If you have any feedback, feel free to leave a comment in the section below, and we will reply as quickly as possible. If you'd like to talk with any of our writers directly, you can do so by joining our [Discord server](http://discord.gg/wowhead) and finding them there!

![](https://wow.zamimg.com/uploads/author-pages/author/ea925294db5fb08bebba4c014a834604ad94e4ad.jpg)

## Jereico

### World of Warcraft Evoker Class Expert

[Twitch](https://www.twitch.tv/Jereico)[Discord](https://discord.gg/vXB3GJsbFw)[YouTube](https://www.youtube.com/@Jereico)[Bluesky](https://bsky.app/profile/jereico.bsky.social)[Author Page](https://www.wowhead.com/author/Jereico)

Jereico (he, him) has written Evoker class guides and editorial content for Wowhead since 2023. He has been an avid fan of MMOs for nearly 25 years, with countless hours dedicated across classic titles like Runescape, Puzzle Pirates, Maple Story, and Guild Wars before first discovering World of Warcraft in 2007.

If you want to get in touch with Jereico, you can find him in his Community Discord, on Twitter and Bluesky, posting videos to YouTube, and occasionally streaming on Twitch.

[Get WowheadPremium$2A MonthEnjoy an ad-free experience, unlock premium features, & support the site!](https://www.wowhead.com/premium)

Comments

Reset Sort« First‹ Previous**1** \- **0** of **0**Next ›Last »

[Add your comment](https://www.wowhead.com/account=signin) \|Sort: newest first, oldest first, highest rated\|Filter by patch:

**No comments have been posted yet.**

Please [log in](https://www.wowhead.com/account=signin) to add your comment, or [register](https://www.wowhead.com/auth/register) if you don't already have an account.

« First‹ Previous**1** \- **0** of **0**Next ›Last »

## Contribute

Add your comment

Please keep the following in mind when posting a comment:

- Your comment must be in English or it will be removed.

- Unsure how to post? Check out our [handy guide](https://www.wowhead.com/help=commenting-and-you)!

- You might want to proof-read your comments before posting them.

- Please post questions on our [forums](https://www.wowhead.com/forums) for quicker reply.


Post a Comment

You are not logged in. Please [log in](https://www.wowhead.com/account=signin) or [register an account](https://www.wowhead.com/auth/register) to add your comment.

Simply browse for your screenshot using the form below.

- Screenshots containing UI elements are generally declined on sight, the same goes for screenshots from the modelviewer or character selection screen.

- The higher the quality the better!

- Please review our [Screenshot Guidelines](https://www.wowhead.com/help=screenshot-guidelines) before submitting!


You are not logged in. Please [log in](https://www.wowhead.com/account=signin) to submit a screenshot.

Simply type the URL of the video in the form below.

URL: Supported: YouTube only

Title: Optional, up to 200 characters

Note: Your video will need to be approved before appearing on the site.

The **Wowhead Client** is a little application we use to keep our database up to date, and to provide you with some nifty extra functionality on the website!

It serves 2 main purposes:

1. It maintains a WoW addon called the **Wowhead Looter**, which collects data as you play the game!

2. It uploads the **collected data** to Wowhead in order to keep the database up-to-date!


You can also use it to keep track of your completed quests, recipes, mounts, companion pets, and titles!

So, what are you waiting for? [Download the client](https://www.wowhead.com/client) and get started.

Do you want to enable desktop notifications for WoW news?

AcceptDeclineMaybe Later

## Talent Tree — Class & Spec Tree Talents
- 358385 | Landslide | landslide
- 363916 | Obsidian Scales | obsidian-scales
- 365585 | Expunge | expunge
- 369913 | Natural Convergence | natural-convergence
- 368838 | Heavy Wingbeats | heavy-wingbeats
- 360995 | Verdant Embrace | verdant-embrace
- 375528 | Forger of Mountains | forger-of-mountains
- 375520 | Innate Magic | innate-magic
- 375406 | Obsidian Bulwark | obsidian-bulwark
- 375554 | Enkindled | enkindled
- 372469 | Scarlet Adaptation | scarlet-adaptation
- 386405 | Inner Radiance | inner-radiance
- 371806 | Recall | recall
- 375443 | Clobbering Sweep | clobbering-sweep
- 375556 | Tailwind | tailwind
- 374251 | Cauterizing Flame | cauterizing-flame
- 369990 | Ancient Flame | ancient-flame
- 376164 | Instinctive Arcana | instinctive-arcana
- 370553 | Tip the Scales | tip-the-scales
- 376930 | Attuned to the Dream | attuned-to-the-dream
- 360806 | Sleep Walk | sleep-walk
- 369909 | Protracted Talons | protracted-talons
- 375544 | Inherent Resistance | inherent-resistance
- 376166 | Draconic Legacy | draconic-legacy
- 375517 | Extended Flight | extended-flight
- 370886 | Bountiful Bloom | bountiful-bloom
- 387787 | Regenerative Magic | regenerative-magic
- 375510 | Blast Furnace | blast-furnace
- 375542 | Exuberance | exuberance
- 374348 | Renewing Blaze | renewing-blaze
- 387341 | Walloping Blow | walloping-blow
- 387761 | Panacea | panacea
- 410352 | Stretch Time | stretch-time
- 1264378 | Unravel | unravel
- 372048 | Oppressing Roar | oppressing-roar
- 375574 | Foci of Life | foci-of-life
- 370665 | Rescue | rescue
- 375561 | Lush Growth | lush-growth
- 369459 | Source of Magic | source-of-magic
- 1267206 | Strike from Above | strike-from-above
- 369939 | Leaping Flames | leaping-flames
- 374346 | Overawe | overawe
- 365933 | Aerial Mastery | aerial-mastery
- 370888 | Twin Guardian | twin-guardian
- 418101 | Potent Mana | potent-mana
- 371032 | Terror of the Skies | terror-of-the-skies
- 374227 | Zephyr | zephyr
- 395152 | Ebon Might | ebon-might
- 395160 | Eruption | eruption
- 396187 | Essence Burst | essence-burst
- 351338 | Quell | quell
- 406659 | Ricocheting Pyroclast | ricocheting-pyroclast
- 375722 | Essence Attunement | essence-attunement
- 396286 | Upheaval | upheaval
- 403631 | Breath of Eons | breath-of-eons
- 404195 | Defy Fate | defy-fate
- 408775 | Ignition Rush | ignition-rush
- 369908 | Power Nexus | power-nexus
- 406904 | Volcanism | volcanism
- 408233 | Bestow Weyrnstone | bestow-weyrnstone
- 412710 | Timelessness | timelessness
- 1268881 | Improved Defy Fate | improved-defy-fate
- 360827 | Blistering Scales | blistering-scales
- 403208 | Draconic Attunements | draconic-attunements
- 409311 | Prescience | prescience
- 408004 | Momentum Shift | momentum-shift
- 407243 | Aspects | aspects-favor
- 454983 | Arcane Reach | arcane-reach
- 412774 | Fate Mirror | fate-mirror
- 410685 | Symbiotic Bloom | symbiotic-bloom
- 409329 | Reactive Hide | reactive-hide
- 408083 | Font of Magic | font-of-magic
- 375796 | Hoarded Power | hoarded-power
- 409267 | Motes of Possibility | motes-of-possibility
- 407869 | Anachronism | anachronism
- 407876 | Accretion | accretion
- 459537 | Imminent Destruction | imminent-destruction
- 404977 | Time Skip | time-skip
- 1250914 | Clairvoyant | clairvoyant
- 410261 | Inferno | infernos-blessing
- 459120 | Rumbling Earth | rumbling-earth
- 407866 | Plot the Future | plot-the-future
- 410260 | Overlord | overlord
- 459725 | Molten Embers | molten-embers
- 1259173 | Duplicate | duplicate

## Hero Talent Trees
### Chronowarden
- 431442 | Chrono Flame | chrono-flame
- 429483 | Warp | warp
- 431695 | Temporal Burst | temporal-burst
- 1260484 | Chronoboon | chronoboon
- 431615 | Reverberations | reverberations
- 431715 | Nozdormu Adept | nozdormu-adept
- 1260568 | Energy Cycles | energy-cycles
- 431657 | Primacy | primacy
- 431484 | Instability Matrix | instability-matrix
- 1260647 | Overclock | overclock
- 432004 | Golden Opportunity | golden-opportunity
- 431875 | Afterimage | afterimage

### Scalecommander
- 438587 | Mass Eruption | mass-eruption
- 441705 | Might of the Black Dragonflight | might-of-the-black-dragonflight
- 434300 | Bombardments | bombardments
- 441245 | Onslaught | onslaught
- 1260745 | Command Squadron | command-squadron
- 441176 | Melt Armor | melt-armor
- 441206 | Wingleader | wingleader
- 441246 | Unrelenting Siege | unrelenting-siege
- 1261448 | Concentrated Power | concentrated-power
- 1261452 | Refined Essence | refined-essence
- 433871 | Maneuverability | maneuverability

## Rotation / Priority
Guide Contents

Patch 12.0.1

4.4/5

(8 Votes)

**~~~~**
**Midnight**

- [Cheat Sheet](https://www.wowhead.com/guide/classes/evoker/augmentation/cheat-sheet)

- [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

- [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps)

  - [How to Play Augmentation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#how-to-play-augmentation)
  - [Rotation Priority](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#rotation-priority)
  - [Major Cooldowns](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#major-cooldowns)
  - [Advanced Tips](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#advanced-tips)

- [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

- [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps)


**~~~~**
**Spec Basics**

- [Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps)

- [Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

- [Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps)

- [Stat Priority](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps)

- [UI & Macros](https://www.wowhead.com/guide/classes/evoker/augmentation/addons-macro-ui-imports)

- [Leveling](https://www.wowhead.com/guide/classes/evoker/augmentation/dps-leveling-tips)


**~~~~**
**Guide Info**

- [Changelog](https://www.wowhead.com/guide/changelog?id=20774)


# Augmentation Evoker Rotation Guide - Midnight

[By Jereico](https://www.wowhead.com/author/Jereico)
Updated:
2026/03/15

LiveJereico[Live on Twitch!](https://www.twitch.tv/jereico) Offline on TwitchFollow: Follow [Discord](https://discord.gg/vXB3GJsbFw) [Twitch](https://www.twitch.tv/jereico) [Twitter](https://twitter.com/coffeeandsteve) [YouTube](https://www.youtube.com/@Jereico)

Welcome to the Augmentation Evoker rotation guide for Midnight Season 1! This guide will teach you all about the optimal rotation for Augmentation Evoker across its various talent builds. It will cover both core ability cadence and cooldown usage in dungeons and raids for **Midnight Season 1**.

[Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps) [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear) [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps) [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps) [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps) [Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps) [![](https://wow.zamimg.com/images/wow/icons/large/inv_misc_groupneedmore.jpg)\\
Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

Show Table of Contents

## Augmentation Evoker Rotation in Midnight Season 1

At its most basic, the bread and butter of Augmentation gameplay is all about weaving together your key damaging abilities and group buffs in order to maximize the damage output of your group. Here are some of the big ideas to consider while playing Augmentation:

|     |     |
| --- | --- |
| |     |     |
| --- | --- |
| ~~~~ | **Keep your buffs up:** Augmentation's rotation is centered around maximizing uptime of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might). [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_sandsoftime.gif)Sands of Time](https://www.wowhead.com/spell=413525/sands-of-time) allows us to extend the duration of Ebon Might through our damaging rotation: casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at appropriate ranks on cooldown, spending resources on [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption), and filling downtime with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) (or [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike)). |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Always be casting:** Keeping high uptime on your rotational spells is key to maintaining a solid resource economy in both raids and Mythic+. Use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) effectively to cast spells on the move, and make sure to fill any "downtime" in your rotation with your filler spells, Living Flame and Azure Strike, in order to deal damage and generate [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst). |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Watch your Essence Burst:** Augmentation Evoker has a few different potential sources of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst), and the buff only stacks up to 2. Make sure to spend your Essence Burst when capped, ideally before casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) generators like [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) and Living Flame to avoid wasting resources. |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Mind your cooldowns:** It's often correct to send cooldowns as soon as they've come back up, but look for opportunities to align your major cooldowns like [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) with allies' cooldowns and big damage moments during an encounter. | |

[![](https://wow.zamimg.com/images/wow/icons/medium/classicon_evoker_augmentation.jpg)Augmentation Evoker Starter Guide](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

## ~~~~ Best Augmentation Evoker Rotation

At its core, Augmentation Evoker follows a simple spell priority aimed at maximizing uptime of buffs on allies. Augmentation spends its resources while buffs are active to extend buff duration, and spends its downtime replenishing resources before starting the cycle over again.

Below, we break down the main priority lists for Augmentation Evoker: Single-Target Rotation, AoE Rotation, and your opener sequence.

**Hero Talent Master Switches**

You can use the master switches below to flip the **_entire page's_** options to your selected choice.

![](https://wow.zamimg.com/images/wow/icons/medium/inv_ability_chronowardenevoker_chronoflame.jpg)Chronowarden

![](https://wow.zamimg.com/images/wow/icons/medium/ability_evoker_eruption.jpg)Scalecommander

Single-Target Priority

AoE Priority

Opener

Pre-Combat Checks

### Best Augmentation Evoker Single Target Rotation

Augmentation in Single Target plays around a spell priority list, while making sure to avoid spending resources outside of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) whenever possible, in order to maximize damage and uptime of buffs on allies.

With Chronowarden selected, the priority is as follows: With Scalecommander selected, the priority is as follows:

**Please select a Hero Talent option to generate a Single Target priority**

_The builds used below are covered in the [Talents page](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps). Anywhere you see the  icon, you can hover over it for additional notes._

### Priority

01. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on chosen DPS players. -

02. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) if a few seconds or less remain on the active buff duration.

03. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) (see section on cooldown usage for more details).

04. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) (see section on cooldown usage for more details).

05. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Max Rank. -

06. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) at Rank 1, unless increased radius is needed to hit relevant targets. -

07. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption). \-

08. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) as filler in nearly all situations.

09. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) as backup filler that can be cast while moving, or used to slow enemies.

10. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) on a Tank. -


_The builds used below are covered in the [Talents page](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps). Anywhere you see the  icon, you can hover over it for additional notes._

### Priority

01. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on chosen DPS players. -

02. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) if a few seconds or less remain on the active buff duration.

03. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) (see section on cooldown usage for more details).

04. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) (see section on cooldown usage for more details).

05. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Max Rank. -

06. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) at Rank 1, unless increased radius is needed to hit relevant targets. -

07. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption). \-

08. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) as filler in nearly all situations.

09. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) as backup filler that can be cast while moving, or used to slow enemies.

10. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) on a Tank. -


### Best Augmentation Evoker AoE Rotation

Augmentation essentially plays the same in AoE as it does in Single Target. Note that [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) can be cast at a higher rank to hit enemies in a wider area. When playing Scalecommander, do make sure to play around [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments) whenever possible; this is covered in the Advanced Tips section of this page.

With Chronowarden selected, the priority is as follows: With Scalecommander selected, the priority is as follows:

**Please select a Hero Talent option to generate a Single Target priority**

_The builds used below are covered in the [Talents page](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps). Anywhere you see the  icon, you can hover over it for additional notes._

### Priority

01. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on chosen DPS players. -

02. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) if a few seconds or less remain on the active buff duration.

03. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) (see section on cooldown usage for more details).

04. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) (see section on cooldown usage for more details).

05. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Max Rank. -

06. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) at Rank 1, unless increased radius is needed to hit relevant targets. -

07. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption). \-

08. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) as filler in nearly all situations.

09. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) as backup filler that can be cast while moving, or used to slow enemies.

10. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) on a Tank. -


_The builds used below are covered in the [Talents page](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps). Anywhere you see the  icon, you can hover over it for additional notes._

### Priority

01. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on chosen DPS players. -

02. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) if a few seconds or less remain on the active buff duration.

03. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) (see section on cooldown usage for more details).

04. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) (see section on cooldown usage for more details).

05. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Max Rank. -

06. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) at Rank 1, unless increased radius is needed to hit relevant targets. -

07. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption). \-

08. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) as filler in nearly all situations.

09. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike) as backup filler that can be cast while moving, or used to slow enemies.

10. Maintain [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) on a Tank. -


### Best Augmentation Evoker Opener

The recommended opener has changed slightly in Midnight: we now immediately cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) after the start of combat to begin buffing the whole raid as soon as possible, and then proceed to cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons). Other than this minor variation, the opener is highly intuitive, and follows the same goals as the core rotation. Be sure to avoid pairing [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath); if we have [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_earthensky.gif)Molten Embers](https://www.wowhead.com/spell=459725/molten-embers) talented, we want to maximize uptime of the [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) damage over time effect.

You can use the buttons below to display openers for both single-target and AoE, depending on your chosen **Hero Talent**.With Chronowarden selected, opener details are as follows:With Scalecommander selected, opener details are as follows:

**Please select a Hero Talent option to generate an Opener sequence**

_The builds used below are covered in the [Talents page](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps). Anywhere you see the  icon, you can hover over it for additional notes._

### Sample Timeline

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_tipthescales.jpg)](https://www.wowhead.com/spell=370553/tip-the-scales)

[![](https://wow.zamimg.com/images/wow/icons/large/inv_12_profession_alchemy_lightpotion_yellow.jpg)](https://www.wowhead.com/item=241308/lights-potential)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_blisteringscales.jpg)](https://www.wowhead.com/spell=360827/blistering-scales) Tank

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_livingflame.jpg)](https://www.wowhead.com/spell=361469/living-flame) Pull

[![](https://wow.zamimg.com/images/wow/icons/large/spell_sarkareth.jpg)](https://www.wowhead.com/spell=395152/ebon-might)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_prescience.jpg)](https://www.wowhead.com/spell=409311/prescience) DPS 1

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_prescience.jpg)](https://www.wowhead.com/spell=409311/prescience) DPS 2

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_breathofeons.jpg)](https://www.wowhead.com/spell=403631/breath-of-eons)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_firebreath.jpg)](https://www.wowhead.com/spell=357208/fire-breath)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_upheaval.jpg)](https://www.wowhead.com/spell=408092/upheaval)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_eruption.jpg)](https://www.wowhead.com/spell=395160/eruption)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_tipthescales.jpg)](https://www.wowhead.com/spell=370553/tip-the-scales)

[![](https://wow.zamimg.com/images/wow/icons/large/inv_12_profession_alchemy_lightpotion_yellow.jpg)](https://www.wowhead.com/item=241308/lights-potential)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_blisteringscales.jpg)](https://www.wowhead.com/spell=360827/blistering-scales) Tank

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_livingflame.jpg)](https://www.wowhead.com/spell=361469/living-flame) Pull

[![](https://wow.zamimg.com/images/wow/icons/large/spell_sarkareth.jpg)](https://www.wowhead.com/spell=395152/ebon-might)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_prescience.jpg)](https://www.wowhead.com/spell=409311/prescience) DPS 1

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_prescience.jpg)](https://www.wowhead.com/spell=409311/prescience) DPS 2

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_breathofeons.jpg)](https://www.wowhead.com/spell=403631/breath-of-eons)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_firebreath.jpg)](https://www.wowhead.com/spell=357208/fire-breath)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_upheaval.jpg)](https://www.wowhead.com/spell=408092/upheaval)

[![](https://wow.zamimg.com/images/wow/icons/large/ability_evoker_eruption.jpg)](https://www.wowhead.com/spell=395160/eruption)

### Opener Sequence

01. Pre-cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) on a Tank.

02. Pre-cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame).

03. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might). \-

04. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on Buff Target 1. Use this time to position for [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons).

05. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on Buff Target 2.

06. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons). Aim for a short, safe flight path. -

07. Use trinket and [![Light's Potential](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_lightpotion_yellow.gif)Light's Potential![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241308/lights-potential). \-

08. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) (off-GCD). -

09. [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Max Rank from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales).

10. [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) at Rank 1.

11. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) until dry on Essence, and fill with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) as needed.

12. Proceed onto the main rotation.


01. Pre-cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) on a Tank.

02. Pre-cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame).

03. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might). \-

04. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on Buff Target 1. Use this time to position for [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons).

05. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) on Buff Target 2.

06. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons). Aim for a short, safe flight path. -

07. Use trinket and [![Light's Potential](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_lightpotion_yellow.gif)Light's Potential![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241308/lights-potential). \-

08. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) (off-GCD).

09. [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Max Rank from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales).

10. [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) at Rank 1.

11. Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) until dry on Essence, and fill with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) as needed.

12. Proceed onto the main rotation.


## Pre-Combat Check

Before any combat happens, it is important for Augmentation Evoker to make sure the following are done. This applies to raids, dungeons, delves, or even open-world content.

- **Check Consumables -** Any or all of food, flask, weapon oil, augment rune, as needed.

- **Cast your Raid Buff -** Use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blessingofthebronze.gif)Blessing of the Bronze](https://www.wowhead.com/spell=364342/blessing-of-the-bronze) to buff you and your raid or party with cooldown reduction on major movement abilities. This buff lasts for an hour.

- **Apply Source of Magic -** Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blue_01.gif)Source of Magic](https://www.wowhead.com/spell=369459/source-of-magic) on your chosen healer. This buff lasts for an hour.

- **Apply Blistering Scales -** Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blisteringscales.gif)Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales) on your chosen target; this will usually be the tank in group content, or yourself in solo play. This buff lasts for an hour, or until removed.

- **(If talented) Draconic Attunements -** Check to make sure you have your preferred [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_draconicattunements.gif)Draconic Attunements](https://www.wowhead.com/spell=403208/draconic-attunements) active. [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_blackattunement.gif)Black Attunement](https://www.wowhead.com/spell=403264/black-attunement) is generally the default choice.

- **(If talented) Apply Timelessness -** Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timelessness.gif)Timelessness](https://www.wowhead.com/spell=412710/timelessness) on your chosen target; this will usually be a DPS player that generates high amounts of threat. This buff lasts for an hour.

- **(If talented) Cast Bestow Weyrnstone -** Cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_bestowweyrnstone.gif)Bestow Weyrnstone](https://www.wowhead.com/spell=408233/bestow-weyrnstone) on your chosen target. This generates an item in both players' inventories which can be activated in combat.


## ~~~~ Augmentation Evoker Major Cooldowns

Empower Spells

Tip The Scales

Ebon Might

Breath of Eons

Time Skip

### ~~~~ Empower Spells

The key to making the most of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) as an Augmentation Evoker is ideally to ensure that you **only cast these abilities while [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) is up** in order to extend the duration of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might), as well as direct [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Shifting Sands](https://www.wowhead.com/spell=413984/shifting-sands) towards nearby buffed allies.

Casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at higher Ranks increases its upfront damage while reducing the duration of its Damage over Time (DoT) effect. Additionally, the Evoker class talent [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_pupilofalexstraza.gif)Leaping Flames](https://www.wowhead.com/spell=369939/leaping-flames) benefits from casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at higher Ranks by increasing the number of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) projectiles. Each projectile deals full damage and has an individual chance chance to generate [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst). Even in single-target, this can cleave onto injured allies and have additional chances to grant [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) assuming there was effective healing.

The capstone talent, [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_earthensky.gif)Molten Embers](https://www.wowhead.com/spell=459725/molten-embers), encourages you to maximize uptime on the [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) DoT effect. With this talent selected, you will always want to cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Rank 1, and will want to ensure ensure that you cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) before [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) to maximize damage.

In summary, **with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_earthensky.gif)Molten Embers](https://www.wowhead.com/spell=459725/molten-embers) talented always cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Rank 1**, otherwise ranking up [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) is encouraged for the additional value from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_pupilofalexstraza.gif)Leaping Flames](https://www.wowhead.com/spell=369939/leaping-flames).

Empowering [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) simply expands the radius of the spell's area of effect, so **in single-target situations Rank 1 [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) is entirely sufficient**. In AoE situations, you will want to uprank [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) such that as many enemies as possible are within the area of effect.

### ~~~~ Tip The Scales

**With [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_earthensky.gif)Molten Embers](https://www.wowhead.com/spell=459725/molten-embers) talented, you will want to use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) on cooldown and just before casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) in your rotation.** This allows you to still cast one of your Empower spells instantly while ensuring that you continue to cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at Rank 1 at all times.

**If you do not have [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_earthensky.gif)Molten Embers](https://www.wowhead.com/spell=459725/molten-embers) talented, you can choose to pair [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) with either of your Empower spells**: [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) to deal damage more quickly and benefit from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_pupilofalexstraza.gif)Leaping Flames](https://www.wowhead.com/spell=369939/leaping-flames), or [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) if the additional radius is beneficial.

Remember that using [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) always saves a small amount of time over casting Empower spells normally, even at Rank 1. More importantly, it makes the Empower spell cast instantly, activating the spell sooner and allowing you to cast while moving.

### Chronowarden Tip The Scales

When playing Chronowarden, in addition to the above, be sure to treat [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst5.gif)Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst) from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) as a major DPS cooldown and aim to align it with your [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) and other major cooldowns for optimal results. [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Chronoboon](https://www.wowhead.com/spell=1260484/chronoboon) does reduce the cooldown of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales), but it is generally best to ignore this cooldown reduction and continue to pair [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons).

### ~~~~ Ebon Might

[![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) is Augmentation's main group buff on a baseline 30-second cooldown, which encourages you to **cast this ability as often as possible while aligning with the DPS cooldowns of other players**. When [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) is down, it is generally best to take the time to build resources and hold onto abilities which extend [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) until your next [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) window is active.

[![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) is beholden to the "pandemic" mechanic of duration extension, meaning that you can cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) while it's active and add the remaining duration onto the new spell cast, provided that this is less than 30% of the base duration of the buff. **It is ideal to re-cast [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) with no more than 3-4 seconds remaining** in order to minimize wasted uptime.

The amount of main stat granted by [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) currently updates dynamically to reflect changes in the caster's Intellect stat, but does not currently update to reflect player deaths or removed buffs.

### ~~~~ Breath of Eons

The ideal usage for any individual cast of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) involves aligning the 10-second Temporal Wounds window with the highest-burst windows of your buffed allies' DPS rotations. However, practically speaking, it is more likely that you will **aim to cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) roughly on cooldown** to maximize uses, assuming some non-zero amount of damage contribution from your buffed allies.

While raiding, make sure to be flexible with the exact timing of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons). Mythic Raid encounters, for example, often have very specific timings where players choose to use their DPS cooldowns, including damage amplifications, shield phases, add phases, and other mechanics. Being aware of these key timings can help maximize your buff output with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons).

### ~~~~ Time Skip

While [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_enchant_optionalreagent_01.gif)Interwoven Threads](https://www.wowhead.com/spell=412713/interwoven-threads) can be used in all PvE content, it comes at the cost of a capstone talent point. This means that Augmentation Evokers will occasionally find additional value taking other capstone talents and instead playing [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip).

[![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip) naturally encourages you to set up windows where multiple strong abilities are all on cooldown, at which point channeling [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip) results in tremendous value returned over a number of different spells.

It is currently recommended that you first use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip) **during your opener and following your first set of Empower spells [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval).** This timing maximizes your cooldown reduction, applies [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Shifting Sands](https://www.wowhead.com/spell=413984/shifting-sands) to two additional targets, and provides additional burst damage through your damaging spells. This timing also maximizes cooldown reduction value from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip) during your [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst5.gif)Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst) window when playing Chronowarden.

After your first cast, consider using [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip) essentially on cooldown, aligning with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst5.gif)Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst) whenever possible (as Chronowarden), and ideally when channeling [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_timeskip.gif)Time Skip](https://www.wowhead.com/spell=404977/time-skip) will reduce the cooldowns of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath), [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval), [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience), and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) by the full 20 seconds.

## ~~~~ Augmentation Evoker Advanced Tips

Bombardments

### Spreading Bombardments

When playing Scalecommander, your Empower spells each grant a buff causing your next cast of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) to be cast as [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Mass Eruption](https://www.wowhead.com/spell=438587/mass-eruption) and apply [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments) to the target. This buff stacks up to 2, allowing you to cast both Empower spells back-to-back. In situations with two or more high-health enemies, cast your second [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) on a second priority target in order to have [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments) rolling on both targets simultaneously. Any time [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_divideandconquer.gif)Extended Battle](https://www.wowhead.com/spell=441212/extended-battle) activates, it extends the duration of all active [![](https://wow.zamimg.com/images/wow/icons/tiny/inv_ability_scalecommanderevoker_bombardments.gif)Bombardments](https://www.wowhead.com/spell=434300/bombardments), meaning that you gain twice the value by doing this, increasing your damage done and further reducing the cooldown on [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_racial_soar.gif)Wingleader](https://www.wowhead.com/spell=441206/wingleader).

Our Augmentation Evoker guides are always updated with the latest information from in-game experience, simulations, and logs. Make sure to check our changelog for this page by clicking on **View Changelog** in the Quick Facts column or on the book icon at the top of the page. If you are interested in more in-depth Augmentation Evoker guides for **Midnight Season 1**, make sure to browse the _Navigation Bar_ at the top of the page, along with our list of **Related Guides** just beneath the _Table of Contents_.Prescience can be cast while targeting specific players, but will otherwise choose a target automatically if the player is targeting an enemy, preferring DPS players with active cooldowns. Avoid capping Prescience charges, and feel free to use Prescience outside of Ebon Might to generate resources, as Prescience itself does not extend Ebon Might.From a damage standpoint, Blistering Scales is generally not worth casting in place of damaging spells during combat. Unless your tank is in immediate danger from melee swings or similar effects, try to cast this spell before the start of a pull, between packs in dungeons, or otherwise during downtime. Recasting this spell is not needed if the Regenerative Chitin talent is selected.Cast Fire Breath at Max Rank whenever possible to benefit from Leaping Flames granting additional chance to activate Essence Burst. If you have Molten Embers talented, instead make sure to only cast Fire Breath at Rank 1, to maximize uptime of the DoT effect. You should generally avoid casting Fire Breath if Ebon Might is not active.You should generally avoid casting Upheaval if Ebon Might is not active.You should generally avoid casting Eruption if Ebon Might is not active. That said, if Essence Burst is about to expire, it can still be worthwhile to cast an Eruption in place of a filler spell to benefit from effects like Ignition Rush and Momentum Shift.Prescience and Ebon Might are removed upon pulling a Raid boss or starting a Mythic+ keystone. **Do not cast these abilities pre-pull.**.Always have a plan for casting Breath of Eons. You typically want to choose the shortest path possible that avoids dangerous mechanics, as well as choose an end location that sets you up for upcoming mechanics. Keep in mind that your flight only needs to make contact with the enemy hitbox; you don't always have to fly directly through the center of the target in order to hit, especially when it comes to large bosses!If you have Molten Embers talented, delay casting Tip The Scales until after casting Fire Breath.The best time to use your active trinket depends on the type of trinket you're using. Trinkets that instantly provide on-use stats are generally best used as soon as you land from Breath of Eons. Trinkets with a substantial cast time or mini-game are used before casting Breath of Eons in order to maximize damage output during the damage amplification window.

![](https://wow.zamimg.com/uploads/author-pages/author/ea925294db5fb08bebba4c014a834604ad94e4ad.jpg)

## Jereico

### World of Warcraft Evoker Class Expert

[Twitch](https://www.twitch.tv/Jereico)[Discord](https://discord.gg/vXB3GJsbFw)[YouTube](https://www.youtube.com/@Jereico)[Bluesky](https://bsky.app/profile/jereico.bsky.social)[Author Page](https://www.wowhead.com/author/Jereico)

Jereico (he, him) has written Evoker class guides and editorial content for Wowhead since 2023. He has been an avid fan of MMOs for nearly 25 years, with countless hours dedicated across classic titles like Runescape, Puzzle Pirates, Maple Story, and Guild Wars before first discovering World of Warcraft in 2007.

If you want to get in touch with Jereico, you can find him in his Community Discord, on Twitter and Bluesky, posting videos to YouTube, and occasionally streaming on Twitch.

[Get WowheadPremium$2A MonthEnjoy an ad-free experience, unlock premium features, & support the site!](https://www.wowhead.com/premium)

Comments (4)

Reset Sort« First‹ Previous**1** \- **4** of **4**Next ›Last »

[Add your comment](https://www.wowhead.com/account=signin) \|Sort: newest first, oldest first, highest rated\|Filter by patch: 11.0.511.0.210.1.5

|     |     |     |
| --- | --- | --- |
| 4<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [Fister](https://www.wowhead.com/user=Fister) (4,069 – **9**·14) [on 2023/07/11](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5644733) (Patch 10.1.5) |  |  |

I have a question regarding [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) use and what it actually affects. Does the ability only affect the buffed player's abilities and spells, or also their pet's abilities and spells?

You mention Unholy Death Knight as a very good target for Prescience on pull due to high burst of the spec, which revolves around Army and Gargoyle, but leave out Demo Lock which has a higher burst ceiling than any class in the game do to Pit Lord and Tyrant (and all the demons summoned from Nether Portal along with the normal demons being summoned: Dreadstalkers, Grimoire Felguard, Vilefiend, Imps (from Hand of Guldan), etc.) all active at the same time.

My question is, if Prescience's buff flows down to pets and allows for their damage to be affected by [![](https://wow.zamimg.com/images/wow/icons/tiny/trade_archaeology_highbornesoulmirror.gif)Fate Mirror](https://www.wowhead.com/spell=412774/fate-mirror) allowing spell/abilities to strike again for 15%, wouldn't that put Demo Lock at the top (or close to) priority on pull for [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience)?

Last edited by [Fister](https://www.wowhead.com/user=Fister) on 2023/07/11 (Patch 10.1.5)

|     |     |
| --- | --- |
| 5 | [Raliath](https://www.wowhead.com/user=Raliath) [on 2023/07/12](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5644733:reply=1627255) (Patch 10.1.5)<br>I believe it comes down to getting value out of Breath of Eons. It lasts 10 sec and is used on pull and stores damage dealt by players with Ebon Might (which will always prio target players with Prescience). Demo does indeed have the highest burst, but it takes too long to ramp. By the time Demo is doing damage (around 15+ sec into the fight) Breath of Eons has ended, so the damage multiplier is wasted on them as they do less damage than tanks until Nether Portal ends. | |

|     |     |     |
| --- | --- | --- |
| 2<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [Rick442](https://www.wowhead.com/user=Rick442) (3,088 – **7**·8) [on 2024/09/03](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5942063) (Patch 11.0.2) |  |  |

When will the Rotation page be updated for TWW ? with molten embers you dont use firebreath at max rank etc.

|     |     |
| --- | --- |
| 1 | [Jereico](https://www.wowhead.com/user=Jereico) <Guide Author> [on 2024/09/03](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5942063:reply=1711369) (Patch 11.0.2)<br>At the time of writing this comment the page is up to date with respect to the recommended Chronowarden builds. While [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_earthensky.gif)Molten Embers](https://www.wowhead.com/spell=459725/molten-embers) does encourage uptime on [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath), this is currently outweighed by the cast time saved from instant cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath). The sequence of casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) into [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) into [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) is set in stone for Chronowarden, and it turns out that you will generally spend most of your Essence during the Rank 3 [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath)’s duration regardless, so canceling the [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) buff is not necessary at this time. If you find yourself playing Scalecommander it would be more appropriate to use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_tipthescales.gif)Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales) with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) instead, however Scalecommander is not considered a competitive option at this time. |
| 1 | [Rick442](https://www.wowhead.com/user=Rick442) [on 2024/09/04](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5942063:reply=1712014) (Patch 11.0.2)<br>While i understand the reasoning, i still find it odd to not try to have 100% uptime on firebreath and therefore on molten embers. I currently use tip the scales with upheaval and firebreath at rank 1 to have 100% uptime on firebreath with Instability Matrix. Thank you for your answer | |

|     |     |     |
| --- | --- | --- |
| 1<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [Relm](https://www.wowhead.com/user=Relm) (5,915 – _1_· **8**·15) [on 2024/08/26](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5930705) (Patch 11.0.2) |  |  |

WIth Mass eruption. wouldn't it be best to cast Fire breath, Eruption, Upheval, Eruption?

|     |     |
| --- | --- |
| 1 | [Jereico](https://www.wowhead.com/user=Jereico) <Guide Author> [on 2024/08/26](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5930705:reply=1706424) (Patch 11.0.2)<br>[![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Mass Eruption](https://www.wowhead.com/spell=438587/mass-eruption) actually stacks up to 2, so you don't really lose any value sequencing it this way. We generally prefer to cast [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=396286/upheaval) first in order to quickly get the second [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Shifting Sands](https://www.wowhead.com/spell=413984/shifting-sands) buff onto an ally during cooldowns, as well as maximize value from [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_accretion.gif)Accretion](https://www.wowhead.com/spell=407876/accretion). | |

|     |     |     |
| --- | --- | --- |
| 1<br>STICKY | |     |     |     |
| --- | --- | --- |
| By [frozenembers](https://www.wowhead.com/user=frozenembers) (9,527 – _2_· **25**·44) [on 2024/10/22](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5986890) (Patch 11.0.5) |  |  |

Why are we not also pre-casting tip the scales?

|     |     |
| --- | --- |
| 1 | [Jereico](https://www.wowhead.com/user=Jereico) <Guide Author> [on 2024/10/22](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps#comments:id=5986890:reply=1726039) (Patch 11.0.5)<br>If you're playing Scalecommander, you certainly can if you like--it's off the global cooldown so it can be cast without interrupting your rotation. When playing Chronowarden it is important to cast it at the appropriate time to make best use of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst5.gif)Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst). | |

« First‹ Previous**1** \- **4** of **4**Next ›Last »

## Contribute

Add your comment

Please keep the following in mind when posting a comment:

- Your comment must be in English or it will be removed.

- Unsure how to post? Check out our [handy guide](https://www.wowhead.com/help=commenting-and-you)!

- You might want to proof-read your comments before posting them.

- Please post questions on our [forums](https://www.wowhead.com/forums) for quicker reply.


Post a Comment

You are not logged in. Please [log in](https://www.wowhead.com/account=signin) or [register an account](https://www.wowhead.com/auth/register) to add your comment.

Simply browse for your screenshot using the form below.

- Screenshots containing UI elements are generally declined on sight, the same goes for screenshots from the modelviewer or character selection screen.

- The higher the quality the better!

- Please review our [Screenshot Guidelines](https://www.wowhead.com/help=screenshot-guidelines) before submitting!


You are not logged in. Please [log in](https://www.wowhead.com/account=signin) to submit a screenshot.

Simply type the URL of the video in the form below.

URL: Supported: YouTube only

Title: Optional, up to 200 characters

Note: Your video will need to be approved before appearing on the site.

The **Wowhead Client** is a little application we use to keep our database up to date, and to provide you with some nifty extra functionality on the website!

It serves 2 main purposes:

1. It maintains a WoW addon called the **Wowhead Looter**, which collects data as you play the game!

2. It uploads the **collected data** to Wowhead in order to keep the database up-to-date!


You can also use it to keep track of your completed quests, recipes, mounts, companion pets, and titles!

So, what are you waiting for? [Download the client](https://www.wowhead.com/client) and get started.

Do you want to enable desktop notifications for WoW news?

AcceptDeclineMaybe Later

## Tier Set Bonuses (MID1)
Information about MID1 tier set bonuses not available in current guide pages. Check Wowhead's gear/tier set pages for the latest information.

## Enchants, Gems, Consumables
Guide Contents

Patch 12.0.1

**~~~~**
**Midnight**

- [Cheat Sheet](https://www.wowhead.com/guide/classes/evoker/augmentation/cheat-sheet)

- [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

- [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps)

- [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

- [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps)

  - [Gems & Enchants](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#gems-enchants)

    - [Gems](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#gems)
    - [Weapon](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#weapon)

  - [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#consumables)

    - [Flasks](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#flasks)
    - [Combat Potion](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#combat-potion)
    - [Health Potion](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#health-potion)
    - [Weapon Buff](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#weapon-buff)
    - [Augment Rune](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#augment-rune)
    - [Food](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps#food)

**~~~~**
**Spec Basics**

- [Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps)

- [Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

- [Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps)

- [Stat Priority](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps)

- [UI & Macros](https://www.wowhead.com/guide/classes/evoker/augmentation/addons-macro-ui-imports)

- [Leveling](https://www.wowhead.com/guide/classes/evoker/augmentation/dps-leveling-tips)


**~~~~**
**Guide Info**

- [Changelog](https://www.wowhead.com/guide/changelog?id=20759)


# Augmentation Evoker Enchants & Consumables - Midnight

[By Jereico](https://www.wowhead.com/author/Jereico)
Updated:
2026/03/14

LiveJereico[Live on Twitch!](https://www.twitch.tv/jereico) Offline on TwitchFollow: Follow [Discord](https://discord.gg/vXB3GJsbFw) [Twitch](https://www.twitch.tv/jereico) [Twitter](https://twitter.com/coffeeandsteve) [YouTube](https://www.youtube.com/@Jereico)

Consumables are an important aspect of high-level content in WoW, such as raids and Mythic+ dungeons. They provide additional ways for players to improve and customize their stats outside of gear.

In this guide, we will explain the best gems, flasks, potions, and enchants to use for Augmentation Evoker in **Midnight Season 1**, as well as cheaper alternatives. Make sure to also check our [Midnight Profession Guide](https://www.wowhead.com/guide/professions/overview) for all profession details.

[Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps) [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear) [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps) [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps) [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps) [Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps) [![](https://wow.zamimg.com/images/wow/icons/large/inv_misc_groupneedmore.jpg)\\
Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

Show Table of Contents

## ~~~~ Best Augmentation Evoker Gems and Enchants in Midnight Season 1

Below is a list of the recommended gems and enchants to use on your gear during Midnight Season 1.

|     |     |
| --- | --- |
| **Slot** | **Best** |
| Weapon | [![Enchant Weapon - Acuity of the Ren'dorei](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_enchantedvellum_purple.gif)Enchant Weapon - Acuity of the Ren'dorei![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=244029/enchant-weapon-acuity-of-the-rendorei) |
| Helm | [![Enchant Helm - Empowered Rune of Avoidance](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_enchantedvellum_blue.gif)Enchant Helm - Empowered Rune of Avoidance![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=244007/enchant-helm-empowered-rune-of-avoidance) |
| Shoulders | [![Enchant Shoulders - Amirdrassil's Grace](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_enchantedvellum_blue.gif)Enchant Shoulders - Amirdrassil's Grace![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=243991/enchant-shoulders-amirdrassils-grace) |
| Chest | [![Enchant Chest - Mark of the Worldsoul](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_enchantedvellum_blue.gif)Enchant Chest - Mark of the Worldsoul![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=243977/enchant-chest-mark-of-the-worldsoul) |
| Legs | [![Sunfire Silk Spellthread](https://wow.zamimg.com/images/wow/icons/tiny/inv_tailoring_spellthread_orange_spellthread.gif)Sunfire Silk Spellthread![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=240133/sunfire-silk-spellthread) |
| Boots | [![Enchant Boots - Lynx's Dexterity](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_enchantedvellum_blue.gif)Enchant Boots - Lynx's Dexterity![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=243953/enchant-boots-lynxs-dexterity) |
| Ring | [![Enchant Ring - Nature's Fury](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_enchantedvellum_blue.gif)Enchant Ring - Nature's Fury![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=243987/enchant-ring-natures-fury) |
| Eversong Diamond | [![Indecipherable Eversong Diamond](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_jewelcrafting_epic_gem_cut_green.gif)Indecipherable Eversong Diamond![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=240983/indecipherable-eversong-diamond) |
| Other Gems | [![Flawless Quick Garnet](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_jewelcrafting_rare_gem_cut_nature_red.gif)Flawless Quick Garnet![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=240906/flawless-quick-garnet) |

### Augmentation Evoker Gems

For your Eversong Diamond, [![Indecipherable Eversong Diamond](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_jewelcrafting_epic_gem_cut_green.gif)Indecipherable Eversong Diamond![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=240983/indecipherable-eversong-diamond) is the best overall option for Augmentation Evoker.

As for your other gems, [![Flawless Quick Garnet](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_jewelcrafting_rare_gem_cut_nature_red.gif)Flawless Quick Garnet![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=240906/flawless-quick-garnet) offers stats best aligned with Augmentation's stat priority, but you may consider alternative gem combinations as needed to best round out your stats.

### Augmentation Evoker Weapon Enchant

[![Enchant Weapon - Acuity of the Ren'dorei](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_enchantedvellum_purple.gif)Enchant Weapon - Acuity of the Ren'dorei![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=244029/enchant-weapon-acuity-of-the-rendorei) is the best overall choice of weapon enchant in PVE content for Augmentation Evoker.

## ~~~~ Best Augmentation Evoker Consumables in Midnight Season 1

Below, we've listed the best flasks, potions, and weapon buffs that Augmentation Evoker can use in PvE content. While Haste is generally recommended as the safest option for gearing characters and for the added benefit of smoothing out gameplay feel, you should ideally be simming your character using [raidbots](https://www.raidbots.com/simbot) to determine the best configuration for you.

|     |     |
| --- | --- |
| Flask | [![Flask of the Shattered Sun](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_flask_sindoreipotion_red--.gif)Flask of the Shattered Sun![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241326/flask-of-the-shattered-sun) |
| Combat Potion | [![Light's Potential](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_lightpotion_yellow.gif)Light's Potential![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241308/lights-potential) |
| Health Potion | [![Silvermoon Health Potion](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_lightpotion_orange.gif)Silvermoon Health Potion![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241304/silvermoon-health-potion) |
| Weapon Buff | [![Thalassian Phoenix Oil](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_manaoil_red.gif)Thalassian Phoenix Oil![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=243734/thalassian-phoenix-oil) |
| Augment Rune | [![Void-Touched Augment Rune](https://wow.zamimg.com/images/wow/icons/tiny/inv_10_enchanting_crystal_color2.gif)Void-Touched Augment Rune](https://www.wowhead.com/item=259085/void-touched-augment-rune) |
| Food | [![Hearty Silvermoon Parade](https://wow.zamimg.com/images/wow/icons/tiny/inv_tradeskill_cooking_feastofblood.gif)Hearty Silvermoon Parade](https://www.wowhead.com/item=266985/hearty-silvermoon-parade) |

### Augmentation Evoker Flask

The best Flask for Augmentation Evokers is [![Flask of the Shattered Sun](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_flask_sindoreipotion_red--.gif)Flask of the Shattered Sun![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241326/flask-of-the-shattered-sun).

### Augmentation Evoker Combat Potions

The best combat potion for Augmentation Evokers in all content is [![Light's Potential](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_lightpotion_yellow.gif)Light's Potential![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241308/lights-potential).

### Augmentation Evoker Health Potions

The best healing potion for Augmentation Evokers is [![Silvermoon Health Potion](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_alchemy_lightpotion_orange.gif)Silvermoon Health Potion![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=241304/silvermoon-health-potion).

### Augmentation Evoker Weapon Buff

For their weapons, Augmentation Evokers will always use [![Thalassian Phoenix Oil](https://wow.zamimg.com/images/wow/icons/tiny/inv_12_profession_enchanting_manaoil_red.gif)Thalassian Phoenix Oil![](https://wow.zamimg.com/images/wow/TextureAtlas/live/professions-chaticon-quality-tier2.png)](https://www.wowhead.com/item=243734/thalassian-phoenix-oil).

### Augmentation Evoker Augment Rune

The augment rune available for Augmentation Evoker is [![Void-Touched Augment Rune](https://wow.zamimg.com/images/wow/icons/tiny/inv_10_enchanting_crystal_color2.gif)Void-Touched Augment Rune](https://www.wowhead.com/item=259085/void-touched-augment-rune).

### Augmentation Evoker Food

Augmentation Evokers will likely prefer to use feasts which provide Intellect over other alternative food options. Personal food can be used instead of a feast, but this comes at the cost of bonus Stamina.

- Feast: [![Hearty Silvermoon Parade](https://wow.zamimg.com/images/wow/icons/tiny/inv_tradeskill_cooking_feastofblood.gif)Hearty Silvermoon Parade](https://www.wowhead.com/item=266985/hearty-silvermoon-parade)

- Personal Food: [![Hearty Royal Roast](https://wow.zamimg.com/images/wow/icons/tiny/inv_cooking_100_roastduck.gif)Hearty Royal Roast](https://www.wowhead.com/item=242747/hearty-royal-roast)


* * *

Our Augmentation Evoker guides are always updated with the latest information from in-game experience, simulations, and logs. Make sure to check our changelog for this page by clicking on **View Changelog** in the Quick Facts column or on the book icon at the top of the page. If you are interested in more in-depth Augmentation Evoker guides for **Midnight Season 1**, make sure to browse the _Navigation Bar_ at the top of the page.

* * *

## Feedback

Thanks for reading our class guides! If you have any feedback, feel free to leave a comment in the section below, and we will reply as quickly as possible. If you'd like to talk with any of our writers directly, you can do so by joining our [Discord server](http://discord.gg/wowhead) and finding them there!

![](https://wow.zamimg.com/uploads/author-pages/author/ea925294db5fb08bebba4c014a834604ad94e4ad.jpg)

## Jereico

### World of Warcraft Evoker Class Expert

[Twitch](https://www.twitch.tv/Jereico)[Discord](https://discord.gg/vXB3GJsbFw)[YouTube](https://www.youtube.com/@Jereico)[Bluesky](https://bsky.app/profile/jereico.bsky.social)[Author Page](https://www.wowhead.com/author/Jereico)

Jereico (he, him) has written Evoker class guides and editorial content for Wowhead since 2023. He has been an avid fan of MMOs for nearly 25 years, with countless hours dedicated across classic titles like Runescape, Puzzle Pirates, Maple Story, and Guild Wars before first discovering World of Warcraft in 2007.

If you want to get in touch with Jereico, you can find him in his Community Discord, on Twitter and Bluesky, posting videos to YouTube, and occasionally streaming on Twitch.

[Get WowheadPremium$2A MonthEnjoy an ad-free experience, unlock premium features, & support the site!](https://www.wowhead.com/premium)

Comments

Reset Sort« First‹ Previous**1** \- **0** of **0**Next ›Last »

[Add your comment](https://www.wowhead.com/account=signin) \|Sort: newest first, oldest first, highest rated\|Filter by patch:

**No comments have been posted yet.**

Please [log in](https://www.wowhead.com/account=signin) to add your comment, or [register](https://www.wowhead.com/auth/register) if you don't already have an account.

« First‹ Previous**1** \- **0** of **0**Next ›Last »

## Contribute

Add your comment

Please keep the following in mind when posting a comment:

- Your comment must be in English or it will be removed.

- Unsure how to post? Check out our [handy guide](https://www.wowhead.com/help=commenting-and-you)!

- You might want to proof-read your comments before posting them.

- Please post questions on our [forums](https://www.wowhead.com/forums) for quicker reply.


Post a Comment

You are not logged in. Please [log in](https://www.wowhead.com/account=signin) or [register an account](https://www.wowhead.com/auth/register) to add your comment.

Simply browse for your screenshot using the form below.

- Screenshots containing UI elements are generally declined on sight, the same goes for screenshots from the modelviewer or character selection screen.

- The higher the quality the better!

- Please review our [Screenshot Guidelines](https://www.wowhead.com/help=screenshot-guidelines) before submitting!


You are not logged in. Please [log in](https://www.wowhead.com/account=signin) to submit a screenshot.

Simply type the URL of the video in the form below.

URL: Supported: YouTube only

Title: Optional, up to 200 characters

Note: Your video will need to be approved before appearing on the site.

The **Wowhead Client** is a little application we use to keep our database up to date, and to provide you with some nifty extra functionality on the website!

It serves 2 main purposes:

1. It maintains a WoW addon called the **Wowhead Looter**, which collects data as you play the game!

2. It uploads the **collected data** to Wowhead in order to keep the database up-to-date!


You can also use it to keep track of your completed quests, recipes, mounts, companion pets, and titles!

So, what are you waiting for? [Download the client](https://www.wowhead.com/client) and get started.

Do you want to enable desktop notifications for WoW news?

AcceptDeclineMaybe Later

## SimC Implementation Notes
See abilities-talents guide section above for detailed mechanical interactions.
Key notes from basics guide:
Guide Contents

Patch 12.0.1

**~~~~**
**Midnight**

- [Cheat Sheet](https://www.wowhead.com/guide/classes/evoker/augmentation/cheat-sheet)

- [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

- [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps)

- [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear)

- [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps)


**~~~~**
**Spec Basics**

- [Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps)

- [Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

  - [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/basics#talent-builds)
  - [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/basics#rotation)

    - [One Button Assistant](https://www.wowhead.com/guide/classes/evoker/augmentation/basics#one-button-assistant)

  - [Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/basics#stats)

- [Abilities](https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps)

- [Stat Priority](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps)

- [UI & Macros](https://www.wowhead.com/guide/classes/evoker/augmentation/addons-macro-ui-imports)

- [Leveling](https://www.wowhead.com/guide/classes/evoker/augmentation/dps-leveling-tips)


**~~~~**
**Guide Info**

- [Changelog](https://www.wowhead.com/guide/changelog?id=32505)


# Augmentation Evoker DPS Basics - Starter Guide for Midnight

[By Jereico](https://www.wowhead.com/author/Jereico)
Updated:
2026/02/24

LiveJereico[Live on Twitch!](https://www.twitch.tv/jereico) Offline on TwitchFollow: Follow [Discord](https://discord.gg/vXB3GJsbFw) [Twitch](https://www.twitch.tv/jereico) [Twitter](https://twitter.com/coffeeandsteve) [YouTube](https://www.youtube.com/@Jereico)

Welcome to our Augmentation Evoker starter guide, which covers everything you need to start playing a new character in Midnight. While our other guide pages go into more detail about individual aspects of Augmentation Evoker gameplay, this simple starter guide covers all the basics in one place.

Visit the complete Augmentation Evoker guide pages linked in the navigation on the left-hand side of the page for more in-depth information!

[Overview](https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps) [BiS Gear](https://www.wowhead.com/guide/classes/evoker/augmentation/bis-gear) [Rotation](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps) [Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps) [Consumables](https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps) [Stats](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps) [![](https://wow.zamimg.com/images/wow/icons/large/inv_misc_groupneedmore.jpg)\\
Basics](https://www.wowhead.com/guide/classes/evoker/augmentation/basics)

Show Table of Contents

## ~~~~ Talent Build for Augmentation Evoker Beginners

The build recommended in this section is a standard recommended build for Scalecommander Augmentation Evoker. This setup is flexible enough to perform well at all level of skill, and will allow you to begin making use of strong utility options while you pick up the fundamentals.

If you're looking for more in-depth builds or explanations regarding talents choices, check out our Talent Builds guide:

[![](https://wow.zamimg.com/images/wow/icons/medium/classicon_evoker_augmentation.jpg)Augmentation Evoker Talent Builds](https://www.wowhead.com/guide/classes/evoker/augmentation/talent-builds-pve-dps)

Scalecommander

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Evoker

Spent: 34 / 34Req Level: 88

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/chronowarden/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBUVFUNCEQFFVVVUBA)

[Landslide](https://www.wowhead.com/spell=358385/landslide)

[Obsidian Scales](https://www.wowhead.com/spell=363916/obsidian-scales?spellModifier=375406:412713)

[Expunge](https://www.wowhead.com/spell=365585/expunge)

1/1

[Natural Convergence](https://www.wowhead.com/spell=369913/natural-convergence?spellModifier=396186)

1/1

[Heavy Wingbeats](https://www.wowhead.com/spell=368838/heavy-wingbeats)

1/1

[Verdant Embrace](https://www.wowhead.com/spell=360995/verdant-embrace)

1/1

[Forger of Mountains](https://www.wowhead.com/spell=375528/forger-of-mountains)

0/1

[Innate Magic](https://www.wowhead.com/spell=375520/innate-magic?def=120623&rank=1)

1/2

[Obsidian Bulwark](https://www.wowhead.com/spell=375406/obsidian-bulwark)

1/1

[Enkindled](https://www.wowhead.com/spell=375554/enkindled?def=120615&rank=2)

2/2

[Scarlet Adaptation](https://www.wowhead.com/spell=372469/scarlet-adaptation)

1/1

[Inner Radiance](https://www.wowhead.com/spell=386405/inner-radiance)

1/1

[Recall](https://www.wowhead.com/spell=371806/recall?spellModifier=403631)

0/1

[Clobbering Sweep](https://www.wowhead.com/spell=375443/clobbering-sweep)

1/1

[Tailwind](https://www.wowhead.com/spell=375556/tailwind)

0/1

[Cauterizing Flame](https://www.wowhead.com/spell=374251/cauterizing-flame)

1/1

[Ancient Flame](https://www.wowhead.com/spell=369990/ancient-flame)

0/1

[Instinctive Arcana](https://www.wowhead.com/spell=376164/instinctive-arcana?def=120631&rank=2)

2/2

[Tip the Scales](https://www.wowhead.com/spell=370553/tip-the-scales?spellModifier=1260484)

1/1

[Attuned to the Dream](https://www.wowhead.com/spell=376930/attuned-to-the-dream?def=120612&rank=1&spellModifier=396186)

0/2

[Sleep Walk](https://www.wowhead.com/spell=360806/sleep-walk)

0/1

[Protracted Talons](https://www.wowhead.com/spell=369909/protracted-talons)

0/1

[Inherent Resistance](https://www.wowhead.com/spell=375544/inherent-resistance?def=120682&rank=2&spellModifier=396186)

2/2

[Draconic Legacy](https://www.wowhead.com/spell=376166/draconic-legacy)

1/1

[Extended Flight](https://www.wowhead.com/spell=375517/extended-flight?def=120676&rank=2)

2/2

[Bountiful Bloom](https://www.wowhead.com/spell=370886/bountiful-bloom)

0/1

[Regenerative Magic](https://www.wowhead.com/spell=387787/regenerative-magic)

0/1

[Blast Furnace](https://www.wowhead.com/spell=375510/blast-furnace)

1/1

[Exuberance](https://www.wowhead.com/spell=375542/exuberance)

0/1

[Renewing Blaze](https://www.wowhead.com/spell=374348/renewing-blaze?spellModifier=375574)

1/1

[Walloping Blow](https://www.wowhead.com/spell=387341/walloping-blow)

0/1

[Panacea](https://www.wowhead.com/spell=387761/panacea)

1/1

[Stretch Time](https://www.wowhead.com/spell=410352/stretch-time)

1/1

[Unravel](https://www.wowhead.com/spell=1264378/unravel)

0/1

[Oppressing Roar](https://www.wowhead.com/spell=372048/oppressing-roar)

0/1

[Foci of Life](https://www.wowhead.com/spell=375574/foci-of-life)

1/1

[Rescue](https://www.wowhead.com/spell=370665/rescue)

1/1

[Lush Growth](https://www.wowhead.com/spell=375561/lush-growth?def=120674&rank=1)

0/2

[Source of Magic](https://www.wowhead.com/spell=369459/source-of-magic)

1/1

[Strike from Above](https://www.wowhead.com/spell=1267206/strike-from-above)

0/1

[Leaping Flames](https://www.wowhead.com/spell=369939/leaping-flames)

1/1

[Overawe](https://www.wowhead.com/spell=374346/overawe)

0/1

[Aerial Mastery](https://www.wowhead.com/spell=365933/aerial-mastery)

1/1

[Twin Guardian](https://www.wowhead.com/spell=370888/twin-guardian)

1/1

[Potent Mana](https://www.wowhead.com/spell=418101/potent-mana)

1/1

[Terror of the Skies](https://www.wowhead.com/spell=371032/terror-of-the-skies)

1/1

[Spatial Paradox / Time Spiral](https://www.wowhead.com/spell=406732/spatial-paradox)

1/1

[Zephyr](https://www.wowhead.com/spell=374227/zephyr)

1/1

Spent: 34 / 34Req Level: 88

![](https://wow.zamimg.com/images/wow/icons/medium/classicon_evoker_augmentation.jpg)

Augmentation

Spent: 34 / 34Req Level: 90

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/chronowarden/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBUVFUNCEQFFVVVUBA)

[Ebon Might](https://www.wowhead.com/spell=395152/ebon-might)

1/1

[Eruption](https://www.wowhead.com/spell=395160/eruption)

1/1

[Essence Burst](https://www.wowhead.com/spell=396187/essence-burst)

1/1

[Quell](https://www.wowhead.com/spell=351338/quell)

1/1

[Ricocheting Pyroclast](https://www.wowhead.com/spell=406659/ricocheting-pyroclast)

1/1

[Essence Attunement](https://www.wowhead.com/spell=375722/essence-attunement)

1/1

[Pupil of Alexstrasza / Echoing Strike](https://www.wowhead.com/spell=407814/pupil-of-alexstrasza)

1/1

[Upheaval](https://www.wowhead.com/spell=396286/upheaval)

1/1

[Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons)

1/1

[Defy Fate](https://www.wowhead.com/spell=404195/defy-fate)

1/1

[Ignition Rush](https://www.wowhead.com/spell=408775/ignition-rush)

1/1

[Power Nexus](https://www.wowhead.com/spell=369908/power-nexus)

1/1

[Volcanism](https://www.wowhead.com/spell=406904/volcanism)

1/1

Perilous Fate / Chrono Ward

0/1

[Bestow Weyrnstone](https://www.wowhead.com/spell=408233/bestow-weyrnstone)

0/1

[Timelessness](https://www.wowhead.com/spell=412710/timelessness)

0/1

[Improved Defy Fate](https://www.wowhead.com/spell=1268881/improved-defy-fate)

1/1

[Blistering Scales](https://www.wowhead.com/spell=360827/blistering-scales)

1/1

[Draconic Attunements](https://www.wowhead.com/spell=403208/draconic-attunements)

0/1

[Prescience](https://www.wowhead.com/spell=409311/prescience?spellModifier=412713:431715)

1/1

[Unyielding Domain / Tectonic Locus](https://www.wowhead.com/spell=408002/tectonic-locus)

1/1

[Regenerative Chitin / Molten Blood](https://www.wowhead.com/spell=406907/regenerative-chitin)

1/1

[Momentum Shift](https://www.wowhead.com/spell=408004/momentum-shift)

1/1

[Aspects' Favor](https://www.wowhead.com/spell=407243/aspects-favor?def=120529&rank=1)

0/2

[Arcane Reach](https://www.wowhead.com/spell=454983/arcane-reach)

0/1

[Fate Mirror](https://www.wowhead.com/spell=412774/fate-mirror)

1/1

[Symbiotic Bloom](https://www.wowhead.com/spell=410685/symbiotic-bloom?def=120527&rank=1)

0/2

[Reactive Hide](https://www.wowhead.com/spell=409329/reactive-hide)

0/1

[Font of Magic](https://www.wowhead.com/spell=408083/font-of-magic)

0/1

[Hoarded Power](https://www.wowhead.com/spell=375796/hoarded-power)

1/1

[Motes of Possibility](https://www.wowhead.com/spell=409267/motes-of-possibility)

1/1

[Anachronism](https://www.wowhead.com/spell=407869/anachronism)

1/1

Prolong Life / Dream of Spring

0/1

[Accretion](https://www.wowhead.com/spell=407876/accretion)

1/1

[Imminent Destruction](https://www.wowhead.com/spell=459537/imminent-destruction)

1/1

[Time Skip](https://www.wowhead.com/spell=404977/time-skip)

1/1

[Clairvoyant](https://www.wowhead.com/spell=1250914/clairvoyant)

0/1

[Inferno's Blessing](https://www.wowhead.com/spell=410261/infernos-blessing)

1/1

[Rumbling Earth](https://www.wowhead.com/spell=459120/rumbling-earth)

1/1

[Plot the Future](https://www.wowhead.com/spell=407866/plot-the-future)

1/1

[Tomorrow, Today / Interwoven Threads](https://www.wowhead.com/spell=412713/interwoven-threads)

1/1

[Overlord](https://www.wowhead.com/spell=410260/overlord)

0/1

[Molten Embers](https://www.wowhead.com/spell=459725/molten-embers)

0/1

[Duplicate / Duplicate / Duplicate](https://www.wowhead.com/spell=1259175/duplicate)

4/4

Spent: 34 / 34Req Level: 90

![](https://wow.zamimg.com/images/wow/icons/medium/class_evoker.jpg)

Chronowarden

Spent: 13 / 13Req Level: 89

Export Talents [Open in Calculator](https://www.wowhead.com/talent-calc/evoker/augmentation/chronowarden/EAQBVFlESQJgRFBREVVBAPVVVVQFFUEBUVFUNCEQFFVVVUBA)

[Chrono Flame](https://www.wowhead.com/spell=431442/chrono-flame?spellModifier=396186:1260647)

[Warp](https://www.wowhead.com/spell=429483/warp)

1/1

[Temporal Burst](https://www.wowhead.com/spell=431695/temporal-burst)

1/1

[Chronoboon](https://www.wowhead.com/spell=1260484/chronoboon)

1/1

[Reverberations](https://www.wowhead.com/spell=431615/reverberations)

1/1

[Temporality / Motes of Acceleration](https://www.wowhead.com/spell=431873/temporality)

1/1

[Nozdormu Adept](https://www.wowhead.com/spell=431715/nozdormu-adept?spellModifier=396186)

1/1

[Energy Cycles](https://www.wowhead.com/spell=1260568/energy-cycles)

1/1

[Primacy](https://www.wowhead.com/spell=431657/primacy)

1/1

[Double-time / Time Convergence](https://www.wowhead.com/spell=431874/double-time?spellModifier=396186)

1/1

[Instability Matrix](https://www.wowhead.com/spell=431484/instability-matrix)

1/1

[Overclock](https://www.wowhead.com/spell=1260647/overclock)

1/1

[Golden Opportunity](https://www.wowhead.com/spell=432004/golden-opportunity?spellModifier=396186)

1/1

[Afterimage](https://www.wowhead.com/spell=431875/afterimage)

1/1

Spent: 13 / 13Req Level: 89

PvP Talents: PvP:

## ~~~~ Rotation Priority for Augmentation Evoker Beginners

This is a simple example of the spell priorities that make up the Augmentation Evoker rotation. More information about the rotation, as well as an explanation of important abilities and advanced tips can be found in the [Augmentation Evoker Rotation Guide](https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps).

|     |     |
| --- | --- |
| |     |     |
| --- | --- |
| ~~~~ | **Keep your buffs up:** Augmentation's rotation is centered around maximizing uptime of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might). [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_sandsoftime.gif)Sands of Time](https://www.wowhead.com/spell=413525/sands-of-time) allows us to extend the duration of Ebon Might through our damaging rotation: casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_upheaval.gif)Upheaval](https://www.wowhead.com/spell=408092/upheaval) and [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_firebreath.gif)Fire Breath](https://www.wowhead.com/spell=357208/fire-breath) at appropriate ranks on cooldown, spending resources on [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption), and filling downtime with [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_livingflame.gif)Living Flame](https://www.wowhead.com/spell=361469/living-flame) (or [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_azurestrike.gif)Azure Strike](https://www.wowhead.com/spell=362969/azure-strike)). |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Always be casting:** Keeping high uptime on your rotational spells is key to maintaining a solid resource economy in both raids and Mythic+. Use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) effectively to cast spells on the move, and make sure to fill any "downtime" in your rotation with your filler spells, Living Flame and Azure Strike, in order to deal damage and generate [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst). |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Watch your Essence Burst:** Augmentation Evoker has a few different potential sources of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst), and the buff only stacks up to 2. Make sure to spend your Essence Burst when capped, ideally before casting [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_essenceburst.gif)Essence Burst](https://www.wowhead.com/spell=359618/essence-burst) generators like [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_prescience.gif)Prescience](https://www.wowhead.com/spell=409311/prescience) and Living Flame to avoid wasting resources. |

* * *

|     |     |
| --- | --- |
| ~~~~ | **Mind your cooldowns:** It's often correct to send cooldowns as soon as they've come back up, but look for opportunities to align your major cooldowns like [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) with allies' cooldowns and big damage moments during an encounter. | |

### Single Button Rotation Assistant

Assisted Highlight and Single-Button Assistant are two new tools designed to assist players with general combat rotation and how their class spells and abilities influence one another. For Augmentation Evoker, these tools can be expected to perform at quite a reasonable level, but do carry some notable drawbacks. Compared to other specializations, Augmentation Evoker is not heavily penalized by the Single-Button Assistant's increased global cooldown, and damage contributed by buffed allies is similarly unaffected. That said, the in-game rotation does not cast important DPS cooldowns or utility spells, and does not explicitly conserve resources so as to maximize buff uptime.

When playing with Assisted Highlight or the Single-Button Assistant, try and cast your major dps cooldown [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_breathofeons.gif)Breath of Eons](https://www.wowhead.com/spell=403631/breath-of-eons) as frequently as possible, and use [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_hover.gif)Hover](https://www.wowhead.com/spell=358267/hover) whenever needed for movement, as Hover allows you to continue to cast while moving. It is also generally recommended to cast filler spells in place of [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_eruption.gif)Eruption](https://www.wowhead.com/spell=395160/eruption) or your Empower spells during downtime between casts of [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might).

## ~~~~ Best Stats for Augmentation Evoker Beginners

For Augmentation Evoker, **Critical Strike** and **Haste** affect both your personal damage output and [![](https://wow.zamimg.com/images/wow/icons/tiny/spell_sarkareth.gif)Ebon Might](https://www.wowhead.com/spell=395152/ebon-might) uptime. **Mastery** affects the base duration of your buffs, as well as the potency of your [![](https://wow.zamimg.com/images/wow/icons/tiny/ability_evoker_masterytimewalker.gif)Shifting Sands](https://www.wowhead.com/spell=413984/shifting-sands) buff. **Versatility** affects only your personal damage output, while also improving survivability.

For more details, check our [Augmentation Evoker Stats guide](https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps).

1. Intellect (Item Level)

2. Critical Strike

3. Haste

4. Mastery

5. Versatility


* * *

Our Augmentation Evoker guides are always updated with the latest information from in-game experience, simulations, and logs. Make sure to check our changelog for this page by clicking on **View Changelog** in the Quick Facts column or on the book icon at the top of the page. If you are interested in more in-depth Augmentation Evoker guides for **Midnight Season 1**, make sure to browse the _Navigation Bar_ at the top of the page, along with our list of **Related Guides** just beneath the _Table of Contents_.

![](https://wow.zamimg.com/uploads/author-pages/author/ea925294db5fb08bebba4c014a834604ad94e4ad.jpg)

## Jereico

### World of Warcraft Evoker Class Expert

[Twitch](https://www.twitch.tv/Jereico)[Discord](https://discord.gg/vXB3GJsbFw)[YouTube](https://www.youtube.com/@Jereico)[Bluesky](https://bsky.app/profile/jereico.bsky.social)[Author Page](https://www.wowhead.com/author/Jereico)

Jereico (he, him) has written Evoker class guides and editorial content for Wowhead since 2023. He has been an avid fan of MMOs for nearly 25 years, with countless hours dedicated across classic titles like Runescape, Puzzle Pirates, Maple Story, and Guild Wars before first discovering World of Warcraft in 2007.

If you want to get in touch with Jereico, you can find him in his Community Discord, on Twitter and Bluesky, posting videos to YouTube, and occasionally streaming on Twitch.

[Get WowheadPremium$2A MonthEnjoy an ad-free experience, unlock premium features, & support the site!](https://www.wowhead.com/premium)

Comments

Reset Sort« First‹ Previous**1** \- **0** of **0**Next ›Last »

[Add your comment](https://www.wowhead.com/account=signin) \|Sort: newest first, oldest first, highest rated\|Filter by patch:

**No comments have been posted yet.**

Please [log in](https://www.wowhead.com/account=signin) to add your comment, or [register](https://www.wowhead.com/auth/register) if you don't already have an account.

« First‹ Previous**1** \- **0** of **0**Next ›Last »

## Contribute

Add your comment

Please keep the following in mind when posting a comment:

- Your comment must be in English or it will be removed.

- Unsure how to post? Check out our [handy guide](https://www.wowhead.com/help=commenting-and-you)!

- You might want to proof-read your comments before posting them.

- Please post questions on our [forums](https://www.wowhead.com/forums) for quicker reply.


Post a Comment

You are not logged in. Please [log in](https://www.wowhead.com/account=signin) or [register an account](https://www.wowhead.com/auth/register) to add your comment.

Simply browse for your screenshot using the form below.

- Screenshots containing UI elements are generally declined on sight, the same goes for screenshots from the modelviewer or character selection screen.

- The higher the quality the better!

- Please review our [Screenshot Guidelines](https://www.wowhead.com/help=screenshot-guidelines) before submitting!


You are not logged in. Please [log in](https://www.wowhead.com/account=signin) to submit a screenshot.

Simply type the URL of the video in the form below.

URL: Supported: YouTube only

Title: Optional, up to 200 characters

Note: Your video will need to be approved before appearing on the site.

The **Wowhead Client** is a little application we use to keep our database up to date, and to provide you with some nifty extra functionality on the website!

It serves 2 main purposes:

1. It maintains a WoW addon called the **Wowhead Looter**, which collects data as you play the game!

2. It uploads the **collected data** to Wowhead in order to keep the database up-to-date!


You can also use it to keep track of your completed quests, recipes, mounts, companion pets, and titles!

So, what are you waiting for? [Download the client](https://www.wowhead.com/client) and get started.

Do you want to enable desktop notifications for WoW news?

AcceptDeclineMaybe Later

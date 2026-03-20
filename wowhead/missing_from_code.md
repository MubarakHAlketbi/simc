# Talents in info_base.md NOT Found in SimC Code

Generated: 2026-03-17
These talent names appear in the Wowhead talent tree but have no matching
`player_talent_t` declaration or `find_talent_spell()` call in the SimC class module.
They may need implementation, or may use a different name convention in SimC.

For each: verify on Wowhead, check if it is a DPS-relevant talent,
then either implement it or mark N/A.

## AUDIT NOTE — 2026-03-20

**Audited by:** Hermes Agent (subagent)

### Critical Scanner Bug Found

The scanner searched for `player_talent_t` keyword to detect talent declarations.
This caused MASSIVE FALSE POSITIVES for two classes:

- **Hunter** uses `spell_data_ptr_t` for all talent declarations in sc_hunter.cpp
  → All 98/93/93 "missing" Hunter talents (BM/MM/SV) are ALREADY IMPLEMENTED
  → Scanner reported 284 missing, actual missing: 0

- **Paladin** uses `const spell_data_t*` for all talent struct members in sc_paladin.hpp
  → All 95/92 "missing" Paladin talents (Prot/Ret) are ALREADY IMPLEMENTED
  → Scanner reported 187 missing, actual missing: 0

### Classes with Accurate Scanner Results
Classes that use `player_talent_t` (standard pattern) are correctly detected:
Mage, Monk, Rogue, Priest, Shaman, Warlock, Warrior — these have small counts (2-21).

### Recommendation
The missing_from_code.md generator script should be updated to also search for:
- `spell_data_ptr_t`
- `const spell_data_t*`
- `find_talent_spell(` (direct call pattern)

---

---

## Hunter / Beast Mastery (98 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 5116 | Concussive Shot | 1 | [link](https://www.wowhead.com/spell=5116) |
| 19574 | Bestial Wrath | 1 | [link](https://www.wowhead.com/spell=19574) |
| 19577 | Intimidation | 1 | [link](https://www.wowhead.com/spell=19577) |
| 19801 | Tranquilizing Shot | 1 | [link](https://www.wowhead.com/spell=19801) |
| 34026 | Kill Command | 1 | [link](https://www.wowhead.com/spell=34026) |
| 34477 | Misdirection | 1 | [link](https://www.wowhead.com/spell=34477) |
| 109215 | Posthaste | 1 | [link](https://www.wowhead.com/spell=109215) |
| 109248 | Binding Shot | 1 | [link](https://www.wowhead.com/spell=109248) |
| 115939 | Beast Cleave | 1 | [link](https://www.wowhead.com/spell=115939) |
| 120679 | Dire Beast | 1 | [link](https://www.wowhead.com/spell=120679) |
| 147362 | Counter Shot | 1 | [link](https://www.wowhead.com/spell=147362) |
| 191384 | Aspect of the Beast | 1 | [link](https://www.wowhead.com/spell=191384) |
| 193455 | Cobra Shot | 1 | [link](https://www.wowhead.com/spell=193455) |
| 193532 | Scent of Blood | 1 | [link](https://www.wowhead.com/spell=193532) |
| 199483 | Camouflage | 1 | [link](https://www.wowhead.com/spell=199483) |
| 199530 | Stomp | 1 | [link](https://www.wowhead.com/spell=199530) |
| 199532 | Killer Cobra | 1 | [link](https://www.wowhead.com/spell=199532) |
| 217200 | Barbed Shot | 1 | [link](https://www.wowhead.com/spell=217200) |
| 231548 | The Beast Within | 1 | [link](https://www.wowhead.com/spell=231548) |
| 264735 | Survival of the Fittest | 1 | [link](https://www.wowhead.com/spell=264735) |
| 266921 | Born To Be Wild | 1 | [link](https://www.wowhead.com/spell=266921) |
| 269737 | Alpha Predator | 1 | [link](https://www.wowhead.com/spell=269737) |
| 270581 | Natural Mending | 1 | [link](https://www.wowhead.com/spell=270581) |
| 273887 | Killer Instinct | 1 | [link](https://www.wowhead.com/spell=273887) |
| 321014 | Pack Tactics | 1 | [link](https://www.wowhead.com/spell=321014) |
| 343242 | Wilderness Medicine | 1 | [link](https://www.wowhead.com/spell=343242) |
| 343244 | Disruptive Rounds | 1 | [link](https://www.wowhead.com/spell=343244) |
| 343247 | Improved Traps | 1 | [link](https://www.wowhead.com/spell=343247) |
| 378002 | Pathfinding | 1 | [link](https://www.wowhead.com/spell=378002) |
| 378004 | Keen Eyesight | 1 | [link](https://www.wowhead.com/spell=378004) |
| 378207 | Kill Cleave | 1 | [link](https://www.wowhead.com/spell=378207) |
| 378209 | Training Expert | 1 | [link](https://www.wowhead.com/spell=378209) |
| 378743 | Dire Command | 1 | [link](https://www.wowhead.com/spell=378743) |
| 384799 | Hunter | 1 | [link](https://www.wowhead.com/spell=384799) |
| 385539 | Rejuvenating Wind | 1 | [link](https://www.wowhead.com/spell=385539) |
| 385810 | Dire Frenzy | 1 | [link](https://www.wowhead.com/spell=385810) |
| 386870 | Brutal Companion | 1 | [link](https://www.wowhead.com/spell=386870) |
| 388039 | Lone Survivor | 1 | [link](https://www.wowhead.com/spell=388039) |
| 392053 | Piercing Fangs | 1 | [link](https://www.wowhead.com/spell=392053) |
| 393933 | War Orders | 1 | [link](https://www.wowhead.com/spell=393933) |
| 424557 | Savagery | 1 | [link](https://www.wowhead.com/spell=424557) |
| 424558 | Master Handler | 1 | [link](https://www.wowhead.com/spell=424558) |
| 430709 | Smoke Screen | 1 | [link](https://www.wowhead.com/spell=430709) |
| 459450 | Padded Armor | 1 | [link](https://www.wowhead.com/spell=459450) |
| 459455 | Scout | 1 | [link](https://www.wowhead.com/spell=459455) |
| 459502 | Serrated Tips | 1 | [link](https://www.wowhead.com/spell=459502) |
| 459506 | Kindling Flare | 1 | [link](https://www.wowhead.com/spell=459506) |
| 459517 | Emergency Salve | 1 | [link](https://www.wowhead.com/spell=459517) |
| 459527 | Unnatural Causes | 1 | [link](https://www.wowhead.com/spell=459527) |
| 459534 | Trigger Finger | 1 | [link](https://www.wowhead.com/spell=459534) |
| 459542 | Specialized Arsenal | 1 | [link](https://www.wowhead.com/spell=459542) |
| 459546 | No Hard Feelings | 1 | [link](https://www.wowhead.com/spell=459546) |
| 459550 | Go for the Throat | 1 | [link](https://www.wowhead.com/spell=459550) |
| 459552 | Laceration | 1 | [link](https://www.wowhead.com/spell=459552) |
| 459693 | Thundering Hooves | 1 | [link](https://www.wowhead.com/spell=459693) |
| 459730 | Huntmaster | 1 | [link](https://www.wowhead.com/spell=459730) |
| 466930 | Black Arrow | 1 | [link](https://www.wowhead.com/spell=466930) |
| 466990 | Withering Fire | 1 | [link](https://www.wowhead.com/spell=466990) |
| 467749 | Bleak Arrows | 1 | [link](https://www.wowhead.com/spell=467749) |
| 467911 | Bleak Powder | 1 | [link](https://www.wowhead.com/spell=467911) |
| 468701 | Serpentine Strikes | 1 | [link](https://www.wowhead.com/spell=468701) |
| 469638 | Soul Drinker | 1 | [link](https://www.wowhead.com/spell=469638) |
| 469880 | Barbed Scales | 1 | [link](https://www.wowhead.com/spell=469880) |
| 471876 | Howl of the Pack Leader | 1 | [link](https://www.wowhead.com/spell=471876) |
| 472352 | Dire Summons | 1 | [link](https://www.wowhead.com/spell=472352) |
| 472357 | Better Together | 1 | [link](https://www.wowhead.com/spell=472357) |
| 472358 | Pack Mentality | 1 | [link](https://www.wowhead.com/spell=472358) |
| 472550 | Fury of the Wyvern | 1 | [link](https://www.wowhead.com/spell=472550) |
| 472639 | Hogstrider | 1 | [link](https://www.wowhead.com/spell=472639) |
| 472660 | No Mercy | 1 | [link](https://www.wowhead.com/spell=472660) |
| 472707 | Shell Cover | 1 | [link](https://www.wowhead.com/spell=472707) |
| 472741 | Stampede! | 1 | [link](https://www.wowhead.com/spell=472741) |
| 1217524 | Dire Cleave | 1 | [link](https://www.wowhead.com/spell=1217524) |
| 1232739 | Wildspeaker | 1 | [link](https://www.wowhead.com/spell=1232739) |
| 1235397 | Umbral Reach | 1 | [link](https://www.wowhead.com/spell=1235397) |
| 1258402 | Touch of Grass | 1 | [link](https://www.wowhead.com/spell=1258402) |
| 1258404 | Catlike Reflexes | 1 | [link](https://www.wowhead.com/spell=1258404) |
| 1258407 | Improved Aspect of the Cheetah | 1 | [link](https://www.wowhead.com/spell=1258407) |
| 1258485 | Improved Aspect of the Turtle | 1 | [link](https://www.wowhead.com/spell=1258485) |
| 1258486 | Improved Feign Death | 1 | [link](https://www.wowhead.com/spell=1258486) |
| 1264289 | Corpsecaller | 1 | [link](https://www.wowhead.com/spell=1264289) |
| 1264290 | Wailing Dead | 1 | [link](https://www.wowhead.com/spell=1264290) |
| 1264291 | Blighted Quiver | 1 | [link](https://www.wowhead.com/spell=1264291) |
| 1264359 | Wild Thrash | 1 | [link](https://www.wowhead.com/spell=1264359) |
| 1264690 | Pact of the Hollow | 1 | [link](https://www.wowhead.com/spell=1264690) |
| 1264775 | Sharpened Fangs | 1 | [link](https://www.wowhead.com/spell=1264775) |
| 1264781 | Lethal Barbs | 1 | [link](https://www.wowhead.com/spell=1264781) |
| 1264934 | Frenzy | 1 | [link](https://www.wowhead.com/spell=1264934) |
| 1265044 | Jagged Wounds | 1 | [link](https://www.wowhead.com/spell=1265044) |
| 1265051 | Thrill of the Hunt | 1 | [link](https://www.wowhead.com/spell=1265051) |
| 1265052 | Heart of the Pack | 1 | [link](https://www.wowhead.com/spell=1265052) |
| 1267003 | Precision Strikes | 1 | [link](https://www.wowhead.com/spell=1267003) |
| 1267218 | Shell Wall | 1 | [link](https://www.wowhead.com/spell=1267218) |
| 1268671 | Cold Feet | 1 | [link](https://www.wowhead.com/spell=1268671) |
| 1268868 | Improved Snaring | 1 | [link](https://www.wowhead.com/spell=1268868) |
| 1268871 | Combat Experience | 1 | [link](https://www.wowhead.com/spell=1268871) |
| 1272099 | Bloodshed | 1 | [link](https://www.wowhead.com/spell=1272099) |
| 1273043 | Nature | 1 | [link](https://www.wowhead.com/spell=1273043) |

## Hunter / Marksmanship (93 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 5116 | Concussive Shot | 1 | [link](https://www.wowhead.com/spell=5116) |
| 19434 | Aimed Shot | 1 | [link](https://www.wowhead.com/spell=19434) |
| 19801 | Tranquilizing Shot | 1 | [link](https://www.wowhead.com/spell=19801) |
| 34477 | Misdirection | 1 | [link](https://www.wowhead.com/spell=34477) |
| 53351 | Kill Shot | 1 | [link](https://www.wowhead.com/spell=53351) |
| 109215 | Posthaste | 1 | [link](https://www.wowhead.com/spell=109215) |
| 109248 | Binding Shot | 1 | [link](https://www.wowhead.com/spell=109248) |
| 147362 | Counter Shot | 1 | [link](https://www.wowhead.com/spell=147362) |
| 194595 | Lock and Load | 1 | [link](https://www.wowhead.com/spell=194595) |
| 199483 | Camouflage | 1 | [link](https://www.wowhead.com/spell=199483) |
| 204089 | Bullseye | 1 | [link](https://www.wowhead.com/spell=204089) |
| 257044 | Rapid Fire | 1 | [link](https://www.wowhead.com/spell=257044) |
| 260240 | Precise Shots | 1 | [link](https://www.wowhead.com/spell=260240) |
| 260243 | Volley | 1 | [link](https://www.wowhead.com/spell=260243) |
| 260309 | Master Marksman | 1 | [link](https://www.wowhead.com/spell=260309) |
| 264735 | Survival of the Fittest | 1 | [link](https://www.wowhead.com/spell=264735) |
| 266921 | Born To Be Wild | 1 | [link](https://www.wowhead.com/spell=266921) |
| 270581 | Natural Mending | 1 | [link](https://www.wowhead.com/spell=270581) |
| 288613 | Trueshot | 1 | [link](https://www.wowhead.com/spell=288613) |
| 343242 | Wilderness Medicine | 1 | [link](https://www.wowhead.com/spell=343242) |
| 343244 | Disruptive Rounds | 1 | [link](https://www.wowhead.com/spell=343244) |
| 343247 | Improved Traps | 1 | [link](https://www.wowhead.com/spell=343247) |
| 343248 | Deathblow | 1 | [link](https://www.wowhead.com/spell=343248) |
| 378002 | Pathfinding | 1 | [link](https://www.wowhead.com/spell=378002) |
| 378004 | Keen Eyesight | 1 | [link](https://www.wowhead.com/spell=378004) |
| 378767 | Focused Aim | 1 | [link](https://www.wowhead.com/spell=378767) |
| 378913 | Light Ammo | 1 | [link](https://www.wowhead.com/spell=378913) |
| 384799 | Hunter | 1 | [link](https://www.wowhead.com/spell=384799) |
| 385539 | Rejuvenating Wind | 1 | [link](https://www.wowhead.com/spell=385539) |
| 388039 | Lone Survivor | 1 | [link](https://www.wowhead.com/spell=388039) |
| 389019 | Bulletstorm | 1 | [link](https://www.wowhead.com/spell=389019) |
| 391559 | Surging Shots | 1 | [link](https://www.wowhead.com/spell=391559) |
| 400456 | Salvo | 1 | [link](https://www.wowhead.com/spell=400456) |
| 407404 | In the Rhythm | 1 | [link](https://www.wowhead.com/spell=407404) |
| 430709 | Smoke Screen | 1 | [link](https://www.wowhead.com/spell=430709) |
| 450373 | Don | 1 | [link](https://www.wowhead.com/spell=450373) |
| 450379 | Invigorating Pulse | 1 | [link](https://www.wowhead.com/spell=450379) |
| 459450 | Padded Armor | 1 | [link](https://www.wowhead.com/spell=459450) |
| 459455 | Scout | 1 | [link](https://www.wowhead.com/spell=459455) |
| 459502 | Serrated Tips | 1 | [link](https://www.wowhead.com/spell=459502) |
| 459506 | Kindling Flare | 1 | [link](https://www.wowhead.com/spell=459506) |
| 459517 | Emergency Salve | 1 | [link](https://www.wowhead.com/spell=459517) |
| 459527 | Unnatural Causes | 1 | [link](https://www.wowhead.com/spell=459527) |
| 459534 | Trigger Finger | 1 | [link](https://www.wowhead.com/spell=459534) |
| 459542 | Specialized Arsenal | 1 | [link](https://www.wowhead.com/spell=459542) |
| 459546 | No Hard Feelings | 1 | [link](https://www.wowhead.com/spell=459546) |
| 459783 | Penetrating Shots | 1 | [link](https://www.wowhead.com/spell=459783) |
| 459794 | Quick Draw | 1 | [link](https://www.wowhead.com/spell=459794) |
| 459802 | Small Game Hunter | 1 | [link](https://www.wowhead.com/spell=459802) |
| 466932 | Black Arrow | 1 | [link](https://www.wowhead.com/spell=466932) |
| 466990 | Withering Fire | 1 | [link](https://www.wowhead.com/spell=466990) |
| 467749 | Bleak Arrows | 1 | [link](https://www.wowhead.com/spell=467749) |
| 467911 | Bleak Powder | 1 | [link](https://www.wowhead.com/spell=467911) |
| 469638 | Soul Drinker | 1 | [link](https://www.wowhead.com/spell=469638) |
| 470943 | Feathered Frenzy | 1 | [link](https://www.wowhead.com/spell=470943) |
| 471366 | Tensile Bowstring | 1 | [link](https://www.wowhead.com/spell=471366) |
| 471428 | Incendiary Ammunition | 1 | [link](https://www.wowhead.com/spell=471428) |
| 473369 | Eagle | 1 | [link](https://www.wowhead.com/spell=473369) |
| 473370 | Double Tap | 1 | [link](https://www.wowhead.com/spell=473370) |
| 473379 | Target Acquisition | 1 | [link](https://www.wowhead.com/spell=473379) |
| 473385 | No Scope | 1 | [link](https://www.wowhead.com/spell=473385) |
| 473523 | Windrunner Quiver | 1 | [link](https://www.wowhead.com/spell=473523) |
| 474421 | Intimidation | 1 | [link](https://www.wowhead.com/spell=474421) |
| 1232955 | Unmatched Precision | 1 | [link](https://www.wowhead.com/spell=1232955) |
| 1235397 | Umbral Reach | 1 | [link](https://www.wowhead.com/spell=1235397) |
| 1253599 | Sentinel | 1 | [link](https://www.wowhead.com/spell=1253599) |
| 1253732 | Lunar Storm | 1 | [link](https://www.wowhead.com/spell=1253732) |
| 1253825 | Moon | 1 | [link](https://www.wowhead.com/spell=1253825) |
| 1253830 | Can | 1 | [link](https://www.wowhead.com/spell=1253830) |
| 1253831 | Sanctified Armaments | 1 | [link](https://www.wowhead.com/spell=1253831) |
| 1253846 | Arcane Talons | 1 | [link](https://www.wowhead.com/spell=1253846) |
| 1253852 | Lunar Calling | 1 | [link](https://www.wowhead.com/spell=1253852) |
| 1258402 | Touch of Grass | 1 | [link](https://www.wowhead.com/spell=1258402) |
| 1258404 | Catlike Reflexes | 1 | [link](https://www.wowhead.com/spell=1258404) |
| 1258407 | Improved Aspect of the Cheetah | 1 | [link](https://www.wowhead.com/spell=1258407) |
| 1258485 | Improved Aspect of the Turtle | 1 | [link](https://www.wowhead.com/spell=1258485) |
| 1258486 | Improved Feign Death | 1 | [link](https://www.wowhead.com/spell=1258486) |
| 1259922 | Lethality | 1 | [link](https://www.wowhead.com/spell=1259922) |
| 1264289 | Corpsecaller | 1 | [link](https://www.wowhead.com/spell=1264289) |
| 1264290 | Wailing Dead | 1 | [link](https://www.wowhead.com/spell=1264290) |
| 1264291 | Blighted Quiver | 1 | [link](https://www.wowhead.com/spell=1264291) |
| 1264690 | Pact of the Hollow | 1 | [link](https://www.wowhead.com/spell=1264690) |
| 1264902 | Moonlight Chakram | 1 | [link](https://www.wowhead.com/spell=1264902) |
| 1264903 | Radiant Edge | 1 | [link](https://www.wowhead.com/spell=1264903) |
| 1267003 | Precision Strikes | 1 | [link](https://www.wowhead.com/spell=1267003) |
| 1267218 | Shell Wall | 1 | [link](https://www.wowhead.com/spell=1267218) |
| 1268671 | Cold Feet | 1 | [link](https://www.wowhead.com/spell=1268671) |
| 1268868 | Improved Snaring | 1 | [link](https://www.wowhead.com/spell=1268868) |
| 1268871 | Combat Experience | 1 | [link](https://www.wowhead.com/spell=1268871) |
| 1273132 | Take Aim | 1 | [link](https://www.wowhead.com/spell=1273132) |
| 1277546 | Focus Fire | 1 | [link](https://www.wowhead.com/spell=1277546) |
| 1277548 | Unload | 1 | [link](https://www.wowhead.com/spell=1277548) |
| 1277572 | Critical Precision | 1 | [link](https://www.wowhead.com/spell=1277572) |

## Hunter / Survival (93 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 5116 | Concussive Shot | 1 | [link](https://www.wowhead.com/spell=5116) |
| 19577 | Intimidation | 1 | [link](https://www.wowhead.com/spell=19577) |
| 19801 | Tranquilizing Shot | 1 | [link](https://www.wowhead.com/spell=19801) |
| 34477 | Misdirection | 1 | [link](https://www.wowhead.com/spell=34477) |
| 109215 | Posthaste | 1 | [link](https://www.wowhead.com/spell=109215) |
| 109248 | Binding Shot | 1 | [link](https://www.wowhead.com/spell=109248) |
| 186270 | Raptor Strike | 1 | [link](https://www.wowhead.com/spell=186270) |
| 187707 | Muzzle | 1 | [link](https://www.wowhead.com/spell=187707) |
| 199483 | Camouflage | 1 | [link](https://www.wowhead.com/spell=199483) |
| 259489 | Kill Command | 1 | [link](https://www.wowhead.com/spell=259489) |
| 259495 | Wildfire Bomb | 1 | [link](https://www.wowhead.com/spell=259495) |
| 260248 | Bloodseeker | 1 | [link](https://www.wowhead.com/spell=260248) |
| 260285 | Tip of the Spear | 1 | [link](https://www.wowhead.com/spell=260285) |
| 264332 | Guerrilla Tactics | 1 | [link](https://www.wowhead.com/spell=264332) |
| 264735 | Survival of the Fittest | 1 | [link](https://www.wowhead.com/spell=264735) |
| 266921 | Born To Be Wild | 1 | [link](https://www.wowhead.com/spell=266921) |
| 270581 | Natural Mending | 1 | [link](https://www.wowhead.com/spell=270581) |
| 321290 | Improved Wildfire Bomb | 1 | [link](https://www.wowhead.com/spell=321290) |
| 343242 | Wilderness Medicine | 1 | [link](https://www.wowhead.com/spell=343242) |
| 343244 | Disruptive Rounds | 1 | [link](https://www.wowhead.com/spell=343244) |
| 343247 | Improved Traps | 1 | [link](https://www.wowhead.com/spell=343247) |
| 378002 | Pathfinding | 1 | [link](https://www.wowhead.com/spell=378002) |
| 378004 | Keen Eyesight | 1 | [link](https://www.wowhead.com/spell=378004) |
| 378934 | Lunge | 1 | [link](https://www.wowhead.com/spell=378934) |
| 378937 | Explosives Expert | 1 | [link](https://www.wowhead.com/spell=378937) |
| 378950 | Sweeping Spear | 1 | [link](https://www.wowhead.com/spell=378950) |
| 378955 | Killer Companion | 1 | [link](https://www.wowhead.com/spell=378955) |
| 384799 | Hunter | 1 | [link](https://www.wowhead.com/spell=384799) |
| 385539 | Rejuvenating Wind | 1 | [link](https://www.wowhead.com/spell=385539) |
| 388039 | Lone Survivor | 1 | [link](https://www.wowhead.com/spell=388039) |
| 450373 | Don | 1 | [link](https://www.wowhead.com/spell=450373) |
| 450379 | Invigorating Pulse | 1 | [link](https://www.wowhead.com/spell=450379) |
| 459450 | Padded Armor | 1 | [link](https://www.wowhead.com/spell=459450) |
| 459455 | Scout | 1 | [link](https://www.wowhead.com/spell=459455) |
| 459502 | Serrated Tips | 1 | [link](https://www.wowhead.com/spell=459502) |
| 459506 | Kindling Flare | 1 | [link](https://www.wowhead.com/spell=459506) |
| 459517 | Emergency Salve | 1 | [link](https://www.wowhead.com/spell=459517) |
| 459527 | Unnatural Causes | 1 | [link](https://www.wowhead.com/spell=459527) |
| 459534 | Trigger Finger | 1 | [link](https://www.wowhead.com/spell=459534) |
| 459542 | Specialized Arsenal | 1 | [link](https://www.wowhead.com/spell=459542) |
| 459546 | No Hard Feelings | 1 | [link](https://www.wowhead.com/spell=459546) |
| 459843 | Grenade Juggler | 1 | [link](https://www.wowhead.com/spell=459843) |
| 459939 | Outland Venom | 1 | [link](https://www.wowhead.com/spell=459939) |
| 459964 | Flanker | 1 | [link](https://www.wowhead.com/spell=459964) |
| 460198 | Wildfire Infusion | 1 | [link](https://www.wowhead.com/spell=460198) |
| 471876 | Howl of the Pack Leader | 1 | [link](https://www.wowhead.com/spell=471876) |
| 472352 | Dire Summons | 1 | [link](https://www.wowhead.com/spell=472352) |
| 472357 | Better Together | 1 | [link](https://www.wowhead.com/spell=472357) |
| 472358 | Pack Mentality | 1 | [link](https://www.wowhead.com/spell=472358) |
| 472550 | Fury of the Wyvern | 1 | [link](https://www.wowhead.com/spell=472550) |
| 472639 | Hogstrider | 1 | [link](https://www.wowhead.com/spell=472639) |
| 472660 | No Mercy | 1 | [link](https://www.wowhead.com/spell=472660) |
| 472707 | Shell Cover | 1 | [link](https://www.wowhead.com/spell=472707) |
| 472741 | Stampede! | 1 | [link](https://www.wowhead.com/spell=472741) |
| 1250646 | Takedown | 1 | [link](https://www.wowhead.com/spell=1250646) |
| 1251592 | Flamefang Pitch | 1 | [link](https://www.wowhead.com/spell=1251592) |
| 1251717 | Strike as One | 1 | [link](https://www.wowhead.com/spell=1251717) |
| 1251718 | Two Against Many | 1 | [link](https://www.wowhead.com/spell=1251718) |
| 1251790 | Savagery | 1 | [link](https://www.wowhead.com/spell=1251790) |
| 1252708 | Mongoose Fury | 1 | [link](https://www.wowhead.com/spell=1252708) |
| 1252931 | Shellshock | 1 | [link](https://www.wowhead.com/spell=1252931) |
| 1252943 | Wildfire Imbuement | 1 | [link](https://www.wowhead.com/spell=1252943) |
| 1253053 | Shower of Blood | 1 | [link](https://www.wowhead.com/spell=1253053) |
| 1253137 | Sic | 1 | [link](https://www.wowhead.com/spell=1253137) |
| 1253599 | Sentinel | 1 | [link](https://www.wowhead.com/spell=1253599) |
| 1253732 | Lunar Storm | 1 | [link](https://www.wowhead.com/spell=1253732) |
| 1253825 | Moon | 1 | [link](https://www.wowhead.com/spell=1253825) |
| 1253830 | Can | 1 | [link](https://www.wowhead.com/spell=1253830) |
| 1253831 | Sanctified Armaments | 1 | [link](https://www.wowhead.com/spell=1253831) |
| 1253846 | Arcane Talons | 1 | [link](https://www.wowhead.com/spell=1253846) |
| 1253852 | Lunar Calling | 1 | [link](https://www.wowhead.com/spell=1253852) |
| 1256938 | Flanked | 1 | [link](https://www.wowhead.com/spell=1256938) |
| 1258402 | Touch of Grass | 1 | [link](https://www.wowhead.com/spell=1258402) |
| 1258404 | Catlike Reflexes | 1 | [link](https://www.wowhead.com/spell=1258404) |
| 1258407 | Improved Aspect of the Cheetah | 1 | [link](https://www.wowhead.com/spell=1258407) |
| 1258485 | Improved Aspect of the Turtle | 1 | [link](https://www.wowhead.com/spell=1258485) |
| 1258486 | Improved Feign Death | 1 | [link](https://www.wowhead.com/spell=1258486) |
| 1259003 | Raptor Swipe | 1 | [link](https://www.wowhead.com/spell=1259003) |
| 1261193 | Boomstick | 1 | [link](https://www.wowhead.com/spell=1261193) |
| 1262409 | Lethal Calibration | 1 | [link](https://www.wowhead.com/spell=1262409) |
| 1262442 | Bonding | 1 | [link](https://www.wowhead.com/spell=1262442) |
| 1264775 | Sharpened Fangs | 1 | [link](https://www.wowhead.com/spell=1264775) |
| 1264781 | Lethal Barbs | 1 | [link](https://www.wowhead.com/spell=1264781) |
| 1264902 | Moonlight Chakram | 1 | [link](https://www.wowhead.com/spell=1264902) |
| 1264903 | Radiant Edge | 1 | [link](https://www.wowhead.com/spell=1264903) |
| 1267003 | Precision Strikes | 1 | [link](https://www.wowhead.com/spell=1267003) |
| 1267218 | Shell Wall | 1 | [link](https://www.wowhead.com/spell=1267218) |
| 1268671 | Cold Feet | 1 | [link](https://www.wowhead.com/spell=1268671) |
| 1268868 | Improved Snaring | 1 | [link](https://www.wowhead.com/spell=1268868) |
| 1268871 | Combat Experience | 1 | [link](https://www.wowhead.com/spell=1268871) |
| 1272136 | Quick Reload | 1 | [link](https://www.wowhead.com/spell=1272136) |
| 1272139 | Twin Fangs | 1 | [link](https://www.wowhead.com/spell=1272139) |
| 1272154 | Primal Surge | 1 | [link](https://www.wowhead.com/spell=1272154) |

## Mage / Arcane (5 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 382424 | Winter | 1 | [link](https://www.wowhead.com/spell=382424) |
| 444968 | Archmage | 1 | [link](https://www.wowhead.com/spell=444968) |
| 449619 | Memory of Al | 1 | [link](https://www.wowhead.com/spell=449619) |
| 461260 | Consortium | 1 | [link](https://www.wowhead.com/spell=461260) |
| 1257942 | Touch of the Archmage | 1 | [link](https://www.wowhead.com/spell=1257942) |

## Mage / Fire (4 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 382424 | Winter | 1 | [link](https://www.wowhead.com/spell=382424) |
| 449619 | Memory of Al | 1 | [link](https://www.wowhead.com/spell=449619) |
| 450831 | Fire | 1 | [link](https://www.wowhead.com/spell=450831) |
| 1257343 | Fired Up | 1 | [link](https://www.wowhead.com/spell=1257343) |

## Mage / Frost (3 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 417489 | Winter | 1 | [link](https://www.wowhead.com/spell=417489) |
| 444968 | Archmage | 1 | [link](https://www.wowhead.com/spell=444968) |
| 1262935 | Hand of Frost | 1 | [link](https://www.wowhead.com/spell=1262935) |

## Monk / Brewmaster (9 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 116841 | Tiger | 1 | [link](https://www.wowhead.com/spell=116841) |
| 383700 | Gai Plin | 1 | [link](https://www.wowhead.com/spell=383700) |
| 383707 | Stormstout | 1 | [link](https://www.wowhead.com/spell=383707) |
| 414131 | Yu | 1 | [link](https://www.wowhead.com/spell=414131) |
| 450514 | Wind | 1 | [link](https://www.wowhead.com/spell=450514) |
| 450595 | Spirit | 1 | [link](https://www.wowhead.com/spell=450595) |
| 450987 | Veteran | 1 | [link](https://www.wowhead.com/spell=450987) |
| 1241097 | Niuzao | 1 | [link](https://www.wowhead.com/spell=1241097) |
| 1265129 | Bring Me Another | 1 | [link](https://www.wowhead.com/spell=1265129) |

## Monk / Windwalker (10 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 116841 | Tiger | 1 | [link](https://www.wowhead.com/spell=116841) |
| 325201 | Dance of Chi-Ji | 1 | [link](https://www.wowhead.com/spell=325201) |
| 392993 | Xuen | 1 | [link](https://www.wowhead.com/spell=392993) |
| 443566 | Chi-Ji | 1 | [link](https://www.wowhead.com/spell=443566) |
| 450514 | Wind | 1 | [link](https://www.wowhead.com/spell=450514) |
| 450595 | Spirit | 1 | [link](https://www.wowhead.com/spell=450595) |
| 450987 | Veteran | 1 | [link](https://www.wowhead.com/spell=450987) |
| 451485 | Brawler | 1 | [link](https://www.wowhead.com/spell=451485) |
| 1261703 | Tigereye Brew | 1 | [link](https://www.wowhead.com/spell=1261703) |
| 1262667 | Yu | 1 | [link](https://www.wowhead.com/spell=1262667) |

## Paladin / Protection (95 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 1022 | Blessing of Protection | 1 | [link](https://www.wowhead.com/spell=1022) |
| 6940 | Blessing of Sacrifice | 1 | [link](https://www.wowhead.com/spell=6940) |
| 10326 | Turn Evil | 1 | [link](https://www.wowhead.com/spell=10326) |
| 31850 | Ardent Defender | 1 | [link](https://www.wowhead.com/spell=31850) |
| 31935 | Avenger | 1 | [link](https://www.wowhead.com/spell=31935) |
| 53376 | Sanctified Wrath | 1 | [link](https://www.wowhead.com/spell=53376) |
| 85043 | Grand Crusader | 1 | [link](https://www.wowhead.com/spell=85043) |
| 86659 | Guardian of Ancient Kings | 1 | [link](https://www.wowhead.com/spell=86659) |
| 96231 | Rebuke | 1 | [link](https://www.wowhead.com/spell=96231) |
| 114154 | Unbreakable Spirit | 1 | [link](https://www.wowhead.com/spell=114154) |
| 115750 | Blinding Light | 1 | [link](https://www.wowhead.com/spell=115750) |
| 183416 | Blessing of Dawn | 1 | [link](https://www.wowhead.com/spell=183416) |
| 190784 | Divine Steed | 1 | [link](https://www.wowhead.com/spell=190784) |
| 199422 | Holy Ritual | 1 | [link](https://www.wowhead.com/spell=199422) |
| 204023 | Crusader | 1 | [link](https://www.wowhead.com/spell=204023) |
| 204054 | Consecrated Ground | 1 | [link](https://www.wowhead.com/spell=204054) |
| 204074 | Righteous Protector | 1 | [link](https://www.wowhead.com/spell=204074) |
| 204077 | Final Stand | 1 | [link](https://www.wowhead.com/spell=204077) |
| 209389 | Bulwark of Order | 1 | [link](https://www.wowhead.com/spell=209389) |
| 213644 | Cleanse Toxins | 1 | [link](https://www.wowhead.com/spell=213644) |
| 230332 | Cavalier | 1 | [link](https://www.wowhead.com/spell=230332) |
| 231663 | Greater Judgment | 1 | [link](https://www.wowhead.com/spell=231663) |
| 234299 | Fist of Justice | 1 | [link](https://www.wowhead.com/spell=234299) |
| 305394 | Unbound Freedom | 1 | [link](https://www.wowhead.com/spell=305394) |
| 315924 | Hand of the Protector | 1 | [link](https://www.wowhead.com/spell=315924) |
| 321136 | Shining Light | 1 | [link](https://www.wowhead.com/spell=321136) |
| 375576 | Divine Toll | 1 | [link](https://www.wowhead.com/spell=375576) |
| 377053 | Seal of Reprisal | 1 | [link](https://www.wowhead.com/spell=377053) |
| 378279 | Gift of the Golden Val | 1 | [link](https://www.wowhead.com/spell=378279) |
| 378285 | Tyr | 1 | [link](https://www.wowhead.com/spell=378285) |
| 378425 | Uther | 1 | [link](https://www.wowhead.com/spell=378425) |
| 378457 | Soaring Shield | 1 | [link](https://www.wowhead.com/spell=378457) |
| 378762 | Ferren Marcus | 1 | [link](https://www.wowhead.com/spell=378762) |
| 378845 | Focused Enmity | 1 | [link](https://www.wowhead.com/spell=378845) |
| 379021 | Sanctuary | 1 | [link](https://www.wowhead.com/spell=379021) |
| 379022 | Consecration in Flame | 1 | [link](https://www.wowhead.com/spell=379022) |
| 383388 | Relentless Inquisitor | 1 | [link](https://www.wowhead.com/spell=383388) |
| 384815 | Seal of Charity | 1 | [link](https://www.wowhead.com/spell=384815) |
| 384909 | Improved Blessing of Protection | 1 | [link](https://www.wowhead.com/spell=384909) |
| 385414 | Afterimage | 1 | [link](https://www.wowhead.com/spell=385414) |
| 385427 | Obduracy | 1 | [link](https://www.wowhead.com/spell=385427) |
| 385450 | Seal of Might | 1 | [link](https://www.wowhead.com/spell=385450) |
| 385515 | Holy Aegis | 1 | [link](https://www.wowhead.com/spell=385515) |
| 385633 | Auras of the Resolute | 1 | [link](https://www.wowhead.com/spell=385633) |
| 386653 | Bulwark of Righteous Fury | 1 | [link](https://www.wowhead.com/spell=386653) |
| 387791 | Empyreal Ward | 1 | [link](https://www.wowhead.com/spell=387791) |
| 391142 | Zealot | 1 | [link](https://www.wowhead.com/spell=391142) |
| 402964 | Sanctified Plates | 1 | [link](https://www.wowhead.com/spell=402964) |
| 403530 | Punishment | 1 | [link](https://www.wowhead.com/spell=403530) |
| 404357 | Guided Prayer | 1 | [link](https://www.wowhead.com/spell=404357) |
| 406101 | Faith | 1 | [link](https://www.wowhead.com/spell=406101) |
| 406468 | Lightforged Blessing | 1 | [link](https://www.wowhead.com/spell=406468) |
| 425518 | Light | 1 | [link](https://www.wowhead.com/spell=425518) |
| 431463 | Zealous Vindication | 1 | [link](https://www.wowhead.com/spell=431463) |
| 431533 | Shake the Heavens | 1 | [link](https://www.wowhead.com/spell=431533) |
| 431551 | Wrathful Descent | 1 | [link](https://www.wowhead.com/spell=431551) |
| 431687 | Higher Calling | 1 | [link](https://www.wowhead.com/spell=431687) |
| 431730 | Sacrosanct Crusade | 1 | [link](https://www.wowhead.com/spell=431730) |
| 432459 | Holy Armaments | 1 | [link](https://www.wowhead.com/spell=432459) |
| 432463 | Hammerfall | 1 | [link](https://www.wowhead.com/spell=432463) |
| 432626 | Undisputed Ruling | 1 | [link](https://www.wowhead.com/spell=432626) |
| 432802 | Solidarity | 1 | [link](https://www.wowhead.com/spell=432802) |
| 432821 | Shared Resolve | 1 | [link](https://www.wowhead.com/spell=432821) |
| 432866 | Laying Down Arms | 1 | [link](https://www.wowhead.com/spell=432866) |
| 432919 | Valiance | 1 | [link](https://www.wowhead.com/spell=432919) |
| 432929 | Divine Hammer | 1 | [link](https://www.wowhead.com/spell=432929) |
| 433011 | Blessing of the Forge | 1 | [link](https://www.wowhead.com/spell=433011) |
| 433718 | Hammer and Anvil | 1 | [link](https://www.wowhead.com/spell=433718) |
| 469309 | Eye for an Eye | 1 | [link](https://www.wowhead.com/spell=469309) |
| 469316 | Stoicism | 1 | [link](https://www.wowhead.com/spell=469316) |
| 469409 | Divine Spurs | 1 | [link](https://www.wowhead.com/spell=469409) |
| 469411 | A Just Reward | 1 | [link](https://www.wowhead.com/spell=469411) |
| 469416 | Lightbearer | 1 | [link](https://www.wowhead.com/spell=469416) |
| 469439 | Inspired Guard | 1 | [link](https://www.wowhead.com/spell=469439) |
| 469445 | Holy Reprieve | 1 | [link](https://www.wowhead.com/spell=469445) |
| 469476 | Divine Reach | 1 | [link](https://www.wowhead.com/spell=469476) |
| 469770 | Blessed Calling | 1 | [link](https://www.wowhead.com/spell=469770) |
| 469780 | Lead the Charge | 1 | [link](https://www.wowhead.com/spell=469780) |
| 469883 | Refining Fire | 1 | [link](https://www.wowhead.com/spell=469883) |
| 1241288 | Hammer of Wrath | 1 | [link](https://www.wowhead.com/spell=1241288) |
| 1241945 | Blessing of Dusk | 1 | [link](https://www.wowhead.com/spell=1241945) |
| 1241958 | Vengeful Wrath | 1 | [link](https://www.wowhead.com/spell=1241958) |
| 1244019 | Undying Embers | 1 | [link](https://www.wowhead.com/spell=1244019) |
| 1244070 | Searing Sunlight | 1 | [link](https://www.wowhead.com/spell=1244070) |
| 1245354 | Vision of Sanctity | 1 | [link](https://www.wowhead.com/spell=1245354) |
| 1245891 | Solace | 1 | [link](https://www.wowhead.com/spell=1245891) |
| 1245979 | Valiant Crusade | 1 | [link](https://www.wowhead.com/spell=1245979) |
| 1246481 | Empyrean Authority | 1 | [link](https://www.wowhead.com/spell=1246481) |
| 1265541 | Fear No Evil | 1 | [link](https://www.wowhead.com/spell=1265541) |
| 1265549 | Brought to Light | 1 | [link](https://www.wowhead.com/spell=1265549) |
| 1267203 | Glory of the Vanguard | 1 | [link](https://www.wowhead.com/spell=1267203) |
| 1271387 | Masterwork | 1 | [link](https://www.wowhead.com/spell=1271387) |
| 1271466 | Reflection of Radiance | 1 | [link](https://www.wowhead.com/spell=1271466) |
| 1271553 | Resounding Strike | 1 | [link](https://www.wowhead.com/spell=1271553) |
| 1277162 | Instrument of the Divine | 1 | [link](https://www.wowhead.com/spell=1277162) |

## Paladin / Retribution (92 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 1022 | Blessing of Protection | 1 | [link](https://www.wowhead.com/spell=1022) |
| 6940 | Blessing of Sacrifice | 1 | [link](https://www.wowhead.com/spell=6940) |
| 10326 | Turn Evil | 1 | [link](https://www.wowhead.com/spell=10326) |
| 31884 | Avenging Wrath | 1 | [link](https://www.wowhead.com/spell=31884) |
| 53385 | Divine Storm | 1 | [link](https://www.wowhead.com/spell=53385) |
| 96231 | Rebuke | 1 | [link](https://www.wowhead.com/spell=96231) |
| 114154 | Unbreakable Spirit | 1 | [link](https://www.wowhead.com/spell=114154) |
| 115750 | Blinding Light | 1 | [link](https://www.wowhead.com/spell=115750) |
| 156322 | Eternal Flame | 1 | [link](https://www.wowhead.com/spell=156322) |
| 183416 | Blessing of Dawn | 1 | [link](https://www.wowhead.com/spell=183416) |
| 184575 | Blade of Justice | 1 | [link](https://www.wowhead.com/spell=184575) |
| 190784 | Divine Steed | 1 | [link](https://www.wowhead.com/spell=190784) |
| 199422 | Holy Ritual | 1 | [link](https://www.wowhead.com/spell=199422) |
| 204054 | Consecrated Ground | 1 | [link](https://www.wowhead.com/spell=204054) |
| 213644 | Cleanse Toxins | 1 | [link](https://www.wowhead.com/spell=213644) |
| 230332 | Cavalier | 1 | [link](https://www.wowhead.com/spell=230332) |
| 231663 | Greater Judgment | 1 | [link](https://www.wowhead.com/spell=231663) |
| 234299 | Fist of Justice | 1 | [link](https://www.wowhead.com/spell=234299) |
| 255937 | Wake of Ashes | 1 | [link](https://www.wowhead.com/spell=255937) |
| 305394 | Unbound Freedom | 1 | [link](https://www.wowhead.com/spell=305394) |
| 326732 | Empyrean Power | 1 | [link](https://www.wowhead.com/spell=326732) |
| 343527 | Execution Sentence | 1 | [link](https://www.wowhead.com/spell=343527) |
| 375576 | Divine Toll | 1 | [link](https://www.wowhead.com/spell=375576) |
| 382536 | Sanctify | 1 | [link](https://www.wowhead.com/spell=382536) |
| 383328 | Final Verdict | 1 | [link](https://www.wowhead.com/spell=383328) |
| 383344 | Expurgation | 1 | [link](https://www.wowhead.com/spell=383344) |
| 383396 | Tempest of the Lightbringer | 1 | [link](https://www.wowhead.com/spell=383396) |
| 384909 | Improved Blessing of Protection | 1 | [link](https://www.wowhead.com/spell=384909) |
| 385427 | Obduracy | 1 | [link](https://www.wowhead.com/spell=385427) |
| 385450 | Seal of Might | 1 | [link](https://www.wowhead.com/spell=385450) |
| 385515 | Holy Aegis | 1 | [link](https://www.wowhead.com/spell=385515) |
| 385633 | Auras of the Resolute | 1 | [link](https://www.wowhead.com/spell=385633) |
| 387170 | Empyrean Legacy | 1 | [link](https://www.wowhead.com/spell=387170) |
| 387791 | Empyreal Ward | 1 | [link](https://www.wowhead.com/spell=387791) |
| 402964 | Sanctified Plates | 1 | [link](https://www.wowhead.com/spell=402964) |
| 402971 | Jurisdiction | 1 | [link](https://www.wowhead.com/spell=402971) |
| 403010 | Blessed Champion | 1 | [link](https://www.wowhead.com/spell=403010) |
| 403026 | Burning Crusade | 1 | [link](https://www.wowhead.com/spell=403026) |
| 403479 | Lightforged Blessing | 1 | [link](https://www.wowhead.com/spell=403479) |
| 403495 | Judgment of Justice | 1 | [link](https://www.wowhead.com/spell=403495) |
| 403509 | Zealot | 1 | [link](https://www.wowhead.com/spell=403509) |
| 403530 | Punishment | 1 | [link](https://www.wowhead.com/spell=403530) |
| 403664 | Blades of Light | 1 | [link](https://www.wowhead.com/spell=403664) |
| 403826 | Blade of Vengeance | 1 | [link](https://www.wowhead.com/spell=403826) |
| 404357 | Guided Prayer | 1 | [link](https://www.wowhead.com/spell=404357) |
| 404512 | Highlord | 1 | [link](https://www.wowhead.com/spell=404512) |
| 405355 | Seething Flames | 1 | [link](https://www.wowhead.com/spell=405355) |
| 406101 | Faith | 1 | [link](https://www.wowhead.com/spell=406101) |
| 406154 | Heart of the Crusader | 1 | [link](https://www.wowhead.com/spell=406154) |
| 406157 | Judge, Jury and Executioner | 1 | [link](https://www.wowhead.com/spell=406157) |
| 406545 | Holy Flames | 1 | [link](https://www.wowhead.com/spell=406545) |
| 406872 | Divine Wrath | 1 | [link](https://www.wowhead.com/spell=406872) |
| 407067 | Rush of Light | 1 | [link](https://www.wowhead.com/spell=407067) |
| 425518 | Light | 1 | [link](https://www.wowhead.com/spell=425518) |
| 431377 | Dawnlight | 1 | [link](https://www.wowhead.com/spell=431377) |
| 431402 | Luminosity | 1 | [link](https://www.wowhead.com/spell=431402) |
| 431404 | Solar Grace | 1 | [link](https://www.wowhead.com/spell=431404) |
| 431413 | Sun Sear | 1 | [link](https://www.wowhead.com/spell=431413) |
| 431425 | Sun | 1 | [link](https://www.wowhead.com/spell=431425) |
| 431463 | Zealous Vindication | 1 | [link](https://www.wowhead.com/spell=431463) |
| 431474 | Second Sunrise | 1 | [link](https://www.wowhead.com/spell=431474) |
| 431533 | Shake the Heavens | 1 | [link](https://www.wowhead.com/spell=431533) |
| 431551 | Wrathful Descent | 1 | [link](https://www.wowhead.com/spell=431551) |
| 431687 | Higher Calling | 1 | [link](https://www.wowhead.com/spell=431687) |
| 431730 | Sacrosanct Crusade | 1 | [link](https://www.wowhead.com/spell=431730) |
| 432463 | Hammerfall | 1 | [link](https://www.wowhead.com/spell=432463) |
| 432626 | Undisputed Ruling | 1 | [link](https://www.wowhead.com/spell=432626) |
| 432929 | Divine Hammer | 1 | [link](https://www.wowhead.com/spell=432929) |
| 439760 | Aurora | 1 | [link](https://www.wowhead.com/spell=439760) |
| 446663 | Burn to Ash | 1 | [link](https://www.wowhead.com/spell=446663) |
| 458359 | Radiant Glory | 1 | [link](https://www.wowhead.com/spell=458359) |
| 469309 | Eye for an Eye | 1 | [link](https://www.wowhead.com/spell=469309) |
| 469316 | Stoicism | 1 | [link](https://www.wowhead.com/spell=469316) |
| 469409 | Divine Spurs | 1 | [link](https://www.wowhead.com/spell=469409) |
| 469411 | A Just Reward | 1 | [link](https://www.wowhead.com/spell=469411) |
| 469416 | Lightbearer | 1 | [link](https://www.wowhead.com/spell=469416) |
| 469439 | Inspired Guard | 1 | [link](https://www.wowhead.com/spell=469439) |
| 469445 | Holy Reprieve | 1 | [link](https://www.wowhead.com/spell=469445) |
| 469476 | Divine Reach | 1 | [link](https://www.wowhead.com/spell=469476) |
| 469770 | Blessed Calling | 1 | [link](https://www.wowhead.com/spell=469770) |
| 469780 | Lead the Charge | 1 | [link](https://www.wowhead.com/spell=469780) |
| 1241288 | Hammer of Wrath | 1 | [link](https://www.wowhead.com/spell=1241288) |
| 1241945 | Blessing of Dusk | 1 | [link](https://www.wowhead.com/spell=1241945) |
| 1241958 | Vengeful Wrath | 1 | [link](https://www.wowhead.com/spell=1241958) |
| 1253598 | Crusade | 1 | [link](https://www.wowhead.com/spell=1253598) |
| 1261113 | Light Within | 1 | [link](https://www.wowhead.com/spell=1261113) |
| 1261562 | Shield of Vengeance | 1 | [link](https://www.wowhead.com/spell=1261562) |
| 1263782 | Walk Into Light | 1 | [link](https://www.wowhead.com/spell=1263782) |
| 1263787 | Endless Gleam | 1 | [link](https://www.wowhead.com/spell=1263787) |
| 1263920 | Born in Sunlight | 1 | [link](https://www.wowhead.com/spell=1263920) |
| 1265541 | Fear No Evil | 1 | [link](https://www.wowhead.com/spell=1265541) |
| 1265549 | Brought to Light | 1 | [link](https://www.wowhead.com/spell=1265549) |

## Priest / Shadow (9 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 9484 | Shackle Horror | 1 | [link](https://www.wowhead.com/spell=9484) |
| 238100 | Angel | 1 | [link](https://www.wowhead.com/spell=238100) |
| 373273 | Idol of Yogg-Saron | 1 | [link](https://www.wowhead.com/spell=373273) |
| 373280 | Idol of N | 1 | [link](https://www.wowhead.com/spell=373280) |
| 373310 | Idol of Y | 1 | [link](https://www.wowhead.com/spell=373310) |
| 373450 | Light | 1 | [link](https://www.wowhead.com/spell=373450) |
| 377349 | Idol of C | 1 | [link](https://www.wowhead.com/spell=377349) |
| 1240364 | Death | 1 | [link](https://www.wowhead.com/spell=1240364) |
| 1264096 | Void Apparitions | 1 | [link](https://www.wowhead.com/spell=1264096) |

## Rogue / Assassination (3 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 457052 | Deathstalker | 1 | [link](https://www.wowhead.com/spell=457052) |
| 1250325 | Regicide | 1 | [link](https://www.wowhead.com/spell=1250325) |
| 1265385 | Implacable | 1 | [link](https://www.wowhead.com/spell=1265385) |

## Rogue / Outlaw (2 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 1259469 | Grand Melee | 1 | [link](https://www.wowhead.com/spell=1259469) |
| 1265861 | Gravedigger | 1 | [link](https://www.wowhead.com/spell=1265861) |

## Rogue / Subtlety (3 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 426591 | Goremaw | 1 | [link](https://www.wowhead.com/spell=426591) |
| 457052 | Deathstalker | 1 | [link](https://www.wowhead.com/spell=457052) |
| 1268932 | Ancient Arts | 1 | [link](https://www.wowhead.com/spell=1268932) |

## Shaman / Elemental (18 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 1064 | Chain Heal | 1 | [link](https://www.wowhead.com/spell=1064) |
| 51485 | Earthgrab Totem | 1 | [link](https://www.wowhead.com/spell=51485) |
| 51514 | Hex | 1 | [link](https://www.wowhead.com/spell=51514) |
| 51886 | Cleanse Spirit | 1 | [link](https://www.wowhead.com/spell=51886) |
| 108271 | Astral Shift | 1 | [link](https://www.wowhead.com/spell=108271) |
| 108287 | Totemic Projection | 1 | [link](https://www.wowhead.com/spell=108287) |
| 192077 | Wind Rush Totem | 1 | [link](https://www.wowhead.com/spell=192077) |
| 204268 | Voodoo Mastery | 1 | [link](https://www.wowhead.com/spell=204268) |
| 355630 | Windveil | 1 | [link](https://www.wowhead.com/spell=355630) |
| 378081 | Nature | 1 | [link](https://www.wowhead.com/spell=378081) |
| 378211 | Refreshing Waters | 1 | [link](https://www.wowhead.com/spell=378211) |
| 381650 | Elemental Warding | 1 | [link](https://www.wowhead.com/spell=381650) |
| 381689 | Brimming with Life | 1 | [link](https://www.wowhead.com/spell=381689) |
| 381930 | Mana Spring | 1 | [link](https://www.wowhead.com/spell=381930) |
| 382215 | Winds of Al | 1 | [link](https://www.wowhead.com/spell=382215) |
| 443425 | Spiritwalker | 1 | [link](https://www.wowhead.com/spell=443425) |
| 462368 | Elemental Resistance | 1 | [link](https://www.wowhead.com/spell=462368) |
| 1270061 | Feedback Loop | 1 | [link](https://www.wowhead.com/spell=1270061) |

## Shaman / Enhancement (21 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 1064 | Chain Heal | 1 | [link](https://www.wowhead.com/spell=1064) |
| 51485 | Earthgrab Totem | 1 | [link](https://www.wowhead.com/spell=51485) |
| 51514 | Hex | 1 | [link](https://www.wowhead.com/spell=51514) |
| 51886 | Cleanse Spirit | 1 | [link](https://www.wowhead.com/spell=51886) |
| 79206 | Spiritwalker | 1 | [link](https://www.wowhead.com/spell=79206) |
| 108271 | Astral Shift | 1 | [link](https://www.wowhead.com/spell=108271) |
| 108287 | Totemic Projection | 1 | [link](https://www.wowhead.com/spell=108287) |
| 192077 | Wind Rush Totem | 1 | [link](https://www.wowhead.com/spell=192077) |
| 204268 | Voodoo Mastery | 1 | [link](https://www.wowhead.com/spell=204268) |
| 355630 | Windveil | 1 | [link](https://www.wowhead.com/spell=355630) |
| 378081 | Nature | 1 | [link](https://www.wowhead.com/spell=378081) |
| 378211 | Refreshing Waters | 1 | [link](https://www.wowhead.com/spell=378211) |
| 381650 | Elemental Warding | 1 | [link](https://www.wowhead.com/spell=381650) |
| 381689 | Brimming with Life | 1 | [link](https://www.wowhead.com/spell=381689) |
| 381930 | Mana Spring | 1 | [link](https://www.wowhead.com/spell=381930) |
| 382215 | Winds of Al | 1 | [link](https://www.wowhead.com/spell=382215) |
| 384444 | Thorim | 1 | [link](https://www.wowhead.com/spell=384444) |
| 392352 | Storm | 1 | [link](https://www.wowhead.com/spell=392352) |
| 445031 | Wind Barrier | 1 | [link](https://www.wowhead.com/spell=445031) |
| 462368 | Elemental Resistance | 1 | [link](https://www.wowhead.com/spell=462368) |
| 1262713 | Storm Unleashed | 1 | [link](https://www.wowhead.com/spell=1262713) |

## Warlock / Affliction (10 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 108415 | Soul Link | 1 | [link](https://www.wowhead.com/spell=108415) |
| 234876 | Death | 1 | [link](https://www.wowhead.com/spell=234876) |
| 386986 | Sacrolash | 1 | [link](https://www.wowhead.com/spell=386986) |
| 416615 | Xavius | 1 | [link](https://www.wowhead.com/spell=416615) |
| 440040 | Xalan | 1 | [link](https://www.wowhead.com/spell=440040) |
| 440045 | Mark of Peroth | 1 | [link](https://www.wowhead.com/spell=440045) |
| 449637 | Sataiel | 1 | [link](https://www.wowhead.com/spell=449637) |
| 1261984 | Shadow of Nathreza | 1 | [link](https://www.wowhead.com/spell=1261984) |
| 1266803 | Alzzin | 1 | [link](https://www.wowhead.com/spell=1266803) |
| 1270701 | Gorefiend | 1 | [link](https://www.wowhead.com/spell=1270701) |

## Warlock / Demonology (8 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 105174 | Hand of Gul | 1 | [link](https://www.wowhead.com/spell=105174) |
| 108415 | Soul Link | 1 | [link](https://www.wowhead.com/spell=108415) |
| 416230 | Imp-erator | 1 | [link](https://www.wowhead.com/spell=416230) |
| 449637 | Sataiel | 1 | [link](https://www.wowhead.com/spell=449637) |
| 1268716 | Mind | 1 | [link](https://www.wowhead.com/spell=1268716) |
| 1270701 | Gorefiend | 1 | [link](https://www.wowhead.com/spell=1270701) |
| 1276163 | Dominion of Argus | 1 | [link](https://www.wowhead.com/spell=1276163) |
| 1276746 | Tyrant | 1 | [link](https://www.wowhead.com/spell=1276746) |

## Warlock / Destruction (8 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 108415 | Soul Link | 1 | [link](https://www.wowhead.com/spell=108415) |
| 440040 | Xalan | 1 | [link](https://www.wowhead.com/spell=440040) |
| 440045 | Mark of Peroth | 1 | [link](https://www.wowhead.com/spell=440045) |
| 1244941 | Alythess | 1 | [link](https://www.wowhead.com/spell=1244941) |
| 1265770 | Embers of Nihilam | 1 | [link](https://www.wowhead.com/spell=1265770) |
| 1266803 | Alzzin | 1 | [link](https://www.wowhead.com/spell=1266803) |
| 1268716 | Mind | 1 | [link](https://www.wowhead.com/spell=1268716) |
| 1270701 | Gorefiend | 1 | [link](https://www.wowhead.com/spell=1270701) |

## Warrior / Arms (4 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 376079 | Champion | 1 | [link](https://www.wowhead.com/spell=376079) |
| 386634 | Executioner | 1 | [link](https://www.wowhead.com/spell=386634) |
| 444779 | Slayer | 1 | [link](https://www.wowhead.com/spell=444779) |
| 1269314 | Master of Warfare | 1 | [link](https://www.wowhead.com/spell=1269314) |

## Warrior / Fury (5 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 376079 | Champion | 1 | [link](https://www.wowhead.com/spell=376079) |
| 385059 | Odyn | 1 | [link](https://www.wowhead.com/spell=385059) |
| 444779 | Slayer | 1 | [link](https://www.wowhead.com/spell=444779) |
| 1265570 | Executioner | 1 | [link](https://www.wowhead.com/spell=1265570) |
| 1269308 | Rampaging Berserker | 1 | [link](https://www.wowhead.com/spell=1269308) |

## Warrior / Protection (2 missing)

| Spell ID | Name | Max Rank | Wowhead |
|----------|------|----------|---------|
| 376079 | Champion | 1 | [link](https://www.wowhead.com/spell=376079) |
| 1269311 | Phalanx | 1 | [link](https://www.wowhead.com/spell=1269311) |

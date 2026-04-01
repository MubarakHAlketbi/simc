# MID1_Shaman_Elemental_Stormbringer — Buffs & Procs

## Buffs
```
Trigger Count	Interval
	Dynamic Buffs
	Start
	Refresh
	Total
	Start
	Trigger
	Duration
	Uptime
	Benefit
	Overflow
	Expiry
	Alnscorned Essence	5.3	86.4	91.6	20.0s	2.9s	33.5s	58.91%	0.00%	0.0 (0.0)	4.7
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_alnscorned_essence
max_stacks:20
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:false
reactable:false
reverse:false
refresh behavior:duration
stack behavior:asynchronous
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:intellect
amount:34.04
Trigger Details
interval_min/max:0.7s / 218.9s
trigger_min/max:0.7s / 97.4s
trigger_pct:99.99%
duration_min/max:0.0s / 196.1s
uptime_min/max:29.01% / 92.26%
Stack Uptimes
alnscorned_essence_1:4.33%
alnscorned_essence_2:4.64%
alnscorned_essence_3:4.87%
alnscorned_essence_4:5.16%
alnscorned_essence_5:5.48%
alnscorned_essence_6:5.88%
alnscorned_essence_7:6.56%
alnscorned_essence_8:7.38%
alnscorned_essence_9:7.01%
alnscorned_essence_10:4.94%
alnscorned_essence_11:2.17%
alnscorned_essence_12:0.44%
alnscorned_essence_13:0.05%
alnscorned_essence_14:0.00%
alnscorned_essence_15:0.00%
Spelldata
id:1266687
name:Alnscorned Essence
tooltip:{$=}pri increased by {$=}w1.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:20
duration:12.00
cooldown:0.00
default_chance:101.00%
	Alnsight	7.3	3.8	11.1	39.3s	24.9s	15.9s	38.73%	0.00%	3.8 (3.8)	6.9
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_alnsight
max_stacks:1
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:12.0s / 127.0s
trigger_min/max:0.0s / 107.8s
trigger_pct:100.00%
duration_min/max:0.0s / 91.7s
uptime_min/max:15.86% / 71.44%
Stack Uptimes
alnsight_1:38.73%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Amirdrassil's Swiftness	3.5	0.7	4.2	65.4s	52.0s	16.0s	18.80%	0.00%	0.7 (0.7)	3.3
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_amirdrassils_swiftness
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste_rating
amount:156.71
Trigger Details
interval_min/max:15.0s / 309.3s
trigger_min/max:0.1s / 309.3s
trigger_pct:100.00%
duration_min/max:0.0s / 75.6s
uptime_min/max:0.00% / 51.94%
Stack Uptimes
amirdrassils_swiftness_1:18.80%
Spelldata
id:1258887
name:Amirdrassil's Swiftness
tooltip:Granted fleeting power by Amirdrassil, the World Tree, increasing your Haste by {$=}w1.
description:{$@spelldesc1244021=Your spells and abilities can beseech the World Trees for a fragment of their power, granting you {$s1=104} of a random secondary stat for {$1258885d=15 seconds}.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Ascendance	3.0	0.0	3.0	120.6s	120.7s	14.7s	14.78%	17.70%	0.0 (0.0)	2.9
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_ascendance
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:120.0s / 121.8s
trigger_min/max:120.0s / 121.8s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:12.41% / 17.64%
Stack Uptimes
ascendance_1:14.78%
Spelldata
id:1219480
name:Ascendance
tooltip:Transformed into a powerful Fire Ascendant, empowering your Mastery: Elemental Overload.{$?=}{$=}w3>0[
Haste increased by {$=}w3%.][]
description:Transform into a Flame Ascendant for {$d=15 seconds}, instantly casting a Flame Shock and a {$s1=0}0% effectiveness Lava Burst at up to {$s7=6} nearby enemies.
While ascended, Elemental Overload damage is increased by {$s8=75}% and spells affected by your Mastery: Elemental Overload cause {$s9=1} additional Elemental {$=}LOverload:Overloads;.
max_stacks:0
duration:15.00
cooldown:120.00
default_chance:0.00%
	Bloodlust	1.0	0.0	1.0	0.0s	0.0s	40.0s	13.52%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_bloodlust
max_stacks:1
base duration:40.00
duration modifier:1.00
base cooldown:300.00
default_chance:100.00%
default_value:0.30
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 0.0s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:40.0s / 40.0s
uptime_min/max:11.11% / 16.67%
Stack Uptimes
bloodlust_1:13.52%
Spelldata
id:2825
name:Bloodlust
tooltip:Haste increased by {$=}w1%.
description:Increases haste by {$s1=30}% for all party and raid members for {$d=40 seconds}.
Allies receiving this effect will become Sated and unable to benefit from Bloodlust or Time Warp again for {$57724d=600 seconds}.
max_stacks:0
duration:40.00
cooldown:300.00
default_chance:0.00%
	Elemental Blast: Critical Strike	13.6	18.1	31.6	22.3s	9.3s	15.9s	71.86%	0.00%	18.1 (18.1)	12.8
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_elemental_blast_critical_strike
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.07
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:crit
amount:7.50%
Trigger Details
interval_min/max:10.0s / 118.2s
trigger_min/max:0.0s / 96.0s
trigger_pct:100.00%
duration_min/max:0.0s / 106.3s
uptime_min/max:42.74% / 91.34%
Stack Uptimes
elemental_blast_critical_strike_1:71.86%
Spelldata
id:118522
name:Elemental Blast: Critical Strike
tooltip:Critical Strike increased by {$s1=3}%.
description:Critical Strike increased by {$s1=3}%.
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Elemental Blast: Haste	13.4	18.0	31.4	22.6s	9.4s	16.0s	71.51%	0.00%	18.0 (18.0)	12.6
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_elemental_blast_haste
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.07
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste
amount:7.50%
Trigger Details
interval_min/max:10.0s / 116.4s
trigger_min/max:0.0s / 90.4s
trigger_pct:100.00%
duration_min/max:0.0s / 115.8s
uptime_min/max:46.03% / 94.46%
Stack Uptimes
elemental_blast_haste_1:71.51%
Spelldata
id:173183
name:Elemental Blast: Haste
tooltip:Haste increased by {$s1=3}%.
description:Haste increased by {$s1=3}%.
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Elemental Blast: Mastery	13.5	18.1	31.6	22.4s	9.3s	16.0s	71.94%	0.00%	18.1 (18.1)	12.8
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_elemental_blast_mastery
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:7.50
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:mastery
amount:7.50%
Trigger Details
interval_min/max:10.0s / 128.0s
trigger_min/max:0.0s / 97.4s
trigger_pct:100.00%
duration_min/max:0.0s / 118.5s
uptime_min/max:45.12% / 91.34%
Stack Uptimes
elemental_blast_mastery_1:71.94%
Spelldata
id:173184
name:Elemental Blast: Mastery
tooltip:Mastery increased by {$=}{{$s1=3}*{$168534=}bc1}%.
description:Mastery increased by {$=}{{$s1=3}*{$168534=}bc1}%.
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Emberwing Burn (Crit)	0.1	0.0	0.1	146.5s	121.1s	9.9s	0.33%	0.00%	0.0 (0.0)	0.1
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_emberwing_burn_crit
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:crit_rating
amount:-233.85
Trigger Details
interval_min/max:120.1s / 240.9s
trigger_min/max:120.3s / 121.5s
trigger_pct:100.00%
duration_min/max:0.0s / 10.0s
uptime_min/max:0.00% / 11.21%
Stack Uptimes
emberwing_burn_crit_1:0.33%
Spelldata
id:1255853
name:Emberwing Burn
tooltip:Critical Strike decreased by {$=}w1.
description:
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Emberwing Burn (Mastery)	0.1	0.0	0.1	164.0s	121.1s	9.9s	0.32%	0.00%	0.0 (0.0)	0.1
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_emberwing_burn_mast
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:mastery_rating
amount:-233.85
Trigger Details
interval_min/max:120.0s / 242.0s
trigger_min/max:120.5s / 121.7s
trigger_pct:100.00%
duration_min/max:0.2s / 10.0s
uptime_min/max:0.00% / 7.93%
Stack Uptimes
emberwing_burn_mast_1:0.32%
Spelldata
id:1255856
name:Emberwing Burn
tooltip:Mastery decreased by {$=}w1.
description:
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Emberwing Burn (Vers)	0.1	0.0	0.1	143.8s	120.4s	9.9s	0.34%	0.00%	0.0 (0.0)	0.1
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_emberwing_burn_vers
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:versatility_rating
amount:-233.85
Trigger Details
interval_min/max:120.0s / 241.9s
trigger_min/max:120.0s / 121.1s
trigger_pct:100.00%
duration_min/max:0.5s / 10.0s
uptime_min/max:0.00% / 8.23%
Stack Uptimes
emberwing_burn_vers_1:0.34%
Spelldata
id:1255857
name:Emberwing Burn
tooltip:Versatility decreased by {$=}w1.
description:
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Emberwing Heatwave	3.0	3.0	6.0	120.6s	40.1s	14.7s	14.79%	0.00%	3.0 (3.0)	2.9
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_emberwing_heatwave
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste_rating
amount:752.71
Trigger Details
interval_min/max:120.0s / 122.6s
trigger_min/max:0.0s / 122.6s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:12.41% / 17.64%
Stack Uptimes
emberwing_heatwave_1:14.79%
Spelldata
id:1250508
name:Emberwing Heatwave
tooltip:Haste increased by {$=}w1.
description:Unleash an {$@=}spellname1250508, increasing your Haste by {$s1=264} for {$d=15 seconds}.
You have a low chance to suffer an {$@=}spellname1255853, reducing one of your other secondary stats by {$s2=82} for {$1255853d=10 seconds}.
max_stacks:0
duration:15.00
cooldown:120.00
default_chance:0.00%
	Fire Elemental	3.0	0.0	3.0	120.6s	120.7s	23.2s	23.29%	33.48%	0.0 (0.0)	2.8
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_fire_elemental
max_stacks:1
base duration:24.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.25
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:120.0s / 121.8s
trigger_min/max:120.0s / 121.8s
trigger_pct:100.00%
duration_min/max:0.0s / 24.0s
uptime_min/max:19.86% / 27.25%
Stack Uptimes
fire_elemental_1:23.29%
Spelldata
id:188592
name:Fire Elemental
tooltip:Flame Shock deals damage {$s2=25}% faster. {$?=}{$=}w3!>0[Newly applied Flame Shocks have {$=}w3% increased duration.][]
description:{$@spelldesc198067=Calls forth a Greater Fire Elemental to rain destruction on your enemies for {$188592d=20 seconds}.
While the Fire Elemental is active, Flame Shock deals damage {$=}{100*(1/(1+{$188592s2=25}/100)-1)}% faster, and newly applied Flame Shocks last {$188592s3=100}% longer.}
max_stacks:0
duration:24.00
cooldown:0.00
default_chance:0.00%
	Lava Surge	22.0	0.0	22.0	13.6s	13.6s	1.0s	7.60%	33.43%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_lava_surge
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:false
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:4.2s / 38.2s
trigger_min/max:4.2s / 38.2s
trigger_pct:99.99%
duration_min/max:0.0s / 9.7s
uptime_min/max:3.20% / 12.87%
Stack Uptimes
lava_surge_1:7.60%
Spelldata
id:77762
name:Lava Surge
tooltip:Your next Lava Burst casts instantly.
description:The Shaman's next Lava Burst casts instantly.
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:100.00%
	Light's Potential	1.5	0.0	1.5	307.6s	0.0s	27.5s	13.45%	0.00%	0.0 (0.0)	1.2
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_lights_potential
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
associated item:Light's Potential
Stat Details
stat:intellect
amount:695.00
Trigger Details
interval_min/max:300.0s / 330.3s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.97% / 18.18%
Stack Uptimes
lights_potential_1:13.45%
Spelldata
id:1236616
name:Light's Potential
tooltip:Primary stat increased by {$=}w1.
description:Drink to increase your primary stat by {$s1=365} for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Master of the Elements	63.9	0.0	63.9	4.7s	4.7s	1.3s	27.62%	29.10%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_master_of_the_elements
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.15
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.8s / 14.5s
trigger_min/max:0.8s / 14.5s
trigger_pct:100.00%
duration_min/max:0.0s / 4.1s
uptime_min/max:21.02% / 32.10%
Stack Uptimes
master_of_the_elements_1:27.62%
Spelldata
id:260734
name:Master of the Elements
tooltip:Your next Nature, Physical, or Frost spell will deal {$s1=0}% increased damage or healing.
description:{$@spelldesc16166=Casting Lava Burst increases the damage or healing of your next Nature{$?a137039=false}[][, Physical,] or Frost spell by {$s2=15}%.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Nature's Swiftness	5.4	0.0	5.4	61.6s	61.4s	2.3s	2.09%	4.43%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_natures_swiftness
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:60.0s / 71.9s
trigger_min/max:60.0s / 71.9s
trigger_pct:100.00%
duration_min/max:0.0s / 11.2s
uptime_min/max:0.50% / 7.73%
Stack Uptimes
natures_swiftness_1:2.09%
Spelldata
id:378081
name:Nature's Swiftness
tooltip:Your next healing or damaging Nature spell is instant cast and costs no mana.
description:Your next healing or damaging Nature spell {$?a1246131=false}[or Hex ][]is instant cast and costs no mana.
max_stacks:0
duration:-0.00
cooldown:60.00
default_chance:100.00%
	Nordrassil's Sagacity	3.5	0.7	4.2	65.9s	52.6s	16.0s	18.63%	0.00%	0.7 (0.7)	3.3
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_nordrassils_sagacity
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:mastery_rating
amount:156.71
Trigger Details
interval_min/max:15.0s / 320.2s
trigger_min/max:0.0s / 320.2s
trigger_pct:100.00%
duration_min/max:0.0s / 63.8s
uptime_min/max:0.00% / 49.95%
Stack Uptimes
nordrassils_sagacity_1:18.63%
Spelldata
id:1258886
name:Nordrassil's Sagacity
tooltip:Granted fleeting power by Nordrassil, the World Tree, increasing your Mastery by {$=}w1.
description:{$@spelldesc1244021=Your spells and abilities can beseech the World Trees for a fragment of their power, granting you {$s1=104} of a random secondary stat for {$1258885d=15 seconds}.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Power of the Maelstrom	9.5	0.1	9.6	29.2s	28.8s	1.7s	5.43%	7.30%	0.1 (0.1)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_power_of_the_maelstrom
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.8s / 307.7s
trigger_min/max:0.8s / 307.7s
trigger_pct:100.00%
duration_min/max:0.0s / 15.1s
uptime_min/max:0.00% / 15.71%
Stack Uptimes
power_of_the_maelstrom_1:5.43%
Spelldata
id:191861
name:Power of the Maelstrom
tooltip:
description:Casting Lava Burst has a {$s1=15}% chance to cause your next Lightning Bolt{$?a454009=true}[, Tempest,][] or Chain Lightning cast to trigger Elemental Overload an additional time, stacking up to {$191877=}U times.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:100.00%
	Precision of the Dragonhawk	8.2	8.5	16.6	36.3s	17.2s	21.7s	59.03%	0.00%	8.5 (8.5)	7.6
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_precision_of_the_dragonhawk
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:crit_rating
amount:124.37
Trigger Details
interval_min/max:15.0s / 138.8s
trigger_min/max:0.0s / 72.9s
trigger_pct:100.00%
duration_min/max:0.0s / 139.3s
uptime_min/max:31.55% / 84.22%
Stack Uptimes
precision_of_the_dragonhawk_1:59.03%
Spelldata
id:1241761
name:Precision of the Dragonhawk
tooltip:You have the Precision of the Dragonhawk, increasing your Critical Strike by {$=}w1.
description:{$@spelldesc1236066=Permanently enchants a weapon with Jan'alai's Precision, causing your spells and abilities to sometimes grant you Precision of the Dragonhawk, increasing your Critical Strike by {$=}ec1s1 for {$1241761d=15 seconds}. Cannot be applied to items lower than level {$=}ecim.
|cnNORMAL_FONT_COLOR:Amani Augments - Zul'Aman Zeal|R }
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Shaladrassil's Strength	3.5	0.7	4.2	65.9s	52.7s	16.0s	18.66%	0.00%	0.7 (0.7)	3.3
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_shaladrassils_strength
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:crit_rating
amount:156.71
Trigger Details
interval_min/max:15.0s / 325.6s
trigger_min/max:0.8s / 325.6s
trigger_pct:100.00%
duration_min/max:0.0s / 57.8s
uptime_min/max:0.00% / 49.08%
Stack Uptimes
shaladrassils_strength_1:18.66%
Spelldata
id:1258890
name:Shaladrassil's Strength
tooltip:Granted fleeting power by Shaladrassil, the World Tree, increasing your Critical Strike by {$=}w1.
description:{$@spelldesc1244021=Your spells and abilities can beseech the World Trees for a fragment of their power, granting you {$s1=104} of a random secondary stat for {$1258885d=15 seconds}.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Storm Elemental	6.8	0.0	6.8	47.8s	48.1s	14.1s	32.10%	0.00%	0.0 (0.0)	6.5
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_storm_elemental
max_stacks:1
base duration:14.40
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:46.1s / 57.9s
trigger_min/max:46.1s / 57.9s
trigger_pct:100.00%
duration_min/max:0.0s / 14.4s
uptime_min/max:29.90% / 35.10%
Stack Uptimes
storm_elemental_1:32.10%
Spelldata
id:157299
name:Storm Elemental
tooltip:
description:{$@spelldesc191717=Casting Stormkeeper summons a {$?a117013=true}[Primal][Greater] Storm Elemental to hurl gusts of wind at your enemies for {$157299d=10 seconds}.}
max_stacks:0
duration:14.40
cooldown:0.00
default_chance:0.00%
	Stormkeeper	17.8	8.3	26.1	17.2s	12.0s	4.0s	23.56%	22.93%	0.6 (0.6)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_stormkeeper
max_stacks:4
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:1.50
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:2.0s / 68.7s
trigger_min/max:0.0s / 55.5s
trigger_pct:100.00%
duration_min/max:0.0s / 52.2s
uptime_min/max:13.79% / 38.55%
Stack Uptimes
stormkeeper_1:10.20%
stormkeeper_2:6.15%
stormkeeper_3:5.29%
stormkeeper_4:1.93%
Spelldata
id:191634
name:Stormkeeper
tooltip:Your next Lightning Bolt will deal {$s2=150}% increased damage, and your next Lightning Bolt or Chain Lightning will be instant cast and cause an Elemental Overload to trigger on every target hit.
description:Charge yourself with lightning, causing your next {$s5=2} Lightning Bolts to deal {$s2=150}% more damage, and also causes your next {$s5=2} Lightning Bolts or Chain Lightings to be instant cast and trigger an Elemental Overload on every target.{$?a1264762=true}[
|cFFFFFFFFGenerates {$1264762s2=10} Maelstrom.|r][]
max_stacks:4
duration:15.00
cooldown:45.00
default_chance:100.00%
	Teldrassil's Tenacity	3.5	0.7	4.2	65.7s	52.4s	16.0s	18.79%	0.00%	0.7 (0.7)	3.3
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_teldrassils_tenacity
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:versatility_rating
amount:156.71
Trigger Details
interval_min/max:15.0s / 318.7s
trigger_min/max:0.8s / 318.7s
trigger_pct:100.00%
duration_min/max:0.0s / 60.9s
uptime_min/max:0.00% / 50.27%
Stack Uptimes
teldrassils_tenacity_1:18.79%
Spelldata
id:1258885
name:Teldrassil's Tenacity
tooltip:Granted fleeting power by Teldrassil, the World Tree, increasing your Versatility by {$=}w1.
description:{$@spelldesc1244021=Your spells and abilities can beseech the World Trees for a fragment of their power, granting you {$s1=104} of a random secondary stat for {$1258885d=15 seconds}.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Tempest	18.1	1.4	19.5	16.9s	15.9s	2.5s	15.16%	0.00%	0.1 (0.1)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_tempest
max_stacks:2
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:1.0s / 71.1s
trigger_min/max:0.0s / 71.1s
trigger_pct:100.00%
duration_min/max:0.0s / 20.7s
uptime_min/max:8.83% / 24.46%
Stack Uptimes
tempest_1:14.04%
tempest_2:1.11%
Spelldata
id:454015
name:Tempest
tooltip:Lightning Bolt replaced by Tempest.
description:Lightning Bolt replaced by Tempest.
max_stacks:2
duration:30.00
cooldown:0.00
default_chance:101.00%
	Thunderous Velocity	6.8	0.0	6.8	47.8s	48.1s	9.9s	22.46%	0.00%	0.0 (0.0)	6.6
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_thunderous_velocity
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.15
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste
amount:15.00%
Trigger Details
interval_min/max:46.1s / 57.9s
trigger_min/max:46.1s / 57.9s
trigger_pct:100.00%
duration_min/max:0.0s / 10.0s
uptime_min/max:20.77% / 24.75%
Stack Uptimes
thunderous_velocity_1:22.46%
Spelldata
id:1272101
name:Thunderous Velocity
tooltip:Haste increased by {$=}{{$=}w1}.1%.
description:{$@spelldesc1264862=Casting Stormkeeper grants {$1272101s1=15}% haste for {$1272101d=10 seconds}.}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:101.00%
Trigger Spelldata
id:1264862
name:Shaman Elemental 12.0 Class Set 2pc
tooltip:
description:Casting Stormkeeper grants {$1272101s1=15}% haste for {$1272101d=10 seconds}.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:101.00%
	Unlimited Power	14.0	16.7	30.7	21.7s	9.6s	14.6s	68.20%	0.00%	0.0 (0.0)	13.3
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_unlimited_power
max_stacks:15
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.01
activated:true
reactable:false
reverse:false
refresh behavior:disabled
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste
amount:1.00%
Trigger Details
interval_min/max:15.0s / 38.7s
trigger_min/max:0.0s / 25.4s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:55.57% / 83.55%
Stack Uptimes
unlimited_power_1:42.50%
unlimited_power_2:19.31%
unlimited_power_3:5.18%
unlimited_power_4:1.03%
unlimited_power_5:0.16%
unlimited_power_6:0.02%
unlimited_power_7:0.00%
unlimited_power_8:0.04%
Spelldata
id:454394
name:Unlimited Power
tooltip:Haste increased by {$s1=1}%.
description:{$@spelldesc454391=Spending {$?s137040=true}[Maelstrom][Maelstrom Weapon stacks] grants you {$454394s1=1}% haste for {$454394d=15 seconds}.
Multiple applications may overlap.}
max_stacks:15
duration:15.00
cooldown:0.00
default_chance:101.00%
	Wind Gust	6.8	43.5	50.3	47.8s	5.8s	12.7s	28.88%	0.00%	23.3 (23.3)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer
cooldown name:buff_wind_gust
max_stacks:4
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.04
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste
amount:4.00%
Trigger Details
interval_min/max:36.6s / 64.5s
trigger_min/max:0.0s / 54.1s
trigger_pct:100.00%
duration_min/max:0.0s / 14.4s
uptime_min/max:23.83% / 33.82%
Stack Uptimes
wind_gust_1:4.93%
wind_gust_2:4.12%
wind_gust_3:3.91%
wind_gust_4:15.90%
Spelldata
id:263806
name:Wind Gust
tooltip:Haste increased by {$=}w1%.
description:Haste increased by {$s1=4}%.
max_stacks:4
duration:-0.00
cooldown:0.00
default_chance:101.00%
	primal_storm_elemental - primal_storm_elemental: Call Lightning	6.8	0.0	6.8	47.8s	47.8s	12.5s	88.00%	92.25%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Shaman_Elemental_Stormbringer_primal_storm_elemental
cooldown name:buff_call_lightning
max_stacks:1
base duration:20.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:45.9s / 58.0s
trigger_min/max:45.9s / 58.0s
trigger_pct:100.00%
duration_min/max:0.0s / 13.0s
uptime_min/max:86.13% / 88.77%
Stack Uptimes
call_lightning_1:88.00%
Spelldata
id:157348
name:Call Lightning
tooltip:Damage done increased by {$=}w2%.
description:Call down a lightning strike on an enemy, dealing {$s1=0} Nature damage, and leaving the Storm Elemental charged with energy for {$d=20 seconds}.
While charged, the Storm Elemental's damage is increased by {$s2=30}%.
max_stacks:0
duration:20.00
cooldown:20.00
default_chance:0.00%
```

## Procs & Uptimes
```
Proc
	Count
	Min
	Max
	Interval
	Min
	Max
	Aftershock	7.7	0.0	22.0	32.5s	0.0s	305.3s
	Ascendance: Elemental Blast	7.9	3.0	16.0	35.1s	0.0s	126.7s
	Ascendance: Lava Burst	16.0	10.0	18.0	16.8s	0.8s	114.4s
	Ascendance: Lightning Bolt	16.5	7.0	23.0	15.8s	0.0s	233.9s
	Ascendance: Tempest	5.9	2.0	10.0	49.7s	0.0s	127.8s
	Elemental Blast: Critical Strike	31.6	14.0	55.0	10.0s	0.0s	96.0s
	Elemental Blast: Haste	31.4	14.0	56.0	10.0s	0.0s	90.4s
	Elemental Blast: Mastery	31.6	15.0	61.0	10.0s	0.0s	97.4s
	Lava Surge	22.0	15.0	28.0	13.6s	4.2s	38.2s
	Lava Surge: During Lava Burst	4.5	0.0	13.0	49.9s	5.6s	319.0s
	Master of the Elements: Elemental Blast	10.6	1.0	23.0	26.3s	1.0s	226.2s
	Master of the Elements: Flame Shock	0.4	0.0	2.0	120.6s	120.0s	121.8s
	Master of the Elements: Lightning Bolt	41.4	25.0	59.0	7.2s	0.9s	48.7s
	Master of the Elements: Tempest	11.2	3.0	21.0	26.8s	0.8s	122.9s
	PotM: Tempest	2.7	0.0	10.0	70.9s	0.9s	348.6s
```

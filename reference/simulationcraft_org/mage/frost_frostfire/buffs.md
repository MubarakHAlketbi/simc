# MID1_Mage_Frost_Frostfire — Buffs & Procs

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
	Alnscorned Essence	5.2	95.5	100.7	20.0s	2.6s	34.0s	59.32%	0.00%	0.0 (0.0)	4.6
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
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
interval_min/max:0.7s / 250.3s
trigger_min/max:0.7s / 98.8s
trigger_pct:99.99%
duration_min/max:0.0s / 200.6s
uptime_min/max:23.43% / 94.07%
Stack Uptimes
alnscorned_essence_1:3.86%
alnscorned_essence_2:4.25%
alnscorned_essence_3:4.54%
alnscorned_essence_4:4.81%
alnscorned_essence_5:5.09%
alnscorned_essence_6:5.41%
alnscorned_essence_7:6.01%
alnscorned_essence_8:6.95%
alnscorned_essence_9:6.34%
alnscorned_essence_10:4.09%
alnscorned_essence_11:2.99%
alnscorned_essence_12:2.49%
alnscorned_essence_13:1.91%
alnscorned_essence_14:0.56%
alnscorned_essence_15:0.01%
Spelldata
id:1266687
name:Alnscorned Essence
tooltip:{$=}pri increased by {$=}w1.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:20
duration:12.00
cooldown:0.00
default_chance:101.00%
	Alnsight	7.3	3.8	11.1	39.3s	24.9s	15.8s	38.64%	0.00%	3.8 (3.8)	6.9
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
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
interval_min/max:12.0s / 144.6s
trigger_min/max:0.0s / 107.7s
trigger_pct:100.00%
duration_min/max:0.0s / 103.7s
uptime_min/max:14.60% / 73.52%
Stack Uptimes
alnsight_1:38.64%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Arcanoweave Insight	5.9	5.2	11.1	49.9s	24.9s	26.8s	52.49%	0.00%	5.2 (5.2)	5.3
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_arcanoweave_insight
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
Stat Details
stat:intellect
amount:43.73
Trigger Details
interval_min/max:20.0s / 182.4s
trigger_min/max:0.0s / 107.0s
trigger_pct:100.00%
duration_min/max:0.0s / 154.0s
uptime_min/max:24.13% / 89.31%
Stack Uptimes
arcanoweave_insight_1:52.49%
Spelldata
id:1229746
name:Arcanoweave Insight
tooltip:{$=}pri increased by {$=}w1.
description:Increases your {$=}pri by $1229511s0.
max_stacks:0
duration:20.00
cooldown:0.00
default_chance:0.00%
	Bloodlust	1.0	0.0	1.0	0.0s	0.0s	40.0s	13.52%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
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
	Brain Freeze	33.9	0.7	34.6	8.8s	8.6s	1.4s	15.41%	70.15%	0.7 (0.7)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_brain_freeze
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stack Uptimes
brain_freeze_1:15.41%
Spelldata
id:190446
name:Brain Freeze
tooltip:Your next Flurry deals {$s2=50}% increased damage.
description:{$@spelldesc190447={$?s431044=true}[Frostfire Bolt][Frostbolt] has a {$m1=25}% chance to reset the remaining cooldown on Flurry and cause your next Flurry to deal {$190446s2=50}% increased damage.}
max_stacks:1
duration:30.00
cooldown:0.00
default_chance:100.00%
	Brainstorm	16.5	17.7	34.2	13.7s	8.7s	12.8s	70.49%	0.00%	0.0 (0.0)	15.9
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_brainstorm
max_stacks:5
base duration:8.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.01
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
amount:1.00%
Trigger Details
interval_min/max:0.0s / 97.6s
trigger_min/max:0.0s / 61.8s
trigger_pct:98.96%
duration_min/max:0.4s / 90.9s
uptime_min/max:49.39% / 87.69%
Stack Uptimes
brainstorm_1:51.34%
brainstorm_2:17.47%
brainstorm_3:1.65%
brainstorm_4:0.03%
brainstorm_5:0.00%
Spelldata
id:461531
name:Brainstorm
tooltip:Your Intellect is increased by {$=}{{$s1=1}}.1%.
description:{$@spelldesc461261=Gaining {$?a137021=false}[Clearcasting]?a137020[Brain Freeze][Hot Streak] increases your Intellect by {$461531s1=1}% for {$461531d=8 seconds}. Multiple instances may overlap.}
max_stacks:5
duration:8.00
cooldown:0.00
default_chance:101.00%
	Comet Storm!	6.4	0.0	6.4	49.3s	49.3s	4.4s	9.39%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_comet_storm
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
interval_min/max:8.0s / 79.3s
trigger_min/max:8.0s / 79.3s
trigger_pct:100.00%
duration_min/max:0.0s / 8.7s
uptime_min/max:6.63% / 13.26%
Stack Uptimes
comet_storm_1:9.39%
Spelldata
id:1247778
name:Comet Storm!
tooltip:Your Blizzard is replaced with Comet Storm.
description:{$@spelldesc1247777=Casting Ray of Frost replaces your Ray of Frost with Comet Storm, calling down a series of 7 icy comets on and around the target, that deals up to {$=}{7*{$153596s1=0}} Frost damage to all enemies within {$153596=}A1 yds of its impacts.
|CFFffffffEach Comet Shatters {$1246769s5=1} {$=}Lstack:stacks; of Freezing.|R}
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:0.00%
	Fingers of Frost	33.6	12.1	45.7	8.9s	6.5s	1.9s	21.66%	50.41%	2.4 (2.4)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_fingers_of_frost
max_stacks:2
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 37.7s
trigger_min/max:0.0s / 27.3s
trigger_pct:14.49%
duration_min/max:0.0s / 16.2s
uptime_min/max:10.70% / 32.85%
Stack Uptimes
fingers_of_frost_1:18.35%
fingers_of_frost_2:3.31%
Spelldata
id:44544
name:Fingers of Frost
tooltip:Your next Ice Lance Shatters your target without removing any Freezing stacks.
description:{$@spelldesc112965={$?s431044=true}[Frostfire Bolt][Frostbolt] has a {$s1=15}% chance to grant a charge of Fingers of Frost.
Fingers of Frost causes your next Ice Lance to deal Shatter damage equal to {$1246769s4=4} stacks of Freezing and does not consume Freezing stacks.
Maximum {$44544u=2} {$=}Lcharge:charges;.}
max_stacks:2
duration:15.00
cooldown:0.00
default_chance:101.00%
	Frostfire Empowerment	19.2	7.1	26.2	15.8s	11.5s	5.9s	37.84%	0.00%	0.9 (0.9)	0.1
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_frostfire_empowerment
max_stacks:2
base duration:20.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.9s / 60.9s
trigger_min/max:0.0s / 29.3s
trigger_pct:100.00%
duration_min/max:0.0s / 43.6s
uptime_min/max:18.97% / 60.30%
Stack Uptimes
frostfire_empowerment_1:30.35%
frostfire_empowerment_2:7.49%
Spelldata
id:431177
name:Frostfire Empowerment
tooltip:Your next Frostfire Bolt deals {$s3=60}% additional damage, explodes for {$=}<ffe>% of its damage to nearby enemies, and is instant cast.
description:{$@spelldesc431176=Casting Frostfire spells has a {$s3=10}% chance to activate Frostfire Empowerment, causing your next Frostfire Bolt to be instant cast, deal {$431177s3=60}% increased damage, explode for {$s2=60}% of its damage to nearby enemies. Damage reduced beyond {$s5=5} targets.{$?=}c2[][
Damage from Frostfire Empowerment applies {$s4=1} {$=}Lstack:stacks; of Freezing.]}
max_stacks:2
duration:20.00
cooldown:0.00
default_chance:101.00%
	Glacial Spike!	13.6	0.5	14.1	22.9s	22.9s	2.1s	9.70%	0.00%	0.5 (0.5)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_glacial_spike
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
interval_min/max:16.5s / 28.7s
trigger_min/max:4.7s / 23.9s
trigger_pct:100.00%
duration_min/max:0.0s / 7.3s
uptime_min/max:7.64% / 13.01%
Stack Uptimes
glacial_spike_1:9.70%
Spelldata
id:1222865
name:Glacial Spike!
tooltip:Your {$?s431044=true}[Frostfire Bolt][Frostbolt] is replaced with Glacial Spike.
description:{$@spelldesc1246832=Frost crystallizes around you, generating an Icicle every {$=}{{$t1=6}}.1 sec. Upon generating {$s2=5} Icicles, {$?s431044=true}[Frostfire Bolt][Frostbolt] upgrades to Glacial Spike for its next cast.
{$@=}spellicon199786 {$@=}spellname199786
{$@spelldesc199786=Conjures a massive spike of ice that impales your target, dealing {$228600s1=0} damage and slowing the target's movement speed by {$205708s1=50}% for {$205708d=8 seconds}.
{$?a1280780=true}[|CFFffffffShatters {$1280780s1=5} {$=}lstack:stacks; of Freezing.|R][|CFFffffffApplies {$1246769s3=3} {$=}lstack:stacks; of Freezing.|R]}
Icicles generate more rapidly out of combat.}
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Hand of Frost	12.1	36.3	48.4	11.1s	6.1s	13.5s	54.44%	0.00%	0.0 (0.0)	11.5
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_hand_of_frost
max_stacks:100
base duration:8.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.02
activated:false
reactable:false
reverse:false
refresh behavior:duration
stack behavior:asynchronous
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 103.1s
trigger_min/max:0.0s / 72.2s
trigger_pct:99.65%
duration_min/max:0.0s / 63.5s
uptime_min/max:33.18% / 79.22%
Stack Uptimes
hand_of_frost_1:26.59%
hand_of_frost_2:8.32%
hand_of_frost_3:4.06%
hand_of_frost_4:8.55%
hand_of_frost_5:4.36%
hand_of_frost_6:1.72%
hand_of_frost_7:0.62%
hand_of_frost_8:0.18%
hand_of_frost_9:0.04%
hand_of_frost_10:0.01%
hand_of_frost_11:0.00%
hand_of_frost_12:0.00%
hand_of_frost_13:0.00%
Spelldata
id:1263263
name:Hand of Frost
tooltip:Spell damage is increased by {$s1=0}%.
description:{$@spelldesc1262981=Each stack of Freezing you Shatter increases your chance to summon a Hand of Frost by an additional {$=}{{$s1=10}/10}.1%.
Damage from Hand of Frost increases your spell damage by {$s2=1}% for {$1263263d=8 seconds}. Multiple applications may overlap.}
max_stacks:100
duration:8.00
cooldown:0.00
default_chance:101.00%
	Hasty Hunt	3.9	6.2	10.1	35.2s	12.9s	24.5s	31.42%	0.00%	6.2 (6.2)	3.5
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_hasty_hunt
max_stacks:1
base duration:15.00
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
Stat Details
stat:haste_rating
amount:85.00
Trigger Details
interval_min/max:15.0s / 184.2s
trigger_min/max:0.0s / 59.9s
trigger_pct:100.00%
duration_min/max:0.0s / 180.5s
uptime_min/max:0.00% / 91.45%
Stack Uptimes
hasty_hunt_1:31.42%
Spelldata
id:1252486
name:Hasty Hunt
tooltip:Haste increased by {$=}w1.
description:
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:101.00%
	Masterful Hunt	3.8	6.0	9.8	34.9s	12.9s	24.4s	30.56%	0.00%	6.0 (6.0)	3.4
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_masterful_hunt
max_stacks:1
base duration:15.00
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
Stat Details
stat:mastery_rating
amount:85.00
Trigger Details
interval_min/max:15.0s / 180.1s
trigger_min/max:0.0s / 55.1s
trigger_pct:100.00%
duration_min/max:0.0s / 178.7s
uptime_min/max:0.00% / 90.75%
Stack Uptimes
masterful_hunt_1:30.56%
Spelldata
id:1252488
name:Masterful Hunt
tooltip:Mastery increased by {$=}w1.
description:Increases Mastery by {$s1=0} for {$d=15 seconds}.
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:101.00%
	Nullsight	3.7	0.0	3.7	90.4s	90.4s	14.7s	18.41%	0.00%	0.0 (0.0)	3.6
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_nullsight
max_stacks:15
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:true
refresh behavior:tick
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Stat Details
stat:mastery_rating
amount:90.27
Trigger Details
interval_min/max:90.0s / 91.2s
trigger_min/max:90.0s / 91.2s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:16.56% / 21.04%
Stack Uptimes
nullsight_1:1.21%
nullsight_2:1.21%
nullsight_3:1.21%
nullsight_4:1.22%
nullsight_5:1.22%
nullsight_6:1.22%
nullsight_7:1.22%
nullsight_8:1.23%
nullsight_9:1.23%
nullsight_10:1.23%
nullsight_11:1.24%
nullsight_12:1.24%
nullsight_13:1.24%
nullsight_14:1.24%
nullsight_15:1.25%
Spelldata
id:1260459
name:Nullsight
tooltip:Mastery increased by {$=}w1. You can see invisible and stealthed enemies.
description:Seize the eye's draconic power, granting you {$1259293s1=755} Mastery diminishing over {$d=15 seconds} and allowing you to see hidden enemies.
max_stacks:0
duration:15.00
cooldown:90.00
default_chance:0.00%
	Overflowing Energy	26.6	25.1	51.7	10.8s	5.5s	6.1s	54.25%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_overflowing_energy
max_stacks:10
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.10
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.9s / 58.2s
trigger_min/max:0.0s / 50.3s
trigger_pct:100.00%
duration_min/max:0.0s / 40.0s
uptime_min/max:29.01% / 75.65%
Stack Uptimes
overflowing_energy_1:28.85%
overflowing_energy_2:14.85%
overflowing_energy_3:7.02%
overflowing_energy_4:2.64%
overflowing_energy_5:0.75%
overflowing_energy_6:0.14%
overflowing_energy_7:0.01%
Spelldata
id:394195
name:Overflowing Energy
tooltip:The critical strike chance of {$?a137021=false}[Arcane Barrage]?a137019[Fireball]?a137020[Frostbolt][Arcane Barrage, Fireball, or Frostbolt] is increased by {$?a137021=false}[{$s3=10}]?a137019[{$s1=20}]?a137020[{$s2=10}][{$s2=10}]%.
description:{$@spelldesc390218=Each time your {$?a137021=false}[Arcane Barrage]?a137019[Fireball]?a137020[Frostbolt][Arcane Barrage, Fireball, or Frostbolt] fails to critically strike, it gains {$?a137021=false}[{$394195s3=10}]?a137019[{$394195s1=20}]?a137020[{$394195s2=10}][{$394195s2=10}]% increased critical strike chance.
Critical strike bonus is removed when the affected spell critically strikes.}
max_stacks:10
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Permafrost Lances	5.3	0.0	5.3	60.9s	60.9s	14.7s	26.08%	0.00%	0.0 (0.0)	5.1
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_permafrost_lances
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.10
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:60.0s / 64.0s
trigger_min/max:60.0s / 64.0s
trigger_pct:100.00%
duration_min/max:1.6s / 15.0s
uptime_min/max:23.63% / 28.68%
Stack Uptimes
permafrost_lances_1:26.08%
Spelldata
id:455122
name:Permafrost Lances
tooltip:The damage of Ice Lance is increased by {$s1=10}%.
description:{$@spelldesc453720=Damage dealt by Fingers of Frost enhanced Ice Lances invoke a Frigid Pulse, dealing {$460623s1=0} Frost damage to nearby targets. Damage reduced beyond {$s1=8} targets.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Potion of Recklessness (Crit)	1.5	0.0	1.5	300.4s	0.0s	27.5s	13.45%	0.00%	0.0 (0.0)	1.2
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_potion_of_recklessness_Crit
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:300.00
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
amount:1725.00
Trigger Details
interval_min/max:300.0s / 301.2s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.97% / 18.18%
Stack Uptimes
potion_of_recklessness_Crit_1:13.45%
Spelldata
id:1236994
name:Potion of Recklessness
tooltip:Granting {$=}w1 {$?=}e1[Critical Strike]?e2[Haste]?e3[Versatility]?e4[Mastery][Highest secondary stat].
Reducing {$?=}e5[Critical Strike]?e6[Haste]?e7[Versatility]?e8[Mastery][lowest secondary stat] by {$=}w10.
description:Gain {$s2=935} of your highest secondary stat while losing {$s6=126} of your lowest secondary stat for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Potion of Recklessness (Vers Penalty)	1.5	0.0	1.5	300.4s	0.0s	27.5s	13.45%	0.00%	0.0 (0.0)	1.2
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_potion_of_recklessness_penalty_Vers
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:300.00
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
amount:-232.00
Trigger Details
interval_min/max:300.0s / 301.2s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.97% / 18.18%
Stack Uptimes
potion_of_recklessness_penalty_Vers_1:13.45%
Spelldata
id:1236994
name:Potion of Recklessness
tooltip:Granting {$=}w1 {$?=}e1[Critical Strike]?e2[Haste]?e3[Versatility]?e4[Mastery][Highest secondary stat].
Reducing {$?=}e5[Critical Strike]?e6[Haste]?e7[Versatility]?e8[Mastery][lowest secondary stat] by {$=}w10.
description:Gain {$s2=935} of your highest secondary stat while losing {$s6=126} of your lowest secondary stat for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Precision of the Dragonhawk	8.1	8.6	16.7	36.6s	17.0s	21.6s	58.44%	0.00%	8.6 (8.6)	7.5
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
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
interval_min/max:15.0s / 170.2s
trigger_min/max:0.0s / 70.7s
trigger_pct:100.00%
duration_min/max:0.0s / 145.7s
uptime_min/max:33.75% / 85.27%
Stack Uptimes
precision_of_the_dragonhawk_1:58.44%
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
	Thermal Void	33.0	0.6	33.7	9.0s	8.8s	1.8s	20.24%	38.45%	0.6 (0.6)	0.1
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_thermal_void
max_stacks:1
base duration:8.00
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
interval_min/max:1.8s / 62.1s
trigger_min/max:0.9s / 62.1s
trigger_pct:100.00%
duration_min/max:0.9s / 10.6s
uptime_min/max:10.74% / 36.37%
Stack Uptimes
thermal_void_1:20.24%
Spelldata
id:1247730
name:Thermal Void
tooltip:Your next Ice Lance will Shatter additional Freezing stacks.
description:{$@spelldesc1247729=Consuming Brain Freeze has a {$s1=100}% chance to cause your next Ice Lance to Shatter {$1246769s4=4} additional stacks of Freezing.}
max_stacks:0
duration:8.00
cooldown:0.00
default_chance:100.00%
	Versatile Hunt	1.0	1.5	2.5	34.8s	13.0s	24.2s	7.72%	0.00%	1.5 (1.5)	0.9
Buff Details
buff initial source:MID1_Mage_Frost_Frostfire
cooldown name:buff_versatile_hunt
max_stacks:1
base duration:15.00
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
Stat Details
stat:versatility_rating
amount:85.00
Trigger Details
interval_min/max:15.0s / 128.2s
trigger_min/max:0.0s / 51.3s
trigger_pct:100.00%
duration_min/max:0.0s / 113.0s
uptime_min/max:0.00% / 88.08%
Stack Uptimes
versatile_hunt_1:7.73%
Spelldata
id:1252489
name:Versatile Hunt
tooltip:Versatility increased by {$=}w1.
description:Increases Versatility by {$s1=0} for {$d=15 seconds}.
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:101.00%
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
	Brain Freeze	34.6	18.0	53.0	8.6s	0.0s	61.8s
	Brain Freeze from Frostbolt	25.0	12.0	41.0	11.1s	0.0s	98.4s
	Brain Freeze from Frozen Orb	5.3	4.0	6.0	60.9s	60.0s	64.0s
	Brain Freeze from Glacial Spike	4.3	0.0	11.0	59.0s	15.9s	323.2s
	Fingers of Frost	45.7	25.0	69.0	6.9s	0.0s	27.3s
	Fingers of Frost from Flurry	4.8	0.0	13.0	49.5s	0.9s	338.5s
	Fingers of Frost from Frostbolt	14.9	4.0	29.0	18.2s	0.0s	188.7s
	Fingers of Frost from Frozen Orb	5.3	4.0	6.0	60.9s	60.0s	64.0s
	Fingers of Frost from Frozen Orb Bolt	4.7	0.0	15.0	49.4s	0.5s	313.2s
	Fingers of Frost from Glacial Spike	16.0	11.0	24.0	22.9s	15.6s	29.4s
	Freezing applied	405.6	295.0	515.0	0.8s	0.0s	9.9s
	Freezing applied (Flurry)	191.4	120.0	272.0	1.6s	0.0s	28.2s
	Freezing applied (Frostfire Bolt)	114.4	75.0	161.0	3.5s	0.0s	33.4s
	Freezing applied (Hand of Frost)	48.5	30.0	73.0	6.0s	0.0s	72.2s
	Freezing applied (Ray of Frost)	51.3	40.0	56.0	5.4s	0.3s	76.5s
	Freezing overflow	7.0	0.0	23.0	22.1s	0.1s	298.7s
```

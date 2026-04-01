# MID1_Mage_Frost_Spellslinger — Buffs & Procs

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
	Alnscorned Essence	5.2	118.1	123.2	20.3s	2.1s	34.7s	59.86%	0.00%	0.0 (0.0)	4.5
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:0.7s / 251.7s
trigger_min/max:0.7s / 93.6s
trigger_pct:99.99%
duration_min/max:0.0s / 202.1s
uptime_min/max:25.04% / 97.18%
Stack Uptimes
alnscorned_essence_1:3.24%
alnscorned_essence_2:3.38%
alnscorned_essence_3:3.49%
alnscorned_essence_4:3.66%
alnscorned_essence_5:3.83%
alnscorned_essence_6:4.00%
alnscorned_essence_7:4.19%
alnscorned_essence_8:4.46%
alnscorned_essence_9:4.77%
alnscorned_essence_10:5.07%
alnscorned_essence_11:5.24%
alnscorned_essence_12:5.28%
alnscorned_essence_13:5.52%
alnscorned_essence_14:3.34%
alnscorned_essence_15:0.38%
alnscorned_essence_16:0.00%
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
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:12.0s / 142.6s
trigger_min/max:0.0s / 106.5s
trigger_pct:100.00%
duration_min/max:0.0s / 111.0s
uptime_min/max:13.21% / 75.13%
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
	Arcanoweave Insight	5.9	5.3	11.2	49.8s	24.8s	26.9s	52.89%	0.00%	5.3 (5.3)	5.3
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:20.0s / 181.6s
trigger_min/max:0.0s / 111.3s
trigger_pct:100.00%
duration_min/max:0.0s / 161.8s
uptime_min/max:22.78% / 87.53%
Stack Uptimes
arcanoweave_insight_1:52.89%
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
buff initial source:MID1_Mage_Frost_Spellslinger
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
	Brain Freeze	26.2	0.9	27.1	11.4s	11.1s	1.4s	12.41%	71.32%	0.9 (0.9)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
brain_freeze_1:12.41%
Spelldata
id:190446
name:Brain Freeze
tooltip:Your next Flurry deals {$s2=50}% increased damage.
description:{$@spelldesc190447={$?s431044=false}[Frostfire Bolt][Frostbolt] has a {$m1=25}% chance to reset the remaining cooldown on Flurry and cause your next Flurry to deal {$190446s2=50}% increased damage.}
max_stacks:1
duration:30.00
cooldown:0.00
default_chance:100.00%
	Brainstorm	16.6	10.0	26.5	13.8s	11.3s	10.5s	57.91%	0.00%	0.0 (0.0)	16.1
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:0.0s / 63.5s
trigger_min/max:0.0s / 40.3s
trigger_pct:98.02%
duration_min/max:0.4s / 49.5s
uptime_min/max:36.84% / 74.58%
Stack Uptimes
brainstorm_1:45.52%
brainstorm_2:11.20%
brainstorm_3:1.16%
brainstorm_4:0.02%
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
	Fingers of Frost	37.8	24.9	62.7	8.0s	4.8s	2.4s	29.25%	43.38%	3.3 (3.3)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:0.0s / 34.4s
trigger_min/max:0.0s / 27.5s
trigger_pct:13.62%
duration_min/max:0.0s / 18.7s
uptime_min/max:20.31% / 39.80%
Stack Uptimes
fingers_of_frost_1:23.60%
fingers_of_frost_2:5.65%
Spelldata
id:44544
name:Fingers of Frost
tooltip:Your next Ice Lance Shatters your target without removing any Freezing stacks.
description:{$@spelldesc112965={$?s431044=false}[Frostfire Bolt][Frostbolt] has a {$s1=15}% chance to grant a charge of Fingers of Frost.
Fingers of Frost causes your next Ice Lance to deal Shatter damage equal to {$1246769s4=4} stacks of Freezing and does not consume Freezing stacks.
Maximum {$44544u=2} {$=}Lcharge:charges;.}
max_stacks:2
duration:15.00
cooldown:0.00
default_chance:101.00%
	Glacial Spike!	13.4	0.4	13.8	23.2s	23.0s	2.3s	9.39%	0.00%	0.4 (0.4)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:14.8s / 34.2s
trigger_min/max:3.7s / 24.4s
trigger_pct:100.00%
duration_min/max:0.0s / 14.2s
uptime_min/max:6.64% / 15.53%
Stack Uptimes
glacial_spike_1:9.39%
Spelldata
id:1222865
name:Glacial Spike!
tooltip:Your {$?s431044=false}[Frostfire Bolt][Frostbolt] is replaced with Glacial Spike.
description:{$@spelldesc1246832=Frost crystallizes around you, generating an Icicle every {$=}{{$t1=6}}.1 sec. Upon generating {$s2=5} Icicles, {$?s431044=false}[Frostfire Bolt][Frostbolt] upgrades to Glacial Spike for its next cast.
{$@=}spellicon199786 {$@=}spellname199786
{$@spelldesc199786=Conjures a massive spike of ice that impales your target, dealing {$228600s1=0} damage and slowing the target's movement speed by {$205708s1=50}% for {$205708d=8 seconds}.
{$?a1280780=false}[|CFFffffffShatters {$1280780s1=5} {$=}lstack:stacks; of Freezing.|R][|CFFffffffApplies {$1246769s3=3} {$=}lstack:stacks; of Freezing.|R]}
Icicles generate more rapidly out of combat.}
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Hand of Frost	13.5	42.1	55.6	10.5s	5.3s	13.9s	62.63%	0.00%	0.0 (0.0)	12.8
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:0.6s / 109.5s
trigger_min/max:0.5s / 74.2s
trigger_pct:99.99%
duration_min/max:0.0s / 99.9s
uptime_min/max:38.17% / 84.28%
Stack Uptimes
hand_of_frost_1:27.86%
hand_of_frost_2:11.39%
hand_of_frost_3:5.55%
hand_of_frost_4:11.18%
hand_of_frost_5:5.30%
hand_of_frost_6:1.19%
hand_of_frost_7:0.15%
hand_of_frost_8:0.01%
hand_of_frost_9:0.00%
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
	Hasty Hunt	3.8	6.2	10.0	35.1s	12.9s	24.7s	31.31%	0.00%	6.2 (6.2)	3.5
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:15.0s / 243.1s
trigger_min/max:0.0s / 57.9s
trigger_pct:100.00%
duration_min/max:0.0s / 241.8s
uptime_min/max:0.00% / 92.17%
Stack Uptimes
hasty_hunt_1:31.31%
Spelldata
id:1252486
name:Hasty Hunt
tooltip:Haste increased by {$=}w1.
description:
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:101.00%
	Masterful Hunt	3.8	6.1	9.9	35.1s	13.0s	24.6s	31.18%	0.00%	6.1 (6.1)	3.5
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:15.0s / 189.2s
trigger_min/max:0.0s / 55.2s
trigger_pct:100.00%
duration_min/max:0.0s / 175.2s
uptime_min/max:0.00% / 91.88%
Stack Uptimes
masterful_hunt_1:31.18%
Spelldata
id:1252488
name:Masterful Hunt
tooltip:Mastery increased by {$=}w1.
description:Increases Mastery by {$s1=0} for {$d=15 seconds}.
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:101.00%
	Nullsight	3.7	0.0	3.7	92.8s	93.1s	14.7s	18.16%	0.00%	0.0 (0.0)	3.6
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:90.0s / 119.6s
trigger_min/max:90.0s / 119.6s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:15.66% / 20.91%
Stack Uptimes
nullsight_1:1.19%
nullsight_2:1.19%
nullsight_3:1.20%
nullsight_4:1.20%
nullsight_5:1.20%
nullsight_6:1.20%
nullsight_7:1.21%
nullsight_8:1.21%
nullsight_9:1.21%
nullsight_10:1.22%
nullsight_11:1.22%
nullsight_12:1.22%
nullsight_13:1.22%
nullsight_14:1.23%
nullsight_15:1.23%
Spelldata
id:1260459
name:Nullsight
tooltip:Mastery increased by {$=}w1. You can see invisible and stealthed enemies.
description:Seize the eye's draconic power, granting you {$1259293s1=755} Mastery diminishing over {$d=15 seconds} and allowing you to see hidden enemies.
max_stacks:0
duration:15.00
cooldown:90.00
default_chance:0.00%
	Overflowing Energy	12.4	11.5	24.0	23.1s	11.7s	13.1s	54.51%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:2.1s / 116.1s
trigger_min/max:1.0s / 95.1s
trigger_pct:100.00%
duration_min/max:0.1s / 81.7s
uptime_min/max:17.47% / 87.58%
Stack Uptimes
overflowing_energy_1:29.35%
overflowing_energy_2:15.07%
overflowing_energy_3:6.70%
overflowing_energy_4:2.54%
overflowing_energy_5:0.70%
overflowing_energy_6:0.13%
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
	Permafrost Lances	11.5	0.1	11.6	26.7s	26.4s	14.8s	56.84%	0.00%	0.1 (0.1)	11.0
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:15.0s / 48.2s
trigger_min/max:11.9s / 42.1s
trigger_pct:100.00%
duration_min/max:1.6s / 30.0s
uptime_min/max:51.71% / 63.97%
Stack Uptimes
permafrost_lances_1:56.84%
Spelldata
id:455122
name:Permafrost Lances
tooltip:The damage of Ice Lance is increased by {$s1=10}%.
description:{$@spelldesc453720=Damage dealt by Fingers of Frost enhanced Ice Lances invoke a Frigid Pulse, dealing {$460623s1=0} Frost damage to nearby targets. Damage reduced beyond {$s1=8} targets.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Potion of Recklessness (Crit)	1.5	0.0	1.5	304.5s	0.0s	27.6s	13.33%	0.00%	0.0 (0.0)	1.2
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:300.0s / 325.2s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:8.33% / 18.18%
Stack Uptimes
potion_of_recklessness_Crit_1:13.33%
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
	Potion of Recklessness (Mastery)	0.0	0.0	0.0	0.0s	0.0s	21.0s	0.13%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
cooldown name:buff_potion_of_recklessness_Mastery
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
stat:mastery_rating
amount:1725.00
Trigger Details
interval_min/max:0.0s / 0.0s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:1.4s / 30.0s
uptime_min/max:0.00% / 9.08%
Stack Uptimes
potion_of_recklessness_Mastery_1:0.13%
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
	Potion of Recklessness (Vers Penalty)	1.5	0.0	1.5	304.3s	0.0s	27.5s	13.45%	0.00%	0.0 (0.0)	1.2
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:300.0s / 325.2s
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
	Precision of the Dragonhawk	8.1	8.7	16.8	36.5s	17.0s	21.6s	58.35%	0.00%	8.7 (8.7)	7.5
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:15.0s / 159.7s
trigger_min/max:0.0s / 69.1s
trigger_pct:100.00%
duration_min/max:0.0s / 131.7s
uptime_min/max:30.91% / 84.36%
Stack Uptimes
precision_of_the_dragonhawk_1:58.35%
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
	Splinterstorm	8.1	0.0	8.1	39.8s	39.8s	9.9s	26.64%	0.00%	0.0 (0.0)	7.9
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
cooldown name:buff_splinterstorm
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
Trigger Details
interval_min/max:10.0s / 101.4s
trigger_min/max:3.4s / 101.4s
trigger_pct:100.00%
duration_min/max:0.0s / 20.0s
uptime_min/max:24.16% / 29.16%
Stack Uptimes
splinterstorm_1:26.64%
Spelldata
id:1247908
name:Splinterstorm
tooltip:Any time you would generates a Frost Splinter, you have a {$443783s2=100}% chance to generate an additional Frost Splinter.
description:{$@spelldesc443783={$?=}c1[Casting Arcane Surge generates {$s1=8} Arcane Splinters][Each time Ray of Frost damages one or more enemies, it generates {$s3=1} Frost {$=}LSplinter:Splinters;].
{$?=}c1[During Arcane Surge, your chance to conjure an additional Arcane Splinter is increased to {$s2=100}%][For {$1247908d=10 seconds} after casting Ray of Frost, your chance to conjure an additional Frost Splinter is increased to {$s2=100}%].}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Thermal Void	26.0	0.0	26.0	11.4s	11.4s	1.5s	12.59%	19.04%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:1.8s / 40.3s
trigger_min/max:0.9s / 40.3s
trigger_pct:100.00%
duration_min/max:0.9s / 8.0s
uptime_min/max:5.56% / 21.43%
Stack Uptimes
thermal_void_1:12.59%
Spelldata
id:1247730
name:Thermal Void
tooltip:Your next Ice Lance will Shatter additional Freezing stacks.
description:{$@spelldesc1247729=Consuming Brain Freeze has a {$s1=100}% chance to cause your next Ice Lance to Shatter {$1246769s4=4} additional stacks of Freezing.}
max_stacks:0
duration:8.00
cooldown:0.00
default_chance:100.00%
	Versatile Hunt	0.9	1.5	2.4	35.3s	13.1s	24.7s	7.64%	0.00%	1.5 (1.5)	0.8
Buff Details
buff initial source:MID1_Mage_Frost_Spellslinger
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
interval_min/max:15.0s / 162.5s
trigger_min/max:0.0s / 49.2s
trigger_pct:100.00%
duration_min/max:0.1s / 143.0s
uptime_min/max:0.00% / 89.55%
Stack Uptimes
versatile_hunt_1:7.64%
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
	Brain Freeze	27.1	13.0	41.0	11.0s	0.0s	40.3s
	Brain Freeze from Frostbolt	10.7	2.0	21.0	24.5s	1.1s	188.6s
	Brain Freeze from Frozen Orb	11.6	9.0	14.0	26.4s	11.9s	42.1s
	Brain Freeze from Glacial Spike	4.8	0.0	13.0	55.0s	16.2s	331.0s
	Fingers of Frost	62.7	42.0	88.0	5.0s	0.0s	27.5s
	Fingers of Frost from Flurry	3.7	0.0	13.0	57.4s	1.9s	332.2s
	Fingers of Frost from Frostbolt	5.5	0.0	15.0	42.6s	1.1s	291.1s
	Fingers of Frost from Frozen Orb	11.6	9.0	14.0	26.4s	11.9s	42.1s
	Fingers of Frost from Frozen Orb Bolt	10.2	1.0	23.0	26.5s	0.3s	277.4s
	Fingers of Frost from Glacial Spike	15.7	10.0	25.0	23.4s	16.0s	36.7s
	Fingers of Frost from Ray of Frost	16.0	14.0	19.0	18.8s	1.2s	99.8s
	Freezing applied	577.6	438.0	733.0	0.6s	0.0s	8.8s
	Freezing applied (Flurry)	145.7	88.0	208.0	2.0s	0.0s	29.9s
	Freezing applied (Frost Splinter)	206.2	134.0	289.0	1.4s	0.0s	31.6s
	Freezing applied (Frostbolt)	42.5	17.0	71.0	8.9s	1.1s	86.1s
	Freezing applied (Glacial Assault)	17.5	5.0	38.0	15.8s	0.0s	204.3s
	Freezing applied (Glacial Spike)	45.9	31.0	61.0	23.4s	16.0s	36.7s
	Freezing applied (Hand of Frost)	55.5	36.0	80.0	5.3s	0.5s	74.2s
	Freezing applied (Ray of Frost)	64.2	56.0	76.0	4.5s	0.3s	98.6s
	Freezing overflow	76.4	20.0	168.0	3.9s	0.0s	218.9s
```

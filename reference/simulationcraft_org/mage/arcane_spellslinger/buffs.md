# MID1_Mage_Arcane_Spellslinger — Buffs & Procs

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
	Alnscorned Essence	5.2	98.4	103.5	20.6s	2.6s	34.7s	59.99%	0.00%	0.0 (0.0)	4.6
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
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
interval_min/max:0.7s / 239.6s
trigger_min/max:0.7s / 101.3s
trigger_pct:99.99%
duration_min/max:0.0s / 202.6s
uptime_min/max:27.12% / 94.56%
Stack Uptimes
alnscorned_essence_1:3.91%
alnscorned_essence_2:4.13%
alnscorned_essence_3:4.37%
alnscorned_essence_4:4.61%
alnscorned_essence_5:4.88%
alnscorned_essence_6:5.17%
alnscorned_essence_7:5.61%
alnscorned_essence_8:6.49%
alnscorned_essence_9:7.07%
alnscorned_essence_10:6.04%
alnscorned_essence_11:3.90%
alnscorned_essence_12:2.17%
alnscorned_essence_13:1.15%
alnscorned_essence_14:0.43%
alnscorned_essence_15:0.06%
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
	Alnsight	7.4	3.8	11.1	39.1s	24.9s	15.8s	38.83%	0.00%	3.8 (3.8)	7.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
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
interval_min/max:12.0s / 143.4s
trigger_min/max:0.0s / 115.1s
trigger_pct:100.00%
duration_min/max:0.0s / 98.2s
uptime_min/max:14.47% / 74.46%
Stack Uptimes
alnsight_1:38.83%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Arcane Charge	49.9	386.3	436.2	6.1s	0.7s	5.4s	90.14%	0.00%	270.9 (411.7)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_arcane_charge
max_stacks:4
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.01
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:crit
amount:1.00%
Trigger Details
interval_min/max:0.3s / 19.0s
trigger_min/max:0.0s / 9.1s
trigger_pct:100.00%
duration_min/max:0.0s / 17.9s
uptime_min/max:82.27% / 94.06%
Stack Uptimes
arcane_charge_1:16.11%
arcane_charge_2:3.24%
arcane_charge_3:7.61%
arcane_charge_4:63.17%
Spelldata
id:36032
name:Arcane Charge
tooltip:Increases the damage of Arcane Blast, Arcane Missiles, Arcane Explosion, and Arcane Barrage by {$36032=}w1%.
Increases the mana cost of Arcane Blast by {$36032=}w2%{$?=}{{$=}w5<0}[, and reduces the cast time of Arcane Blast by {$=}w5%.][.]
Increases the number of targets hit by Arcane Barrage for 50% damage by {$36032=}w3.
description:$@spelldesc114664
max_stacks:4
duration:-0.00
cooldown:0.00
default_chance:100.00%
	Arcane Salvo	50.5	623.2	673.6	6.0s	0.4s	5.9s	98.85%	0.00%	109.2 (168.1)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_arcane_salvo
max_stacks:20
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.07
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 18.7s
trigger_min/max:0.0s / 4.3s
trigger_pct:100.00%
duration_min/max:0.0s / 18.7s
uptime_min/max:95.74% / 100.00%
Stack Uptimes
arcane_salvo_1:0.34%
arcane_salvo_2:0.29%
arcane_salvo_3:0.25%
arcane_salvo_4:0.77%
arcane_salvo_5:14.96%
arcane_salvo_6:3.80%
arcane_salvo_7:3.73%
arcane_salvo_8:3.63%
arcane_salvo_9:3.57%
arcane_salvo_10:3.52%
arcane_salvo_11:4.31%
arcane_salvo_12:5.69%
arcane_salvo_13:6.42%
arcane_salvo_14:6.46%
arcane_salvo_15:6.30%
arcane_salvo_16:6.36%
arcane_salvo_17:6.36%
arcane_salvo_18:6.35%
arcane_salvo_19:6.30%
arcane_salvo_20:9.44%
Spelldata
id:1242974
name:Arcane Salvo
tooltip:Increases the damage of your next Arcane Barrage by {$s1=3}%.{$?a384858=true}[
Arcane Barrage has a {$=}{{$s2=1}*{$384858s1=4} }% chance to also fire an Arcane Orb.][]
description:{$@spelldesc384452=Each wave of Arcane Missiles increases the damage of Arcane Barrage by {$1242974s1=3}%, up to {$=}{{$1242974s1=3}*{$1242974u=20}}%.}
max_stacks:20
duration:-0.00
cooldown:0.00
default_chance:100.00%
	Arcane Surge	3.6	0.0	3.6	94.1s	94.1s	14.9s	17.75%	0.00%	0.0 (0.0)	3.5
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_arcane_surge
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.35
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:92.1s / 101.5s
trigger_min/max:92.1s / 101.5s
trigger_pct:100.00%
duration_min/max:0.4s / 15.0s
uptime_min/max:14.72% / 20.51%
Stack Uptimes
arcane_surge_1:17.75%
Spelldata
id:365362
name:Arcane Surge
tooltip:Spell damage increased by {$=}w1% and Mana Regeneration increase {$=}w3%.{$?a443783=true}[
You have a {$443783s2=100}% to conjure an additional Arcane Splinter.][]
description:{$@spelldesc365350=Expend all of your current mana to annihilate your enemy target and nearby enemies for up to {$?a457521=true}[{$=}{{$s1=0 + 372.0%}*{$s2=2}*({$457521s1=50}/100+1)}][{$=}{{$s1=0 + 372.0%}*{$s2=2}}] Arcane damage based on Mana spent. Deals reduced damage beyond {$s3=8} targets.
For the next {$365362d=15 seconds}, your Mana regeneration is increased by {$365362s3=425}% and spell damage is increased by {$365362s1=35}%.
|cFFFFFFFFGenerates Clearcasting.|r}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Arcanoweave Audacity	7.0	14.7	21.7	44.6s	14.1s	30.5s	71.00%	0.00%	14.7 (14.7)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_arcanoweave_audacity
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
Stat Details
stat:crit_rating
amount:155.10
Trigger Details
interval_min/max:4.7s / 263.4s
trigger_min/max:0.1s / 93.8s
trigger_pct:100.00%
duration_min/max:0.0s / 253.6s
uptime_min/max:35.59% / 97.08%
Stack Uptimes
arcanoweave_audacity_1:71.00%
Spelldata
id:1241289
name:Arcanoweave Audacity
tooltip:Critical Strike increased by {$=}w1.
description:{$@spelldesc1241262=Gain {$1241289s1=103} Critical Strike while above {$s1=80}% health.}
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:0.00%
	Berserking	2.0	0.0	2.0	188.2s	188.2s	12.0s	8.11%	0.00%	0.0 (0.0)	2.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_berserking
max_stacks:1
base duration:12.00
duration modifier:1.00
base cooldown:180.00
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
interval_min/max:183.4s / 198.7s
trigger_min/max:183.4s / 198.7s
trigger_pct:100.00%
duration_min/max:12.0s / 12.0s
uptime_min/max:6.67% / 10.00%
Stack Uptimes
berserking_1:8.11%
Spelldata
id:26297
name:Berserking
tooltip:Haste increased by {$s1=10}%.
description:Increases your haste by {$s1=10}% for {$d=12 seconds}.
max_stacks:0
duration:12.00
cooldown:180.00
default_chance:0.00%
	Bloodlust	1.0	0.0	1.0	0.0s	0.0s	40.0s	13.52%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
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
	Brainstorm	17.5	21.9	39.5	12.0s	7.6s	12.7s	73.87%	0.00%	0.0 (0.0)	16.8
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
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
interval_min/max:0.0s / 92.5s
trigger_min/max:0.0s / 33.7s
trigger_pct:95.60%
duration_min/max:0.0s / 88.5s
uptime_min/max:59.99% / 89.23%
Stack Uptimes
brainstorm_1:48.41%
brainstorm_2:17.38%
brainstorm_3:6.96%
brainstorm_4:1.06%
brainstorm_5:0.07%
Spelldata
id:461531
name:Brainstorm
tooltip:Your Intellect is increased by {$=}{{$s1=1}}.1%.
description:{$@spelldesc461261=Gaining {$?a137021=true}[Clearcasting]?a137020[Brain Freeze][Hot Streak] increases your Intellect by {$461531s1=1}% for {$461531d=8 seconds}. Multiple instances may overlap.}
max_stacks:5
duration:8.00
cooldown:0.00
default_chance:101.00%
	Clearcasting	13.0	28.2	41.3	22.7s	7.2s	16.8s	72.92%	0.00%	6.0 (6.0)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_clearcasting
max_stacks:3
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-1.00
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.3s / 233.6s
trigger_min/max:0.0s / 33.7s
trigger_pct:100.00%
duration_min/max:0.0s / 228.6s
uptime_min/max:41.55% / 95.32%
Stack Uptimes
clearcasting_1:36.06%
clearcasting_2:28.11%
clearcasting_3:8.76%
Spelldata
id:263725
name:Clearcasting
tooltip:You can now cast Arcane Missiles.
description:{$@spelldesc79684=Casting Arcane spells has a {$s2=10}% chance to grant access to Arcane Missiles or make your next Arcane Explosion free.}
max_stacks:3
duration:30.00
cooldown:0.00
default_chance:100.00%
	Intuition	46.6	0.0	46.6	6.3s	6.3s	0.6s	9.44%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_intuition
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.25
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.9s / 46.2s
trigger_min/max:0.9s / 46.2s
trigger_pct:100.00%
duration_min/max:0.0s / 9.1s
uptime_min/max:4.27% / 16.26%
Stack Uptimes
intuition_1:9.44%
Spelldata
id:1223797
name:Intuition
tooltip:Your next Arcane Barrage deals {$s1=25}% increased damage.
description:{$@spelldesc453724=Damage dealt by Arcane Orb and Arcane Missiles increased by {$s1=10}%.}
max_stacks:1
duration:10.00
cooldown:0.00
default_chance:100.00%
	Light's Potential	1.4	0.0	1.4	303.8s	304.6s	27.9s	13.07%	0.00%	0.0 (0.0)	1.1
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
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
interval_min/max:300.0s / 323.7s
trigger_min/max:300.0s / 323.7s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.69% / 18.18%
Stack Uptimes
lights_potential_1:13.07%
Spelldata
id:1236616
name:Light's Potential
tooltip:Primary stat increased by {$=}w1.
description:Drink to increase your primary stat by {$s1=365} for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Might of the Void	8.2	8.5	16.7	36.2s	17.1s	21.5s	58.68%	0.00%	8.5 (8.5)	7.6
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_might_of_the_void
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
stat:intellect
amount:66.80
Trigger Details
interval_min/max:15.0s / 145.7s
trigger_min/max:0.0s / 71.9s
trigger_pct:100.00%
duration_min/max:0.0s / 132.5s
uptime_min/max:34.67% / 89.12%
Stack Uptimes
might_of_the_void_1:58.68%
Spelldata
id:1241715
name:Might of the Void
tooltip:Wielding a wisp the Void's power, increasing your {$=}pri by {$=}w1.
description:{$@spelldesc1236095=Permanently enchants a weapon with Acuity of the Ren'dorei, causing your spells and abilities to grant you Might of the Void, providing you with {$=}ec1s1 {$=}pri for {$1241715d=15 seconds}. Cannot be applied to items lower than level {$=}ecim.
|cnNORMAL_FONT_COLOR:Thalassian Talents - Silvermoon's Spellpower|R }
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Nullsight	3.6	0.0	3.6	94.0s	94.0s	14.9s	17.83%	0.00%	0.0 (0.0)	3.5
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
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
interval_min/max:90.0s / 100.3s
trigger_min/max:90.0s / 100.3s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:15.41% / 20.54%
Stack Uptimes
nullsight_1:1.18%
nullsight_2:1.18%
nullsight_3:1.18%
nullsight_4:1.19%
nullsight_5:1.19%
nullsight_6:1.19%
nullsight_7:1.19%
nullsight_8:1.19%
nullsight_9:1.19%
nullsight_10:1.19%
nullsight_11:1.19%
nullsight_12:1.19%
nullsight_13:1.19%
nullsight_14:1.20%
nullsight_15:1.20%
Spelldata
id:1260459
name:Nullsight
tooltip:Mastery increased by {$=}w1. You can see invisible and stealthed enemies.
description:Seize the eye's draconic power, granting you {$1259293s1=755} Mastery diminishing over {$d=15 seconds} and allowing you to see hidden enemies.
max_stacks:0
duration:15.00
cooldown:90.00
default_chance:0.00%
	Overflowing Energy	14.2	17.5	31.7	21.3s	9.4s	12.9s	61.26%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
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
interval_min/max:2.5s / 85.5s
trigger_min/max:1.2s / 64.6s
trigger_pct:100.00%
duration_min/max:0.0s / 62.4s
uptime_min/max:37.68% / 78.26%
Stack Uptimes
overflowing_energy_1:27.26%
overflowing_energy_2:17.77%
overflowing_energy_3:9.78%
overflowing_energy_4:4.43%
overflowing_energy_5:1.57%
overflowing_energy_6:0.41%
overflowing_energy_7:0.06%
overflowing_energy_8:0.00%
Spelldata
id:394195
name:Overflowing Energy
tooltip:The critical strike chance of {$?a137021=true}[Arcane Barrage]?a137019[Fireball]?a137020[Frostbolt][Arcane Barrage, Fireball, or Frostbolt] is increased by {$?a137021=true}[{$s3=10}]?a137019[{$s1=20}]?a137020[{$s2=10}][{$s2=10}]%.
description:{$@spelldesc390218=Each time your {$?a137021=true}[Arcane Barrage]?a137019[Fireball]?a137020[Frostbolt][Arcane Barrage, Fireball, or Frostbolt] fails to critically strike, it gains {$?a137021=true}[{$394195s3=10}]?a137019[{$394195s1=20}]?a137020[{$394195s2=10}][{$394195s2=10}]% increased critical strike chance.
Critical strike bonus is removed when the affected spell critically strikes.}
max_stacks:10
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Presence of Mind	5.6	0.0	5.6	55.9s	55.9s	2.7s	5.12%	7.11%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Spellslinger
cooldown name:buff_presence_of_mind
max_stacks:2
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
interval_min/max:46.2s / 105.9s
trigger_min/max:46.2s / 105.9s
trigger_pct:100.00%
duration_min/max:0.0s / 9.9s
uptime_min/max:3.06% / 9.35%
Stack Uptimes
presence_of_mind_1:2.40%
presence_of_mind_2:2.72%
Spelldata
id:205025
name:Presence of Mind
tooltip:Arcane Blast is instant cast.
description:Causes your next {$=}n Arcane {$=}LBlast:Blasts; to be instant cast{$?a134735=false}[ and deal {$s2=100}% of normal damage][].
max_stacks:0
duration:-0.00
cooldown:45.00
default_chance:100.00%
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
	Arcane Salvo applied	1147.1	858.0	1442.0	0.5s	0.0s	4.3s
	Arcane Salvo applied (Arcane Barrage)	227.6	160.0	300.0	6.4s	1.7s	53.7s
	Arcane Salvo applied (Arcane Blast)	306.3	236.0	376.0	2.0s	0.9s	15.4s
	Arcane Salvo applied (Arcane Missiles)	9.3	0.0	49.0	5.2s	0.2s	286.0s
	Arcane Salvo applied (Arcane Orb)	276.4	198.0	356.0	2.2s	0.1s	29.1s
	Arcane Salvo applied (Arcane Splinter)	327.5	218.0	459.0	0.9s	0.0s	23.0s
	Arcane Salvo overflow	168.1	103.0	265.0	2.7s	0.0s	54.1s
```

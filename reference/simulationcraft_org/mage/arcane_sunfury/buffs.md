# MID1_Mage_Arcane_Sunfury — Buffs & Procs

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
	Alnscorned Essence	5.2	108.6	113.8	20.0s	2.3s	34.3s	59.42%	0.00%	0.0 (0.0)	4.6
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:0.7s / 234.5s
trigger_min/max:0.7s / 99.1s
trigger_pct:99.99%
duration_min/max:0.0s / 206.7s
uptime_min/max:26.28% / 92.84%
Stack Uptimes
alnscorned_essence_1:3.51%
alnscorned_essence_2:3.60%
alnscorned_essence_3:3.78%
alnscorned_essence_4:3.96%
alnscorned_essence_5:4.15%
alnscorned_essence_6:4.35%
alnscorned_essence_7:4.59%
alnscorned_essence_8:4.88%
alnscorned_essence_9:5.37%
alnscorned_essence_10:6.34%
alnscorned_essence_11:6.34%
alnscorned_essence_12:4.68%
alnscorned_essence_13:2.80%
alnscorned_essence_14:0.95%
alnscorned_essence_15:0.12%
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
	Alnsight	7.3	3.8	11.1	39.4s	25.0s	15.8s	38.54%	0.00%	3.8 (3.8)	6.9
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:12.0s / 150.2s
trigger_min/max:0.0s / 111.2s
trigger_pct:100.00%
duration_min/max:0.0s / 106.5s
uptime_min/max:14.23% / 72.35%
Stack Uptimes
alnsight_1:38.54%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Arcane Charge	52.6	371.7	424.3	5.7s	0.7s	5.3s	92.75%	0.00%	268.8 (384.8)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:0.0s / 25.6s
trigger_min/max:0.0s / 8.3s
trigger_pct:100.00%
duration_min/max:0.0s / 25.2s
uptime_min/max:87.77% / 95.82%
Stack Uptimes
arcane_charge_1:12.25%
arcane_charge_2:7.20%
arcane_charge_3:9.89%
arcane_charge_4:63.40%
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
	Arcane Salvo	38.4	608.8	647.2	7.8s	0.5s	6.6s	84.06%	0.00%	95.6 (205.1)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_arcane_salvo
max_stacks:25
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
interval_min/max:1.2s / 25.6s
trigger_min/max:0.0s / 4.8s
trigger_pct:100.00%
duration_min/max:0.0s / 24.4s
uptime_min/max:79.43% / 87.37%
Stack Uptimes
arcane_salvo_1:1.86%
arcane_salvo_2:6.67%
arcane_salvo_3:2.01%
arcane_salvo_4:4.63%
arcane_salvo_5:2.02%
arcane_salvo_6:2.00%
arcane_salvo_7:5.09%
arcane_salvo_8:2.69%
arcane_salvo_9:4.45%
arcane_salvo_10:1.61%
arcane_salvo_11:3.68%
arcane_salvo_12:2.32%
arcane_salvo_13:3.29%
arcane_salvo_14:3.19%
arcane_salvo_15:2.51%
arcane_salvo_16:3.63%
arcane_salvo_17:2.55%
arcane_salvo_18:2.31%
arcane_salvo_19:2.23%
arcane_salvo_20:3.10%
arcane_salvo_21:3.68%
arcane_salvo_22:1.70%
arcane_salvo_23:2.75%
arcane_salvo_24:2.34%
arcane_salvo_25:11.73%
Spelldata
id:1242974
name:Arcane Salvo
tooltip:Increases the damage of your next Arcane Barrage by {$s1=3}%.{$?a384858=true}[
Arcane Barrage has a {$=}{{$s2=1}*{$384858s1=4} }% chance to also fire an Arcane Orb.][]
description:{$@spelldesc384452=Each wave of Arcane Missiles increases the damage of Arcane Barrage by {$1242974s1=3}%, up to {$=}{{$1242974s1=3}*{$1242974u=20}}%.}
max_stacks:25
duration:-0.00
cooldown:0.00
default_chance:100.00%
	Arcane Soul	3.7	0.0	3.7	92.1s	92.1s	4.0s	4.70%	0.00%	0.0 (0.0)	3.5
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_arcane_soul
max_stacks:1
base duration:3.00
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
interval_min/max:75.3s / 97.1s
trigger_min/max:75.3s / 97.1s
trigger_pct:100.00%
duration_min/max:0.0s / 4.0s
uptime_min/max:4.03% / 5.38%
Stack Uptimes
arcane_soul_1:4.70%
Spelldata
id:451038
name:Arcane Soul
tooltip:Arcane Barrage grants Clearcasting, {$s2=5} stacks of Arcane Salvo, and generates {$s1=4} Arcane Charges.
description:Arcane Barrage grants Clearcasting and generates {$s1=4} Arcane Charges.
Each cast of Arcane Barrage grants {$s2=5} stacks of Arcane Salvo and casting Arcane Barrage does not consume Arcane Salvo.
max_stacks:0
duration:3.00
cooldown:0.00
default_chance:100.00%
	Arcane Surge	3.7	0.0	3.7	92.5s	92.5s	16.7s	20.49%	0.00%	0.0 (0.0)	3.5
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:92.0s / 97.1s
trigger_min/max:92.0s / 97.0s
trigger_pct:100.00%
duration_min/max:0.4s / 17.0s
uptime_min/max:17.99% / 23.16%
Stack Uptimes
arcane_surge_1:20.49%
Spelldata
id:365362
name:Arcane Surge
tooltip:Spell damage increased by {$=}w1% and Mana Regeneration increase {$=}w3%.{$?a443783=false}[
You have a {$443783s2=100}% to conjure an additional Arcane Splinter.][]
description:{$@spelldesc365350=Expend all of your current mana to annihilate your enemy target and nearby enemies for up to {$?a457521=true}[{$=}{{$s1=0 + 372.0%}*{$s2=2}*({$457521s1=50}/100+1)}][{$=}{{$s1=0 + 372.0%}*{$s2=2}}] Arcane damage based on Mana spent. Deals reduced damage beyond {$s3=8} targets.
For the next {$365362d=15 seconds}, your Mana regeneration is increased by {$365362s3=425}% and spell damage is increased by {$365362s1=35}%.
|cFFFFFFFFGenerates Clearcasting.|r}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Arcanoweave Audacity	7.0	14.7	21.7	44.5s	14.0s	30.4s	70.97%	0.00%	14.7 (14.7)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:7.5s / 261.6s
trigger_min/max:0.1s / 111.9s
trigger_pct:100.00%
duration_min/max:0.0s / 257.8s
uptime_min/max:35.50% / 100.00%
Stack Uptimes
arcanoweave_audacity_1:70.97%
Spelldata
id:1241289
name:Arcanoweave Audacity
tooltip:Critical Strike increased by {$=}w1.
description:{$@spelldesc1241262=Gain {$1241289s1=103} Critical Strike while above {$s1=80}% health.}
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:0.00%
	Bloodlust	1.0	0.0	1.0	0.0s	0.0s	40.0s	13.52%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
	Brainstorm	15.2	46.5	61.7	14.4s	4.8s	16.0s	81.21%	0.00%	4.6 (4.7)	12.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:0.0s / 116.8s
trigger_min/max:0.0s / 31.2s
trigger_pct:95.80%
duration_min/max:0.0s / 105.4s
uptime_min/max:65.91% / 93.27%
Stack Uptimes
brainstorm_1:39.42%
brainstorm_2:23.14%
brainstorm_3:9.76%
brainstorm_4:5.30%
brainstorm_5:3.59%
Spelldata
id:461531
name:Brainstorm
tooltip:Your Intellect is increased by {$=}{{$s1=1}}.1%.
description:{$@spelldesc461261=Gaining {$?a137021=true}[Clearcasting]?a137020[Brain Freeze][Hot Streak] increases your Intellect by {$461531s1=1}% for {$461531d=8 seconds}. Multiple instances may overlap.}
max_stacks:5
duration:8.00
cooldown:0.00
default_chance:101.00%
	Clearcasting	31.3	33.1	64.4	9.7s	4.6s	4.8s	50.08%	0.00%	8.3 (8.3)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_clearcasting
max_stacks:3
base duration:20.00
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
interval_min/max:0.1s / 65.8s
trigger_min/max:0.0s / 31.2s
trigger_pct:100.00%
duration_min/max:0.0s / 57.3s
uptime_min/max:31.59% / 71.52%
Stack Uptimes
clearcasting_1:31.58%
clearcasting_2:12.00%
clearcasting_3:6.51%
Spelldata
id:263725
name:Clearcasting
tooltip:You can now cast Arcane Missiles.
description:{$@spelldesc79684=Casting Arcane spells has a {$s2=10}% chance to grant access to Arcane Missiles or make your next Arcane Explosion free.}
max_stacks:3
duration:20.00
cooldown:0.00
default_chance:100.00%
	Entropic Embrace	5.6	1.6	7.2	49.4s	36.8s	13.4s	25.08%	0.00%	1.6 (1.6)	5.4
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_entropic_embrace
max_stacks:1
base duration:12.00
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
interval_min/max:12.0s / 169.1s
trigger_min/max:0.0s / 162.9s
trigger_pct:100.00%
duration_min/max:0.0s / 58.9s
uptime_min/max:4.80% / 59.39%
Stack Uptimes
entropic_embrace_1:25.08%
Spelldata
id:256374
name:Entropic Embrace
tooltip:Damage and healing increased by {$=}w1%.
description:{$@spelldesc255669=Your abilities have a chance to empower you with the essence of the Void, causing your damage and healing effects to deal an additional {$256374s1=5}% as Shadowfrost for {$256374d=12 seconds}.
{$?a1232189=false}[Within Voidstorm, Entropic Embrace's duration is doubled.][]}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:0.00%
	Intuition	26.7	0.0	26.7	11.0s	11.0s	1.0s	8.46%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:2.0s / 71.8s
trigger_min/max:2.0s / 71.8s
trigger_pct:100.00%
duration_min/max:0.0s / 10.0s
uptime_min/max:0.83% / 19.43%
Stack Uptimes
intuition_1:8.46%
Spelldata
id:1223797
name:Intuition
tooltip:Your next Arcane Barrage deals {$s1=25}% increased damage.
description:{$@spelldesc453724=Damage dealt by Arcane Orb and Arcane Missiles increased by {$s1=10}%.}
max_stacks:1
duration:10.00
cooldown:0.00
default_chance:100.00%
	Lesser Time Warp	3.7	0.0	3.7	92.1s	92.1s	6.0s	7.03%	0.00%	0.0 (0.0)	3.5
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_lesser_time_warp
max_stacks:1
base duration:6.00
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
Stat Details
stat:haste
amount:15.00%
Trigger Details
interval_min/max:75.3s / 97.1s
trigger_min/max:75.3s / 97.1s
trigger_pct:100.00%
duration_min/max:0.0s / 6.0s
uptime_min/max:6.05% / 8.02%
Stack Uptimes
lesser_time_warp_1:7.03%
Spelldata
id:1260277
name:Lesser Time Warp
tooltip:Haste increased by {$?=}c1[{$=}w1][{$=}w2]%.
description:Warp the flow of time, increasing your haste by {$s1=15}%.
max_stacks:0
duration:6.00
cooldown:0.00
default_chance:0.00%
	Light's Potential	1.5	0.0	1.5	306.9s	0.0s	26.1s	12.87%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:298.0s / 331.6s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.32% / 17.67%
Stack Uptimes
lights_potential_1:12.87%
Spelldata
id:1236616
name:Light's Potential
tooltip:Primary stat increased by {$=}w1.
description:Drink to increase your primary stat by {$s1=365} for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Mana Cascade	4.5	216.3	220.7	41.6s	1.4s	66.5s	99.08%	0.00%	20.5 (34.1)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_mana_cascade
max_stacks:10
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.01
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:asynchronous
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste
amount:0.50%
Trigger Details
interval_min/max:0.0s / 217.6s
trigger_min/max:0.0s / 5.4s
trigger_pct:100.00%
duration_min/max:0.0s / 216.4s
uptime_min/max:97.51% / 99.99%
Stack Uptimes
mana_cascade_1:2.27%
mana_cascade_2:2.88%
mana_cascade_3:3.22%
mana_cascade_4:5.28%
mana_cascade_5:9.71%
mana_cascade_6:19.77%
mana_cascade_7:19.35%
mana_cascade_8:18.92%
mana_cascade_9:8.31%
mana_cascade_10:9.37%
Spelldata
id:449322
name:Mana Cascade
tooltip:Haste increased by {$=}{{$s2=5}/10}.1%.
description:{$@spelldesc449293={$?=}c1[Casting Arcane Blast or Arcane Barrage][Consuming Hot Streak] grants you {$?=}c1[{$=}{{$449322s2=5}/10}.1][{$=}{{$449314s2=5}/10}.1]% Haste for {$449322d=10 seconds}1. Stacks up to {$449314u=10} times. Multiple instances may overlap.}
max_stacks:10
duration:10.00
cooldown:0.00
default_chance:101.00%
	Might of the Void	8.1	8.6	16.7	36.5s	17.0s	21.6s	58.49%	0.00%	8.6 (8.6)	7.5
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:15.0s / 146.2s
trigger_min/max:0.0s / 71.2s
trigger_pct:100.00%
duration_min/max:0.0s / 128.0s
uptime_min/max:37.31% / 85.95%
Stack Uptimes
might_of_the_void_1:58.49%
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
	Nullsight	3.6	0.0	3.6	92.6s	92.6s	14.7s	17.82%	0.00%	0.0 (0.0)	3.5
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:90.0s / 97.9s
trigger_min/max:90.0s / 97.9s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:15.66% / 20.10%
Stack Uptimes
nullsight_1:1.17%
nullsight_2:1.17%
nullsight_3:1.17%
nullsight_4:1.18%
nullsight_5:1.18%
nullsight_6:1.18%
nullsight_7:1.19%
nullsight_8:1.19%
nullsight_9:1.19%
nullsight_10:1.19%
nullsight_11:1.20%
nullsight_12:1.20%
nullsight_13:1.20%
nullsight_14:1.21%
nullsight_15:1.21%
Spelldata
id:1260459
name:Nullsight
tooltip:Mastery increased by {$=}w1. You can see invisible and stealthed enemies.
description:Seize the eye's draconic power, granting you {$1259293s1=755} Mastery diminishing over {$d=15 seconds} and allowing you to see hidden enemies.
max_stacks:0
duration:15.00
cooldown:90.00
default_chance:0.00%
	Overflowing Energy	15.3	18.7	34.0	20.1s	8.9s	12.5s	63.69%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
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
interval_min/max:1.6s / 85.8s
trigger_min/max:0.8s / 75.7s
trigger_pct:100.00%
duration_min/max:0.0s / 83.2s
uptime_min/max:39.46% / 82.95%
Stack Uptimes
overflowing_energy_1:29.49%
overflowing_energy_2:18.12%
overflowing_energy_3:9.75%
overflowing_energy_4:4.36%
overflowing_energy_5:1.51%
overflowing_energy_6:0.40%
overflowing_energy_7:0.07%
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
	Overpowered Missiles	13.9	1.9	15.9	20.7s	18.1s	3.9s	18.27%	0.00%	1.9 (1.9)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_overpowered_missiles
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:1.00
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:1.2s / 207.7s
trigger_min/max:0.0s / 207.7s
trigger_pct:100.00%
duration_min/max:0.0s / 22.3s
uptime_min/max:3.20% / 37.75%
Stack Uptimes
overpowered_missiles_1:18.27%
Spelldata
id:1277009
name:Overpowered Missiles
tooltip:Arcane Missiles damage increased by {$s1=100}%, fires at up to additional {$=}{{$s2=3}-1} nearby targets, and generates maximum Arcane Salvo stacks.
description:{$@spelldesc1244329=Gaining Clearcasting has a {$s1=25}% chance to cause your next Arcane Missiles to be Overpowered, causing it to deal {$1277009s1=100}% increased damage, generate maximum stacks of Arcane Salvo, and strike {$1277009s2=3} additional {$=}Ltarget:targets; at {$1243307s1=50}% effectiveness.}
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:0.00%
	Spellfire Sphere	4.6	22.5	27.1	68.6s	11.4s	76.2s	92.67%	0.00%	8.9 (8.9)	0.0
Buff Details
buff initial source:MID1_Mage_Arcane_Sunfury
cooldown name:buff_spellfire_sphere
max_stacks:5
base duration:604800.00
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
Trigger Details
interval_min/max:0.0s / 108.2s
trigger_min/max:0.0s / 21.5s
trigger_pct:100.00%
duration_min/max:0.0s / 96.9s
uptime_min/max:84.60% / 100.00%
Stack Uptimes
spellfire_sphere_1:12.09%
spellfire_sphere_2:12.62%
spellfire_sphere_3:13.07%
spellfire_sphere_4:12.33%
spellfire_sphere_5:42.55%
Spelldata
id:448604
name:Spellfire Sphere
tooltip:Spell damage increased by {$=}W1%.
description:Increases your spell damage by {$?=}c1[{$=}{{$s1=1}}.1][{$=}{{$s2=1}}.1]%. Stacks up to {$u=5} times.
max_stacks:5
duration:604800.00
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
	Arcane Salvo applied	1036.1	690.0	1446.0	0.6s	0.0s	4.8s
	Arcane Salvo applied (Arcane Blast)	216.2	146.0	286.0	2.7s	0.8s	41.5s
	Arcane Salvo applied (Arcane Missiles)	386.4	238.0	595.0	0.8s	0.0s	29.0s
	Arcane Salvo applied (Arcane Orb)	102.8	68.0	142.0	5.7s	0.8s	47.2s
	Arcane Salvo applied (Arcane Soul)	67.0	40.0	85.0	19.1s	0.8s	95.4s
	Arcane Salvo applied (Overpowered Missiles)	263.6	72.0	510.0	3.2s	0.1s	198.4s
	Arcane Salvo overflow	205.1	89.0	376.0	3.8s	0.0s	74.0s
```

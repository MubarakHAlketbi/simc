# MID1_Rogue_Outlaw_Trickster — Buffs & Procs

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
	Acrobatic Strikes	6.5	663.4	669.9	49.4s	0.4s	45.8s	99.07%	100.00%	605.4 (605.4)	5.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_acrobatic_strikes
max_stacks:10
base duration:3.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.01
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Damage Modifiers
direct:1.00 + 0.00/stack
periodic:1.00 + 0.00/stack
auto_attack:1.00 + 0.03/stack
crit_chance:1.00
is_stacking:true
Trigger Details
interval_min/max:3.2s / 237.7s
trigger_min/max:0.0s / 7.1s
trigger_pct:100.00%
duration_min/max:0.0s / 286.8s
uptime_min/max:97.09% / 100.00%
Stack Uptimes
acrobatic_strikes_1:0.72%
acrobatic_strikes_2:0.88%
acrobatic_strikes_3:0.87%
acrobatic_strikes_4:0.84%
acrobatic_strikes_5:0.85%
acrobatic_strikes_6:0.85%
acrobatic_strikes_7:0.85%
acrobatic_strikes_8:0.84%
acrobatic_strikes_9:0.85%
acrobatic_strikes_10:91.53%
Spelldata
id:455144
name:Acrobatic Strikes
tooltip:Auto-attack damage increased by {$=}w1% and movement speed increased by {$=}w2%.
description:{$@spelldesc455143=Auto-attacks increase auto-attack damage by {$455144s1=3}% and movement speed by {$455144s2=1}% for {$455144d=3 seconds}, stacking up to {$455144u=10} times.}
max_stacks:10
duration:3.00
cooldown:0.00
default_chance:101.00%
	Adrenaline Rush	7.9	0.0	7.9	40.7s	40.6s	14.5s	38.07%	40.71%	106.5 (106.5)	7.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_adrenaline_rush
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.20
activated:true
reactable:false
reverse:false
refresh behavior:tick
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Trigger Details
interval_min/max:28.8s / 62.9s
trigger_min/max:28.8s / 62.9s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:29.94% / 45.39%
Stack Uptimes
adrenaline_rush_1:38.07%
Spelldata
id:13750
name:Adrenaline Rush
tooltip:Energy regeneration increased by {$=}w1%.
Maximum Energy increased by {$=}w6.
Attack speed increased by {$=}w2%.
{$?=}{$=}w4>0[Damage of combo point generating abilities and finishers increased by {$=}w4%.][]
description:Increases your Energy regeneration rate by {$s1=75}%, your maximum Energy by {$s6=50}, and your attack speed by {$s2=20}% for {$d=15 seconds}.{$?=}{$s4=0}>0[
Damage of combo point generating abilities and finishers increased by {$s4=0}%.][]
max_stacks:0
duration:15.00
cooldown:180.00
default_chance:0.00%
	Alnscorned Essence	5.2	119.1	124.2	20.3s	2.1s	34.4s	59.61%	0.00%	0.0 (0.0)	4.6
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
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
stat:agility
amount:34.04
Trigger Details
interval_min/max:0.7s / 278.6s
trigger_min/max:0.7s / 102.5s
trigger_pct:99.99%
duration_min/max:0.0s / 226.0s
uptime_min/max:26.96% / 88.66%
Stack Uptimes
alnscorned_essence_1:3.13%
alnscorned_essence_2:3.27%
alnscorned_essence_3:3.41%
alnscorned_essence_4:3.57%
alnscorned_essence_5:3.72%
alnscorned_essence_6:3.88%
alnscorned_essence_7:4.05%
alnscorned_essence_8:4.25%
alnscorned_essence_9:4.44%
alnscorned_essence_10:4.68%
alnscorned_essence_11:5.48%
alnscorned_essence_12:7.28%
alnscorned_essence_13:5.08%
alnscorned_essence_14:2.91%
alnscorned_essence_15:0.46%
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
	Alnsight	7.3	3.8	11.1	39.4s	25.0s	15.8s	38.52%	0.00%	3.8 (3.8)	6.9
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
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
interval_min/max:12.0s / 147.1s
trigger_min/max:0.0s / 113.7s
trigger_pct:100.00%
duration_min/max:0.0s / 109.7s
uptime_min/max:14.42% / 68.28%
Stack Uptimes
alnsight_1:38.52%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Arcanoweave Insight	5.9	5.2	11.1	49.8s	24.9s	26.9s	52.93%	0.00%	5.2 (5.2)	5.3
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
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
stat:agility
amount:87.46
Trigger Details
interval_min/max:20.0s / 172.9s
trigger_min/max:0.0s / 108.1s
trigger_pct:100.00%
duration_min/max:0.0s / 151.6s
uptime_min/max:24.50% / 92.39%
Stack Uptimes
arcanoweave_insight_1:52.93%
Spelldata
id:1229746
name:Arcanoweave Insight
tooltip:{$=}pri increased by {$=}w1.
description:Increases your {$=}pri by $1229511s0.
max_stacks:0
duration:20.00
cooldown:0.00
default_chance:0.00%
	Between the Eyes	4.2	36.0	40.2	57.1s	7.4s	68.4s	96.41%	96.27%	0.0 (0.0)	3.3
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_between_the_eyes
max_stacks:20
base duration:2.00
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
Damage Modifiers
direct:1.00 + 0.06/stack
periodic:1.00 + 0.06/stack
auto_attack:1.00 + 0.00/stack
crit_chance:1.00
is_stacking:true
Trigger Details
interval_min/max:0.8s / 353.5s
trigger_min/max:0.8s / 33.5s
trigger_pct:69.14%
duration_min/max:0.0s / 357.2s
uptime_min/max:82.92% / 99.54%
Stack Uptimes
between_the_eyes_1:14.42%
between_the_eyes_2:23.15%
between_the_eyes_3:22.46%
between_the_eyes_4:17.45%
between_the_eyes_5:9.84%
between_the_eyes_6:5.34%
between_the_eyes_7:2.23%
between_the_eyes_8:0.98%
between_the_eyes_9:0.34%
between_the_eyes_10:0.13%
between_the_eyes_11:0.04%
between_the_eyes_12:0.01%
between_the_eyes_13:0.00%
between_the_eyes_14:0.00%
between_the_eyes_15:0.00%
Spelldata
id:315341
name:Between the Eyes
tooltip:Damage dealt increased by {$=}w2%.
description:Finishing move that blasts your target with your pistol, dealing Physical damage and increasing your damage dealt by {$s2=4}%. Multiple instances of this bonus can overlap.{$?a235484=true}[ Critical strikes with this ability deal four times normal damage.][]
 1 point : {$=}{{$=}<damage>*1} damage, 4 sec
 2 points: {$=}{{$=}<damage>*2} damage, 6 sec
 3 points: {$=}{{$=}<damage>*3} damage, 8 sec
 4 points: {$=}{{$=}<damage>*4} damage, 10 sec
 5 points: {$=}{{$=}<damage>*5} damage, 12 sec{$?s193531=true}|((s394320|s394321)&!s193531)[
 6 points: {$=}{{$=}<damage>*6} damage, 14 sec][]{$?s193531=true}&(s394320|s394321)[
 7 points: {$=}{{$=}<damage>*7} damage, 16 sec][]
max_stacks:20
duration:2.00
cooldown:45.00
default_chance:101.00%
	Blade Rush	23.8	0.0	23.8	12.9s	12.9s	5.0s	39.37%	0.00%	94.5 (94.5)	23.4
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_blade_rush
max_stacks:1
base duration:5.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:5.00
activated:true
reactable:false
reverse:false
refresh behavior:tick
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Trigger Details
interval_min/max:5.5s / 28.1s
trigger_min/max:5.5s / 28.1s
trigger_pct:100.00%
duration_min/max:0.0s / 5.0s
uptime_min/max:32.07% / 46.31%
Stack Uptimes
blade_rush_1:39.37%
Spelldata
id:271896
name:Blade Rush
tooltip:Generates {$s1=5} Energy every sec.
description:{$@spelldesc271877=Charge to your target with your blades out, dealing {$=}{$271881sw1*{$271881s2=230}/100} Physical damage to the target and $271881sw1 to all other nearby enemies. Damage reduced beyond $271881sw3 targets.
While Blade Flurry is active, damage to non-primary targets is increased by {$s1=100}%.
|cFFFFFFFFGenerates {$=}{{$271896s1=5}*{$271896d=5 seconds}/{$271896t1=1}} Energy over {$271896d=5 seconds}.}
max_stacks:0
duration:5.00
cooldown:0.00
default_chance:0.00%
	Bloodlust	1.0	0.0	1.0	0.0s	0.0s	40.0s	13.52%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_bloodlust
max_stacks:1
base duration:40.00
duration modifier:1.00
base cooldown:300.00
default_chance:100.00%
default_value:0.30
activated:true
reactable:true
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
	Deadly Pursuit	9.0	86.3	95.2	34.1s	34.1s	26.5s	78.99%	0.00%	86.3 (0.0)	8.2
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_deadly_pursuit
max_stacks:1
base duration:4.00
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
interval_min/max:7.4s / 254.1s
trigger_min/max:7.4s / 254.1s
trigger_pct:100.00%
duration_min/max:0.0s / 244.9s
uptime_min/max:60.85% / 95.71%
Stack Uptimes
deadly_pursuit_1:78.99%
Spelldata
id:1259613
name:Deadly Pursuit
tooltip:
description:
max_stacks:0
duration:4.00
cooldown:0.00
default_chance:0.00%
	Deadly Pursuit (_cdr)	8.2	0.0	8.2	32.5s	32.5s	0.2s	0.59%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_deadly_pursuit_cdr
max_stacks:1
base duration:5.00
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
interval_min/max:7.5s / 241.1s
trigger_min/max:7.5s / 241.1s
trigger_pct:100.00%
duration_min/max:0.0s / 5.0s
uptime_min/max:0.01% / 3.91%
Stack Uptimes
deadly_pursuit_cdr_1:0.59%
Spelldata
id:1259614
name:Deadly Pursuit
tooltip:Cooldown recovery rate of Adrenaline Rush, Between the Eyes, Blade Flurry, Blade Rush, Grappling Hook, Keep it Rolling, Killing Spree, Roll the Bones, and Sprint increased by {$=}w1%.
description:{$@spelldesc1259612=After spending {$s1=15} combo points, if you spend no combo points for {$1259613d=4 seconds}, abilities affected by Restless Blades will cool down {$1259614s1=200}% faster for {$1259614d=5 seconds} or until you spend a combo point.}
max_stacks:0
duration:5.00
cooldown:0.00
default_chance:101.00%
	Deadly Pursuit (_tracker)	9.1	18.0	27.1	34.1s	11.1s	4.6s	13.84%	0.00%	8.9 (45.6)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_deadly_pursuit_tracker
max_stacks:15
base duration:150.00
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
interval_min/max:7.5s / 251.3s
trigger_min/max:0.8s / 248.1s
trigger_pct:100.00%
duration_min/max:0.0s / 16.7s
uptime_min/max:2.65% / 26.05%
Stack Uptimes
deadly_pursuit_tracker_2:0.00%
deadly_pursuit_tracker_3:0.00%
deadly_pursuit_tracker_4:0.00%
deadly_pursuit_tracker_5:0.01%
deadly_pursuit_tracker_6:2.34%
deadly_pursuit_tracker_7:4.68%
deadly_pursuit_tracker_8:0.00%
deadly_pursuit_tracker_9:0.00%
deadly_pursuit_tracker_10:0.00%
deadly_pursuit_tracker_11:0.01%
deadly_pursuit_tracker_12:0.43%
deadly_pursuit_tracker_13:3.34%
deadly_pursuit_tracker_14:3.02%
Spelldata
id:1259613
name:Deadly Pursuit
tooltip:
description:
max_stacks:0
duration:4.00
cooldown:0.00
default_chance:0.00%
	Disorienting Strikes	8.0	0.0	8.0	39.3s	39.3s	5.6s	14.90%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_disorienting_strikes
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
interval_min/max:25.6s / 64.8s
trigger_min/max:25.6s / 64.8s
trigger_pct:100.00%
duration_min/max:0.0s / 11.0s
uptime_min/max:10.02% / 21.76%
Stack Uptimes
disorienting_strikes_1:4.28%
disorienting_strikes_2:10.62%
Spelldata
id:441274
name:Disorienting Strikes
tooltip:
description:{$?a137036=true}[Killing Spree][Secret Technique] has {$s1=10}% reduced cooldown and allows your next {$s2=2} strikes of Unseen Blade to ignore its cooldown.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:0.00%
	Double Trouble	3.6	0.0	3.6	71.4s	63.9s	40.3s	48.29%	49.74%	0.0 (0.0)	3.1
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_double_trouble
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
Damage Modifiers
direct:1.20
periodic:1.00
auto_attack:1.00
crit_chance:1.00
is_stacking:false
Trigger Details
interval_min/max:30.0s / 345.7s
trigger_min/max:30.0s / 285.8s
trigger_pct:100.00%
duration_min/max:0.0s / 60.0s
uptime_min/max:0.00% / 99.68%
Stack Uptimes
double_trouble_1:48.29%
Spelldata
id:1214934
name:Double Trouble
tooltip:Sinister Strike has a {$=}w1% increased chance to strike twice and grant Opportunity.
Sinister Strike and Ambush generate {$=}w2 additional combo {$=}Lpoint:points; and deal {$=}w3% increased damage.
description:$@spelldesc1214774
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:0.00%
	Escalating Blade	14.5	47.8	62.4	21.2s	4.8s	15.7s	76.21%	0.00%	5.5 (5.5)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_escalating_blade
max_stacks:4
base duration:0.00
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
interval_min/max:2.6s / 57.9s
trigger_min/max:0.0s / 23.3s
trigger_pct:100.00%
duration_min/max:0.0s / 55.9s
uptime_min/max:57.45% / 92.04%
Stack Uptimes
escalating_blade_1:21.08%
escalating_blade_2:22.25%
escalating_blade_3:21.80%
escalating_blade_4:11.09%
Spelldata
id:441786
name:Escalating Blade
tooltip:Building to a Coup de Grace.
description:{$@spelldesc441423=After {$441786s1=4} strikes with Unseen Blade, your next {$?a137036=true}[Dispatch][Eviscerate] will be performed as a Coup de Grace, functioning as if it had consumed {$s3=5} additional combo points, and granting you {$s2=5} stacks of Flawless Form.}
max_stacks:4
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Flawless Form	6.6	77.5	84.1	47.1s	3.6s	43.1s	94.70%	96.58%	61.8 (108.1)	5.6
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_flawless_form
max_stacks:5
base duration:12.00
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
Damage Modifiers
direct:1.00 + 0.04/stack
periodic:1.00 + 0.04/stack
auto_attack:1.00 + 0.00/stack
crit_chance:1.00
is_stacking:true
Stack Uptimes
flawless_form_1:7.12%
flawless_form_2:5.78%
flawless_form_3:3.28%
flawless_form_4:2.01%
flawless_form_5:76.51%
Spelldata
id:441326
name:Flawless Form
tooltip:Finishing moves deal {$s1=4}% increased damage.
description:{$@spelldesc441321=Unseen Blade and {$?a137036=true}[Killing Spree][Secret Technique] increase the damage of your finishing moves by {$441326s1=4}% for {$441326d=12 seconds}. Max {$441326u=5} stacks.}
max_stacks:5
duration:12.00
cooldown:0.00
default_chance:101.00%
	Gravedigger	7.3	0.0	7.3	38.0s	38.0s	6.3s	15.52%	18.02%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_gravedigger
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-1.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:15.4s / 133.7s
trigger_min/max:15.4s / 133.7s
trigger_pct:100.00%
duration_min/max:0.0s / 28.0s
uptime_min/max:3.11% / 33.61%
Stack Uptimes
gravedigger_1:15.52%
Spelldata
id:1265935
name:Gravedigger
tooltip:Your next Between the Eyes costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.
description:{$@spelldesc1265863=When you Dispatch you have a {$s1=12}% chance per combo point spent to hide a bullet up your sleeve. When you've hidden {$s2=6} bullets, your next Between the Eyes consumes them and costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.}
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:100.00%
	Jackpot	1.0	0.0	1.0	114.7s	103.1s	51.8s	16.55%	25.64%	0.0 (0.0)	0.8
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_jackpot
max_stacks:1
base duration:30.00
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
stat:crit
amount:15.00%
Damage Modifiers
direct:1.20
periodic:1.00
auto_attack:1.00
crit_chance:1.00
is_stacking:false
Trigger Details
interval_min/max:30.0s / 335.5s
trigger_min/max:30.0s / 276.2s
trigger_pct:100.00%
duration_min/max:0.0s / 60.0s
uptime_min/max:0.00% / 90.33%
Stack Uptimes
jackpot_1:16.55%
Spelldata
id:1214937
name:Jackpot
tooltip:Sinister Strike has a {$=}w1% increased chance to strike twice and grant Opportunity.
Sinister Strike and Ambush generate {$=}w2 additional combo {$=}Lpoint:points; and deal {$=}w3% increased damage.
Restless Blades cooldown reduction increased by {$=}w4%.
Critical strike chance increased by {$=}w5%.
description:$@spelldesc1214774
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:0.00%
	Killing Spree	8.0	0.0	8.0	39.3s	39.3s	2.6s	6.80%	0.00%	44.4 (44.4)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_killing_spree
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:clip
tick_time behavior:hasted
period:0.50
Trigger Details
interval_min/max:25.6s / 64.8s
trigger_min/max:25.6s / 64.8s
trigger_pct:100.00%
duration_min/max:0.0s / 3.2s
uptime_min/max:4.90% / 8.68%
Stack Uptimes
killing_spree_1:6.80%
Spelldata
id:51690
name:Killing Spree
tooltip:Blasting nearby enemies every {$=}{{$t1=0.500}}.2 sec.
description:Finishing move that unleashes a barrage of gunfire, striking random enemies within {$=}r yards for Physical damage. Number of strikes increased per combo point.
Restores {$1235074m2=0} combo {$=}Lpoint:points; every {$=}{{$t1=0.500}}.2 sec.
 1 point : {$=}{{$=}<dmg>*2} over {$=}{{$424556d=500 milliseconds}}.2 sec
 2 points: {$=}{{$=}<dmg>*3} over {$=}{{$424556d=500 milliseconds}*2}.2 sec
 3 points: {$=}{{$=}<dmg>*4} over {$=}{{$424556d=500 milliseconds}*3}.2 sec
 4 points: {$=}{{$=}<dmg>*5} over {$=}{{$424556d=500 milliseconds}*4}.2 sec
 5 points: {$=}{{$=}<dmg>*6} over {$=}{{$424556d=500 milliseconds}*5}.2 sec{$?s193531=true}|((s394320|s394321)&!s193531)[
 6 points: {$=}{{$=}<dmg>*7} over {$=}{{$424556d=500 milliseconds}*6}.2 sec][]{$?s193531=true}&(s394320|s394321)[
 7 points: {$=}{{$=}<dmg>*8} over {$=}{{$424556d=500 milliseconds}*7}.2 sec][]
max_stacks:0
duration:0.00
cooldown:162.00
default_chance:0.00%
	Light's Potential	1.5	0.0	1.5	303.2s	303.2s	27.5s	13.37%	0.00%	0.0 (0.0)	1.2
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
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
stat:agility
amount:695.00
Trigger Details
interval_min/max:300.0s / 329.3s
trigger_min/max:300.0s / 329.3s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.87% / 18.14%
Stack Uptimes
lights_potential_1:13.37%
Spelldata
id:1236616
name:Light's Potential
tooltip:Primary stat increased by {$=}w1.
description:Drink to increase your primary stat by {$s1=365} for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Loaded Dice	6.7	1.2	7.9	47.9s	40.6s	24.7s	46.24%	91.52%	1.2 (1.2)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_loaded_dice
max_stacks:1
base duration:45.00
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
interval_min/max:30.2s / 97.1s
trigger_min/max:28.8s / 62.9s
trigger_pct:100.00%
duration_min/max:0.0s / 61.2s
uptime_min/max:11.55% / 71.56%
Stack Uptimes
loaded_dice_1:46.24%
Spelldata
id:256171
name:Loaded Dice
tooltip:The result of your next Roll the Bones will be improved by one level.
description:{$@spelldesc256170=Activating Adrenaline Rush improves the result of your next Roll the Bones by one level.}
max_stacks:0
duration:45.00
cooldown:0.00
default_chance:100.00%
	Might of the Void	8.2	8.6	16.7	36.4s	17.1s	21.4s	58.05%	0.00%	8.6 (8.6)	7.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
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
stat:agility
amount:66.80
Trigger Details
interval_min/max:15.0s / 145.3s
trigger_min/max:0.0s / 76.1s
trigger_pct:100.00%
duration_min/max:0.0s / 140.0s
uptime_min/max:31.23% / 85.48%
Stack Uptimes
might_of_the_void_1:58.05%
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
	One of a Kind	0.3	0.0	0.3	101.0s	101.0s	11.8s	1.30%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_one_of_a_kind
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
Trigger Details
interval_min/max:11.2s / 255.3s
trigger_min/max:11.2s / 255.3s
trigger_pct:100.00%
duration_min/max:0.3s / 21.6s
uptime_min/max:0.00% / 13.67%
Stack Uptimes
one_of_a_kind_1:1.30%
Spelldata
id:1214933
name:One of a Kind
tooltip:Sinister Strike has a {$=}w1% increased chance to strike twice and grant Opportunity.
description:$@spelldesc1214774
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:0.00%
	Opportunity	47.9	13.3	61.2	6.3s	4.9s	3.9s	61.51%	100.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_opportunity
max_stacks:6
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:1.20
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:2.4s / 48.4s
trigger_min/max:0.8s / 28.8s
trigger_pct:65.15%
duration_min/max:0.0s / 44.5s
uptime_min/max:47.45% / 75.06%
Stack Uptimes
opportunity_1:1.58%
opportunity_2:1.58%
opportunity_3:46.38%
opportunity_4:0.44%
opportunity_5:0.44%
opportunity_6:11.10%
Spelldata
id:195627
name:Opportunity
tooltip:Your next Pistol Shot costs {$s1=50}% less Energy and deals {$s2=100}% increased damage.
description:{$@spelldesc279876=Sinister Strike has a {$s1=30}% chance to hit an additional time and grant Opportunity.
{$@=}spellicon195627 {$@=}spellname195627
Your next Pistol Shot costs {$195627s1=50}% less Energy and deals {$195627s2=100}% increased damage.}
max_stacks:6
duration:12.00
cooldown:0.00
default_chance:100.00%
	Palmed Bullets	4.0	42.6	46.6	73.6s	6.3s	66.8s	89.76%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_palmed_bullets
max_stacks:10
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
interval_min/max:19.1s / 335.9s
trigger_min/max:1.0s / 49.0s
trigger_pct:100.00%
duration_min/max:0.0s / 347.5s
uptime_min/max:65.31% / 98.53%
Stack Uptimes
palmed_bullets_1:13.01%
palmed_bullets_2:15.13%
palmed_bullets_3:15.41%
palmed_bullets_4:15.61%
palmed_bullets_5:15.08%
palmed_bullets_6:8.48%
palmed_bullets_7:4.51%
palmed_bullets_8:1.83%
palmed_bullets_9:0.56%
palmed_bullets_10:0.14%
Spelldata
id:1265931
name:Palmed Bullets
tooltip:{$=}w2 {$=}Lbullet:bullets; hidden up your sleeve. When you've hidden {$1265863s2=6} bullets, your next Between the Eyes consumes them and costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.
description:{$@spelldesc1265863=When you Dispatch you have a {$s1=12}% chance per combo point spent to hide a bullet up your sleeve. When you've hidden {$s2=6} bullets, your next Between the Eyes consumes them and costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.}
max_stacks:10
duration:30.00
cooldown:0.00
default_chance:101.00%
	Precision of the Dragonhawk	8.1	8.6	16.8	36.5s	17.0s	21.4s	58.15%	0.00%	8.6 (8.6)	7.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
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
interval_min/max:15.0s / 170.0s
trigger_min/max:0.0s / 72.6s
trigger_pct:100.00%
duration_min/max:0.0s / 145.0s
uptime_min/max:33.02% / 88.90%
Stack Uptimes
precision_of_the_dragonhawk_1:58.15%
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
	Roll the Bones	6.5	0.3	6.8	50.0s	44.7s	45.9s	99.01%	0.00%	0.3 (0.3)	5.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_roll_the_bones
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
Trigger Details
interval_min/max:30.0s / 95.7s
trigger_min/max:6.3s / 63.3s
trigger_pct:100.00%
duration_min/max:0.0s / 95.5s
uptime_min/max:97.40% / 99.84%
Stack Uptimes
roll_the_bones_1:99.01%
Spelldata
id:1214909
name:Roll the Bones
tooltip:Gained a random combat enhancement.
description:Roll the dice of fate, providing a combat enhancement of random power for {$d=30 seconds}.
1 set or better: Add {$1214937s1=20}% increased chance to gain Opportunity.
2 sets or better: Add increased combo point generation.
3 sets or better: Add {$1214937s4=30}% bonus to Restless Blades' effect.
Jackpot: Add {$1214937s5=10}% increased critical strike chance.
max_stacks:0
duration:30.00
cooldown:45.00
default_chance:0.00%
	Slice and Dice	1.0	0.0	1.0	0.0s	0.0s	300.0s	100.00%	88.33%	99.5 (99.5)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_slice_and_dice
max_stacks:1
base duration:6.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.60
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:3.00
Trigger Details
interval_min/max:0.0s / 0.0s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:240.0s / 360.0s
uptime_min/max:100.00% / 100.00%
Stack Uptimes
slice_and_dice_1:100.00%
Spelldata
id:315496
name:Slice and Dice
tooltip:Attack speed increased by {$=}w1%.
description:Finishing move that consumes combo points to increase attack speed by {$s1=50}%. Lasts longer per combo point.
 1 point : 12 seconds
 2 points: 18 seconds
 3 points: 24 seconds
 4 points: 30 seconds
 5 points: 36 seconds{$?s193531=true}|((s394320|s394321|s457512)&!s193531)[
 6 points: 42 seconds][]{$?s193531=true}&(s394320|s394321|s457512)[
 7 points: 48 seconds][]
max_stacks:0
duration:6.00
cooldown:0.00
default_chance:0.00%
	Stealth	1.0	0.0	1.0	0.0s	0.0s	0.0s	0.00%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_stealth
max_stacks:1
base duration:150.00
duration modifier:1.00
base cooldown:2.00
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
interval_min/max:0.0s / 0.0s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:0.0s / 0.0s
uptime_min/max:0.00% / 0.00%
Stack Uptimes
stealth_1:0.00%
Spelldata
id:1784
name:Stealth
tooltip:Stealthed.{$?=}{$=}w3!=0[
Movement speed increased by {$=}w3%.][]
description:Conceals you in the shadows until cancelled, allowing you to stalk enemies without being seen. $?s14062[Movement speed while stealthed is increased by {$s3=0}% and damage dealt is increased by {$s4=0}%.]?s108209[ Abilities cost {$112942s1=10}% less while stealthed. ][]{$?s31223=false}[ Attacks from Stealth and for {$31223s1=5} sec after deal {$31665s1=10}% more damage.][]
max_stacks:0
duration:-0.00
cooldown:2.00
default_chance:100.00%
	Supercharge (_1)	7.9	0.0	7.9	40.7s	40.6s	1.3s	1.24%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_supercharge_1
max_stacks:1
base duration:0.00
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
interval_min/max:28.8s / 62.9s
trigger_min/max:28.8s / 62.9s
trigger_pct:100.00%
duration_min/max:0.0s / 3.2s
uptime_min/max:0.45% / 3.31%
Stack Uptimes
supercharge_1_1:1.24%
Spelldata
id:470398
name:Supercharge
tooltip:Rogue's first combo point is supercharged.
Damaging finishing moves consume a supercharged combo point to function as if they spent {$470347s2=2} additional combo points.
description:{$@spelldesc470347={$?a137035=false}[Shadow Dance]?a137036[Adrenaline Rush][Kingsbane] supercharges {$m1=1} combo {$=}Lpoint:points;.
Damaging finishing moves consume a supercharged combo point to function as if they spent {$m2=2} additional combo {$=}Lpoint:points;.}
max_stacks:1
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Triple Threat	1.9	0.0	1.9	100.5s	93.0s	51.6s	32.87%	36.66%	0.0 (0.0)	1.6
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_triple_threat
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
Damage Modifiers
direct:1.20
periodic:1.00
auto_attack:1.00
crit_chance:1.00
is_stacking:false
Trigger Details
interval_min/max:30.0s / 336.2s
trigger_min/max:30.0s / 296.1s
trigger_pct:100.00%
duration_min/max:0.0s / 60.0s
uptime_min/max:0.00% / 99.33%
Stack Uptimes
triple_threat_1:32.87%
Spelldata
id:1214935
name:Triple Threat
tooltip:Sinister Strike has a {$=}w1% increased chance to strike twice and grant Opportunity.
Sinister Strike and Ambush generate {$=}w2 additional combo {$=}Lpoint:points; and deal {$=}w3% increased damage.
Restless Blades cooldown reduction increased by {$=}w4%.
description:$@spelldesc1214774
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:0.00%
	Umbral Plume	6.5	0.0	6.5	49.2s	60.0s	46.3s	100.00%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_umbral_plume
max_stacks:60
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Stat Details
stat:crit_rating
amount:4.70
Trigger Details
interval_min/max:1.0s / 60.0s
trigger_min/max:60.0s / 60.0s
trigger_pct:100.00%
duration_min/max:0.0s / 60.0s
uptime_min/max:100.00% / 100.00%
Stack Uptimes
umbral_plume_1:1.84%
umbral_plume_2:1.51%
umbral_plume_3:1.51%
umbral_plume_4:1.52%
umbral_plume_5:1.52%
umbral_plume_6:1.53%
umbral_plume_7:1.53%
umbral_plume_8:1.54%
umbral_plume_9:1.54%
umbral_plume_10:1.55%
umbral_plume_11:1.55%
umbral_plume_12:1.56%
umbral_plume_13:1.56%
umbral_plume_14:1.57%
umbral_plume_15:1.57%
umbral_plume_16:1.58%
umbral_plume_17:1.58%
umbral_plume_18:1.59%
umbral_plume_19:1.60%
umbral_plume_20:1.60%
umbral_plume_21:1.61%
umbral_plume_22:1.61%
umbral_plume_23:1.62%
umbral_plume_24:1.62%
umbral_plume_25:1.63%
umbral_plume_26:1.63%
umbral_plume_27:1.64%
umbral_plume_28:1.64%
umbral_plume_29:1.65%
umbral_plume_30:1.66%
umbral_plume_31:1.66%
umbral_plume_32:1.67%
umbral_plume_33:1.67%
umbral_plume_34:1.68%
umbral_plume_35:1.68%
umbral_plume_36:1.69%
umbral_plume_37:1.69%
umbral_plume_38:1.70%
umbral_plume_39:1.71%
umbral_plume_40:1.71%
umbral_plume_41:1.72%
umbral_plume_42:1.72%
umbral_plume_43:1.73%
umbral_plume_44:1.74%
umbral_plume_45:1.74%
umbral_plume_46:1.75%
umbral_plume_47:1.75%
umbral_plume_48:1.76%
umbral_plume_49:1.77%
umbral_plume_50:1.77%
umbral_plume_51:1.78%
umbral_plume_52:1.78%
umbral_plume_53:1.79%
umbral_plume_54:1.80%
umbral_plume_55:1.80%
umbral_plume_56:1.81%
umbral_plume_57:1.81%
umbral_plume_58:1.82%
umbral_plume_59:1.83%
umbral_plume_60:1.83%
Spelldata
id:1265808
name:Umbral Plume
tooltip:Critical Strike increased by {$=}w1.
description:{$@spelldesc1260592=The Plume's radiance grants you {$1260592s1=157} Mastery, waning over {$=}{{$1260615t2=1}*{$1260615u=60}} sec before reigniting to full incandescence. The Plume's power also regenerates while out of combat.}
max_stacks:60
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Whirl of Blades	23.7	0.1	23.8	12.9s	12.9s	7.9s	62.66%	70.52%	0.1 (0.1)	23.1
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_whirl_of_blades
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
Damage Modifiers
direct:1.05
periodic:1.05
auto_attack:1.05
crit_chance:1.00
is_stacking:false
Trigger Details
interval_min/max:8.0s / 28.1s
trigger_min/max:5.5s / 28.1s
trigger_pct:100.00%
duration_min/max:0.0s / 16.0s
uptime_min/max:51.31% / 73.39%
Stack Uptimes
whirl_of_blades_1:62.66%
Spelldata
id:1275176
name:Whirl of Blades
tooltip:Damage dealt increased by {$=}w1%.
description:{$@spelldesc1264859=Blade Rush's cooldown is reduced by {$=}{-{$s1=6000}/1000} sec and it increases your damage dealt by {$1275176s1=5}% for {$1275176d=8 seconds}.}
max_stacks:0
duration:8.00
cooldown:0.00
default_chance:0.00%
	Zero In	38.9	323.7	362.6	7.7s	0.8s	7.0s	91.42%	94.57%	13.4 (13.4)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Trickster
cooldown name:buff_zero_in
max_stacks:20
base duration:20.00
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
Damage Modifiers
direct:1.00 + 0.03/stack
periodic:1.00 + 0.00/stack
auto_attack:1.00 + 0.00/stack
crit_chance:1.03
is_stacking:true
Trigger Details
interval_min/max:0.0s / 33.0s
trigger_min/max:0.0s / 13.5s
trigger_pct:100.00%
duration_min/max:0.0s / 32.8s
uptime_min/max:83.80% / 96.30%
Stack Uptimes
zero_in_1:9.12%
zero_in_2:8.78%
zero_in_3:7.98%
zero_in_4:7.25%
zero_in_5:6.61%
zero_in_6:6.11%
zero_in_7:5.74%
zero_in_8:5.39%
zero_in_9:5.01%
zero_in_10:4.61%
zero_in_11:4.14%
zero_in_12:3.67%
zero_in_13:3.17%
zero_in_14:2.68%
zero_in_15:2.25%
zero_in_16:1.82%
zero_in_17:1.49%
zero_in_18:1.19%
zero_in_19:0.95%
zero_in_20:3.46%
Spelldata
id:1259486
name:Zero In
tooltip:Damage and critical strike chance of your next Between the Eyes is increased by {$=}w1%.
description:{$@spelldesc1259485=Your auto-attack critical strikes increase the damage and critical strike chance of your next Between the Eyes by {$1259486s1=3}%, stacking up to {$1259486u=20} times.}
max_stacks:20
duration:20.00
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
	Roll the Bones Buff Lost: one_of_a_kind	0.3	0.0	3.0	93.5s	8.5s	254.6s
	Roll the Bones Buffs: 1	0.3	0.0	3.0	101.0s	11.2s	255.3s
	Roll the Bones Buffs: 2	3.6	0.0	8.0	71.4s	30.0s	345.7s
	Roll the Bones Buffs: 3	1.9	0.0	7.0	100.5s	30.0s	336.2s
	Roll the Bones Buffs: 4	1.0	0.0	5.0	114.7s	30.0s	335.5s
	Skyfury (Main Hand)	44.7	22.0	72.0	6.6s	0.6s	85.5s
	Skyfury (Off Hand)	65.0	33.0	103.0	4.6s	0.4s	53.8s
	Supercharger between_the_eyes	7.0	3.0	10.0	45.0s	28.5s	256.5s
	Supercharger coup_de_grace	0.0	0.0	2.0	175.5s	175.5s	175.5s
	Supercharger dispatch	0.7	0.0	6.0	87.8s	31.2s	306.2s
	Supercharger killing_spree	0.1	0.0	1.0	0.0s	0.0s	0.0s
	delayed_aa_channel	53.4	33.0	76.0	5.3s	0.0s	63.0s
```

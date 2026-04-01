# MID1_Rogue_Outlaw_Fatebound — Buffs & Procs

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
	Acrobatic Strikes	1.0	695.2	696.2	165.4s	0.4s	288.7s	99.98%	100.00%	685.9 (685.9)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:41.5s / 346.7s
trigger_min/max:0.0s / 5.0s
trigger_pct:100.00%
duration_min/max:0.2s / 360.0s
uptime_min/max:99.32% / 100.00%
Stack Uptimes
acrobatic_strikes_1:0.09%
acrobatic_strikes_2:0.11%
acrobatic_strikes_3:0.09%
acrobatic_strikes_4:0.10%
acrobatic_strikes_5:0.10%
acrobatic_strikes_6:0.10%
acrobatic_strikes_7:0.10%
acrobatic_strikes_8:0.10%
acrobatic_strikes_9:0.10%
acrobatic_strikes_10:99.10%
Spelldata
id:455144
name:Acrobatic Strikes
tooltip:Auto-attack damage increased by {$=}w1% and movement speed increased by {$=}w2%.
description:{$@spelldesc455143=Auto-attacks increase auto-attack damage by {$455144s1=3}% and movement speed by {$455144s2=1}% for {$455144d=3 seconds}, stacking up to {$455144u=10} times.}
max_stacks:10
duration:3.00
cooldown:0.00
default_chance:101.00%
	Adrenaline Rush	9.5	0.0	9.5	33.3s	35.7s	14.6s	45.90%	50.75%	128.4 (128.4)	9.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:14.7s / 59.3s
trigger_min/max:15.0s / 59.3s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:36.11% / 54.30%
Stack Uptimes
adrenaline_rush_1:45.90%
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
	Alnscorned Essence	5.2	122.6	127.8	20.3s	2.1s	34.8s	59.84%	0.00%	0.0 (0.0)	4.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:0.7s / 264.5s
trigger_min/max:0.7s / 94.3s
trigger_pct:99.99%
duration_min/max:0.0s / 265.4s
uptime_min/max:28.17% / 95.13%
Stack Uptimes
alnscorned_essence_1:3.07%
alnscorned_essence_2:3.19%
alnscorned_essence_3:3.33%
alnscorned_essence_4:3.47%
alnscorned_essence_5:3.62%
alnscorned_essence_6:3.79%
alnscorned_essence_7:3.94%
alnscorned_essence_8:4.13%
alnscorned_essence_9:4.30%
alnscorned_essence_10:4.52%
alnscorned_essence_11:5.15%
alnscorned_essence_12:6.93%
alnscorned_essence_13:5.11%
alnscorned_essence_14:3.71%
alnscorned_essence_15:1.57%
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
	Alnsight	7.3	3.8	11.1	39.2s	24.8s	15.9s	38.69%	0.00%	3.8 (3.8)	6.9
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:12.0s / 163.9s
trigger_min/max:0.0s / 106.7s
trigger_pct:100.00%
duration_min/max:0.0s / 102.5s
uptime_min/max:14.53% / 73.86%
Stack Uptimes
alnsight_1:38.69%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Arcanoweave Insight	5.9	5.3	11.1	49.8s	24.8s	27.0s	52.89%	0.00%	5.3 (5.3)	5.3
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:20.0s / 206.7s
trigger_min/max:0.0s / 118.9s
trigger_pct:100.00%
duration_min/max:0.0s / 164.3s
uptime_min/max:22.79% / 85.47%
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
	Between the Eyes	3.1	45.9	49.0	70.5s	6.1s	94.4s	97.64%	97.51%	0.0 (0.0)	2.1
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:0.8s / 355.6s
trigger_min/max:0.8s / 30.1s
trigger_pct:69.16%
duration_min/max:0.1s / 358.2s
uptime_min/max:90.21% / 99.55%
Stack Uptimes
between_the_eyes_1:7.61%
between_the_eyes_2:15.01%
between_the_eyes_3:19.18%
between_the_eyes_4:19.31%
between_the_eyes_5:15.01%
between_the_eyes_6:10.13%
between_the_eyes_7:5.81%
between_the_eyes_8:3.11%
between_the_eyes_9:1.45%
between_the_eyes_10:0.64%
between_the_eyes_11:0.25%
between_the_eyes_12:0.09%
between_the_eyes_13:0.03%
between_the_eyes_14:0.01%
between_the_eyes_15:0.01%
between_the_eyes_16:0.00%
between_the_eyes_17:0.00%
between_the_eyes_18:0.00%
between_the_eyes_19:0.00%
between_the_eyes_20:0.00%
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
	Blade Rush	26.4	0.1	26.5	11.6s	11.7s	5.0s	43.76%	0.00%	105.1 (105.1)	26.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:5.0s / 25.4s
trigger_min/max:1.8s / 25.4s
trigger_pct:100.00%
duration_min/max:0.0s / 10.0s
uptime_min/max:34.74% / 50.53%
Stack Uptimes
blade_rush_1:43.76%
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
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
	Deadly Pursuit	4.9	126.9	131.8	62.8s	62.8s	55.7s	90.54%	0.00%	126.9 (0.0)	4.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:7.5s / 330.4s
trigger_min/max:7.5s / 330.4s
trigger_pct:100.00%
duration_min/max:0.0s / 354.3s
uptime_min/max:74.13% / 99.10%
Stack Uptimes
deadly_pursuit_1:90.54%
Spelldata
id:1259613
name:Deadly Pursuit
tooltip:
description:
max_stacks:0
duration:4.00
cooldown:0.00
default_chance:0.00%
	Deadly Pursuit (_cdr)	4.0	0.0	4.0	54.6s	54.6s	0.2s	0.29%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:7.5s / 291.0s
trigger_min/max:7.5s / 291.0s
trigger_pct:100.00%
duration_min/max:0.0s / 5.0s
uptime_min/max:0.00% / 3.25%
Stack Uptimes
deadly_pursuit_cdr_1:0.29%
Spelldata
id:1259614
name:Deadly Pursuit
tooltip:Cooldown recovery rate of Adrenaline Rush, Between the Eyes, Blade Flurry, Blade Rush, Grappling Hook, Keep it Rolling, Killing Spree, Roll the Bones, and Sprint increased by {$=}w1%.
description:{$@spelldesc1259612=After spending {$s1=15} combo points, if you spend no combo points for {$1259613d=4 seconds}, abilities affected by Restless Blades will cool down {$1259614s1=200}% faster for {$1259614d=5 seconds} or until you spend a combo point.}
max_stacks:0
duration:5.00
cooldown:0.00
default_chance:101.00%
	Deadly Pursuit (_tracker)	4.9	9.8	14.7	62.8s	19.6s	4.0s	6.55%	0.00%	4.9 (21.7)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:7.5s / 326.6s
trigger_min/max:0.8s / 323.3s
trigger_pct:100.00%
duration_min/max:0.0s / 14.6s
uptime_min/max:0.90% / 17.22%
Stack Uptimes
deadly_pursuit_tracker_5:0.16%
deadly_pursuit_tracker_6:1.03%
deadly_pursuit_tracker_7:2.04%
deadly_pursuit_tracker_10:0.00%
deadly_pursuit_tracker_11:0.24%
deadly_pursuit_tracker_12:0.55%
deadly_pursuit_tracker_13:1.36%
deadly_pursuit_tracker_14:1.16%
Spelldata
id:1259613
name:Deadly Pursuit
tooltip:
description:
max_stacks:0
duration:4.00
cooldown:0.00
default_chance:0.00%
	Double Trouble	3.5	0.0	3.5	72.7s	71.9s	40.2s	47.24%	48.65%	0.0 (0.0)	3.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:30.0s / 333.1s
trigger_min/max:30.0s / 273.5s
trigger_pct:100.00%
duration_min/max:0.0s / 60.0s
uptime_min/max:0.00% / 99.56%
Stack Uptimes
double_trouble_1:47.24%
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
	Lucky Coin (fatebound_coin_flips)	13.4	80.1	93.4	23.3s	3.2s	10.2s	45.26%	0.00%	1.4 (1.4)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
cooldown name:buff_fatebound_coin_flips
max_stacks:7
base duration:150.00
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
interval_min/max:15.4s / 38.5s
trigger_min/max:0.0s / 20.0s
trigger_pct:100.00%
duration_min/max:0.0s / 25.7s
uptime_min/max:38.99% / 51.80%
Stack Uptimes
fatebound_coin_flips_1:6.90%
fatebound_coin_flips_2:7.47%
fatebound_coin_flips_3:7.62%
fatebound_coin_flips_4:7.67%
fatebound_coin_flips_5:7.73%
fatebound_coin_flips_6:7.88%
Spelldata
id:1248970
name:Lucky Coin
tooltip:
description:Every {$s1=7} coin flips, keep a lucky coin that bends you towards your fate for {$1248971d=12 seconds}. Your Agility is increased by {$1248971s1=4}%, the damage and bonuses of Fatebound Coins are increased by {$1248971s3=50}%, and coin flips are {$1248971s5=15}% more likely to match the same face as the last flip.
Coin flips do not count toward finding a lucky coin while you have a lucky coin.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:101.00%
	Fatebound Coin (Heads)	25.9	65.8	91.7	11.7s	0.0s	6.4s	50.17%	59.82%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
cooldown name:buff_fatebound_coin_heads
max_stacks:99
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
Damage Modifiers
direct:1.12 + 0.02/stack
periodic:1.12 + 0.02/stack
auto_attack:1.12 + 0.02/stack
crit_chance:1.00
is_stacking:true
Stack Uptimes
fatebound_coin_heads_1:9.43%
fatebound_coin_heads_2:11.33%
fatebound_coin_heads_3:8.77%
fatebound_coin_heads_4:6.27%
fatebound_coin_heads_5:4.45%
fatebound_coin_heads_6:3.13%
fatebound_coin_heads_7:2.13%
fatebound_coin_heads_8:1.46%
fatebound_coin_heads_9:1.01%
fatebound_coin_heads_10:0.69%
fatebound_coin_heads_11:0.48%
fatebound_coin_heads_12:0.33%
fatebound_coin_heads_13:0.22%
fatebound_coin_heads_14:0.15%
fatebound_coin_heads_15:0.10%
fatebound_coin_heads_16:0.07%
fatebound_coin_heads_17:0.05%
fatebound_coin_heads_18:0.03%
fatebound_coin_heads_19:0.02%
fatebound_coin_heads_20:0.02%
fatebound_coin_heads_21:0.01%
fatebound_coin_heads_22:0.01%
fatebound_coin_heads_23:0.01%
fatebound_coin_heads_24:0.00%
fatebound_coin_heads_25:0.00%
fatebound_coin_heads_26:0.00%
fatebound_coin_heads_27:0.00%
fatebound_coin_heads_28:0.00%
fatebound_coin_heads_29:0.00%
fatebound_coin_heads_30:0.00%
fatebound_coin_heads_31:0.00%
fatebound_coin_heads_32:0.00%
fatebound_coin_heads_33:0.00%
Spelldata
id:452923
name:Fatebound Coin (Heads)
tooltip:Damage increased by {$=}w1%.$?a454300[ Leech increased by {$=}{{$=}W3}.1%.][]
description:Flip a Fatebound Coin each time a finishing move consumes {$452536s1=5} or more combo points. Heads increases the damage of your attacks by {$=}{{$s3=2}+{$s1=2}}%, lasting {$d=15 seconds} or until you flip Tails.
For each time the same face is flipped in a row, Heads increases damage by an additional {$s1=2}%.
max_stacks:99
duration:15.00
cooldown:0.00
default_chance:101.00%
	Fatebound Coin (Tails)	25.1	65.3	90.4	11.9s	0.0s	6.5s	49.99%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
cooldown name:buff_fatebound_coin_tails
max_stacks:99
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
Stack Uptimes
fatebound_coin_tails_1:9.60%
fatebound_coin_tails_2:11.10%
fatebound_coin_tails_3:8.69%
fatebound_coin_tails_4:6.25%
fatebound_coin_tails_5:4.46%
fatebound_coin_tails_6:3.13%
fatebound_coin_tails_7:2.13%
fatebound_coin_tails_8:1.44%
fatebound_coin_tails_9:1.01%
fatebound_coin_tails_10:0.69%
fatebound_coin_tails_11:0.48%
fatebound_coin_tails_12:0.32%
fatebound_coin_tails_13:0.21%
fatebound_coin_tails_14:0.15%
fatebound_coin_tails_15:0.10%
fatebound_coin_tails_16:0.07%
fatebound_coin_tails_17:0.05%
fatebound_coin_tails_18:0.03%
fatebound_coin_tails_19:0.02%
fatebound_coin_tails_20:0.02%
fatebound_coin_tails_21:0.01%
fatebound_coin_tails_22:0.01%
fatebound_coin_tails_23:0.01%
fatebound_coin_tails_24:0.00%
fatebound_coin_tails_25:0.00%
fatebound_coin_tails_26:0.00%
fatebound_coin_tails_27:0.00%
fatebound_coin_tails_28:0.00%
fatebound_coin_tails_29:0.00%
fatebound_coin_tails_30:0.00%
fatebound_coin_tails_31:0.00%
fatebound_coin_tails_32:0.00%
Spelldata
id:452917
name:Fatebound Coin (Tails)
tooltip:Fatebound Coin damage increased by {$=}w1%.$?a454300[ Leech increased by {$=}{{$=}W2}.1%.][]
description:Flip a Fatebound Coin each time a finishing move consumes {$452536s1=5} or more combo points. Tails deals {$s1=10} Cosmic damage to your target.
For each time the same face is flipped in a row, Tails increases its damage by {$s1=10}%.
max_stacks:99
duration:15.00
cooldown:0.00
default_chance:101.00%
	(fatebound_) Lucky Coin	12.9	0.0	12.9	23.3s	23.3s	11.8s	50.69%	0.00%	0.0 (0.0)	12.4
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
cooldown name:buff_fatebound_lucky_coin
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
Stat Details
Trigger Details
interval_min/max:15.5s / 40.0s
trigger_min/max:15.5s / 40.0s
trigger_pct:100.00%
duration_min/max:0.0s / 12.0s
uptime_min/max:44.79% / 56.25%
Stack Uptimes
fatebound_lucky_coin_1:50.69%
Spelldata
id:1248971
name:Lucky Coin
tooltip:Agility increased by {$=}w1%. Damage and bonuses of Fatebound Coins increased by {$=}w3%. Coin flips are {$=}w5% more likely to match the same face as the last flip.
description:{$@spelldesc1248970=Every {$s1=7} coin flips, keep a lucky coin that bends you towards your fate for {$1248971d=12 seconds}. Your Agility is increased by {$1248971s1=4}%, the damage and bonuses of Fatebound Coins are increased by {$1248971s3=50}%, and coin flips are {$1248971s5=15}% more likely to match the same face as the last flip.
Coin flips do not count toward finding a lucky coin while you have a lucky coin.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:0.00%
	Gravedigger	11.4	0.0	11.4	25.2s	25.2s	6.0s	22.56%	22.78%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:12.2s / 73.4s
trigger_min/max:12.2s / 73.4s
trigger_pct:100.00%
duration_min/max:0.0s / 26.2s
uptime_min/max:10.40% / 36.71%
Stack Uptimes
gravedigger_1:22.56%
Spelldata
id:1265935
name:Gravedigger
tooltip:Your next Between the Eyes costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.
description:{$@spelldesc1265863=When you Dispatch you have a {$s1=12}% chance per combo point spent to hide a bullet up your sleeve. When you've hidden {$s2=6} bullets, your next Between the Eyes consumes them and costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.}
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:100.00%
	Jackpot	1.0	0.0	1.0	119.5s	105.4s	53.5s	17.59%	26.53%	0.0 (0.0)	0.8
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:30.1s / 334.6s
trigger_min/max:30.1s / 304.6s
trigger_pct:100.00%
duration_min/max:0.0s / 90.0s
uptime_min/max:0.00% / 94.79%
Stack Uptimes
jackpot_1:17.59%
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
	Light's Potential	1.5	0.0	1.5	302.3s	302.3s	27.4s	13.39%	0.00%	0.0 (0.0)	1.2
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
uptime_min/max:9.96% / 18.13%
Stack Uptimes
lights_potential_1:13.39%
Spelldata
id:1236616
name:Light's Potential
tooltip:Primary stat increased by {$=}w1.
description:Drink to increase your primary stat by {$s1=365} for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Loaded Dice	7.0	2.4	9.5	45.2s	35.7s	29.1s	58.22%	99.08%	2.4 (2.4)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:14.7s / 111.5s
trigger_min/max:15.0s / 59.3s
trigger_pct:100.00%
duration_min/max:0.0s / 76.2s
uptime_min/max:29.13% / 78.87%
Stack Uptimes
loaded_dice_1:58.22%
Spelldata
id:256171
name:Loaded Dice
tooltip:The result of your next Roll the Bones will be improved by one level.
description:{$@spelldesc256170=Activating Adrenaline Rush improves the result of your next Roll the Bones by one level.}
max_stacks:0
duration:45.00
cooldown:0.00
default_chance:100.00%
	Might of the Void	8.1	8.6	16.7	36.4s	17.0s	21.4s	58.01%	0.00%	8.6 (8.6)	7.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:15.0s / 165.1s
trigger_min/max:0.0s / 77.3s
trigger_pct:100.00%
duration_min/max:0.0s / 144.4s
uptime_min/max:30.93% / 86.18%
Stack Uptimes
might_of_the_void_1:58.01%
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
	One of a Kind	0.0	0.0	0.0	16.2s	16.2s	10.6s	0.13%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:13.1s / 18.9s
trigger_min/max:13.1s / 18.9s
trigger_pct:100.00%
duration_min/max:0.3s / 22.1s
uptime_min/max:0.00% / 9.03%
Stack Uptimes
one_of_a_kind_1:0.13%
Spelldata
id:1214933
name:One of a Kind
tooltip:Sinister Strike has a {$=}w1% increased chance to strike twice and grant Opportunity.
description:$@spelldesc1214774
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:0.00%
	Opportunity	29.5	33.4	62.9	10.2s	4.8s	7.7s	75.72%	100.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:3.0s / 103.0s
trigger_min/max:0.8s / 24.8s
trigger_pct:70.16%
duration_min/max:0.0s / 101.5s
uptime_min/max:56.43% / 90.45%
Stack Uptimes
opportunity_1:0.96%
opportunity_2:0.96%
opportunity_3:46.42%
opportunity_4:1.10%
opportunity_5:1.10%
opportunity_6:25.18%
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
	Palmed Bullets	4.5	66.3	70.7	64.6s	4.1s	60.7s	90.84%	0.00%	0.2 (0.2)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:12.3s / 334.0s
trigger_min/max:0.8s / 36.3s
trigger_pct:100.00%
duration_min/max:0.0s / 348.8s
uptime_min/max:76.48% / 98.31%
Stack Uptimes
palmed_bullets_1:10.17%
palmed_bullets_2:12.91%
palmed_bullets_3:14.63%
palmed_bullets_4:15.46%
palmed_bullets_5:15.11%
palmed_bullets_6:10.30%
palmed_bullets_7:6.74%
palmed_bullets_8:3.61%
palmed_bullets_9:1.41%
palmed_bullets_10:0.50%
Spelldata
id:1265931
name:Palmed Bullets
tooltip:{$=}w2 {$=}Lbullet:bullets; hidden up your sleeve. When you've hidden {$1265863s2=6} bullets, your next Between the Eyes consumes them and costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.
description:{$@spelldesc1265863=When you Dispatch you have a {$s1=12}% chance per combo point spent to hide a bullet up your sleeve. When you've hidden {$s2=6} bullets, your next Between the Eyes consumes them and costs no Energy, generates {$1279356s1=6} combo points, and immediately resets its own cooldown.}
max_stacks:10
duration:30.00
cooldown:0.00
default_chance:101.00%
	Precision of the Dragonhawk	8.2	8.5	16.7	36.4s	17.1s	21.4s	58.13%	0.00%	8.5 (8.5)	7.5
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:15.0s / 155.9s
trigger_min/max:0.0s / 74.7s
trigger_pct:100.00%
duration_min/max:0.0s / 147.0s
uptime_min/max:32.25% / 87.79%
Stack Uptimes
precision_of_the_dragonhawk_1:58.13%
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
	Roll the Bones	6.4	0.0	6.5	50.4s	51.3s	46.2s	99.14%	0.00%	0.0 (0.0)	5.4
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:30.0s / 90.8s
trigger_min/max:6.9s / 62.9s
trigger_pct:100.00%
duration_min/max:0.0s / 90.0s
uptime_min/max:97.97% / 99.93%
Stack Uptimes
roll_the_bones_1:99.14%
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
	Slice and Dice	1.0	0.0	1.0	0.0s	0.0s	300.0s	100.00%	90.11%	99.5 (99.5)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
cooldown name:buff_slice_and_dice
max_stacks:1
base duration:6.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.50
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
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
	Supercharge (_1)	9.5	0.0	9.5	33.3s	35.7s	2.0s	6.23%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:14.7s / 59.3s
trigger_min/max:15.0s / 59.3s
trigger_pct:100.00%
duration_min/max:0.0s / 6.7s
uptime_min/max:3.85% / 9.44%
Stack Uptimes
supercharge_1_1:6.23%
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
	Supercharge (_2)	9.5	0.0	9.5	33.3s	35.7s	1.2s	1.11%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
cooldown name:buff_supercharge_2
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
interval_min/max:14.7s / 59.3s
trigger_min/max:15.0s / 59.3s
trigger_pct:100.00%
duration_min/max:0.0s / 3.2s
uptime_min/max:0.45% / 3.00%
Stack Uptimes
supercharge_2_1:1.11%
Spelldata
id:470406
name:Supercharge
tooltip:Rogue's second combo point is supercharged.
Damaging finishing moves consume a supercharged combo point to function as if they spent {$470347s2=2} additional combo points.
description:{$@spelldesc470347={$?a137035=false}[Shadow Dance]?a137036[Adrenaline Rush][Kingsbane] supercharges {$m1=1} combo {$=}Lpoint:points;.
Damaging finishing moves consume a supercharged combo point to function as if they spent {$m2=2} additional combo {$=}Lpoint:points;.}
max_stacks:1
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Triple Threat	1.9	0.0	1.9	106.5s	97.1s	53.4s	34.19%	37.50%	0.0 (0.0)	1.6
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:30.0s / 334.2s
trigger_min/max:30.0s / 303.7s
trigger_pct:100.00%
duration_min/max:0.0s / 90.0s
uptime_min/max:0.00% / 99.72%
Stack Uptimes
triple_threat_1:34.19%
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
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
	Whirl of Blades	25.9	0.5	26.5	11.8s	11.7s	8.0s	69.48%	76.75%	0.5 (0.5)	25.3
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:8.0s / 27.6s
trigger_min/max:1.8s / 25.4s
trigger_pct:100.00%
duration_min/max:0.0s / 23.5s
uptime_min/max:55.43% / 80.31%
Stack Uptimes
whirl_of_blades_1:69.48%
Spelldata
id:1275176
name:Whirl of Blades
tooltip:Damage dealt increased by {$=}w1%.
description:{$@spelldesc1264859=Blade Rush's cooldown is reduced by {$=}{-{$s1=6000}/1000} sec and it increases your damage dealt by {$1275176s1=5}% for {$1275176d=8 seconds}.}
max_stacks:0
duration:8.00
cooldown:0.00
default_chance:0.00%
	Zero In	46.7	339.8	386.5	6.4s	0.8s	5.8s	89.84%	93.55%	9.5 (9.5)	0.0
Buff Details
buff initial source:MID1_Rogue_Outlaw_Fatebound
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
interval_min/max:0.0s / 32.5s
trigger_min/max:0.0s / 10.4s
trigger_pct:100.00%
duration_min/max:0.0s / 30.1s
uptime_min/max:83.20% / 95.19%
Stack Uptimes
zero_in_1:9.99%
zero_in_2:8.89%
zero_in_3:7.54%
zero_in_4:6.78%
zero_in_5:6.36%
zero_in_6:6.07%
zero_in_7:5.83%
zero_in_8:5.52%
zero_in_9:5.16%
zero_in_10:4.74%
zero_in_11:4.25%
zero_in_12:3.71%
zero_in_13:3.14%
zero_in_14:2.61%
zero_in_15:2.12%
zero_in_16:1.69%
zero_in_17:1.33%
zero_in_18:1.03%
zero_in_19:0.78%
zero_in_20:2.29%
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
	Roll the Bones Buff Lost: one_of_a_kind	0.0	0.0	2.0	10.4s	8.5s	13.5s
	Roll the Bones Buffs: 1	0.0	0.0	2.0	16.2s	13.1s	18.9s
	Roll the Bones Buffs: 2	3.5	0.0	9.0	72.7s	30.0s	333.1s
	Roll the Bones Buffs: 3	1.9	0.0	6.0	106.5s	30.0s	334.2s
	Roll the Bones Buffs: 4	1.0	0.0	5.0	119.5s	30.1s	334.6s
	Skyfury (Main Hand)	46.7	22.0	76.0	6.4s	0.6s	100.2s
	Skyfury (Off Hand)	67.5	36.0	105.0	4.4s	0.4s	58.7s
	Supercharger between_the_eyes	14.8	6.0	23.0	20.2s	0.8s	141.8s
	Supercharger dispatch	4.0	0.0	10.0	65.1s	1.6s	326.0s
```

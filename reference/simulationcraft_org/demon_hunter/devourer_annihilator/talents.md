# MID1_Demon_Hunter_Devourer_Annihilator — Talents & Gear

## Talent Export String
```
CgcBAAAAAAAAAAAAAAAAAAAAAAA2MmZmZmZmBzMAAAAAAALzYAzAAAAAAAAwMGMmZmZMzMzYmFzYsotNmZmZ2abmZGAjZAIwMzgxMA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	108,624.8	108,624.8	98.3 / 0.091%	16,843.8 / 15.5%	7,022.3
	Resource
	Out
	In
	Waiting
	APM
	Active
	Fury	15.5	15.7	0.00%	48.9	100.0%
	Talent	CgcBAAAAAAAAAAAAAAAAAAAAAAA2MmZmZmZmBzMAAAAAAALzYAzAAAAAAAAwMGMmZmZMzMzYmFzYsotNmZmZ2abmZGAjZAIwMzgxMA
	Set Bonus
Devouring Reaver's Sheathe (MID1)
Demon Hunter Devourer 12.0 Class Set 2pc (2pc)
Demon Hunter Devourer 12.0 Class Set 4pc (4pc)
Charts
Abilities
	Damage Stats
	DPS
	DPS%
	Execute
	Interval
	Total Time
	DPE
	DPET
	Type
	Count
	Hit
	Crit
	Avg
	Crit%
	Up%
	MID1_Demon_Hunter_Devourer_Annihilator	108,625
	Catastrophe
	3,074	2.8%	0.0	0.00s	0.0s	0	0	Periodic	121.2	7,612	0	7,612	0.0%	80.8%
Stats Details: Catastrophe
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	121.20	121.20	124.08	0.0000	2.0000	922,559.19	922,559.19	0.00%	3,805.81	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	100.00%	121.20	85	160	7,611.58	922	34,415	7,612.18	6,142	9,299	922,559	922,559	0.00%
Action Details: Catastrophe
id:1256676
school:cosmic
range:100.0
travel_speed:0.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Damage Over Time
tick_may_crit:false
tick_zero:false
tick_on_application:false
rolling_periodic:true
attack_power_mod.tick:0.000000
spell_power_mod.tick:0.000000
base_td:0.000000
base_td_mult:1.000000
base_multiplier:1.000000
dot_duration:8.00
base_tick_time:2.00
hasted_ticks:false
dot_behavior:unknown
Spelldata
id:1256676
name:Catastrophe
school:cosmic
tooltip:Suffering {$=}w1 Cosmic damage every {$t1=2} sec.
description:{$@spelldesc1253769=Enemies struck by a Voidfall Meteor take an additional {$?a212613=false}[{$s1=25}%][{$s2=25}%] damage over {$1256667d=8 seconds}.}
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Demon Soul	163073	#1	20.0%	Spell Data
	Demon Soul	347765	#1	20.0%	Spell Data
	Periodic Damage
	Demon Soul	163073	#2	20.0%	Spell Data
	Demon Soul	347765	#2	20.0%	Spell Data
	Collapsing Star
	0 (25,709)	0.0% (23.7%)	16.4	17.53s	31.0s / 10.3%	471,437	248,919
Stats Details: Collapsing Star
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	16.37	0.00	0.00	0.00	0.00	1.8940	0.0000	0.00	0.00	0.00%	248,919.02	248,919.02
Action Details: Collapsing Star
id:1221150
school:cosmic
range:25.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:5.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:3.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:1221150
name:Collapsing Star
school:cosmic
tooltip:
description:Channel an immense amount of void energy into a single, cataclysmic blast, {$?a1242486=true}[critically striking for {$=}{{$1221162s1=0}*2}][dealing {$1221162s1=0}] Cosmic damage to your target and {$?a1242486=true}[{$=}{2*({$1221162s1=0}*({$s2=75}/100))}][{$=}{{$1221162s1=0}*({$s2=75}/100)}] Cosmic damage to all nearby enemies. Damage reduced beyond {$s1=8} targets.
While casting Collapsing Star, your Fury drain is significantly reduced.{$?a1240204=true}[
|CFFffffffGenerates {$1240204s1=3} Soul {$=}LFragment:Fragments;|R.][]
Action Priority List
default[R]:16.48
if_expr:variable.should_use_star
Collapsing Star (_damage)
	23,896	22.0%	0.0	0.00s	0.0s	0	0	Direct	16.4	0	438,418	438,418	100.0%
Stats Details: Collapsing Star Damage
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	16.37	0.00	0.00	0.00	0.0000	0.0000	7,175,414.43	7,175,414.43	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	16.37	11	22	438,418.18	163,217	1,055,858	437,435.91	361,166	530,488	7,175,414	7,175,414	0.00%
Action Details: Collapsing Star Damage
id:1221162
school:cosmic
range:25.0
travel_speed:44.0000
radius:8.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:1.00
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
reduced_aoe_targets:8
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:5.625000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.107700
base_multiplier:1.000000
Spelldata
id:1221162
name:Collapsing Star
school:cosmic
tooltip:
description:{$@spelldesc1221150=Channel an immense amount of void energy into a single, cataclysmic blast, {$?a1242486=true}[critically striking for {$=}{{$1221162s1=0}*2}][dealing {$1221162s1=0}] Cosmic damage to your target and {$?a1242486=true}[{$=}{2*({$1221162s1=0}*({$s2=75}/100))}][{$=}{{$1221162s1=0}*({$s2=75}/100)}] Cosmic damage to all nearby enemies. Damage reduced beyond {$s1=8} targets.
While casting Collapsing Star, your Fury drain is significantly reduced.{$?a1240204=true}[
|CFFffffffGenerates {$1240204s1=3} Soul {$=}LFragment:Fragments;|R.][]}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Midnight	1242486	#1	100.0%	Talent
	Crit Bonus	Calamitous	1242495	#1	40.0%	Talent
	Direct Damage	Devourer Demon Hunter	1213636	#1	-5.0%	Spec Spell
	Midnight	1250088	#4	6.0%	Talent
	Demon Hunter Devourer 12.0 Class Set 4pc	1264882	#1	10.0%	Set Bonus
	Periodic Damage	Devourer Demon Hunter	1213636	#2	-5.0%	Spec Spell
	Midnight	1250088	#5	6.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Monster Within	1238855	#1	1.00000	Spell Data	Mastery, Passive, Value-function
	Void Metamorphosis	1217607	#4	1.20000	Spell Data	Mastery
	Feast of Souls	1232310	#1	1.0%	Spell Data
	Rolling Torment	1244235	#1	0.5%	Spell Data
	Impending Apocalypse	1227338	#1	30.0%	Spell Data
	Periodic Damage
	Mastery: Monster Within	1238855	#2	1.00000	Spell Data	Mastery, Passive, Value-function
	Void Metamorphosis	1217607	#5	1.20000	Spell Data	Mastery
	Feast of Souls	1232310	#2	1.0%	Spell Data
	Rolling Torment	1244235	#2	0.5%	Spell Data
	Damage on Debuff
	Devourer's Bite	1241532	#1	12.0%
Meteor Shower
	0 (1,814)	0.0% (1.7%)	4.4	72.21s	0.0s	122,833	0
Stats Details: Meteor Shower
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	4.42	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Meteor Shower
id:1264126
school:cosmic
range:100.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:1264126
name:Meteor Shower
school:cosmic
tooltip:
description:{$@spelldesc153561=Calls down a meteor which lands at the target location after {$177345d=3 seconds}, dealing {$351140s1=0} Fire damage to all enemies, and burns the ground, dealing {$=}{8*{$155158s1=0}} Fire damage over {$175396d=4 seconds} to all enemies in the area.
{$?a1254857=false}[The enemy closest to the center of the Meteor's impact takes {$1254857s1=75}% increased damage. ][]Damage reduced beyond 8 targets.}
Meteor Shower (_damage)
	1,814	1.7%	0.0	0.00s	0.0s	0	0	Direct	52.6	8,611	20,661	10,324	14.2%
Stats Details: Meteor Shower Damage
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	52.60	0.00	0.00	0.00	0.0000	0.0000	543,066.52	543,066.52	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	85.78%	45.12	25	60	8,610.81	5,751	14,502	8,616.65	7,500	9,927	388,540	388,540	0.00%
	crit	14.22%	7.48	0	18	20,661.10	13,919	34,120	20,660.22	0	29,765	154,526	154,526	0.00%
Action Details: Meteor Shower Damage
id:1264129
school:cosmic
range:100.0
travel_speed:0.0000
radius:6.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.500000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.158050
base_multiplier:1.000000
Spelldata
id:1264129
name:Meteor Shower
school:cosmic
tooltip:
description:{$@spelldesc1256307=Your first {$?a212613=false}[Spirit Bomb][Collapsing Star] after {$?a212613=false}[entering demon form][casting Void Metamorphosis] causes a {$?a212613=false}[Shadowflame][Cosmic] meteor shower to assault the area, dealing {$?a212613=false}[{$=}{{$1264130s1=0}*({$s1=12})} Shadowflame][{$=}{{$1264129s1=0}*({$s1=12})} Cosmic] damage over {$=}{{$s1=12}/2} sec.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Calamitous	1242495	#1	40.0%	Talent
	Direct Damage	Devourer Demon Hunter	1213636	#1	-5.0%	Spec Spell
	Harness the Cosmos	1279247	#1	15.0%	Talent
	Midnight	1250088	#4	6.0%	Talent
	Periodic Damage	Devourer Demon Hunter	1213636	#2	-5.0%	Spec Spell
	Harness the Cosmos	1279247	#2	15.0%	Talent
	Midnight	1250088	#5	6.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Monster Within	1238855	#1	1.00000	Spell Data	Mastery, Passive, Value-function
	Void Metamorphosis	1217607	#4	1.20000	Spell Data	Mastery
	Feast of Souls	1232310	#1	1.0%	Spell Data
	Rolling Torment	1244235	#1	0.5%	Spell Data
	Periodic Damage
	Mastery: Monster Within	1238855	#2	1.00000	Spell Data	Mastery, Passive, Value-function
	Void Metamorphosis	1217607	#5	1.20000	Spell Data	Mastery
	Feast of Souls	1232310	#2	1.0%	Spell Data
	Rolling Torment	1244235	#2
```

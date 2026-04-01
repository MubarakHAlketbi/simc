# MID1_Mage_Fire_Frostfire — Talents & Gear

## Talent Export String
```
C8DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMDZmZGAAAmZZGzMLzCEAAwiZmx2YmZGAAAAAgNzMzMDAAGzYmZmZmZ2AmZADzYMYwA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	105,174.2	105,174.2	66.3 / 0.063%	11,567.9 / 11.0%	21.1
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	4,981.0	4,933.3	0.00%	75.0	100.0%
	Talent	C8DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMDZmZGAAAmZZGzMLzCEAAwiZmx2YmZGAAAAAgNzMzMDAAGzYmZmZmZ2AmZADzYMYwA
	Set Bonus
Voidbreaker's Accordance (MID1)
Mage Fire 12.0 Class Set 2pc (2pc)
Mage Fire 12.0 Class Set 4pc (4pc)
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
	MID1_Mage_Fire_Frostfire	105,174
	Burnout
	5,400	5.1%	5.1	60.46s	0.0s	319,579	0	Direct	5.1	319,580	0	319,580	0.0%
Stats Details: Burnout
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	5.07	5.07	0.00	0.00	0.00	0.0000	0.0000	1,621,252.83	1,621,252.83	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	100.00%	5.07	4	6	319,579.51	184,583	634,734	319,970.87	270,450	371,082	1,621,253	1,621,253	0.00%
Action Details: Burnout
id:1271335
school:fire
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
Direct Damage
may_crit:false
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.000000
base_dd_min:302111.074187
base_dd_max:302111.074187
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:1271335
name:Burnout
school:fire
tooltip:
description:{$@spelldesc1271171=Fire Blast deals {$1271173s1=0} additional Fire damage to up to $s2 nearby enemies.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Fire Blast
	7,069	6.7%	89.4	3.36s	0.0s	23,714	0	Direct	89.4	0	23,713	23,713	100.0%
Stats Details: Fire Blast
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	89.38	89.38	0.00	0.00	0.00	0.0000	0.0000	2,119,522.95	2,119,522.95	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	89.38	64	113	23,713.46	14,896	42,521	23,690.93	21,566	25,774	2,119,523	2,119,523	0.00%
Action Details: Fire Blast
id:108853
school:frostfire
range:40.0
travel_speed:0.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
min_gcd:0.0000
cooldown:12.000
cooldown hasted:true
category cooldown:true
charges:3
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:1.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:mana
base_cost:2500
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.986250
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:2.063100
base_multiplier:1.000000
Spelldata
id:108853
name:Fire Blast
school:frostfire
tooltip:
description:Blasts the enemy, critically striking for {$=}{{$s1=0}*2} Fire damage.
Castable while casting other spells.
Action Priority List
fireblast[a]:47.10
if_expr:cooldown_react&!buff.hot_streak.react&(buff.combustion.up|buff.hyperthermia.up)&(hot_streak_spells_in_flight+buff.heating_up.react=1)&gcd.remains<gcd.max
fireblast[b]:24.18
if_expr:cooldown_react&!buff.hot_streak.react&(action.fireball.executing&action.fireball.execute_remains>0.1|buff.pyroclasm.react&action.pyroblast.executing&action.pyroblast.execute_remains>0.1)&((target.health.pct>=30|!talent.scorch)&buff.heating_up.react)&(hot_streak_spells_in_flight+buff.heating_up.react=1)&gcd.remains<gcd.max
fireblast[c]:7.97
if_expr:cooldown_react&!buff.hot_streak.react&time<variable.combustion_delay&(talent.firestarter|action.fireball.executing&action.fireball.execute_remains>0.1|buff.pyroclasm.react&action.pyroblast.executing&action.pyroblast.execute_remains>0.1)&(hot_streak_spells_in_flight+buff.heating_up.react=1)&gcd.remains<gcd.max&cooldown.combustion.ready
fireblast[d]:9.96
if_expr:talent.frostfire_bolt&target.health.pct<30&buff.combustion.down&cooldown.combustion.remains>5
fireblast[e]:0.16
if_expr:fight_remains<1
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charge Cooldown	Flame On	205029	#2	-2000.0%	Talent
	Charges	Flame On	205029	#1	1.0%	Talent
	Fervent Flickering	387044	#1	1.0%	Talent
	Crit Bonus	Dualcasting Adept	1248014	#2	20.0%	Talent
	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Direct Damage	Heat Sink	1248002	#2	15.0%	Talent
	Frostfire Infusion	431166	#3	4.0%	Talent
	Fervent Flickering	387044	#2	25.0%	Talent
	From the Ashes	342344	#2	15.0%	Talent
	Wildfire	1254828	#2	20.0%	Talent
	Hasted Cooldown	Mage	137018	#2	0.0%	Class Spell
	Periodic Damage	Frostfire Infusion	431166	#4	4.0%	Talent
	School	Heat Sink	1248002	#1	0.0%	Talent
	Frostfire Bolt
	26,489	25.2%	164.5	1.82s	189.5s / 63.2%	48,354	41,972	Direct	165.3	19,643	63,072	47,175	63.4%
	Periodic	404.4	160	486	384	68.6%	96.0%
Stats Details: Frostfire Bolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	164.50	165.32	404.42	404.42	159.66	1.1520	0.7119	7,954,186.70	7,954,186.70	0.00%	16,661.23	41,972.39
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	36.60%	60.51	40	84	19,643.14	15,256	45,125	19,642.84	17,313	22,563	1,188,673	1,188,673	0.00%
	crit	63.40%	104.81	79	131	63,071.55	35,031	164,706	62,964.04	56,504	71,338	6,610,381	6,610,381	0.00%
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	31.35%	126.80	82	175	160.25	8	262	160.26	148	175	20,319	20,319	0.00%
	crit	68.65%	277.62	212	351	485.60	35	920	485.15	453	526	134,814	134,814	0.00%
Action Details: Frostfire Bolt
id:431044
school:frostfire
range:40.0
travel_speed:40.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:1.57
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:mana
base_cost:5000
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:2.470000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.716000
base_multiplier:1.000000
Damage Over Time
tick_may_crit:true
tick_zero:false
tick_on_application:false
rolling_periodic:false
attack_power_mod.tick:0.000000
spell_power_mod.tick:0.025750
base_td:0.000000
base_td_mult:1.716000
base_multiplier:1.000000
dot_duration:8.00
base_tick_time:1.00
hasted_ticks:true
dot_behavior:DOT_REFRESH_DURATION
Spelldata
id:431044
name:Frostfire Bolt
school:frostfire
tooltip:
description:Launches a bolt of frostfire at the enemy, causing {$468655s1=0} Frostfire damage, slowing movement speed by {$205708s1=50}%, and causing an additional {$468655=}o2 Frostfire damage over {$468655d=8 seconds}.{$?a1246769=false}[
|CFFffffffApplies {$1246769s1=1} {$=}lstack:stacks; of Freezing.|R][]
Action Priority List
ff_combustion[Q]:3.45
if_expr:buff.combustion.down
ff_combustion[T]:7.92
ff_filler[Y]:153.90
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cast Time	Thermal Conditioning	431117	#1	-10.0%	Talent
Frostfire Empowerment
	0	0.0%	33.0	8.83s	0.0s
Stats Details: Frostfire Empowerment
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	33.02	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Frostfire Empowerment
id:431186
school:frostfire
range:40.0
travel_speed:0.0000
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
base_crit:0.00
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
reduced_aoe_targets:5
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:false
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.000000
base_dd_min:63286.793552
base_dd_max:63286.793552
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:431186
name:Frostfire Empowerment
school:frostfire
tooltip:
description:{$@spelldesc431176=Casting Frostfire spells has a {$s3=10}% chance to activate Frostfire Empowerment, causing your next Frostfire Bolt to be instant cast, deal {$431177s3=60}% increased damage, explode for {$s2=60}% of its damage to nearby enemies. Damage reduced beyond {$s5=5} targets.{$?=}c2[][
Damage from Frostfire Empowerment applies {$s4=1} {$=}Lstack:stacks; of Freezing.]}
	Ignite
	25,710	24.4%	930.3	0.32s	0.0s	8,291	0	Periodic	299.4	25,765	0	25,765	0.0%	99.8%
Stats Details: Ignite
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	930.32	0.00	299.37	299.37	929.32	0.0000	1.0000	7,713,173.46	7,713,173.46	0.00%	25,765.11	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	100.00%	299.37	239	359	25,765.01	1,872	105,585	25,765.98	22,770	28,987	7,713,173	7,713,173	0.00%
Action Details: Ignite
id:12654
school:fire
range:50000.0
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
base_td_mult:1.040000
base_multiplier:1.000000
dot_duration:9.00
base_tick_time:1.00
hasted_ticks:false
dot_behavior:unknown
Spelldata
id:12654
name:Ignite
school:fire
tooltip:Deals {$=}w1 Fire damage every {$t1=1} sec.{$?=}{$=}w3>0[
Movement speed reduc
```

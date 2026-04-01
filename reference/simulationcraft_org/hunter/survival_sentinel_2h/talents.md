# MID1_Hunter_Survival_Sentinel_2H — Talents & Gear

## Talent Export String
```
C8PAAAAAAAAAAAAAAAAAAAAAAMWgBmxoxyAYmgNjZmxMPwy8AAAAAAAMjZmZYGDjZwYaGAAAAwAAYZbmZWMzMzYmZMAMDbMMGzYjB
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	108,604.8	108,604.8	70.4 / 0.065%	12,108.8 / 11.1%	6,365.1
	Resource
	Out
	In
	Waiting
	APM
	Active
	Focus	12.9	12.7	0.30%	47.8	100.0%
	Talent	C8PAAAAAAAAAAAAAAAAAAAAAAMWgBmxoxyAYmgNjZmxMPwy8AAAAAAAMjZmZYGDjZwYaGAAAAwAAYZbmZWMzMzYmZMAMDbMMGzYjB
	Set Bonus
Root Warden's Regalia (MID_RWR)
Root Warden's Regalia (2pc)
Voidlight Bindings (MID_VB)
Voidlight Bindings (2pc)
Primal Sentry's Camouflage (MID1)
Hunter Beast Survival 12.0 Class Set 2pc (2pc)
Hunter Beast Survival 12.0 Class Set 4pc (4pc)
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
	MID1_Hunter_Survival_Sentinel_2H	108,605
	auto_attack_mh
	8,463	7.8%	137.1	2.64s	0.0s	18,528	7,509	Direct	137.1	13,792	28,280	18,528	32.7%
Stats Details: Auto Attack Mh
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	137.06	137.06	0.00	0.00	0.00	2.4675	0.0000	2,539,444.52	3,627,777.89	30.00%	7,508.91	7,508.91
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	67.31%	92.25	58	130	13,791.68	11,793	19,370	13,782.61	13,116	14,600	1,272,295	1,817,564	30.00%
	crit	32.69%	44.81	21	73	28,279.56	24,179	39,789	28,260.61	26,521	30,499	1,267,150	1,810,214	30.00%
Action Details: Auto Attack Mh
id:0
school:physical
range:5.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:0.0000
gcd_type:none
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:3.60
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
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:1.000000
	Boomstick
	0 (6,709)	0.0% (6.2%)	6.9	46.78s	18.5s / 6.2%	291,543	108,655
Stats Details: Boomstick
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	6.90	0.00	27.49	0.00	0.00	2.6833	0.6101	0.00	0.00	0.00%	108,654.97	108,654.97
Action Details: Boomstick
id:1261193
school:physical
range:20.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:45.000
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
resource:focus
base_cost:50
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Damage Over Time
tick_may_crit:false
tick_zero:true
tick_on_application:true
rolling_periodic:false
attack_power_mod.tick:0.000000
spell_power_mod.tick:0.000000
base_td:0.000000
base_td_mult:1.000000
base_multiplier:1.000000
dot_duration:3.00
base_tick_time:1.00
hasted_ticks:true
dot_behavior:DOT_REFRESH_PANDEMIC
Spelldata
id:1261193
name:Boomstick
school:physical
tooltip:
description:Unload a series of {$=}{({$d=3 seconds}/{$t1=1})+1} shotgun blasts {$s3=20} yds in front of you, dealing {$=}{{$1261215s1=0}*4} Physical damage over {$d=3 seconds}. Deals reduced damage beyond {$s2=8} targets.
Action Priority List
sentst[C]:5.70
if_expr:buff.tip_of_the_spear.up&!cooldown.takedown.ready&!debuff.sentinels_mark.remains
sentst[F]:1.20
if_expr:buff.tip_of_the_spear.up
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	Quick Reload	1272136	#1	-15000.0	Talent
	Crit Bonus	Vulnerability	1257011	#1	20.0%	Talent
	Direct Damage	Explosives Expert	378937	#1	5.0%	Talent
Boomstick (_damage)
	6,709	6.2%	27.5	10.50s	0.0s	73,145	0	Direct	27.5	50,604	119,722	73,142	32.6%
Stats Details: Boomstick Damage
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	27.49	27.49	0.00	0.00	0.00	0.0000	0.0000	2,010,551.51	2,872,216.44	30.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	67.39%	18.52	8	29	50,603.62	41,257	76,595	50,608.69	44,011	57,947	937,336	1,339,052	30.00%
	crit	32.61%	8.96	1	19	119,722.00	96,377	182,842	119,742.56	100,441	156,893	1,073,215	1,533,165	30.00%
Action Details: Boomstick Damage
id:1261215
school:physical
range:20.0
travel_speed:0.0000
radius:20.0
trigger_gcd:0.0000
gcd_type:none
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
reduced_aoe_targets:8
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:1261215
name:Boomstick
school:physical
tooltip:
description:{$@spelldesc1261193=Unload a series of {$=}{({$d=3 seconds}/{$t1=1})+1} shotgun blasts {$s3=20} yds in front of you, dealing {$=}{{$1261215s1=0}*4} Physical damage over {$d=3 seconds}. Deals reduced damage beyond {$s2=8} targets.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Vulnerability	1257011	#1	20.0%	Talent
	Direct Damage	Explosives Expert	378937	#1	5.0%	Talent
	Lunar Storm
	8,065	7.4%	0.0	0.00s	0.0s	0	0	Direct	135.1	12,966	28,089	17,911	32.7%
Stats Details: Lunar Storm
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	135.12	0.00	0.00	0.00	0.0000	0.0000	2,420,127.84	2,420,127.84	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	67.30%	90.94	40	140	12,965.73	10,442	20,382	12,961.66	11,888	14,472	1,179,101	1,179,101	0.00%
	crit	32.70%	44.18	15	80	28,088.72	22,287	44,236	28,078.07	25,076	31,475	1,241,027	1,241,027	0.00%
Action Details: Lunar Storm
id:1253733
school:arcane
range:100.0
travel_speed:0.0000
radius:10.0
trigger_gcd:0.0000
gcd_type:attack_haste
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
reduced_aoe_targets:8
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:1253733
name:Lunar Storm
school:arcane
tooltip:
description:{$@spelldesc1253732=When Sentinel's Mark is consumed, it summons a barrage of {$s1=4} lunar missiles, each dealing {$1253733s1=0} Arcane damage to enemies within {$s2=10} yds.}
	Moonlight Chakram
	0 (8,772)	0.0% (8.1%)	5.3	61.16s	6.4s / 2.1%	495,182	408,243
Stats Details: Moonlight Chakram
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	5.32	0.00	0.00	0.00	0.00	1.2131	0.0000	0.00	0.00	0.00%	408,243.32	408,243.32
Action Details: Moonlight Chakram
id:1264949
school:arcane
range:40.0
travel_speed:60.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
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
id:1264949
name:Moonlight Chakram
school:arcane
tooltip:
description:Throw a chakram blessed with moonlight at your current target that will rapidly deal {$1266081s1=0} Physical damage {$=}x times, bouncing to other targets if they are nearby.
Action Priority List
sentst[G]:5.32
if_expr:buff.tip_of_the_spear.up
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Hasted Gcd	Hunter	137014	#3	0.0%	Class Spell
Moonlight Chakram (_damage)
	8,772	8.1%	0.0	0.00s	0.0s	0	0	Direct	37.1	51,256	111,149	70,890	32.8%
Stats Details: Moonlight Chakram Damage
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	37.14	0.00	0.00	0.00	0.0000	0.0000	2,632,761.19	3,761,087.42	30.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	67.22%	24.96	11	40	51,256.21	17,176	120,889	51,182.45	38,842	62,737	1,279,560	1,827,943	30.00%
	crit	32.78%	12.17	2	25	111,148.91	37,085	263,096	110,982.06	58,389	198,860	1,353,201	1,933,145	30.00%
Action Details: Moonlight Chakram Damage
id:1266081
school:physical
range:100.0
travel_speed:0.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:attack_haste
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
id:1266081
name:Moonlight Chakram
school:physical
tooltip:
description:{$@spelldesc1264949=Throw a chakram blessed with moonlight at your current target that will rapidly deal {$1266081s1=0} Physical damage {$=}x times, bouncing to other targets if they are nearby.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Hasted Gcd	Hunter	137014	#3	0.0%	Class Spell
	Raptor Strike
	10,098 (22,202)	9.3% (20.4%)	51.8	5.66s	125.9s / 42.0%	128,647	52,937	Direct	51.8	40,261	95,998	58,514	32.7%
Stats Details: Raptor Strike
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	51.79	51.79	0.00	0.00	0.00	2.4302	0.0000	3,030,304.78	4,329,006.83	30.00%	52,936.65	52,936.65
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	67.25%	34.83	18	52	40,260.82	23,208	68,808	40,244.19	37,193	43,602	1,402,245	2,003,208	30.00%
	crit	32.75%	16.96
```

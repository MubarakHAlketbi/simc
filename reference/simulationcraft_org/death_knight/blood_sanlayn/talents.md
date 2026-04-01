# MID1_Death_Knight_Blood_San'layn — Talents & Gear

## Talent Export String
```
CoPAAAAAAAAAAAAAAAAAAAAAAwYWGzMmZmZmhZbmZmmZxMjhxAAAAAzMzMzwMzYmZMDAMzMzAAAwADMjNNW2AZZAbAmhBAAMzgBGA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	59,890.5	59,890.5	58.3 / 0.097%	10,060.0 / 16.8%	4,498.9
	HPS
	HPS(e)
	HPS Error
	HPS Range
	HPR
	43,083.3	43,083.3	48.9 / 0.114%	8,479.8 / 19.7%	3,924.9
	APS
	APS Error
	APS Range
	APR
	22,493.3	23.8 / 0.106%	3,020.4 / 13.4%	3,924.9
	DTPS
	DTPS Error
	DTPS Range
	78,203.0	92.99 / 0.12%	15,787 / 20.2%
	Resource
	Out
	In
	Waiting
	APM
	Active
	Runic Power	11.0	11.1	0.02%	67.3	100.0%
	Talent	CoPAAAAAAAAAAAAAAAAAAAAAAwYWGzMmZmZmhZbmZmmZxMjhxAAAAAzMzMzwMzYmZMDAMzMzAAAwADMjNNW2AZZAbAmhBAAMzgBGA
	Set Bonus
Voidlight Bindings (MID_VB)
Voidlight Bindings (2pc)
Relentless Rider's Lament (MID1)
Death Knight Blood 12.0 Class Set 2pc (2pc)
Death Knight Blood 12.0 Class Set 4pc (4pc)
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
	MID1_Death_Knight_Blood_San'layn	59,890
	auto_attack_mh
	5,375	9.0%	200.3	1.79s	0.0s	8,051	4,473	Direct	200.3	6,469	12,931	8,051	24.5%
Stats Details: Auto Attack Mh
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	200.34	200.34	0.00	0.00	0.00	1.8001	0.0000	1,613,017.63	2,304,310.90	30.00%	4,472.75	4,472.75
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	75.51%	151.27	101	204	6,468.52	4,623	12,777	6,464.47	6,035	6,930	978,521	1,397,887	30.00%
	crit	24.49%	49.07	21	78	12,931.41	9,247	25,555	12,923.07	11,418	14,613	634,497	906,424	30.00%
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
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Dance of Midnight	1264407	#5	6.0%	Spell Data
	Blood Boil
	2,728	4.5%	48.4	6.16s	44.9s / 15.0%	16,901	18,220	Direct	48.4	13,602	27,167	16,901	24.3%
Stats Details: Blood Boil
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	48.40	48.40	0.00	0.00	0.00	0.9276	0.0000	818,006.82	818,006.82	0.00%	18,220.04	18,220.04
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	75.68%	36.63	19	54	13,601.78	8,096	38,344	13,604.94	11,293	16,424	498,218	498,218	0.00%
	crit	24.32%	11.77	1	28	27,167.34	16,192	75,927	27,183.95	18,466	40,632	319,789	319,789	0.00%
Action Details: Blood Boil
id:50842
school:shadow
range:0.0
travel_speed:0.0000
radius:10.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:7.500
cooldown hasted:true
category cooldown:true
charges:2
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
Spelldata
id:50842
name:Blood Boil
school:shadow
tooltip:
description:Deals {$s1=0} Shadow damage$?s212744[ to all enemies within {$=}A1 yds.][ and infects all enemies within {$=}A1 yds with Blood Plague.
{$@=}spellicon55078 |cFFFFFFFF{$@=}spellname55078|r
{$@spelldesc55078=A shadowy disease that drains {$=}o1 health from the target over {$d=24 seconds}. }]
Action Priority List
san_gift[E]:3.48
if_expr:!drw.bp_ticking
san_gift[I]:1.81
if_expr:buff.boiling_point.up&!buff.boiling_point_echo.up
san_gift[K]:0.04
sanlayn[T]:13.43
if_expr:buff.boiling_point.up&!buff.boiling_point_echo.up
sanlayn[V]:29.64
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Blood Death Knight	137008	#1	15.0%	Spec Spell
	Death Knight Blood 12.0 Class Set 2pc	1264799	#1	8.0%	Set Bonus
	Hasted Cooldown	Death Knight	137005	#3	108.0%	Class Spell
	Periodic Damage	Blood Death Knight	137008	#2	15.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Blood Shield	77535	#2	8.0%	Spell Data	No-stacks
	Boiling Point	1265968	#1	50.0%	Spell Data
	Dance of Midnight	1264407	#1	6.0%	Spell Data
	Sanguine Ground	391459	#1	6.0%	Spell Data
	Periodic Damage
	Blood Shield	77535	#3	8.0%	Spell Data	No-stacks
	Dance of Midnight	1264407	#2	6.0%	Spell Data
	Sanguine Ground	391459	#3	6.0%	Spell Data
	Damage on Debuff
	Brittle	374557	#1	6.0%
	Blood Plague	55078	#4	5.0%
	Blood Boil (_boiling_point)
	1,079	1.8%	19.5	14.60s	0.0s	16,607	0	Direct	19.3	13,515	27,016	16,801	24.3%
Stats Details: Blood Boil Boiling Point
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	19.52	19.30	0.00	0.00	0.00	0.0000	0.0000	324,236.93	324,236.93	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	75.66%	14.60	3	31	13,514.93	8,096	36,174	13,454.95	9,951	18,282	197,352	197,352	0.00%
	crit	24.34%	4.70	0	15	27,016.45	16,192	73,193	26,654.52	0	51,657	126,885	126,885	0.00%
Action Details: Blood Boil Boiling Point
id:50842
school:shadow
range:0.0
travel_speed:0.0000
radius:10.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:0.000
cooldown hasted:true
category cooldown:true
charges:2
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
Spelldata
id:50842
name:Blood Boil
school:shadow
tooltip:
description:Deals {$s1=0} Shadow damage$?s212744[ to all enemies within {$=}A1 yds.][ and infects all enemies within {$=}A1 yds with Blood Plague.
{$@=}spellicon55078 |cFFFFFFFF{$@=}spellname55078|r
{$@spelldesc55078=A shadowy disease that drains {$=}o1 health from the target over {$d=24 seconds}. }]
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Blood Death Knight	137008	#1	15.0%	Spec Spell
	Death Knight Blood 12.0 Class Set 2pc	1264799	#1	8.0%	Set Bonus
	Hasted Cooldown	Death Knight	137005	#3	108.0%	Class Spell
	Periodic Damage	Blood Death Knight	137008	#2	15.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Blood Shield	77535	#2	8.0%	Spell Data	No-stacks
	Boiling Point	1265968	#1	50.0%	Spell Data
	Dance of Midnight	1264407	#1	6.0%	Spell Data
	Sanguine Ground	391459	#1	6.0%	Spell Data
	Periodic Damage
	Blood Shield	77535	#3	8.0%	Spell Data	No-stacks
	Dance of Midnight	1264407	#2	6.0%	Spell Data
	Sanguine Ground	391459	#3	6.0%	Spell Data
	Damage on Debuff
	Brittle	374557	#1	6.0%
	Blood Plague	55078	#4	5.0%
	Blood Draw
	95	0.2%	2.7	120.98s	0.0s	10,318	0	Direct	2.7	8,328	16,665	10,318	23.9%
Stats Details: Blood Draw
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	2.75	2.75	0.00	0.00	0.00	0.0000	0.0000	28,349.19	28,349.19	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	76.13%	2.09	0	3	8,328.49	5,494	15,515	8,043.96	0	14,579	17,420	17,420	0.00%
	crit	23.87%	0.66	0	3	16,665.37	11,008	31,778	8,739.43	0	31,778	10,929	10,929	0.00%
Action Details: Blood Draw
id:374606
school:shadow
range:0.0
travel_speed:0.0000
radius:8.0
trigger_gcd:0.0000
gcd_type:attack_haste
min_gcd:0.0000
cooldown:120.000
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
Spelldata
id:374606
name:Blood Draw
school:shadow
tooltip:
description:{$@spelldesc374598=When you fall below {$s1=30}% health you drain {$374606s1=0} health from nearby enemies, the damage you take is reduced by {$454871s1=10}% and your Death Strike cost is reduced by {$=}{{$454871s2=100}/-10} for {$454871d=8 seconds}.
Can only occur every {$374609d=120 seconds}.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Blood Death Knight	137008	#1	15.0%	Spec Spell
	Periodic Damage	Blood Death Knight	137008	#2	15.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Blood Shield	77535	#2	8.0%	Spell Data	No-stacks
	Dance of Midnight	1264407	#1	6.0%	Spell Data
	Sanguine Ground	391459	#1	6.0%	Spell Data
	Periodic Damage
	Blood Shield	77535	#3	8.0%	Spell Data	No-stacks
	Dance of Midnight	1264407	#2	6.0%	Spell Data
	Sanguine Ground	391459	#3	6.0%	Spell Data
	Damage on Debuff
	Brittle	374557	#1	6.0%
	Blood Plague	55078	#4	5.0%
	Blood Mist
	690	1.2%	33.0	8.75s	0.0s	6,282	0	Direct	33.0	5,046	10,098	6,282	24.5%
Stats Details: Blood Mist
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Tim
```

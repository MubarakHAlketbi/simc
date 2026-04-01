# MID1_Warlock_Affliction_Hellcaller — Talents & Gear

## Talent Export String
```
CkQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZhhZmZmlBAAYmZZWmZmlxAAWgBmFjGzAysBWGAAAmBAAmZAzMjxwwMjZmZGMzMzAAmBG
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	99,300.2	99,300.2	67.0 / 0.068%	11,650.7 / 11.7%	49.6
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	1,840.1	1,830.3	0.00%	51.8	100.0%
	Talent	CkQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZhhZmZmlBAAYmZZWmZmlxAAWgBmFjGzAysBWGAAAmBAAmZAzMjxwwMjZmZGMzMzAAmBG
	Set Bonus
Reign of the Abyssal Immolator (MID1)
Warlock Affliction 12.0 Class Set 2pc (2pc)
Warlock Affliction 12.0 Class Set 4pc (4pc)
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
	MID1_Warlock_Affliction_Hellcaller	99,300
	Agony
	12,111	12.2%	18.4	17.49s	18.9s / 6.3%	197,852	192,469	Periodic	288.0	9,154	20,204	12,615	31.3%	99.8%
Stats Details: Agony
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	18.37	0.00	288.03	288.03	17.36	1.0280	1.0396	3,633,614.06	3,633,614.06	0.00%	11,415.19	192,468.57
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	68.68%	197.80	138	256	9,153.99	159	15,238	9,148.72	8,634	9,755	1,810,693	1,810,693	0.00%
	crit	31.32%	90.22	52	133	20,204.39	670	33,631	20,192.69	18,603	22,019	1,822,921	1,822,921	0.00%
Action Details: Agony
id:980
school:shadow
range:40.0
travel_speed:0.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.05
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
Damage Over Time
tick_may_crit:true
tick_zero:false
tick_on_application:false
rolling_periodic:false
attack_power_mod.tick:0.000000
spell_power_mod.tick:0.070553
base_td:0.000000
base_td_mult:2.266970
base_multiplier:1.000000
dot_duration:18.00
base_tick_time:1.60
hasted_ticks:true
dot_behavior:DOT_REFRESH_PANDEMIC
Spelldata
id:980
name:Agony
school:shadow
tooltip:Suffering {$=}w1 Shadow damage every {$t1=1.600} sec. Damage increases over time.
description:Inflicts increasing agony on the target, causing up to {$=}{{$s1=0}*{$d=18 seconds}/{$t1=1.600}*{$u=8}} Shadow damage over {$d=18 seconds}. Damage starts low and increases over the duration. Refreshing Agony maintains its current damage level.
|cFFFFFFFFAgony damage sometimes generates 1 Soul Shard.|r
Action Priority List
HC_st[E]:15.46
if_expr:refreshable
HC_st[H]:2.91
if_expr:dot.agony.remains<20&cooldown.summon_darkglare.remains<gcd
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Malediction	453087	#1	5.0%	Talent
	Xalan's Cruelty	440040	#1	10.0%	Talent
	Crit Bonus	Contagion	453096	#1	15.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Xalan's Cruelty	440040	#3	6.0%	Talent
	Period	Creeping Death	264000	#1	-20.0%	Talent
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Mark of Xavius	440046	#1	30.0%	Talent
	Xalan's Cruelty	440040	#4	6.0%	Talent
	Sudden Onset	1260209	#1	10.0%	Talent
	Shared Agony	1259825	#1	10.0%	Talent
	Niskaran Methods	1279510	#2	10.0%	Talent
	Warlock Affliction 12.0 Class Set 4pc	1264870	#2	20.0%	Set Bonus
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Darkglare Presence	1280663	#1	20.0%	Spell Data
	Periodic Damage
	Mastery: Potent Afflictions	77215	#1	2.50000	Spell Data	Mastery, Passive
	Darkglare Presence	1280663	#2	20.0%	Spell Data
	Blackened Soul
	7,814	7.9%	0.0	0.00s	0.0s	0	0	Direct	238.1	7,900	16,201	9,851	23.5%
Stats Details: Blackened Soul
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	238.09	0.00	0.00	0.00	0.0000	0.0000	2,345,413.38	2,345,413.38	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	76.50%	182.13	124	253	7,899.80	4,993	13,188	7,894.32	7,295	8,748	1,438,837	1,438,837	0.00%
	crit	23.50%	55.96	25	92	16,200.52	10,237	26,899	16,189.81	14,474	18,185	906,577	906,577	0.00%
Action Details: Blackened Soul
id:445736
school:shadowflame
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
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.996334
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.596500
base_multiplier:1.000000
Spelldata
id:445736
name:Blackened Soul
school:shadowflame
tooltip:
description:{$@spelldesc440043=Spending Soul Shards on damaging spells will further corrupt enemies affected by your Wither, increasing its stack count by {$s1=1}.
Each time Wither gains a stack it has a chance to collapse, consuming a stack every {$445731t1=1} sec to deal {$445736s1=0} Shadowflame damage to its host until 1 stack remains.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Affliction Warlock	137043	#12	55.0%	Spec Spell
	Summoner's Embrace	453105	#1	3.0%	Talent
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Dark Harvest
	0 (3,513)	0.0% (3.5%)	5.4	60.46s	12.5s / 4.2%	194,917	84,064
Stats Details: Dark Harvest
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	5.40	0.00	21.48	0.00	0.00	2.3188	0.5192	0.00	0.00	0.00%	84,064.33	84,064.33
Action Details: Dark Harvest
id:1257052
school:shadowflame
range:0.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:60.000
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
resource:mana
base_cost:2500
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Damage Over Time
tick_may_crit:false
tick_zero:false
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
dot_behavior:DOT_REFRESH_DURATION
Spelldata
id:1257052
name:Dark Harvest
school:shadowflame
tooltip:Consuming the life force of each target afflicted by your damaging periodic effects, dealing {$=}{{$1257065s1=0 + 839.6%}*(1+ {$d=3 seconds}/{$t1=1})} Shadowflame damage over {$d=3 seconds}.
Damage dealt by Dark Harvest heals you for {$=}{{$1257065=}e1*100}% of damage done.
description:Consume the life force of each target afflicted by your damaging periodic effects, dealing {$=}{{$1257065s1=0 + 839.6%}*(1+ {$d=3 seconds}/{$t1=1})} Shadowflame damage over {$d=3 seconds}.
Damage dealt by Dark Harvest heals you for {$=}{{$1257065=}e1*100}% of damage done.
Action Priority List
HC_st[G]:5.40
if_expr:execute_time<(dot.agony.remains<?dot.corruption.remains)
Dark Harvest (_tick)
	3,513	3.5%	0.0	0.00s	0.0s	0	0	Direct	21.5	37,716	77,324	48,967	28.4%
Stats Details: Dark Harvest Tick
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	21.48	0.00	0.00	0.00	0.0000	0.0000	1,051,896.96	1,051,896.96	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	71.60%	15.38	4	24	37,716.01	29,900	53,213	37,706.12	34,888	42,708	580,079	580,079	0.00%
	crit	28.40%	6.10	0	16	77,324.43	61,305	108,098	77,166.52	0	91,503	471,818	471,818	0.00%
Action Details: Dark Harvest Tick
id:1257065
school:shadowflame
range:100.0
travel_speed:0.0000
radius:100.0
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
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:8.395520
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.157308
base_multiplier:1.000000
Spelldata
id:1257065
name:Dark Harvest
school:shadowflame
tooltip:
description:{$@spelldesc1257052=Consume the life force of each target afflicted by your damaging periodic effects, dealing {$=}{{$1257065s1=0 + 839.6%}*(1+ {$d=3 seconds}/{$t1=1})} Shadowflame damage over {$d=3 seconds}.
Damage dealt by Dark Harvest heals you for {$=}{{$1257065=}e1*100}% of damage done.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Xalan's Cruelty	440040	#8	10.0%	Talent
	Xalan's Ferocity	440044	#9	10.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Xalan's Cruelty	440040	#7	6.0%	Talent
	Xalan's Ferocity	440044	#8	6.0%	Talent
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Haunt
	6,819	6.9%	17.9	16.30s	17.9s / 6.0%	114,600	114,574	Direct	18.8	85,539	175,650	108,861	25.9%
Stats Details: Haunt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	17.86	18.80	298.76	298.76	17.80	1.0003	1.0000	2,046,976.29	34,533,098.47	94.07%	6,464.97	114,573.84
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	74.12%	13.94	5	21	85,538.60	65,371	117,411	85,470.26	78,637	93,756	1,192,221	1,192,221	0.00%
	crit	25.88%	4.87	0	13	175,650.32	134,032	240,729	174,678.15	0	232,927	854,756	854,756	0.00%
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	100.00%	298.76	239	359	0.00	0	0	0.00	0	0	0	32,486,122	100.00%
Action Details: Haunt
id:48181
school:shadow
range:40.0
travel_speed:40.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:15.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:1.20
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
attack_power_mod.direct:0
```

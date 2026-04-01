# MID1_Warlock_Affliction_Soul_Harvester — Talents & Gear

## Talent Export String
```
CkQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZhhZmZmlBAAYmZxyMzsMzAAjllBGwEMDbBG2GAAAmBAAwMDzMjBGmZmZGzgZmZGAwMwA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	104,004.4	104,004.4	69.3 / 0.067%	12,034.3 / 11.6%	55.8
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	1,653.6	1,645.0	0.00%	49.0	100.0%
	Talent	CkQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZhhZmZmlBAAYmZxyMzsMzAAjllBGwEMDbBG2GAAAmBAAwMDzMjBGmZmZGzgZmZGAwMwA
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
	MID1_Warlock_Affliction_Soul_Harvester	104,004
	Agony
	6,592	6.3%	17.3	17.98s	18.4s / 6.1%	114,063	107,378	Periodic	270.0	5,637	11,548	7,324	28.5%	99.8%
Stats Details: Agony
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	17.34	0.00	270.04	270.04	16.33	1.0623	1.1087	1,977,681.08	1,977,681.08	0.00%	6,223.06	107,377.62
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	71.47%	193.00	136	252	5,637.17	257	9,702	5,633.28	5,289	5,998	1,087,954	1,087,954	0.00%
	crit	28.53%	77.04	44	114	11,548.18	510	19,868	11,540.17	10,288	12,599	889,727	889,727	0.00%
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
base_td_mult:1.359600
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
SH_st[E]:17.34
if_expr:refreshable
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Malediction	453087	#1	5.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Period	Creeping Death	264000	#1	-20.0%	Talent
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Shared Agony	1259825	#1	10.0%	Talent
	Warlock Affliction 12.0 Class Set 4pc	1264870	#2	20.0%	Set Bonus
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Darkglare Presence	1280663	#1	20.0%	Spell Data
	Periodic Damage
	Mastery: Potent Afflictions	77215	#1	2.50000	Spell Data	Mastery, Passive
	Darkglare Presence	1280663	#2	20.0%	Spell Data
	Corruption (_direct)
	8 (3,761)	0.0% (3.6%)	1.0	0.00s	0.9s / 0.3%	1,128,463	1,265,093	Direct	1.0	1,929	3,954	2,501	28.3%
Stats Details: Corruption Direct
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	1.00	1.00	0.00	0.00	0.00	0.8925	0.0000	2,500.88	2,500.88	0.00%	1,265,093.31	1,265,093.31
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	71.74%	0.72	0	1	1,928.53	1,924	2,046	1,383.52	0	2,046	1,384	1,384	0.00%
	crit	28.26%	0.28	0	1	3,953.75	3,946	4,088	1,117.36	0	4,088	1,117	1,117	0.00%
Action Details: Corruption Direct
id:172
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
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:172
name:Corruption
school:shadow
tooltip:
description:Corrupts the target, causing {$s3=0} Shadow damage and {$?a196103=true}[{$146739s1=0} Shadow damage every {$146739t1=2} sec.][an additional {$146739=}o1 Shadow damage over {$146739d=14 seconds}.]
Action Priority List
SH_st[F]:1.00
if_expr:refreshable
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Malediction	453087	#1	5.0%	Talent
	Direct Damage	Absolute Corruption	196103	#3	15.0%	Talent
	Periodic Damage	Absolute Corruption	196103	#2	15.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Potent Afflictions	77215	#2	2.50000	Spell Data	Mastery, Passive
	Darkglare Presence	1280663	#1	20.0%	Spell Data
	Periodic Damage
	Mastery: Potent Afflictions	77215	#1	2.50000	Spell Data	Mastery, Passive
	Darkglare Presence	1280663	#2	20.0%	Spell Data
Corruption
	3,753	3.6%	0.0	0.00s	0.0s	0	0	Periodic	358.5	2,418	4,958	3,141	28.5%	99.5%
Stats Details: Corruption
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	358.47	358.47	0.00	0.0000	0.8324	1,125,962.35	1,125,962.35	0.00%	3,773.37	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	71.55%	256.48	187	328	2,418.41	1,610	4,132	2,417.07	2,278	2,558	620,263	620,263	0.00%
	crit	28.45%	102.00	59	154	4,958.02	3,390	8,437	4,955.33	4,588	5,426	505,699	505,699	0.00%
Action Details: Corruption
id:146739
school:shadow
range:40.0
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
base_crit:0.05
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
tick_may_crit:true
tick_zero:false
tick_on_application:false
rolling_periodic:false
attack_power_mod.tick:0.000000
spell_power_mod.tick:0.275438
base_td:0.000000
base_td_mult:1.184500
base_multiplier:1.000000
dot_duration:720.00
base_tick_time:1.20
hasted_ticks:true
dot_behavior:DOT_REFRESH_PANDEMIC
Spelldata
id:146739
name:Corruption
school:shadow
tooltip:Suffering {$=}w1 Shadow damage every {$t1=1.200} sec.
description:{$@spelldesc172=Corrupts the target, causing {$s3=0} Shadow damage and {$?a196103=true}[{$146739s1=0} Shadow damage every {$146739t1=2} sec.][an additional {$146739=}o1 Shadow damage over {$146739d=14 seconds}.]}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Malediction	453087	#1	5.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Absolute Corruption	196103	#3	15.0%	Talent
	Period	Creeping Death	264000	#1	-20.0%	Talent
	Sataiel's Volition	449637	#1	-25.0%	Talent
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Absolute Corruption	196103	#2	15.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Potent Afflictions	77215	#2	2.50000	Spell Data	Mastery, Passive
	Darkglare Presence	1280663	#1	20.0%	Spell Data
	Periodic Damage
	Mastery: Potent Afflictions	77215	#1	2.50000	Spell Data	Mastery, Passive
	Darkglare Presence	1280663	#2	20.0%	Spell Data
	Dark Harvest
	0 (4,416)	0.0% (4.2%)	7.8	40.27s	18.5s / 6.2%	168,913	71,772
Stats Details: Dark Harvest
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	7.85	0.00	31.27	0.00	0.00	2.3536	0.5273	0.00	0.00	0.00%	71,772.22	71,772.22
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
SH_st[G]:7.85
if_expr:soul_shard<3&execute_time<(dot.agony.remains<?dot.corruption.remains)
Dark Harvest (_tick)
	4,416	4.2%	0.0	0.00s	0.0s	0	0	Direct	31.3	33,958	69,622	42,377	23.6%
Stats Details: Dark Harvest Tick
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	31.27	0.00	0.00	0.00	0.0000	0.0000	1,325,130.50	1,325,130.50	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	76.39%	23.89	11	35	33,958.41	28,293	47,359	33,916.46	31,540	36,851	811,214	811,214	0.00%
	crit	23.61%	7.38	0	18	69,621.61	60,759	97,101	69,522.74	0	83,310	513,917	513,917	0.00%
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
target:
```

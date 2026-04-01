# MID1_Paladin_Protection — Talents & Gear

## Talent Export String
```
CIEAAAAAAAAAAAAAAAAAAAAAAsMzAzyMLmZMDLLDzYmFbzYAAAAAAAAg0MziZMmxYmt2AgBADsNAAwMTbzMbzAEYzADWMzMAzMAALzAMzAG
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	69,620.0	69,620.0	56.2 / 0.081%	9,792.7 / 14.1%	-1.0
	HPS
	HPS(e)
	HPS Error
	HPS Range
	HPR
	25,404.6	25,404.6	60.5 / 0.238%	10,443.1 / 41.1%	-1.0
	APS
	APS Error
	APS Range
	APR
	5,581.7	12.9 / 0.231%	1,533.0 / 27.5%	-1.0
	DTPS
	DTPS Error
	DTPS Range
	70,041.5	64.26 / 0.09%	11,194 / 16.0%
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	0.0	0.0	0.02%	86.7	100.0%
	Talent	CIEAAAAAAAAAAAAAAAAAAAAAAsMzAzyMLmZMDLLDzYmFbzYAAAAAAAAg0MziZMmxYmt2AgBADsNAAwMTbzMbzAEYzADWMzMAzMAALzAMzAG
	Set Bonus
Voidlight Bindings (MID_VB)
Voidlight Bindings (2pc)
Luminant Verdict's Vestments (MID1)
Paladin Protection 12.0 Class Set 2pc (2pc)
Paladin Protection 12.0 Class Set 4pc (4pc)
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
	MID1_Paladin_Protection	69,620
	Avenger's Shield
	2,987 (4,807)	4.3% (6.9%)	34.2	8.76s	34.5s / 11.5%	42,100	41,776	Direct	34.2	18,550	39,547	26,175	36.3%
Stats Details: Avengers Shield
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	34.24	34.23	0.00	0.00	0.00	1.0078	0.0000	895,931.26	895,931.26	0.00%	41,775.50	41,775.50
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	63.68%	21.80	10	35	18,550.14	13,841	32,253	18,535.13	16,515	20,710	404,353	404,353	0.00%
	crit	36.32%	12.43	3	25	39,546.80	27,681	64,507	39,573.67	32,506	47,268	491,578	491,578	0.00%
Action Details: Avengers Shield
id:31935
school:holy
range:30.0
travel_speed:35.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:15.000
cooldown hasted:true
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:3
split_aoe_damage:false
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:on_hit
energize_resource:holy_power
energize_amount:0.0
Spelldata
id:31935
name:Avenger's Shield
school:holy
tooltip:Silenced.
description:Hurls your shield at an enemy target, dealing {$s1=0} Holy damage, interrupting and silencing the non-Player target for {$d=3 seconds}, and then jumping to {$=}{{$=}x1-1} additional nearby enemies. {$?a209389=true}[
Shields you for {$209388d=8 seconds}, absorbing {$209389s1=60}% as much damage as it dealt.][]{$?a378285=false}[
Deals {$=}<dmg> additional damage to all enemies within {$378286=}A1 yds of each target hit.][]
Action Priority List
default[F]:24.31
if_expr:buff.vanguard.up|(buff.avenging_wrath.up&apex.3)
default[I]:9.93
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Hasted Cooldown	Protection Paladin	137028	#7	100.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Light-Blessed Shield	1272298	#1	5.0%	Spell Data	Callback
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
Consecration (ss_as)
	143	0.2%	0.0	0.00s	0.0s	0	0	Periodic	33.3	900	1,956	1,286	36.5%	0.0%
Stats Details: Ss As
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	33.35	0.00	0.0000	0.0000	42,882.83	42,882.83	0.00%	0.00	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	63.47%	21.16	8	35	900.40	750	1,398	899.54	769	1,023	19,057	19,057	0.00%
	crit	36.53%	12.18	3	24	1,955.79	1,499	2,795	1,957.46	1,622	2,405	23,826	23,826	0.00%
Action Details: Ss As
id:81297
school:holy
range:30.0
travel_speed:0.0000
radius:8.0
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
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:81297
name:Consecration
school:holy
tooltip:
description:Deals {$s1=0} Holy damage every {$26573t1=1} sec to enemies within {$=}A1 yards.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	Consecration	327980	#1	-50.0%	Spec Spell
	Direct Damage	Protection Paladin	137028	#26	55.0%	Spec Spell
	Consecration in Flame	379022	#2	30.0%	Talent
	Hasted Cooldown	Protection Paladin	137028	#7	100.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
	Damage on Debuff
	Sanctify	382538	#1	20.0%
Glory of the Vanguard (_as)
	1,677	2.4%	24.3	12.25s	0.0s	20,716	0	Direct	24.3	14,158	30,423	20,716	40.3%
Stats Details: Glory Of The Vanguard As
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	24.28	24.28	0.00	0.00	0.00	0.0000	0.0000	502,900.28	502,900.28	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	59.68%	14.49	3	28	14,157.94	11,162	20,809	14,167.77	11,896	17,087	205,126	205,126	0.00%
	crit	40.32%	9.79	1	20	30,422.98	22,324	41,617	30,476.23	24,089	40,779	297,774	297,774	0.00%
Action Details: Glory Of The Vanguard As
id:1269175
school:holy
range:30.0
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
id:1269175
name:Glory of the Vanguard
school:holy
tooltip:
description:{$@spelldesc1267203=Judgment has a chance to grant you Vanguard, causing your next Avenger's Shield to leave an echoing bolt of light in a line between you and the initial target, piercing any enemies for {$1269175s1=0} Holy damage.}
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
	Consecration
	0 (1,851)	0.0% (2.7%)	22.4	13.75s	22.1s / 7.4%	24,761	25,071
Stats Details: Consecration
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	22.43	0.00	0.00	0.00	0.00	0.9877	0.0000	0.00	0.00	0.00%	25,070.94	25,070.94
Action Details: Consecration
id:26573
school:holy
range:0.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:4.500
cooldown hasted:true
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:false
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:26573
name:Consecration
school:holy
tooltip:Damage every {$t1=1} sec.
description:Consecrates the land beneath you, causing {$?s405289=false}[{$=}{{$=}<dmg>*1.05} Radiant][{$=}{{$=}<dmg>*1.05} Holy] damage over {$d=14 seconds} to enemies who enter the area{$?s204054=false}[ and reducing their movement speed by {$204054s2=50}%.][.] Limit {$s2=1}.
Action Priority List
default[K]:16.96
if_expr:!consecration.up
default[N]:4.47
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	Consecration	327980	#1	-50.0%	Spec Spell
	Direct Damage	Protection Paladin	137028	#26	55.0%	Spec Spell
	Consecration in Flame	379022	#2	30.0%	Talent
	Duration	Consecration in Flame	379022	#1	2000.0	Talent
	Hasted Cooldown	Protection Paladin	137028	#7	100.0%	Spec Spell
Consecration (_tick)
	1,851	2.7%	0.0	0.00s	0.0s	0	0	Periodic	443.4	885	1,920	1,252	35.5%	0.0%
Stats Details: Consecration Tick
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	443.40	0.00	0.0000	0.0000	555,296.17	555,296.17	0.00%	0.00	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	64.53%	286.11	202	384	885.32	750	1,398	885.09	852	920	253,303	253,303	0.00%
	crit	35.47%	157.28	98	226	1,920.08	1,499	2,795	1,919.65	1,805	2,033	301,993	301,993	0.00%
Action Details: Consecration Tick
id:81297
school:holy
range:50000.0
travel_speed:0.0000
radius:8.0
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
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:81297
name:Consecration
school:holy
tooltip:
description:Deals {$s1=0} Holy damage every {$26573t1=1} sec to enemies within {$=}A1 yards.
Affected By (Passive)
	Type	Spell	ID
```

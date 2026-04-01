# MID1_Paladin_Protection_Lightsmith — Talents & Gear

## Talent Export String
```
CIEAAAAAAAAAAAAAAAAAAAAAAsMzAzyMLmZMDLLDzYmFbzYAAAAAAAAg0MziZMmxYmt2AgBADsNAAACwMzyySbzMWMwgFzMDwMDAmZAwMDyA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	55,405.8	55,405.8	45.8 / 0.083%	7,951.6 / 14.4%	-1.0
	HPS
	HPS(e)
	HPS Error
	HPS Range
	HPR
	22,189.6	22,189.6	65.9 / 0.297%	11,363.8 / 51.2%	-1.0
	APS
	APS Error
	APS Range
	APR
	7,284.0	22.9 / 0.314%	2,767.8 / 38.0%	-1.0
	DTPS
	DTPS Error
	DTPS Range
	66,677.6	62.79 / 0.09%	10,697 / 16.0%
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	0.0	0.0	0.01%	84.0	100.0%
	Talent	CIEAAAAAAAAAAAAAAAAAAAAAAsMzAzyMLmZMDLLDzYmFbzYAAAAAAAAg0MziZMmxYmt2AgBADsNAAACwMzyySbzMWMwgFzMDwMDAmZAwMDyA
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
	MID1_Paladin_Protection_Lightsmith	55,406
	Avenger's Shield
	3,248 (5,197)	5.9% (9.4%)	36.5	8.26s	38.5s / 12.8%	42,697	40,501	Direct	36.5	18,885	40,350	26,692	36.4%
Stats Details: Avengers Shield
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	36.51	36.49	0.00	0.00	0.00	1.0542	0.0000	974,015.24	974,015.24	0.00%	40,500.86	40,500.86
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	63.63%	23.22	9	39	18,885.16	14,070	32,820	18,871.43	16,859	21,673	438,496	438,496	0.00%
	crit	36.37%	13.27	3	30	40,350.21	28,140	65,640	40,371.21	34,128	51,381	535,519	535,519	0.00%
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
default[D]:25.93
if_expr:buff.vanguard.up|(buff.avenging_wrath.up&apex.3)
default[H]:10.58
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
	120	0.2%	0.0	0.00s	0.0s	0	0	Periodic	27.8	910	1,980	1,294	35.8%	0.0%
Stats Details: Ss As
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	27.84	0.00	0.0000	0.0000	36,009.52	36,009.52	0.00%	0.00	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	64.17%	17.86	5	32	910.25	762	1,422	909.06	780	1,054	16,260	16,260	0.00%
	crit	35.83%	9.97	0	22	1,979.87	1,524	2,844	1,980.51	0	2,622	19,749	19,749	0.00%
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
	1,830	3.3%	25.9	11.55s	0.0s	21,181	0	Direct	25.9	14,499	31,026	21,181	40.4%
Stats Details: Glory Of The Vanguard As
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	25.90	25.90	0.00	0.00	0.00	0.0000	0.0000	548,650.77	548,650.77	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	59.57%	15.43	2	30	14,498.89	11,347	21,174	14,504.79	12,108	17,496	223,711	223,711	0.00%
	crit	40.43%	10.47	1	24	31,025.97	22,694	42,349	31,059.28	25,010	41,231	324,940	324,940	0.00%
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
	0 (1,543)	0.0% (2.8%)	18.7	16.56s	18.8s / 6.3%	24,789	24,547
Stats Details: Consecration
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	18.66	0.00	0.00	0.00	0.00	1.0099	0.0000	0.00	0.00	0.00%	24,547.33	24,547.33
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
default[L]:14.92
if_expr:!consecration.up
default[O]:2.74
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	Consecration	327980	#1	-50.0%	Spec Spell
	Direct Damage	Protection Paladin	137028	#26	55.0%	Spec Spell
	Consecration in Flame	379022	#2	30.0%	Talent
	Duration	Consecration in Flame	379022	#1	2000.0	Talent
	Hasted Cooldown	Protection Paladin	137028	#7	100.0%	Spec Spell
Consecration (_tick)
	1,543	2.8%	0.0	0.00s	0.0s	0	0	Periodic	369.0	893	1,939	1,254	34.5%	0.0%
Stats Details: Consecration Tick
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	368.99	0.00	0.0000	0.0000	462,594.47	462,594.47	0.00%	0.00	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	65.54%	241.84	159	345	893.13	762	1,422	892.89	845	938	215,994	215,994	0.00%
	crit	34.46%	127.15	73	189	1,939.41	1,524	2,844	1,938.81	1,792	2,073	246,601	246,601	0.00%
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

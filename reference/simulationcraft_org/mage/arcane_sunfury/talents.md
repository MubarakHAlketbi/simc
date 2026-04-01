# MID1_Mage_Arcane_Sunfury — Talents & Gear

## Talent Export String
```
C4DAAAAAAAAAAAAAAAAAAAAAAYGmZZmZmFmZGamxAAAwAAmZmmlltZAgYDAgNmZmxYzyMzMLzMGjZmxYhZmZMDAwAAAMAzMgZAwwA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	96,253.0	96,253.0	82.7 / 0.086%	14,463.7 / 15.0%	6.7
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	13,755.2	13,500.4	0.10%	44.5	100.0%
	Talent	C4DAAAAAAAAAAAAAAAAAAAAAAYGmZZmZmFmZGamxAAAwAAmZmmlltZAgYDAgNmZmxYzyMzMLzMGjZmxYhZmZMDAwAAAMAzMgZAwwA
	Set Bonus
Arcanoweave Trappings (MID_AT)
Arcanoweave Trappings (2pc)
Voidbreaker's Accordance (MID1)
Mage Arcane 12.0 Class Set 2pc (2pc)
Mage Arcane 12.0 Class Set 4pc (4pc)
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
	MID1_Mage_Arcane_Sunfury	96,253
	Arcane Assault
	738	0.8%	212.0	1.41s	0.0s	1,044	0	Direct	211.7	829	1,747	1,046	23.6%
Stats Details: Arcane Assault
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	211.99	211.75	0.00	0.00	0.00	0.0000	0.0000	221,399.11	221,399.11	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	76.43%	161.83	117	208	829.37	559	1,546	829.32	774	887	134,215	134,215	0.00%
	crit	23.57%	49.92	26	80	1,746.54	1,174	3,220	1,746.36	1,558	1,992	87,184	87,184	0.00%
Action Details: Arcane Assault
id:225119
school:arcane
range:40.0
travel_speed:24.0000
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
spell_power_mod.direct:0.172500
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:225119
name:Arcane Assault
school:arcane
tooltip:
description:Launches bolts of arcane energy at the enemy target, causing {$s1=0 + 17.2%} Arcane damage.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Arcane Barrage
	23,316 (26,769)	24.2% (27.8%)	53.7	5.58s	59.6s / 19.9%	149,460	134,833	Direct	53.5	92,832	197,173	130,879	36.5%
Stats Details: Arcane Barrage
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	53.75	53.46	0.00	0.00	0.00	1.1085	0.0000	6,997,118.42	6,997,118.42	0.00%	134,832.60	134,832.60
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	63.54%	33.97	20	50	92,832.29	2,866	235,963	92,783.67	70,358	110,481	3,153,416	3,153,416	0.00%
	crit	36.46%	19.49	9	33	197,173.42	6,035	502,408	197,115.41	139,934	246,292	3,843,702	3,843,702	0.00%
Action Details: Arcane Barrage
id:44425
school:arcane
range:40.0
travel_speed:24.0000
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
spell_power_mod.direct:0.879520
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:44425
name:Arcane Barrage
school:arcane
tooltip:
description:Launches bolts of arcane energy at the enemy target, causing {$s1=0 + 88.0%} Arcane damage.
For each Arcane Charge, deals {$36032s2=90}% additional damage{$?a321526=false}[, grants you {$=}{{$321526s1=200}/100}.1% of your maximum mana,][]{$?a231564=true}[ and hits {$231564s1=1} additional nearby {$=}Ltarget:targets; for {$231564s2=40}% of its damage][].
|cFFFFFFFFConsumes all Arcane Charges.|r
Action Priority List
default[K]:1.68
if_expr:fight_remains<gcd.max*2
sunfury[V]:45.79
if_expr:(buff.arcane_charge.stack=4&variable.sunfury_hold_for_cds&((((buff.clearcasting.react&talent.high_voltage)|(cooldown.arcane_orb.charges_fractional>0.95&active_enemies>=3))&((buff.arcane_salvo.react>=6&buff.arcane_salvo.react<7)|(buff.arcane_salvo.react>=12&buff.arcane_salvo.react<13)|(buff.arcane_salvo.react>=18&buff.arcane_salvo.react<19)|((buff.arcane_salvo.react<19)&!talent.resonance&active_enemies>=3)))|buff.arcane_salvo.stack=25))|prev_off_gcd.touch_of_the_magi|(debuff.touch_of_the_magi.remains<gcd.max&debuff.touch_of_the_magi.up&buff.arcane_charge.stack=4)|buff.arcane_soul.up
sunfury[Z]:6.28
if_expr:(variable.sf_touch_surge&(!prev_gcd.1.arcane_surge|prev_off_gcd.touch_of_the_magi&buff.arcane_salvo.react=25))|!variable.sf_touch_surge
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Hasted Cooldown	Mage	137018	#1	0.0%	Class Spell
(orb_barrage_) Arcane Orb
	0 (3,453)	0.0% (3.6%)	44.9	6.51s	0.0s	23,097	0
Stats Details: Orb Barrage Arcane Orb
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	44.86	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Orb Barrage Arcane Orb
id:153626
school:arcane
range:40.0
travel_speed:30.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
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
resource:mana
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:1.0
Spelldata
id:153626
name:Arcane Orb
school:arcane
tooltip:
description:Launches an Arcane Orb forward from your position, traveling up to 40 yds, dealing {$153640s1=0 + 243.2%} Arcane damage to enemies it passes through.
|cFFFFFFFFGrants 1 Arcane Charge when cast and every time it deals damage.|r
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charges	Charged Orb	384651	#1	1.0%	Talent
(orb_barrage_) Arcane Orb
	3,453	3.6%	44.8	6.51s	0.0s	23,110	0	Direct	44.8	18,247	40,764	23,111	21.6%
Stats Details: Orb Barrage Arcane Orb Bolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	44.83	44.83	0.00	0.00	0.00	0.0000	0.0000	1,036,073.24	1,036,073.24	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	78.40%	35.15	18	54	18,246.89	12,577	39,361	18,240.89	16,179	20,679	641,331	641,331	0.00%
	crit	21.60%	9.68	0	25	40,763.76	27,878	87,222	40,755.14	0	58,243	394,743	394,743	0.00%
Action Details: Orb Barrage Arcane Orb Bolt
id:153640
school:arcane
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
energize_amount:1.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:2.432000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.150000
base_multiplier:1.000000
Spelldata
id:153640
name:Arcane Orb
school:arcane
tooltip:
description:{$@spelldesc153626=Launches an Arcane Orb forward from your position, traveling up to 40 yds, dealing {$153640s1=0 + 243.2%} Arcane damage to enemies it passes through.
|cFFFFFFFFGrants 1 Arcane Charge when cast and every time it deals damage.|r}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Mage Arcane 12.0 Class Set 4pc	1264833	#1	10.0%	Set Bonus
	Direct Damage	Charged Orb	384651	#2	15.0%	Talent
	Arcane Blast
	23,660	24.6%	108.1	2.72s	129.3s / 43.1%	65,633	54,884	Direct	108.1	50,643	112,388	65,634	24.3%
Stats Details: Arcane Blast
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	108.09	108.09	0.00	0.00	0.00	1.1959	0.0000	7,094,501.96	7,094,501.96	0.00%	54,883.82	54,883.82
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	75.72%	81.85	46	120	50,642.63	5,461	120,640	50,606.33	44,388	55,656	4,145,126	4,145,126	0.00%
	crit	24.28%	26.24	8	46	112,388.08	12,086	263,901	112,307.16	91,676	146,518	2,949,376	2,949,376	0.00%
Action Details: Arcane Blast
id:30451
school:arcane
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
base_execute_time:2.25
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:mana
base_cost:6531
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:2.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:1.239000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.350000
base_multiplier:1.000000
Spelldata
id:30451
name:Arcane Blast
school:arcane
tooltip:
description:Blasts the target with energy, dealing {$30451s1=0 + 123.9%} Arcane damage.
Each Arcane Charge increases damage by {$36032s1=60}% and mana cost by {$36032s5=100}%, and reduces cast time by {$36032s4=8}%.
|cFFFFFFFFGenerates {$s2=1} Arcane {$=}lCharge:Charges;.|r
Action Priority List
sunfury[Y]:108.09
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Mage Arcane 12.0 Class Set 4pc	1264833	#1	10.0%	Set Bonus
	Direct Damage	Burden of Power	451035	#3	25.0%	Talent
	Consortium's Bauble	461260	#2	8.0%	Talent
	Mana cost	Consortium's Bauble	461260	#1	-5.0%	Talent
	Arcane Missiles
	22,698	23.6%	55.2	5.40s	98.3s / 32.8%	123,413	69,331	Periodic	386.4	13,759	30,380	17,634	23.3%	29.4%
Stats Details: Arcane Missiles
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	55.21	0.00	386.40	386.38	14.63	1.7801	0.2281	6,813,333.61	6,813,333.61	0.00%	69,330.68	69,330.68
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	76.69%	296.32	182	448	13,759.46
```

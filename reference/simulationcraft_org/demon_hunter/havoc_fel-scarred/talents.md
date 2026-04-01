# MID1_Demon_Hunter_Havoc_Fel-Scarred — Talents & Gear

## Talent Export String
```
CEkAAAAAAAAAAAAAAAAAAAAAAYgZmZMjZmZmhJjZGAAAAAAwsZMbzMmZmtZmx2sNPwMMGzYZgtZxMGmNNNmZGDbAAAAAAAAMzgBAAAgB
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	114,803.6	114,803.6	66.3 / 0.058%	11,455.8 / 10.0%	4,437.6
	Resource
	Out
	In
	Waiting
	APM
	Active
	Fury	25.9	26.3	1.54%	60.3	100.0%
	Talent	CEkAAAAAAAAAAAAAAAAAAAAAAYgZmZMjZmZmhJjZGAAAAAAwsZMbzMmZmtZmx2sNPwMMGzYZgtZxMGmNNNmZGDbAAAAAAAAMzgBAAAgB
	Set Bonus
Devouring Reaver's Sheathe (MID1)
Demon Hunter Havoc 12.0 Class Set 2pc (2pc)
Demon Hunter Havoc 12.0 Class Set 4pc (4pc)
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
	Avoid%
	Up%
	MID1_Demon_Hunter_Havoc_Fel-Scarred	114,804
	Annihilation
	0 (8,844)	0.0% (7.7%)	75.0	3.89s	75.6s / 25.2%	35,373	35,116
Stats Details: Annihilation
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	75.02	0.00	0.00	0.00	0.00	1.0073	0.0000	0.00	0.00	0.00%	35,116.01	35,116.01
Action Details: Annihilation
id:201427
school:magic
range:5.0
travel_speed:0.0000
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
resource:fury
base_cost:40
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:201427
name:Annihilation
school:magic
tooltip:
description:Slice your target for {$=}{{$227518s1=0}+{$201428s1=0}} Chaos damage. Annihilation has a {$197125h=20}% chance to refund {$193840s1=20} Fury.
Action Priority List
meta[a]:2.05
if_expr:buff.metamorphosis.remains<gcd.max&(!hero_tree.felscarred|buff.demonsurge_demonic_intensity.up&cooldown.eye_beam.remains)|debuff.essence_break.up
meta[c]:14.25
if_expr:action.annihilation.demonsurge_available&cooldown.blade_dance.remains&(buff.inertia.up|!talent.inertia)
meta[g]:58.71
if_expr:((fury>=75-variable.fury_gen_per_sec*gcd.max-(!variable.use_blade_dance*15)-20*variable.cs_machine+25*variable.pool_glaive_tempest)|soul_fragments.total>0|talent.blind_fury&cooldown.eye_beam.remains<gcd.max*2)&(cooldown.blade_dance.remains|!variable.use_blade_dance)|buff.metamorphosis.remains<5&(!variable.use_blade_dance|variable.use_blade_dance&cooldown.blade_dance.remains>=buff.metamorphosis.remains&cooldown.blade_dance.remains>gcd.max|buff.metamorphosis.remains<gcd.max|fury>=75|buff.inertia.up)
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Demon Hide	428241	#1	3.0%	Talent
	Hasted Gcd	Havoc Demon Hunter	212612	#6	100.0%	Spec Spell
	Periodic Damage	Demon Hide	428241	#3	3.0%	Talent
Annihilation (_damage_1)
	4,987	4.3%	0.0	0.00s	0.0s	0	0	Direct	75.0	11,470	28,462	19,946	49.9%	0.0%
Stats Details: Annihilation Damage 1
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	75.02	0.00	0.00	0.00	0.0000	0.0000	1,496,263.43	1,496,263.43	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	50.12%	37.60	19	58	11,469.95	7,802	25,961	11,468.05	10,264	12,950	431,221	431,221	0.00%
	crit	49.88%	37.42	19	57	28,461.59	18,829	67,133	28,465.26	24,838	32,440	1,065,042	1,065,042	0.00%
Action Details: Annihilation Damage 1
id:227518
school:chaos
range:15.0
travel_speed:0.0000
radius:0.0
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
weapon_multiplier:0.000000
Spelldata
id:227518
name:Annihilation
school:chaos
tooltip:
description:{$@spelldesc201427=Slice your target for {$=}{{$227518s1=0}+{$201428s1=0}} Chaos damage. Annihilation has a {$197125h=20}% chance to refund {$193840s1=20} Fury.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Havoc Demon Hunter	212612	#1	22.0%	Spec Spell
	Remorseless	1266328	#1	3.0%	Talent
	Demon Hide	428241	#1	3.0%	Talent
	Periodic Damage	Havoc Demon Hunter	212612	#2	22.0%	Spec Spell
	Remorseless	1266328	#2	3.0%	Talent
	Demon Hide	428241	#3	3.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Demon Soul	163073	#1	20.0%	Spell Data
	Demon Soul	347765	#1	20.0%	Spell Data
	Inertia	427641	#1	18.0%	Spell Data
	Blind Focus	1272364	#1	5.0%	Spell Data	Passive, Value-function
	Periodic Damage
	Demon Soul	163073	#2	20.0%	Spell Data
	Demon Soul	347765	#2	20.0%	Spell Data
	Inertia	427641	#2	18.0%	Spell Data
	Blind Focus	1272364	#2	5.0%	Spell Data	Passive, Value-function
	Damage on Debuff
	Serrated Glaive	390155	#1	15.0%
Annihilation (_damage_2)
	3,857	3.4%	0.0	0.00s	0.0s	0	0	Direct	74.9	8,865	22,090	15,442	49.7%	0.0%
Stats Details: Annihilation Damage 2
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	74.95	0.00	0.00	0.00	0.0000	0.0000	1,157,313.27	1,157,313.27	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	50.27%	37.68	17	59	8,864.64	6,131	20,079	8,862.00	7,737	9,858	333,979	333,979	0.00%
	crit	49.73%	37.27	18	56	22,090.49	14,795	58,086	22,095.26	19,182	26,052	823,334	823,334	0.00%
Action Details: Annihilation Damage 2
id:201428
school:chaos
range:15.0
travel_speed:0.0000
radius:0.0
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
weapon_multiplier:0.000000
Spelldata
id:201428
name:Annihilation
school:chaos
tooltip:
description:{$@spelldesc201427=Slice your target for {$=}{{$227518s1=0}+{$201428s1=0}} Chaos damage. Annihilation has a {$197125h=20}% chance to refund {$193840s1=20} Fury.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Havoc Demon Hunter	212612	#1	22.0%	Spec Spell
	Remorseless	1266328	#1	3.0%	Talent
	Demon Hide	428241	#1	3.0%	Talent
	Periodic Damage	Havoc Demon Hunter	212612	#2	22.0%	Spec Spell
	Remorseless	1266328	#2	3.0%	Talent
	Demon Hide	428241	#3	3.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Demon Soul	163073	#1	20.0%	Spell Data
	Demon Soul	347765	#1	20.0%	Spell Data
	Inertia	427641	#1	18.0%	Spell Data
	Blind Focus	1272364	#1	5.0%	Spell Data	Passive, Value-function
	Periodic Damage
	Demon Soul	163073	#2	20.0%	Spell Data
	Demon Soul	347765	#2	20.0%	Spell Data
	Inertia	427641	#2	18.0%	Spell Data
	Blind Focus	1272364	#2	5.0%	Spell Data	Passive, Value-function
	Damage on Debuff
	Serrated Glaive	390155	#1	15.0%
	auto_attack_mh
	3,842	3.3%	155.8	2.24s	0.0s	7,398	3,825	Direct	155.8	4,805	11,811	7,398	48.2%	16.3%
Stats Details: Auto Attack Mh
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	155.83	155.83	0.00	0.00	0.00	1.9340	0.0000	1,152,765.54	1,646,807.91	30.00%	3,824.97	3,824.97
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	35.45%	55.24	29	88	4,805.34	3,906	6,488	4,805.12	4,501	5,209	265,424	379,178	30.00%
	crit	48.21%	75.13	38	113	11,811.32	9,426	17,388	11,805.89	11,046	12,699	887,341	1,267,630	30.00%
	miss	16.34%	25.47	9	48	0.00	0	0	0.00	0	0	0	0	0.00%
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
base_execute_time:2.60
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
	Demon Soul	163073	#3	20.0%	Spell Data
	Demon Soul	347765	#3	20.0%	Spell Data
	Inertia	427641	#3	18.0%	Spell Data
	auto_attack_oh
	1,873	1.6%	152.3	2.24s	0.0s	3,691	1,910	Direct	152.3	2,404	5,909	3,691	48.2%	16.7%
Stats Details: Auto Attack Oh
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	152.26	152.26	0.00	0.00	0.00	1.9326	0.0000	562,062.62	802,946.60	30.00%	1,910.02	1,910.02
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	35.09%	53.43	26	85	2,404.46	1,954	3,245	2,404.56	2,247	2,597	128,482	183,546	30.00%
	crit	48.19%	73.38	40	109	5,908.67	4,715	8,697	5,906.02	5,543	6,365	433,580	619,400	30.00%
	miss	16.71%	25.45	9	45	0.00	0	0	0.00	0	0	0	0	0.00%
Action Details: Auto Attack Oh
id:1
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
base_execute_time:2.60
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
```

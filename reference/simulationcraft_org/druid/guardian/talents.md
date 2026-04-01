# MID1_Druid_Guardian — Talents & Gear

## Talent Export String
```
CgGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgZmxsYmZMzmZZgZbZgxMMaimZmFzMzMLjZeADAAAAgZYGLzAAAAQNzysMzMDAgFMDgFzgBsYZbAwMbwA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	88,270.5	88,270.5	86.9 / 0.098%	14,800.1 / 16.8%	6,975.9
	HPS
	HPS(e)
	HPS Error
	HPS Range
	HPR
	25,006.5	25,006.5	16.6 / 0.066%	2,843.8 / 11.4%	1,978.9
	APS
	APS Error
	APS Range
	APR
	580.7	0.4 / 0.071%	50.1 / 8.6%	1,978.9
	DTPS
	DTPS Error
	DTPS Range
	91,723.9	103.31 / 0.11%	17,810 / 19.4%
	Resource
	Out
	In
	Waiting
	APM
	Active
	Rage	12.6	12.8	0.00%	61.1	100.0%
	Talent	CgGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgZmxsYmZMzmZZgZbZgxMMaimZmFzMzMLjZeADAAAAgZYGLzAAAAQNzysMzMDAgFMDgFzgBsYZbAwMbwA
	Set Bonus
Voidlight Bindings (MID_VB)
Voidlight Bindings (2pc)
Sprouts of the Luminous Bloom (MID1)
Druid Guardian 12.0 Class Set 2pc (2pc)
Druid Guardian 12.0 Class Set 4pc (4pc)
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
	MID1_Druid_Guardian	88,270
	Barkskin (+brambles)
	260	0.3%	9.3	34.20s	0.0s	8,415	0	Direct	135.7	458	924	575	25.3%	0.0%
Stats Details: Barkskin
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	9.28	135.70	0.00	0.00	0.00	0.0000	0.0000	78,088.15	78,088.15	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	74.73%	101.41	67	137	457.98	385	693	457.75	434	475	46,442	46,442	0.00%
	crit	25.25%	34.27	12	59	923.55	769	1,386	923.05	824	1,006	31,647	31,647	0.00%
	parry	0.02%	0.03	0	1	0.00	0	0	0.00	0	0	0	0	0.00%
Action Details: Barkskin+brambles
id:22812
school:nature
range:0.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:0.0000
gcd_type:attack_haste
min_gcd:0.0000
cooldown:34.200
cooldown hasted:false
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
id:22812
name:Barkskin
school:nature
tooltip:All damage taken reduced by {$=}w1%.{$?a301768=true}[
Healing received increased by {$301768s2=20}%.][]{$?a1250923=false}[
Maximum health increased by {$1250923s2=20}%.][]
description:Your skin becomes as tough as bark, reducing all damage you take by {$s1=20}%{$?a301768=true}[, increasing healing received by {$301768s2=20}%,][]{$?a1250923=false}[, increasing maximum health by {$1250923s2=20}%,][] and preventing damage from delaying your spellcasts. Lasts {$d=14 seconds}.
Usable while stunned, frozen, incapacitated, feared, or asleep, and in all shapeshift forms.
Action Details: Barkskin Brambles
id:213709
school:nature
range:100.0
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
id:213709
name:Brambles
school:nature
tooltip:
description:{$@spelldesc203953=Sharp brambles protect you, absorbing and reflecting up to {$=}<shield> damage from each attack.
While Barkskin is active, the brambles also deal {$213709s1=0} Nature damage to all nearby enemies every {$22812t3=1} sec.}
Action Priority List
cooldowns[N]:9.28
if_expr:buff.bear_form.up
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	Guardian Druid	137010	#10	-15000.0	Spec Spell
	Survival of the Fittest	203965	#1	-24.0%	Talent
	Direct Damage	Killer Instinct	108299	#1	6.0%	Talent
	Circle of the Wild	474530	#1	5.0%	Talent
	Duration	Improved Barkskin	327993	#1	4000.0	Talent
	Ursoc's Endurance	393611	#1	2000.0	Talent
	Periodic Damage	Killer Instinct	108299	#2	6.0%	Talent
	Circle of the Wild	474530	#2	5.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Damage on Debuff
	Thrash	192090	#2	2.0% DISABLED
	Bear Melee
	4,003	4.5%	184.8	1.95s	0.0s	6,496	3,510	Direct	184.8	5,180	10,429	6,496	25.1%	0.0%
Stats Details: Bear Melee
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	184.82	184.82	0.00	0.00	0.00	1.8510	0.0000	1,200,631.47	1,715,187.81	30.00%	3,509.72	3,509.72
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	74.92%	138.47	95	184	5,180.05	4,359	7,852	5,178.58	5,000	5,360	717,268	1,024,669	30.00%
	crit	25.08%	46.35	22	76	10,428.76	8,718	15,705	10,425.62	9,645	11,260	483,363	690,519	30.00%
Action Details: Bear Melee
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
base_execute_time:2.50
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:on_hit
energize_resource:rage
energize_amount:4.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:1.000000
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Cat Form	768	#4	40.0%	Spell Data
	Damage on Debuff
	Thrash	192090	#3	2.0%
	Brambles
	1,079	1.2%	210.2	1.42s	0.0s	1,541	0	Direct	210.2	1,224	2,464	1,541	25.6%	0.0%
Stats Details: Brambles
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	210.18	210.18	0.00	0.00	0.00	0.0000	0.0000	323,911.80	323,911.80	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	74.34%	156.26	105	210	1,224.11	1,026	1,848	1,223.50	1,181	1,262	191,274	191,274	0.00%
	crit	25.62%	53.84	27	87	2,463.63	2,052	3,696	2,462.60	2,314	2,624	132,638	132,638	0.00%
	parry	0.04%	0.08	0	2	0.00	0	0	0.00	0	0	0	0	0.00%
Action Details: Brambles
id:203958
school:nature
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
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.000000
base_dd_min:735.200000
base_dd_max:735.200000
base_dd_mult:1.113000
base_multiplier:1.000000
Spelldata
id:203958
name:Brambles
school:nature
tooltip:
description:{$@spelldesc203953=Sharp brambles protect you, absorbing and reflecting up to {$=}<shield> damage from each attack.
While Barkskin is active, the brambles also deal {$213709s1=0} Nature damage to all nearby enemies every {$22812t3=1} sec.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Killer Instinct	108299	#1	6.0%	Talent
	Circle of the Wild	474530	#1	5.0%	Talent
	Periodic Damage	Killer Instinct	108299	#2	6.0%	Talent
	Circle of the Wild	474530	#2	5.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Damage on Debuff
	Thrash	192090	#2	2.0%
	Cat Melee
	40	0.0%	3.0	134.67s	0.0s	3,928	6,085	Direct	3.0	2,977	5,990	3,928	31.6%	0.0%
Stats Details: Cat Melee
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	3.00	3.00	0.00	0.00	0.00	0.6457	0.0000	11,768.14	16,811.63	30.00%	6,084.87	6,084.87
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	68.43%	2.05	0	6	2,976.79	2,755	3,391	2,800.87	0	3,391	6,103	8,718	28.36%
	crit	31.57%	0.95	0	5	5,989.71	5,509	6,782	3,893.97	0	6,782	5,665	8,093	19.53%
Action Details: Cat Melee
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
base_execute_time:1.00
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
	Cat Form	768	#4	40.0%	Spell Data
	Damage on Debuff
	Thrash	192090	#3	2.0%
	Galactic Guardian
	3,459 (5,088)	3.9% (5.8%)	44.5	6.71s	0.0s	34,288	0	Direct	44.5	3,867	7,797	4,870	25.5%	0.0%
	Periodic	198.1	3,300	6,648	4,144	25.2%	0.0%	97.8%
Stats Details: Galactic Guardian
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	44.50	44.50	198.09	198.09	42.91	0.0000	1.4815	1,037,602.56	1,037,602.56	0.00%	5,198.78	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	74.49%	33.15	14	56	3,867.22	3,206	5,776	3,866.99	3,549	4,210	128,181	128,181	0.00%
	crit	25.51%	11.35	1	25	7,796.64	6,413	11,551	7,794.78	6,744	9,558	88,506	88,506	0.00%
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	74.78%	148.13	98	194	3,299.61	4	5,013	3,298.46	3,070	3,405	488,765	488,765	0.00%
```

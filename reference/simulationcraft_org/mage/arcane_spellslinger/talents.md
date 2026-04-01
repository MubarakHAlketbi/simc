# MID1_Mage_Arcane_Spellslinger — Talents & Gear

## Talent Export String
```
C4DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMzQzMzAAAwAAgAmZmZZZmZYBAgtxMzMmtFLzMzYmxYMzMGLMzMjZAAGAAAzsAAmBADD
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	101,621.6	101,621.6	76.3 / 0.075%	13,333.7 / 13.1%	5.8
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	17,376.1	17,932.1	0.48%	52.1	100.0%
	Talent	C4DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMzQzMzAAAwAAgAmZmZZZmZYBAgtxMzMmtFLzMzYmxYMzMGLMzMjZAAGAAAzsAAmBADD
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
	MID1_Mage_Arcane_Spellslinger	101,622
	Arcane Assault
	683	0.7%	200.0	1.49s	0.0s	1,023	0	Direct	199.8	817	1,710	1,024	23.2%
Stats Details: Arcane Assault
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	200.02	199.81	0.00	0.00	0.00	0.0000	0.0000	204,622.76	204,622.76	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	76.84%	153.53	111	196	817.32	534	1,390	817.42	757	893	125,484	125,484	0.00%
	crit	23.16%	46.28	21	79	1,710.08	1,124	2,934	1,709.98	1,416	2,139	79,139	79,139	0.00%
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
	25,977 (29,231)	25.6% (28.8%)	50.2	5.90s	59.0s / 19.7%	174,793	148,650	Direct	49.8	111,947	233,815	156,320	36.4%
Stats Details: Arcane Barrage
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	50.16	49.84	0.00	0.00	0.00	1.1759	0.0000	7,790,988.22	7,790,988.22	0.00%	148,649.87	148,649.87
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	63.59%	31.69	18	45	111,947.09	3,215	214,441	111,919.12	96,061	127,138	3,547,949	3,547,949	0.00%
	crit	36.41%	18.15	9	32	233,814.62	6,870	450,191	233,688.38	184,711	278,788	4,243,039	4,243,039	0.00%
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
base_dd_mult:1.150000
base_multiplier:1.000000
Spelldata
id:44425
name:Arcane Barrage
school:arcane
tooltip:
description:Launches bolts of arcane energy at the enemy target, causing {$s1=0 + 88.0%} Arcane damage.
For each Arcane Charge, deals {$36032s2=90}% additional damage{$?a321526=true}[, grants you {$=}{{$321526s1=200}/100}.1% of your maximum mana,][]{$?a231564=true}[ and hits {$231564s1=1} additional nearby {$=}Ltarget:targets; for {$231564s2=40}% of its damage][].
|cFFFFFFFFConsumes all Arcane Charges.|r
Action Priority List
default[L]:1.95
if_expr:fight_remains<gcd.max*2
spellslinger_orbm[Y]:47.91
if_expr:(buff.arcane_charge.stack=4|talent.orb_barrage)&buff.arcane_salvo.react>=20&cooldown.touch_of_the_magi.remains>gcd.max*(4-(2*(active_enemies>=2)))|(((buff.arcane_surge.remains<gcd.max&buff.arcane_surge.up)|(debuff.touch_of_the_magi.remains<gcd.max&debuff.touch_of_the_magi.up))&buff.arcane_salvo.react>=15)
spellslinger_orbm[d]:0.30
if_expr:(time>5&!prev_gcd.1.arcane_surge)|(prev_off_gcd.touch_of_the_magi&buff.arcane_salvo.react=20)
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Direct Damage	Polished Focus	1261082	#4	15.0%	Talent
	Hasted Cooldown	Mage	137018	#1	0.0%	Class Spell
(orb_barrage_) Arcane Orb
	0 (3,254)	0.0% (3.2%)	39.0	7.54s	0.0s	25,033	0
Stats Details: Orb Barrage Arcane Orb
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	38.99	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
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
	3,254	3.2%	39.0	7.54s	0.0s	25,053	0	Direct	39.0	20,097	44,514	25,053	20.3%
Stats Details: Orb Barrage Arcane Orb Bolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	38.96	38.96	0.00	0.00	0.00	0.0000	0.0000	976,084.06	976,084.06	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	79.70%	31.05	15	49	20,096.95	13,221	38,882	20,092.34	16,382	23,783	624,041	624,041	0.00%
	crit	20.30%	7.91	0	20	44,514.06	29,265	85,344	44,481.39	0	76,642	352,043	352,043	0.00%
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
base_dd_mult:1.265000
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
	Direct Damage	Splintering Orbs	444256	#3	10.0%	Talent
	Charged Orb	384651	#2	15.0%	Talent
	Arcane Blast
	26,365	25.9%	152.3	1.95s	190.9s / 63.6%	51,931	41,419	Direct	153.2	39,822	89,149	51,630	23.9%
Stats Details: Arcane Blast
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	152.26	153.15	0.00	0.00	0.00	1.2538	0.0000	7,907,006.18	7,907,006.18	0.00%	41,419.19	41,419.19
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	76.06%	116.49	81	157	39,822.35	4,799	102,192	39,801.19	35,744	43,835	4,639,000	4,639,000	0.00%
	crit	23.94%	36.66	14	64	89,148.71	10,600	225,891	89,101.63	68,504	106,800	3,268,007	3,268,007	0.00%
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
base_dd_mult:1.242000
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
cooldowns[T]:18.20
if_expr:(talent.splintering_sorcery|variable.sf_touch_surge)&buff.arcane_salvo.react<20&((variable.opener&variable.time_for_pooling)|(!variable.opener&talent.orb_mastery&cooldown.arcane_surge.remains<(gcd.max*(mana.pct%(8+(8*(active_enemies>=2)))))))
spellslinger_orbm[b]:10.46
if_expr:buff.presence_of_mind.up
spellslinger_orbm[c]:123.60
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Mage Arcane 12.0 Class Set 4pc	1264833	#1	10.0%	Set Bonus
	Direct Damage	Signature Spell	470021	#3	15.0%	Talent
	Consortium's Bauble	461260	#2	8.0%	Talent
	Mana cost	Consortium's Bauble	461260	#1	-5.0%	Talent
	Arcane Missiles
	283	0.3%	1.3	71.48s	2.6s / 0.9%	63,920	32,535	Periodic	9.3	7,161	15,802	9,132	22.8%	0.8%
Stats Details: Arcane Missiles
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
```

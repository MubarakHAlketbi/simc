# MID1_Mage_Fire_Sunfury — Talents & Gear

## Talent Export String
```
C8DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMDZmZGAAAGAwMz0sssMDAwmZmx2wYmBAAAAAsZmZmZAAwYGzYmZMz2AwMDxMGDmhB
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	102,438.5	102,438.5	77.7 / 0.076%	13,384.4 / 13.1%	23.4
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	4,203.6	4,156.8	0.00%	81.8	100.0%
	Talent	C8DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMDZmZGAAAGAwMz0sssMDAwmZmx2wYmBAAAAAsZmZmZAAwYGzYmZMz2AwMDxMGDmhB
	Set Bonus
Voidbreaker's Accordance (MID1)
Mage Fire 12.0 Class Set 2pc (2pc)
Mage Fire 12.0 Class Set 4pc (4pc)
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
	MID1_Mage_Fire_Sunfury	102,438
	Burnout
	5,279	5.2%	5.0	60.49s	0.0s	314,613	0	Direct	5.0	314,614	0	314,614	0.0%
Stats Details: Burnout
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	5.04	5.04	0.00	0.00	0.00	0.0000	0.0000	1,584,352.57	1,584,352.57	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	100.00%	5.04	4	6	314,614.45	156,131	696,291	315,122.65	261,074	378,982	1,584,353	1,584,353	0.00%
Action Details: Burnout
id:1271335
school:fire
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
may_crit:false
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.000000
base_dd_min:312890.733390
base_dd_max:312890.733390
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:1271335
name:Burnout
school:fire
tooltip:
description:{$@spelldesc1271171=Fire Blast deals {$1271173s1=0} additional Fire damage to up to $s2 nearby enemies.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Fire Blast
	8,012	7.8%	123.7	2.44s	0.0s	19,434	0	Direct	123.7	0	19,434	19,434	100.0%
Stats Details: Fire Blast
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	123.66	123.66	0.00	0.00	0.00	0.0000	0.0000	2,403,143.90	2,403,143.90	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	123.66	90	163	19,433.88	11,604	36,155	19,412.36	17,986	20,971	2,403,144	2,403,144	0.00%
Action Details: Fire Blast
id:108853
school:fire
range:40.0
travel_speed:0.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
min_gcd:0.0000
cooldown:11.000
cooldown hasted:true
category cooldown:true
charges:3
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:1.00
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
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.986250
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.725000
base_multiplier:1.000000
Spelldata
id:108853
name:Fire Blast
school:fire
tooltip:
description:Blasts the enemy, critically striking for {$=}{{$s1=0}*2} Fire damage.
Castable while casting other spells.
Action Priority List
fireblast[R]:74.29
if_expr:cooldown_react&!buff.hot_streak.react&(buff.combustion.up|buff.hyperthermia.up)&(hot_streak_spells_in_flight+buff.heating_up.react=1)&gcd.remains<gcd.max
fireblast[S]:25.37
if_expr:cooldown_react&!buff.hot_streak.react&(action.fireball.executing&action.fireball.execute_remains>0.1|buff.pyroclasm.react&action.pyroblast.executing&action.pyroblast.execute_remains>0.1)&((target.health.pct>=30|!talent.scorch)&buff.heating_up.react)&(hot_streak_spells_in_flight+buff.heating_up.react=1)&gcd.remains<gcd.max
fireblast[T]:13.80
if_expr:cooldown_react&!buff.hot_streak.react&(target.health.pct<30&talent.scorch)&(hot_streak_spells_in_flight+buff.heating_up.react=0)&action.scorch.executing&buff.heat_shimmer.down&gcd.remains<gcd.max
fireblast[U]:9.19
if_expr:cooldown_react&!buff.hot_streak.react&time<variable.combustion_delay&(talent.firestarter|action.fireball.executing&action.fireball.execute_remains>0.1|buff.pyroclasm.react&action.pyroblast.executing&action.pyroblast.execute_remains>0.1)&(hot_streak_spells_in_flight+buff.heating_up.react=1)&gcd.remains<gcd.max&cooldown.combustion.ready
fireblast[V]:1.00
if_expr:fight_remains<1
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charge Cooldown	Flame On	205029	#2	-2000.0%	Talent
	Spellfire Salvo	1260616	#2	-1000.0%	Talent
	Charges	Flame On	205029	#1	1.0%	Talent
	Fervent Flickering	387044	#1	1.0%	Talent
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Direct Damage	Fervent Flickering	387044	#2	25.0%	Talent
	From the Ashes	342344	#2	15.0%	Talent
	Wildfire	1254828	#2	20.0%	Talent
	Hasted Cooldown	Mage	137018	#2	0.0%	Class Spell
	Fireball
	5,719	5.6%	66.7	3.14s	86.7s / 28.9%	25,706	19,782	Direct	66.7	16,697	37,000	25,706	44.4%
Stats Details: Fireball
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	66.71	66.71	0.00	0.00	0.00	1.2995	0.0000	1,714,952.18	1,714,952.18	0.00%	19,781.90	19,781.90
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	55.63%	37.11	19	56	16,696.55	14,250	28,195	16,695.25	15,339	18,577	619,622	619,622	0.00%
	crit	44.37%	29.60	18	44	36,999.66	30,149	68,129	37,020.17	33,941	40,906	1,095,330	1,095,330	0.00%
Action Details: Fireball
id:133
school:fire
range:40.0
travel_speed:45.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:1.75
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
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:3.881250
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:133
name:Fireball
school:fire
tooltip:
description:Throws a fiery ball that causes {$s1=0} Fire damage.{$?a157642=false}[
Each time your Fireball fails to critically strike a target, it gains a stacking {$157644s1=20}% increased critical strike chance. Effect ends when Fireball critically strikes.][]
Action Priority List
sf_combustion[Y]:3.11
if_expr:buff.combustion.down&(!prev_gcd.1.meteor|buff.bloodlust.down)
sf_filler[f]:63.60
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Ignite
	26,708	26.1%	560.2	0.54s	0.0s	14,295	0	Periodic	299.4	26,749	0	26,749	0.0%	99.8%
Stats Details: Ignite
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	560.19	0.00	299.38	299.38	559.19	0.0000	1.0000	8,008,110.98	8,008,110.98	0.00%	26,749.07	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	100.00%	299.38	239	359	26,749.26	1,350	109,436	26,765.24	23,208	31,352	8,008,111	8,008,111	0.00%
Action Details: Ignite
id:12654
school:fire
range:50000.0
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
Damage Over Time
tick_may_crit:false
tick_zero:false
tick_on_application:false
rolling_periodic:true
attack_power_mod.tick:0.000000
spell_power_mod.tick:0.000000
base_td:0.000000
base_td_mult:1.000000
base_multiplier:1.000000
dot_duration:9.00
base_tick_time:1.00
hasted_ticks:false
dot_behavior:unknown
Spelldata
id:12654
name:Ignite
school:fire
tooltip:Deals {$=}w1 Fire damage every {$t1=1} sec.{$?=}{$=}w3>0[
Movement speed reduced by {$=}w3%.][]
description:{$@spelldesc12846=Your target burns for an additional {$=}{{$s1=0}}.1% over {$12654d=9 seconds} of the total direct damage caused by your Fireball, Fire Blast, Pyroblast{$?s153561=false}[, Meteor][], and Flamestrike. If this effect is reapplied, any remaining damage will be added to the new Ignite.{$?a1254756=true}[
Fire Blast causes {$s1=0}% of your Ignite to spread to {$s5=0} nearby {$=}Lenemy:enemies;.][]}
	Intensifying Flame
	7,553	7.4%	299.4	1.00s	0.0s	7,564	0	Periodic	299.4	7,564	0	7,564	0.0%	0.0%
Stats Details: Intensifying Flame
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	299.38	0.00	0.00	299.38	0.00	0.0000	0.0000	2,264,524.04	2,264,524.04	0.00%	0.00	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	100.00%	299.38	239	359	7,564.12	382	30,946	7,568.64	6,563	8,866	2,264,524	2,264,524	0.00%
Action Details: Intensifying Flame
id:419800
school:fire
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
may_crit:false
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.000000
base_dd_min:5737.649757
base_dd_max:5737.649757
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:419800
name:Intensifying Flame
school:fire
tooltip:
description:{$@spelldesc416714=While Ignite is on {$s1=3} or fewer enemies it flares up dealing an additional {$s2=30}% of its damage to affected targets.}
	Meteorite
	0 (4,970)	0.0% (4.9%)	163.9	1.79s	0.0s	9,098	0
Stats Details: Meteorite
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	163.94	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Meteorite
id:449559
school:fire
range:40.0
travel_speed:0.0000
radius:-1.0
trigg
```

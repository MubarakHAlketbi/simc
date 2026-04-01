# MID1_Monk_Brewmaster — Buffs & Procs

## Buffs
```
Trigger Count	Interval
	Dynamic Buffs
	Start
	Refresh
	Total
	Start
	Trigger
	Duration
	Uptime
	Benefit
	Overflow
	Expiry
	Alnscorned Essence	5.2	110.6	115.8	20.2s	2.3s	34.3s	59.59%	0.00%	0.0 (0.0)	4.6
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_alnscorned_essence
max_stacks:20
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:false
reactable:false
reverse:false
refresh behavior:duration
stack behavior:asynchronous
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:agility
amount:34.04
Trigger Details
interval_min/max:0.7s / 242.4s
trigger_min/max:0.7s / 97.8s
trigger_pct:99.99%
duration_min/max:0.0s / 193.4s
uptime_min/max:28.20% / 95.95%
Stack Uptimes
alnscorned_essence_1:3.37%
alnscorned_essence_2:3.51%
alnscorned_essence_3:3.67%
alnscorned_essence_4:3.84%
alnscorned_essence_5:4.05%
alnscorned_essence_6:4.23%
alnscorned_essence_7:4.43%
alnscorned_essence_8:4.66%
alnscorned_essence_9:4.89%
alnscorned_essence_10:5.21%
alnscorned_essence_11:6.73%
alnscorned_essence_12:10.48%
alnscorned_essence_13:0.53%
alnscorned_essence_14:0.00%
Spelldata
id:1266687
name:Alnscorned Essence
tooltip:{$=}pri increased by {$=}w1.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:20
duration:12.00
cooldown:0.00
default_chance:101.00%
	Alnsight	7.3	3.8	11.2	39.4s	24.8s	15.8s	38.65%	0.00%	3.8 (3.8)	6.9
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_alnsight
max_stacks:1
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:12.0s / 124.6s
trigger_min/max:0.0s / 108.8s
trigger_pct:100.00%
duration_min/max:0.0s / 94.8s
uptime_min/max:14.92% / 76.25%
Stack Uptimes
alnsight_1:38.65%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Aspect of Harmony (_accumulator)	11.6	1127.4	1139.1	27.1s	0.3s	23.4s	90.75%	0.00%	1127.4 (1127.4)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_aspect_of_harmony_accumulator
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:refresh
tick_time behavior:unhasted
period:1.00
Trigger Details
interval_min/max:0.1s / 57.6s
trigger_min/max:0.0s / 12.0s
trigger_pct:100.00%
duration_min/max:0.0s / 53.8s
uptime_min/max:86.60% / 93.46%
Stack Uptimes
aspect_of_harmony_accumulator_1:90.75%
Spelldata
id:450521
name:Aspect of Harmony
tooltip:Storing {$?a450508=true}[{$450508=}w5][0] vitality.
description:{$@spelldesc450508=Store vitality from {$?a137023=true}[{$s1=12}%][{$s2=10}%] of your damage dealt and {$?a137023=true}[{$s3=6}%][{$s4=30}%] of your {$?a137023=true}[effective ][]healing.{$?a137024=false}[ Vitality stored from overhealing is reduced.][]
For {$450711d=10 seconds} after casting {$?a137023=true}[Celestial Brew][Thunder Focus Tea] your spells and abilities draw upon the stored vitality to deal {$s6=40}% additional {$?a137023=true}[damage over {$450763d=8 seconds}][healing over {$450769d=8 seconds}].}
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:0.00%
	Aspect of Harmony (_spender)	9.7	9.2	18.9	31.8s	15.5s	2.5s	8.06%	0.00%	9.2 (9.2)	0.1
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_aspect_of_harmony_spender
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:7.0s / 57.1s
trigger_min/max:1.8s / 55.1s
trigger_pct:100.00%
duration_min/max:0.0s / 11.0s
uptime_min/max:5.66% / 12.39%
Stack Uptimes
aspect_of_harmony_spender_1:8.06%
Spelldata
id:450711
name:Aspect of Harmony
tooltip:Drawing upon {$?a450508=true}[{$450508=}w5][0] vitality.
description:{$@spelldesc450508=Store vitality from {$?a137023=true}[{$s1=12}%][{$s2=10}%] of your damage dealt and {$?a137023=true}[{$s3=6}%][{$s4=30}%] of your {$?a137023=true}[effective ][]healing.{$?a137024=false}[ Vitality stored from overhealing is reduced.][]
For {$450711d=10 seconds} after casting {$?a137023=true}[Celestial Brew][Thunder Focus Tea] your spells and abilities draw upon the stored vitality to deal {$s6=40}% additional {$?a137023=true}[damage over {$450763d=8 seconds}][healing over {$450769d=8 seconds}].}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:101.00%
	Balanced Stratagem (_magic)	34.4	189.9	224.3	8.8s	1.3s	7.7s	88.21%	98.43%	57.4 (57.4)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_balanced_stratagem_magic
max_stacks:5
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:2.0s / 32.5s
trigger_min/max:1.0s / 5.0s
trigger_pct:100.00%
duration_min/max:0.0s / 31.5s
uptime_min/max:84.34% / 91.06%
Stack Uptimes
balanced_stratagem_magic_1:12.29%
balanced_stratagem_magic_2:14.31%
balanced_stratagem_magic_3:13.75%
balanced_stratagem_magic_4:12.49%
balanced_stratagem_magic_5:35.37%
Spelldata
id:451508
name:Balanced Stratagem
tooltip:Healing and damage of your next Elemental spell or ability is increased by {$s1=3}%.
description:{$@spelldesc450889=Casting a Physical spell or ability increases the damage and healing of your next Fire or Nature spell or ability by {$451508s1=3}%, and vice versa. Stacks up to {$451508=}U.}
max_stacks:5
duration:15.00
cooldown:0.00
default_chance:100.00%
	Balanced Stratagem (_physical)	42.8	0.6	43.5	7.0s	6.9s	0.8s	11.91%	18.31%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_balanced_stratagem_physical
max_stacks:5
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:1.0s / 27.4s
trigger_min/max:1.0s / 27.4s
trigger_pct:100.00%
duration_min/max:0.0s / 3.1s
uptime_min/max:9.27% / 14.94%
Stack Uptimes
balanced_stratagem_physical_1:11.90%
balanced_stratagem_physical_2:0.01%
Spelldata
id:451514
name:Balanced Stratagem
tooltip:Healing and damage of your next Physical spell or ability is increased by {$s1=3}%.
description:{$@spelldesc450889=Casting a Physical spell or ability increases the damage and healing of your next Fire or Nature spell or ability by {$451508s1=3}%, and vice versa. Stacks up to {$451508=}U.}
max_stacks:5
duration:15.00
cooldown:0.00
default_chance:100.00%
	Blackout Combo	95.1	0.0	95.1	3.2s	3.2s	1.5s	48.05%	68.60%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_blackout_combo
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:3.0s / 8.4s
trigger_min/max:3.0s / 8.4s
trigger_pct:100.00%
duration_min/max:0.0s / 4.1s
uptime_min/max:44.49% / 51.46%
Stack Uptimes
blackout_combo_1:48.05%
Spelldata
id:228563
name:Blackout Combo
tooltip:Your next ability is empowered.
description:{$@spelldesc196736=Blackout Kick also empowers your next ability:
{$@=}spellicon100780 Tiger Palm: Damage increased by {$228563s1=100}%.
{$@=}spellicon121253 Keg Smash: Reduces the remaining cooldown on your Brews by {$s3=2} additional sec.}
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:100.00%
	Blessing of the Capybara	4.4	1.2	5.6	58.7s	43.8s	16.5s	24.06%	0.00%	1.2 (1.2)	4.1
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_blessing_of_the_capybara
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:agility
amount:109.54
Trigger Details
interval_min/max:15.0s / 344.8s
trigger_min/max:0.0s / 344.8s
trigger_pct:100.00%
duration_min/max:0.0s / 63.4s
uptime_min/max:0.00% / 56.19%
Stack Uptimes
blessing_of_the_capybara_1:24.06%
Spelldata
id:1252524
name:Blessing of the Capybara
tooltip:Blessed by Filo, gaining {$=}w1 {$=}pri.
description:Blessed by Filo, gaining {$=}pri.
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Bloodlust	1.0	0.0	1.0	0.0s	0.0s	40.0s	13.52%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_bloodlust
max_stacks:1
base duration:40.00
duration modifier:1.00
base cooldown:300.00
default_chance:100.00%
default_value:0.30
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 0.0s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:40.0s / 40.0s
uptime_min/max:11.11% / 16.67%
Stack Uptimes
bloodlust_1:13.52%
Spelldata
id:2825
name:Bloodlust
tooltip:Haste increased by {$=}w1%.
description:Increases haste by {$s1=30}% for all party and raid members for {$d=40 seconds}.
Allies receiving this effect will become Sated and unable to benefit from Bloodlust or Time Warp again for {$57724d=600 seconds}.
max_stacks:0
duration:40.00
cooldown:300.00
default_chance:0.00%
	Celestial Flames	13.8	6.1	19.8	21.7s	14.8s	7.1s	32.45%	28.98%	6.1 (6.1)	13.5
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_celestial_flames
max_stacks:1
base duration:6.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:6.0s / 143.6s
trigger_min/max:0.0s / 143.6s
trigger_pct:100.00%
duration_min/max:0.0s / 32.1s
uptime_min/max:12.45% / 52.65%
Stack Uptimes
celestial_flames_1:32.45%
Spelldata
id:1263641
name:Celestial Flames
tooltip:
description:{$@spelldesc1263353=Drinking from Brews has a {$h=30}% chance to coat you with Celestial Flames for {$325190d=6 seconds}. While Celestial Flames is active:
{$@=}spellicon196730 {$@=}spellname196730:
Kegs thrown by Special Delivery are ignited and splash upon landing, dealing {$1263667s1=0} Fire damage to up to 5 nearby enemies.
{$@=}spellicon116847 {$@=}spellname116847:
Rushing Jade Wind becomes a firestorm, increasing its radius by {$1263641s2=30}% and causing it to deal Fire damage.
}
max_stacks:0
duration:6.00
cooldown:0.00
default_chance:100.00%
	Celestial Infusion	10.1	8.8	18.9	30.2s	15.5s	12.1s	40.80%	100.00%	8.8 (8.8)	1.4
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_celestial_infusion
max_stacks:1
base duration:16.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Absorb Details
school:chaos
high priority:no
Trigger Details
interval_min/max:1.8s / 72.0s
trigger_min/max:1.8s / 55.1s
trigger_pct:100.00%
duration_min/max:0.0s / 35.9s
uptime_min/max:29.12% / 57.48%
Stack Uptimes
celestial_infusion_1:40.80%
Spelldata
id:1241059
name:Celestial Infusion
tooltip:Absorbs {$s2=30}~% of incoming damage, up to {$=}w1 total.
description:A strong herbal brew that coalesces purified chi escaping your body into a celestial guard, absorbing {$s2=30}% of incoming damage, up to {$=}<absorb> total.
max_stacks:0
duration:16.00
cooldown:0.00
default_chance:0.00%
	Counterstrike	44.6	22.7	67.3	6.6s	4.3s	2.2s	32.94%	50.07%	22.7 (22.7)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_counterstrike
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:1.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:2.0s / 42.0s
trigger_min/max:2.0s / 34.0s
trigger_pct:100.00%
duration_min/max:0.0s / 11.2s
uptime_min/max:20.33% / 48.67%
Stack Uptimes
counterstrike_1:32.94%
Spelldata
id:383800
name:Counterstrike
tooltip:Your next Tiger Palm or Spinning Crane Kick deals {$=}w1% increased damage.
description:{$@spelldesc383785=Each time you dodge or an enemy misses you, your next Tiger Palm or Spinning Crane Kick deals {$383800s1=100}% increased damage.}
max_stacks:1
duration:10.00
cooldown:0.00
default_chance:100.00%
	Draught of Rampant Abandon	1.5	0.0	1.5	298.1s	0.0s	26.2s	12.96%	0.00%	0.0 (0.0)	1.3
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_draught_of_rampant_abandon
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
associated item:Draught of Rampant Abandon
Stat Details
stat:agility
amount:774.00
Trigger Details
interval_min/max:298.0s / 298.8s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.38% / 17.68%
Stack Uptimes
draught_of_rampant_abandon_1:12.96%
Spelldata
id:1236998
name:Draught of Rampant Abandon
tooltip:{$=}pri increased by $s0.
description:Increases {$=}pri by $s0 for {$d=30 seconds}. While under the effects of this potion the Void may extract its toll, opening a void zone at your feet.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:100.00%
	Elusive Brawler	68.2	192.6	260.9	4.3s	1.1s	3.9s	89.50%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_elusive_brawler
max_stacks:100
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.9s / 34.0s
trigger_min/max:0.0s / 2.0s
trigger_pct:100.00%
duration_min/max:0.0s / 34.0s
uptime_min/max:86.46% / 92.45%
Stack Uptimes
elusive_brawler_1:23.06%
elusive_brawler_2:10.32%
elusive_brawler_3:7.21%
elusive_brawler_4:4.71%
elusive_brawler_5:2.67%
elusive_brawler_6:1.99%
elusive_brawler_7:1.78%
elusive_brawler_8:1.71%
elusive_brawler_9:1.85%
elusive_brawler_10:1.76%
elusive_brawler_11:1.74%
elusive_brawler_12:1.78%
elusive_brawler_13:1.72%
elusive_brawler_14:1.72%
elusive_brawler_15:1.73%
elusive_brawler_16:1.70%
elusive_brawler_17:1.70%
elusive_brawler_18:1.70%
elusive_brawler_19:1.67%
elusive_brawler_20:1.68%
elusive_brawler_21:1.67%
elusive_brawler_22:1.64%
elusive_brawler_23:1.66%
elusive_brawler_24:1.64%
elusive_brawler_25:1.62%
elusive_brawler_26:1.61%
elusive_brawler_27:1.54%
elusive_brawler_28:1.35%
elusive_brawler_29:1.07%
elusive_brawler_30:0.73%
elusive_brawler_31:0.43%
elusive_brawler_32:0.22%
elusive_brawler_33:0.09%
elusive_brawler_34:0.03%
elusive_brawler_35:0.01%
elusive_brawler_36:0.00%
elusive_brawler_37:0.00%
elusive_brawler_38:0.00%
Spelldata
id:195630
name:Elusive Brawler
tooltip:Dodge chance increased by {$=}w1%.
description:{$@spelldesc117906=Each time you are hit by a melee attack, or hit with Blackout Kick, you gain stacking {$=}{{$s1=0}}.1% increased Dodge chance until your next successful Dodge.
Also increases your attack power by {$=}{{$s2=0}}.1%.}
max_stacks:100
duration:10.00
cooldown:0.00
default_chance:100.00%
	Empty Barrel	29.0	5.1	34.2	10.4s	8.8s	2.2s	21.35%	58.35%	5.1 (5.1)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_empty_barrel
max_stacks:1
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 50.1s
trigger_min/max:0.0s / 50.1s
trigger_pct:100.00%
duration_min/max:0.0s / 12.0s
uptime_min/max:11.84% / 35.03%
Stack Uptimes
empty_barrel_1:21.35%
Spelldata
id:1265307
name:Empty Barrel
tooltip:Toss an Empty Barrel along with your next Keg Smash
description:{$@spelldesc1265129=Drinking a Brew has a {$=}H% chance to leave you with an Empty Barrel, which is tossed along with your next Keg Smash to deal {$1265133s1=0} Physical damage to your target. Ricochets up to {$1265133=}x1 times at {$=}{{$1265133=}f1*100}% effectiveness.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:0.00%
	Empty the Cellar	2.5	0.0	2.5	90.1s	90.1s	13.3s	11.13%	10.34%	0.0 (0.0)	0.3
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_empty_the_cellar
max_stacks:1
base duration:20.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:60.0s / 291.4s
trigger_min/max:60.0s / 291.4s
trigger_pct:100.00%
duration_min/max:0.0s / 20.0s
uptime_min/max:0.00% / 26.51%
Stack Uptimes
empty_the_cellar_1:11.13%
Spelldata
id:1262768
name:Empty the Cellar
tooltip:Empty the Cellar is available to cast
description:Fire a volley of {$1262329s1=5} {$=}Lkeg:kegs; at nearby targets.
max_stacks:0
duration:20.00
cooldown:0.00
default_chance:0.00%
	Exploding Keg	2.5	0.0	2.5	90.1s	90.1s	3.0s	2.51%	0.00%	0.0 (0.0)	2.5
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_exploding_keg
max_stacks:1
base duration:3.00
duration modifier:1.00
base cooldown:60.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:60.0s / 291.4s
trigger_min/max:60.0s / 291.4s
trigger_pct:100.00%
duration_min/max:0.0s / 3.0s
uptime_min/max:0.00% / 4.85%
Stack Uptimes
exploding_keg_1:2.51%
Spelldata
id:325153
name:Exploding Keg
tooltip:Misses melee attacks.
description:Hurls a flaming keg at the target location, dealing {$s1=0} Fire damage to nearby enemies, causing your attacks against them to deal {$388867s1=0} additional Fire damage, and causing their melee attacks to deal {$s2=100}% reduced damage for the next {$d=3 seconds}.
Resets the cooldown of Keg Smash.
max_stacks:0
duration:3.00
cooldown:60.00
default_chance:101.00%
	Fortifying Brew	2.1	0.0	2.1	175.7s	175.7s	14.7s	10.24%	0.00%	0.0 (0.0)	2.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_fortifying_brew
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:161.0s / 205.0s
trigger_min/max:161.0s / 205.0s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:8.33% / 12.96%
Stack Uptimes
fortifying_brew_1:10.24%
Spelldata
id:120954
name:Fortifying Brew
tooltip:{$?=}{$=}w1>0[Health increased by {$=}<health>%, damage taken reduced by {$=}<damage>%.][]{$?=}{$=}w6>0[
Effectiveness of Stagger increased by {$115203s1=20}%.][]{$?a451029=false}&{$=}c2[
Staggering {$451029s1=20}% of incoming damage.][]
description:Turns your skin to stone for {$120954d=15 seconds}{$?a388917=true}[, increasing your current and maximum health by {$=}<health>%][]{$?s322960=false}[, increasing the effectiveness of Stagger by {$322960s1=15}%][]{$?a388917=true}[, reducing all damage you take by {$=}<damage>%][]{$?a451029=false}&{$=}c2[, and Staggering {$451029s1=20}% of incoming damage][].
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
Trigger Spelldata
id:388917
name:Fortifying Brew
tooltip:
description:Turns your skin to stone for {$120954d=15 seconds}, increasing your current and maximum health by {$=}<health>% and reducing all damage you take by {$=}<damage>%.
Combines with other Fortifying Brew effects.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:0.00%
	Fuel on the Fire	2.5	0.0	2.5	90.1s	90.1s	14.9s	12.50%	9.54%	0.0 (0.0)	0.3
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_fuel_on_the_fire
max_stacks:2
base duration:20.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:60.0s / 291.4s
trigger_min/max:60.0s / 291.4s
trigger_pct:100.00%
duration_min/max:0.0s / 20.0s
uptime_min/max:0.00% / 27.10%
Stack Uptimes
fuel_on_the_fire_1:7.82%
fuel_on_the_fire_2:4.68%
Spelldata
id:1262035
name:Fuel on the Fire
tooltip:Your next Keg Smash will summon a whirl of flame.
description:{$@spelldesc1262017=Exploding Keg also causes your next {$s1=2} {$=}Lcast:casts; of Keg Smash to summon a whirl of flame which spirals outwards, dealing {$1262159s1=0} additional Fire damage to each enemy struck.}
max_stacks:2
duration:20.00
cooldown:0.00
default_chance:101.00%
	Gift of the Ox	3.1	44.9	48.1	64.0s	6.2s	92.5s	96.44%	99.19%	14.3 (14.3)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_gift_of_the_ox
max_stacks:5
base duration:60.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:asynchronous
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 299.8s
trigger_min/max:0.0s / 30.1s
trigger_pct:100.00%
duration_min/max:0.0s / 302.2s
uptime_min/max:86.28% / 99.01%
Stack Uptimes
gift_of_the_ox_1:5.19%
gift_of_the_ox_2:8.52%
gift_of_the_ox_3:15.82%
gift_of_the_ox_4:21.95%
gift_of_the_ox_5:44.95%
Spelldata
id:124506
name:Gift of the Ox
tooltip:
description:{$@spelldesc124502=When you take damage, you have a chance to summon a Healing Sphere.
{$@=}spellicon224863{$@=}spellname224863:
{$@spelldesc224863=Summon a Healing Sphere visible only to you. Moving through this Healing Sphere heals you for {$124507s1=0}.}}
max_stacks:0
duration:30.00
cooldown:0.00
default_chance:0.00%
	Harmonic Surge	9.3	59.1	68.4	30.8s	4.3s	28.0s	86.87%	87.16%	5.0 (6.2)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_harmonic_surge
max_stacks:6
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:3.0s / 182.0s
trigger_min/max:0.8s / 34.0s
trigger_pct:100.00%
duration_min/max:0.2s / 181.0s
uptime_min/max:75.06% / 93.58%
Stack Uptimes
harmonic_surge_1:10.06%
harmonic_surge_2:12.03%
harmonic_surge_3:16.82%
harmonic_surge_4:19.11%
harmonic_surge_5:18.26%
harmonic_surge_6:10.59%
Spelldata
id:1270990
name:Harmonic Surge
tooltip:Your next Tiger Palm or Vivify will cause a Harmonic Surge.
description:{$@spelldesc1270958=Casting {$?s322507=false}[Celestial Brew]?s1241059[Celestial Infusion][Thunder Focus Tea] guarantees that your next {$?=}c1[{$s5=2}][{$s6=2}] {$=}Lcast:casts; of Tiger Palm or Vivify will trigger a Harmonic Surge, dealing {$?=}c1[{$=}{{$s1=55}*{$1239442s1=0}/100}][{$=}{{$s2=10}*{$1239442s1=0}/100}] Nature damage split between your target and other nearby enemies, and {$?=}c1[{$=}{{$s3=10}*{$1239443s1=0}/100}][{$=}{{$s4=40}*{$1239443s1=0}/100}] healing to up to {$1239443s2=5} injured allies.}
max_stacks:6
duration:30.00
cooldown:0.00
default_chance:101.00%
	Heavy Stagger (_stagger)	16.2	0.0	16.2	18.5s	18.4s	4.3s	22.90%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_heavy_stagger_stagger
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 62.1s
trigger_min/max:0.0s / 60.0s
trigger_pct:100.00%
duration_min/max:0.0s / 25.9s
uptime_min/max:9.36% / 40.12%
Stack Uptimes
heavy_stagger_stagger_1:22.90%
Spelldata
id:124273
name:Heavy Stagger
tooltip:{$=}w1 damage is being staggered every {$124255t1=0.500} sec.
Stagger Remaining: {$=}w2
description:{$@spelldesc124255={$@spelldesc115069=You shrug off attacks, delaying a portion of Physical damage based on your Agility, instead taking it over {$124273d=10 seconds}. Affects magical attacks at {$s5=58}% effectiveness.{$?s383714=true}[
{$@spelldesc383714=Gain up to {$=}{{$s1=5}*{$s3=3}}% Mastery based on your current level of Stagger.}][]}}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Invoke Niuzao, the Black Ox	3.0	0.0	3.0	120.7s	120.7s	24.1s	24.03%	0.00%	0.0 (0.0)	2.8
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_invoke_niuzao_the_black_ox
max_stacks:1
base duration:25.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.40
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:120.0s / 126.6s
trigger_min/max:120.0s / 126.6s
trigger_pct:100.00%
duration_min/max:0.0s / 25.0s
uptime_min/max:20.20% / 28.10%
Stack Uptimes
invoke_niuzao_the_black_ox_1:24.03%
Spelldata
id:132578
name:Invoke Niuzao, the Black Ox
tooltip:Niuzao is staggering {$s2=40}% of the Monk's Stagger damage.
description:Summons an effigy of Niuzao, the Black Ox for {$d=25 seconds} that attacks your primary target and Stomps when you cast Blackout Kick, damaging all nearby enemies.
While active, {$s2=40}% of damage delayed by Stagger is instead Staggered by Niuzao, and Niuzao is healed for {$s5=100}% of your purified Stagger.
max_stacks:0
duration:25.00
cooldown:120.00
default_chance:0.00%
	Light Stagger (_stagger)	47.8	0.0	47.8	6.1s	6.1s	1.8s	28.59%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_light_stagger_stagger
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 54.9s
trigger_min/max:0.0s / 54.9s
trigger_pct:100.00%
duration_min/max:0.0s / 23.0s
uptime_min/max:15.41% / 46.18%
Stack Uptimes
light_stagger_stagger_1:28.59%
Spelldata
id:124275
name:Light Stagger
tooltip:{$=}w1 damage is being staggered every {$124255t1=0.500} sec.
Stagger Remaining: {$=}w2
description:{$@spelldesc124255={$@spelldesc115069=You shrug off attacks, delaying a portion of Physical damage based on your Agility, instead taking it over {$124273d=10 seconds}. Affects magical attacks at {$s5=58}% effectiveness.{$?s383714=true}[
{$@spelldesc383714=Gain up to {$=}{{$s1=5}*{$s3=3}}% Mastery based on your current level of Stagger.}][]}}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Might of the Void	8.2	8.6	16.7	36.3s	17.0s	21.4s	58.30%	0.00%	8.6 (8.6)	7.6
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_might_of_the_void
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:agility
amount:66.80
Trigger Details
interval_min/max:15.0s / 140.3s
trigger_min/max:0.0s / 72.4s
trigger_pct:100.00%
duration_min/max:0.0s / 122.0s
uptime_min/max:34.90% / 86.53%
Stack Uptimes
might_of_the_void_1:58.30%
Spelldata
id:1241715
name:Might of the Void
tooltip:Wielding a wisp the Void's power, increasing your {$=}pri by {$=}w1.
description:{$@spelldesc1236095=Permanently enchants a weapon with Acuity of the Ren'dorei, causing your spells and abilities to grant you Might of the Void, providing you with {$=}ec1s1 {$=}pri for {$1241715d=15 seconds}. Cannot be applied to items lower than level {$=}ecim.
|cnNORMAL_FONT_COLOR:Thalassian Talents - Silvermoon's Spellpower|R }
max_stacks:0
duration:15.00
cooldown:0.00
default_chance:0.00%
	Moderate Stagger (_stagger)	58.6	0.0	58.6	5.1s	5.1s	2.5s	48.49%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_moderate_stagger_stagger
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 37.1s
trigger_min/max:0.0s / 37.1s
trigger_pct:100.00%
duration_min/max:0.0s / 17.0s
uptime_min/max:34.35% / 60.93%
Stack Uptimes
moderate_stagger_stagger_1:48.49%
Spelldata
id:124274
name:Moderate Stagger
tooltip:{$=}w1 damage is being staggered every {$124255t1=0.500} sec.
Stagger Remaining: {$=}w2
description:{$@spelldesc124255={$@spelldesc115069=You shrug off attacks, delaying a portion of Physical damage based on your Agility, instead taking it over {$124273d=10 seconds}. Affects magical attacks at {$s5=58}% effectiveness.{$?s383714=true}[
{$@spelldesc383714=Gain up to {$=}{{$s1=5}*{$s3=3}}% Mastery based on your current level of Stagger.}][]}}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	none_stagger	0.1	0.0	0.1	119.9s	118.3s	0.5s	0.02%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_none_stagger
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:1.0s / 274.9s
trigger_min/max:1.0s / 274.9s
trigger_pct:100.00%
duration_min/max:0.0s / 4.0s
uptime_min/max:0.00% / 1.62%
Stack Uptimes
none_stagger_1:0.02%
	Pretense of Instability	28.5	37.7	66.2	10.6s	4.5s	7.3s	69.09%	0.00%	37.7 (37.7)	27.8
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_pretense_of_instability
max_stacks:1
base duration:5.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:5.0s / 32.1s
trigger_min/max:0.0s / 13.7s
trigger_pct:100.00%
duration_min/max:0.0s / 29.1s
uptime_min/max:63.38% / 76.52%
Stack Uptimes
pretense_of_instability_1:69.09%
Spelldata
id:393515
name:Pretense of Instability
tooltip:Increases Dodge by {$s1=10}%.
description:Increases Dodge by {$s1=10}%.
max_stacks:1
duration:5.00
cooldown:0.00
default_chance:0.00%
Trigger Spelldata
id:393516
name:Pretense of Instability
tooltip:
description:Drinking a Brew grants you {$393515s1=10}% dodge for {$393515d=5 seconds}.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:100.00%
	Radiant Plume	6.5	0.0	6.5	49.2s	60.0s	46.3s	100.00%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_radiant_plume
max_stacks:60
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Stat Details
stat:mastery_rating
amount:4.70
Trigger Details
interval_min/max:1.0s / 60.0s
trigger_min/max:60.0s / 60.0s
trigger_pct:100.00%
duration_min/max:0.0s / 60.0s
uptime_min/max:100.00% / 100.00%
Stack Uptimes
radiant_plume_1:1.84%
radiant_plume_2:1.51%
radiant_plume_3:1.51%
radiant_plume_4:1.52%
radiant_plume_5:1.52%
radiant_plume_6:1.53%
radiant_plume_7:1.53%
radiant_plume_8:1.54%
radiant_plume_9:1.54%
radiant_plume_10:1.55%
radiant_plume_11:1.55%
radiant_plume_12:1.56%
radiant_plume_13:1.56%
radiant_plume_14:1.57%
radiant_plume_15:1.57%
radiant_plume_16:1.58%
radiant_plume_17:1.58%
radiant_plume_18:1.59%
radiant_plume_19:1.60%
radiant_plume_20:1.60%
radiant_plume_21:1.61%
radiant_plume_22:1.61%
radiant_plume_23:1.62%
radiant_plume_24:1.62%
radiant_plume_25:1.63%
radiant_plume_26:1.63%
radiant_plume_27:1.64%
radiant_plume_28:1.64%
radiant_plume_29:1.65%
radiant_plume_30:1.66%
radiant_plume_31:1.66%
radiant_plume_32:1.67%
radiant_plume_33:1.67%
radiant_plume_34:1.68%
radiant_plume_35:1.68%
radiant_plume_36:1.69%
radiant_plume_37:1.69%
radiant_plume_38:1.70%
radiant_plume_39:1.71%
radiant_plume_40:1.71%
radiant_plume_41:1.72%
radiant_plume_42:1.72%
radiant_plume_43:1.73%
radiant_plume_44:1.74%
radiant_plume_45:1.74%
radiant_plume_46:1.75%
radiant_plume_47:1.75%
radiant_plume_48:1.76%
radiant_plume_49:1.77%
radiant_plume_50:1.77%
radiant_plume_51:1.78%
radiant_plume_52:1.78%
radiant_plume_53:1.79%
radiant_plume_54:1.80%
radiant_plume_55:1.80%
radiant_plume_56:1.81%
radiant_plume_57:1.81%
radiant_plume_58:1.82%
radiant_plume_59:1.83%
radiant_plume_60:1.83%
Spelldata
id:1260615
name:Radiant Plume
tooltip:Mastery increased by {$=}w1.
description:{$@spelldesc1260592=The Plume's radiance grants you {$1260592s1=157} Mastery, waning over {$=}{{$1260615t2=1}*{$1260615u=60}} sec before reigniting to full incandescence. The Plume's power also regenerates while out of combat.}
max_stacks:60
duration:-0.00
cooldown:0.00
default_chance:101.00%
	Refreshing Drink	11.5	9.5	21.0	27.2s	14.5s	13.0s	49.91%	48.64%	9.5 (9.5)	3.3
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_refreshing_drink
max_stacks:1
base duration:20.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:1.8s / 77.0s
trigger_min/max:1.0s / 55.1s
trigger_pct:100.00%
duration_min/max:0.0s / 58.0s
uptime_min/max:32.79% / 71.24%
Stack Uptimes
refreshing_drink_1:49.91%
Spelldata
id:1265140
name:Refreshing Drink
tooltip:Upon taking damage, automatically consume a refreshing drink to heal for {$1265145=}o1 over {$1265145d=8 seconds}.
description:{$@spelldesc1265145=Upon taking damage, automatically consume a refreshing drink to heal for {$=}o1 over {$d=8 seconds}.}
max_stacks:0
duration:20.00
cooldown:0.00
default_chance:101.00%
	Shuffle	2.0	142.6	144.6	3.5s	2.1s	149.7s	99.82%	100.00%	142.6 (142.6)	1.0
Buff Details
buff initial source:MID1_Monk_Brewmaster
cooldown name:buff_shuffle
max_stacks:1
base duration:5.00
duration modifier:1.00
base cooldown:0.10
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:3.5s / 3.5s
trigger_min/max:1.0s / 5.0s
trigger_pct:100.00%
duration_min/max:3.0s / 356.5s
uptime_min/max:99.78% / 99.86%
Stack Uptimes
shuffle_1:99.82%
Spelldata
id:215479
name:Shuffle
tooltip:Your Stagger is {$=}w3% more effective.
description:{$@spelldesc115308=A swig of strong brew allows you to Stagger substantially more damage for {$215479d=5 seconds}.
Shares charges with Purifying Brew.}
max_stacks:0
duration:5.00
cooldown:0.00
default_chance:0.00%
Trigger Spelldata
id:322120
name:Shuffle
tooltip:
description:Niuzao's teachings allow you to shuffle during combat, increasing the effectiveness of your |CFFffffffStagger|R by {$s1=100}%.
Shuffle is granted by attacking enemies with your Keg Smash, Blackout Kick, and Spinning Crane Kick.
{$@=}spellicon115069 {$@=}spellname115069: {$@spelldesc115069=You shrug off attacks, delaying a portion of Physical damage based on your Agility, instead taking it over {$124273d=10 seconds}. Affects magical attacks at {$s5=58}% effectiveness.{$?s383714=true}[
{$@spelldesc383714=Gain up to {$=}{{$s1=5}*{$s3=3}}% Mastery based on your current level of Stagger.}][]}
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:100.00%
```

## Procs & Uptimes
```
Proc
	Count
	Min
	Max
	Interval
	Min
	Max
	Blackout Combo - Keg Smash	7.0	1.0	12.0	41.5s	2.0s	296.1s
	Blackout Combo - Tiger Palm	87.6	67.0	108.0	3.4s	2.0s	13.9s
	Elusive Footwork	31.7	13.0	54.0	9.3s	3.0s	98.1s
	Sal'salabim Breath of Fire Reset	49.5	34.0	66.0	6.0s	1.0s	35.0s
	Skyfury (Main Hand)	18.0	4.0	35.0	16.2s	2.6s	187.0s
	delayed_aa_cast	9.9	8.0	12.0	31.8s	30.7s	38.1s
```

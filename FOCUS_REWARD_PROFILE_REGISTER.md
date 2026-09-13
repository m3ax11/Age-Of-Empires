# Focus Structure Reward-Profile Register

This register accompanies `FOCUS_STRUCTURE_REWORK.md`. It records permanent reward profiles introduced or proposed by the structure pass and prevents different countries from receiving the same mechanical identity for the same kind of choice.

A conflict exists when profiles in the same decision type share at least two of three principal modifier categories. Similar modifiers used for materially different decision types are recorded but do not automatically constitute a conflict. Immediate political power, experience and stability rewards are excluded unless they form the lasting identity of the choice.

## Implemented profiles

| Decision type | Country and focus | Permanent profile | Status |
|---|---|---|---|
| Minor maritime theatre commitment | Denmark — `AOEIW9_DEN_dip_a_5` | Naval organisation, naval speed, convoy escort | Implemented |
| Minor continental theatre commitment | Denmark — `AOEIW9_DEN_dip_b_5` | Military-factory output, arms-factory construction, recruitable population | Implemented |
| Minor continental theatre commitment | Norway — `AOEIW9_NOR_dip_a_5` | Army organisation, planning, recruitable population | Implemented |
| Minor maritime theatre commitment | Norway — `AOEIW9_NOR_dip_b_5` | Naval speed, navy fuel consumption, dockyard construction | Implemented; pair 1 correction |
| Minor continental theatre commitment | Ireland — `AOEIW9_IRE_dip_a_5` | Army defence, mobilisation speed, stability | Implemented; pairs 2–3 correction |
| Minor maritime theatre commitment | Ireland — `AOEIW9_IRE_dip_b_5` | Convoy escort, trade influence, stability | Implemented; pair 4 correction |
| Major continental economic method | France — `AOEIW9_FRA_dip_a_3` | Trade influence, factory-efficiency growth, infrastructure construction | Implemented |
| Major continental military method | France — `AOEIW9_FRA_dip_a_5` | Army organisation, supply consumption, land-fort construction | Implemented |
| Major maritime economic method | France — `AOEIW9_FRA_dip_b_3` | Dockyard output, trade influence, consumer-goods demand | Implemented |
| Major maritime military method | France — `AOEIW9_FRA_dip_b_5` | Naval organisation, air-mission efficiency, naval-base construction | Implemented |
| Major maritime military method | USA — `AOEIW9_USA_dip_a_2` | Convoy escort, radar-station construction, decryption | Implemented; pair 5 correction |
| Major maritime economic method | USA — `AOEIW9_USA_dip_a_3` | Factory-efficiency growth, political-power growth, civilian-factory construction | Implemented; pair 8 correction |
| Major maritime military method | USA — `AOEIW9_USA_dip_b_2` | Sortie efficiency, air-mission efficiency, air-base construction | Implemented; pair 7 correction |
| Major maritime economic method | USA — `AOEIW9_USA_dip_b_3` | Dockyard output, resource extraction, dockyard construction | Implemented; pairs 9–10 correction |
| Industrial endgame | USA — `AOEIW9_USA_special_8` | Military-factory output, maximum production efficiency, supply consumption | Implemented |
| Secession settlement | USA — `AOEIW22_USA_reunify_union` | Stability, political power, consumer-goods demand | Implemented |
| Constitutional settlement | USA — `AOEIW22_USA_anglo_monarchy` | Political power, stability, trade influence, consumer-goods demand | Implemented |
| Constitutional settlement | USA — `AOEIW22_USA_aristocratic_republic` | Political power, stability, research speed, military-factory output | Implemented |
| Major maritime military method | United Kingdom — `AOEIW9_ENG_dip_a_2` | Convoy escort, naval detection, naval coordination | Implemented |
| Major maritime economic method | United Kingdom — `AOEIW9_ENG_dip_a_3` | Dockyard construction speed, subjects' autonomy gain reduction, trade influence | Implemented |
| Major continental military method | United Kingdom — `AOEIW9_ENG_dip_b_2` | Planning speed, reinforcement rate, army defence | Implemented |
| Major continental economic method | United Kingdom — `AOEIW9_ENG_dip_b_3` | Intelligence-network growth, military-factory output, war support | Implemented |

| Major continental economic method | Russia — `AOEIW9_SOV_dip_a_3` | Railway construction, resource-penalty reduction, fuel gain | Implemented; broad-gauge mobilisation |
| Major continental military method | Russia — `AOEIW9_SOV_dip_a_4` | Winter-attrition reduction, army speed, reduced organisation loss while moving | Implemented; winter-front movement and cohesion |
| Major maritime economic method | Russia — `AOEIW9_SOV_dip_b_3` | Resource extraction, trade influence, railway construction | Implemented; Black Sea export corridor |
| Major maritime military method | Russia — `AOEIW9_SOV_dip_b_4` | Naval minelaying, navy fuel consumption, repair speed | Implemented; Sevastopol mine command |
| Industrial endgame | Russia — `AOEIW9_SOV_special_8` | Military-factory output, resource extraction, railway construction | Implemented; industrial-colossus payoff |

The apparent `military-factory output` label in this register refers to `industrial_capacity_factory`; arms-factory construction is recorded separately as `production_speed_arms_factory_factor`.

## Consolidated closure implementation record

The consolidated batch was approved and implemented on 13 September 2026. It closes pairs 1–4 and 7–10, implements Russia's rewritten profiles and structural package, and retains the separately completed pair-5 change and pair-6 cascade. Pair 3 closes through the Irish pair-2 correction; pair 10 closes through the USA pair-9 correction.

| Country/focus | Previous profile | Implemented final profile | Conflict pair(s) | Full-register result |
|---|---|---|---|---|
| Norway — `AOEIW9_NOR_dip_b_5` | Naval organisation, naval speed, dockyard output | Naval speed, navy fuel consumption, dockyard construction | 1 | Maximum overlap 1/3; one Norwegian gameplay change. |
| Ireland — `AOEIW9_IRE_dip_a_5` | Army organisation, arms-factory construction, recruitable population | Army defence, mobilisation speed, stability | 2 and 3 | Maximum overlap 1/3; pair 3 closes as a cascade without a second gameplay change. |
| Ireland — `AOEIW9_IRE_dip_b_5` | Convoy escort, dockyard output, trade influence | Convoy escort, trade influence, stability | 4 | Maximum overlap 1/3, including the revised USA Atlantic commerce profile. |
| Russia — `AOEIW9_SOV_dip_a_3` | Withdrawn France-copy: trade, factory-efficiency growth, infrastructure | Railway construction, resource-penalty reduction, fuel gain | Russia/France register conflict | Maximum overlap 1/3; broad-gauge economic mobilisation. |
| Russia — `AOEIW9_SOV_dip_a_4` | Withdrawn France-copy: army organisation, supply, forts | Winter-attrition reduction, army speed, reduced organisation loss while moving | Russia/France register conflict | Maximum overlap 0/3; winter-front movement and cohesion. |
| Russia — `AOEIW9_SOV_dip_b_3` | Resource extraction, trade, infrastructure | Resource extraction, trade influence, railway construction | Russia/France register conflict | Maximum overlap 1/3; Black Sea grain, oil and rail exports. |
| Russia — `AOEIW9_SOV_dip_b_4` | Withdrawn France-copy: naval organisation, air support, naval bases | Naval minelaying, navy fuel consumption, repair speed | Russia/France register conflict | Maximum overlap 1/3; Sevastopol mine warfare and austere fleet maintenance. |
| Russia — `AOEIW9_SOV_special_8` | Token endpoint: 10 army experience | Military-factory output, resource extraction, railway construction | Industrial-endgame cross-check | Maximum overlap 1/3 with the USA Arsenal; no new conflict. |
| USA — `AOEIW9_USA_dip_b_2` | Air-mission efficiency, naval organisation, air-base construction | Sortie efficiency, air-mission efficiency, air-base construction | 7 | Maximum overlap 1/3; carrier-deck tempo replaces generic fleet organisation. |
| USA — `AOEIW9_USA_dip_a_3` | Trade influence, factory-efficiency growth, consumer-goods relief | Factory-efficiency growth, political-power growth, civilian-factory construction | 8 | Maximum overlap 1/3; revised from the earlier draft because trade plus factory efficiency would conflict with France's Rhine profile. |
| USA — `AOEIW9_USA_dip_b_3` | Dockyard output, resource extraction, trade influence | Dockyard output, resource extraction, dockyard construction | 9 and 10 | Maximum overlap 1/3; pair 10 closes as a cascade without a second gameplay change. |

Russia's accompanying structural package is implemented as documented in `FOCUS_STRUCTURE_REWORK.md`: mutex methods with OR reconvergence inside both compatible theatres; mutex Field Workshops/Signals; the Ural logistics prerequisite for the industrial capstone; the industrial-colossus prerequisite and permanent spirit; and targeted AI weights. Existing IDs, political architectures, targets, war goals and immediate rewards remain preserved.

The implemented final-state matrix contains **zero 2/3 conflicts** within either the maritime or continental profile groups. All six pairwise comparisons among the four final USA method profiles are 0/3. Among Russia's four method profiles, only the two economic methods share railway construction (1/3); every other Russian pair is 0/3.

## USA internal divergence check

The four final American theatre-method profiles were compared pairwise after the consolidated corrections. All six comparisons are 0/3.

| USA profile pair | Shared principal categories | Result |
|---|---|---|
| Atlantic mission ↔ Pacific mission | None (0/3) | No internal conflict |
| Atlantic mission ↔ Atlantic commercial pressure | None (0/3) | No internal conflict |
| Atlantic mission ↔ Pacific commercial pressure | None (0/3) | No internal conflict |
| Pacific mission ↔ Atlantic commercial pressure | None (0/3) | No internal conflict |
| Pacific mission ↔ Pacific commercial pressure | None (0/3) | No internal conflict |
| Atlantic commercial pressure ↔ Pacific commercial pressure | None (0/3) | No internal conflict |

## Retrospective implemented-country conflict closure

| Pair | Final shared categories | Status | Implemented resolution |
|---|---|---|---|
| 1 — Denmark Baltic Sound ↔ Norway Atlantic Lifeline | Naval speed (1/3) | **Resolved** | Norway now uses naval speed, navy fuel consumption and dockyard construction. |
| 2 — Denmark Continental Mobilisation ↔ Ireland Border Emergency | None (0/3) | **Resolved** | Ireland now uses army defence, mobilisation speed and stability. |
| 3 — Norway Scandinavian Field Command ↔ Ireland Border Emergency | None (0/3) | **Resolved by pair 2 cascade** | The Irish border profile no longer duplicates organisation and manpower. |
| 4 — Ireland Atlantic Republic ↔ France Mediterranean Commerce | Trade influence (1/3) | **Resolved** | Ireland now uses convoy escort, trade influence and stability. |
| 5 — Denmark Baltic Sound ↔ USA Atlantic Mission | Convoy escort (1/3) | **Resolved** | USA uses convoy escort, radar-station construction and decryption. |
| 6 — France Mediterranean Military ↔ USA Atlantic Mission | None (0/3) | **Resolved by pair 5 cascade** | No second gameplay edit was needed. |
| 7 — France Mediterranean Military ↔ USA Pacific Mission | Air-mission efficiency (1/3) | **Resolved** | USA uses sortie efficiency, air-mission efficiency and air-base construction. |
| 8 — France Mediterranean Commerce ↔ USA Atlantic Commercial Pressure | None (0/3) | **Resolved** | USA uses factory-efficiency growth, political-power growth and civilian-factory construction. |
| 9 — Ireland Atlantic Republic ↔ USA Pacific Commercial Pressure | None (0/3) | **Resolved** | USA uses dockyard output, resource extraction and dockyard construction. |
| 10 — France Mediterranean Commerce ↔ USA Pacific Commercial Pressure | Dockyard output (1/3) | **Resolved by pair 9 cascade** | The USA profile no longer uses trade influence. |

There are no open 2/3 reward-profile conflicts in the completed DEN/NOR/IRE/FRA/SOV/USA/ENG structure-pass register.

## Register maintenance rule

Every future structural proposal must add its permanent profiles here before approval. The proposal must name the nearest existing profile in the same decision type and count shared principal categories. A 2/3-or-greater match must be redesigned around the country's geography, economy, imperial relationships or military institutions before implementation.

Retrospective corrections must be rechecked against the **entire current register**, including profiles added after the original conflict was recorded and unapproved profiles that are still active proposals. Passing the original pairwise comparison is not sufficient. If a later profile creates a new 2/3 match, the correction must be redesigned and presented again before any gameplay implementation.

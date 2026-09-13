# Focus Structure Reward-Profile Register

This register accompanies `FOCUS_STRUCTURE_REWORK.md`. It records permanent reward profiles introduced or proposed by the structure pass and prevents different countries from receiving the same mechanical identity for the same kind of choice.

A conflict exists when profiles in the same decision type share at least two of three principal modifier categories. Similar modifiers used for materially different decision types are recorded but do not automatically constitute a conflict. Immediate political power, experience and stability rewards are excluded unless they form the lasting identity of the choice.

## Implemented profiles

| Decision type | Country and focus | Permanent profile | Status |
|---|---|---|---|
| Minor maritime theatre commitment | Denmark — `AOEIW9_DEN_dip_a_5` | Naval organisation, naval speed, convoy escort | Implemented |
| Minor continental theatre commitment | Denmark — `AOEIW9_DEN_dip_b_5` | Military-factory output, arms-factory construction, recruitable population | Implemented |
| Minor continental theatre commitment | Norway — `AOEIW9_NOR_dip_a_5` | Army organisation, planning, recruitable population | Implemented |
| Minor maritime theatre commitment | Norway — `AOEIW9_NOR_dip_b_5` | Naval organisation, naval speed, dockyard output | Implemented |
| Minor continental theatre commitment | Ireland — `AOEIW9_IRE_dip_a_5` | Army organisation, arms-factory construction, recruitable population | Implemented |
| Minor maritime theatre commitment | Ireland — `AOEIW9_IRE_dip_b_5` | Convoy escort, dockyard output, trade influence | Implemented |
| Major continental economic method | France — `AOEIW9_FRA_dip_a_3` | Trade influence, factory-efficiency growth, infrastructure construction | Implemented |
| Major continental military method | France — `AOEIW9_FRA_dip_a_5` | Army organisation, supply consumption, land-fort construction | Implemented |
| Major maritime economic method | France — `AOEIW9_FRA_dip_b_3` | Dockyard output, trade influence, consumer-goods demand | Implemented |
| Major maritime military method | France — `AOEIW9_FRA_dip_b_5` | Naval organisation, air-mission efficiency, naval-base construction | Implemented |
| Major maritime military method | USA — `AOEIW9_USA_dip_a_2` | Convoy escort, naval organisation, naval-base construction | Implemented |
| Major maritime economic method | USA — `AOEIW9_USA_dip_a_3` | Trade influence, factory-efficiency growth, consumer-goods demand | Implemented |
| Major maritime military method | USA — `AOEIW9_USA_dip_b_2` | Air-mission efficiency, naval organisation, air-base construction | Implemented |
| Major maritime economic method | USA — `AOEIW9_USA_dip_b_3` | Dockyard output, resource extraction, trade influence | Implemented |
| Industrial endgame | USA — `AOEIW9_USA_special_8` | Military-factory output, maximum production efficiency, supply consumption | Implemented |
| Secession settlement | USA — `AOEIW22_USA_reunify_union` | Stability, political power, consumer-goods demand | Implemented |
| Constitutional settlement | USA — `AOEIW22_USA_anglo_monarchy` | Political power, stability, trade influence, consumer-goods demand | Implemented |
| Constitutional settlement | USA — `AOEIW22_USA_aristocratic_republic` | Political power, stability, research speed, military-factory output | Implemented |
| Major maritime military method | United Kingdom — `AOEIW9_ENG_dip_a_2` | Convoy escort, naval detection, naval coordination | Implemented |
| Major maritime economic method | United Kingdom — `AOEIW9_ENG_dip_a_3` | Dockyard construction speed, subjects' autonomy gain reduction, trade influence | Implemented |
| Major continental military method | United Kingdom — `AOEIW9_ENG_dip_b_2` | Planning speed, reinforcement rate, army defence | Implemented |
| Major continental economic method | United Kingdom — `AOEIW9_ENG_dip_b_3` | Intelligence-network growth, military-factory output, war support | Implemented |

The apparent `military-factory output` label in this register refers to `industrial_capacity_factory`; arms-factory construction is recorded separately as `production_speed_arms_factory_factor`.

## Proposed profiles

| Decision type | Country and focus | Proposed profile | Register result |
|---|---|---|---|
| Major continental economic method | Russia — `AOEIW9_SOV_dip_a_3` | Trade influence, factory-efficiency growth, infrastructure construction | **Conflict:** exact France Rhine economic profile. Russia proposal must be rewritten before approval. |
| Major continental military method | Russia — `AOEIW9_SOV_dip_a_4` | Army organisation, supply consumption, land-fort construction | **Conflict:** exact France Rhine military profile. Russia proposal must be rewritten before approval. |
| Major continental economic method | Russia — `AOEIW9_SOV_dip_b_3` | Resource extraction, trade influence, infrastructure construction | **Conflict:** 2/3 overlap with France Rhine economic profile. Russia proposal must be rewritten before approval. |
| Major maritime military method | Russia — `AOEIW9_SOV_dip_b_4` | Naval organisation, air-mission support, naval-base construction | **Conflict:** exact France Mediterranean military profile. Russia proposal must be rewritten before approval. |

## USA internal divergence check

The four implemented American theatre-method profiles were compared pairwise before any retrospective correction to conflict pairs 5–10. No pair currently reaches the 2-of-3 conflict threshold. Any later approved correction must be checked against all three other American profiles again.

| USA profile pair | Shared principal categories | Result |
|---|---|---|
| Atlantic mission ↔ Pacific mission | Naval organisation (1/3) | No internal conflict |
| Atlantic mission ↔ Atlantic commercial pressure | None (0/3) | No internal conflict |
| Atlantic mission ↔ Pacific commercial pressure | None (0/3) | No internal conflict |
| Pacific mission ↔ Atlantic commercial pressure | None (0/3) | No internal conflict |
| Pacific mission ↔ Pacific commercial pressure | None (0/3) | No internal conflict |
| Atlantic commercial pressure ↔ Pacific commercial pressure | Trade influence (1/3) | No internal conflict |

## Retrospective implemented-country conflicts

No gameplay change in this section is authorized. Each conflict requires a separate user decision before implementation.

| Pair | Shared categories | Finding | Narrow correction proposed |
|---|---|---|---|
| Denmark Baltic Sound ↔ Norway Atlantic Lifeline | Naval organisation, naval speed | **Conflict (2/3)** | Change Norway to naval speed, navy fuel consumption and dockyard construction speed, representing long coastal distances and austere Norwegian basing. Denmark retains command of enclosed straits. |
| Denmark Continental Mobilisation ↔ Ireland Border Emergency | Arms-factory construction, recruitable population | **Conflict (2/3)** | Change Ireland to army defence, mobilisation speed and stability, representing border security and emergency institutions rather than continental mass mobilisation. |
| Norway Scandinavian Field Command ↔ Ireland Border Emergency | Army organisation, recruitable population | **Conflict (2/3)** | The same proposed Ireland correction resolves this pair while Norway retains planning for Scandinavian field operations. This remains a separate approval item because it is a separate conflict pair. |
| Ireland Atlantic Republic ↔ France Mediterranean Commerce | Dockyard output, trade influence | **Conflict (2/3)** | Change Ireland to convoy escort, trade influence and political-power growth, representing diaspora shipping and neutral brokerage rather than dockyard-led imperial commerce. |
| Denmark Baltic Sound ↔ USA Atlantic Mission | Convoy escort, naval organisation | **Conflict (2/3)** | Change the USA Atlantic mission to naval detection, convoy escort and radar-station construction, representing hemispheric surveillance rather than control of narrow seas. |
| France Mediterranean Military ↔ USA Atlantic Mission | Naval organisation, naval-base construction | **Conflict (2/3)** | The proposed USA Atlantic surveillance correction also resolves this pair; France retains fleet organisation and Mediterranean bases. Separate approval is still required for this pair. |
| France Mediterranean Military ↔ USA Pacific Mission | Naval organisation, air-mission efficiency | **Conflict (2/3)** | Change the USA Pacific mission to sortie efficiency, air-mission efficiency and air-base construction, making carrier aviation and island airfields its identity. |
| France Mediterranean Commerce ↔ USA Atlantic Commercial Pressure | Trade influence, consumer-goods demand | **Conflict (2/3)** | Change the USA Atlantic commercial profile to trade influence, factory-efficiency growth and political-power growth, representing Wall Street credit and federal purchasing. |
| Ireland Atlantic Republic ↔ USA Pacific Commercial Pressure | Dockyard output, trade influence | **Conflict (2/3)** | Change the USA Pacific profile to dockyard output, resource extraction and dockyard construction speed. Ireland's separately proposed correction would also remove the overlap, but this pair retains its own approval gate. |
| France Mediterranean Commerce ↔ USA Pacific Commercial Pressure | Dockyard output, trade influence | **Conflict (2/3)** | The proposed USA Pacific shipbuilding/resource correction resolves this pair while France keeps Mediterranean trade and consumer relief. Separate approval is still required for this pair. |

## Register maintenance rule

Every future structural proposal must add its permanent profiles here before approval. The proposal must name the nearest existing profile in the same decision type and count shared principal categories. A 2/3-or-greater match must be redesigned around the country's geography, economy, imperial relationships or military institutions before implementation.

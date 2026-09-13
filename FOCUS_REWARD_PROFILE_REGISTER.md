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
| Major maritime military method | USA — `AOEIW9_USA_dip_a_2` | Convoy escort, radar-station construction, decryption | Implemented; pair 5 correction |
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
| Major continental economic method | Russia — `AOEIW9_SOV_dip_a_3` | Railway construction, resource-penalty reduction, fuel gain | No conflict; broad-gauge mobilisation and reserves are specifically Russian. |
| Major continental military method | Russia — `AOEIW9_SOV_dip_a_4` | Winter-attrition reduction, army speed, reduced organisation loss while moving | No conflict; this represents movement and cohesion across Russia's winter frontier. |
| Major maritime economic method | Russia — `AOEIW9_SOV_dip_b_3` | Resource extraction, trade influence, railway construction | No conflict; the Black Sea export corridor shares at most one category with any registered profile. |
| Major maritime military method | Russia — `AOEIW9_SOV_dip_b_4` | Naval minelaying, navy fuel consumption, repair speed | No conflict; this represents an austere Black Sea fleet based at Sevastopol. |
| Industrial endgame | Russia — `AOEIW9_SOV_special_8` | Military-factory output, resource extraction, railway construction | No conflict; only military-factory output overlaps the USA industrial endgame. |

## Consolidated closure proposal — awaiting one approval

The repository still records conflict pairs 1–4 as open. They are included here because the register cannot truthfully be declared conflict-free by addressing only Russia and pairs 7–10. Pair 3 is closed by the same Irish Border Emergency change as pair 2; pair 10 is closed by the same USA Pacific commerce change as pair 9.

| Country/focus | Current or withdrawn profile | Proposed final profile | Conflict pair(s) | Full-register result |
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

Russia's accompanying structural package remains the one already documented in `FOCUS_STRUCTURE_REWORK.md`: mutex methods with OR reconvergence inside both compatible theatres; mutex Field Workshops/Signals; the Ural logistics prerequisite for the industrial capstone; the industrial-colossus prerequisite and permanent spirit; and targeted AI weights. Existing IDs, political architectures, targets, war goals and immediate rewards remain preserved.

The proposed final-state matrix contains **zero 2/3 conflicts** within either the maritime or continental profile groups. All six pairwise comparisons among the four final USA method profiles are 0/3. Among Russia's four method profiles, only the two economic methods share railway construction (1/3); every other Russian pair is 0/3.

## USA internal divergence check

The four implemented American theatre-method profiles were compared pairwise before any retrospective correction to conflict pairs 5–10. No pair currently reaches the 2-of-3 conflict threshold. Any later approved correction must be checked against all three other American profiles again.

| USA profile pair | Shared principal categories | Result |
|---|---|---|
| Atlantic mission ↔ Pacific mission | None (0/3) | No internal conflict |
| Atlantic mission ↔ Atlantic commercial pressure | None (0/3) | No internal conflict |
| Atlantic mission ↔ Pacific commercial pressure | None (0/3) | No internal conflict |
| Pacific mission ↔ Atlantic commercial pressure | None (0/3) | No internal conflict |
| Pacific mission ↔ Pacific commercial pressure | None (0/3) | No internal conflict |
| Atlantic commercial pressure ↔ Pacific commercial pressure | Trade influence (1/3) | No internal conflict |

## Retrospective implemented-country conflicts

No gameplay change in this section is authorized yet. The earlier separate-pair gates have been replaced by the single consolidated approval table above.

### Pair 5 implementation record

The earlier suggestion of naval detection, convoy escort and radar construction is withdrawn. It would remove the Danish overlap but share convoy escort and naval detection with Britain's later-registered Admiralty profile, creating a new 2-of-3 conflict.

The revised American profile is **convoy escort, radar-station construction and decryption**. It represents the United States Navy's Neutrality Patrol, a continental coastal-warning network and American signals intelligence. Radar construction is treated as a construction category, distinct from Britain's permanent naval-detection bonus; decryption is an intelligence category, distinct from British naval coordination.

| Current registered maritime profile checked | Shared categories with revised USA Atlantic mission | Result |
|---|---|---|
| Denmark — Baltic Sound | Convoy escort (1/3) | No conflict; Denmark retains naval organisation and speed for control of enclosed straits. |
| Norway — Atlantic Lifeline | None (0/3) | No conflict. |
| Ireland — Atlantic Republic | Convoy escort (1/3) | No conflict. |
| France — Mediterranean military posture | None (0/3) | No conflict. |
| USA — Pacific mission | None (0/3) | No internal conflict. |
| United Kingdom — Admiralty Atlantic mission | Convoy escort (1/3) | No conflict; British detection and coordination remain distinct. |
| Russia — proposed maritime military method | None (0/3) | No conflict with the currently registered, still-unapproved Russian draft. |

This profile was approved and implemented. The focus ID and its existing immediate rewards remain unchanged.

### Pair 7 detail — included in the consolidated closure proposal

Change the USA Pacific mission to **sortie efficiency, air-mission efficiency and air-base construction**. This represents carrier-deck tempo, naval aviation coordination and the island airfield chain. It removes naval organisation, the category shared with France, while retaining one deliberately shared air-mission category.

| Current registered maritime profile checked | Shared categories with proposed USA Pacific mission | Result |
|---|---|---|
| Denmark — Baltic Sound | None (0/3) | No conflict. |
| Norway — Atlantic Lifeline | None (0/3) | No conflict. |
| Ireland — Atlantic Republic | None (0/3) | No conflict. |
| France — Mediterranean military posture | Air-mission efficiency (1/3) | No conflict; France retains naval organisation and naval-base construction. |
| USA — corrected Atlantic mission | None (0/3) | No internal conflict. |
| USA — Atlantic commercial pressure | None (0/3) | No internal conflict. |
| USA — Pacific commercial pressure | None (0/3) | No internal conflict. |
| United Kingdom — Admiralty Atlantic mission | None (0/3) | No conflict. |
| Russia — proposed Black Sea military method | None (0/3) | No conflict with the rewritten Russian proposal. |

This is a proposal only. No USA gameplay or localisation file has been changed for pair 7.

| Pair | Shared categories | Finding | Narrow correction proposed |
|---|---|---|---|
| Denmark Baltic Sound ↔ Norway Atlantic Lifeline | Naval organisation, naval speed | **Conflict (2/3)** | Change Norway to naval speed, navy fuel consumption and dockyard construction speed, representing long coastal distances and austere Norwegian basing. Denmark retains command of enclosed straits. Included in the consolidated closure proposal. |
| Denmark Continental Mobilisation ↔ Ireland Border Emergency | Arms-factory construction, recruitable population | **Conflict (2/3)** | Change Ireland to army defence, mobilisation speed and stability, representing border security and emergency institutions rather than continental mass mobilisation. Included in the consolidated closure proposal. |
| Norway Scandinavian Field Command ↔ Ireland Border Emergency | Army organisation, recruitable population | **Conflict (2/3)** | The pair-2 Irish correction also resolves this pair; no second gameplay change is required. Included as a cascade in the consolidated closure proposal. |
| Ireland Atlantic Republic ↔ France Mediterranean Commerce | Dockyard output, trade influence | **Conflict (2/3)** | Change Ireland to convoy escort, trade influence and stability, representing diaspora shipping and the credibility of armed neutrality. Included in the consolidated closure proposal. |
| Denmark Baltic Sound ↔ USA Atlantic Mission | Convoy escort only after correction | **Resolved (1/3)** | The approved USA Atlantic mission now uses convoy escort, radar-station construction and decryption. Denmark retains naval organisation and speed; the corrected American profile creates no new 2/3 conflict in the complete post-UK register. |
| France Mediterranean Military ↔ USA Atlantic Mission | None after the pair 5 correction | **Resolved (0/3)** | Closed with separate approval and no further gameplay change. France retains naval organisation, air-mission efficiency and naval-base construction; the USA Atlantic mission now uses convoy escort, radar-station construction and decryption. |
| France Mediterranean Military ↔ USA Pacific Mission | Naval organisation, air-mission efficiency | **Conflict (2/3)** | Change the USA Pacific mission to sortie efficiency, air-mission efficiency and air-base construction, making carrier aviation and island airfields its identity. Full-register review found no resulting 2/3 conflict. |
| France Mediterranean Commerce ↔ USA Atlantic Commercial Pressure | Trade influence, consumer-goods demand | **Conflict (2/3)** | Change the USA Atlantic profile to factory-efficiency growth, political-power growth and civilian-factory construction. Removing trade avoids a new 2/3 overlap with France's Rhine profile. Included in the consolidated closure proposal. |
| Ireland Atlantic Republic ↔ USA Pacific Commercial Pressure | Dockyard output, trade influence | **Conflict (2/3)** | Change the USA Pacific profile to dockyard output, resource extraction and dockyard construction speed. The revised Irish Atlantic profile leaves only dockyard output in common. Included in the consolidated closure proposal. |
| France Mediterranean Commerce ↔ USA Pacific Commercial Pressure | Dockyard output, trade influence | **Conflict (2/3)** | The pair-9 USA Pacific correction removes trade and resolves this pair; no second gameplay change is required. Included as a cascade in the consolidated closure proposal. |

## Register maintenance rule

Every future structural proposal must add its permanent profiles here before approval. The proposal must name the nearest existing profile in the same decision type and count shared principal categories. A 2/3-or-greater match must be redesigned around the country's geography, economy, imperial relationships or military institutions before implementation.

Retrospective corrections must be rechecked against the **entire current register**, including profiles added after the original conflict was recorded and unapproved profiles that are still active proposals. Passing the original pairwise comparison is not sufficient. If a later profile creates a new 2/3 match, the correction must be redesigned and presented again before any gameplay implementation.

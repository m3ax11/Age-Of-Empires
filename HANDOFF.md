# Age of Empires — RT56 Edition: development handoff

Reconstructed from the supplied archive on 2026-09-10 and advanced as a release-candidate working copy on 2026-09-11. The original archive remains the provenance baseline; this file records the current implementation state.

## 2026-09-11 release-candidate status

The working copy is now a Git repository. Commit `a29d19aa` is the untouched extracted archive plus the initial audit handoff. All later work is reviewable against that baseline. Do not discard the current working tree: it contains the integrated release pass.

Completed in the current working tree:

- Repaired the unmatched brace in `common/characters/KAL.txt`.
- Restored four compatibility ideas used by the legacy China handlers without changing the CHI-player/MAN-Puyi architecture.
- Removed thirteen duplicate scripted-trigger collisions by renaming the earlier redundant definitions with the `AOEIW_legacy_` prefix; the later RT56 definitions remain authoritative.
- Completed all previously missing AOE English localization detected by the validator and replaced the visible USA mobilization placeholder.
- Reorganized Spanish South America into two integrated subjects. ARG administers the Southern Cone; PRU administers the Andes and northern Spanish South America. Both retain local cores and Spain retains imperial cores. Central America and the Caribbean remain directly Spanish.
- Added Spain's Cádiz imperial-governance lifecycle: 11 focuses, 12 decisions, 18 events, 11 spirits, 3 dynamic modifiers and 4 AI plans. It covers Argentine and Peruvian investment, petitions, wartime mobilization, foreign reactions and a postwar commonwealth/directorate payoff.
- Added Germany's release-candidate continuation: 28 focuses, 7 decisions, 20 events, 20 ideas and 6 AI plans. The four political outcomes now lead into distinct continental orders, while economy, resource, armed-forces and postwar settlement branches provide 1940s play.
- Added the `AOEIW37_WORLD` imperial-war and aftermath chain for FRA–MLI/VIN, SOV–UKR/GEO/KAZ and POR–BRA. War service, metropolitan collapse, subject memoranda, reconstruction policy, outside-power reactions and joint supply boards now form one sequence.
- Replaced all eleven broken icon identifiers in `AOEIW_historical_germany_ideas.txt`, supplied the existing large Choybalsan portrait, and resolved new Germany/Spain/world icon references against the installed game assets.
- Reconciled the standalone installation instructions in `README.txt` and `AOE_RT56_EDITION_README.txt`.
- Added `tools/validate_aoeiw.py`. With installed HOI4 1.19.2 as its reference, it currently parses 5,257 mod script files and reports no proven brace, duplicate AOE ID, AOE reference, AOE English-localization, province/strategic-region or Spanish-subject contract failures.

The every-country inventory covers all 49 countries that directly own a state in the supported 1936 start. Forty-five have an AOE-selected tree. ADR, LIE, MNC and SAN rely on inherited/shared microstate content. The detailed tier table and risk assessment are in `work/world-release-audit.md` outside the packaged mod; `work/country-coverage.json` is its machine-readable source.

Work still in progress: regional authored-content passes under the `AOEIW38_AMERICAS_AFRICA`, `AOEIW38_EUROPE` and `AOEIW38_ASIA_MIDDLE` prefixes. These target repeated generic mid-tier content, Mongolia, Yemen, regional reactions and postwar outcomes. Re-run the full validator and asset/reference scans after integrating them.

Known release gate: no fresh game has yet loaded this exact post-change working tree. A separate HOI4 process was already running another mod, so it was not interrupted. Before packaging, run only this edition on HOI4 1.19.2, start Time of Upheaval in 1936, preserve the raw `error.log`, and smoke-test GER, SPR/ARG/PRU, CHI/MAN, USA, British succession and one imperial-aftermath chain.

## Authoritative input and working copy

- User-selected source: `C:\Users\Stack\Documents\Codex\2026-08-20\files-mentioned-by-the-user-agentic\r6\Age Of Empires - RT56 Edition.zip`.
- ZIP SHA-256: `2b424e8ab25ef102eda864e4a9e553a6ec6eb90d96382e975b63252cee6a26e7`.
- Extracted working copy: `C:\Users\Stack\Documents\Codex\2026-09-10\we-are-continuing-development-of-an\work\archive-audit\Age_Of_Empires_RT56_Edition`.
- This handoff is also copied into that working copy as `HANDOFF.md`. The original ZIP remains unchanged. Other installed/Desktop copies were not treated as sources or merged into this copy.
- No `AGENTS.md`, existing handoff, dedicated TODO file, or Git metadata was present in the archive. Git was initialized after extraction; `a29d19aa` records the archive baseline.

All paths below are relative to the extracted mod root unless explicitly absolute.

## Current state

This is an extensive standalone, all-in-one merger of The Road to 56, Age of Empires, and their compatibility layer. `descriptor.mod` declares HOI4 `1.19.*` and replaces `history/states` and `map/strategicregions`. That is a declared target, not a verified runtime result.

`AOE_RT56_EDITION_README.txt` and `README.txt` now consistently say to enable **only this edition**, without separate RT56/AOE/compatibility mods, and start a new game after updating. `README.md` is inherited RT56 contributor documentation, including attribution and contribution conventions, rather than an AOE design specification. `Credits.txt` and `Unique Commanders IDS.txt` should be retained.

The archive contains 29,554 files. Principal counts:

| Area | Files / definitions |
|---|---|
| National focuses | 251 files; 26,844 focus definitions across the merged content |
| AOE focus content | 56 tree definitions; 4,043 AOE-prefixed focuses |
| Events | 288 files; 11,427 event definitions |
| Decisions | 322 files including categories |
| Shared scripting | 34 on-action files, 50 scripted-effect files, 40 scripted-trigger files |
| History | 409 country files, 614 unit/OOB files, 1,143 state files |
| Map | 298 strategic regions; full province, terrain, railway, supply and other map assets |
| Localisation | 350 files under English and 47 under German; additional language/replace folders |

Content names span older V6–V10/phase systems through phase 35. `common/national_focus/AOEIW_GER_focus.txt:2` explicitly labels its layout `AOEIW36 wide modular layout`. These names establish that content exists, not a trustworthy chronological changelog.

## Design and lore to preserve

- The supported AOE scenario is **Time of Upheaval**, starting `1936.1.1.12`, in `common/bookmarks/the_gathering_storm.txt`. The canonical English bookmark text is in `localisation/english/zzzzzzzzzzzzzzzzzz_AOEIW_V83_canonical_l_english.yml:2–11`.
- The imperial order survived into 1936: Germany is an empire and dominant continental military power; France is the Second French Empire under Napoleon IV; SOV represents the Russian Empire under threat of reform/reaction/revolution; Spain remains an empire under Alfonso XIII; the Ottoman state survives. Do not “correct” these to vanilla history.
- `SOV` is deliberately reused for imperial Russia. British history recruits Queen Victoria and a King George alternative, and the succession decisions allow choosing between them. Historical longevity is a setting choice, not an audit bug.
- The setting supports imperial, democratic, nationalist and revolutionary alternatives, including extensive communist routes for France, Germany, Italy and Russia. Preserve the existing branch choices.
- Vanilla ideology groups coexist with `imperialism`, `constitutional_monarchism`, and `autocratic_imperialism`, defined in `common/ideologies/age_of_empires_imperial_world_leaders_ideologies.txt`. Their subtypes and character roles are cross-referenced by political transitions and repair hooks.
- Country history plus startup hooks establish imperial subjects and factions. German history creates the Reichspakt. World-expansion startup makes UKR/GEO/KAZ Russian subjects, EST/MAL German subjects, MLI/VIN French subjects, and ARG/PRU Spanish subjects.
- The **current edition begins with the former American breakaways already integrated into USA**. `common/on_actions/zzzzzz_AOEIW_world_expansion_on_actions.txt:22–29` explicitly says this and sets the reunited flag. Do not restore a divided America merely because old reclamation decisions remain.
- **China stability constraint:** `common/scripted_effects/AOEIW_phase20_chinese_crisis_effects.txt:1–3` requires CHI to remain the player and become the United Front; MAN carries Puyi's Qing state from its Jehol bootstrap to its postwar settlement. No civil-war engine, tag swap, or landless-tag spawn in this chain. The startup hook also preserves global target `WTT_communist_china` to avoid an empty-country dereference in inherited WTT decisions.
- `common/bookmarks/blitzkrieg.txt` is an explicitly unsupported inherited 1939 bookmark whose comments say to retain it because deletion breaks menu elements. Do not remove it to enforce the single AOE scenario.

## Architecture and important paths

| System | Entry points and responsibilities |
|---|---|
| Countries and characters | `common/country_tags/`, `common/countries/`, `common/characters/`, `history/countries/`; vanilla tag definitions may come from the base game |
| Main country trees | `common/national_focus/AOEIW_<TAG>_focus.txt`; major AOE selectors commonly have weight 10,000, above inherited RT56 trees |
| China/frontier trees | `AOEIW_phase20_united_front_focus.txt` has holding/UF selectors at 200,000/100,000; `AOEIW_frontier_{MAN,MON,QIN,XIC}_focus.txt` adds frontier content |
| World expansion | `common/national_focus/AOEIW_world_expansion_focus.txt`, matching decisions/events/ideas/characters/localisation and `zzzzzz_AOEIW_world_expansion_on_actions.txt` |
| Events and decisions | `events/AOEIW*`, `common/decisions/AOEIW*`, `common/decisions/categories/AOEIW*`; coexist with retained RT56/vanilla-derived content |
| Shared effects/triggers | `common/scripted_effects/AOEIW*` handles political transitions, China, Russian revolution, consolidation, coalitions and QoL; AOE also uses inherited `common/scripted_triggers/` definitions |
| Germany parliament | `common/scripted_effects/AOEIW28_german_coalitions.txt`, `events/AOEIW28_german_elections.txt`, matching on-actions/decisions, `AOEIW34_german_election_campaign.txt`, and `interface/AOEIW34_rt56_parliament_assets.gfx`; phase-34 polls feed phase-30 seat variables and phase-29 cabinet logic |
| Systemic political depth | `AOEIW22_nationalities_on_actions.txt`, `AOEIW24_systemic_depth.txt` across on-actions/events/decisions; Austrian crownland tensions and USA/SOV/ITA political variables |
| Governance/programmes | `common/bop/AOEIW35_major_governance.txt`, `common/dynamic_modifiers/AOEIW35_major_programmes.txt`, phase-35 focuses/events/decisions; phase-32 programmes and phase-35 frontier life also exist |
| Consolidation/postwar | `common/scripted_effects/AOEIW_consolidation_effects.txt`, `common/decisions/AOEIW_consolidation_systems.txt`, final faction/Japan/postwar decisions and events |
| Super-events/UI | phase-21 events/on-actions, `common/scripted_guis/AOEIW_phase21_super_events.txt`, scripted localisation, interface/GFX, `sound/AOEIW_phase21_super_events.asset`; hidden manual test hooks are intentional |
| OOBs and map | `history/units/AOEIW*` has land/naval and BBA/legacy-air variants; `RT56_STATE_MERGE.csv` is the geographical mapping ledger |
| Localisation | `localisation/english/`, `localisation/german/`, `localisation/replace/`; canonical/repair files have long `zz...` prefixes |

The state merge ledger has 1,143 rows: 991 exact-label matches, 118 owner transitions, 29 stable-legacy-ID matches, and 5 retained RT56-owner states. There are **116 cross-numeric-ID mappings**. RT56 provides topology; AOE supplies scenario ownership/imperial cores. Never equate an old AOE state ID with an RT56 state ID without checking this ledger and the actual state file.

World tree IDs also deliberately preserve old conceptual tags while their selectors use reused country slots: BTF→EST, CAF→GEO, TRK→KAZ, HEJ→OMA, INA→VIN, FWA→MLI, GEA→MAL, NEE→QUE, TCO→CSA, FAM→HAI. Preserve both the old content IDs and actual target tags.

## Work already present and checks completed

“Present” means implemented in files, not proven complete through gameplay. The build already contains the merged world, substantial country trees and political alternatives, China redesign and legacy compatibility handlers, German election/coalition mechanics, governance balances, national programmes, frontier content, initial army/doctrine support, super-events and UI work. These should be repaired narrowly rather than replaced.

This audit indexed 5,242 script/interface/map definition files with a comment/string-aware structural scanner, followed by targeted manual inspection and reference checks. Results:

- No duplicate event, focus, state, strategic-region or scripted-effect IDs found in the scanned archive definitions.
- No duplicate AOE-related idea, character, decision-category, dynamic-modifier or balance-of-power definitions found in the checked structures.
- No custom focus prerequisite cycles or empty custom focus reward blocks found.
- No unresolved AOE event/focus/OOB references in the checked reference forms; custom effect/trigger calls, focus shortcut/relative-position references, and checked explicit state references resolved.
- No duplicate province assignments across states or across strategic regions; all state provinces have a strategic region. This is not a complete terrain/adjacency/railway validation.
- No missing referenced files among the 72 locally declared country tags. Base-game tags are not fully redeclared here.
- Custom localisation files checked had BOMs and language headers. No duplicate AOE-prefixed English keys found by the key scan; keep naming conventions despite that clean result.
- All extracted original files matched their ZIP CRCs before adding this handoff.

## Initial audit findings and disposition

### 1. Confirmed structural error — resolved

`common/characters/KAL.txt` had one unmatched opening brace. The missing top-level closure has been restored, and the release validator now reports no structural imbalance.

### 2. Confirmed English localisation gaps — resolved

The following world-expansion gaps were present in the archive and have now been localized:

- Seven spirit names in `common/ideas/AOEIW_world_expansion_ideas.txt`: `AOEIW_world_frontier_state`, `AOEIW_world_colonial_administration`, `AOEIW_world_american_breakaway`, `AOEIW_world_USA_fractured_republic`, `AOEIW_world_USA_industrial_recovery`, `AOEIW_world_USA_reunited`, `AOEIW_world_FRA_metropolitan_command`. Several are applied at startup, so this is not exclusively dormant content.
- Both categories in `common/decisions/categories/AOEIW_world_expansion_categories.txt`: `AOEIW_world_american_reclamation_category` and `AOEIW_world_british_succession_category`.
- All five decision names in `common/decisions/AOEIW_world_expansion_decisions.txt`: emergency reconstruction, federal mobilisation, reclamation, proclaim King George, confirm Queen Victoria (preserve their exact IDs).
- Seven event strings in `events/AOEIW_world_expansion_events.txt`: `AOEIW_world.1.t/.d/.a` and `AOEIW_world.2.t/.d/.a/.b`.
- The broader scan also found missing research/doctrine-bonus display names such as `AOEIW_event_land_doctrine` and `AOEIW_AUS_event_air` in country event files. These are bonus labels, not missing event titles; review their presentation separately.

The added release content also has complete English names and descriptions under its own prefixes. Two character-ID lookup candidates remain intentional: `AOEIW20_QIN_puyi` and `AOEIW20_MAN_puyi` explicitly use the existing `AOEIW_CHI_puyi` name key.

### 3. Legacy China compatibility debt — resolved

`common/national_focus/AOEIW_CHI_focus.txt` referenced four undefined idea IDs: `AOEIW20_CHI_dynastic_crisis`, `AOEIW20_CHI_costly_dynastic_settlement`, `AOEIW20_CHI_nra_underground`, and `AOEIW20_CHI_mao_underground`. Compatibility definitions now exist in `common/ideas/AOEIW_phase20_chinese_crisis.txt`.

The normal CHI selectors still prefer the newer holding/UF trees, and the compatibility definitions do not revive the superseded unstable China implementation.

### 4. Inherited integration candidates needing runtime/base-game verification

- Thirteen scripted-trigger IDs were defined more than once. Earlier redundant copies now use the `AOEIW_legacy_` prefix, preserving the source for review while leaving the later RT56 definitions authoritative.
- Namespace case mismatches occur in inherited files: `BBA_Switzerland` is declared but 31 events use `BBA_switzerland`; `NSB_news.200` also differs from the declared lowercase namespace. Treat as candidates until checked against engine behavior; no such mismatch was found for AOE events.
- The archive-only scan reports 301 unresolved event-reference occurrences, 8 focus-reference occurrences and 74 OOB-reference occurrences outside the AOE subset. Some can resolve from the base game/DLC or parameter substitution. These are **not 383 confirmed bugs**. Example candidates include `PRC_sea_soviet_advisors`, `GER_around_maginot_vanilla`, and `GER_weserubung`.
- The USA reclamation chain remains alongside an already-reunited start. Its launch requires QUE/CSA/HAI to exist, so the normal start appears to block that old chain. Confirm intended visibility/release behavior before deleting it.
- Phase-35 governance, phase-36 layout and German coalition transitions need in-game regression coverage. Static completeness does not prove correct scopes, UI behavior, reachable branches or balanced effects.

### 5. Explicit AOE TODOs and documentation debt — resolved

- The German transport aircraft are now documented as an intentional limited airborne capability.
- The Russian transport brigade is explicitly abstracted into the logistics pool rather than left as an unfinished note.
- The restored Choybalsan advisor now uses the existing RT56 large portrait.
- Many other TODO/placeholder hits belong to inherited RT56 content, and “unfinished” also occurs in deliberate lore titles. They are not evidence of a half-completed previous-session edit.
- Reconcile the old compatibility README with the standalone instructions. No archive-local test history or patch-by-patch completion log establishes what the previous session finished.

## Conventions and next task

Preserve all `AOEIW`, numbered phase prefixes, lower-/uppercase event namespaces, variables, country/global flags, cosmetic tags, event targets, and focus IDs. Filename age does not mean obsolete: phase-28 files contain phase-34 logic. Preserve selector weights, mutually exclusive branches, `allow_branch` visibility and existing layout-dirty calls unless a specific defect warrants changing them. Keep UTF-8 BOM/language headers in localisation and retain attribution. The inherited commander ID document reserves future legacy IDs starting at 5600; check existing allocations before adding legacy IDs.

**Recommended next task:** finish and validate the three AOEIW38 regional batches, then perform the exact-build fresh-start/runtime gate described near the top of this handoff. Prioritize engine errors that cite AOE-owned files; qualify inherited RT56 warnings rather than changing them blindly.

The bundled `errorlog_cleaner.py` rewrites the installed game's log to suppress some entries; it was not run. Keep raw logs for validation.

## Audit limitations and reproducibility

No game was launched, no saved campaign was loaded, and no external RT56/vanilla installation was used to complete the reference database. All binary assets were inventoried and CRC-checked but not visually reviewed. This is a repository-level structural/reference audit, not an exhaustive engine schema validator or a full gameplay QA pass.

Audit helpers live outside the mod in the task workspace: `work/audit_mod.py`, `work/deep_audit.py`, `work/final_checks.py`; machine results are in `work/audit-results/`. Run the helpers in that order from the task workspace. Candidate reports contain the intentionally qualified/false-positive cases discussed above; do not auto-fix their raw output. No mod scripts were executed by these helpers.

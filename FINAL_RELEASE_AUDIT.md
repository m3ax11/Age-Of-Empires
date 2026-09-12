# Age of Empires — RT56 Edition: maximaler Final-Release-Audit

Stand: 12. September 2026, Repository-HEAD `d611a3c3`. Dieses Dokument ist die verbindliche Restarbeitenliste für den finalen Patch. Es unterscheidet bestätigte Fehler, statisch belegte Qualitätsprobleme, Runtime-Prüfpflichten und optionale Verbesserungen. Bestehende Lore, IDs und funktionierende Systeme werden nicht allein aus Stilgründen ersetzt.

## Release-Urteil

Der Mod ist strukturell wesentlich weiter als ein Prototyp: 4.107 AOE-Fokusse, 867 AOE-Events, ungefähr 446 AOE-Entscheidungsdefinitionen, vollständige Länder- und Kartenhistorie sowie mehrere miteinander verbundene Endgame-Systeme sind vorhanden. Der statische Validator parst 5.279 relevante Dateien und findet derzeit **keinen bestätigten AOE-Struktur-, Referenz-, englischen Lokalisierungs-, Karten- oder Szenariovertragfehler**.

Der aktuelle Build ist trotzdem noch kein freigabefertiger Final-Patch. Die wichtigsten Gründe sind:

1. Der aktuelle HEAD nach Fokuslayout, Kartenregel, Doktrinbonus und Branding wurde noch nicht bis in einen neuen 1936-Spielstand geladen.
2. Es fehlen 1.136 deutsche AOE-Lokalisierungsschlüssel. Die neuesten und wichtigsten Inhaltsserien sind fast vollständig nur Englisch.
3. 3.121 AOE-Beschreibungen gehören zu Textgruppen, die mindestens viermal identisch vorkommen. Besonders Luftwaffe, Marine, Wirtschaft, Politik und die kleineren Länder wirken dadurch sichtbar schablonenhaft.
4. 957 Fokusse haben nach einem bewusst strengen Heuristiktest nur kleine Zahlenbelohnungen; 932 Fokusse dauern 70 Tage. Das ist kein automatischer Fehler, aber ein großer Pacing- und Identitätsprüfbereich.
5. Die 473 Fokusse in `AOEIW_world_expansion_focus.txt` sind der deutlich schwächste Block: 56,4 % dauern 70 Tage und 247 wirken belohnungsseitig rein numerisch.
6. Die wichtigsten Systeme sind statisch vorhanden, aber noch nicht als vollständige 1936–1942-Kampagnen geprüft: Selektoren, Ereignisscopes, Friedensfolgen, Untertanenautonomie, KI, Kartenmodus, +4,50 Erfahrung und Fokusbaumdarstellung.

## Bedeutung der Prioritäten

- **P0 – Releaseblocker:** vor einer öffentlichen Version zwingend beheben oder im aktuellen Build erfolgreich prüfen.
- **P1 – Finished-Feeling:** stärkste sichtbare Qualitätsprobleme; sie entscheiden, ob der Mod handgefertigt und abgeschlossen wirkt.
- **P2 – Kampagnenqualität:** Balance, Langzeitfolgen, KI und länderspezifische Tiefe.
- **P3 – optionale Veredelung:** verbessert Präsentation und Wiederspielwert, blockiert aber keinen stabilen Release Candidate.
- **Bestätigt:** direkt aus Dateien oder Validator reproduzierbar.
- **Prüfkandidat:** statischer Hinweis; erst nach Sicht- oder Spielprüfung ändern.

## P0 — zwingende Releaseblocker

### P0.1 Aktuellen HEAD in einem echten neuen Spiel laden

Der Commit `cf7576f7` dokumentiert einen sauberen Hauptmenüstart eines früheren Inhaltsstands. Danach kamen `339888ab` und `d611a3c3` mit Fokuslayouts, Iconänderungen, Kartenregel, täglicher Erfahrung und Frontendgrafik. Daher gilt der jetzige HEAD noch nicht als enginegeprüft.

Abnahme:

- Nur `Age Of Empires – RT56 Edition` aktivieren.
- HOI4 1.19.x starten und **Time of Upheaval**, 1. Januar 1936 wählen.
- Rohes `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log` sichern; `errorlog_cleaner.py` nicht ausführen.
- Einen Spieltag laufen lassen, speichern, neu laden und bis mindestens 8. Januar laufen lassen.
- Keine AOE-Parserfehler, fehlenden AOE-Sprites, ungültigen Effekte, unbekannten Ideen, ungültigen Zustände oder Scopefehler akzeptieren.
- Prüfen, dass das neue Age-of-Empires-Hauptmenübild, Bookmark, Modname und Ladeschirm gemeinsam erscheinen.

### P0.2 Deutsche Lokalisierung der letzten Inhaltsserien vervollständigen

**Bestätigt:** Von 27.736 englischen AOE-Schlüsseln fehlen 1.136 in Deutsch; Abdeckung 95,9 %. Bei Fokusnamen und Fokusbeschreibungen fehlen 128 von 8.214 Schlüsseln; Abdeckung 98,4 %. In deutscher Sprache erscheinen dadurch Roh-IDs oder englische Lücken in zentralem neuem Inhalt.

Fehlende Schlüssel nach englischer Quelldatei:

| Anzahl | Datei |
|---:|---|
| 200 | `localisation/english/AOEIW37_GER_release_l_english.yml` |
| 185 | `localisation/english/AOEIW38_ASIA_MIDDLE_l_english.yml` |
| 180 | `localisation/english/AOEIW38_AMERICAS_AFRICA_l_english.yml` |
| 171 | `localisation/english/AOEIW37_SPR_imperial_administration_l_english.yml` |
| 168 | `localisation/english/AOEIW_world_expansion_l_english.yml` |
| 114 | `localisation/english/AOEIW38_EUROPE_regional_reckoning_l_english.yml` |
| 76 | `localisation/english/AOEIW37_WORLD_imperial_aftermath_l_english.yml` |
| 12 | `localisation/english/AOEIW24_systemic_depth_l_english.yml` |
| 10 | `localisation/english/AOEIW30_german_parliament_l_english.yml` |
| 10 | `localisation/english/zzzzzzzzzzzzzzzzzzzzzzzzzzzz_AOEIW_historical_germany_l_english.yml` |
| 10 | `localisation/english/zzzzzzzzzzzzzzzzzz_AOEIW_V83_canonical_l_english.yml` |

Die 64 neuen Fokusse ohne deutsche Namen/Beschreibungen verteilen sich auf GER 28, SPR 11, MON 5, YEM 5 sowie BRA, CAN, EGY, ETH und MEX mit jeweils 3. Übersetzungen müssen natürliche deutsche HOI4-Texte sein; maschinell wirkende Wort-für-Wort-Fassungen würden das Problem nur verschieben. UTF-8-BOM und `l_german:` bleiben Pflicht.

### P0.3 Kartenmodusregel im Spiel prüfen

Betroffene Dateien:

- `common/game_rules/zz_AOEIW_game_rules.txt`
- `common/map_modes/zz_AOEIW_imperial_world_map_mode.txt`
- `interface/zz_AOEIW_mapmode.gfx`
- `localisation/english/AOEIW_qol_l_english.yml`
- `localisation/german/AOEIW_qol_l_german.yml`

Abnahme:

- Regel ist im Spielaufbau sichtbar, eindeutig lokalisiert und standardmäßig Ein.
- Ein zeigt die vorgesehenen imperialen, ideologischen, Fraktions-, Untertanen- und Kriegsfarben.
- Aus neutralisiert die AOE-Farbschicht ohne Scriptfehler; Button und Tooltip dürfen nicht behaupten, der Modus sei aktiv.
- Einstellung über Save/Load und Multiplayer-Hostkonfiguration erhalten.
- Kein anderer Kartenmodus und keine politische Standardkartenfarbe wird verändert.

### P0.4 Tägliche +4,50 Armee-, Marine- und Lufterfahrung balancieren

Die vom Nutzer gewünschte Erfahrung ist implementiert in:

- `common/ideas/AOEIW_qol_ideas.txt`
- `common/scripted_effects/zz_AOEIW_qol_effects.txt`
- `common/on_actions/zzzzz_AOEIW_qol_on_actions.txt`

Abnahme:

- Jedes Startland und jedes später entstehende Land erhält exakt einen sichtbaren Bonus.
- Keine monatliche Mehrfachstapelung, kein Verlust nach Bürgerkrieg/Tagwechsel und keine doppelten Ideen nach Save/Load.
- Armee-, Marine- und Luftdoktrin können wie gewünscht bis 1939 abgeschlossen werden.
- KI gibt die Erfahrung tatsächlich für Doktrinen aus.
- XP-Cap, Offizierskorps, Fahrzeug-/Schiff-/Flugzeugdesigns und Spezialkräfte werden nicht unbeabsichtigt entwertet.
- Falls +4,50 nach 1939 dauerhaft zu viel Überschusserfahrung erzeugt, Bonus nach vollständigen Doktrinen oder über eine klar kommunizierte 1939-Regel auslaufen lassen. Die gewünschte frühe Doktringeschwindigkeit bleibt erhalten.

### P0.5 Fokusbaumdarstellung live abnehmen

Der aktuelle statische Layouttest meldet keine Kollision in Russland und in allen anderen AOE-Bäumen außer sechs bewusst überlagerten/bedingt sichtbaren Deutschland-Kandidaten. Er meldet aber weiterhin 16 lange Russland-Verbindungen und acht lange Deutschland-Verbindungen. Der Test kann Sichtbarkeitsbedingungen, Zoom, Textbreite und tatsächliche Linienführung nicht simulieren.

Pflichtscreenshots bei 100 %, 125 % und 150 % UI-Skalierung:

- SOV: imperiale Route, Sowjetroute, Föderation/Eurasien und Denikin getrennt öffnen.
- GER: SPD/KPD, Bundestag/Reichstag, monarchische und autoritäre Routen getrennt öffnen.
- USA, FRA, ITA, JAP, ENG und SPR vollständig herauszoomen und kritische Bereiche hineinzoomen.
- Kein Fokusrahmen darf einen anderen Rahmen überdecken; keine Linie durch Titel oder Icons; keine weit entfernte Linie darf wie eine falsche Voraussetzung wirken.

Deutschland-Prüfkandidaten bei identischen Koordinaten:

- `AOEIW17_GER_quota_tank_standardisation` / `AOEIW30_GER_dstp_budget_right`
- `AOEIW17_GER_artillery_syndicates` / `AOEIW30_GER_kpd`
- `AOEIW17_GER_workers_armoured_corps` / `AOEIW30_GER_kpd_parliamentary_front`
- `AOEIW17_GER_rotterdam_protocol` / `AOEIW30_GER_kpd_red_welfare`
- `AOEIW17_GER_fortress_of_labour` / `AOEIW30_GER_kpd_mandate_delivered`
- `AOEIW30_GER_elections_to_bundestag` / `AOEIW30_GER_elections_to_reichstag`

Diese Positionen nur verändern, wenn beide Fokusse im selben sichtbaren Zustand erscheinen. Bedingt exklusive Varianten dürfen dieselbe Position behalten.

### P0.6 Releaseartefakte erst nach der Abnahme neu bauen

Arbeitsquelle bleibt das Git-Repository. Danach müssen installierte Kopie, `.mod`-Descriptor und ZIP denselben Commit enthalten. ZIP vollständig auf CRC prüfen. Keine ältere AOE-, RT56- oder Kompatibilitätskopie darf im Launcher gleichzeitig aktiv sein.

## P1 — stärkste Finished-Feeling-Probleme

### P1.1 Wiederholte Standardtexte durch länderspezifische Beschreibungen ersetzen

**Bestätigt:** 207 Gruppen enthalten je mindestens vier identische AOE-Beschreibungen; zusammen betreffen sie 3.121 Schlüssel. Die größten Serien werden je 33-mal für Luftwaffe, Marine, Wirtschaft und militärische Standardpfade wiederverwendet. Eine weitere Beschreibung für fortlaufende nationale Programme erscheint 36-mal. Auch vier aufeinanderfolgende politische Ideen eines Landes teilen häufig denselben Satz.

Vorgehen:

- Zuerst alle sichtbaren politischen, diplomatischen, Krisen-, Regimewechsel- und Endgame-Texte individualisieren.
- Danach Armee-, Marine-, Luft- und Wirtschaftsblöcke pro Land mit realen Institutionen, Geografie, Rivalen, Industrieproblemen und imperialen Beziehungen schreiben.
- Eine gemeinsame Mechanik darf ähnlich erklärt werden, aber Setup, Akteur und erwartete Folge müssen landesspezifisch sein.
- Stufenideen erhalten Fortschrittstexte: Ausgangsproblem, konkrete Reform, nächste Hürde und abgeschlossener Zustand.
- Keine Beschreibung soll nur den Fokusnamen wiederholen oder eine abstrakte „nationale Anstrengung“ behaupten.

Akzeptanz: Kein wichtiges Land besitzt mehr als zwei direkt aufeinanderfolgende Fokusse mit austauschbarer Beschreibung. Die großen politischen und Nachkriegspfade haben keine identischen Texte mit anderen Ländern.

### P1.2 Schwache und generische Fokusbelohnungen gezielt ersetzen

Die Heuristik markiert 957 von 4.107 Fokussen, deren direkte Belohnung nur aus politischer Macht, Stabilität, Kriegsunterstützung, Kommandomacht, Erfahrung, Popularität oder Manpower besteht. Das ist ein Prüfhinweis, kein automatischer Defekt.

Jeder markierte Fokus wird nach Funktion geprüft:

- Setup-Fokus: Flag, Variable, Idee, Ereignis oder Entscheidung muss den späteren Pfad vorbereiten.
- Diplomatiefokus: Zielstaat reagiert über Event, Meinung, KI-Strategie, Garantie, Pakt, Fraktion oder Gegenentscheidung.
- Wirtschaftsprojekt: konkreter Staat, Bauplatz, Ressourcen-, Produktions- oder Infrastrukturfolge.
- Militärreform: Idee, Doktrinentscheidung, Berater, Einheit, Designbonus oder Organisationsfolge.
- Regimewechsel: Charaktere, Parteiname, Kabinett, Gesetze, Balance of Power und ausländische Reaktionen.
- Endknoten: dauerhafte Identität, neue Mechanik oder postwar payoff; nicht nur +100 politische Macht.

### P1.3 Fokusdauer und Kampagnenpacing neu messen

932 Fokusse haben `cost = 7`, also üblicherweise 70 Tage. Der Gesamtanteil von 22,7 % ist nicht allein problematisch, aber die Verteilung ist ungleich. Die Welt-/Untertanenbäume liegen bei 56,4 %, kleinere Standardbäume meist bei 22–27 %, während neuere Großmachtpfade oft unter 11 % liegen.

Zielkorridor:

- 21–35 Tage: Krisenentscheidungen, Verhandlungen, Reaktionen, unmittelbare Kriegsmaßnahmen.
- 35–56 Tage: normale politische und wirtschaftliche Entwicklung.
- 70 Tage: institutionelle Großreform, industrielle Großprojekte, Doktrinwende oder Endgame-Schritt.
- Keine Route soll 1936–1939 überwiegend aus sieben aufeinanderfolgenden 70-Tage-Fokussen bestehen.
- Fokusdauer gegen Entscheidungsaktivität messen: während langer Fokusse muss der Spieler etwas Sinnvolles tun können.

### P1.4 `AOEIW_world_expansion_focus.txt` als eigene Qualitätsschuld behandeln

Dieser Block umfasst 473 Fokusse in vielen kompakten Länderbäumen. Davon dauern 267 70 Tage; 247 haben nur einfache Zahlenbelohnungen. Die Datei besitzt 84 Endknoten. Sie ist damit der größte sichtbare Ursprung für „Land hat einen Baum, aber keine Identität“.

Betroffene Konzept-IDs und tatsächliche Tags müssen erhalten bleiben:

- BTF→EST, CAF→GEO, TRK→KAZ, HEJ→OMA, INA→VIN, FWA→MLI, GEA→MAL, NEE→QUE, TCO→CSA, FAM→HAI.

Verbesserung:

- Pro spielbarem Welt-/Untertanenbaum eine einzigartige Kernmechanik oder Krise.
- Je ein Loyalitäts-, Autonomie- und Unabhängigkeitsendpunkt, sofern mit dem Setting vereinbar.
- Mindestens eine echte Reaktion des Oberherrn und eines regionalen Nachbarn.
- Zwei bis vier austauschbare Militär-/Industriefokusse durch Entscheidungen oder Ideenprogression ersetzen.
- Endknoten an die späteren `AOEIW37/38`-Systeme anschließen.

### P1.5 KI-Gewichte der chinesischen United Front ergänzen

**Bestätigter Prüfkandidat:** Alle 34 Fokusse in `common/national_focus/AOEIW_phase20_united_front_focus.txt` besitzen kein eigenes `ai_will_do`; zusätzlich fehlt es bei `AOEIW9_AUS_mil_army_10`. Defaultgewicht kann technisch funktionieren, bildet aber keine Strategie für Chiang, Mao, dauerhaften Rat, Küstenverteidigung und Wiederaufbau.

Erforderlich:

- Historische und alternative KI-Pläne für die drei Führungsentscheidungen.
- Kriegszustand, Frontlage, Industrie, Unterstützung und MAN/JAP-Status berücksichtigen.
- KI darf nach Sieg nicht in wartime-only Fokussen hängen bleiben.
- `CHI` bleibt der Spieler-/United-Front-Tag; `MAN` behält Puyi. Keine Tagwechsel als Abkürzung.

### P1.6 Länderereignisse aus der 15er-Schablone herauslösen

29 Dateien `events/AOEIW_<TAG>_events.txt` enthalten jeweils exakt 15 Ereignisse. Viele benutzen ähnliche Variablen, Bilder und PP/Stabilitätsbelohnungen. Die Struktur ist funktionsfähig, aber für Spieler wiedererkennbar.

Pro Land mindestens drei Ankerereignisse umarbeiten:

1. Auftaktkrise mit konkreten innenpolitischen Gruppen.
2. Reaktion eines tatsächlich betroffenen Nachbarn/Oberherrn/Untertanen.
3. Spätes Ergebnis, das frühere Entscheidungen auswertet.

Optionen müssen unterschiedliche Folgekosten haben, in späteren Texten wieder aufgegriffen werden und der KI verständliche Gewichte geben.

### P1.7 Icons semantisch und visuell abnehmen

Der technische Spritevalidator ist sauber und direkt benachbarte Eltern/Kinder benutzen nun null identische Icons. Trotzdem wurden 4.107 Iconzuweisungen mit nur 364 verschiedenen Bildern gefunden. Häufig sind `GFX_goal_generic_army_doctrines` (197), `GFX_focus_generic_railroad` (134), `GFX_focus_generic_military_industry` (120) und `GFX_focus_generic_election` (100).

Verbesserung:

- Einzigartige Bilder für Pfadwurzeln, Staatskrisen, Regimewechsel, Bündnisgründungen, große Friedensschlüsse und Endgame.
- Standardicons nur dort, wo der Inhalt wirklich standardisiert ist.
- Idee, Entscheidung, Eventbild und Fokusicon eines Systems als zusammengehörige visuelle Sprache gestalten.
- DDS-Alphakanal, Fokusrahmenzuschnitt, Shine-Sprite und 100/125/150-%-Skalierung prüfen.
- Keine neuen Bilder nur zur Erhöhung der Zahl; zentrale Identität priorisieren.

### P1.8 Kriege und Eroberungen auf Nachspiel prüfen

Besonders ITA, JAP, TUR, GRE, ROM, YUG, ETH, SOV und USA benötigen vollständige Liveketten:

- Kriegsgrund → Krieg → Sieg/Niederlage → Frieden/Besatzung → Integration/Freilassung → Wiederaufbau → Diplomatiereaktion.
- Keine Entscheidung darf nach einem Friedensvertrag auf einen nicht mehr existierenden Controller warten.
- Claims und Cores müssen die RT56-State-IDs aus `RT56_STATE_MERGE.csv` verwenden.
- Kapitulation, Exilregierung, Bürgerkrieg und Fraktionswechsel als alternative Zustände testen.
- Friedensinhalt darf nicht nur durch `has_war = no` erscheinen, wenn das konkrete Ziel gar nicht erreicht wurde.

### P1.9 Untertanen- und Imperiumsbeziehungen bilateral prüfen

Pflichtpaare:

- SOV–UKR/GEO/KAZ
- FRA–MLI/VIN
- GER–EST/MAL und deutscher Einfluss auf POL
- SPR–ARG/PRU
- POR–BRA
- ENG–RAJ/CAN sowie britische Thronfolge
- CHI–MAN im besonderen stabilen Tagmodell

Jede Beziehung benötigt sichtbare Pflichten, Investitionen, Kriegsdienst, Petitionen, Reaktionen auf den Sturz des Oberherrn, Nachkriegsstatut und KI-Verhalten. Mehrere Untertanen dürfen dem Oberherrn keine unendlich stapelbaren identischen Geister geben.

### P1.10 Fokus-Selektoren und DLC-Kombinationen testen

Viele Länder besitzen AOE- und geerbte RT56-/DLC-Bäume. Hohe AOE-Gewichte sind vorhanden, beweisen aber nicht jeden Startzustand. Für alle 49 Startbesitzer prüfen:

- AOE-Baum gewinnt mit allen DLCs.
- AOE-Baum gewinnt mit minimal unterstützter DLC-Kombination.
- Kein Land erhält gleichzeitig zwei sichtbare Bäume oder einen leeren Baum.
- Bürgerkrieg, Freilassung und Tagwiederherstellung wählen den vorgesehenen Baum.
- ADR/LIE/MNC/SAN sind bewusste Mikrostaatausnahmen, keine versehentlich vergessenen Selektoren.

## Fokusbaum-Messwerte pro Datei

`Schwach` bedeutet nur einfache direkte Zahlenbelohnung nach der oben beschriebenen Heuristik. `Event` und `Diplo` zählen Fokusse mit entsprechenden direkten Effekten; verschachtelte Scripted Effects können weitere Folgen enthalten. Werte sind Priorisierungshilfen.

| Baum | Fokusse | 70 Tage | Schwach | Event | Diplo | Krieg/Nachspiel | Endknoten | Fehlende AI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AUS | 91 | 22,0 % | 14 | 3 | 8 | 1 | 4 | 1 |
| BEL | 74 | 25,7 % | 9 | 1 | 6 | 1 | 3 | 0 |
| BRA | 87 | 24,1 % | 20 | 1 | 3 | 1 | 2 | 0 |
| BUL | 74 | 21,6 % | 10 | 0 | 8 | 0 | 3 | 0 |
| CAN | 87 | 24,1 % | 22 | 1 | 2 | 2 | 2 | 0 |
| CHI | 106 | 8,5 % | 21 | 8 | 8 | 2 | 9 | 0 |
| DEN | 74 | 25,7 % | 15 | 0 | 2 | 2 | 3 | 0 |
| EGY | 77 | 26,0 % | 17 | 1 | 2 | 2 | 2 | 0 |
| ENG | 115 | 7,8 % | 25 | 5 | 8 | 2 | 8 | 0 |
| ETH | 77 | 23,4 % | 15 | 1 | 2 | 2 | 2 | 0 |
| FIN | 84 | 25,0 % | 21 | 0 | 2 | 2 | 3 | 0 |
| FRA | 182 | 6,6 % | 37 | 11 | 10 | 2 | 22 | 0 |
| MAN Frontier | 24 | 0,0 % | 6 | 2 | 0 | 0 | 2 | 0 |
| MON Frontier | 29 | 3,4 % | 7 | 7 | 0 | 0 | 1 | 0 |
| QIN Frontier | 24 | 0,0 % | 8 | 0 | 0 | 0 | 1 | 0 |
| XIC Frontier | 24 | 0,0 % | 6 | 2 | 0 | 0 | 1 | 0 |
| GER | 328 | 10,7 % | 46 | 40 | 15 | 7 | 30 | 0 |
| GRE | 74 | 21,6 % | 15 | 0 | 2 | 2 | 3 | 0 |
| HOL | 84 | 25,0 % | 14 | 0 | 8 | 1 | 3 | 0 |
| IRE | 74 | 25,7 % | 16 | 0 | 2 | 3 | 3 | 0 |
| ITA | 148 | 20,3 % | 23 | 10 | 13 | 3 | 5 | 0 |
| JAP | 123 | 7,3 % | 27 | 5 | 8 | 1 | 9 | 0 |
| MEX | 87 | 24,1 % | 21 | 1 | 2 | 2 | 2 | 0 |
| NOR | 74 | 27,0 % | 16 | 0 | 2 | 2 | 3 | 0 |
| PER | 84 | 25,0 % | 21 | 0 | 2 | 2 | 3 | 0 |
| CHI United Front | 34 | 26,5 % | 13 | 0 | 0 | 0 | 2 | 34 |
| POL | 84 | 25,0 % | 13 | 1 | 9 | 2 | 3 | 0 |
| POR | 84 | 25,0 % | 13 | 0 | 8 | 1 | 3 | 0 |
| RAJ | 95 | 8,4 % | 27 | 0 | 2 | 2 | 8 | 0 |
| ROM | 84 | 25,0 % | 15 | 0 | 9 | 1 | 3 | 0 |
| SIA | 74 | 25,7 % | 16 | 0 | 2 | 2 | 3 | 0 |
| SOV | 224 | 19,2 % | 36 | 11 | 11 | 2 | 22 | 0 |
| SPR | 104 | 22,1 % | 16 | 9 | 9 | 2 | 5 | 0 |
| SWE | 84 | 25,0 % | 21 | 0 | 2 | 2 | 3 | 0 |
| SWI | 82 | 9,8 % | 18 | 0 | 2 | 2 | 9 | 0 |
| TUR | 95 | 8,4 % | 28 | 0 | 2 | 2 | 8 | 0 |
| USA | 201 | 21,9 % | 27 | 13 | 9 | 5 | 13 | 0 |
| Welt-/Untertanenbäume | 473 | 56,4 % | 247 | 5 | 0 | 6 | 84 | 0 |
| YUG | 84 | 25,0 % | 15 | 0 | 9 | 0 | 3 | 0 |
| **Gesamt** | **4.107** | **932** | **957** |  |  |  | **298** | **35** |

## Länderweiser finaler Qualitätsplan

### Tier 1 — weltprägende Länder

- **AUS – Österreich:** Kronländer und Nationalitäten sind die Kernidentität. Alle politischen Lösungen müssen die Nationalitätenvariablen bis 1942 auswerten. Loyalität, Föderalisierung, Repression und militärische Zentralisierung brauchen unterschiedliche Außenreaktionen. `AOEIW9_AUS_mil_army_10` erhält ein bewusstes KI-Gewicht. Endgame gegen GER, SOV, Balkan und Italien testen.
- **CHI – China:** United-Front-Selektor, MAN/Puyi-Kontinuität und Nachkrieg sind releasekritisch. Chiang-, Mao- und Ratsausgang brauchen eigene KI-Pläne, Regierungsbilder, Wiederaufbau und ausländische Reaktionen. Sieg über Japan darf nicht in einer dauerhaften Kriegsregierung enden.
- **ENG – Großbritannien:** Thronfolge, Parlament und imperialer Bund müssen Kanada, Indien und weitere Dominions wirklich verändern. Kolonialverlust, Exil, Heimkehr und ein gewonnener Weltkrieg benötigen verschiedene Nachkriegsordnungen. Victoria/George bleiben bewusste Lore.
- **FRA – Frankreich:** Napoleonisches Imperium, demokratische/kommunistische Alternativen und Kolonialapparat benötigen deutlich unterscheidbare Endspiele. MLI/VIN müssen Krieg, Kapitulation und Wiederaufbau bilateral erleben. 22 Endknoten prüfen, ob einige bloß parallele Sackgassen sind.
- **GER – Deutschland:** Der umfangreichste Baum trägt Wahlkampf, Parlament, Koalitionen, Monarchie, Revolution, Wirtschaft und vier kontinentale Ordnungen. Sechs bedingte Koordinatenüberlagerungen und die Übergänge von Wahlsitzen zu Kabinett/Endgame live prüfen. Jeder europäische Ordnungsweg braucht andere Untertanen-, Handels-, Militär- und Nachkriegsfolgen.
- **ITA – Italien:** Kommunistische, monarchische, korporative und mediterrane Wege besitzen Identität. Eroberungen im Mittelmeer brauchen Besatzung, Marinebasen, Untertanen und Friedensverwaltung. Die langen Verbindungen um La Spezia und „Two Italies“ visuell prüfen.
- **JAP – Japan:** Armee/Marine/Hof-Rivalität soll Industrie, China, MAN und Pazifikstrategie dauerhaft verändern. Sieg oder Niederlage in China, Ressourcenraum, Inselverwaltung und spätes Friedenssystem durchspielen. Direkte Krieg/Nachspiel-Dichte im Baum ist niedrig; Scripted-Effect-Folgen belegen.
- **SOV – Russland:** Imperium, Sowjets, Föderation, Eurasien und Denikin müssen getrennte, lesbare 1940er Ziele besitzen. 16 lange Linien im aktuellen Layout live kontrollieren. UKR/GEO/KAZ, Europa/Asien-Ausrichtung, Bürgerkrieg und postimperiale Ordnung sind Pflichtpfade.
- **SPR – Spanien:** Cádiz-Kongress, ARG/PRU, Zentralamerika/Karibik, Vizekönigtum und Commonwealth brauchen sichtbare Folgejahre. Untertanenentscheidungen von beiden Seiten testen; elf neue Fokusse vollständig deutsch lokalisieren. Imperialer Krieg darf nicht nur mit Gebietskernen enden.
- **TUR – Osmanisches Reich:** Das überlebende Reich darf nicht wie ein umbenannter Türkei-Baum wirken. Millets, Arabien, Balkan, Kaukasus, Meerengen und Provinzverwaltung als fortlaufende Probleme nutzen. Grenzwiederherstellung braucht Friedens-, Autonomie- und Verwaltungsinhalt.
- **USA – Vereinigte Staaten:** Der Start ist absichtlich wiedervereinigt. Alte Breakaway-Reclamation muss unsichtbar bleiben, sofern QUE/CSA/HAI nicht existieren. Präsidentschaft, Wirtschaftsordnung, alternative Amerikas und Nachkriegsrolle bis 1942 testen. 13 Endknoten und lange Restaurationslinien auf Sackgassen prüfen.

### Tier 2 — Regionalmächte

- **BEL – Belgien:** Handels-, Kongo-/Imperial- und Sicherheitspolitik stärker verzahnen; deutsche, französische und niederländische Reaktionen. Ein Event im direkten Fokusfluss ist zu wenig als alleinige Identitätsstütze.
- **BUL – Bulgarien:** Balkanrevision, Hof, Armee und Nachbarschaft müssen nach territorialem Erfolg in Verwaltung und Diplomatie münden. Direkter Baum enthält keinen erkannten Event- oder Krieg/Nachspiel-Anker; verschachtelte Folgen prüfen.
- **CAN – Kanada:** Britische Bindung gegen eigenständige Zwei-Ozean-Politik ausspielen. Kriegsbeitrag, Wehrpflicht, Industrie und Friedensdividende mit ENG-Reaktion verbinden; drei neue Fokusse deutsch lokalisieren.
- **EGY – Ägypten:** Kanal, Nil, Sudan, britische und osmanische Ansprüche als wiederkehrendes System. Kontrolle des Kanals muss Handel, Diplomatie und Krieg verändern; drei neue Fokusse deutsch lokalisieren.
- **FIN – Finnland:** Russlandfrage, Neutralität, Nordische Kooperation und Grenzkrieg benötigen unterschiedliche Friedensausgänge. Wirtschaftlicher Wiederaufbau nach Gebietserwerb/-verlust ergänzen, falls im Livepfad nicht vorhanden.
- **GRE – Griechenland:** Megali-/Balkanambitionen brauchen Besatzungs- und Minderheitenpolitik. Marine, Handel und Rivalität mit TUR/ITA in späteren Entscheidungen fortführen.
- **HOL – Niederlande:** Handel und Kolonien sind die Identität. Überseeverlust, Exilregierung, Rückkehr und Indonesien-/MAL-Umfeld als zusammenhängenden Bogen prüfen. Neue europäische Restaurationsentscheidung soll nicht generisch wirken.
- **MEX – Mexiko:** Öl, Arbeiter, USA und hemisphärische Unabhängigkeit bilden den einzigartigen Kern. Späte Raffinerie-/Arbeiterroute mit Reaktionen und längerem Wirtschaftsmechanismus verbinden; drei neue Fokusse deutsch lokalisieren.
- **PER – Persien:** Druck von SOV, ENG, TUR und RAJ soll Alignment, Öl und militärische Beschaffung verändern. Späte Wahl darf nicht bei einem Meinungsmodifikator enden.
- **POR – Portugal:** BRA ist strategisch zu groß für reine Untertanendekoration. Kriegspflicht, Zusammenbruch, Memorandum, Wiederaufbau und Charter auf beiden Seiten testen. Kolonial-/Seewegpolitik mit dem Brasilienpfad verbinden.
- **RAJ – Indien:** Britische Beziehung, Kriegsdienst und Verfassungsfrage brauchen einen nachvollziehbaren Autonomiebogen. Unabhängigkeit und Loyalität dürfen nicht dieselben Industrie-/Militärbelohnungen besitzen.
- **ROM – Rumänien:** Öl, Krone, Grenzrevision und Großmachtdruck bis zum Friedensschluss führen. Späte Gebietsgewinne benötigen Kern-, Besatzungs- oder Minderheitenentscheidungen.
- **SWE – Schweden:** Neutralität, Rüstungsexport und nordische Führung sollen auf regionale Kriege reagieren. Nach 1940 eine erkennbare nordische Sicherheits- oder Wirtschaftsordnung schaffen.
- **SWI – Schweiz:** Verteidigung, Kantone, Finanzen und Neutralität brauchen diplomatische Kosten. Neun Endknoten prüfen: Alternativen dürfen kompakt sein, aber nicht wie abgebrochene Zweige wirken.

### Tier 3 — Sekundärstaaten

- **DEN – Dänemark:** Nordische Sicherheit, Meerengen und Kolonial-/Inselpolitik durch einzigartige Ereignisse stärken. Besetzung, Exil und Befreiung als kompletter Zyklus.
- **ETH – Äthiopien:** Überleben ist nur der erste Akt. Wiederaufbau, Hochlandkorridore, Rotes Meer, Eritrea/Somaliland und EGY/ITA-Reaktionen bilden das Endspiel; drei neue Fokusse deutsch lokalisieren.
- **IRE – Irland:** Neutralität, britische Beziehung und Wiedervereinigung brauchen längerfristige Folgen. Kriegseintritt oder Neutralität sollen Wirtschaft, Häfen und innenpolitische Lager verändern.
- **MON – Mongolei:** Frontier Council, östliche Solidarität, Neutralität und Steppe Compact sind neu vorhanden. Fünf neue Fokusse plus zugehörige Events/Entscheidungen deutsch lokalisieren; SOV/CHI/MAN/JAP-Reaktionen und AI-Pacing testen.
- **NOR – Norwegen:** Handel, Marine, Neutralität, Besetzung/Exil und Rückkehr stärker verknüpfen. Mit 27 % den höchsten 70-Tage-Anteil eines normalen Länderbaums auf Pacing prüfen.
- **SIA – Siam:** Zwischen JAP, CHI und Kolonialmächten muss jede außenpolitische Wahl erkennbare Gegenreaktionen auslösen. Territoriale Ergebnisse in Indochina/Malaya verwalten.
- **YUG – Serbien/Jugoslawien:** innere Nationalitäten und Balkanansprüche brauchen Föderalisierungs-, Repressions- und Besatzungsfolgen. Direkter Baum zeigt keinen erkannten Krieg/Nachspiel-Anker; tatsächliche Scripted Effects prüfen.

### Tier 4 — Untertanen, Frontier-Staaten und Mikrostaaten

- **ADR – Andorra:** geerbter Acht-Fokus-Baum. Entweder klar als kompakte Mikrostaat-Challenge kennzeichnen oder drei bis fünf Entscheidungen für Schmuggel, Neutralität und Schutzmacht ergänzen.
- **ARG – Argentinien:** spanischer Southern-Cone-Verwalter mit kompaktem Weltbaum. Loyalität, Autonomie, Kriegspflicht und Cádiz-Ausgang von ARG-Seite testen; eigener regionaler Anspruch darf nicht der spanischen Verwaltung widersprechen.
- **BRA – Brasilien:** großer eigener Baum und portugiesischer Untertan. Die neue Amazon-/Atlantik-Serie, POR-Kriegskette und regionale Diplomatie zu einer einzigen langfristigen Beziehung verbinden; drei neue Fokusse deutsch lokalisieren.
- **EST – Estland:** deutscher Untertan mit kompaktem Weltbaum. Deutsches Endgame muss aus EST-Sicht Autonomie, Sicherheit oder Integration sichtbar verändern.
- **GEO – Georgien:** russischer Untertan. Kriegsdienst, Zusammenbruch und Charter müssen nach SOV-Pfad variieren; Kaukasusnachbarn reagieren lassen.
- **KAZ – Kasachstan:** russischer Untertan. Steppe, Ressourcen und Grenzsicherheit als Identität; imperiale Zentralisierung und Föderation dürfen nicht dieselbe Endlage erzeugen.
- **LIE – Liechtenstein:** großer geerbter Baumkandidat, aber keine AOE-Schicht. Lore, Herrscher, Diplomatie und Selektor unter dem AOE-Szenario prüfen; keine pauschale Neuentwicklung ohne sichtbaren Bruch.
- **MAL – Malaysia:** deutscher Untertan mit kompaktem Weltbaum. Rohstoffe, Seewege, JAP und GER müssen im deutschen Ordnungsweg reagieren.
- **MAN – Puyis Qing-Staat:** Sonderfall mit kleinem Frontier-Baum, aber zentraler Chinafunktion. MAN darf nie versehentlich landlos werden; Kapitulation, CHI-Sieg, JAP-Niederlage und Nachkriegsstatut gemeinsam testen.
- **MLI – Mali:** französischer Untertan. Kriegsdienst, französischer Zusammenbruch, Notregierung und Charter mit regionaler Eigenidentität verbinden.
- **MNC – Monaco:** kein gezählter AOE-Baum. Bewusste Mini-Erfahrung oder klare Nichtpriorität; mindestens korrekte Regierung, Leader, Ideen und Nachbarschaft sicherstellen.
- **POL – Polen:** in diesem Setting deutscher Untertan trotz 84-Fokus-Baum. Souveräne Expansionsteile dürfen im Untertanenstart nicht widersprüchlich offen sein. Petition, deutsche Reaktion und möglicher Statuswechsel testen.
- **PRU – Peru:** spanischer Andenverwalter. Investitionen, Petitionen, Krieg und Commonwealth/Directorate auf PRU-Seite testen.
- **QIN – Frontier:** 24 Fokusse; Assembly/Command-Exklusivität, CHI/MAN-Anschluss und Endstatus prüfen. Acht schwache Belohnungskandidaten individualisieren.
- **SAN – San Marino:** kein gezählter AOE-Baum. Wie Monaco bewusst kompakt gestalten oder wenigstens einen klaren Überlebens-/Schutzmachtpfad bieten.
- **UKR – Ukraine:** russischer Untertan. Kriegsdienst-zu-Charter-Bogen, SOV-Regimewechsel und mögliche Unabhängigkeit konsequent auswerten.
- **VIN – Vietnam:** französischer Untertan. Französischer Zusammenbruch, JAP-Druck und Wiederaufbau müssen unterschiedliche politische Ergebnisse liefern.
- **XIC – Frontier:** 24 Fokusse; Officers/Civic-Exklusivität, regionale Ressourcen und Anschluss an die chinesische Nachkriegsordnung prüfen.
- **YEM – Jemen:** kompakter Weltbaum plus neue Meerengenserie. Fünf neue Fokusse deutsch lokalisieren; Bab el-Mandeb, offener Hafen/Küstenwache, EGY/ETH/TUR/ENG-Reaktionen und Nachkrieg ausspielen.

## P2 — systemweite Kampagnen- und Balanceprüfung

### Ereignisse

- Jede Option hat sichtbare, unterschiedliche Kosten/Folgen und sinnvolle KI-Gewichte.
- Delayed Events bewahren ROOT/FROM/PREV und gespeicherte Event Targets.
- Ereignisse feuern nur einmal, wenn ihr Inhalt einmalig ist; wiederholbare Ereignisse skalieren kontrolliert.
- Nachrichtenereignisse erscheinen nur bei weltpolitischer Relevanz.
- Gegenstaaten erhalten Reaktionen statt stiller Grenz-, Fraktions- oder Regierungsänderungen.
- Eventbilder passen zu Land, Epoche und Akteuren; Schlüsselereignisse erhalten eigene Bilder.
- Abgebrochene Folgereferenzen und Ereignisse ohne erreichbaren Caller durch Laufzeittelemetrie finden.

### Entscheidungen

- Kategorien erscheinen erst bei relevantem Inhalt und verschwinden wieder.
- `visible`, `available`, `complete_effect`, `remove_effect`, `days_remove` und `fire_only_once` gegeneinander testen.
- Kosten sind bei +4,50 täglicher Erfahrung und hoher PP-Vergabe weiterhin relevant.
- Keine Entscheidungsmission bleibt nach Tod/Annexion des Zielstaats dauerhaft hängen.
- Cooldowns, Flags und Ideen verhindern Spam und unendliche Stapelung.
- Tooltips nennen Zielstaat, Gebiete, Autonomieänderung, Kriegsfolge und Ablaufzeit.

### Nationale Geister, dynamische Modifier und Balance of Power

- Jede frühe Problemidee besitzt einen erreichbaren Verbesserungs- oder Entfernungspfad.
- Stufenideen werden sauber ausgetauscht; alte Stufe bleibt nicht zusätzlich aktiv.
- Regierungs-/Koalitionsideen verschwinden beim Regierungswechsel.
- Dynamische Modifier akkumulieren nur vorgesehene Werte und werden nach Save/Load korrekt rekonstruiert.
- Balance-of-Power-Seiten, Ranges und Decisions sind in jeder Ideologie erreichbar und können nicht softlocken.
- Dauerhafte Endgameideen unterschiedlicher Länder auf Produktions-, Forschung-, Manpower- und Kampfstärke vergleichen.

### Diplomatie, Fraktionen und KI

- Historische KI erzeugt eine plausible AOE-Welt; alternative KI erzeugt echte Divergenz bis 1940–42.
- Bündnisgründung verändert Strategie gegenüber Mitgliedern, Rivalen und Schutzstaaten.
- KI schützt Untertanen, reagiert auf Memoranden und nutzt Nachkriegsentscheidungen.
- Fraktionswechsel entfernt widersprüchliche Garantien, Kriegsteilnahmen und Strategien.
- Nichtangriffspakte, Garantien und Meinungswerte dürfen Kriegspfade nicht ungewollt blockieren.
- Jede große alternative Regierung erhält eigene `ai_strategy_plan`-Bedingungen und Abbruchbedingungen.

### Wirtschaft und Militär

- Fabrik-, Slot-, Infrastruktur- und Ressourcenbelohnungen gegen Ausgangswirtschaft skalieren; Kleinstaaten nicht durch flache Großmachtwerte übermächtig machen.
- Bauplätze nur in tatsächlich besessenen/kontrollierten Staaten vergeben; Küstenbauten brauchen Küstenfilter.
- Forschungsboni dürfen nicht auf bereits obsolette Technologien zielen.
- OOBs, Templates und Varianten mit/ohne BBA prüfen; keine Geisterflügel oder ungültigen Module.
- Flottenpfade für Binnenländer vermeiden oder bewusst an Küstengewinn koppeln.
- Mobilisierung und Rekrutierung gegen Bevölkerung und Industrie jedes Landes prüfen.

### Karte und Geschichte

- `RT56_STATE_MERGE.csv` bleibt verbindlich: 1.143 Zeilen, 116 Cross-ID-Zuordnungen.
- Keine alte AOE-State-ID direkt übernehmen, ohne Ledger und aktuelle Staatsdatei zu prüfen.
- Eigentümer, Controller, Cores, Victory Points, Ressourcen, Supply Hubs, Häfen und Railways im Spiel kontrollieren.
- Inseln, Enklaven, Meerengen und neue Subjektgrenzen auf Versorgung und Frontzugänglichkeit prüfen.
- `replace_path` für `history/states` und `map/strategicregions` verlangt vollständige Abdeckung bei jedem Update.

### Lokalisierung und Redaktion

- Nach Übersetzungsabschluss alle Roh-IDs per deutscher und englischer UI-Suche prüfen.
- Staatsnamen, Imperiumsbezeichnungen, Fraktionsnamen und Ideologiebegriffe vereinheitlichen.
- „Russia/Russian Empire/SOV“, „Britain/United Kingdom/Empire“ und spanische Untertanentitel kontextabhängig konsistent verwenden.
- Apostrophe, Gedankenstriche, Anführungszeichen, Großschreibung und Umlaute vereinheitlichen.
- Tooltips kurz halten; Lorebeschreibungen dürfen länger sein, sollen aber konkrete Akteure nennen.
- Übertriebene, abstrakte oder wiederholte Formulierungen ersetzen, die wie generierter Fülltext wirken.

### UI, Grafik und Audio

- Neues Branding auf 16:9, 16:10 und 4:3/Crop-Verhalten prüfen.
- Hauptmenübuttons dürfen Titel und wichtige Bildbereiche nicht verdecken.
- Fokus-/Ideen-/Entscheidungsicons auf schwarzen Hintergrund, Alpha, falsche Nation und falsche Epoche prüfen.
- Super-Event-GUI auf Pause, Tonlautstärke, Überspringen, Wiederholung und Multiplayer prüfen.
- Audioassets brauchen gültige Kategorien; keine fehlenden Soundreferenzen akzeptieren.
- Parlaments-GUI bei verschiedenen Auflösungen und langen deutschen Texten testen.

### Performance und Stabilität

- Observer-Lauf 1936–1942 mit monatlichem Save und Errorlog-Snapshot.
- Monatliche/wochentliche On-Actions profilieren; keine unnötigen `every_country`/`every_state`-Schleifen.
- Entscheidungen und scripted GUIs dürfen nicht permanent teure globale Trigger auswerten.
- Eventflut, Savegröße und Tag-Lag nach großen Kriegen beobachten.
- Wiederholte Wiederaufbau-/Petitionssysteme auf exponentielle Eventketten prüfen.

## P3 — optionale Veredelung

- Eigene Fokusicons für 30–50 wichtigste Staatsentscheidungen und Endgameziele.
- Eigene Eventbilder für Thronfolgen, Revolutionen, Cádiz, deutsche Wahlen, chinesische Einigung und imperiale Nachkriegskonferenzen.
- Länderabhängige Starttooltips: strategische Lage, Hauptmechanik, erste Krise und empfohlene Schwierigkeit.
- Journal-/Chronikentscheidung, die wichtige frühere Beschlüsse und ihre Folgen zusammenfasst.
- Mehr gewichtete Flavor-Events in Friedenszeiten, ohne PP-Klickspam.
- Endscreen/News-Events für klar erreichte AOE-Weltordnungen.
- Optionale Regeln für Doktringeschwindigkeit und Mikrostaaten, falls Spieler unterschiedliche Balance wünschen.
- Achievements/Challenges als Modziele, sofern ohne Ironman-Versprechen.
- Modversion und Changelog sichtbar im Hauptmenü oder Bookmark.
- Übersetzer-, Autoren- und Asset-Credits aktualisieren; vorhandene `Credits.txt` und `Unique Commanders IDS.txt` bewahren.

## Konventionen, die nicht gebrochen werden dürfen

- `SOV` bleibt das Tag des alternativen Russlands.
- `CHI` bleibt Spieler-/United-Front-Tag; `MAN` trägt Puyi/Qing.
- Die imperiale 1936-Welt, langlebige Monarchen und vorhandenen ideologischen Alternativen bleiben Lore.
- Der bereits wiedervereinigte USA-Start bleibt Standard.
- Der geerbte 1939-Bookmark bleibt aus Menükompatibilitätsgründen vorhanden, ist aber nicht unterstützt.
- `AOEIW`, Phasennummern, Fokus-/Event-/Ideen-/Entscheidungs-IDs, Variablen, Flags, Targets und kosmetische Tags nicht kosmetisch umbenennen.
- Selektorgewichte, `allow_branch`, Exklusivität und Layoutdirty-Hooks nur mit belegtem Grund ändern.
- Konzept-IDs der Weltbäume und ihre wiederverwendeten echten Tags nicht gleichsetzen.
- State-ID-Änderungen ausschließlich mit `RT56_STATE_MERGE.csv`.
- Funktionierende RT56-/DLC-Systeme nicht neu schreiben, nur weil eine andere Architektur schöner wäre.

## Empfohlene Reihenfolge des finalen Patches

1. Aktuellen HEAD in Time of Upheaval starten und Rohlog sichern.
2. Alle 1.136 fehlenden deutschen AOE-Schlüssel ergänzen und redaktionell prüfen.
3. SOV-/GER-/Major-Fokusbäume live fotografieren und nur bestätigte visuelle Fehler korrigieren.
4. Kartenmodus und +4,50 Erfahrung mit Save/Load und neu entstehenden Ländern testen.
5. Chinese United Front AI-Gewichte ergänzen und CHI/MAN-Kampagne testen.
6. Welt-/Untertanenbäume: 70-Tage-Ketten, 247 schwache Rewards und 84 Endknoten priorisiert überarbeiten.
7. Wiederholte Beschreibungen zuerst für Tier 1, dann Tier 2, anschließend Welt-/Untertanenländer ersetzen.
8. GER, SPR/ARG/PRU, CHI/MAN, ENG/RAJ/CAN, SOV-Untertanen und ein imperialer Nachkriegsbogen vollständig bis 1942 spielen.
9. Regionale Kriegs-/Friedenspfade für ITA/JAP/TUR/GRE/ROM/YUG/ETH prüfen und fehlendes Nachspiel ergänzen.
10. Observer-Lauf, Performance, Save/Load, UI-Skalierung, Audio und finalen Raw-Log-Gate durchführen.
11. Validator ausführen, installierte Kopie synchronisieren, ZIP mit CRC prüfen und Git-Commit/Changelog festhalten.

## Finale Freigabekriterien

Der Mod erhält den finalen Patch erst, wenn alle folgenden Aussagen wahr sind:

- `python tools/validate_aoeiw.py` meldet PASS.
- Ein frischer 1936-Start des aktuellen HEAD erzeugt keine AOE-Enginefehler.
- Englisch und Deutsch zeigen keine AOE-Rohschlüssel in den unterstützten Hauptpfaden.
- SOV und GER besitzen keine gleichzeitig sichtbaren Fokusüberlappungen oder irreführenden Fernlinien.
- Kartenmodus Ein/Aus und +4,50 Erfahrung funktionieren über Save/Load und neue Länder.
- Jeder Tier-1-Pfad hat Setup, Entwicklung, Hauptentscheidung, Konsequenz, Nachspiel und Endgame.
- Jeder wichtige Krieg besitzt eine erreichbare Friedens-/Besatzungs-/Wiederaufbaufolge.
- Die zentralen Untertanenbeziehungen funktionieren bilateral.
- Historische und alternative KI schließen zentrale Pfade ab und benutzen die neuen Systeme.
- Kein frühes Problem-Nationalspirit bleibt ohne erreichbare Lösung.
- Kein Schlüsselpfad besteht überwiegend aus austauschbaren 70-Tage-Fokussen mit kleinen Zahlenbelohnungen.
- Hauptmenü, Fokusbäume, Events, Entscheidungen, Parlament und Super-Events sind visuell sauber.
- Observer 1936–1942, manueller Save/Load und mindestens die festgelegten Flaggschiff-Kampagnen bestehen.
- Installierte Mod, Descriptor, Release-ZIP und Git-Commit sind identisch dokumentiert.

## Reproduzierbare Auditquellen

- `tools/validate_aoeiw.py` – bestätigte Struktur-, Referenz-, Lokalisierungs-, Sprite-, Karten- und Szenarioverträge.
- `HANDOFF.md` – Architektur, Lore, vorhandene Systeme, frühere Reparaturen und Pfadkonventionen.
- `FINISHED_FEEL_FIX_LIST.md` – bereits umgesetzter Layout-/Icon-/QoL-Pass.
- Workspace `work/release_inventory.py` und `work/audit-results/release_inventory.json` – Fokus-, Pacing-, Reward-, AI- und Lokalisierungsstatistik.
- Workspace `work/world-release-audit.md` und `work/country-coverage.json` – 49-Länder-Abdeckung und Tierbewertung.
- Workspace `work/layout_check.py` und `work/icon_adjacency_check.py` – statische Koordinaten- und Nachbariconprüfung.


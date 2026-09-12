# Age of Empires — Finished-Feel-Fixliste

Stand: 12. September 2026. Diese Liste ist die Freigabeplanung vor weiteren Gameplay-Änderungen. Sie trennt bestätigte sichtbare Fehler von Prüfkandidaten. Bestehende Lore, funktionierende Systeme, Fokus-IDs, Event-IDs, Flags, Variablen und Pfadlogik bleiben erhalten, solange ein konkreter Defekt keine eng begrenzte Änderung verlangt.

## P0 — bestätigte sichtbare Fehler

### 1. Russischen Fokusbaum neu layouten

Betroffene Datei: `common/national_focus/AOEIW_SOV_focus.txt`.

Die Screenshots und der Koordinatenaudit bestätigen einen 59 Spalten breiten Baum mit 24 außergewöhnlich langen Verbindungen. Die schlimmsten Verbindungen überspannen 30 bis 51 Spalten. Ursache sind später ergänzte russische Pfade, die in dieselbe Koordinatenfläche wie der ältere Politik-, Wirtschafts- und Militärteil gesetzt wurden.

Umsetzung:

- Die vier politischen Einstiege — imperiale Ordnung, Sowjetpfad, Russische Föderation und Denikin — als klaren, kompakten Auswahlbereich anordnen.
- Die eurasische Route sichtbar als eigener politisch-diplomatischer Block führen.
- Wirtschaft, Wissenschaft und Rüstung unter ihrem jeweiligen Einstieg bündeln, damit ihre Linien nicht durch politische Pfade laufen.
- Lange horizontale `prerequisite`-Linien verkürzen; Eltern und Kinder vertikal oder diagonal in unmittelbarer Nähe anordnen.
- Lange gepunktete `mutually_exclusive`-Linien zwischen weit entfernten Wurzeln beseitigen. Zuerst wird geprüft, ob dieselbe Exklusivität über den zentralen Auswahlknoten dargestellt werden kann, ohne die Logik zu verändern.
- Überlappende Fokusrahmen, abgeschnittene Namen und Linien durch Fokusfelder entfernen.
- Endknoten jedes Pfads als sichtbaren Abschluss gruppieren, damit keine Route scheinbar im Nichts endet.
- Alle vorhandenen IDs, Belohnungen, Trigger, `allow_branch`-Bedingungen und historischen Wahlmöglichkeiten bewahren.

Besonders auffällige Verbindungen:

- `AOEIW_IMM_SOV_national_destiny` → `AOEIW35_SOV_institutional_settlement`: 51 Spalten.
- `AOEIW_IMM_SOV_root` ↔ `AOEIW22_SOV_denikin_conspiracy`: 47 Spalten.
- `AOEIW9_SOV_politics_root` → `AOEIW22_SOV_denikin_conspiracy`: 40 Spalten.
- `AOEIW_IMM_SOV_root` ↔ `AOEIW22_SOV_russian_republic`: 37 Spalten.
- `AOEIW9_SOV_politics_root` → `AOEIW22_SOV_russian_republic`: 30 Spalten.

### 2. Deutschlands sichtbare Linienprobleme korrigieren

Betroffene Datei: `common/national_focus/AOEIW_GER_focus.txt`.

Der Screenshot mit „Break Prussian Officer Rule“ stammt aus dem deutschen Baum. Der Audit findet sieben Koordinatenkollisionen und 17 lange Verbindungen in dem 61 Spalten breiten Baum.

Umsetzung:

- Den Bereich um `AOEIW9_GER_politics_p3_5` („Break Prussian Officer Rule“) entflechten.
- Politische Hauptpfade und die historische Oppositionsroute räumlich sauber trennen.
- Die 18 Spalten langen gegenseitigen Ausschlüsse und die 11 Spalten lange Root-Verbindung verkürzen.
- Die später ergänzten Wahl-, Koalitions- und Regierungsprogramm-Blöcke an ihre tatsächlichen politischen Eltern ziehen.
- Echte Koordinatenkollisionen einzeln auflösen; bewusst deckungsgleiche alternative Darstellungen nur behalten, wenn sie im Spiel niemals gleichzeitig sichtbar sind.

## P1 — vollständiger Icon-Pass aller AOE-Länder

Der Referenzvalidator findet derzeit keine fehlenden registrierten AOE-Sprites. Das sichtbare Problem ist daher vor allem Auswahl, Wiederholung, Stil, Skalierung und semantische Passung. In 39 AOE-Fokusdateien wurden 4.107 Icon-Zuweisungen mit nur 364 unterschiedlichen Icons gefunden. Besonders oft erscheinen `GFX_goal_generic_army_doctrines` (197-mal), `GFX_focus_generic_railroad` (134-mal), `GFX_focus_generic_military_industry` (120-mal) und `GFX_focus_generic_election` (100-mal).

Der Pass umfasst jedes Land und jeden AOE-Baum:

- Fehlende, schwarze, falsch skalierte, beschnittene oder zur Laufzeit nicht geladene Icons anhand von Spielansicht und Log prüfen.
- Inhaltlich falsche Icons ersetzen: Parlament/Krone für Verfassungsfragen, Fabrik/Ressource für Wirtschaft, Teilstreitkraft für Militär und Flagge/Vertrag für Außenpolitik.
- Direkt benachbarte Wiederholungen beseitigen, besonders wenn dadurch wichtige Entscheidungen wie gewöhnliche Füllfokusse aussehen.
- Den vier bis sechs wichtigsten Pfaden großer Länder eine erkennbare visuelle Sprache geben.
- Vorhandene gute individuelle RT56-, DLC- und AOE-Icons weiterverwenden; neue Grafiken nur für zentrale Identitäts-, Krisen-, Regimewechsel- und Endgame-Fokusse erstellen.
- Jedes neue oder neu zugewiesene Sprite auf Registrierung, DDS-Format, Alphakanal, Fokusrahmen-Zuschnitt und Auflösung prüfen.
- Ideen-, Entscheidungs- und Eventbilder in denselben Pass aufnehmen, wenn sie leer, unpassend oder wiederholt wirken.

Reihenfolge:

1. Russland und Deutschland, weil dort gleichzeitig Layoutfehler sichtbar sind.
2. USA, Frankreich, Italien, Japan, Großbritannien, Spanien und China.
3. Österreich, Türkei, Indien und die regionalen AOE-Länder.
4. Welt-/Subjektbäume in `AOEIW_world_expansion_focus.txt`; identische Koordinaten verschiedener separater Bäume sind dort kein Fehler.

## P1 — weitere Fokusbaum-Strukturkorrekturen

Der Koordinatenaudit markiert Kandidaten; jede Stelle wird vor einer Änderung im Fokusbaum-Kontext geprüft.

- **USA:** 67 Spalten, 27 lange Verbindungen. Besonders die 42-Spalten-Verbindung zum institutionellen Abschluss und mehrere 18–29 Spalten lange Ausschlüsse prüfen.
- **Frankreich:** 58 Spalten, 13 lange Verbindungen. Institutioneller Abschluss sowie alte und neue politische Alternativen kompakter zusammenführen.
- **Italien:** 48 Spalten, 18 lange Verbindungen und zwei mögliche Kollisionen. Kommunistische, imperiale und Wirtschaftsblöcke entflechten.
- **Japan:** 43 Spalten, 13 lange Verbindungen und zwei mögliche Kollisionen. Militärabschluss, Spezialzweig und institutionellen Abschluss neu ausrichten.
- **Großbritannien:** 37 Spalten, 12 lange Verbindungen und zwei mögliche Kollisionen. Armee-, Wirtschafts- und Regierungsabschluss prüfen.
- **Spanien:** Diplomatieeinstieg liegt 19 Spalten vom politischen Abschluss entfernt; die kolonialen Nachkriegs- und Subjektinhalte sichtbar an den Hauptpfad anbinden.
- **Österreich, China, Ägypten, Brasilien, Kanada, Mexiko, Rumänien, Siam und Äthiopien:** einzelne lange Anschlüsse prüfen und nur bei sichtbarer Beeinträchtigung verschieben.
- Fokusnamen mit mehrzeiligem Überlauf, abgeschnittene Beschriftungen und tote Leerflächen in allen geänderten Bäumen mit 100-%-UI-Skalierung kontrollieren.

## P1 — Einstellung für den benutzerdefinierten Kartenmodus

Vorhandenes System:

- Definition: `common/map_modes/zz_AOEIW_imperial_world_map_mode.txt`.
- Button-Grafik: `interface/zz_AOEIW_mapmode.gfx`.
- Lokalisierung: `localisation/english/AOEIW_qol_l_english.yml` und `localisation/german/AOEIW_qol_l_german.yml`.

Umsetzung:

- Eine klar lokalisierte Custom-Game-Rule „Imperial World Map Mode: On/Off“ ergänzen; Standard ist **On**.
- Die Farblogik des Modus über `has_game_rule` steuern.
- Bei **Off** keine AOE-Block-, Ideologie-, Untertanen- oder Kriegsfarben anwenden. Da Scripted Map Modes beim Laden registriert werden, wird im Runtime-Test geprüft, ob der Button selbst bedingt ausgeblendet werden kann. Falls die Engine das nicht unterstützt, bleibt der Button sichtbar und der Tooltip erklärt, dass der AOE-Farbmodus deaktiviert ist.
- Englische und deutsche Regeltexte, Tooltips und Optionsbeschreibungen hinzufügen.
- Regel in Start, Save/Load und Multiplayer-Host-Konfiguration testen.

## P1 — 4,5 passive Doctrine-Erfahrung

Bereits vorhanden ist je eine kostenlose erste Land-, Luft- und Marinedoktrin über `common/scripted_effects/zz_AOEIW_qol_effects.txt` und `common/on_actions/zzzzz_AOEIW_qol_on_actions.txt`.

Umsetzung:

- Allen existierenden Ländern ab Kampagnenstart **+4,50 tägliche Armee-, Marine- und Lufterfahrung** geben, damit die Doktrinen bis 1939 vollständig ausgebaut werden können.
- Dafür die dokumentierten Modifier `experience_gain_army`, `experience_gain_navy` und `experience_gain_air` verwenden.
- Den Bonus als sichtbaren, lokalisierten globalen AOE-Ideeneffekt umsetzen, damit der Spieler die Quelle der Erfahrung versteht.
- Dynamisch entstehende Länder ebenfalls erfassen.
- Bestehende kostenlose Einstiegsdoktrinen beibehalten und die Kombination auf XP-Cap, Ausgabenverhalten der KI und tatsächlichen 1939-Fortschritt testen.
- Im Balancetest entscheiden, ob der +4,50-Bonus nach vollständigem Doktrinausbau oder ab 1939 entfernt werden muss, damit überschüssige Erfahrung spätere Designs nicht unbeabsichtigt dominiert. Die verlangte Aufbaugeschwindigkeit bleibt dabei erhalten.

## Implementierungsstand dieser Serie

Abgeschlossen im Repository:

- Russland neu gruppiert: keine exakte Koordinatenkollision; die bestätigten 30–51-Spalten-Fehlverbindungen sind beseitigt.
- Deutschland entflechtet: der echte imperiale Endknoten-Zusammenstoß ist behoben; bedingt sichtbare Wahl-/Oppositionsvarianten behalten ihre bewusst gemeinsamen Positionen.
- USA, Frankreich, Italien, Japan und Großbritannien: institutionelle Endspielblöcke neu angeordnet; keine bestätigte Koordinatenkollision bleibt.
- Icon-Pass über alle AOE-Fokusdateien: direkt verbundene Eltern und Kinder verwenden keine identischen Icons mehr; zentrale individuelle End- und Regimeicons bleiben erhalten.
- Unnötige Fernlinien aus `mutually_exclusive` entfernt, wenn die bestehende `allow_branch`-Logik dieselbe Pfadsperre bereits vollständig abbildet.
- Custom-Game-Rule für den Imperial-World-Kartenmodus ergänzt; Standard ist Ein, Aus neutralisiert die benutzerdefinierte Farbschicht.
- Sichtbare globale Doktrinentwicklung mit +4,50 täglicher Armee-, Marine- und Lufterfahrung ergänzt, einschließlich monatlicher Absicherung für neu entstehende Länder.
- Statischer Release-Validator: 5.279 Dateien, PASS.

Ausstehend ist die Engine-/Spielansicht-Abnahme nach Installation: Hauptmenü, Regelanzeige, neuer 1936-Start, Fokusbaumdarstellung und Roh-`error.log`.

## P2 — Finished-Feeling-Inhaltsprüfung

Die großen Inhalts- und Regionalpässe sind bereits implementiert. Dieser Abschnitt ist eine gezielte Spielprüfung, keine Erlaubnis für einen pauschalen Neubau.

Für jedes wichtige Land werden komplette Pfade von 1936 bis 1942 geprüft:

- Aufbau → Entwicklung → Hauptentscheidung/Krieg → Konsequenz → Nachspiel → Endgame-Auszahlung.
- Keine Route darf direkt nach Regimewechsel, Bündnisgründung, Sieg oder Imperialreform enden.
- Diplomatische Fokusse müssen bei betroffenen Staaten eine Reaktion, Beziehung, KI-Strategie, Entscheidung oder Folgeereignis auslösen.
- Kriege brauchen erreichbare Friedens-, Besatzungs-, Freilassungs- oder Wiederaufbauinhalte.
- Untertanen brauchen mindestens sichtbare Autonomie-, Investitions-, Integrations- oder Verfassungsschritte, wenn sie Kernbestandteil des Pfads sind.
- Nationale Geister sollen eine erkennbare Entwicklung haben und nicht als dauerhaftes frühes Platzhalterproblem liegen bleiben.
- Wirtschafts- und Militärpfade auf schwache generische Belohnungen, nutzlose Forschungboni und Belohnungen nach bereits erforschter Technik prüfen.
- KI-Pläne müssen zentrale Pfade tatsächlich abschließen und neue Entscheidungen verwenden.

Erste Runtime-Reihenfolge:

1. Russland: Imperium, Sowjets, Föderation, Eurasien und Denikin jeweils bis zum politischen Endzustand.
2. Deutschland: Monarchie/Regierung, Opposition, Wahl/Koalition und Nachkrieg.
3. Spanien: Imperium, ARG/PRU-Untertanen und koloniale Nachkriegsverwaltung.
4. China/Mandschurei/Japan: Krieg, Sieg/Niederlage und Nachkriegsordnung.
5. USA und britische Nachfolge.
6. Je ein europäischer, amerikanisch-afrikanischer und asiatisch-nahöstlicher Regionalpfad.

## P2 — Release-Politur

- Alle Fokusnamen und Beschreibungen der geänderten Bäume auf fehlende Keys, Platzhalter, Wiederholungen und holpriges Englisch/Deutsch prüfen.
- Fokusdauer und Belohnungen entlang eines vollständigen Pfads messen; zu viele 70-Tage-Schritte, Leerlauf und Ausreißer korrigieren.
- Tooltips für irreversible politische Entscheidungen, Gebietsübergaben, Kriegserklärungen und Untertanenstatus ergänzen.
- Ereignisoptionen müssen Folgen ankündigen und die Gegenpartei korrekt benennen.
- Ideologien, Staatsnamen, Fraktionsnamen und Begriffe innerhalb eines Landes einheitlich halten.
- Sichtbare AOE-UI-Elemente bei 100 %, 125 % und 150 % UI-Skalierung prüfen.
- Hauptmenü-Start, neues 1936-Spiel, Speichern/Laden und Beobachterlauf bis 1942 als Release-Gates verwenden.

## Technische Abnahme und Installation

Nach jedem zusammenhängenden Paket:

1. `tools/validate_aoeiw.py` gegen die installierte HOI4-Version ausführen.
2. Neue Fokus- und Eventreferenzen, IDs, Lokalisierung, Sprites und Klammern prüfen.
3. Einen echten Spielstart mit Roh-`error.log` durchführen.
4. Betroffenen Baum im Spiel visuell kontrollieren; statische Koordinatenprüfung allein genügt nicht.
5. Erst nach erfolgreicher Prüfung die Arbeitskopie nach `Documents\Paradox Interactive\Hearts of Iron IV\mod\Age_Of_Empires_RT56_Edition` synchronisieren und das Release-ZIP erneuern.

## Bewusst zu bewahrende Regeln

- `SOV` bleibt das Tag des alternativen Russlands.
- Die imperiale 1936-Welt, langlebige Monarchen und vorhandenen ideologischen Alternativen bleiben Teil des Settings.
- Fokus-, Event-, Ideen-, Entscheidungs-, Flag- und Variablen-IDs werden nicht aus ästhetischen Gründen umbenannt.
- `allow_branch`, Selektorprioritäten und gegenseitige Ausschlüsse werden nur geändert, wenn dieselbe Pfadlogik nachweislich erhalten bleibt.
- Funktionierende Systeme werden nicht umgebaut, nur weil eine andere Struktur möglich wäre.
- Die richtige Standalone-Edition bleibt die einzige aktivierte Age-of-Empires-Mod.

## Empfohlene erste Implementierungsserie

1. Russland-Layout und Russland-Icons gemeinsam korrigieren.
2. Deutschland-Linienproblem und Deutschland-Icons korrigieren.
3. Custom-Game-Rule für den Kartenmodus sowie +4,50 Doctrine-Erfahrung implementieren.
4. USA/Frankreich/Italien/Japan/Großbritannien auf lange Linien und Icon-Wiederholungen überarbeiten.
5. Restliche Länder im Icon- und Layoutpass abarbeiten.
6. Danach erst die vollständigen 1936–1942-Pfade spielen und konkrete inhaltliche Lücken schließen.

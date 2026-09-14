# Map and Roster Pass

## Umsetzungsstand — 14. September 2026

Die bisherigen Freigabesperren sind durch die ausdrueckliche Gesamtfreigabe des Benutzers aufgehoben. Der jetzt umgesetzte Kartenstand ersetzt den frueheren Vorschlag einer osmanischen Fragmentierung: Das Osmanische Reich bleibt als zusammenhaengender Block in Anatolien, der Levante und Mesopotamien bestehen. Eigenstaendig sind das Emirat Zentralarabien (`SAU`) und das Koenigreich Hedschas (`OMA`); Oman, Khasab und Dhofar stehen unter britischer Kontrolle.

Australien (`AST`) und Neuseeland (`NZL`) starten mit ihren Kerngebieten und Mandaten als britische Dominions. Die Dominion-Kabinettsentscheidungen verbinden Konsultation beziehungsweise Verteidigungskoordination mit Autonomie, Stabilitaet, Kriegsmoral und Beziehungen. Die Suedafrikanische Republik (`SAF`) startet unabhaengig auf Transvaal, Cape, Natal und Orange Free State ohne Commonwealth-Forschungsgruppe oder britisches Cosmetic Tag. Der Belgrade Settlement wird durch spiegelnde AUS-/YUG-Startevents und Beziehungen sichtbar erklaert.

Alle 299 Laenderfarbbloecke wurden auf eine hellere, besser unterscheidbare Palette umgestellt; 29 wichtige Tags besitzen bewusst gesetzte Ankerfarben. Sowohl der AOE-Imperial-World-Map-Mode und seine Spielregel als auch der mitgelieferte RT56-Custom-Map-Mode liegen nur noch als `.disabled` vor und werden von HOI4 nicht registriert. Die reproduzierbaren Werkzeuge sind `tools/apply_map_roster_state_ownership.py` und `tools/rebalance_country_colors.py`. Der statische Validator parst 5.279 Scriptdateien ohne bestaetigten Fehler.

Die China-Neuordnung wurde in diesem Kartenpaket nicht erzwungen, weil die bestehende Qing-/United-Front-Krise pauschale State-Transfers enthaelt und eine ungetestete Clique-Aufteilung diese funktionierende Kette beschaedigen wuerde. Sie bleibt ein eigener Content-Pass.

Stand: 14. September 2026. Dieser Bericht ist ein eigener Arbeitsstrang. Er verändert weder den Reward-Register-Abschluss noch den Großmächte-Strukturpass noch den späteren Farbkontrast-Pass. Die Zahlen stammen aus dem aktuellen Repository und beziehen sich auf den 1936-Start.

## Schritt 0 — Custom Map Mode vorübergehend deaktiviert

Der benutzerdefinierte Imperial-World-Kartenmodus war in `common/map_modes/zz_AOEIW_imperial_world_map_mode.txt` registriert. Die Definition wurde nach `common/map_modes/zz_AOEIW_imperial_world_map_mode.txt.disabled` verschoben. Dadurch lädt HOI4 sie nicht mehr als Map-Mode-Skript. Die Sprite-Definition `interface/zz_AOEIW_mapmode.gfx`, die Spielregel in `common/game_rules/zz_AOEIW_game_rules.txt` und die zugehörige Lokalisierung bleiben erhalten, damit die Funktion später ohne Rekonstruktion wiederhergestellt werden kann.

Reaktivierung: `common/map_modes/zz_AOEIW_imperial_world_map_mode.txt.disabled` wieder in `common/map_modes/zz_AOEIW_imperial_world_map_mode.txt` umbenennen. Die Abschaltung ist in Commit `d6e17564` festgehalten und bereits in die installierte Mod synchronisiert.

## Schritt 1 — Australien und Neuseeland als Dominions

### Aktueller Zustand

Die vorgesehenen Tags existieren bereits: Australien ist `AST` (`AUS` ist in diesem Mod Österreich-Ungarn), Neuseeland ist `NZL`. Beide besitzen Country-History, Charaktere und OOB-Verweise:

- `history/countries/AST - Australia.txt`, Hauptstadt State 285
- `history/countries/NZL - New Zealand.txt`, Hauptstadt State 284
- `common/national_focus/australia.txt` mit 171 Fokusdefinitionen
- `common/national_focus/australia_taog.txt` mit 217 Fokusdefinitionen und DLC-Auswahl
- `common/national_focus/new_zealand.txt`

Sie sind trotzdem beim Start landlos. Alle relevanten States besitzen `owner = ENG` und `add_core_of = ENG`. Ein Start-On-Action setzt nur `RAJ` und `CAN` frei; `AST` und `NZL` werden nicht als britische Untertanen angelegt.

### Vorgesehene State-Zuordnung

| Staat | Startgebiet | Status nach Umsetzung |
|---|---|---|
| `AST` | 285 Australian Capital Territory; 517 Victoria; 518 Tasmania; 519 South Australia; 520 Northern Territory; 521 Queensland; 522 Western Australia; 674 Central Australia; 870 North West Australia; 871 South West Australia; 872 North Queensland; 873 South West Queensland | `AST` Owner/Controller und Core |
| `AST` | 523 New Guinea; 725 Nauru | `AST` Owner/Controller, vorerst kein Core; australisch verwaltete Territorien |
| `NZL` | 284 New Zealand | `NZL` Owner/Controller und Core |
| `NZL` | 726 Samoa | `NZL` Owner/Controller, kein Core; Mandatsgebiet. Das vorhandene NZL-State-Scope für Widerstand bleibt sinnvoll. |

Die ENG-Cores werden aus diesen Gebieten entfernt. Britische Ansprüche werden nicht als permanente Cores konserviert, weil dies die Dominion-Logik und Besatzung bei einer späteren Trennung verfälschen würde.

### Dominion-Start und Autonomieleiter

Empfohlener Start:

- `ENG` wird Overlord von `AST` und `NZL`.
- Beide starten als `autonomy_dominion` mit niedriger Freiheit innerhalb dieser Stufe, Richtwert `freedom_level = 0.15` bis `0.20`.
- Der bestehende Commonwealth-Forschungsverbund bleibt erhalten.
- Die UK-Regierungsbalance „Parliament and Dominions“ gegen „Imperial Cabinet“ wird zum politischen Einstiegspunkt. Eine schmale Entscheidungsleiter genügt: Konsultation und materielle Hilfe erhöhen Autonomie und Loyalität; Zentralisierung senkt Autonomie, kostet Beziehungen oder Stabilität und erzeugt innenpolitischen Widerstand.
- Die Leiter benutzt vorhandene Autonomie-Stufen und wird nicht als zweites, paralleles Untertanensystem gebaut.

### Wirtschaftliche Auswirkung

Australiens zwölf Kernstates enthalten zusammen 6.540.400 Einwohner, 11 Zivilfabriken, 4 Militärfabriken und 2 Werften. Neuseeland und Samoa enthalten zusammen 568.997 Einwohner und 2 Zivilfabriken. New Guinea und Nauru fügen rund 720.841 Einwohner, aber keine Startfabriken hinzu.

ENG verliert damit die direkte Kontrolle über insgesamt 13 Zivilfabriken, 4 Militärfabriken, 2 Werften und rund 7,83 Millionen Einwohner. Ein Teil der Industrie und des Manpowers fließt nur noch entsprechend der Dominion-Autonomie an den Overlord. Das ist eine spürbare, beabsichtigte Abschwächung des britischen Starts und muss im Runtime-Test gegen Deutschlands, Frankreichs und Japans frühe Stärke geprüft werden.

### Kollisionscheck mit Commit `7620695a`

Der UK-Strukturcommit änderte ausschließlich `common/national_focus/AOEIW_ENG_focus.txt`, passende Ideen/Lokalisierung und die Register-/Berichtsdokumentation. Keine AST-/NZL-State-History und kein Dominion-On-Action wurde dort verändert. Die Theaterstruktur und ihre Reward-Profile bleiben unangetastet.

Die einzige inhaltliche Berührung ist gewollt: `AOEIW_STRUCT_ENG_imperial_preference` und die bereits vorhandene Governance-Balance enthalten britische Untertanenpolitik. Die neue Autonomieleiter soll dort anschließen, ohne Fokus-IDs, Mutex-Struktur oder die vier britischen Theaterprofile zu ändern.

### Freigabeumfang

Bei Freigabe werden ausschließlich die genannten State-Histories, ein enger Start-On-Action-/Scripted-Effect-Hook, notwendige Dominion-Entscheidungen sowie englische und deutsche Lokalisierung geändert. AST/NZL-Fokusbäume werden nur auf kaputte Annahmen über Landbesitz geprüft, nicht neu geschrieben.

**Konzept wartet auf Freigabe, keine Dateien verändert.**

## Schritt 2 — Dutch South Africa

### Aktueller Zustand und Tag-Entscheidung

Der passende Tag `SAF` existiert bereits und besitzt eine vollständige technische Basis:

- `history/countries/SAF - South Africa.txt` mit Hauptstadt 275, OOB und Charakteren
- `common/national_focus/south_africa.txt` mit 89 Fokusdefinitionen
- vorhandene Flaggen, Parteien, Namen und Diplomatieverweise

SAF ist landlos, weil Transvaal, Cape, Natal und Orange Free State ENG gehören und ENG-Cores sind. Die History setzt außerdem `SAF_ENG` als britisches Cosmetic Tag und bindet das Land an Commonwealth-Forschung. Beides widerspricht der gewünschten niederländisch-burischen Unabhängigkeit.

Ein neuer Tag wäre unnötig riskant: Er würde vorhandene Flaggen, Charaktere, Diplomatieprüfungen und RT56-Kompatibilität duplizieren. Empfohlen wird daher, `SAF` in diesem Szenario als eigenständige Dutch-Boer Republic zu verwenden.

### State- und Wirtschaftsgrundlage

| State | Einwohner | Startindustrie |
|---|---:|---:|
| 275 Transvaal | 2.987.089 | 5 Zivil-, 1 Militärfabrik |
| 681 Cape | 1.637.178 | 2 Zivilfabriken |
| 719 Natal | 3.962.157 | 2 Zivilfabriken |
| 940 Orange Free State | 693.274 | keine Fabrik |

Gesamt: 9.279.698 Einwohner, 9 Zivilfabriken und 1 Militärfabrik. Natal besitzt außerdem 48 Chromium und 4 Coal; Cape besitzt 2 Tungsten. Die irreführende Dateibezeichnung `681-Soviet Lakes.txt` ist Altbestand, während State-Kommentar und Lokalisierung korrekt „Cape“ lauten. Sie sollte in diesem Pass nicht umbenannt werden, weil der State-ID-Pfad technisch funktioniert.

British South West Africa (541), Bechuanaland (542), Rhodesia (545) und andere umliegende Kolonialgebiete bleiben britisch. Dadurch entsteht das gewünschte Verhältnis: Großbritannien ist ein mächtiger kolonialer Nachbar, aber kein Mutterland oder Overlord.

### Politische Identität und Inhalt

Der Staat soll in der englischen Fassung als **South African Republic** mit niederländisch-burischer Prägung auftreten; die deutsche Fassung kann **Südafrikanische Republik** verwenden. „Dutch South Africa“ bleibt die Arbeitsbezeichnung, damit kein ahistorischer direkter Besitz der Niederlande behauptet wird.

Ein eigener AOE-Szenariobaum mit etwa 32–36 Fokussen ersetzt für diesen Start den britisch geprägten RT56-Baum, ohne dessen Datei zu löschen. Fünf verbundene Handlungsstränge:

1. Volksraad, afrikanische Mehrheiten, englischsprachige Städte und der Streit um Staatsbürgerschaft;
2. Witwatersrand-Gold, Kimberley-Diamanten, Minenarbeit und Bahnexporte;
3. Kommando-Tradition gegen eine professionalisierte Union Defence Force;
4. kulturelle und wirtschaftliche Beziehungen zu den Niederlanden gegen pragmatische Abkommen mit britischen Kolonialnachbarn;
5. regionale Sicherheit, Grenzhandel und ein späteres südafrikanisches Endspiel.

Diese Pfade brauchen mindestens je eine Reaktion des Vereinigten Königreichs oder der Niederlande, Folgedecisions für Rohstoffe und einen klaren Nachkriegs-/Regionalabschluss. Sie sollen nicht aus austauschbaren Verwaltungsfokusketten bestehen.

### Farbe und Systemgrenzen

Die gegenwärtigen SAF-Farbdefinitionen widersprechen sich: Grün in `common/countries/South Africa.txt`, Pink in `common/countries/colors.txt`. Empfohlen ist ein eindeutiges Kupfer/Ocker, etwa `rgb { 181 111 52 }`. Es ist von ENG-Rot, POR-Grün, TUR-Türkis und den zentralafrikanischen Nachbarn grob unterscheidbar; der spätere globale Farbpass kann den exakten Wert korrigieren.

SAF startet vollständig unabhängig. Es erhält keine Dominion-Autonomieleiter, kein `SAF_ENG` Cosmetic Tag und keinen Commonwealth-Untertanenhook. Der Verlust von 9 Zivilfabriken, 1 Militärfabrik, 9,28 Millionen Einwohnern und wichtigen Rohstoffen für ENG ist Teil der Balanceprüfung von Schritt 1 und 2 zusammen.

### Freigabeumfang

Bei Freigabe werden die vier State-Histories, SAF-History/Scenario-Initialisierung, ein AOE-spezifischer Fokusbaum, die benötigten Ideen/Ereignisse/Entscheidungen, Farbe und zweisprachige Lokalisierung umgesetzt. Bestehende RT56-Dateien bleiben als Kompatibilitätsinhalt erhalten.

**Konzept wartet auf Freigabe, keine Dateien verändert.**

## Schritt 3 — China und Zentralasien

### Audit-Ergebnis

Die im Zielbild genannten Tags und Systeme sind teilweise vorhanden, aber die gewünschte sichtbare Aufteilung besteht 1936 nicht vollständig.

Vorhandene Country-Histories: `CHI`, `MAN`, `MON`, `QIN`, `SIK`, `TIB`, `XIC`, `XSM` und `YUN`. `QIN` ist als eigener AOE-Tag reserviert. Kompakte AOE-Frontier-Bäume existieren für `MAN`, `MON`, `QIN` und `XIC`.

Die tatsächliche 1936-Verteilung ist wesentlich zentralisierter:

- `CHI` besitzt 80 chinesische States.
- `MAN` besitzt nur State 610 Jehol als Startanker.
- `MON` besitzt fünf States.
- `SIK`, `XSM`, `TIB`, `YUN`, `XIC` und `QIN` besitzen keine Startgebiete.

Nach Spielbeginn startet `events/AOEIW_phase20_chinese_crisis.txt` über `common/on_actions/zzzz_AOEIW_phase20_united_front_on_actions.txt`. Innerhalb etwa einer Woche überträgt die Kette große Gebiete von CHI an MAN, setzt United-Front-/Qing-Cosmetics und führt zu einem Krieg CHI gegen MAN. Bei Qing-Niederlage gehen Gebiete zurück und MAN bleibt als kleiner japanischer Untertan zurück.

Das ist dynamisch, aber kein Vielstaatensystem nach dem beschriebenen Vorbild. Xinjiang Clique, Xibei San Ma, Tibet, Sichuan Province und Yunnan Clique bleiben landlos. Außerdem sieht der Spieler zunächst ein riesiges CHI, das wenige Tage später abrupt umgebaut wird. Die politische Ursache wird zwar über Events erzählt, die Karte kommuniziert beim Länderauswahlbildschirm jedoch eine andere Welt als die spätere Krise.

### Konkrete Lücke und enger Vorschlag

Eine Korrektur ist gerechtfertigt, aber sie sollte die funktionierende Qing-/United-Front-Kette erhalten:

1. `SIK`, `XSM`, `TIB`, `YUN` und `XIC` erhalten bereits 1936 ihre regionalen Kerngebiete und werden sichtbar spielbar. Die exakte State-Liste wird vor der Implementierung gegen alle Crisis-Transfers, Cores, Railways und Supply Hubs geprüft; bekannte Anker sind 287/617 Xinjiang, 322 Tibet und 325 Yunnan.
2. Diese Gebiete werden aus den pauschalen CHI→MAN-Transfers ausgenommen. Ihre Regierungen reagieren stattdessen per Einladung, Neutralität, Anerkennung oder Bündnisentscheidung auf die Krise.
3. `MAN` bleibt aus Kompatibilitätsgründen der operative Qing-Staat. `QIN` bleibt als reservierter Tag/Cosmetic-/Focus-Kompatibilität erhalten und wird nicht zusätzlich ohne klare Rolle auf die Karte gesetzt.
4. `XIC` verwendet seinen vorhandenen Frontier-Baum. Für `SIK`, `XSM`, `TIB` und `YUN` werden zunächst vorhandene RT56-Bäume auf Szenariotauglichkeit geprüft; nur fehlende Identität oder tote Annahmen rechtfertigen kompakte AOE-Ergänzungen im Bereich 15–25 Fokusse.
5. Shanghai League braucht vor jeder Umsetzung eine eindeutige Tag- und State-Zuordnung. Im aktuellen Startinventar ist kein klar als Shanghai League aktiver Staat belegt; dies ist eine zweite konkrete Lücke, aber kein Grund für einen ungeprüften neuen Tag.

Damit würde der Start sofort die alternative Ordnung zeigen, während die Chinese Crisis weiterhin dynamisch um Zentralregierung, Qing und Bündnisbildung eskaliert.

**Konzept wartet auf Freigabe, keine Dateien verändert.**

## Schritt 4 — Verworfener Altvorschlag: Osmanische Fraktionierung

> Dieser Vorschlag wurde ausdruecklich verworfen und nicht implementiert. Verbindlich ist der Umsetzungsstand am Dokumentanfang: TUR bleibt zusammenhaengend; nur Zentralarabien und Hedschas sind unabhaengig, waehrend Oman/Dhofar britisch sind.


### Aktueller Zustand

TUR besitzt derzeit einen sehr großen Block von Istanbul und Anatolien über Kurdistan, Syrien, Palästina, Mesopotamien, Zentralarabien und Oman. Yemen (293) ist bereits `YEM`; Persien ist eigenständig. Entgegen der Zielannahme ist Zentralarabien noch nicht unabhängig: `SAU` besitzt eine History und einen 26-Fokus-AOE-Baum, startet aber landlos. `OMA` wurde in AOE bereits als Kingdom of Hejaz vorbereitet und besitzt ebenfalls einen 26-Fokus-AOE-Baum, startet jedoch ebenfalls ohne Land.

Die sicherste Lösung verwendet vorhandene Tags. Das vermeidet zusätzliche Flag-Atlas-, Charakter-, Diplomatie- und Kompatibilitätsrisiken.

### Vorgeschlagener Start-Roster

| Tag und Arbeitsname | Vorgesehene States | Identität und Baum | Grobe Farbe |
|---|---|---|---|
| `TUR` — Ottoman Rump State | Istanbul/Thrace, westliches und zentrales Anatolien; Mesopotamien bleibt zunächst osmanischer Konfliktraum | bestehender spielbarer Kernstaat; Reform, Rückeroberung oder kontrollierter Rückzug | bestehendes Türkis |
| `KUR` — Kurdish Confederation | 350 Diyarbekir, 352 Hakkari, 800 Van, 1048 Sulymaniyah, 1049 Erbil | Stammespakt, Bergverteidigung, Mosulfrage; 18–22 neue AOE-Fokusse | vorhandenes Gold |
| `SYR` — Syrian Provincial Congress | 553 Lebanon, 554 Syria, 677 Aleppo, 680 Deir-az-Zur, optional 799 Hatay nach Grenzprüfung | Damaskus-Kongress, Kaufleute, arabische Offiziere, Hafenzölle; 20–24 Fokusse | Slate Blue |
| `ARM` — Armenian Republic | 353 Erzurum, 354 Trabzon; Hauptstadt muss aus der derzeitigen externen 230-Verwendung in dieses Gebiet verlegt werden | Flüchtlingsansiedlung, Grenzschutz, Kaukasusdiplomatie; 18–24 AOE-Fokusse statt des für diesen Start übergroßen Altbaums | Ziegelorange statt persischem Violett |
| `SAU` — Emirate of Central Arabia | 292 Nejd, 854 Jawf, 857 Ha'il, 858 Najiran, 859 Dammam, 678 Rub al Khali; 675 Al Hajara nach Grenzprüfung | Riad, Stammeskonsolidierung, Ölförderrechte; vorhandener 26-Fokus-AOE-Baum als Basis | vorhandenes helles Salbeigrün |
| `OMA` — Kingdom of Hejaz | 679 Hejaz, 855 Tabuk, 856 Asir-Makkah, 1022 Maan | Haschemiten, Pilgerverkehr, Hedschasbahn, Rotes Meer; vorhandener 26-Fokus-AOE-Baum | vorhandenes Kastanienrot |

Dies fügt fünf sichtbare Akteure neben dem osmanischen Rumpf hinzu. Iraq wird in diesem Pass nicht als sechster Neustaat herausgelöst; Baghdad, Basra und das zentrale Mesopotamien bleiben ein später Druckpunkt zwischen TUR, KUR, Persien und arabischen Bewegungen. Israel/Palästina-States werden erst nach Prüfung der dort bereits vorhandenen Content-Annahmen verteilt und nicht beiläufig einem neuen syrischen Block zugeschlagen.

### State-, Core- und Diplomatieprinzip

- Jeder neue Staat erhält Owner/Controller und Cores nur auf seinem stabilen Kerngebiet.
- TUR-Cores in abgetrennten Gebieten werden in Claims oder gezielte Rückeroberungsentscheidungen überführt, damit neue Staaten nicht dauerhaft als besetztes Kernland behandelt werden.
- Grenzfälle 675 Al Hajara und 799 Hatay werden über Startsupply, Eisenbahnverbindungen, Victory Points und Nachbarprovinzen entschieden.
- Die fünf Staaten bekommen getrennte Startbeziehungen und Reaktionen auf TUR. Ein gemeinsames „break free“-Textmuster wird vermieden.
- Frühe Kriege brauchen Friedens- und Nachkriegsfolgen: Anerkennung, Autonomie, Föderationsangebote, Claims und Integrationsentscheidungen.

### Technische Pfade und Risiken

Wichtige Bestandsdateien sind `history/countries/TUR - Turkey.txt`, `SAU - Saudi Arabia.txt`, `OMA - Oman.txt`, die entsprechenden ARM/KUR/SYR-Histories sowie `common/national_focus/AOEIW_world_expansion_focus.txt`. OMA ist dort bewusst als Hejaz vorbereitet und darf nicht zugleich als unabhängiges Oman interpretiert werden.

Vor Umsetzung müssen TUR-/Persia-/Levant-Fokusprüfungen nach `original_tag = SAU` und `original_tag = OMA` regressionstauglich gemacht werden. Die Aufteilung verändert Supply, Fabriken, Bevölkerung und Frontlängen stark; eine reine Parserprüfung reicht nicht, weshalb ein frischer 1936-Start und AI-Simulation bis mindestens 1939 Pflicht sind.

**Konzept wartet auf Freigabe, keine Dateien verändert.**

## Schritt 5 — Österreich-Ungarn und Jugoslawien

### Audit-Ergebnis

Die gewünschte Nationalitäten-/Autonomiemechanik existiert bereits weitgehend:

- `common/on_actions/AOEIW22_nationalities_on_actions.txt` initialisiert föderales, dualistisches oder zentralistisches Modell und allgemeine Spannung.
- `common/decisions/AOEIW22_political_expansion_decisions.txt` enthält Föderalisierung, zentrale Verwaltung, Kompromiss und Gendarmerie.
- `common/on_actions/AOEIW24_systemic_depth.txt` setzt magyarische, tschechische, südslawische und galizische Spannungen.
- `common/decisions/AOEIW24_systemic_depth.txt` enthält unter anderem Hungarian Compromise, Bohemian Crown, South Slav Diet und Congress of Crownlands.
- Die zugehörigen Events und Austria-Fokuspfade erzählen bereits von Crownland Congress, Danubian Federal Compact und Wiener Zentraldienst.

Das Problem ist daher kein fehlendes System, sondern ein fehlender Ausgangskontext: Die Dateien erklären nicht überzeugend, warum ein vereintes Habsburgerreich neben einem unabhängigen jugoslawischen Staat existiert, während Wien weiterhin „South Slav“ delegates und tension verwaltet.

### Empfehlung: vorhandenes System erzählerisch abschließen

Kein zweites Autonomiesystem wird gebaut. Der saubere Fix ist eine kleine, verbundene Ergänzung:

1. Ein AUS-Startevent erklärt den früheren **Belgrade Settlement**: Nach einer Südslawenkrise erkannte Wien einen unabhängigen südslawischen Staat an, um den verbleibenden habsburgischen Verband aus Ungarn, Böhmen, der Slowakei, Galizien und den österreichischen Ländern zu retten.
2. Ein spiegelndes YUG-Startevent erklärt, dass Belgrad seine Unabhängigkeit gewonnen hat, aber Grenz-, Minderheiten- und Handelsfragen offen sind.
3. Ein kleiner, sichtbarer Startmodifier oder Tooltip auf beiden Seiten hält die Folgen fest: fragile Entspannung, wirtschaftliche Verflechtung und konkurrierende Ansprüche. Er darf keinen neuen permanenten Reward-Profilkonflikt erzeugen.
4. Die vorhandene Variable `AOEIW24_AUS_south_slav_tension` wird im Text als Spannung um verbliebene südslawische Minderheiten und die Beziehung zu Belgrad erklärt. Sie behauptet nicht mehr, ganz Jugoslawien sei ein Kronland.
5. Die vorhandene Entscheidung „Convene a South Slav Diet“ oder ihr Folgeevent erhält bei bestehendem YUG eine echte Außenwirkung, etwa Relations-/Guarantee-/Claim-Optionen. Die exakte Wirkung wird gegen die AUS- und YUG-Struktur geprüft und bewahrt alle bestehenden Fokus-IDs.
6. Bookmark- und Country-History-Texte werden zweisprachig ergänzt. State-Grenzen bleiben unverändert.

Diese Lösung macht die Koexistenz sofort verständlich und benutzt die bereits vorhandene Mechanik als späteren Konfliktmotor. Ein bloßer Kommentar in einer History-Datei wäre für den Spieler unsichtbar und reicht deshalb nicht als Release-Fix.

**Konzept wartet auf Freigabe, keine Dateien verändert.**

## Weitere Kandidaten — nur Ausblick

Nach diesem Pass verdienen folgende Regionen später eine reine Roster-Prüfung:

- Britisch-West- und Ostafrika: große direkte ENG-Blöcke mit möglichen regionalen Akteuren;
- französisches Nord- und Westafrika: Kolonialverwaltung, lokale Eliten und Nachkriegsfolgen;
- Niederländisch-Indien: ein großer Kolonialblock mit bereits vorhandenen IND-Kompatibilitätsannahmen;
- Kaukasus jenseits Armeniens: Georgia/Azerbaijan nur bei tragfähiger State- und Content-Basis;
- Zentralasien nördlich von Xinjiang: mögliche regionale Akteure nur, wenn sie mehr als bloße Kartenfarbe liefern;
- Karibik und britische Inselstützpunkte: eher Interaktions-/Autonomiecontent als viele winzige Tags.

Keine dieser Regionen gehört zum freigegebenen Implementierungsumfang.

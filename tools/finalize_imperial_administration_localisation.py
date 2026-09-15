from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

EN_TITLES = {
    "IAF": ["The Massawa-Mogadishu Axis", "The Viceroy's Council", "Call the Colonial Consultative Assembly", "A Statuto for the Red Sea", "The Colonial Treasury", "Finish the Strada Imperiale", "Open the Port of Assab", "A Treasury in Asmara", "Comando Africa Orientale", "Expand the Ascari Battalions", "Motor Columns for the Ogaden", "The Red Sea Defence Plan", "The Cairo-Rome Air Route", "A Viceroyalty That Can Endure"],
    "MAF": ["The Duala Charter", "Renew the Company Concessions", "Seat the District Councils", "The Governor-General's Ordinance", "Open the Interior", "Rails to the Copperbelt", "Steamers on the Congo", "The Central African Customs Union", "Rebuild the Schutztruppe", "The Colonial Officer Corps", "Commission African Officers", "The Equatorial Defence Staff", "The Cape-to-Cairo Problem", "From Charter to Federation"],
    "GPA": ["Raise the Imperial Ensign", "The Naval Governor", "Convene the Island Council", "The Rabaul Ordinances", "Make the Stations Pay", "The Copra Syndicate", "Build the Island Dockyards", "A Pacific Supply Account", "Guard the Sea Lanes", "Recruit the Coastwatchers", "Base the Cruiser Squadron", "The Oceanic Defence Network", "Speak for the Islands", "Germany's Oceanic Gate"],
}

EN_DESCS = {
    "IAF": [
        "Massawa and Mogadishu lie a thousand miles apart. A regular coastal service, common accounts and a single chain of command must make them one colony in more than name.",
        "The viceroy will govern through appointed officials and officers answerable to Rome. Orders will travel quickly, although little authority will remain in local hands.",
        "Merchants, elders and municipal delegates demand a place at the table. Their assembly will slow decrees but give the administration roots beyond its garrisons.",
        "A colonial statute will settle the powers of Asmara, Mogadishu and Rome before the next emergency forces the question.",
        "Separate Eritrean and Somali accounts conceal waste and competing priorities. One treasury can direct customs revenue toward roads, ports and defence.",
        "Engineers will close the gaps in the imperial road and establish guarded depots along its length. Troops and lorries must be able to cross the colony without waiting on coastal shipping.",
        "Assab can become the southern outlet of the Eritrean plateau. New quays and warehouses will turn the neglected harbour into a useful Red Sea station.",
        "Customs receipts will remain in Asmara long enough to finance local obligations. Rome will still set policy, but the viceroyalty will no longer plead for every lira.",
        "The scattered colonial commands need one operational headquarters. Staff officers in Asmara will prepare joint plans for both shores of the Horn.",
        "The Ascari know the climate, languages and tracks on which any campaign will depend. Enlarged battalions under experienced local NCOs will form the backbone of the field army.",
        "The Ogaden punishes forces tied to railheads. Light motor columns carrying their own fuel and water can patrol the interior and concentrate before an enemy can respond.",
        "Massawa, Assab and Mogadishu will share warning stations, reserves and coastal plans. An attack on one port must bring the whole command into action.",
        "Regular aircraft between Cairo, Asmara and Rome will carry orders, specialists and urgent cargo around the British-held sea lanes.",
        "The roads, treasury and colonial army now answer to the same government. Italian East Africa can survive a shipping crisis and bargain with Rome from a position of proven usefulness.",
    ],
    "MAF": [
        "Duala's administrators must turn a chain of conquered territories into a government. The charter defines who collects revenue, commands the police and answers to Berlin.",
        "Trading companies offer ships, accountants and capital in return for broad concessions. Restoring their privileges will extract resources quickly and place much of the interior beyond public scrutiny.",
        "District chiefs and municipal delegates can carry policy where German officials are few. Recognising their councils trades some control for consent and steadier administration.",
        "The governor-general will publish one code for customs, labour and district government. Rival colonial offices can no longer issue contradictory orders.",
        "The coast cannot support the administration by itself. Survey parties and river posts will connect inland farms and mines to the customs system.",
        "A dependable railway toward the Copperbelt promises heavy mineral traffic and rapid troop movement, but it will consume the administration's construction budget.",
        "The Congo already provides a road into the interior. Dredging channels and subsidising river steamers can move cargo sooner than another transcontinental railway.",
        "Internal tariffs keep each former colony looking toward its old capital. A shared customs area will give Mittelafrika one market and one source of revenue.",
        "The old Schutztruppe tradition offers a cadre for the new territory. Its companies must be rebuilt around modern signals, medical services and dependable supply columns.",
        "German officers will retain direct command from company to headquarters. Discipline and doctrine will be consistent, even where the force lacks local initiative.",
        "African NCOs already carry much of the daily burden. Commissions and staff schooling will widen recruitment and give the army officers who understand its districts.",
        "Duala will coordinate garrisons, river patrols and railway reserves through an equatorial defence staff. No district should face a revolt or invasion alone.",
        "British routes from the Cape toward Cairo cut across every German plan for the interior. Diplomats and surveyors must decide where commerce ends and strategic encirclement begins.",
        "Mittelafrika now possesses common accounts, transport and a territorial army. The charter can mature into a federation capable of governing between instructions from Berlin.",
    ],
    "GPA": [
        "Rabaul will again fly the imperial colours over Germany's scattered Pacific stations. A naval administration must first establish which islands it can actually supply and defend.",
        "A naval governor can align every harbour, wireless post and plantation with fleet requirements. Civilian concerns will yield whenever the sea command demands it.",
        "Planters, missionaries and island representatives know the stations better than visiting officers. An island council will give them influence over taxation and labour policy.",
        "The Rabaul ordinances will reconcile naval authority with civilian courts and local councils. Captains and district officers will finally work from the same rulebook.",
        "Prestige cannot pay for coal, cables or repair crews. The stations must export enough copra and phosphates to meet a meaningful share of their own bills.",
        "A single syndicate can standardise contracts, shipping and processing across the islands. Its profits will finance administration, at the cost of concentrating economic power.",
        "Rabaul and the principal anchorages need slips, workshops and fuel storage. Even modest dockyards will reduce the long voyage to Asian yards for every repair.",
        "Revenue from plantations and harbour dues will be reserved for fuel, stores and emergency shipping. The fleet should know what the islands can provide before war begins.",
        "No garrison can protect every beach. Defence depends on seeing hostile ships early and keeping supply vessels moving between distant anchorages.",
        "Radio-equipped coastwatchers will report ships and aircraft from islands too small for permanent garrisons. Their value lies in warning the fleet before the enemy disappears into the ocean.",
        "A cruiser squadron at Rabaul gives the administration a mobile reserve and a visible claim to the sea lanes. Dockyard capacity will be organised around keeping it at sea.",
        "Wireless posts, coastwatchers and naval bases will operate as one network. Each island becomes an observation point and each harbour a fallback position.",
        "The island council will send a permanent delegation to Berlin. Pacific policy must reflect distances and risks that are invisible on maps in the Wilhelmstrasse.",
        "The administration now offers Germany ports, intelligence and a fleet base across the western Pacific. Its survival rests on the network built between the islands, rather than any single fortress.",
    ],
}

DE_TITLES = {
    "IAF": ["Die Achse Massaua-Mogadischu", "Der Rat des Vizekoenigs", "Einberufung der kolonialen Ratsversammlung", "Ein Statuto fuer das Rote Meer", "Die Kolonialkasse", "Vollendung der Strada Imperiale", "Oeffnung des Hafens von Assab", "Eine Staatskasse in Asmara", "Comando Africa Orientale", "Die Askari-Bataillone erweitern", "Motorkolonnen fuer den Ogaden", "Der Verteidigungsplan fuer das Rote Meer", "Die Luftlinie Kairo-Rom", "Ein Vizekoenigtum von Bestand"],
    "MAF": ["Die Duala-Charta", "Erneuerung der Konzessionsgesellschaften", "Sitze fuer die Bezirksraete", "Die Verordnung des Generalgouverneurs", "Das Binnenland erschliessen", "Schienen zum Copperbelt", "Dampfer auf dem Kongo", "Die zentralafrikanische Zollunion", "Die Schutztruppe wiederaufbauen", "Das Kolonialoffizierskorps", "Afrikanische Offiziere ernennen", "Der aequatoriale Verteidigungsstab", "Das Kap-Kairo-Problem", "Von der Charta zur Foederation"],
    "GPA": ["Die Reichsflagge hissen", "Der Marinegouverneur", "Einberufung des Inselrats", "Die Rabauler Verordnungen", "Die Stationen muessen sich tragen", "Das Kopra-Syndikat", "Werften fuer die Inseln", "Ein pazifischer Versorgungsetat", "Die Seewege sichern", "Kuestenbeobachter anwerben", "Das Kreuzergeschwader stationieren", "Das ozeanische Verteidigungsnetz", "Fuer die Inseln sprechen", "Deutschlands Tor zum Ozean"],
}

DE_DESCS = {
    "IAF": [
        "Massaua und Mogadischu liegen weit auseinander. Ein fester Kuestendienst, gemeinsame Buecher und eine Befehlslinie muessen aus beiden Gebieten mehr als nur auf dem Papier eine Kolonie machen.",
        "Der Vizekoenig wird mit ernannten Beamten und Offizieren regieren, die Rom verantwortlich sind. Befehle gelangen schneller ans Ziel, waehrend vor Ort nur wenig Entscheidungsraum bleibt.",
        "Haendler, Aelteste und staedtische Abgesandte verlangen Mitsprache. Ihre Versammlung verlangsamt Erlasse, verankert die Verwaltung aber jenseits ihrer Garnisonen.",
        "Ein Kolonialstatut regelt die Befugnisse Asmaras, Mogadischus und Roms, bevor der naechste Notstand die Frage erzwingt.",
        "Getrennte eritreische und somalische Konten verdecken Verschwendung und widerstreitende Plaene. Eine Kasse kann Zoelle gezielt fuer Strassen, Haefen und Verteidigung einsetzen.",
        "Pioniere schliessen die Luecken der Reichsstrasse und legen bewachte Depots an. Truppen und Lastwagen sollen die Kolonie ohne den Umweg ueber See durchqueren koennen.",
        "Assab kann zum suedlichen Ausfuhrhafen des eritreischen Hochlands werden. Neue Kais und Lagerhaeuser machen aus dem vernachlaessigten Hafen einen brauchbaren Stuetzpunkt.",
        "Die Zolleinnahmen bleiben lange genug in Asmara, um lokale Pflichten zu bezahlen. Rom bestimmt weiter die Politik, doch der Vizekoenig muss nicht mehr um jede Lira bitten.",
        "Die verstreuten Kolonialkommandos brauchen ein gemeinsames Hauptquartier. Stabsoffiziere in Asmara bereiten Plaene fuer beide Seiten des Horns vor.",
        "Die Askari kennen Klima, Sprachen und Wege. Vergroesserte Bataillone unter erfahrenen einheimischen Unteroffizieren bilden das Rueckgrat des Feldheeres.",
        "Der Ogaden bestraft Truppen, die an Bahnen gebunden sind. Leichte Motorkolonnen mit eigenem Treibstoff und Wasser koennen den Raum sichern und sich rasch sammeln.",
        "Massaua, Assab und Mogadischu teilen Warnposten, Reserven und Kuestenplaene. Ein Angriff auf einen Hafen setzt das gesamte Kommando in Bewegung.",
        "Regelmaessige Fluege zwischen Kairo, Asmara und Rom transportieren Befehle, Fachleute und dringende Fracht unabhaengig von den britisch beherrschten Seewegen.",
        "Strassen, Kasse und Kolonialheer gehorchen nun derselben Regierung. Italienisch-Ostafrika kann eine Schifffahrtskrise ueberstehen und Rom seinen Nutzen beweisen.",
    ],
    "MAF": [
        "Die Beamten in Duala muessen aus eroberten Gebieten eine Regierung formen. Die Charta bestimmt, wer Steuern erhebt, die Polizei fuehrt und Berlin Rechenschaft schuldet.",
        "Handelsgesellschaften bieten Schiffe, Buchhalter und Kapital gegen weitreichende Konzessionen. Ihre Vorrechte versprechen schnelle Ertraege, entziehen das Binnenland aber oeffentlicher Kontrolle.",
        "Bezirkschefs und staedtische Abgesandte tragen Politik dorthin, wo deutsche Beamte fehlen. Anerkannte Raete tauschen einen Teil der Kontrolle gegen Zustimmung und bestaendigere Verwaltung.",
        "Der Generalgouverneur erlaesst ein Recht fuer Zoll, Arbeit und Bezirke. Die alten Kolonialaemter duerfen keine widerspruechlichen Anweisungen mehr geben.",
        "Die Kueste kann die Verwaltung nicht allein tragen. Vermessungstrupps und Flussposten verbinden die Farmen und Minen des Binnenlands mit dem Zollsystem.",
        "Eine verlaessliche Bahn zum Copperbelt verspricht Erzverkehr und schnelle Truppenbewegungen, beansprucht jedoch den groessten Teil des Bauetats.",
        "Der Kongo ist bereits eine Strasse ins Innere. Ausgebaggerte Fahrrinnen und gefoerderte Dampfer bewegen Fracht frueher als eine weitere Kontinentalbahn.",
        "Binnenzoelle binden jede ehemalige Kolonie an ihre alte Hauptstadt. Ein gemeinsamer Zollraum gibt Mittelafrika einen Markt und eine Einnahmequelle.",
        "Die alte Tradition der Schutztruppe liefert den Kader fuer das neue Gebiet. Ihre Kompanien brauchen moderne Fernmelder, Sanitaetsdienste und verlaessliche Versorgungskolonnen.",
        "Deutsche Offiziere behalten den unmittelbaren Befehl von der Kompanie bis zum Hauptquartier. Disziplin und Lehre bleiben einheitlich, doch lokale Eigeninitiative bleibt knapp.",
        "Afrikanische Unteroffiziere tragen bereits den Alltag der Truppe. Offizierspatente und Stabsschulen erweitern die Rekrutierung und geben dem Heer Kenner seiner Bezirke.",
        "Duala koordiniert Garnisonen, Flusspatrouillen und Bahnreserven durch einen aequatorialen Verteidigungsstab. Kein Bezirk soll Aufstand oder Invasion allein begegnen.",
        "Britische Wege vom Kap nach Kairo durchkreuzen jeden deutschen Plan fuer das Binnenland. Diplomaten und Vermesser muessen bestimmen, wo Handel endet und Einkreisung beginnt.",
        "Mittelafrika besitzt gemeinsame Konten, Verkehrswege und ein Territorialheer. Aus der Charta kann eine Foederation werden, die auch zwischen Weisungen aus Berlin regiert.",
    ],
    "GPA": [
        "Rabaul hisst wieder die Reichsflagge ueber Deutschlands verstreuten Pazifikstationen. Die Marineverwaltung muss zuerst klaeren, welche Inseln sie versorgen und verteidigen kann.",
        "Ein Marinegouverneur richtet Haefen, Funkposten und Plantagen an den Beduerfnissen der Flotte aus. Zivile Anliegen weichen, sobald das Seekommando es verlangt.",
        "Pflanzer, Missionare und Inselvertreter kennen die Stationen besser als anreisende Offiziere. Ein Inselrat gibt ihnen Einfluss auf Steuern und Arbeitspolitik.",
        "Die Rabauler Verordnungen gleichen Marinegewalt, Zivilgerichte und lokale Raete ab. Kapitaene und Bezirksbeamte arbeiten endlich nach demselben Regelwerk.",
        "Prestige bezahlt weder Kohle noch Kabel oder Werftarbeiter. Kopra und Phosphate muessen einen bedeutenden Teil der eigenen Rechnungen decken.",
        "Ein Syndikat vereinheitlicht Vertraege, Verschiffung und Verarbeitung auf den Inseln. Seine Gewinne finanzieren die Verwaltung, konzentrieren aber wirtschaftliche Macht.",
        "Rabaul und die wichtigsten Ankerplaetze brauchen Hellingen, Werkstaetten und Treibstofflager. Schon kleine Werften ersparen fuer jede Reparatur die lange Fahrt nach Asien.",
        "Einnahmen aus Plantagen und Hafengebuehren werden fuer Treibstoff, Vorraete und Notschiffe reserviert. Die Flotte soll vor Kriegsbeginn wissen, was die Inseln leisten koennen.",
        "Keine Garnison kann jeden Strand bewachen. Die Verteidigung muss feindliche Schiffe frueh sehen und Versorgungsschiffe zwischen fernen Ankerplaetzen in Fahrt halten.",
        "Kuestenbeobachter mit Funkgeraeten melden Schiffe und Flugzeuge von Inseln, die keine feste Garnison tragen koennen. Ihre Warnung erreicht die Flotte, bevor der Gegner wieder im Ozean verschwindet.",
        "Ein Kreuzergeschwader in Rabaul gibt der Verwaltung eine bewegliche Reserve und einen sichtbaren Anspruch auf die Seewege. Die Werften halten es einsatzbereit.",
        "Funkposten, Kuestenbeobachter und Marinestuetzpunkte arbeiten als ein Netz. Jede Insel wird zum Beobachtungsposten und jeder Hafen zur Ausweichstellung.",
        "Der Inselrat entsendet eine staendige Abordnung nach Berlin. Pazifikpolitik muss Entfernungen und Gefahren beruecksichtigen, die auf Karten in der Wilhelmstrasse unsichtbar bleiben.",
        "Die Verwaltung bietet Deutschland Haefen, Aufklaerung und eine Flottenbasis im westlichen Pazifik. Ihr Bestand ruht auf dem Netz zwischen den Inseln und nicht auf einer einzelnen Festung.",
    ],
}

SUFFIXES = ["root", "left", "right", "charter", "econ", "econ_l", "econ_r", "econ_cap", "mil", "mil_l", "mil_r", "mil_cap", "dip", "final"]

EXTRA_EN = {
    "AOEIW39_IAF_viceroys_council": "The Viceroy's Council", "AOEIW39_IAF_viceroys_council_desc": "Appointed officials execute Rome's orders quickly, reinforcing authority and military readiness while restraining local autonomy.",
    "AOEIW39_IAF_consultative_assembly": "The Colonial Consultative Assembly", "AOEIW39_IAF_consultative_assembly_desc": "Municipal delegates and local notables lend the administration legitimacy and press for a greater share of its decisions.",
    "AOEIW39_IAF_ascari_command": "The Ascari Command", "AOEIW39_IAF_ascari_command_desc": "Expanded locally recruited battalions give the viceroyalty manpower and cohesion suited to East African operations.",
    "AOEIW39_IAF_motor_columns": "Ogaden Motor Columns", "AOEIW39_IAF_motor_columns_desc": "Self-contained mobile columns cross arid country quickly and place less strain on the thin supply network.",
    "AOEIW39_MAF_company_rule": "Renewed Company Rule", "AOEIW39_MAF_company_rule_desc": "Concession companies maximise extraction and factory output, while coercive management erodes political stability.",
    "AOEIW39_MAF_district_councils": "The District Councils", "AOEIW39_MAF_district_councils_desc": "Recognised local councils improve consent and administration while shifting a measure of authority away from Duala.",
    "AOEIW39_MAF_schutztruppe": "The New Schutztruppe", "AOEIW39_MAF_schutztruppe_desc": "A centrally commanded colonial force emphasises discipline, defence and unit cohesion.",
    "AOEIW39_MAF_african_officers": "African Officer Commissions", "AOEIW39_MAF_african_officers_desc": "Opening commissions to experienced African soldiers broadens recruitment and strengthens recovery in the field.",
    "AOEIW39_GPA_naval_governor": "The Naval Governor", "AOEIW39_GPA_naval_governor_desc": "Naval authority directs the islands toward dockyard work and longer-range operations while holding autonomy in check.",
    "AOEIW39_GPA_island_council": "The Island Council", "AOEIW39_GPA_island_council_desc": "Civilian and island representatives bring steadier government, improved trade relations and pressure for self-rule.",
    "AOEIW39_GPA_coastwatchers": "The Coastwatcher Service", "AOEIW39_GPA_coastwatchers_desc": "Radio posts hidden across the islands extend naval detection and give exposed garrisons time to prepare.",
    "AOEIW39_GPA_cruiser_station": "The Rabaul Cruiser Station", "AOEIW39_GPA_cruiser_station_desc": "Workshops, fuel depots and a permanent squadron make Rabaul a base for fast ocean patrols.",
    "AOEIW39_imperial_roster.3.t": "The Administration Takes Shape", "AOEIW39_imperial_roster.3.a": "Put the settlement into force.",
    "AOEIW39_final_IAF": "The roads, ports and colonial command now work as one system. Italian East Africa can endure a broken sea route and continue the campaign from its own resources.",
    "AOEIW39_final_MAF": "Duala now presides over common accounts, transport and defence. Mittelafrika has become a territorial federation rather than a collection of conquered districts.",
    "AOEIW39_final_GPA": "Rabaul's wireless network, dockyards and island councils bind the Pacific stations together. Germany now possesses an oceanic administration able to warn, supply and defend itself.",
}

EXTRA_DE = {
    "AOEIW39_IAF_viceroys_council": "Der Rat des Vizekoenigs", "AOEIW39_IAF_viceroys_council_desc": "Ernannte Beamte setzen Roms Befehle rasch um, staerken Autoritaet und Kriegsbereitschaft und begrenzen dabei die lokale Selbstverwaltung.",
    "AOEIW39_IAF_consultative_assembly": "Die koloniale Ratsversammlung", "AOEIW39_IAF_consultative_assembly_desc": "Staedtische Abgesandte und lokale Notabeln geben der Verwaltung Rueckhalt und verlangen groesseren Anteil an ihren Entscheidungen.",
    "AOEIW39_IAF_ascari_command": "Das Askari-Kommando", "AOEIW39_IAF_ascari_command_desc": "Vergroesserte einheimische Bataillone geben dem Vizekoenigtum Arbeitskraft und Zusammenhalt fuer ostafrikanische Feldzuege.",
    "AOEIW39_IAF_motor_columns": "Motorkolonnen im Ogaden", "AOEIW39_IAF_motor_columns_desc": "Selbststaendige mobile Kolonnen durchqueren trockenes Land schnell und entlasten das duenne Versorgungsnetz.",
    "AOEIW39_MAF_company_rule": "Erneuerte Konzessionsherrschaft", "AOEIW39_MAF_company_rule_desc": "Konzessionsgesellschaften steigern Rohstoffgewinnung und Produktion, waehrend ihre Zwangsmethoden die politische Stabilitaet untergraben.",
    "AOEIW39_MAF_district_councils": "Die Bezirksraete", "AOEIW39_MAF_district_councils_desc": "Anerkannte lokale Raete verbessern Zustimmung und Verwaltung und verlagern einen Teil der Macht aus Duala.",
    "AOEIW39_MAF_schutztruppe": "Die neue Schutztruppe", "AOEIW39_MAF_schutztruppe_desc": "Eine zentral gefuehrte Kolonialtruppe setzt auf Disziplin, Verteidigung und Zusammenhalt.",
    "AOEIW39_MAF_african_officers": "Afrikanische Offizierspatente", "AOEIW39_MAF_african_officers_desc": "Offizierspatente fuer erfahrene afrikanische Soldaten verbreitern die Rekrutierung und staerken die Erholung im Feld.",
    "AOEIW39_GPA_naval_governor": "Der Marinegouverneur", "AOEIW39_GPA_naval_governor_desc": "Die Marinegewalt richtet die Inseln auf Werftarbeit und weitreichende Einsaetze aus und haelt ihre Selbstverwaltung klein.",
    "AOEIW39_GPA_island_council": "Der Inselrat", "AOEIW39_GPA_island_council_desc": "Zivile und insulare Vertreter sorgen fuer bestaendigere Regierung, bessere Handelsbeziehungen und Druck auf mehr Selbstverwaltung.",
    "AOEIW39_GPA_coastwatchers": "Der Kuestenbeobachtungsdienst", "AOEIW39_GPA_coastwatchers_desc": "Verborgene Funkposten auf den Inseln erweitern die Seeaufklaerung und geben gefaehrdeten Garnisonen Zeit zur Vorbereitung.",
    "AOEIW39_GPA_cruiser_station": "Der Kreuzerstandort Rabaul", "AOEIW39_GPA_cruiser_station_desc": "Werkstaetten, Treibstofflager und ein staendiges Geschwader machen Rabaul zur Basis schneller Ozeanpatrouillen.",
    "AOEIW39_imperial_roster.3.t": "Die Verwaltung nimmt Gestalt an", "AOEIW39_imperial_roster.3.a": "Die Ordnung in Kraft setzen.",
    "AOEIW39_final_IAF": "Strassen, Haefen und Kolonialkommando arbeiten nun als ein System. Italienisch-Ostafrika kann einen unterbrochenen Seeweg ueberstehen und den Feldzug aus eigenen Mitteln fortsetzen.",
    "AOEIW39_final_MAF": "Duala verfuegt nun ueber gemeinsame Konten, Verkehrswege und Verteidigung. Mittelafrika ist zu einer Territorialfoederation statt einer Ansammlung eroberter Bezirke geworden.",
    "AOEIW39_final_GPA": "Rabauls Funknetz, Werften und Inselraete verbinden die Pazifikstationen. Deutschland besitzt nun eine ozeanische Verwaltung, die sich selbst warnen, versorgen und verteidigen kann.",
}

COUNTRY_EN = {"IAF": ("Italian East Africa", "Italian East Africa", "Italo-East African"), "MAF": ("Mittelafrika", "Mittelafrika", "Mittelafrikan"), "GPA": ("German Pacific Administration", "the German Pacific Administration", "German Pacific")}
COUNTRY_DE = {"IAF": ("Italienisch-Ostafrika", "Italienisch-Ostafrika", "italienisch-ostafrikanisch"), "MAF": ("Mittelafrika", "Mittelafrika", "mittelafrikanisch"), "GPA": ("Deutsche Pazifikverwaltung", "die Deutsche Pazifikverwaltung", "deutsch-pazifisch")}

def rewrite(path: Path, titles, descs, extra, countries):
    text = path.read_text(encoding="utf-8-sig")
    replacements = {}
    for tag in ("IAF", "MAF", "GPA"):
        for suffix, title, desc in zip(SUFFIXES, titles[tag], descs[tag]):
            replacements[f"AOEIW39_{tag}_{suffix}"] = title
            replacements[f"AOEIW39_{tag}_{suffix}_desc"] = desc
        name, definite, adjective = countries[tag]
        replacements[tag] = name
        replacements[f"{tag}_DEF"] = definite
        replacements[f"{tag}_ADJ"] = adjective
        replacements[f"{tag}_neutrality"] = name
        replacements[f"{tag}_neutrality_DEF"] = definite
        replacements[f"{tag}_neutrality_ADJ"] = adjective
    replacements.update(extra)
    lines = text.splitlines()
    found = set()
    for i, line in enumerate(lines):
        m = re.match(r"\s*([^:#]+):\d+\s+\"", line)
        if m and m.group(1) in replacements:
            key = m.group(1)
            value = replacements[key].replace('"', '\\"')
            lines[i] = f' {key}:0 "{value}"'
            found.add(key)
    for key, value in replacements.items():
        if key not in found:
            lines.append(f' {key}:0 "{value.replace(chr(34), chr(92) + chr(34))}"')
    path.write_text("\n".join(lines) + "\n", encoding="utf-8-sig")

rewrite(ROOT / "localisation/english/zzzzzzzzzzzzzzzzzz_AOEIW39_imperial_roster_l_english.yml", EN_TITLES, EN_DESCS, EXTRA_EN, COUNTRY_EN)
rewrite(ROOT / "localisation/german/zzzzzzzzzzzzzzzzzz_AOEIW39_imperial_roster_l_german.yml", DE_TITLES, DE_DESCS, EXTRA_DE, COUNTRY_DE)

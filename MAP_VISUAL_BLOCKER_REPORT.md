# Kartenoptik- und Konturblocker

Stand: 14. September 2026. Dieser Bericht klaert die beiden vom Benutzer gesetzten Blocker. Er nimmt keine State-Umverteilung und keine Rendering-Aenderung vor.

## 1. Custom Map Mode und sichtbarer Kartenlook

Der aktuelle Screenshot zeigt den normalen politischen Kartenmodus, nicht den frueheren AOE-Custom-Map-Mode und nicht den RT56-Core/Claim-Map-Mode.

Der technische Nachweis:

- `common/map_modes/zz_AOEIW_imperial_world_map_mode.txt.disabled` definiert einen separat waehlbaren Scripted Map Mode. Er faerbt Laender nach Fraktion beziehungsweise Ideologie, dimmt Untertanen mit `alpha = 0.68` und verwendet `far_text = faction`. Diese Darstellung entspricht dem Screenshot nicht.
- `common/map_modes/rt56_custom_map_modes.txt.disabled` definiert einen separat waehlbaren Core/Claim-Modus mit Gruen, Violett, Cyan und Rot. Auch diese Darstellung entspricht dem Screenshot nicht.
- Commit `d6e17564` benannte den AOE-Modus von `.txt` nach `.txt.disabled` um. Commit `b9098890` deaktivierte zusaetzlich den RT56-Modus, die AOE-Spielregel und das AOE-Map-Mode-GFX. Im installierten Build existiert ausser `documentation.txt` keine aktive `.txt`-Datei unter `common/map_modes`; die frische Engine-Logdatei enthaelt keinen Treffer auf diese Modi.
- Die Deaktivierung entfernt die waehlbaren Buttons und Overlays. Sie veraendert den normalen politischen Kartenmodus nicht. Ein normaler Vorher/Nachher-Screenshot darf daher allein durch diese Deaktivierung gleich aussehen. Die fruehere Annahme, damit werde der gemalte Standardlook ausgeschaltet, war falsch.

### Tatsaechliche Ursache des dunklen, gemalten Looks

Die wichtigste Ursache ist `gfx/FX/standardfuncsgfx.fxh`. Gegenueber der aktuellen Vanilla-Datei ersetzt die Mod die normale Tag-/Nachtberechnung durch einen festen Wert:

```text
return 0.42f;
```

Der Kommentar nennt dies ausdruecklich eine permanente Daemmerungsdarstellung. Dadurch bleiben Terrain, Stadtlichter und Schattierung auch am Tag in einem dunklen Abend-Look.

`common/defines/zz_AOEIW_graphics.lua` verstaerkt den Effekt. Die Datei nennt sich selbst `Dark strategic-atlas presentation` und setzt:

- Country saturation `0.54` statt Vanilla `0.60`;
- Country brightness `0.76` statt Vanilla `0.80`;
- Border width `1.80` statt Vanilla `1.50`;
- Country gradient thickness `6/27` statt Vanilla `5/25`.

Die Mod liefert ausserdem eigene Terrain-Assets. Der staerkste Bildunterschied gegen Vanilla liegt in `map/terrain/mud_diffuse_rgb_gloss_a_0.dds` mit rund 24–25 mittlerer absoluter RGB-Abweichung. `atlas0.dds` weicht lokal sichtbar ab. Die Welt- und Wasser-Colormaps sind im Pixelvergleich dagegen fast identisch und erklaeren den starken Dunkellook nicht.

### Empfohlener, enger Rendering-Fix

1. In `gfx/FX/standardfuncsgfx.fxh` die feste Daemmerung entfernen und die aktuelle Vanilla-Funktion `DayNightFactor(vGlobeNormal, FEATHER_MIN, FEATHER_MAX)` wiederherstellen.
2. In `common/defines/zz_AOEIW_graphics.lua` die erzwungenen Helligkeits-, Saettigungs- und Grenzwerte entfernen, damit Vanilla-Werte gelten. `CITY_SPRAWL_SHRINK_DISTANCE` kann getrennt bewertet werden.
3. Danach einen A/B-Screenshot im normalen politischen Kartenmodus anfertigen. Nur falls der Look danach noch zu gemalt ist, `mud_diffuse_rgb_gloss_a_0.dds` und gegebenenfalls `atlas0.dds` auf aktuelle Vanilla-Assets zurueckfallen lassen.
4. `terrain.bmp` und `world_normal.bmp` nicht durch Vanilla ersetzen; sie gehoeren zur RT56-Kartengeometrie und sind kein sicherer kosmetischer Tausch.

## 2. Arabische State-Konturen

Die aktuelle Zuordnung besteht nicht aus zersplitterten oder nur ueber Einzelprovinzen verbundenen Fragmenten.

| Einheit | Aktuelle States | Graphbefund |
|---|---|---|
| `SAU` — Emirat Zentralarabien | 292 Nejd, 675 Al Hajara, 678 Rub al Khali, 854 Jawf, 857 Ha'il, 858 Najiran, 859 Dammam | sieben States, eine zusammenhaengende Landkomponente; jeder State grenzt an mindestens einen weiteren SAU-State |
| `OMA` — Koenigreich Hedschas | 679 Hejaz, 855 Tabuk, 856 Asir-Makkah, 1022 Maan | vier States, eine zusammenhaengende Landkomponente; 1022 ist ueber 855 und 856 ueber 679 angebunden |
| `ENG` — Oman/Dhofar | 294 Oman, 979 Khasab, 1102 Inner Oman, 1103 Dhofar | britische Kuesten-/Protektoratsgebiete wie beauftragt |

Die unregelmaessige Kontur entsteht aus den vorhandenen RT56-State- und Provinzgrenzen sowie der starken Terrain-/Gradientendarstellung. Eine Owner-Umverteilung kann diese Grenzlinie nur verschieben, nicht glaetten. Die China-Bloecke wirken kompakter, weil ihre States grossflaechiger geschnitten sind und ihre Farbe/Glow-Darstellung staerker zusammenfasst.

### Vorher/Nachher-Vorschlag

Fuer Zentralarabien und Hedschas wird keine State-Uebertragung empfohlen:

- Vorher: SAU sieben zusammenhaengende States; OMA vier zusammenhaengende States.
- Nachher: dieselben States. Der Umriss bleibt geografisch und loreseitig korrekt; der Rendering-Fix reduziert den kuenstlich betonten fransigen Eindruck.

Das Entfernen von 675/854 oder 1022 wuerde lediglich Al Hajara/Jawf beziehungsweise Maan an das Osmanische Reich zurueckgeben und die im Referenzbild gewuenschte Nordausdehnung der arabischen Staaten abschneiden. Es loest keinen technischen Fragmentierungsfehler.

## 3. Verbindlich genannte Pazifik-States

Diese sechs Uebertragungen sind klar und bilden zusammenhaengende Gebiete. Sie sind noch nicht umgesetzt, damit die geforderte Vorher/Nachher-Uebersicht zuerst geprueft werden kann.

| State | Vorher | Vorgeschlagenes Nachher | Core-Status |
|---|---|---|---|
| 634 Solomon Islands | ENG Owner/Core | AST Owner/Controller | australisch verwaltetes Gebiet, kein AST-Core |
| 1096 Kaiser Wilhelmsland | ENG Owner/Core | AST Owner/Controller | australisch verwaltetes Gebiet, kein AST-Core; grenzt direkt an AST-State 523 New Guinea |
| 1136 Auckland | ENG Owner/Core | NZL Owner/Controller/Core | neuseelaendisches Kernland; grenzt an NZL-State 284 |
| 1139 Marlborough | ENG Owner/Core | NZL Owner/Controller/Core | neuseelaendisches Kernland; grenzt an 723 |
| 723 Southern Island | ENG Owner/Core | NZL Owner/Controller/Core | neuseelaendisches Kernland; verbindet 1139 und 1140 |
| 1140 Otago | ENG Owner/Core | NZL Owner/Controller/Core | neuseelaendisches Kernland; grenzt an 723 |

Bei der Umsetzung werden die ENG-Cores entfernt. Australien erhaelt auf den beiden Mandats-/Verwaltungsgebieten bewusst keine Cores; Neuseeland erhaelt auf seinen vier Heimatstates Cores.

# Tools

Übersicht aller TBk-Werkzeuge in der QGIS-Verarbeitungswerkzeugkiste, gegliedert nach den Gruppen, wie sie dort erscheinen. Innerhalb von **c**, **d** und **e** sind die Kern-Werkzeuge zusätzlich durchnummeriert (`1`, `2`, `3`, …) — das entspricht ihrer typischen Reihenfolge im [Generate-BK-Workflow](workflows.md).

## a — Main Workflows

Fertige Gesamt-Workflows, die mehrere Einzelwerkzeuge automatisch in der richtigen Reihenfolge ausführen. Für den Normalfall reicht es, direkt eines dieser beiden Werkzeuge zu verwenden, statt die Einzelschritte manuell auszuführen.

| Werkzeug | Beschreibung |
| --- | --- |
| **Generate BK** | Haupt-Workflow: erzeugt aus VHM/MG-Rastern und Perimeter die fertige Bestandeskarte. Details siehe [Workflows](workflows.md). |
| **Generate BK Regionwise** | Wie *Generate BK*, aber unterteilt den Perimeter anhand eines Attributfelds in Teilregionen, verarbeitet diese einzeln und führt die Ergebnisse anschliessend wieder zusammen. Damit lassen sich Bestandesgrenzen an vorgegebenen Regionen ausrichten (z.B. Erschliessungseinheiten, Eigentümer- oder Erschliessungsgrenzen) — der Perimeter muss dafür vorher bereits in diese Regionen aufgeteilt sein. Details: [Workflows](workflows.md#variante-generate-bk-regionwise). |

## b — Preprocessing

Bereitet Rohdaten zu den Raster-Eingaben auf, die *Generate BK* benötigt.

| Werkzeug | Beschreibung |
| --- | --- |
| **TBk prepare VHM (and MG)** | Verarbeitet das Vegetationshöhenmodell (VHM) und optional den Nadelholzanteil-Raster (Mischungsgrad/MG) zu den für *Generate BK* benötigten Eingaben: `VHM_detail`, `VHM_10m`, `VHM_150cm`, `MG_10m`, `MG_10m_binary`. ⚠️ Zur Skalierung des Mischungsgrads (0–10'000 vs. 0–100, Laub-/Nadelholz-Richtung) siehe [Achtung-Box in Workflows](workflows.md#phase-1-preprocessing). |

## c — Stand Delineation (Core)

Der eigentliche Kern-Algorithmus: pixelweise Klassifikation anhand des Vegetationshöhenmodells, anschliessend Polygonisierung.

| Werkzeug | Beschreibung |
| --- | --- |
| **1 Delineate Stand** | Bestandes-Klassifikation anhand eines Vegetationshöhen-Rasters (üblicherweise ein 10×10m-Maximalhöhen-Raster aus LiDAR- oder Stereo-Luftbildkorrelation-Daten). Ergebnis: rohe, klassifizierte Bestandespolygone. |
| **2 Simplify and Clean** | Bereinigt die rohe Klassifikation: eliminiert Polygone unterhalb der Mindestfläche **unbedingt** (wird immer in den flächenmässig grössten Nachbarn gemergt, unabhängig von der Höhenähnlichkeit) und vereinfacht die Bestandesgrenzen anhand der Vereinfachungstoleranz. |

## d — Postprocessing Geometry

Geometrische Nachbearbeitung der klassifizierten Bestände.

| Werkzeug | Beschreibung |
| --- | --- |
| **3 Merge similar neighbours** | Vereinigt kleine Bestände mit einem benachbarten Bestand ähnlicher Oberhöhe (hdom) — im Unterschied zu *Simplify and Clean* nur, wenn sich die hdom-Werte innerhalb der Toleranz ähneln; unähnliche kleine Bestände bleiben unverändert. Iteriert, bis keine Kandidaten mehr infrage kommen. |
| **3b Merge similar neighbours graph-based** | Graph-basierte Alternative zu *Merge similar neighbours*: baut einen Ähnlichkeitsgraphen (Kanten zwischen kleinen Beständen und ähnlichen, angrenzenden Nachbarn) und löst zusammenhängende Komponenten in einem einzigen Durchgang auf. Unterschied zum iterativen Ansatz: eine Kette kleiner Bestände zwischen zwei ähnlichen grossen Beständen wird in einem Schritt vereinigt statt über mehrere Durchläufe. |
| **4 Clip to perimeter and eliminate gaps** | Schneidet das Ergebnis auf den Projektperimeter zu und schliesst dabei entstehende Lücken. |

## e — Postprocessing Attributes

Berechnet und ergänzt die inhaltlichen Attribute der Bestandeskarte.

| Werkzeug | Beschreibung |
| --- | --- |
| **5 Calculate crown coverage** | Berechnet den Deckungsgrad (DG) je Bestand aus dem 150cm-VHM. |
| **6 Add coniferous proportion** | Ergänzt den Nadelholzanteil (NH, in %) je Bestand aus dem Mischungsgrad-Raster. |
| **Append stand attributes** | Ergänzt weitere Bestandes-Attribute (Vegetationszone, Waldstandort) per räumlichem Join. |

## f — Additional Modules

Optionale Zusatzmodule, die üblicherweise **nach** dem Hauptworkflow auf eine bereits erzeugte Bestandeskarte angewendet werden.

| Werkzeug | Beschreibung |
| --- | --- |
| **TBk postprocess local density** | Erkennt innerhalb der Bestandespolygone Zonen unterschiedlicher lokaler Dichte (Deckungsgrad-Klassen), z.B. um besonders dichte oder lückige Teilflächen abzugrenzen. Konfigurierbare Prozent-Schwellen und Fenster-Radien je Klasse; kleine Löcher/Splitter werden gefiltert, optional geglättet ("buffer smoothing"). |
| **TBk postprocess ddom SD estimate** | Schätzt den dominanten Brusthöhendurchmesser (ddom) und darauf aufbauend die Entwicklungsstufe (SD/Stade de développement) aus hdom, Nadelholzanteil (NH) und Waldstandort/Bonität. |
| **TBk postprocess V estimate** | Schätzt den Vorrat (Volumen) aus hdom, Deckungsgrad (DG) und Nadelholzanteil (NH). |
| **TBk postprocess OS Change** | Berechnet die Veränderung der Oberschicht zwischen zwei TBk-Kartenständen (Entwicklung der Deckungsgrad-Ebene, `dg_layer`). |
| **TBk WIS.2 Web prep export (KML)** | Bereitet eine Bestandeskarte für den Export nach WIS.2 Web auf. |
| **TBk WIS.2 Desktop export (XML)** | Exportiert eine erzeugte Bestandeskarte für WIS.2 Desktop. |
| **TBk WIS.2 Web import CSV** | Importiert Daten aus einem WIS.2-Web-CSV-Export. |

!!! note "Nicht in dieser Übersicht"
    Die Gruppen **g Utility** (z.B. Projekt-/Layout-Erstellung, Merge mehrerer Bestandeskarten, generischer räumlicher Join — inkl. *Tree species from raster*, das trotz Ablage im Quellcode bei den Attribut-Tools UI-seitig unter Utility läuft) und **y Legacy** (Vorgänger-Werkzeuge vor der Modularisierung) sind nicht Teil dieser ersten Fassung der technischen Dokumentation.

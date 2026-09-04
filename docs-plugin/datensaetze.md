# Datensätze

## Benötigte Eingabedaten

| Datensatz | Typ | Anforderung |
| --- | --- | --- |
| **Projektperimeter** ("Waldmaske") | Vektor (Polygon) | Deckt das gesamte zu verarbeitende Waldgebiet ab. Muss **frei von Geometrie-/Topologiefehlern** sein (keine doppelten Knoten, Überlappungen, Lücken) — sonst bricht der Algorithmus ab. Besonders fehleranfällig bei Multipolygonen mit vielen kleinen Teilen (z.B. wenn Waldwege aus dem Perimeter ausgeschnitten sind). |
| **Vegetationshöhenmodell (VHM)** | Raster | Auflösung ≤ 1.5 m, deckt den gesamten Perimeter ab. Quelle z.B. LiDAR oder Stereo-Luftbildkorrelation. Wird vom Preprocessing-Tool auf die Auflösungen 10×10m (Bestandesbildung) und 1.5×1.5m (Ermittlung Deckungsgrad) skaliert und mit dem Mischungsgrad-Raster gemeinsam ausgerichtet. |
| **Mischungsgrad (MG)** | Raster (optional) | Werte 0–100, beschreiben den Nadelholzanteil in % pro Pixel. Wird vom Preprocessing-Tool gemeinsam mit dem 10×10m-VHM-Raster ausgerichtet. Rohdaten liegen oft in anderer Skalierung/Richtung vor — siehe [Achtung: Skalierung des Mischungsgrads](anwendung.md#wo-finde-ich-die-werkzeuge) beim Preprocessing. |

Alle Eingabedaten müssen korrekt georeferenziert sein (keine Projektionsfehler) und NoData korrekt definiert haben. Sie müssen nicht zwingend im selben Koordinatensystem vorliegen, es wird aber empfohlen, vorher alle Daten in dasselbe System zu projizieren.

### Geometrie-Fehlerprüfung (Perimeter)

In QGIS mit den Standard-Werkzeugen **Check Validity** und **Repair Geometries** prüfen und viele einfache Fehler direkt korrigieren.

## Von TBk erzeugte Zwischen-/Eingabedaten

Das [Preprocessing-Werkzeug](workflows.md#phase-1-preprocessing) erzeugt aus den Rohdaten die eigentlichen Eingaben für *Generate BK*:

| Datei | Beschreibung |
| --- | --- |
| `VHM_detail.tif` | Hochaufgelöstes VHM (Zwischenschritt) |
| `VHM_10m.tif` | VHM aggregiert auf 10×10m — Haupteingabe für die Bestandesabgrenzung |
| `VHM_150cm.tif` | VHM in 150cm-Auflösung — für die Deckungsgrad-Berechnung |
| `MG_10m.tif` | Mischungsgrad, ausgerichtet auf das 10m-VHM (nur falls MG-Eingabe vorhanden) |
| `MG_10m_binary.tif` | Binarisierter Mischungsgrad (nur falls MG-Eingabe vorhanden) |

## Ausgabedaten

| Datei | Beschreibung |
| --- | --- |
| `TBk_Bestandeskarte.gpkg` | Hauptergebnis: die Bestandeskarte mit Attributen zu Oberhöhe (hdom), Maximalhöhe (hmax), Deckungsgrad, Mischungsverhältnis und Grundstruktur |
| `TBk_Project.qgz` | QGIS-Projekt zur Visualisierung, inkl. 4 vordefinierten Drucklayouts (A1/A3, Hoch-/Querformat) |

Details zur inhaltlichen Bedeutung der Attribute: siehe [inhaltliche Dokumentation ↗](https://HAFL-WWI.github.io/TBk-Docs/tbk/).

## Konfiguration über TOML-Dateien

Alle Werkzeuge akzeptieren alternativ eine `.toml`-Konfigurationsdatei (Parameter `config_file`), deren Werte alle im Dialog gesetzten Parameter überschreiben. Die wichtigsten gemeinsamen Schlüssel (siehe `default_input_config.toml` im Plugin-Repository):

```toml
vhm_10m = ""                              # VHM 10m, Haupteingabe
vhm_150cm = ""                            # VHM 150cm, für Deckungsgrad
coniferous_raster = ""                    # Mischungsgrad-Raster für Bestandesmittel
coniferous_raster_for_classification = "" # Mischungsgrad-Raster für Klassifikation
perimeter = ""                            # Perimeter zum Zuschneiden
output_root = ""                          # Ausgabeordner
del_tmp = true                            # Temporäre Dateien/Felder löschen
```

Für die Reproduzierbarkeit generieren die [Workflows](workflows.md) selbst eine direkt einsetzbare Config-Datei mit den tatsächlich verwendeten Parametern des jeweiligen Laufs. Aus technischen Gründen müssen die obligatorischen Parameter dabei trotzdem im UI-Dialog (mit beliebigen Werten) ausgefüllt werden — sie werden anschliessend durch die Werte aus der Config-Datei überschrieben, sofern eine solche übergeben wird.

Nützlich, um Läufe reproduzierbar zu machen oder Verarbeitungen ausserhalb der QGIS-Oberfläche zu automatisieren.

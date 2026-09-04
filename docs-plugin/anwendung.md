# Anwendung

## Wo finde ich die Werkzeuge?

Nach der Installation erscheinen alle TBk-Werkzeuge im QGIS-Fenster **Verarbeitungswerkzeugkiste** (Processing Toolbox) unter dem Provider **TBk**. Dort sind sie in sechs (plus zwei interne) Gruppen gegliedert, die auch alphabetisch sortiert sind, damit sie in typischer Bearbeitungsreihenfolge erscheinen:

- **a Main Workflows** — fertige Gesamt-Workflows
- **b Preprocessing** — Eingabedaten aufbereiten
- **c Stand Delineation (Core)** — Kern-Algorithmus zur Bestandesabgrenzung
- **d Postprocessing Geometry** — Geometrie nachbearbeiten
- **e Postprocessing Attributes** — Attribute berechnen/ergänzen
- **f Additional Modules** — optionale Zusatzmodule

Details zu den einzelnen Werkzeugen: siehe [Tools](tools.md). Typische Reihenfolge/Zusammenspiel der Werkzeuge: siehe [Workflows](workflows.md).

!!! warning "Achtung: Skalierung des Mischungsgrads (MG) beim Preprocessing"
    Das Preprocessing-Werkzeug ([TBk prepare VHM (and MG)](tools.md#b-preprocessing)) erwartet den Mischungsgrad standardmässig mit Werten **0–10'000** (Default des LFI-Mischungsgrads), wobei 10'000 einem Nadelholzanteil von 100.00 % entspricht. Das steuert der erweiterte Parameter **„Rescale Forest mixture degree values“** (Default: `100`).

    - Enthält das Eingaberaster bereits Werte **0–100**: den Faktor von `100` auf `1` setzen (keine Skalierung).
    - Zeigt das Eingaberaster stattdessen den **Laubholz**-Anteil (100 = 100 % Laubholz / 0 % Nadelholz) statt des Nadelholz-Anteils: das Raster vorher mit `100 − Rasterwert` umkehren, bevor es als Eingabe verwendet wird.

## Grundlegende Bedienung

Jedes TBk-Werkzeug ist ein normaler QGIS-Verarbeitungsalgorithmus:

1. Werkzeug in der Toolbox doppelklicken (öffnet den Parameter-Dialog)
2. Eingabe-Layer/Parameter setzen
3. Bei Bedarf **Erweiterte Parameter** aufklappen (meist mit sinnvollen Voreinstellungen, in der Regel nicht nötig zu ändern)
4. **Ausführen**

Da die Werkzeuge normale Processing-Algorithmen sind, lassen sie sich auch in der **QGIS-Python-Konsole** (`processing.run(...)`) oder im **Model Designer** verwenden — z.B. um eigene Varianten der Standard-Workflows zusammenzustellen.

## Speicherort der Ausgabe

Bei den meisten Werkzeugen muss ein **Ausgabeordner** angegeben werden — wird dieser nicht gesetzt, landet das Ergebnis in einem temporären Ordner und ist schwer wiederzufinden.

Der Hauptworkflow ([Generate BK](workflows.md)) legt standardmässig einen Zeitstempel-Unterordner an:

```
{Ausgabeordner}/{YYYYMMDD-HHMM}/
├── TBk_Bestandeskarte.gpkg      Ergebnis: die Bestandeskarte
├── TBk_Project.qgz              QGIS-Projekt zur Visualisierung
├── bk_process/                  Zwischenergebnisse
└── dg_layers/                   Deckungsgrad-Rasterebenen
```

Das Anlegen des Zeitstempel-Unterordners lässt sich über den erweiterten Parameter **„Create subfolder with timestamp“** deaktivieren.

## Aufräumen temporärer Daten

Die Checkbox **„Delete temporary files and fields“** ist standardmässig aktiviert und löscht Zwischenergebnisse/-felder nach erfolgreichem Lauf. Für Debugging kann es hilfreich sein, sie zu deaktivieren, um Zwischenschritte zu inspizieren.

## Konfiguration über TOML-Dateien (fortgeschritten)

Alle Parameter eines Werkzeugs lassen sich alternativ über eine **`.toml`-Konfigurationsdatei** setzen (Parameter `config_file`). Werte aus der Datei überschreiben dabei alle im Dialog gesetzten Werte. Das ist nützlich, um Läufe reproduzierbar zu machen oder Batch-Verarbeitungen ausserhalb der QGIS-Oberfläche zu steuern. Die Struktur der TOML-Datei entspricht direkt den Parameternamen der Werkzeuge — siehe [Datensätze](datensaetze.md) für die wichtigsten Schlüssel.

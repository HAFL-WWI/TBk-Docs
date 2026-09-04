# Installation

## Voraussetzungen

- **QGIS ≥ 3.10** (empfohlen: eine aktuelle LTR-Version)
- **GRASS** und der **GRASS-Provider** müssen in QGIS installiert und aktiviert sein (Einstellungen → Erweiterungen/Plugin-Verwaltung)

!!! warning "Lokal statt Netzlaufwerk/Cloud arbeiten"
    Ein- und Ausgabedaten sollten **lokal** liegen, nicht auf einem Netzlaufwerk oder Cloud-Speicher (OneDrive, etc.). Bei synchronisierten Ordnern kann es vorkommen, dass (temporäre) Ausgabedateien nicht geschrieben oder gelesen werden können, was zu schwer nachvollziehbaren Fehlern führt.

## Zwei Versionen

| Version | Beschreibung |
| --- | --- |
| **TBk Plugin** (aktuell) | Neueste Version, wird laufend aktualisiert. Enthält alle Funktionen inkl. der regionsweisen Berechnung. Download: *[TBk Plugin Download-Link — TODO: URL ergänzen]* |
| **TBk Core** (stabil) | Bewährte Version mit allen Funktionen bis Oktober 2025, getestet mit QGIS 3.16–3.44. Wird **nicht mehr weiterentwickelt** und enthält **keine** regionsweise Berechnung. Kann **parallel** zur aktuellen Version installiert werden. Download: *[TBk Core Download-Link — TODO: URL ergänzen]* |

!!! note "TODO"
    Die konkreten Download-Links fehlen noch hier (aus der Zwischenablage gingen beim Einfügen nur die Link-Texte, nicht die URLs mit). Bitte die zwei Links nachtragen.

## Installation als ZIP-Datei

Das Plugin wird als ZIP-Datei installiert:

1. In QGIS: **Erweiterungen → Erweiterungen verwalten und installieren…**
2. Reiter **Aus ZIP-Datei installieren**
3. Heruntergeladene `.zip`-Datei auswählen und installieren

Nach der Installation erscheinen die TBk-Werkzeuge in der **Verarbeitungswerkzeugkiste** (Processing Toolbox) unter dem Provider **TBk**, gegliedert in die Gruppen a–f (siehe [Tools](tools.md)).

Da TBk Plugin und TBk Core parallel installiert werden können, tauchen ggf. beide Provider gleichzeitig in der Toolbox auf — am Namen der Gruppe/des Providers unterscheidbar.

# TBk-Docs

Prototyp der TBk-Dokumentation auf Basis von [MkDocs](https://www.mkdocs.org/) + [Material](https://squidfunk.github.io/mkdocs-material/).

Migriert schrittweise das bestehende Handbuch (`H07_TBk/01_TBk/Dokumentation/Handbuch/TBk_Manuel_V11_*.docx`) in eine versionierte, mehrsprachige (DE/FR/EN) Online-Dokumentation mit PDF-Export.

Hintergrund/Entscheidungen: siehe `H07_TBk/01_TBk/Dokumentation/H07_TBk_doc.md` (Sublog).

## Zwei getrennte Dokumentationen

Dieses Repo baut **zwei unabhängige MkDocs-Sites** aus zwei Configs, damit inhaltliche und technische Doku getrennt navigierbar sind und je ein eigenes PDF exportieren:

| Config              | Quelle       | Inhalt                                                              | Live-URL               |
| -------------------- | ------------ | -------------------------------------------------------------------- | ------------------------ |
| `mkdocs.yml`          | `docs/`        | Inhaltliche Doku (TBk-Karten, Grundlagen, Abgrenzung, Datenquellen) | `.../TBk-Docs/tbk/`        |
| `mkdocs-plugin.yml`   | `docs-plugin/` | Technische Doku (Installation, Anwendung, Tools, Workflows, Datensätze) | `.../TBk-Docs/tbk-plugin/` |

Beide Sites verlinken sich gegenseitig über einen Tab am Ende der Navigation ("Technische Doku ↗" / "Inhaltliche Doku ↗"). Die Root-URL (`landing/index.html`) zeigt eine einfache Übersichtsseite mit Links auf beide.

## Lokal entwickeln

```bash
pip install -r requirements.txt
mkdocs serve                       # inhaltliche Doku (docs/)
mkdocs serve -f mkdocs-plugin.yml -a 127.0.0.1:8001   # technische Doku (docs-plugin/), eigener Port
```

Öffnet auf http://127.0.0.1:8000/ bzw. http://127.0.0.1:8001/

## Mehrsprachigkeit

Jede Seite kann sprachspezifische Varianten haben: `seite.md` (Default/Deutsch), `seite.fr.md`, `seite.en.md`. Fehlt eine Übersetzung, wird automatisch auf die Default-Sprache zurückgefallen ([mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/)).

## Bilder & PDFs einbinden

- Einzelne Grafiken (z.B. aus PowerPoint-Folien exportiert): als PNG unter `docs/assets/img/<kapitel>/` ablegen, per `![Alt](assets/img/<kapitel>/datei.png)` einbinden.
- Grössere Ressourcen (ganze Dokumente): als PDF unter `docs/assets/pdf/` ablegen und verlinken oder per `<iframe>` einbetten.
- Beide Ordner sind über [Git LFS](https://git-lfs.com/) getrackt (siehe `.gitattributes`) — Binärdaten blähen die normale Git-History nicht auf.

## PDF-Export

Automatisch beim Build via `mkdocs-to-pdf`-Plugin, je Config ein eigenes PDF:
- Inhaltliche Doku: `dist/tbk/pdf/tbk-dokumentation.pdf` (Config `mkdocs.yml`)
- Technische Doku: `dist/tbk-plugin/pdf/tbk-plugin-dokumentation.pdf` (Config `mkdocs-plugin.yml`)

## Deployment

GitHub Actions Workflow (`.github/workflows/deploy.yml`) baut bei jedem Push auf `main` beide Configs in `dist/tbk/` bzw. `dist/tbk-plugin/`, kopiert die Landingpage nach `dist/index.html` und deployt `dist/` als Ganzes nach GitHub Pages.

## Migration aus dem Handbuch (docx)

`scripts/migrate_handbuch.py` migriert Text + Abbildungen aus `Handbuch/TBk_Manuel_V11_DE.docx` und `_FR.docx` direkt in die entsprechenden `docs/*.md`/`*.fr.md`-Dateien (überschreibt bestehende Inhalte). Nützlich, um nach einer Handbuch-Aktualisierung neu zu migrieren. Vergleicht dabei automatisch die Bilder-Anzahl pro Kapitel zwischen DE/FR und warnt bei Abweichungen (kann auf echte Lücken im Quelldokument hinweisen, vgl. Migrations-Hinweis in `datenquellen/vhm.md`). `scripts/align_tables.py <datei.md>` richtet danach alle Markdown-Tabellen im Rohtext aus.

```bash
python scripts/migrate_handbuch.py
for f in $(find docs -name "*.md"); do python scripts/align_tables.py "$f"; done
```

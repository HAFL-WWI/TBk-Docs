# TBk-Docs

Prototyp der TBk-Dokumentation auf Basis von [MkDocs](https://www.mkdocs.org/) + [Material](https://squidfunk.github.io/mkdocs-material/).

Migriert schrittweise das bestehende Handbuch (`H07_TBk/01_TBk/Dokumentation/Handbuch/TBk_Manuel_V11_*.docx`) in eine versionierte, mehrsprachige (DE/FR/EN) Online-Dokumentation mit PDF-Export.

Hintergrund/Entscheidungen: siehe `H07_TBk/01_TBk/Dokumentation/H07_TBk_doc.md` (Sublog).

## Lokal entwickeln

```bash
pip install -r requirements.txt
mkdocs serve
```

Öffnet auf http://127.0.0.1:8000/

## Mehrsprachigkeit

Jede Seite kann sprachspezifische Varianten haben: `seite.md` (Default/Deutsch), `seite.fr.md`, `seite.en.md`. Fehlt eine Übersetzung, wird automatisch auf die Default-Sprache zurückgefallen ([mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/)).

## Bilder & PDFs einbinden

- Einzelne Grafiken (z.B. aus PowerPoint-Folien exportiert): als PNG unter `docs/assets/img/<kapitel>/` ablegen, per `![Alt](assets/img/<kapitel>/datei.png)` einbinden.
- Grössere Ressourcen (ganze Dokumente): als PDF unter `docs/assets/pdf/` ablegen und verlinken oder per `<iframe>` einbetten.
- Beide Ordner sind über [Git LFS](https://git-lfs.com/) getrackt (siehe `.gitattributes`) — Binärdaten blähen die normale Git-History nicht auf.

## PDF-Export

Automatisch beim Build via `mkdocs-to-pdf`-Plugin (siehe `mkdocs.yml`), Output unter `site/pdf/tbk-dokumentation.pdf`.

## Deployment

GitHub Actions Workflow (`.github/workflows/deploy.yml`) baut und deployt bei jedem Push auf `main` automatisch nach GitHub Pages.

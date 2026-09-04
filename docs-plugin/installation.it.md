# Installazione

## Requisiti

- **QGIS ≥ 3.10** (si raccomanda una versione LTR attuale)
- **GRASS** e il **provider GRASS** devono essere installati e attivati in QGIS (Impostazioni → Gestisci/Installa estensioni)

!!! warning "Lavorare in locale invece che su un'unità di rete/cloud"
    I dati di input e output dovrebbero trovarsi **in locale**, non su un'unità di rete o uno spazio cloud (OneDrive, ecc.). Con cartelle sincronizzate può succedere che i file di output (temporanei) non possano essere scritti o letti, causando errori difficili da interpretare.

## Due versioni

| Versione | Descrizione |
| --- | --- |
| **TBk Plugin** (attuale) | Versione più recente, aggiornata continuamente. Contiene tutte le funzionalità, incluso il calcolo per regioni. [Download ↗](https://nextcloud.bfh.science/index.php/s/Fmmr55zssrLAnfH) |
| **TBk Core** (stabile) | Versione consolidata con tutte le funzionalità fino a ottobre 2025, testata con QGIS 3.16–3.44. **Non più sviluppata** e **priva** del calcolo per regioni. Può essere installata **in parallelo** alla versione attuale. [Download ↗](https://nextcloud.bfh.science/index.php/s/Pw46A2GCqMDt2Gn) |

## Installazione come file ZIP

Il plugin si installa come file ZIP:

1. In QGIS: **Estensioni → Gestisci e installa estensioni…**
2. Scheda **Installa da ZIP**
3. Selezionare il file `.zip` scaricato e installarlo

Dopo l'installazione, gli strumenti TBk compaiono nella **cassetta degli strumenti di elaborazione** (Processing Toolbox) sotto il provider **TBk**, organizzati nei gruppi a–f (vedi [Strumenti](tools.md)).

Poiché TBk Plugin e TBk Core possono essere installati in parallelo, entrambi i provider possono comparire contemporaneamente nella cassetta degli strumenti — distinguibili dal nome del gruppo/provider.

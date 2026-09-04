# Utilizzo

## Dove trovo gli strumenti?

Dopo l'installazione, tutti gli strumenti TBk compaiono nella **cassetta degli strumenti di elaborazione** (Processing Toolbox) di QGIS, sotto il provider **TBk**. Qui sono organizzati in sei gruppi (più due interni), ordinati anche alfabeticamente in modo da apparire nel tipico ordine di elaborazione:

- **a Main Workflows** — workflow completi già pronti
- **b Preprocessing** — preparazione dei dati di input
- **c Stand Delineation (Core)** — algoritmo centrale per la delimitazione dei popolamenti
- **d Postprocessing Geometry** — post-elaborazione della geometria
- **e Postprocessing Attributes** — calcolo/aggiunta di attributi
- **f Additional Modules** — moduli aggiuntivi opzionali

Dettagli sui singoli strumenti: vedi [Strumenti](tools.md). Ordine tipico/interazione degli strumenti: vedi [Workflow](workflows.md).

## Funzionamento di base

Ogni strumento TBk è un normale algoritmo di elaborazione di QGIS:

1. Fare doppio clic sullo strumento nella cassetta degli strumenti (apre la finestra dei parametri)
2. Impostare i layer/parametri di input
3. Se necessario, espandere i **parametri avanzati** (di solito con valori predefiniti sensati, generalmente non serve modificarli)
4. **Eseguire**

Poiché gli strumenti sono normali algoritmi di elaborazione, possono essere utilizzati anche dalla **console Python di QGIS** (`processing.run(...)`) o nel **Model Designer** — ad esempio per comporre proprie varianti dei workflow standard.

## Posizione dell'output

La maggior parte degli strumenti richiede l'indicazione di una **cartella di output** — se non viene impostata, il risultato finisce in una cartella temporanea ed è difficile da ritrovare.

Il workflow principale ([Generate BK](workflows.md)) crea per default una sottocartella con timestamp:

```
{cartella di output}/{YYYYMMDD-HHMM}/
├── TBk_Bestandeskarte.gpkg      Risultato: la carta dei popolamenti
├── TBk_Project.qgz              Progetto QGIS per la visualizzazione
├── bk_process/                  Risultati intermedi
└── dg_layers/                   Layer raster del grado di copertura
```

La creazione della sottocartella con timestamp può essere disattivata tramite il parametro avanzato **"Create subfolder with timestamp"**.

## Pulizia dei dati temporanei

La casella **"Delete temporary files and fields"** è attivata per default ed elimina risultati/campi intermedi dopo un'esecuzione riuscita. Per il debug può essere utile disattivarla per ispezionare i passaggi intermedi.

## Configurazione tramite file TOML (avanzato)

Tutti i parametri di uno strumento possono essere impostati in alternativa tramite un **file di configurazione `.toml`** (parametro `config_file`). I valori del file sovrascrivono tutti i valori impostati nella finestra di dialogo. Utile per rendere le esecuzioni riproducibili o per pilotare elaborazioni batch al di fuori dell'interfaccia QGIS. La struttura del file TOML corrisponde direttamente ai nomi dei parametri degli strumenti — vedi [Dati](datensaetze.md) per le chiavi più importanti.

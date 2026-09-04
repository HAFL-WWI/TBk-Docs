# Dati

## Dati di input richiesti

| Dataset | Tipo | Requisito |
| --- | --- | --- |
| **Perimetro del progetto** ("maschera forestale") | Vettoriale (poligono) | Copre l'intera area forestale da elaborare. Deve essere **privo di errori di geometria/topologia** (nessun nodo duplicato, sovrapposizione, lacuna) — altrimenti l'algoritmo si interrompe. Particolarmente soggetto a errori con multipoligoni composti da molte piccole parti (ad es. quando le strade forestali sono ritagliate dal perimetro). |
| **Modello di altezza della vegetazione (VHM)** | Raster | Risoluzione ≤ 1.5 m, copre l'intero perimetro. Fonte ad es. LiDAR o correlazione di immagini aeree stereoscopiche. Riscalato dallo strumento di preprocessing alle risoluzioni 10×10m (formazione dei popolamenti) e 1.5×1.5m (determinazione del grado di copertura) e allineato insieme al raster del grado di mescolanza. |
| **Grado di mescolanza (MG)** | Raster (opzionale) | Valori 0–100, che descrivono la proporzione di conifere in % per pixel. Allineato dallo strumento di preprocessing insieme al raster VHM 10×10m. I dati grezzi si presentano spesso con una scala/direzione diversa — vedi [Attenzione: scala del grado di mescolanza](workflows.md#fase-1-preprocessing) nel preprocessing. |

Tutti i dati di input devono essere correttamente georeferenziati (nessun errore di proiezione) e avere il NoData definito correttamente. Non devono necessariamente trovarsi nello stesso sistema di coordinate, ma si raccomanda di proiettare in anticipo tutti i dati nello stesso sistema.

### Controllo degli errori di geometria (perimetro)

Verificare in QGIS con gli strumenti standard **Check Validity** e **Repair Geometries**, che correggono direttamente molti errori semplici.

## Dati intermedi/di input generati da TBk

Lo [strumento di preprocessing](workflows.md#fase-1-preprocessing) trasforma i dati grezzi negli input effettivi per *Generate BK*:

| File | Descrizione |
| --- | --- |
| `VHM_detail.tif` | VHM ad alta risoluzione (passaggio intermedio) |
| `VHM_10m.tif` | VHM aggregato a 10×10m — input principale per la delimitazione dei popolamenti |
| `VHM_150cm.tif` | VHM a risoluzione di 150cm — per il calcolo del grado di copertura |
| `MG_10m.tif` | Grado di mescolanza, allineato al VHM 10m (solo se è presente un input MG) |
| `MG_10m_binary.tif` | Grado di mescolanza binarizzato (solo se è presente un input MG) |

## Dati di output

| File | Descrizione |
| --- | --- |
| `TBk_Bestandeskarte.gpkg` | Risultato principale: la carta dei popolamenti con attributi di altezza dominante (hdom), altezza massima (hmax), grado di copertura, rapporto di mescolanza e struttura di base |
| `TBk_Project.qgz` | Progetto QGIS per la visualizzazione, incl. 4 layout di stampa predefiniti (A1/A3, verticale/orizzontale) |

Dettagli sul significato dei contenuti degli attributi: vedi la [documentazione dei contenuti ↗](https://HAFL-WWI.github.io/TBk-Docs/tbk/).

## Configurazione tramite file TOML

Tutti gli strumenti possono in alternativa accettare un file di configurazione `.toml` (parametro `config_file`), i cui valori sovrascrivono tutti i parametri impostati nella finestra di dialogo. Le chiavi comuni più importanti (vedi `default_input_config.toml` nel repository del plugin):

```toml
vhm_10m = ""                              # VHM 10m, input principale
vhm_150cm = ""                            # VHM 150cm, per il grado di copertura
coniferous_raster = ""                    # Raster del grado di mescolanza per la media del popolamento
coniferous_raster_for_classification = "" # Raster del grado di mescolanza per la classificazione
perimeter = ""                            # Perimetro per il ritaglio
output_root = ""                          # Cartella di output
del_tmp = true                            # Eliminare i file/campi temporanei
```

Per la riproducibilità, i [workflow](workflows.md) generano essi stessi un file di configurazione direttamente utilizzabile con i parametri effettivamente usati in quella esecuzione. Per motivi tecnici, i parametri obbligatori devono comunque essere compilati nella finestra di dialogo dell'interfaccia (con valori qualsiasi) — vengono poi sovrascritti dai valori del file di configurazione, se ne viene fornito uno.

Utile per rendere le esecuzioni riproducibili o per automatizzare l'elaborazione al di fuori dell'interfaccia QGIS.

# Strumenti

Panoramica di tutti gli strumenti TBk nella cassetta degli strumenti di elaborazione di QGIS, organizzati secondo i gruppi come vi compaiono. All'interno di **c**, **d** ed **e**, gli strumenti principali sono inoltre numerati (`1`, `2`, `3`, …) — corrispondente al loro ordine tipico nel [workflow Generate BK](workflows.md).

## a — Main Workflows

Workflow completi già pronti, che eseguono automaticamente più strumenti singoli nell'ordine corretto. Nel caso normale è sufficiente usare direttamente uno di questi due strumenti invece di eseguire manualmente i singoli passaggi.

| Strumento | Descrizione |
| --- | --- |
| **Generate BK** | Workflow principale: genera la carta dei popolamenti finale a partire dai raster VHM/MG e da un perimetro. Dettagli: vedi [Workflow](workflows.md). |
| **Generate BK Regionwise** | Come *Generate BK*, ma suddivide il perimetro in sotto-regioni in base a un campo attributo, le elabora singolarmente e infine riunisce nuovamente i risultati. Questo permette di allineare i confini dei popolamenti a regioni predefinite (ad es. unità di esbosco/accesso, confini di proprietà o confini di accesso) — il perimetro deve essere già suddiviso in queste regioni in anticipo. Dettagli: [Workflow](workflows.md#variante-generate-bk-regionwise). |

## b — Preprocessing

Prepara i dati grezzi trasformandoli nei raster di input richiesti da *Generate BK*.

| Strumento | Descrizione |
| --- | --- |
| **TBk prepare VHM (and MG)** | Elabora il modello di altezza della vegetazione (VHM) e, opzionalmente, il raster della proporzione di conifere (grado di mescolanza/MG) negli input richiesti da *Generate BK*: `VHM_detail`, `VHM_10m`, `VHM_150cm`, `MG_10m`, `MG_10m_binary`. ⚠️ Sulla scala del grado di mescolanza (0–10'000 vs. 0–100, direzione latifoglie/conifere) vedi il [riquadro di attenzione in Workflow](workflows.md#fase-1-preprocessing). |

## c — Stand Delineation (Core)

Il vero e proprio algoritmo centrale: classificazione pixel per pixel basata sul modello di altezza della vegetazione, seguita dalla poligonizzazione.

| Strumento | Descrizione |
| --- | --- |
| **1 Delineate Stand** | Classificazione dei popolamenti a partire da un raster di altezza della vegetazione (tipicamente un raster di altezza massima 10×10m da LiDAR o correlazione di immagini aeree stereoscopiche). Risultato: poligoni di popolamento grezzi, classificati. |
| **2 Simplify and Clean** | Ripulisce la classificazione grezza: elimina **incondizionatamente** i poligoni sotto la superficie minima (sempre fusi con il vicino di superficie maggiore, indipendentemente dalla somiglianza di altezza) e semplifica i confini dei popolamenti in base alla tolleranza di semplificazione. |

## d — Postprocessing Geometry

Post-elaborazione geometrica dei popolamenti classificati.

| Strumento | Descrizione |
| --- | --- |
| **3 Merge similar neighbours** | Unisce i piccoli popolamenti a un popolamento vicino di altezza dominante (hdom) simile — a differenza di *Simplify and Clean*, solo se i valori hdom sono simili entro la tolleranza; i piccoli popolamenti dissimili restano invariati. Itera finché non ci sono più candidati idonei. |
| **3b Merge similar neighbours graph-based** | Alternativa basata su grafo a *Merge similar neighbours*: costruisce un grafo di similarità (archi tra piccoli popolamenti e vicini adiacenti simili) e risolve le componenti connesse in un unico passaggio. Differenza rispetto all'approccio iterativo: una catena di piccoli popolamenti tra due grandi popolamenti simili viene unita in un solo passaggio invece che in più passaggi. |
| **4 Clip to perimeter and eliminate gaps** | Ritaglia il risultato sul perimetro del progetto e chiude le eventuali lacune risultanti. |

## e — Postprocessing Attributes

Calcola e completa gli attributi di contenuto della carta dei popolamenti.

| Strumento | Descrizione |
| --- | --- |
| **5 Calculate crown coverage** | Calcola il grado di copertura (DG) per popolamento a partire dal VHM a 150cm. |
| **6 Add coniferous proportion** | Aggiunge la proporzione di conifere (NH, in %) per popolamento a partire dal raster del grado di mescolanza. |
| **Append stand attributes** | Aggiunge ulteriori attributi di popolamento (zona di vegetazione, stazione forestale) tramite join spaziale. |

## f — Additional Modules

Moduli aggiuntivi opzionali, solitamente applicati **dopo** il workflow principale a una carta dei popolamenti già generata.

| Strumento | Descrizione |
| --- | --- |
| **TBk postprocess local density** | Rileva all'interno dei poligoni di popolamento zone di diversa densità locale (classi di grado di copertura), ad es. per delimitare sotto-aree particolarmente dense o rade. Soglie percentuali e raggi della finestra mobile configurabili per classe; piccoli fori/frammenti vengono filtrati, con smussamento opzionale ("buffer smoothing"). |
| **TBk postprocess ddom SD estimate** | Stima il diametro dominante a petto d'uomo (ddom) e, su questa base, lo stadio di sviluppo (SD/Stade de développement) a partire da hdom, proporzione di conifere (NH) e stazione forestale/classe di fertilità. |
| **TBk postprocess V estimate** | Stima la provvigione (volume) a partire da hdom, grado di copertura (DG) e proporzione di conifere (NH). |
| **TBk postprocess OS Change** | Calcola la variazione dello strato superiore tra due stati della carta TBk (evoluzione del layer del grado di copertura, `dg_layer`). |
| **TBk WIS.2 Web prep export (KML)** | Prepara una carta dei popolamenti per l'esportazione verso WIS.2 Web. |
| **TBk WIS.2 Desktop export (XML)** | Esporta una carta dei popolamenti generata per WIS.2 Desktop. |
| **TBk WIS.2 Web import CSV** | Importa dati da un'esportazione CSV di WIS.2 Web. |

!!! note "Non trattati in questa panoramica"
    I gruppi **g Utility** (ad es. creazione di progetti/layout, unione di più carte dei popolamenti, join spaziale generico — incluso *Tree species from raster*, che pur trovandosi nel codice sorgente accanto agli strumenti sugli attributi è classificato lato interfaccia sotto Utility) e **y Legacy** (strumenti predecessori precedenti alla modularizzazione) non fanno parte di questa prima versione della documentazione tecnica.

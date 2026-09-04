# Outils

Aperçu de tous les outils TBk dans la boîte à outils de traitement de QGIS, organisés selon les groupes tels qu'ils y apparaissent. Au sein de **c**, **d** et **e**, les outils centraux sont en plus numérotés (`1`, `2`, `3`, …) — ce qui correspond à leur ordre typique dans le [workflow Generate BK](workflows.md).

## a — Main Workflows

Workflows complets prêts à l'emploi, qui exécutent automatiquement plusieurs outils individuels dans le bon ordre. Dans le cas normal, il suffit d'utiliser directement l'un de ces deux outils plutôt que d'exécuter les étapes individuelles manuellement.

| Outil | Description |
| --- | --- |
| **Generate BK** | Workflow principal : génère la carte des peuplements finale à partir des rasters VHM/MG et d'un périmètre. Détails : voir [Workflows](workflows.md). |
| **Generate BK Regionwise** | Comme *Generate BK*, mais subdivise le périmètre en sous-régions sur la base d'un champ d'attribut, les traite individuellement, puis fusionne à nouveau les résultats. Cela permet d'aligner les limites de peuplements sur des régions prédéfinies (p. ex. unités d'exploitation/desserte, limites de propriété ou limites de desserte) — le périmètre doit pour cela déjà être subdivisé en ces régions au préalable. Détails : [Workflows](workflows.md#variante-generate-bk-regionwise). |

## b — Preprocessing

Prépare les données brutes pour obtenir les rasters d'entrée dont *Generate BK* a besoin.

| Outil | Description |
| --- | --- |
| **TBk prepare VHM (and MG)** | Traite le modèle de hauteur de végétation (VHM) et, en option, le raster de proportion de résineux (degré de mélange/MG) pour obtenir les entrées requises par *Generate BK* : `VHM_detail`, `VHM_10m`, `VHM_150cm`, `MG_10m`, `MG_10m_binary`. ⚠️ Sur la mise à l'échelle du degré de mélange (0–10'000 vs. 0–100, sens feuillus/résineux), voir l'[encadré d'attention dans Workflows](workflows.md#phase-1-preprocessing). |

## c — Stand Delineation (Core)

L'algorithme central proprement dit : classification pixel par pixel à partir du modèle de hauteur de végétation, suivie d'une polygonisation.

| Outil | Description |
| --- | --- |
| **1 Delineate Stand** | Classification des peuplements à partir d'un raster de hauteur de végétation (généralement un raster de hauteur maximale 10×10m issu de LiDAR ou de corrélation d'images aériennes stéréoscopiques). Résultat : polygones de peuplements bruts, classifiés. |
| **2 Simplify and Clean** | Nettoie la classification brute : élimine **inconditionnellement** les polygones sous la surface minimale (toujours fusionnés avec le voisin ayant la plus grande surface, indépendamment de la similarité de hauteur) et simplifie les limites de peuplements selon la tolérance de simplification. |

## d — Postprocessing Geometry

Post-traitement géométrique des peuplements classifiés.

| Outil | Description |
| --- | --- |
| **3 Merge similar neighbours** | Fusionne les petits peuplements avec un peuplement voisin de hauteur dominante (hdom) similaire — contrairement à *Simplify and Clean*, uniquement si les valeurs hdom sont similaires dans la tolérance ; les petits peuplements dissemblables restent inchangés. Itère jusqu'à ce qu'il n'y ait plus de candidats éligibles. |
| **3b Merge similar neighbours graph-based** | Alternative basée sur un graphe à *Merge similar neighbours* : construit un graphe de similarité (arêtes entre petits peuplements et voisins adjacents similaires) et résout les composantes connexes en une seule passe. Différence par rapport à l'approche itérative : une chaîne de petits peuplements entre deux grands peuplements similaires est fusionnée en une étape au lieu de plusieurs passes. |
| **4 Clip to perimeter and eliminate gaps** | Découpe le résultat selon le périmètre du projet et referme les éventuelles lacunes qui en résultent. |

## e — Postprocessing Attributes

Calcule et complète les attributs de contenu de la carte des peuplements.

| Outil | Description |
| --- | --- |
| **5 Calculate crown coverage** | Calcule le degré de couverture (DG) par peuplement à partir du VHM 150cm. |
| **6 Add coniferous proportion** | Ajoute la proportion de résineux (NH, en %) par peuplement à partir du raster de degré de mélange. |
| **Append stand attributes** | Ajoute d'autres attributs de peuplement (zone de végétation, station forestière) par jointure spatiale. |

## f — Additional Modules

Modules complémentaires optionnels, généralement appliqués **après** le workflow principal à une carte des peuplements déjà générée.

| Outil | Description |
| --- | --- |
| **TBk postprocess local density** | Détecte, au sein des polygones de peuplements, des zones de densité locale différente (classes de degré de couverture), p. ex. pour délimiter des sous-secteurs particulièrement denses ou clairsemés. Seuils en pourcentage et rayons de fenêtre configurables par classe ; les petits trous/éclats sont filtrés, avec un lissage optionnel (« buffer smoothing »). |
| **TBk postprocess ddom SD estimate** | Estime le diamètre dominant à hauteur de poitrine (ddom) et, sur cette base, le stade de développement (SD) à partir de hdom, de la proportion de résineux (NH) et de la station forestière/qualité de station. |
| **TBk postprocess V estimate** | Estime le volume sur pied à partir de hdom, du degré de couverture (DG) et de la proportion de résineux (NH). |
| **TBk postprocess OS Change** | Calcule le changement de la strate supérieure entre deux états de carte TBk (évolution de la couche de degré de couverture, `dg_layer`). |
| **TBk WIS.2 Web prep export (KML)** | Prépare une carte des peuplements pour l'export vers WIS.2 Web. |
| **TBk WIS.2 Desktop export (XML)** | Exporte une carte des peuplements générée pour WIS.2 Desktop. |
| **TBk WIS.2 Web import CSV** | Importe des données depuis un export CSV WIS.2 Web. |

!!! note "Non couvert dans cet aperçu"
    Les groupes **g Utility** (p. ex. création de projet/mise en page, fusion de plusieurs cartes des peuplements, jointure spatiale générique — y compris *Tree species from raster*, qui malgré son emplacement dans le code source à côté des outils d'attributs est classé côté interface sous Utility) et **y Legacy** (outils prédécesseurs d'avant la modularisation) ne font pas partie de cette première version de la documentation technique.

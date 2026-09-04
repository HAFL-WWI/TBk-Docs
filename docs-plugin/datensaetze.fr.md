# Données

## Données d'entrée requises

| Jeu de données | Type | Exigence |
| --- | --- | --- |
| **Périmètre du projet** (« masque forestier ») | Vecteur (polygone) | Couvre l'ensemble de la surface forestière à traiter. Doit être **exempt d'erreurs de géométrie/topologie** (pas de nœuds dupliqués, de recouvrements, de lacunes) — sinon l'algorithme s'interrompt. Particulièrement sujet aux erreurs avec des multipolygones comportant de nombreuses petites parties (p. ex. lorsque des chemins forestiers sont découpés du périmètre). |
| **Modèle de hauteur de végétation (VHM)** | Raster | Résolution ≤ 1.5 m, couvre l'ensemble du périmètre. Source p. ex. LiDAR ou corrélation d'images aériennes stéréoscopiques. Mis à l'échelle par l'outil de prétraitement aux résolutions 10×10m (formation des peuplements) et 1.5×1.5m (détermination du degré de couverture), et aligné conjointement avec le raster de degré de mélange. |
| **Degré de mélange (MG)** | Raster (optionnel) | Valeurs 0–100, décrivant la proportion de résineux en % par pixel. Aligné par l'outil de prétraitement conjointement avec le raster VHM 10×10m. Les données brutes se présentent souvent avec une autre échelle/direction — voir [Attention : mise à l'échelle du degré de mélange](workflows.md#phase-1-preprocessing) lors du prétraitement. |

Toutes les données d'entrée doivent être correctement géoréférencées (pas d'erreurs de projection) et avoir une valeur NoData correctement définie. Elles ne doivent pas nécessairement être dans le même système de coordonnées, mais il est recommandé de projeter au préalable toutes les données dans le même système.

### Vérification des erreurs de géométrie (périmètre)

Vérifier dans QGIS avec les outils standards **Check Validity** et **Repair Geometries**, qui corrigent directement de nombreuses erreurs simples.

## Données intermédiaires/d'entrée générées par TBk

L'[outil de prétraitement](workflows.md#phase-1-preprocessing) transforme les données brutes en entrées effectives pour *Generate BK* :

| Fichier | Description |
| --- | --- |
| `VHM_detail.tif` | VHM haute résolution (étape intermédiaire) |
| `VHM_10m.tif` | VHM agrégé à 10×10m — entrée principale pour la délimitation des peuplements |
| `VHM_150cm.tif` | VHM à une résolution de 150cm — pour le calcul du degré de couverture |
| `MG_10m.tif` | Degré de mélange, aligné sur le VHM 10m (uniquement si une entrée MG est fournie) |
| `MG_10m_binary.tif` | Degré de mélange binarisé (uniquement si une entrée MG est fournie) |

## Données de sortie

| Fichier | Description |
| --- | --- |
| `TBk_Bestandeskarte.gpkg` | Résultat principal : la carte des peuplements avec les attributs de hauteur dominante (hdom), hauteur maximale (hmax), degré de couverture, proportion de mélange et structure de base |
| `TBk_Project.qgz` | Projet QGIS pour la visualisation, incl. 4 mises en page d'impression prédéfinies (A1/A3, portrait/paysage) |

Détails sur la signification des attributs sur le plan du contenu : voir la [documentation de contenu ↗](https://HAFL-WWI.github.io/TBk-Docs/tbk/).

## Configuration via des fichiers TOML

Tous les outils peuvent alternativement accepter un fichier de configuration `.toml` (paramètre `config_file`), dont les valeurs remplacent tous les paramètres définis dans la boîte de dialogue. Les clés communes les plus importantes (voir `default_input_config.toml` dans le dépôt du plugin) :

```toml
vhm_10m = ""                              # VHM 10m, entrée principale
vhm_150cm = ""                            # VHM 150cm, pour le degré de couverture
coniferous_raster = ""                    # Raster de degré de mélange pour la moyenne du peuplement
coniferous_raster_for_classification = "" # Raster de degré de mélange pour la classification
perimeter = ""                            # Périmètre pour le découpage
output_root = ""                          # Dossier de sortie
del_tmp = true                            # Supprimer les fichiers/champs temporaires
```

Pour la reproductibilité, les [workflows](workflows.md) génèrent eux-mêmes un fichier de configuration directement réutilisable, contenant les paramètres effectivement utilisés lors de l'exécution concernée. Pour des raisons techniques, les paramètres obligatoires doivent malgré tout être renseignés dans la boîte de dialogue de l'interface (avec des valeurs quelconques) — ils sont ensuite remplacés par les valeurs du fichier de configuration, si un tel fichier est fourni.

Utile pour rendre les exécutions reproductibles ou pour automatiser des traitements en dehors de l'interface QGIS.

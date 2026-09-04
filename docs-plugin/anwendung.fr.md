# Utilisation

## Où trouver les outils ?

Après l'installation, tous les outils TBk apparaissent dans la **boîte à outils de traitement** (Processing Toolbox) de QGIS, sous le fournisseur **TBk**. Ils y sont organisés en six groupes (plus deux internes), également triés par ordre alphabétique afin d'apparaître dans un ordre de traitement typique :

- **a Main Workflows** — workflows complets prêts à l'emploi
- **b Preprocessing** — préparation des données d'entrée
- **c Stand Delineation (Core)** — algorithme central de délimitation des peuplements
- **d Postprocessing Geometry** — post-traitement de la géométrie
- **e Postprocessing Attributes** — calcul/ajout d'attributs
- **f Additional Modules** — modules complémentaires optionnels

Détails sur les différents outils : voir [Outils](tools.md). Ordre typique/interaction des outils : voir [Workflows](workflows.md).

## Utilisation de base

Chaque outil TBk est un algorithme de traitement QGIS ordinaire :

1. Double-cliquer sur l'outil dans la boîte à outils (ouvre la boîte de dialogue des paramètres)
2. Définir les couches/paramètres d'entrée
3. Si nécessaire, déplier les **paramètres avancés** (généralement dotés de valeurs par défaut adaptées, rarement nécessaire de les modifier)
4. **Exécuter**

Les outils étant des algorithmes de traitement ordinaires, ils peuvent également être utilisés depuis la **console Python de QGIS** (`processing.run(...)`) ou dans le **Model Designer** — par exemple pour composer ses propres variantes des workflows standards.

## Emplacement de la sortie

La plupart des outils nécessitent qu'un **dossier de sortie** soit indiqué — s'il n'est pas défini, le résultat se retrouve dans un dossier temporaire et devient difficile à retrouver.

Le workflow principal ([Generate BK](workflows.md)) crée par défaut un sous-dossier horodaté :

```
{dossier de sortie}/{YYYYMMDD-HHMM}/
├── TBk_Bestandeskarte.gpkg      Résultat : la carte des peuplements
├── TBk_Project.qgz              Projet QGIS pour la visualisation
├── bk_process/                  Résultats intermédiaires
└── dg_layers/                   Couches raster du degré de couverture
```

La création du sous-dossier horodaté peut être désactivée via le paramètre avancé **« Create subfolder with timestamp »**.

## Nettoyage des données temporaires

La case à cocher **« Delete temporary files and fields »** est activée par défaut et supprime les résultats/champs intermédiaires après une exécution réussie. Pour le débogage, il peut être utile de la désactiver afin d'inspecter les étapes intermédiaires.

## Configuration via des fichiers TOML (avancé)

Tous les paramètres d'un outil peuvent également être définis via un **fichier de configuration `.toml`** (paramètre `config_file`). Les valeurs du fichier remplacent alors toutes les valeurs définies dans la boîte de dialogue. Cela permet de rendre les exécutions reproductibles ou de piloter des traitements par lots en dehors de l'interface QGIS. La structure du fichier TOML correspond directement aux noms des paramètres des outils — voir [Données](datensaetze.md) pour les clés les plus importantes.

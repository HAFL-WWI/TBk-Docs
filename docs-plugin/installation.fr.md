# Installation

## Prérequis

- **QGIS ≥ 3.10** (une version LTR actuelle est recommandée)
- **GRASS** et le **fournisseur GRASS** doivent être installés et activés dans QGIS (Réglages → Gérer/Installer les extensions)

!!! warning "Travailler en local plutôt que sur un lecteur réseau/cloud"
    Les données d'entrée et de sortie devraient se trouver **en local**, pas sur un lecteur réseau ou un stockage cloud (OneDrive, etc.). Avec des dossiers synchronisés, il peut arriver que des fichiers de sortie (temporaires) ne puissent pas être écrits ou lus, ce qui entraîne des erreurs difficiles à comprendre.

## Deux versions

| Version | Description |
| --- | --- |
| **TBk Plugin** (actuelle) | Version la plus récente, mise à jour en continu. Contient toutes les fonctionnalités, y compris le calcul par région. [Téléchargement ↗](https://nextcloud.bfh.science/index.php/s/Fmmr55zssrLAnfH) |
| **TBk Core** (stable) | Version éprouvée avec toutes les fonctionnalités jusqu'à octobre 2025, testée avec QGIS 3.16–3.44. **N'est plus développée** et ne contient **pas** le calcul par région. Peut être installée **en parallèle** de la version actuelle. [Téléchargement ↗](https://nextcloud.bfh.science/index.php/s/Pw46A2GCqMDt2Gn) |

## Installation sous forme de fichier ZIP

Le plugin s'installe sous forme de fichier ZIP :

1. Dans QGIS : **Extensions → Gérer et installer les extensions…**
2. Onglet **Installer depuis un ZIP**
3. Sélectionner le fichier `.zip` téléchargé et l'installer

Après l'installation, les outils TBk apparaissent dans la **boîte à outils de traitement** (Processing Toolbox) sous le fournisseur **TBk**, organisés dans les groupes a–f (voir [Outils](tools.md)).

TBk Plugin et TBk Core pouvant être installés en parallèle, les deux fournisseurs peuvent apparaître simultanément dans la boîte à outils — on les distingue par le nom du groupe/fournisseur.

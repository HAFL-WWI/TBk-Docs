# Description étape par étape du fonctionnement de TBk dans les grandes lignes

### Situation de départ

| La formation des peuplements se fait avec la mise en réseau des arbres dominants de dimensions plus ou moins similaires. <br>Les arbres dominants sont représentés dans TBk par les cellules raster (pixels) d’un are (10*10m) issues d’un modèle de hauteur de la végétation. La valeur de ces cellules correspond à la valeur maximale de hauteur sur leur surface, soit, de façon simplifiée, à la hauteur du plus grand arbre sur cette surface. | ![](../assets/img/abgrenzung-funktionsweise/img-1.png) 1 pixel = 1 are (10*10m) représenté par la hauteur maximale des arbres (cf. flèche bleue) |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |

### Point de cristallisation et début de la formation d’un peuplement

| TBk cherche d'abord le pixel dans un périmètre donné avec la plus grande hauteur d’arbre (valeur maximale).<br>Ensuite, le programme cherche dans les environs de ce pixel s'il y a suffisamment de pixels avec des valeurs similaires resp. avec des valeurs dans une certaine plage de tolérance prédéfinie. <br>Si cette condition est remplie, ce pixel est considéré comme un point de cristallisation pour la formation d’un nouveau peuplement. Il est représenté par « + » dans la figure à droite. | ![](../assets/img/abgrenzung-funktionsweise/img-2.png) |
| -------------------------------------------------------------------------------- | ------------------------------------------------------ |

### Formation et délimitation d’un peuplement

| Ensuite, TBk vérifie pour tous les pixels ayant des valeurs similaires s'ils peuvent eux-mêmes servir de points de continuation pour le même peuplement, c'est-à-dire s'il y a suffisamment de pixels ayant des valeurs similaires dans leur environnement.<br>Le processus se répète jusqu'à ce qu'il n'y ait plus de points de continuation. A ce moment-là, la formation du peuplement est terminée et ses limites définies, à condition que la surface soit supérieure à la surface minimale définie, soit normalement 0.1 ha. | ![](../assets/img/abgrenzung-funktionsweise/img-3.png) |
| -------------------------------------------------------------------------------- | ------------------------------------------------------ |

Cette délimitation se fait de façon similaire à celle effectuée manuellement sur le terrain (cf. section délimitation des peuplements en forêt), ce qui permet, en forêt, d’interpréter relativement facilement la carte des peuplements ainsi générée.

![Abbildung](../assets/img/abgrenzung-funktionsweise/img-4.png)

### Formation des peuplements de façon successive dans un périmètre forestier donné

| Après avoir formé et délimité un peuplement, TBk recherche le pixel qui a la valeur la plus élevée dans le périmètre forestier et qui n'appartient pas déjà à un peuplement formé, et ainsi de suite… | ![](../assets/img/abgrenzung-funktionsweise/img-5.png) |
| -------------------------------------------------------------------------------- | ------------------------------------------------------ |

### Surfaces restantes (cf. ch. 3.1)

A la fin du processus, il est possible qu’il y ait des surfaces sur lesquelles aucun peuplement n’a pu être formé. C’est le cas p.ex. sur certaines surfaces Lothar composées de quelques hêtres de différentes dimensions qui étaient anciennement sous couvert et sur lesquelles s’est établi un rajeunissement partiel. Dans ce cas, il n’y a pas suffisamment d’arbres dominants de dimensions plus ou moins similaires pour former un peuplement. Ces surfaces sont caractérisées par un astérisque « * » dans la description de base de la carte des peuplements.

### Description des peuplements

La hauteur dominante (hdom) est déterminée en faisant la moyenne des cellules raster de 10*10m caractérisées par les valeurs de hauteur maximales et correspondant aux points de cristallisation, aux points de continuation et aux cellules raster avec des valeurs plus ou moins similaires. Sur les surfaces restantes, la hauteur qui dépasse 80 % des autres hauteurs (80e percentile) est utilisée comme estimation de la hauteur dominante.

Le degré de recouvrement est calculé sur la base des cellules raster du modèle de hauteur de la végétation selon une résolution de 1.5*1.5m. La hauteur maximale par cellule est utilisée pour déterminer son appartenance à la strate supérieure si sa hauteur est supérieure à 2/3 de la hauteur dominante, à la strate intermédiaire si sa hauteur se situe entre 1/3 et 2/3 de hdom et à la strate inférieure si sa hauteur est inférieure à 1/3 de hdom. La somme des surfaces des cellules par strate divisée par la surface du peuplement donne le degré de recouvrement de chaque strate. Le degré de recouvrement de la strate supérieure est déterminé à partir de 1/3 du hdom pour les plus jeunes peuplements avec moins de 14 m de hauteur dominante.

Les phases de préparation pour la conversion en futaie irrégulière sont déterminées selon le tableau suivant :

| Etage de végétation                                             | Résineux et hdom max par phases | Résineux et hdom max par phases | Résineux et hdom max par phases | Feuillus et hdom max par phases | Feuillus et hdom max par phases | Feuillus et hdom max par phases |
| --------------------------------------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
|                                                                 | Phase -3                        | Phase -2                        | Phase -1                        | Phase -3                        | Phase -2                        | Phase -1                        |
| Collinéen (KL), submontagnard (SM) et montagnard inférieur (UM) | 10                              | 18                              | 26                              | 9                               | 16                              | 23                              |
| Montagnard supérieur (OM)                                       | 9                               | 16                              | 23                              | 7                               | 13                              | 19                              |
| Haut-montagnard (HM)                                            | 7                               | 13                              | 19                              | 6                               | 11                              | 16                              |
| Subalpin (SA)                                                   | 6                               | 11                              | 16                              | 5                               | 9                               | 13                              |

Les phases de conversion en futaie irrégulière sont déterminées selon le schéma suivant pour les peuplements avec une hauteur dominante supérieure à la hauteur dominante maximale pour la phase -1 :

![Abbildung](../assets/img/abgrenzung-funktionsweise/img-6.png)

Les limites inférieures et supérieures du degré de recouvrement des étages intermédiaires et inférieures prennent en compte le fait que les arbres situés sous couvert dans ces étages ne sont pas considérés dans le calcul du degré de recouvrement.

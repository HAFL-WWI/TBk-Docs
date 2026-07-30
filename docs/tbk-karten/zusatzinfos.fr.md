# Informations complémentaires : matériel sur pied, accroissement et composition en essences

### Matériel sur pied (TBk JU, FR)

TBk permet aussi de mettre en valeur les inventaires par placette d’échantillonnage en élaborant des estimateurs de matériel sur pied permettant d’estimer ces valeurs dendrométriques pour chaque peuplement TBk. La figure suivante présente celui du canton de Fribourg.

![Abbildung](../assets/img/tbk-karten-zusatzinfos/img-1.png)

Fig. 2.10 Estimateur du matériel sur pied pour le canton de Fribourg. Le code couleur en lien avec le diamètre dominant (ddom) correspond à celui des stades de développement.

L’estimation du matériel sur pied s’est faite sur la base des inventaires par placette d’échantillonnage des cantons du Jura, d’Argovie et de l’Inventaire Forestier National (IFN) par recoupement avec les peuplements TBk selon leur hauteur dominante (classes de 5 m), le degré de recouvrement de leur strate/étage supérieur (classes : 0-40%, 40-60%, 60-80% et 80-100%) et selon que le peuplement est majoritairement constitué de feuillus ou de résineux.

La combinaison de ces trois caractéristiques permet de définir des types de peuplement (ou strates d’un point de vue statistique). Pour chaque type de peuplement, la moyenne du matériel sur pied de toutes les placettes situées dans les peuplements de ce type a été calculée, ainsi que l’erreur-type qui permet de déterminer un intervalle de valeurs probables pour la valeur moyenne.

Le matériel sur pied de chaque peuplement TBk est déterminé sur cette base selon le type de peuplement auquel il correspond.

Pour plus d’informations, cf. annexe 3.

### Accroissement en volume (TBk FR)

Un estimateur pour l’accroissement en volume est aussi disponible. Il est cependant moins fiable vu le nombre limité de placettes disponibles (provenant uniquement de l’Inventaire Forestier National et sans tenir compte des différences de productivité des stations).

![Abbildung](../assets/img/tbk-karten-zusatzinfos/img-2.png)

Fig. 2.11 Estimateur de l’accroissement en volume pour le canton de Fribourg. Le code couleur en lien avec le diamètre dominant (ddom) correspond à celui des stades de développement.

Pour plus d’informations, cf. annexe 3.

### Composition en essences (TBk FR / Arborizer)

La composition en essences des peuplements peut être déterminée si des données sur la répartition spatiale des essences sont disponibles. C’est par exemple le cas dans le canton de Fribourg avec la carte indicative des essences obtenue avec l’outil digital Arborizer développé par Raffael Bienz (waldfride Analytics) (cf. fig. suivante et le rapport technique).

![Abbildung](../assets/img/tbk-karten-zusatzinfos/img-3.png)

Fig. 2.12 Carte indicative des essences obtenue au moyen de l’Arborizer (Raffael Bienz, waldfride Analytics) ; les couronnes détectées sont représentées par un polygone dont la couleur est en lien avec les essences

La reconnaissance des couronnes des arbres et des essences se fait en deux parties : la première consiste à détecter et délimiter les couronnes, la seconde à déterminer l’essence de chaque couronne détectée. Pour ce faire, les modèles de deep learning sont utilisés en se basant sur des orthophotos avec une résolution de 10 ou 25 cm et des données collectées sur le terrain par les gardes forestiers du canton sur la présence des essences (données d’entrainement).

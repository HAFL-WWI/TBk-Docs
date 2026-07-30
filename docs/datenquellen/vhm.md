# Vegetationshöhenmodell (VHM)

Das Vegetationshöhenmodell (VHM), auch digitales Vegetationsmodell genannt, beschreibt die Höhe von Bäumen durch Subtraktion des digitalen Modells der Vegetationsoberfläche von dem des Geländes, Modelle, die z. B. durch LiDAR-Befliegung und/oder Stereokorrelation von Luftbildern gewonnen werden (siehe Glossar).

Swisstopo hat bereits zwei vollständige Befliegungen der Schweiz durchgeführt, die im Folgenden als LiDAR 2000+ für die Erhebungen zwischen 2002 und 2008 und LiDAR 2010+ für die Erhebungen zwischen 2017 und 2024 bezeichnet werden. Zu beachten ist, dass die dritte Befliegung von Swisstopo im Jahr 2024 startete.

LiDAR 2000+ und LiDAR 2010+ unterscheiden sich insbesondere in der Dichte der erhaltenen Punktwolken (ca. 1 Punkt pro 2m2 bei LiDAR 2000+ und im Durchschnitt 15-20 Punkte/m2 bei LiDAR 2010+). Da der Deckungsgrad auf der Basis einer Auflösung von 1.5*1.5m bestimmt wird, was in etwa der Auflösung von LiDAR 2000+ entspricht, sollte dieser Unterschied keine Auswirkungen auf die Vergleichbarkeit der erzielten Ergebnisse haben, wie z.B. die folgende Abb. (aus TBk Jura) zeigt: Der Detaillierungsgrad und die Vergleichbarkeit der Daten sind so hoch, dass erkennbar ist, wie sich die Kronen zwischen 2006 und 2022 ausgedehnt haben und welche Bäume in dieser Zeit genutzt wurden.

![Abbildung](../assets/img/datenquellen-vhm/img-1.jpeg)

Abb. 4.1 TBk-Bestandeskarten auf der Basis des Vegetationshöhenmodells einer LiDAR-Befliegung von 2006 bzw. 2022 (TBk Jura) und Vergleich der Veränderungen in der Oberschicht über diesen Zeitraum (die blaue Farbe in beiden Bestandeskarten zeigt eine Oberhöhe hdom von 0m an: Bei der betreffenden Fläche sind fast keine Bäume vorhanden – es handelt es sich um eine Wytweide)

Es wäre jedoch sinnvoll, die beiden Datenquellen systematisch genauer zu vergleichen, um sicherzustellen, dass es keine Verzerrungen gibt.

Der Vergleich von VHMs aus LiDAR-Befliegungen (LiDAR-VHMs unten) mit VHMs aus Stereokorrelation von Luftbildern (STEREO-VHMs unten) sollte angesichts der unterschiedlichen Datenquellen, die verwendet wurden, mit grösserer Vorsicht erfolgen. Die VHM STEREO überschätzen den Deckungsgrad tendenziell (im Durchschnitt um etwa +10%). Die folgende Abbildung zeigt die Unterschiede zwischen den beiden Datenquellen, die nahezu aus demselben Befliegungsjahr stammen. Die Ergebnisse sind zwar in etwa gleich, unterscheiden sich aber im Detailierungsgrad, z.B. erscheint in der folgenden Abbildung der STEREO-VHM basierenden Bestandeskarte die Oberschicht der Bestände tendenziell etwas dichter und weniger detailliert in der räumlichen Verteilung. Dieser Aspekt muss noch weiter untersucht werden.

![Abbildung](../assets/img/datenquellen-vhm/img-2.jpeg)

Abb. 4.2 TBk-Bestandeskarten generiert mit einem Vegetationshöhenmodell aus einer LiDAR-Befliegung von 2012 (links) und mit einem Vegetationshöhenmodell aus der Stereokorrelation von Luftbildern von 2013 (rechts).

!!! note "Migrations-Hinweis"
    Diese Abbildung fehlt im Original-Handbuch `TBk_Manuel_V11_DE.docx` (Bild nicht eingebettet, nur die Bildunterschrift ist vorhanden) und wurde stattdessen aus der französischen Fassung (`TBk_Manuel_V11_FR.docx`, Fig. 4.2) übernommen. Lohnt sich, im Original-docx zu ergänzen.

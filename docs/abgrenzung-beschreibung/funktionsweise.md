# Beschreibung Schritt-für-Schritt- der Funktionsweise von TBk in groben Zügen

### Ausgangslage

| Die Bildung von Beständen erfolgt durch die Vernetzung von dominanten Bäumen mit mehr oder weniger ähnlichen Baumhöhen. <br>Die dominanten Bäume werden in TBk durch 1 Are (10*10m) grosse Rasterzellen (Pixel) aus einem Vegetationshöhenmodell repräsentiert. Der Wert dieser Zellen entspricht dem maximalen Höhenwert auf ihrer Fläche, vereinfacht gesagt, der Höhe des grössten Baumes auf dieser Fläche. | ![](../assets/img/abgrenzung-funktionsweise/img-1.png) 1 Pixel = 1 Are (10*10m), dargestellt durch die maximale Höhe der Bäume (siehe blauer Pfeil). |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |

### Kristallisationspunkt und Beginn der Bildung eines Bestandes.

| TBk sucht zuerst nach dem Pixel mit der grössten Baumhöhe (Maximalwert) in einem bestimmten Perimeter.<br>Anschliessend sucht das Programm in der Umgebung dieses Pixels, ob es genügend Pixel mit ähnlichen Werten bzw. mit Werten innerhalb eines bestimmten, vordefinierten Toleranzbereichs gibt. <br>Wenn diese Bedingung erfüllt ist, wird dieses Pixel als Kristallisationspunkt für die Bildung eines neuen Bestandes betrachtet. Er wird in der Abbildung rechts mit "+ " dargestellt. | ![](../assets/img/abgrenzung-funktionsweise/img-2.png) |
| -------------------------------------------------------------------------------- | ------------------------------------------------------ |

### Bildung und Abgrenzung eines Bestandes

| Anschliessend prüft TBk für alle Pixel mit ähnlichen Werten, ob sie selbst als Fortsetzungspunkte für denselben Bestand dienen können, d.h. ob es in ihrer Umgebung genügend Pixel mit ähnlichen Werten gibt.<br>Der Vorgang wird so lange wiederholt, bis es keine Fortsetzungspunkte mehr gibt. Zu diesem Zeitpunkt ist die Bildung des Bestandes abgeschlossen und seine Bestandesgrenzen definiert, sofern die Fläche grösser ist als die definierte Mindestfläche, die normalerweise 0,1 ha beträgt. | ![](../assets/img/abgrenzung-funktionsweise/img-3.png) |
| -------------------------------------------------------------------------------- | ------------------------------------------------------ |

Dieses Vorgehen erfolgt ähnlich wie die manuelle Abgrenzung im Feld (siehe Abschnitt Abgrenzung von Beständen im Wald), so dass im Wald die so erzeugte Bestandeskarte relativ leicht interpretiert werden kann.

![Abbildung](../assets/img/abgrenzung-funktionsweise/img-4.png)

### Sukzessive Bildung von Beständen in einem bestimmten Waldgebiet

| Nachdem ein Bestand gebildet und abgegrenzt wurde, sucht TBk nach dem Pixel mit dem höchsten Wert im Waldperimeter, der nicht bereits zu einem gebildeten Bestand gehört, und so weiter... | ![](../assets/img/abgrenzung-funktionsweise/img-5.png) |
| -------------------------------------------------------------------------------- | ------------------------------------------------------ |

### Verbleibende Flächen (vgl. Kap. 3.1)

Am Ende des Prozesses kann es sein, dass es Flächen gibt, aus denen kein Bestand gebildet werden konnte. Dies ist z.B. auf einigen Lothar-Flächen der Fall, die aus einigen Buchen unterschiedlicher Grösse bestehen, die früher unter Kronendach standen und auf denen sich eine Teilverjüngung etabliert hat. In diesem Fall gibt es nicht genügend dominante Bäume von mehr oder weniger ähnlicher Grösse, damit ein Bestand gebildet werden kann. Diese Flächen sind in der Grundbeschreibung der TBk-Bestandeskarte mit einem Sternchen "*" gekennzeichnet.

### Beschreibung der Bestände

Die Oberhöhe (hdom) wird bestimmt, indem der Mittelwert der 10*10m Rasterzellen gebildet wird, die durch maximale Höhenwerte gekennzeichnet sind und Kristallisationspunkten, Fortsetzungspunkten und Rasterzellen mit mehr oder weniger ähnlichen Werten entsprechen. Auf den verbleibenden Flächen wird die Höhe, die 80 % der anderen Höhen übersteigt (80. Perzentil), als Schätzung der Oberhöhe verwendet.

Der Deckungsgrad wird auf der Grundlage der Rasterzellen des Vegetationshöhenmodells mit einer Auflösung von 1,5*1,5m berechnet. Die maximale Höhe pro Zelle wird verwendet, um ihre Zugehörigkeit zur Oberschicht zu bestimmen, wenn ihre Höhe mehr als 2/3 der Oberhöhe beträgt, zur Mittelschicht, wenn ihre Höhe zwischen 1/3 und 2/3 hdom liegt, und zur Unterschicht, wenn ihre Höhe weniger als 1/3 hdom beträgt. Die Summe der Flächen der Zellen pro Schicht geteilt durch die Fläche des Bestandes ergibt den Deckungsgrad jeder Schicht. Der Deckungsgrad der Oberschicht wird bei den jüngsten Beständen mit weniger als 14 m Oberhöhe ab 1/3 hdom bestimmt.

Die Vorbereitungsphasen für die Überführung in einen ungleichförmigen Hochwald werden gemäss der folgenden Tabelle bestimmt:

| Vegetationshöhenstufe                            | Nadelholz und hdom max nach Phasen | Nadelholz und hdom max nach Phasen | Nadelholz und hdom max nach Phasen | Laubholz und hdom max nach Phasen | Laubholz und hdom max nach Phasen | Laubholz und hdom max nach Phasen |
| ------------------------------------------------ | ---------------------------------- | ---------------------------------- | ---------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
|                                                  | Phase -3                           | Phase -2                           | Phase -1                           | Phase -3                          | Phase -2                          | Phase -1                          |
| Kollin (KL), Submontan (SM) und untermontan (UM) | 10                                 | 18                                 | 26                                 | 9                                 | 16                                | 23                                |
| Obermontan (OM)                                  | 9                                  | 16                                 | 23                                 | 7                                 | 13                                | 19                                |
| Hochmontan (HM)                                  | 7                                  | 13                                 | 19                                 | 6                                 | 11                                | 16                                |
| Subalpin (SA)                                    | 6                                  | 11                                 | 16                                 | 5                                 | 9                                 | 13                                |

Die Überführungsphasen in den ungleichförmigen Hochwald werden nach folgendem Schema für Bestände bestimmt, deren Oberhöhe grösser ist als die maximale Oberhöhe der zugehörigen Phase -1.

![Abbildung](../assets/img/abgrenzung-funktionsweise/img-6.png)

Die unteren und oberen Grenzen des Deckungsgrades der mittleren und unteren Stufen berücksichtigen, dass Bäume bzw. Verjüngung, die in diesen Stufen unter dem Kronendach stehen, bei der Berechnung des Deckungsgrades nicht berücksichtigt werden.

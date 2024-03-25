# LA245 Prototyp

Matteo Jakob, I21a, 25.03.2024

## Inhaltsverzeichnis

1. [Problembeschreibung](#problembeschreibung)
2. [Anforderungen](#anforderungen)
3. [Art und Vorgehensweise](#art-und-vorgehensweise)
4. [Resultat](#resultat)
5. [Fazit](#fazit)
6. [Reflexion](#reflexion)

### Problembeschreibung

Eine Home-Gym-App verliert an Relevanz aufgrund der Konkurrenz. Da es hunderte Alternativen gibt, ist der Benutzer nicht dazu geneigt, genau unsere App herunterzuladen. Es braucht eine Innovation: Personalisierte Workouts.

Es gibt also einen Online Coach, welcher personalisierte Trainings anbietet.
Um heraus zu stechen darf die App sich auf den jeweiligen Benutzer anpassen, indem er;

- Workouts erhaltet, welches seinem Niveau entspricht, also die anzahl Reps und Sets grösser oder kleiner werden.
- Spezifische Workouts für spezifische Muskelgruppen bekommt, die evt. Nicht genug entwickelt sind oder einfach des Benutzers Interesse entsprechen.
- Wochenplanung, wie oft und wie lange die Trainings anhalten sollen.

### Anforderungen

| Nr. | Muss/kann | Funktional/Qualität/Rand | Bschreibung                                                                                                                     |
| --- | --------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Muss      | Funktional               | Der User kann eigene Inputs geben                                                                                               |
| 2   | Muss      | Funktional               | Es werden personalisierte Trainings generiert (Unterschiedliche Anzahl an Reps und Sets, auch unterschiedliche Trainingsformen) |
| 3   | Muss      | Funktional               | Der Nutzer kann eigene Trainingsgeräte hinzufügen                                                                               |
| 4   | Kann      | Funktional               | Dem Nutzer werden Fragen gestellt, somit er genauere Daten geben kann                                                           |
| 5   | Kann      | Rand                     | Programmierumgebung Python                                                                                                      |
| 6   | Kann      | Funktional               | Der Nutzer kann die Länge der Workouts angeben                                                                                  |
| 7   | Kann      | Funktional               | Der Nutzer kann Muskelgruppen angeben                                                                                           |

### Art und Vorgehensweise

Eine Möglichkeit zur Integration von KI wäre, einen Prompt zu generieren, der eine Trainingsaufgabe und Daten zur Sportlichkeit des Benutzers enthält. Mit diesen Informationen könnte die KI automatisch Trainingssets mit angepasster Intensivität erstellen. Diese Methode ermöglicht auch die einfache Einbeziehung von vorhandenen Trainingsgeräten zu Hause. Zum Beispiel könnten, falls der Nutzer Hanteln besitzt, Übungen mit Hanteln in das Training integriert werden.

Die zweite Möglichkeit besteht darin, vor und nach jedem Training Feedback vom Benutzer einzuholen, um festzustellen, ob das Training zu einfach, zu schwer oder gerade richtig war. Basierend auf diesem Feedback können dann beispielsweise die Anzahl der Wiederholungen angepasst werden.

Obwohl die erste Möglichkeit mit der einfachen Integration weiterer Trainingsobjekte sehr attraktiv ist, gibt es ein Problem: Die Nutzung der KI erfordert Tokens, die kostenpflichtig sind und somit für mich nicht geeignet sind. Aus diesem Grund finde ich die zweite Möglichkeit attraktiver umzusetzen, da sie keine zusätzlichen Kosten verursacht und dennoch personalisierte Trainings ermöglicht.

### Resultat

![Output part 1](https://i.imgur.com/AOijF5V.png)
![Output part 2](https://i.imgur.com/RDkyWiq.png)

### Fazit

Ich habe mich zwar zuerst für die "Keine-KI"-Version entschieden, aufgrund von den Kosten. Jedoch war dies zu einfach und dachte mir, ich mache mir eine kleine Herausforderung. Nun habe ich ein Prototyp erstellt, welches dir bereits realistisch machbare Trainings anbietet und bereits zu gebrauchen ist.

Für eine volle Version wäre lediglich eine GUI und angepasste effizientere Fragen erforderlich. Man könnte auch einen eigenen Assistenten innerhalb von OpenAI generieren, anstatt das öffentliche Modell zu nutzen, jedoch ist dies momentan ausserhalb dieses Prototyps.

### Reflexion

Gut gelaufen ist das generieren der Prompts, sobald man die API am rennen hat, ist es recht einfach Prompts zu generieren.

Nicht so gut gelaufen ist die Verbindung mit OpenAI API, da man einen Token brauchte. Diesen Token muss man ausserhalb des Codes haben aus Sicherheitsgründen, welches Probleme mit der Verbindung mit sich trägt. Nach längerem studieren ist herausgekommen, dass eine Library fehlt, welche nicht in der OpenAI API erwäht wurde.

Nächstes Mal würde ich schauen, dass ich alle benötigten Tools und Bibliotheken sicher installiert sind, damit eine reibungslose Verbindung mit der API erfolgt. Eine gründlichere Recherche könnte dabei helfen Probleme im Voraus zu identifizieren und auch zu bekämpfen. Dies würde Frustation ein bisschen mindern.

Ich bin erfreut, dass ich doch noch mit KI gearbeitet habe, da es mir wichtige Einblicke in der Machbarkeit weiterer KI-Projekten gibt und ich nun mit der OpenAI API versierter bin.

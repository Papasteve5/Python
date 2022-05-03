
# Schreibe ein Programm, welches eine Liste aus Zeichenketten alphabetisch sortiert.
# Der Benutzer soll per Eingabe entscheiden, welche Elemente in die Liste kommen
# und er soll so viele Elementen eingeben können, wie er will.
# Wenn er mit der Eingabe fertig ist, soll er mit einem Befehl (zum Beispiel q) die Eingabe beenden.


data = []

data = [eingabe for eingabe in input("Gebe deine Eingaben ein: ").split()]

print(sorted(data))



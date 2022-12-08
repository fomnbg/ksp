"""
a) Lesen Sie zeilenweise verschiedene Begriffe ein und zählen Sie, wie oft die Begriffe jeweils vorkommen. Verwenden Sie ein Dictionary
Geben Sie die Begriffe zusammen mit ihrer Häufigkeit aus.
Folgendes Dictionary ist gegeben:
freunde = {"Max":"Mustermann","Eva":"Mustermann","Felix":"Mustermann"}
- Fragen Sie ab, ob Max Mustermann im Dictionary enthalten ist
- Geben Sie die Vor- und Nachnamen aller Personen im Dictionary alphabetisch nach
Vorname sortiert aus.
"""

dict = {}
w = input("Enter a word: ")

while w != "":
    if w not in dict.keys():
        dict.update({w: 1})
    else:
        dict[w] += 1
    w = input("Enter a word: ")

for key, value in dict.items():
    print(key + ":", value)

# ab hier Aufgabe b, ist aber keine gute Aufgabe 

freunde = {"Max": "Mustermann", "Eva": "Mustermann", "Felix": "Mustermann"}

if freunde["Max"] == "Mustermann":
    print("enthalten")

for key in sorted(freunde):
    print(key, freunde[key])
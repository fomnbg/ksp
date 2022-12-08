"""
Schreiben Sie ein Programm, das ein Wort einliest. 
Das Wort wird dann so oft ausgegeben, wie es Buchstaben hat.
"""

wort = input("Geben Sie das Wort ein: ")
buchstaben = len(wort)

for i in range(buchstaben):
    print(wort)
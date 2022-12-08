"""
Schreiben Sie ein Programm, das den Anwender nach einem Start- und Endwert fragt 
und dann alle Zahlen (Integer) inklusive der eingegebenen ausgibt.
"""

start = input("Geben Sie den Startwert an: ")
start = int(start)
ende = input("Geben Sie den Endwert an: ")
ende = int(ende)

# man kann auch int folgendermaßen einlesen
# variable = int(input("Gib deinen Input ein: "))

for i in range(start, ende+1):
    print(i)
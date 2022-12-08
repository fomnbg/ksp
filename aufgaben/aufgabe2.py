"""
a) Schreiben Sie in Python ein Programm, das Kilometer einliest und in Meilen um- rechnet. 
(Umrechnungsfaktor: 1.609)
b) Fangen Sie Eingaben < 0 mit einer Fehlermeldung ab.
"""

km = ""

while 1:
    km = input("Gebe ein: ")

    if km < 0:
        print("Fehler")
    else:
        break
mi = int(km) / 1.609
print("Das entspricht" + str(mi) + "Meilen")
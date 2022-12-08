"""
Bei dieser Aufgabe geht es darum, sukzessive eine Liste von Zeichenketten aufzubauen. 
In diesen Fällen weist man einer Variablen zunächst – sozusagen als Starter – eine leere Liste zu, 
die dann im weiteren Ablauf nach und nach um die vom User eingegebenen Sätze erweitert wird.
Die Methode der Wahl dafür ist .append()
Wenn der User 'Stop' eingibt, ist Schluss und die gesamte Zeichenkette wird ausgegeben.
"""

x = []

while 1:
    y = input("Eingabe:")
    if(y == "stop"):
        break
    x.append(y)

print(x)

#Zusatz um die Liste als "normalen" Text aufzugeben

for wort in x:
    print(wort, end=' ')
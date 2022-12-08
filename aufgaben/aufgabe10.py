"""
Schreiben Sie eine Funktion, die einen Temperaturwert von 
Celsius nach Fahrenheit umwandelt.
Umwandlungsformel: °F = °C * 1,8 + 32
Legen Sie eine Liste mit Temperaturwerten an. 
Wandeln Sie die Werte von Celsius nach Fahrenheit um 
und speichern Sie die Werte in einer neuen Liste.
Bestimmen Sie den höchsten Wert.
"""

def c2f(c):
    return c*1.8+32

l = [0, 20, 30, 50, 80, 100]
l2 = []

for c in l:
    l2.append(c2f(c))

#print(l)
print(l2)
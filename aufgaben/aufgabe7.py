"""
Schreiben Sie ein Programm, das überprüft, ob eine eingegebene Zahl ein Primzahl ist.
Lagern Sie die Primzahlerkennung in eine Funktion aus, die true oder false zurückliefert.
"""

import math

def is_prime(x):
    
    if x == 2:
        return True

    t = 2
    while x/t != round(x/t):
        t = t+1
        if t > math.sqrt(x):
            return True
    return False

x = int(input("Bitte geben Sie eine Zahl ein: "))

if is_prime(x):
    print(x, " ist prim.")
else:
    print(x, " ist nicht prim.")
"""
a) Schreiben Sie eine Funktion, die Sekunden übergeben bekommt und Stunden, Minuten und Sekunden als Tupel zurückliefert.
b) Schreiben Sie eine Funktion, die eine Liste übergeben bekommt und das erste und das letzte Element der Liste als Tupel zurückliefert.
"""

def s2hms(s):
    h = s // 3600
    m = (s // 60)%60
    s = s % 60
    return h,m,s

def lf(list):
    first = list[0]
    last = list[-1]
    return first, last

s = 12345
print(s2hms(s))

list = ['Josch', 'Alex', 'Stephan', 'Pipo']
print(lf(list))
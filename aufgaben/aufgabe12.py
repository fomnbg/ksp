"""
a) Schreiben Sie eine Funktion Loesche_Erstes, die das erste Element 
einer als Parameter übergebenen Liste löscht.
b) Schreiben Sie eine Funktion Ist_Sortiert, die true zurückliefert, 
falls eine Liste (Parameter) aufsteigend sortiert ist und false sonst. 
Sie dürfen davon ausgehen, dass die Elemente der Liste mit < bzw. > vergleichbar sind.
"""

def loesche_erstes(list):
    del list[0] # kann man auch mit folgendem machen: >>> list.remove(list[0])
    return list

def ist_sortiert(list):
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            return False
    return True
        

x = [1, 2, 3, 5, 4]
loesche_erstes(x)
print(x)
print(ist_sortiert(x))
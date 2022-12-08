import re

string = "Bla Kbla bla 30.2.19 Mai blaK  Maijuni MaiJuni bla 24.12.2022 K Mai"
print(string)

pattern = r"\bMai\b" # das r vor einem String steht für raw-String

m1 = re.findall(pattern, string)
print(len(m1))

m2 = re.sub(pattern, "Juni", string)
print("m2:", m2)

m3 = re.sub(r"\bJuni\b", "Monat Juni", m2)
print("m3:", m3)

m4 = re.sub("K", "T", m3)
print("m4:", m4)

pattern = r"[0123]?\d\.[01]?\d\.\d{2,4}"
m5 = re.findall(pattern, string)
print(m5)

list_length = len(m5)
print(list_length)

liste = []
#liste = [None] * list_length    # i * None, weil man nicht in eine leere Liste schreiben kann mit split()

for i in range(list_length):
    liste.append(m5[i].split('.'))
    #print(liste)
    # liste[i] = m5[i].split('.') 
    print("Amerikanische Schreibweise: " + liste[i][1] + "." + liste[i][0] + "." + liste[i][2])
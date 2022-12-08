"""
Legen Sie in Python eine Liste mit dem Namen von 4 Freunden an.
- Geben Sie die Anweisungen an um alle Namen auszugeben
- Lesen Sie einen Namen ein und löschen diesen aus der Liste, 
falls er enthalten ist. Falls er nicht enthalten ist, geben Sie eine Fehlermeldung aus.
"""

list = ['Philipp', 'Gabriel', 'Stephan', 'Janis']
print("\nUrsprünglich angelegte Liste:")
for i in list:
    print(i)

name = input("\nName zum löschen eingeben: ")
if name in list:
    list.remove(name)
else:
    print(name, "ist nicht in der Liste enthalten")

print("\nNeue, gelöschte Liste: ")
for i in list:
    print(i)

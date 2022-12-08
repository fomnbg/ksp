"""
Schreiben Sie ein Programm, das mittels Eingabe 2er Zahlen 
und eines passenden Operanden alle 4 Grundrechenarten ausführen kann.
"""

while 1:

    a = input("Bitte gbeen Sie Zahl 1 ein: ")

    try:
        a = int(a)
    except:
        try:
            a = float(a)
        except:
            print("Zahl 1 ungültig!")

while 1:

    b = input("Bitte gbeen Sie Zahl 2 ein: ")

    try:
        b = int(b)
    except:
        try:
            b = float(b)
        except:
            print("Zahl 2 ungültig!")


while 1:

    o = input("Bitte geben Sie einen Operanden (+, -, *, /) ein:")

    if o == "+":
        e = a+b
        break
    elif o =="-":
        e = a-b
        break
    elif o == "*":
        e = a*b
        break
    elif o == "/":
        e = a/b
        break
    else:
        print("Der Operand ist ungültig.\n")

print(e)
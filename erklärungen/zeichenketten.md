# Zeichenketten: Datentyp `str`

- Kennzeichnung durch einfache, doppelte oder dreimal doppelte Hochkomma
    ```python
    t1 = 'Text'
    t2 = "Josch ist ein Kek"
    t3 = """Zeichenkette über
         mehrere Zeilen"""
    r1 = r"Das hier ist ein raw-String" 
    f1 = f"Hier steht dein {t1}, und außerdem: {t2}"    
    ```
- Einlesen von Tastatur: `input()`
    ```python
    t4 = input("Geben Sie die Variable an: ")
    ```
    > Wenn man direkt einen bestimmten Datentyp einlesen will, dann macht man das so:
    ```python
    t5 = int(input("Geben sie die Variable für den Integer ein: "))
    ```
- Ausgabe auf Konsole: `print()`
    ```python
    print("Hier kann stehen was du willst")
    print("Für Variablen anhängen: ", t5)
    ```
# Zeichenketten: 
## Datentyp `str`

### Strings sind unveränderbar, es können Zeichen oder Bereiche ersetzt werden
#### Die einzige Möglichkeit zur Veränderung eines String ist die Erzeugung eines neuen Objekts
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
- Operatoren
    - \+ : Verkettung von Sequenzen: 
    ```python
    t6 = t1 + t2
    ```
    - \* : Vervielfachung von Sequenzen:
    ```python
    t7 = t1*3
    ```

## Operationen 
- #### Teilbereich von Sequenzen: Slices 
    Angabe: [startindex: endindex]
    Nummerierung beginnt bei 0, alternativ -1
    ```python
    tname = "Das hier steht nur als Beispiel da"
    ts1 = tname[6:9]
    ts2 = tname[6:] # Bereich endet mit Ende der Zeichenkette
    ts3 = tname[:5] # Bereich beginnt bei 0
    ts4 = tname[0:-5] # Index mit einer negativen Zahl wird vom Ende aus gemessen
    ```
- #### `len()`
    ermittelt die Anzahl der Elemente
    ```python
    lg = len(tname)
    ```
- #### `count()`
    liefert Anzahl der Vorkommen eines Suchtexts innerhalb eines analysierten Textes
    ```python
    t = "das ist ein Beispielsatz"
    anz = t.count("ei")
    ```
- #### `find()`
    ergibt die Position, an der ein Suchtext innerhalb eines analysierten Textes vorkommt. Optional kann ein zweiter Parameter angegeben werden, ab welcher Position gesucht werden soll. Rückgabe -1 bedeutet, dass Suchtext
    nicht gefunden wurde
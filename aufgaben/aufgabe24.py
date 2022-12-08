import math


#protected kann nur in der eigenen Klasse verwendet werden
#private können nur mit abgeleiteten Klassen verwendet werden
#public für alle

class Shape():
    def __init__(self, bezeichnung):
        self._Bezeichnung = bezeichnung
        
class Dreieck(Shape):
    def __init__(self, bezeichnung, grundseite, hoehe):
        super().__init__(bezeichnung)
        self.__Grundseite = grundseite
        self.__Hoehe = hoehe
        
    def Draw(self):
        print(f"Ich bin ein {self._Bezeichnung}")
        
    def CalculateArea(self):
        x = 0.5*self.__Grundseite*self.__Hoehe
        print(f"Flaecheninhalt: {x}")
        pass
        
class Rechteck(Shape):
    def __init__(self, bezeichnung, laenge, breite):
        super().__init__(bezeichnung)
        self.__Laenge = laenge
        self.__Breite = breite
        
    def Draw(self):
        print(f"Ich bin ein {self._Bezeichnung}")
        
    def CalculateArea(self):
        x = self.__Laenge*self.__Breite
        print(f"Flaecheninhalt: {x}")

class Kreis(Shape):
    def __init__(self, bezeichnung, radius):
        super().__init__(bezeichnung)
        self.__Radius = radius

    def Draw(self):
        print(f"Ich bin ein {self._Bezeichnung}")
        
    def CalculateArea(self):
        x = math.pi*(self.__Radius**2)
        print(f"Flaecheninhalt: {round(x, 2)}")
        
s1 = Dreieck("Dreieck", 7, 3)
s2 = Rechteck("Rechteck", 5, 10)
s3 = Kreis("Kreis", 6)
s4 = Kreis("Kreis", 5)
s5 = Dreieck("Dreieck", 4, 4)
s6 = Rechteck("Rechteck", 3, 3)
s7 = Rechteck("Rechteck", 10, 3)

objekte = [s1, s2, s3, s4, s5, s6, s7]

for i in objekte:
    i.Draw()
    i.CalculateArea()
    print(21*"_")
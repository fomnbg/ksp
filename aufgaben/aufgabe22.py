class User():
    def __init__(self, first_name, last_name, gender, academic_title_front = "", academic_title_back = "", title_of_nobility = ""):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__academic_title_front = academic_title_front
        self.__academic_title_back = academic_title_back
        self.__title_of_nobility = title_of_nobility

    def describe_user(self):
        print("First name: ", self.__first_name)
        print("Title of nobility: ", self.__title_of_nobility)
        print("Last name: ", self.__last_name)
        print("Gender: ", self.__gender)
        print("Academic Title (front): ", self.__academic_title_front)
        print("Academic Title (back): ", self.__academic_title_back)

    def greet_user(self, formal = 0):
        if formal:
            greeting = "Sehr geehrte"
            if self.__gender:
                greeting += "r Herr"
            else:
                greeting  += "Frau"
            greeting += self.__academic_title_front
            greeting += " " + self.__title_of_nobility
            greeting += " " + self.__last_name
            greeting += " " + self.__academic_title_back
        else:
            greeting = "Hallo " + self.__first_name
        return greeting

#ab hier die eigentliche Aufgabe 22, weil sie auf 21 aufbaut

class Warteschlange():
    __queue = []
    
    def __init__(self):
        pass
    def ankommen(self, user):
        self.__queue.append(user)
    def verlassen(self, user):
        self.__queue.remove(user)
    def anzahl_aktuell(self):
        return len(self.__queue)
    def ausgabe(self):
        for u in self.__queue:
            print(u.greet_user())


u1 = User("Hans", "Dampf", 1, "Prof. Dr.- Ing. Dr. h.c. mult. Dr. E.h. mult.", "M.Sc.", "von")
u2 = User("Gretel", "Schmidt", 0)

queue = Warteschlange()
queue.ankommen(u1)
queue.ankommen(u2)
print("Länge der Wartschlange aktuell: ", queue.anzahl_aktuell())
queue.ausgabe()
queue.verlassen(u2)
print("Länge der Wartschlange aktuell: ", queue.anzahl_aktuell())
queue.ankommen(User("Sebastian", "Vettel", 0))
print("Länge der Wartschlange aktuell: ", queue.anzahl_aktuell())
queue.ausgabe()
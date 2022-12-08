#Aufgabe doch nicht wichtig -> irrelevant

class Quiz():
    fragen ={
        "Was ist die Hauptstadt von Deutschland": "Berlin",
        "Was ist die Hauptstadt von Frankreich": "Paris",
        "Was ist die Hauptstadt von USA": "Washington", 
        "Was ist die Hauptstadt von Spanien": "Madrid"
    }
    
    def __init__(self, name, punktestand):
        self.__Name = name
        self.__Punktestand = int(punktestand)
        
    def Start(self):
        for i in self.fragen.keys():
            antwort = input(i + "?")
            if i == antwort: 
                self.__Punktestand += 1
            cont = input("Möchten Sie das Quiz beenden (b) oder weiterspielen (w)?\n")
            if cont == "b":
                break
            #else:
            #    continue

    def AddEntry(self):
        entry = input("Welche Frage wollen Sie einfügen?:\n")
        print(entry)
        if entry in self.fragen.keys(): 
            print("Der Eintrag ist schon vorhanden.")
        else:
            self.fragen[entry] = input(f"Wie Lautet die Antwort zur Frage: {entry}?:\n")
            
    def PrintQuiz(self, name):
        if name == self.__Name:
            print(self.fragen)
            
        else:
            print("Dieser Name ist nicht vorhanden!")
        

print("Quiz")
#jn = input("Starten? [j]a  [n]ein")
optionen = input("[1]Spiel Starten\n[2]Fragen Hinzufügen:\n[3]Punktestand Anzeigen\n[4]Alle Fragen Anzeigen\n\n")
save1, save2, save3, save4 = "empty", "empty", "empty", "empty"
stand = input(f"Speicherstand Wählen: \n#1[{save1}]\t\t#3[{save3}]\n#2[{save2}]\t\t#4[{save4}]")
q1 = Quiz("Empty", 0) 
q2 = Quiz("Empty", 0)
q3 = Quiz("Empty", 0) 
q4 = Quiz("Empty", 0)
###Platz für Entrys###
#q1.AddEntry()
#print("______________")
###Games###
#q1.Start()
#q1.PrintQuiz("Tim")   
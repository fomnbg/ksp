class Restaurant():
    geoeffnet = False
    def __init__(self, restaurant_name, cuisine_type, seats):
        self.Restaurant_name = restaurant_name
        self.Cuisine_type = cuisine_type
        self.Seats = seats
        
    def describe_Restaurant(self):
        print(f"Der Name des Restaurants lautet \"{self.Restaurant_name}\", es handelt sich um {self.Cuisine_type}e Küche und das Restaurant hat {self.Seats} Sitze.\nOffen: {self.geoeffnet}\n")
        
    def open_restaurant(self):
        self.geoeffnet = True
        
    def close_restaurant(self):
        self.geoeffnet = False

    pass

class Eisdiele(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, seats, sorte):
        super().__init__(restaurant_name, cuisine_type, seats)
        self.Sorte = sorte
        
        
    def describe_Eisdiele(self):
        print(f"Der Name der Eisdiele lautet \"{self.Restaurant_name}\", es handelt sich um {self.Cuisine_type}es Eis und die Eisdiele hat {self.Seats} Sitze.\nEissorten: {self.Sorte}\nOffen: {self.geoeffnet}\n")
    pass 


R1 = Restaurant("Lucio's", "Italienisch", "27")
R2 = Restaurant("Backstube", "Deutsch", "12")
R3 = Restaurant("Peking Ente", "Chinesisch", "40")
S1 = Eisdiele("Gonzales", "Italienisch", "0", "Schoko, Vanillie, Erdbeere, Blau")
R1.open_restaurant()
S1.open_restaurant()
R1.describe_Restaurant()
R2.describe_Restaurant()
R3.describe_Restaurant()
S1.describe_Eisdiele()
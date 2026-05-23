'''
Created on 23-May-2026

@author: Vivek

Encapsulation: Restriction of access to class members (methods/ variables)

Capsule: 

1. Protected members: Can be accessed with in the same class or its child classes
    > add suffix single underscore(_) while defining the name
2. Private members: Can be accessed only within the same class
    > add suffix single underscore(__) while defining the name

Why?

To prevent data-manipulation/ data corruption
'''

class CarClass():
    __fuel_type = "Petrol"
    def __init__(self, name, color, model): # Constructor: method used to construct an Object
        print(f"A {color} color {name} car is created in the year {model}")
        self.name = name
        self.color = color
        self.model = model
        
        
    def start(self): # implemented method
        print(f"{self.name} is started")
        
    def move_forward(self): # implemented method
        print(f"{self.name} is moving forward")
        
    def move_backword(self): # implemented method
        print(f"{self.name} is moving backward")
        
    def stop(self): # implemented method
        print(f"{self.name} has stopped")


car1 = CarClass("Swift", "Red", "2026")
print(dir(car1))
print(car1._CarClass__fuel_type) # name mangling
car1._CarClass__fuel_type = "Water"
print(car1._CarClass__fuel_type)
print("CarClass.__fuel_type:", CarClass.__fuel_type)
CarClass.__fuel_type = "Water"
print("CarClass.__fuel_type:", CarClass.__fuel_type)


car2 = CarClass("Innova", "Silver", "2026")
print("CarClass.__fuel_type:", CarClass.__fuel_type)







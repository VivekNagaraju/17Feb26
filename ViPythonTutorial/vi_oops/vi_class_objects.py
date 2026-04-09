'''
Created on 09-Apr-2026

@author: Vivek

Type of car1: <class '__main__.CarClass'>
Type of f: <class 'list'>
'''

class CarClass:
    def __init__(self, name, color, model): # Constructor: method used to construct an Object
        print(f"A {color} color {name} car is created in the year {model}")
        self.name = name
        self.color = color
        self.model = model
        
    def start(self):
        print(f"{self.name} is started")
        
    def move_forward(self):
        print(f"{self.name} is moving forward")
        
    def move_backword(self):
        print(f"{self.name} is moving backward")
        
    def stop(self):
        print(f"{self.name} has stopped")
        
car1 = CarClass("Swift", "Red", 2026)   # Creation of object   
car1.start()    # calling the functions through object
print(type(car1))


car2 = CarClass("Thar", "Black", 2026)  
car2.start()  
car1.move_forward()
car2.move_forward()     
      
        
        
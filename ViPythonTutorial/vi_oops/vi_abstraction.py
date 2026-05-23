'''
Created on 22-May-2026

@author: Vivek

Abstraction:

Abstract:

Interfaces: Class containing abstract methods only
'''
from abc import ABC, abstractmethod


class CarClass(ABC):
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
    
    @abstractmethod    
    def drive_train(self): # unimplemented method
        pass
    
class HatchBackCar(CarClass):
    def drive_train(self):
        print("Front Wheel Drive(FWD) implemented")

swift = HatchBackCar("Swift", "white", 2026)
swift.start()
swift.drive_train()
    
    
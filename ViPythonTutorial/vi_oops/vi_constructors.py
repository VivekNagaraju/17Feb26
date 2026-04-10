'''
Created on 10-Apr-2026

@author: Vivek

Constructor: 

Constructor is a special/ magic method used to construct an object
Constructor is used for initial initializations that are required during object
creation

1. It is not mandatory to define a constructor
    - If constructor is not defined by the python will have the own constructor created    
2. Constructor is called implicitly during object creation
    - We can call a constructor explicitly if required
3. Constructor can be parameterised or non-parameterised
4. Constructor name should be __init__
'''
class Animal:
    def __init__(self):
        print("Animal class constructor is called")
        
    def eat(self):
        print("Animal is eating")
        
animal1 = Animal() # Creating an object
# animal1.eat()
# print(dir(animal1))
animal1.__init__()
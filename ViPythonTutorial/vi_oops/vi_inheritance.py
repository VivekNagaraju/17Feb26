'''
Created on 12-May-2026

@author: Vivek

Inheritance: 

1. Transfer of properties(methods, parameters, constructor) from Parent class to Child class
2. Using an Object from Child class we can call the properties from its Parent class

Types of inheritance:
1. Single level inheritance: GF -> F
2. Multi-level inheritance: GF -> F -> C
3. Multiple inheritance: F,M -> C

Method Resolution Order(MRO)
'''

class GrandFather:
    def __init__(self, name, age):
        print("Constructor is called")
        print(f"An Object is created with name:{name} and age:{age}")
        
    def gf_method(self):
        print("This is GrandFather method")
        
class Father(GrandFather):
    def __init__(self, name, age, dob):
        # print("Constructor is called")
        # print(f"An Object is created with name:{name}, age:{age}")
        super().__init__(name, age)
        print(f"Object born on {dob}")
        
    def f_method(self):
        print("This is Father method")
        
    def car_method(self):
        print("This is Father's car")
              
class Mother:
    def m_method(self):
        print("This is mother method")
        
    def car_method(self):
        print("This is Mother's car")
        
        
class Child(Father, Mother):
    def c_method(self):
        print("This is Child method")
        
    def car_method(self):
        print("This is Child's car")        

print("======GrandFather Object=======")        
ajja = GrandFather("Gaddappa", 110)
# ajja.gf_method()

print("======Father Object=======")
appa = Father("Nammappa", 65, "19/5/2000")
# appa.f_method()
# appa.gf_method()

print("======Mother Object=======")
amma = Mother()

print("======Child Object=======")
naanu = Child("Magu", 25, "19/5/2026")
# naanu.c_method()
# naanu.f_method()
# naanu.gf_method()
# naanu.m_method()
# naanu.car_method()

print("=====Method Resolution Order(MRO)=====")
print(Child.mro())


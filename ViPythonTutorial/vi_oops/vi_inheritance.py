'''
Created on 12-May-2026

@author: Vivek

Inheritance: 

1. Transfer of properties(methods, parameters, constructor) from Parent class to Child class
2. Using an Object from Child class we can call the properties from its Parent class
'''
class GrandFather:
    def gf_method(self):
        print("This is GrandFather method")
        
class Father(GrandFather):
    def f_method(self):
        print("This is Father method")

print("======GrandFather Object=======")        
ajja = GrandFather()
ajja.gf_method()

print("======Father Object=======")
appa = Father()
appa.f_method()
appa.gf_method()


'''
Created on 17-Jun-2026

@author: Vivek

Types of variables:

1. Method variable/ local variable: Variables having scope within a method Ex: name, roll_no, kannada, english, maths
2. Instance variable/ object variable: Scope is within an object. Defined using 'self' keyword. Ex: self.name
3. Class variable/ static variable: Scope is within the class. Defined within a class but outside of methods(constructor). Ex: school_name
    Note: 
        Usage: We need to call a class variable using class name.
4. Global variable: Scope is in the entire program (.py file). Defined outside of all classes and methods. Ex: city
'''

city = "Mysuru"

class Student:
    school_name = "iQuest"
    def __init__(self, name, roll_no):
        print(f"A student got admitted to {Student.school_name} in {city}")
        print(f"A Student object is created with name: {name} and roll_no: {roll_no}")
        self.name = name
        self.roll_no = roll_no
        
    def calculate_total_marks(self, kannada, english, maths):
        self.total_marks = kannada + english + maths 
        print(f"total_marks attained by {self.name}:", self.total_marks)
      
    def show_percentage(self): 
        percentage = (self.total_marks/3)
        print(f"Percentage:", percentage)
        
std1=Student("Vivek", 21)
std1.calculate_total_marks(125, 35, 85)
std1.show_percentage()
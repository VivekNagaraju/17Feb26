'''
Created on 23-Mar-2026

@author: Vivek

Functions: A function is a group of statements or a block of code which perform 
            certain task
            
    Ads:
        1. Reduce code repetition and increase code re-usability
        2. Maintainance will be easier
        
    Types of functions:
        1. Pre-defined functions: Available at the time of Python installation
            Ex: print(), id(), type()........
        2. User defined functions: Defined by users
            Ex: add()
    
    Syntax:
        def function_name(parameters):
            function_body
            
        def - keyword - mandatory
        function_name - Name of the function - mandatory
        () - parenthesis - mandatory
        : - colon - mandatory
        paramters(Ex: a,b)- variables which accepts/ recieve values passed to a function
                         - not mandatory
        function_body - block of code - not mandatory - pass (keyword)
        
    After defining a function we can call it using its name by passing the parameters if required   
'''
a = 4
b = 7
print(f"Sum of {a} and {b}:",a+b)

c = 47
d = 76
print(c+d)

e = 87
f = 54
print(e+f)

def add(a, b): # defining the function
    print(f"Sum of {a} and {b}:",a+b)
    
# calling the function
add(34, 56)
add(23, 14)






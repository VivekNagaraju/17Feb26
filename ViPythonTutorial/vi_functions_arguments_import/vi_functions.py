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
    
Return Keyword: using return a function can return value to the user 

1. A function can call another function
2. We can pass a function as a parameter/ value to another function
3. We can assign a function to a variable
4. We can define a function inside another function
5. We can return a function from another function
6. A function calling the same function - recursive functions

Ex: Factorial: 
    4!  = 4*3*2*1
        = 4*3!
        = 4*3*2!
        = 4*3*2*1!
        = 4*3*2*1*0!
        
    n! = n*(n-1)!
    
Q. Write a program to find the factorial of any integer

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

def add(a, b): # defining the function # function with parameters
    # print(f"Sum of {a} and {b}:",a+b)
    c = a+b
    return c
    
    
def start_msg(): # Function without parameters
    print("Welcome to iQuest!!")
    def sec_msg():
        print("Let's start programming...")
    sec_msg()
    
def mul(a, b):
    c = a*b
    return c

def composite(a, b): # calling a function inside another function
    # start_msg() 
    # print(add(a, b))
    # print(mul(a, b))
    c = add(a, b)
    d = mul(a, b)
    return c, d
    
def first_fun():
    def sec_fun():
        print("This is sec function")   
    return sec_fun


# calling the function
start_msg() 
print(add(34, 56))
# d = add(23, 14)
# print(d*2)
print("========Composite function========")
print(composite(10, 20))
e, f = composite(10, 20)
print(e)
print(f)

g = add # Assigning function to a variable
print(g(100, 200)) # call the function using new variable

h = first_fun() # h = sec_fun # Assigning function to a variable
h() # call the function using new variable

'''
Factorial: 
    4!  = 4*3*2*1
        = 4*3!
        = 4*3*2!
        = 4*3*2*1!
        = 4*3*2*1*0!
        
    n!  = n*(n-1)! when n != 0
    n!  = 1 when n = 0
    
    4!  = 4*factorial(3)
        = 4*3*factorial(2)
        = 4*3*2*factorial(1)
        = 4*3*2*1*factorial(0)
        = 4*3*2*1*0*factorial(-1)
'''

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

print("factorial(4):",factorial(4))
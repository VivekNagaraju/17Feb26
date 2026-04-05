'''
Created on 31-Mar-2026

@author: Vivek

Function arguments:

Argument = variables/ values which are used inside function parenthesis 

1. Formal arguments: Variables/ parameters defined inside function parenthesis which receives the values sent from function call
    a. Default arguments
    b. Variable length arguments
    c. Keyword Variable length arguments
2. Actual arguments: Values/ parameters passed during function call
    a. Positional arguments
    b. Keyword arguments

Ex:

def add(a, b): # a, b --> formal arguments
    c = a+b
    return c
    
print(add(4, 5)) # 4, 5 --> actual arguments
'''
def add(a=0, b=0): # Default arguments
    c = a+b
    return c

def sub(a, b):
    c = a-b
    return c

'''    
print(add(4, 5))
print(sub(4, 5)) # Positional arguments
print(sub(b=4, a=5)) # Keyword arguments
print(add())
print(add(6))
print(add(6,9))
# print(add(6,9,10))
print()
print(1)
print(1, 3, 4)
print(5, 3, 4, 5, 2)
'''
#Variable length arguments
def var_len(*a): # we can pass any number of positional arguments
    print(a)
# var_len(1, 2, 3, 4, 6)
# var_len(1, 2)
# var_len(x=1, y=2) #TypeError: var_len() got an unexpected keyword argument 'x'
# Q. Define an add function which accepts any number of values and gives the total

# Varial length keyword arguments
def kw_var_len(**a): # we can pass any number of keyword arguments
    print(a)

# kw_var_len(x=3, y=8, z=9)
# kw_var_len(3) #TypeError: kw_var_len() takes 0 positional arguments but 1 was given

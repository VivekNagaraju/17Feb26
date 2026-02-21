'''
Created on 19-Feb-2026

@author: Vivek

Variables: A name given to the memory location which stores value

Syntax:

variable_name = value

Invalid cases:

1. value = variable_name  EX: 30 = g
2. Variable name should not start with number Ex: 2nd_variable = 27
'''

# Creating a variable - initialization
a = 10
b = 20
print(a+b) # add the above 2 variables

c, d = 4, 5 # defining multiple variables in a single line
print(c)
print(d)

e = f = 20 # assigning single value for multiple variables
print(e)
print(f)

print(id(e))
print(id(f))

# variable2 = 27

f = 48 # re-initialization
print(id(f))





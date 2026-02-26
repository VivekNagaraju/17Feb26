'''
Created on 25-Feb-2026

@author: Vivek

Looping statements(LS): LS are used to execute any statements repeatedly

A loop will be executed repeatedly until a condition is fulfilled

Types of LS:

1. While loop:
    a. Initial variable
    b. Condition
    c. Increment/ decrement
2. For loop

Infinite Loop: Loop never stops execution

'''
'''
count = 0 # Variable initialization

while count < 5 : # Defining condition
    print("My name is Vivek")
    # count = count + 1 # Increment
    count += 1
'''
'''
# Infinite loop creation:

# Case 1:

count = 5

while count > 0:
    print("My name is Vivek")
    count += 1
    
# Case 2:

count = 0

while count < 5:
    print("My name is Vivek")
    count -= 1

# Case 3: Intentionally created

while True:
    print("My name is bharath")
    
'''
'''
# No Output
count = 5
while count > 5:
    print("My name is bharath")
    # count = count + 1 # Increment
    count = count + 1    
'''




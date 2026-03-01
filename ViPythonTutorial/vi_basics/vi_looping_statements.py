'''
Created on 25-Feb-2026

@author: Vivek

Looping statements(LS): LS are used to execute any statements repeatedly

A loop will be executed repeatedly until a condition is fulfilled

Types of LS:

1. While loop
    Components of while loop:
        a. Initial variable
        b. Condition
        c. Increment/ decrement
2. For loop: to iterate over a sequence/ range

Infinite Loop: Loop never stops execution

range:
    start: from where sequence should start; default = 0
    stop: end point. No default value (mandatory use should pass)
    step: difference b/w sequence of integers produced; default = +1
    
Loop control statements/ keywords: control the execution of loops
- break: Break the execution of a loop once for all when a condition is satisfied
- continue: skip the execution of statements for one particular iteration.
        Once continue statement is executed statements after that will be skipped
        for that particular iteration. Loop will continue normally after that.
        
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

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
'''
for i in range(1, 100):
    if i == 50:
        break
    print(i)
'''
'''
i = 1
while i<=100:
    if i == 50:
        i += 1
        continue
    print(i)   
    i += 1
'''

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

1. Print star 5 times in a row --> for loop
2. Switch to next line --> print()
3. repeat Step 1 and 2 , 4 times --> use for loop

'''   
''' 
i = 0
while i <= 4:
    print("* * * * *")
    i += 1
'''
'''
for i in range(5):
    print("* * * * *")
'''
'''
for j in range(5): # No. of lines
    for i in range(5): # No. of stars
        print("*", end=" ")    
    print()
'''
'''
*
* *
* * *
* * * *
* * * * *
'''
for j in range(1, 6): # No. of lines
    for i in range(j): # No. of stars
        print("*", end=" ")    
    print()
    
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
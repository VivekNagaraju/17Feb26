'''
Created on 23-Feb-2026

@author: Vivek

Conditional statements: Statements based on a condition from which flow of program execution will be decided
Conditional statements are also called as decision-making statements.

We define conditions using 'if' keyword.

Syntax:
 
 if <condition>:
    code

Indentation: Leading spaces(spaces given at the beginning of any statement) given to define a block of code
'''
age = int(input("Please enter your age:"))
'''
if age >= 18:
    print("You're an adult")
else:
    print("You're not an adult")
'''
if age > 0:
    if age <= 3:
        print("You're an infant")
        
    elif age <= 12:
        print("You're a child")
        
    elif age <= 18:
        print("You're a teen")
        
    elif age <= 60:
        print("You're an adult")
        
    else:
        print("You're a senior citizen")
        
else:
    print("Please enter a valid integer greater than Zero")

    

'''
Created on 11-Mar-2026

@author: Vivek

Dictionary: is used to group together key-value pair elements

dictionary = {key1:value1, key2:value2,....}

Creation:
    1. An empty dictionary can be created
    2. Dictionary with elements:
        - any data-type can be used for key/ value
        - duplicate keys are not allowed (key should always be unique) 
        
Accessing:
    1. Using keys
    2. Using loops
    
Modification: is done using keys
    - when an existing key is used its value will be updated
    - when a new key is used, new set of key-value pair will be added to the dictionary
     
'''
# Dictionary with elements
a = {1:"Bharath", 2:"Srinidhi", 3:"Vivek", 3:"Manju"}
print("a:", a)
print(type(a))

salary = {"Bharath": 10000, "Srinidhi":10000, "Vivek":5000}
print("salary:", salary)

print(salary["Bharath"])
print(a[2])

print("=====Accessing using loop=======")
for i in a:
    print(i)

for i in a.values():
    print(i)

print("========Modification=======")
salary["Bharath"] = 20000
print("salary:", salary)

salary["Manju"] = 30000
print("salary:", salary)

print("======Pre-defined functions======")
print("salary.items():",salary.items())
print("salary.keys():",salary.keys())
print("salary.values():",salary.values())
print(salary.popitem())
print("salary:", salary)
print(salary.pop("Vivek"))
print("salary:", salary)
# print(salary.pop("Vivek")) # KeyError: 'Vivek'
# print("salary:", salary)
print(salary.pop("Vivek", "Key is not present"))
print("salary:", salary)

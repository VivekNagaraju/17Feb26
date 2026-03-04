'''
Created on 04-Mar-2026

@author: Vivek

List:

Creation:
    1. An empty list can be created
    2. List with data elements:
        a. Homogeneous
        b. Heterogeneous
    3. using built-in function
    
Accessing: Fetching elements from a DS
    1. Using Loops
    2. Using Index:
        - Position value of a data element in a DS
        Types of Indexing
        a. Positive index: Left -> Right; starts with 0, 1, 2...
        b. Negative index: Right -> Left; starts with -1, -2, -3....
    
'''
a = [] # Creating an empty list
print(a)
print(type(a))

b = [3, 4, 5, 56, 87] # Homogeneous list
print("b:", b)
print(type(b))

c = [3, 4.5, "Vivek", 6+7j, True, None] # Heterogeneous list
print("c:", c)

# Create a list using built-in function
d = list(range(10))
print("d:", d)

# Accessing using for loop

for i in c:
    print(i)

# Accessing using Index: ds_name[index_value]
print("d[5]:", d[5])
print("d[-5]", d[-5])
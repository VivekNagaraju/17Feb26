'''
Created on 04-Mar-2026

@author: Vivek

List:

Creation:
    1. An empty list can be created
    2. List with data elements:
        a. Homogeneous list can be created
        b. Heterogeneous list can be created
        c. List can have duplicate elements
    3. List can be created using built-in function
    
Accessing: Fetching elements from a DS
    1. Using Loops
    2. Using Index:
        - Position value of a data element in a DS
        Types of Indexing
        a. Positive index: Left -> Right; starts with 0, 1, 2...
        b. Negative index: Right -> Left; starts with -1, -2, -3....
    3. Using slicing operator: to access group of elements based on index values
        Syntax: list_name[start_index : stop_index : step_value]
        start_index: default value: 0/-1; inclusive
        stop_index: default value: len(list)/-(len(list)+1) ; exclusive
        step_value: default value: +1
        
        when step is +ve: start_index  < stop_index
        when step is -ve: start_index  > stop_index
        
Modification:
    - Re-initialization using index
    - List is mutable: list once created can be modified
    
        
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

'''
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
'''
print("======Accessing using while loop========")
index = 0
while index < len(b) :
    print(b[index])
    index += 1

print("======Accessing using slicing operator=======")
print("c:", c)
print("c[::]:", c[::])
print("c[:5:]:", c[:5:])
print("c[:6:]:", c[:6:])
print("c[::2]:", c[::2])
print("c[-1:-7:-1]:", c[-1:-7:-1])
print("c[::-1]:", c[::-1])
print("c[0:7:1]:", c[0:7:1])
print("c[-1:-7:]:", c[-1:-7:])
print("c[-2:-7:]:", c[-2:-7:])
print("c[-7:-1:]:", c[-7:-1:])

c[4] = False
print("c:", c)

print("========Predefined  functions========")
print("b:", b)
b.append(99)
print("b:", b)
b.extend(c)
print("b:", b)
b.append(c)
print("b:", b)
print("b.count(3):", b.count(3))
print("b.index(3):", b.index(3))
print("b.index(3, 1):", b.index(3, 1))
# b.index(value, start, stop)
b.insert(5, 101)
print("b:", b)

f = [2, 4, 5, 6, 2, 4, 7, 8, 9, 9, 28, 7, 9]
# Print above list in the console
# Ask user to select a number from the displayed list and take the input
# Display the number of occurrences of the element selected
# Display the indices of the element in the list 

print("Type of f:", type(f))

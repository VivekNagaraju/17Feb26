'''
Created on 21-Feb-2026

@author: Vivek

Data-type: Category to which a data belongs to.

Types of data:

Fundamental data types: 
1. int - 10, 20, -10, -20
2. float - 0.3, 4.5, -5.6
3. boolean -True, False 
4. string - 
5. complex numbers - a+bj

Why we need to determine type of a data?
- based on data types certain operations will be performed
- based on data types certain memory location will be allotted 

Dynamically Typing:
- In python type of a data is determined during runtime


'''
a = "vivek"
print(a)
print(type(a))

a = 10
print(a)
print(type(a))

b = 4.5
print(b)
print(type(b))

c = True
print(c)
print(type(c))

d = 4+7j
print(d)
print(type(d))

# Type casting: converting one data type into another data type
e = float(a)
print(e)
print(type(e))

f = "4"
print(f)
print(type(f))

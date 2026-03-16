'''
Created on 14-Mar-2026

@author: Vivek

Strings:

Single line strings
''
""

Multi line strings
''' '''
""" """
p = i + 1
j = 1
i = 0
p = 1

j = 2
i = 0, 1
p = 2, 3

j = 3
i = 0, 1, 2
p = 4, 5, 6

j = 4
i = 0, 1, 2, 3
p = 7, 8, 9, 10

1
2 3
4 5 6
7 8 9 10

He said,"Yes"!!

'''

name1 = 'Vivek'
name2 = "Manju"
address = """c/o iQuest,
            near Infosys
            Mysuru"""
name3 = "nagaraju"
print("name1:",name1)
print(type(name1))
print("name2:",name2)
print("name3:",name3)
print(type(name3))
print("address:", address)
print(type(address))

print("name1[2]:",name1[2])

cap_name3 = name3.capitalize()
print("cap_name3:", cap_name3)
print("name3:",name3)

print("address.casefold():",address.casefold())

print("address.lower():", address.lower())

text_german = "Straße" # German for "street"

print("text_german.casefold():",text_german.casefold())
print("text_german.lower():",text_german.lower())

print("address.swapcase():", address.swapcase())

print('name1.center(25, "="):', name1.center(25, "="))

print('name1.ljust(25, "="):', name1.ljust(25, "="))

print('name1.rjust(25, "="):', name1.rjust(25, "="))

print('He said,"Yes"!!')



'''
Created on 22-Feb-2026

@author: Vivek

Operator: A symbol which performs operation on one or more operand/s

Operations:
1. Arithmetic operation: addition(+), subtraction(-), multiplication(*), division(/), modulus(%), exponential(**), integer/ floor division(//); i/p - numerical; o/p - numerical
2. Comparison/ relational operation: >, <, ==, >=, <=, !=; i/p: numerical, o/p: boolean;
3. Logical operation: and (&), or (|), not; i/p: Boolean, o/p: Boolean
4. Membership operation: in, not in - check for an element in a group
5. Identity operation: is, is not - check whether 2 variables/ objects identical
6. Negation operation: -
7. Assigning operation: =
'''

a = 200
b = -3
c = a+b 
print(f'Sum of {a} and {b} is', c)

print(True and False)
print(True & False)

print(not False)

d = False
e = True
f = not(d and e)
print(f)

print(True | False)

print('i' in 'Vivek')
print('I' in 'Vivek') # False # Case sensitive

a = b = 10
print(a is b)
c = '10'
print(a is c)
print(a == c)


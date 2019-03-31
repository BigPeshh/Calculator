from sympy import *

x = Symbol('x')

a = input("Equation: ")

print("First Derivative: ", diff(a, x, 1))
print("Second Derivative: ", diff(a, x, 2))
print("Thrid Derivative: ", diff(a, x, 3))

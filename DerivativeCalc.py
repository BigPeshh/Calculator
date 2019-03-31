from sympy import *

x = Symbol('x')
a = int(input("Coefficient: "))
n = int(input("Exponent: "))
f = a*x**n

df = f.diff(x)
print("First Derivative: ", df)

d2f = df.diff(x)
print("Second Derivative: ", d2f)

d3f = d2f.diff(x)
print("3rd Derivative: ", d3f)

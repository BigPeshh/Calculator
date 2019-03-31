import sympy as sp

print("====================================================")
print("            System of 3 Linear Equations            ")
print("====================================================")
print(" ")

eq1 = sp.Function('eq1')
eq2 = sp.Function('eq2')
eq3 = sp.Function('eq3')

x, y, z = sp.symbols('x y z')

print("Equation 1")
a = float(input("Coefficent of x:"))
b = float(input("Coefficent of y:"))
c = float(input("Coefficent of z:"))
d = float(input("Coefficent of constant:"))
print("Equation 2")
e = float(input("Coefficent of x:"))
f = float(input("Coefficent of y:"))
g = float(input("Coefficent of z:"))
h = float(input("Coefficent of constant:"))
print("Equation 3")
i = float(input("Coefficent of x:"))
j = float(input("Coefficent of y:"))
k = float(input("Coefficent of z:"))
l = float(input("Coefficent of constant:"))

eq1 = sp.Eq(a*x + b*y + c*z, d)
eq2 = sp.Eq(e*x + f*y + g*z, h)
eq3 = sp.Eq(i*x + j*y + k*z, l)
print(eq1)
print(eq2)
print(eq3)

row1 = [a, b, c, d]
row2 = [e, f, g, h]
row3 = [i, j, k, l]
print(row1)
print(row2)
print(row3)

system = sp.Matrix((row1, row2, row3))
print(sp.solve_linear_system(system, x, y, z))
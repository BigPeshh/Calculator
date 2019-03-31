import sympy as sp

print("====================================================")
print("            System of 2 Linear Equations            ")
print("====================================================")
print(" ")

eq1 = sp.Function('eq1')
eq2 = sp.Function('eq2')

x, y = sp.symbols('x y')

print("Equation 1")
a = float(input("Coefficent of x:"))
b = float(input("Coefficent of y:"))
c = float(input("Coefficent of constant:"))
print("Equation 2")
d = float(input("Coefficent of x:"))
e = float(input("Coefficent of y:"))
f = float(input("Coefficent of constant:"))

eq1 = sp.Eq(a*x + b*y, c)
eq2 = sp.Eq(d*x + e*y, f)
print(eq1)
print(eq2)

row1 = [a, b, c]
row2 = [d, e, f]
print(row1)
print(row2)

system = sp.Matrix((row1, row2))
print(sp.solve_linear_system(system, x, y))






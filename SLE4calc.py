import sympy as sp

print("====================================================")
print("            System of 4 Linear Equations            ")
print("====================================================")
print(" ")

eq1 = sp.Function('eq1')
eq2 = sp.Function('eq2')
eq3 = sp.Function('eq3')
eq4 = sp.Function('eq4')

x, y, z, w = sp.symbols('x y z w')

print("Equation 1")
a = float(input("Coefficent of x:"))
b = float(input("Coefficent of y:"))
c = float(input("Coefficent of z:"))
d = float(input("Coefficent of w:"))
e = float(input("Coefficent of constant:"))
print("Equation 2")
f = float(input("Coefficent of x:"))
g = float(input("Coefficent of y:"))
h = float(input("Coefficent of z:"))
i = float(input("Coefficent of w:"))
j = float(input("Coefficent of constant:"))
print("Equation 3")
k = float(input("Coefficent of x:"))
l = float(input("Coefficent of y:"))
m = float(input("Coefficent of z:"))
n = float(input("Coefficent of w:"))
o = float(input("Coefficent of constant:"))
print("Equation 4")
p = float(input("Coefficent of x:"))
q = float(input("Coefficent of y:"))
r = float(input("Coefficent of z:"))
s = float(input("Coefficent of w:"))
t = float(input("Coefficent of constant:"))

eq1 = sp.Eq(a*x + b*y + c*z + d*w, e)
eq2 = sp.Eq(f*x + g*y + h*z + i*w, j)
eq3 = sp.Eq(k*x + l*y + m*z + n*w, o)
eq4 = sp.Eq(p*x + q*y + r*z + s*w, t)
print(eq1)
print(eq2)
print(eq3)
print(eq4)

row1 = [a, b, c, d, e]
row2 = [f, g, h, i, j]
row3 = [k, l, m, n, o]
row4 = [p, q, r, s, t]
print(row1)
print(row2)
print(row3)
print(row4)

system = sp.Matrix((row1, row2, row3, row4))
print(sp.solve_linear_system(system, x, y, z, w))
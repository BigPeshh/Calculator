import sympy as sp 

print("====================================================")
print("               Integral Calculator                  ")
print("====================================================")
print(" ")

x = sp.Symbol('x')
f = input("Equation: ")
g = sp.integrate(f, x)
h = sp.integrate(g, x)

print("First Integration: ", sp.integrate(f, x))
print("Second Integration: ", sp.integrate(g, x))
print("Third Integration: ", sp.integrate(h, x))

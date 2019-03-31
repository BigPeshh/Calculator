import numpy as np 

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def scalx(n, x):
    return n*x
def scaly(m, y):
    return m*y

print("====================================================")
print("                 Matrix Operations                  ")
print("====================================================")
print("  Please select the number of the operation needed  ")
print("____________________________________________________")
print(" ")
print("                  1. Addition                       ")
print("                 2. Subtraction                     ")
print("               3. Multiplication                    ")
print("            4. Scalar Multiplication                ")
print("____________________________________________________")

choice = int(input("Operation: "))
print("Separate columns by commas and rows by semi-columns")
x = np.matrix(float(input("Matrix 1: ")))
y = np.matrix(float(input("Matrix 2: ")))
n = float(input("Scalar for Matrix 1: "))
m = float(input("Scalar for Matrix 2: "))

if choice == '1':
    print(add(x, y))
elif choice == '2':
    print(sub(x, y))
elif choice == '3':
    print(mult(x, y))
elif choice == '4':
    print(scalx(n, x))
    print(scaly(m, y))

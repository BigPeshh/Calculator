import sympy as sp

print("====================================================")
print("             System of Linear Equations             ")
print("====================================================")
print("   Please select the number of the choice needed    ")
print("____________________________________________________")
print(" ")
print("                  1. Two Equations                  ")
print("                 2. Three Equations                 ")
print("                  3. Four Equations                 ")
print("____________________________________________________")

choice = int(input("Number of Equations: "))

if choice == '1':
    import SLE2calc
elif choice == '2':
    import SLE3calc
elif choice == '3':
    import SLE4calc

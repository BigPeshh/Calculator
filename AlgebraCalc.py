print("====================================================")
print("                Algebra Calculator                  ")
print("====================================================")
print("  Please select the number of the operation needed  ")
print("____________________________________________________")
print(" ")
print("           1. System of Linear Equations            ")
print("                 2. Matrices                        ")
print("____________________________________________________")

choice = int(input("Operation Number: "))

if choice == '1':
    import SLEcalc
if choice == '2':
    import MatrixCalc
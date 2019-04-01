print("====================================================")
print("                Calculus Calculator                 ")
print("====================================================")
print("  Please select the number of the operation needed  ")
print("____________________________________________________")
print(" ")
print("                   1. Derivative                    ")
print("                  2. Integration                    ")
print("____________________________________________________")

choice = int(input("Operation Number: "))

if choice == '1':
    import DerivativeCalc
elif choice == '2':
    import IntegralCalc

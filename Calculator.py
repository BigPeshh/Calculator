print("====================================================")
print("                     Calculator                     ")
print("====================================================")
print("   Please select the number of the choice needed    ")
print("____________________________________________________")
print(" ")
print("                1. Basic operations                 ")
print("            2. System of Linear Equations           ")
print("                3. Matrix Calculator                ")
print("              4. Derivative Calculator              ")
print("____________________________________________________")

choice = input("Choice: ")

if choice == '1':
    import BasicOperations
elif choice == '2':
    import SLEcalc
elif choice == '3':
    import MatrixCalc
elif choice == '4':
    import DERIVcalc
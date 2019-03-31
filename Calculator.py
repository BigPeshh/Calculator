print("====================================================")
print("                     Calculator                     ")
print("====================================================")
print("   Please select the number of the choice needed    ")
print("____________________________________________________")
print(" ")
print("                1. Basic Operations                 ")
print("              2. Advanced Operations                ")
print("               3. Algebra Calculator                ")
print("               4. Calculus Calculator               ")
print("____________________________________________________")

choice = int(input("Choice: "))

if choice == '1':
    import BasicOperations
elif choice == '2':
    import AdvancedOperations
elif choice == '3':
    import AlgebraCalc
elif choice == '4':
    import CalculusCalc

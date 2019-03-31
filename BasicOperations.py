# define addition, subtraction, multiplication, and division

def add(x, y):
   return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y

print("====================================================")
print("                 Basic Operations                   ")
print("====================================================")
print("  Please select the number of the operation needed  ")
print("____________________________________________________")
print(" ")
print("                  1. Addition                       ")
print("                 2. Subtraction                     ")
print("               3. Multiplication                    ")
print("                  4. Division                       ")
print("____________________________________________________")

op = input("Operation: ")

num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))

if op == '1':
    print(num1, "+", num2, "=", add(num1,num2))
elif op == '2':
    print(num1, "-", num2, "=", sub(num1,num2))
elif op == '3':
    print(num1, "*", num2, "=", mult(num1,num2))
elif op == '4':
    print(num1, "/", num2, "=", div(num1,num2))
else:
    print("ERROR: SELECT AN OPERATION ON THE LIST")
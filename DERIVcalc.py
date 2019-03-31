def derivative():
    a = float(input("Coefficient: "))
    n = float(input("Exponent: "))
    if n > 1:
        print("Derivative: ", a*n, "x^", n-1 )
    elif n == 0:
        print("Derivative: 0")
    elif n == 1:
        print("Derivative: ", a)
    elif n < 0:
        print("Derivative: ", a*n, "/x^", abs(n-1))
derivative()
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Sorry factorial for negative values is not available")
elif n == 0:
    print("The factorial for zero is 1")
else:
    for i in range(1, n+1):
        factorial = factorial * i
    print(f"The factorial of", n, "is", factorial)


x = int(input("Enter a number you want:"))

factorials = 1
if x < 0:
    print("Factorial for negative values is not available")
elif x == 0:
    print("Factorial for zero results 1")
else:
    for i in range(1, x+1):
        factorials = factorials * i
    print("The factorials for the entered number is :", factorials)

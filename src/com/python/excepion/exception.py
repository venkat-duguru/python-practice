try:
    number1 = eval(input("Enter first number"))
    number2 = eval(input("Enter second number"))
    result = number1 + number2
    print(result)
except Exception as e:
    print(e)

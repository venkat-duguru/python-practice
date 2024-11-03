try:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    result = a/b


except Exception as e:
    print("value error")
else:
    print(f"Result is {result}")
finally:
   print("Whatever it is i will executed")


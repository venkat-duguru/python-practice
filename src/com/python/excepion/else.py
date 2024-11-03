try:
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
    result = a/b
except Exception as zde:
    print("Zero division error")
else:
    print(result)

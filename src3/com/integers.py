n = int(input("Enter a number: "))
if n == 0 or n == 1:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            print(i, 'times', n // i, 'is', n)
            break
    else:
        print(n, "is a prime number")

else:
    print(n, "is not a prime number")


numb = int(input("Enter a number: "))
if numb == 0 or numb == 1:
    print(numb, "is not a prime number")
elif n > 1:
    for i in range(2, numb):
        if (numb % i) == 0:
            print(numb, "is not a prime number")
            print(i, 'times', numb // i, 'is', numb)
            break
    else:
        print(numb, "is a prime number")
else:
    print(numb, "is not a prime number")
    
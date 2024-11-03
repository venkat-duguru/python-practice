def fibonacci(n):
    if n < 0:
        print("Invalid input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(9))


#write a program for fibonacci series
n = int(input("Enter a number: "))
n1, n2 = 0, 1
print("Fibonacci series", n1, n2, end=" ")
for i in range(2, n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()


#Reverse for the above program
x = int(input("Enter a number: "))
for i in range(x, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

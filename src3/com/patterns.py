n = int(input("Enter a number"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


x = int(input("Enter a number"))
for i in range(x, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()


#print a tiangle shape with
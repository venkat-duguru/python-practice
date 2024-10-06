#Program1 write a program to print square shape with '*' symbol
n = int(input("Enter number of rows :"))
for i in range(1, n+1):
    print("*"*n)

#Program2 write a program to print numbers for 'n' no of times in 'n' no of rows
n = int(input("Enter number of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, end=' ')
    print()

#Program3 write a program to print 'n' numbers in 'n' no of rows
n = int(input("Enter number of rows you want:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end=' ')
    print()

#Program4 write a program to print 'n' numbers in descending order in 'n' no of rows
a = int(input("enter number of rows"))
for i in range(1, a+1):
    for j in range(1, a+1):
        print(a+1-j, end=" ")
    print()

#Program5 write a program to print 'n' numbers for 'n' no of times in a row in descending order
n = int(input("Enter number of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(a+1-i, end=" ")
    print()

#Program6 write a program to print right angeled triangle shape
n = int(input("Enter number of rows :"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

#Program7
n = int(input("Enter no of rows:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#Program8
n = int(input("Enter number of rows:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64 + j), end=' ')
    print()

#Program9
n = int(input("Enter number of rows:"))
for i in range(1, n +1):
    for j in range(1, i+1):
        print(chr(64+i), end=" ")
    print()

#Program10
n = int(input("Enter number of rows :"))
for i in range(1, n+1):
    print(""*(i-1), end=" ")
    for j in range(65, 66+n-i):
        print(chr(j), end=" ")
    print()
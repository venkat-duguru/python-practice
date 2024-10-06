#Program Find maximum of the given numbers by using ternary operator
a = int(input("Enter first value"))
b = int(input("Enter second value"))
max = a if a > b else b
print("Maximum value is:", max)


#Program Find minimum of given numbers using ternary operator
a = int(input("Enter first number :"))
b = int(input("Enter second number:"))
min = a if a < b else b
print(f"minimum value : {min}")


#Program to find maximum from three different numbers using ternary operator
a = int(input("Enter first value:"))
b = int(input("Enter second value:"))
c = int(input("Enter third value:"))
max = a if a > b and a > c else b if b > c else c
print(f"Maximum value is : {max}")


#Program to find minimum value from three different values using ternary operator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
min = a if a < b and a < c else b if b < c else c
print("Minimum value is", min)

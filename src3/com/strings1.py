s = input("Enter a string: ")
s1 = " "
for i in s:
    s1 = i + s1
print(s1)


a = "Anchor"
a1 = " "
for i in a:
    a1 = i + a1
print(a1)


#write a program to find a factorial for a number
n = int(input("Enter a number for factorial: "))
factorial = 1
if n < 0:
    print("The factorial for negative numbers is not available")
elif n == 0:
    print("The factorial for zero is 1")
else:
    for i in range(1, n+1):
        factorial = factorial * i
print(f"The factorial for {n} is: ",factorial)


#Write a program on fizz and buzz concept
for i in range(1, 101):

    if (i % 15) == 0:
        print("FizzBuzz")
    elif (i % 3) == 0:
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")
    else:
        print(i)


#swapping of 2 variables
x = 5
y = 10
x, y = y, x
print("after swapping value of x is ", x)
print("after swapping value of y is ", y)


#or
x = 1
y = 2
x = x + y
y = x - y
x = x - y
print(x)
print(y)


#for three numbers
s = 11
t = 12
u = 13
s = s + t + u
t = s - t - u
u = s - t - u
s = s - t - u
print(s)
print(t)
print(u)


#swap the case of a string
s = input("Enter a string: ")
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.casefold())

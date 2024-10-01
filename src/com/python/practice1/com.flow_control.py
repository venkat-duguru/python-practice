#Program print a string as an iterable
string = "Python is Versatile"
for x in string:
    print(x)

#Program to find factorial of a number
number = int(input("Enter a number:"))

factorial = 1
if number < 0:
    print("Sorry, factorial does not exist for negative number")
elif number == 0:
    print("The factorial for zero is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i

    print(factorial)

#Program to find Grade by using marks
marks = int(input("Enter marks of a student to know grade"))
if marks >= 90:
    print("Its A Grade")
elif marks >= 80:
    print("Its B Grade")
elif marks >= 70:
    print("Its C Grade")
elif marks >= 40:
    print("Its D Grade")
else:
    print("Its Fail")

#Program to find sum of first n natural numbers
N = int(input("Enter a number: "))
sum = 0
for i in range(1, N+1):
    sum = sum + i
print(sum)


#Program using flow controls if and else
name = input("Enter name:")
if name == "Venkat":
    print("Hello Venkat Goog Morning")
    print("How are you?")
else:
    print("Hi")
    print("Bye")

#Program using if, elif, else
brand = input("Enter your favourite brand:")
if brand == "RC":
    print("It is children's brand")
elif brand == "KF":
    print("It not gives that much kick")
elif brand == "KO":
    print("It is too light to drink")
elif brand == "FO":
    print("Buy one get one free")
else:
    print("Try other Brands")

#Program
n1 = eval(input("Enter first number:"))
n2 = eval(input("Enter second number:"))
n3 = eval(input("Enter third number:"))
if n1 > n2 and n1 > n3:
    print("Biggest number is", n1)
elif n2 > n3 and n2 > n1:
    print("Biggest number is", n2)
else:
    print("Biggest number is", n3)

#Program Check whether the given number is in between 1 and 100 or not
n = int(input("Enter a number:"))
if (n > 1) and (n < 100):
    print("The number", n, "is in between 1 and 100")
else:
    print("The number", n, "is not in between 1 and 100")

#Program
n = int(input("Enter a number:"))

if 1 <= n <= 100:
    print("The number is in between 1 and 100")
else:
    print("please enter a valid number")

#Program
n = int(input("Enter a digit from 0 to 9"))
if n == 0:
    print("Zero")
elif n == 1:
    print("One")
elif n == 2:
    print("Two")
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Five")
elif n == 6:
    print("Six")
elif n == 7:
    print("Seven")
elif n == 8:
    print("Eight")
elif n == 9:
    print("Nine")
else:
    print("Please enter a number from 0 to 9 only")


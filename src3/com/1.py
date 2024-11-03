#print that the given sequence number is an armstrong or not
n = int(input("Enter a number"))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp //= 10

if n == sum:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")


#check wheter the given number is prime or not
n = int(input("Enter a number"))
if n == 0 or n == 1:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")

else:
    print(n, "is not a prime")


#find the factorial of  a number
n = int(input("Enter a number: "))
factorial = 1
if n < 1:
    print("sorry factorial not available for negative numbers")
elif n == 0:
    print("factorial for zero is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i

print("factorial for", n, "is", factorial)


#Find the given sequence is a palindrome or not
n = input("Enter a sequence: ")
if n == n[::-1]:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")


#find the given number is odd or even
n = int(input("Enter a number: "))
if (n % 2) == 0:
    print(n, "is an even number")
else:
    print(n, "is an odd number")


#write a program to find the number of consonants and ovewels in a sequence
n = input("Enter a sequence: ")
vowels = 0
consonants = 0
for i in n:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1


print("number of vowels in the sequence is", vowels)
print("number of consonants in the sequence is", consonants)


#write a program to for printing a sequence of fibonacci series
n = int(input("Enter a number: "))
n1, n2 = 0, 1
print("Fibonacci series", n1, n2, end=" ")
for i in range(2, n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


#write a program to print half pyramid of stars
rows = int(input("Enter no. of rows"))
for i in range(rows):
    for j in range(i + 1):
        print('*', end=" ")
    print()


#write a program for reverse a string
s = input("Enter a string: ")
s1 = " "
for i in s:
    s1 = i + s1

print(s1)


#write a program to print a triangle pattern
s = int(input("Enter a number: "))
for i in range(s):
    print(' ' * (s-i-1) + "#" * (2*i+1))

print()


#write a program by defining class and object method
class Car:
    name = None
    color = None
    model = None

    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def display_info(self):
        print(f"The name of the car is {self.name} in the color of {self.color} is {self.model} model")


car = Car("swift", "red", "latest")
car.display_info()


#write a program to by defining a class and return method
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius * self.radius


circle = Circle(5)
print(circle.area())


#write a program to defining encapsulation
class Employee:
    def __init__(self, salary, information):
        self.__salary = salary
        self.__information = information

    def worker_info(self):
        print("The salary of the employee is", self.__salary)
        print("The information of the employee is", self.__information)


employee = Employee(10000, "got hike ")
employee.worker_info()


#write a program on single inheritance
class Bird:

    def fly(self):
        return "All birds can fly"


class Penguine:

    def fly(self):
        return "penguine cannot fly"


bird = Bird()
print(bird.fly())
p = Penguine()
print(p.fly())


#write program on multi-inheritance
class Father:
    def height(self):
        return "Tall"


class Mother:
    def color(self):
        return "Fair"


class Child(Father, Mother):
    pass


child = Child()
print(child.height())
print(child.color())








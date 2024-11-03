#write a program to find the no. of vowels and consonants in a string

str1 = input("Enter a string : ")
vowels = 0
consonants = 0
for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print("Total no of vowels in the string is", vowels)
print("Total no of consonants in the string is", consonants)


#write a program to find the duplicate characters in a string
s = "geeksforgeeks"
p = ""
for i in s:
    if i not in p:
        p = p+i
print(p)
print(list(p))


#write a program to find the sum and average of a list
L = [4, 5, 1, 2, 9, 7, 10, 8]

# variable to store the sum of
# the list
count = 0

# Finding the sum
for i in L:
    count += i

# divide the total elements by
# number of elements
avg = count / len(L)

print("sum = ", count)
print("average = ", avg)


#Reverse a List Write a Python function that takes a list and
# returns a new list with the elements reversed.
# Do this without using the built-in reverse method.
a = [1, 2, 3, 4, 5]

a1 = []

for val in a:
    a1.insert(0, val)
print(a1)


#Remove Duplicates from a List Create a Python function that takes a list as input
# and removes duplicate elements, preserving the order of the elements. Return the new list
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


#Find Common Elements Create a Python program that takes two lists and returns a new list containing
#elements that are common in both input lists.
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")


#Count the Occurrences of an Element Write a Python function that takes a list and an element as input and
#counts how many times that element appears in the list
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

print(a.count(2))
print(a.count(3))

#or
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# Initial count is zero
count = 0

# Iterate over the list
for val in a:

    # If num is equal to 3
    if val == 3:
        # Increase the counter
        count += 1

print(count)


#Count the Occurrences of an Element Write a Python function that takes a tuple and an element as input
#and counts how many times that element appears in the tuple.

# Program to count the number of times an element
# Present in the list


def countX(tup, x):
	count = 0
	for ele in tup:
		if (ele == x):
			count = count + 1
	return count


# Driver Code
tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8

print(countX(tup, enq))
print(countX(tup, enq1))
print(countX(tup, enq2))


#Unique Characters Create a Python program that takes a string as input
# and checks if all the characters inthe string are unique (i.e., no character repeats).
# Return True if all characters are unique, and False.
st = "abcbd"
a=""
for i in st:
	if i not in a:
		a+=i
if(a==st):
	print(True)
else:
	print(False)



#Write a Python function that takes a dictionary of items and their prices as input
# and finds and prints the keys (items) with the highest prices.
# Find Keys with Maximum Value
Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}

Keymax = max(zip(Tv.values(), Tv.keys()))[1]
print(Keymax)


#Convert two lists into a dictionary in Python without using a built-in method
index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = dict(zip(index, languages))
print(dictionary)


#Write a program to print sum of digits.
num = int(input("Enter Number: "))
sum = 0

for i in num:
    sum += i

print(sum)



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


#Write a Program to print the multiplication table.
num = int(input("Display multiplication table of? "))
for i in range(1, num-1):
   print(num, 'x', i, '=', num*i)


#Write a Python program that uses list comprehension to create a new list containing the squares of the
#numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares)


#Write a Python program that uses a "for" loop to iterate over a string and
# prints out each character along with its count.
count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)


#Write a Python program that uses a list comprehension to create a new list
#that contains only the uppercase letters in an existing list of strings.
input = ['fun', 'Foo', 'BaR']

# Converting
lst = [x.upper() for x in input]

# printing output
print(lst)


#To write a program in python find the second smallest and third largest number in a list
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]

length = len(list1)
list1.sort()
print("Largest element is:", list1[length - 1])
print("Smallest element is:", list1[0])
print("Second Largest element is:", list1[length - 2])
print("Second Smallest element is:", list1[1])


#Write a Python program to remove duplicates from a list
#while preserving the order of elements
a = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by converting to a set
a = list(set(a))

print(a)


#Create a simple calculator operations using function.
# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))



    else:
        print("Invalid Input")


#Write a short program that prints each number from 1 to 100 on a new line.
#For each multiple of 3, print "Fizz" instead of the number.
#For each multiple of 5, print "Buzz" instead of the number.
#For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number
for i in range(1, 101):

    if (i % 15) == 0:
        print("FizzBuzz")
    elif (i % 3) == 0:
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")
    else:
        print(i)


#Reverse a number including negative numbers also
num = 123456
print(str(num)[::-1])


#Write a program to swap values of two variables without using third variable and also swap the values of
#three variables without using fourth variable
x = 5
y = 10
x, y = y, x
print("after swapping value of x is ", x)
print("after swapping value of y is ", y)


#write a program to swap the case
s = input("Enter a string: ")
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.casefold())


#Program to find the armstrong number
n = int(input("Enter a number: "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == n:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")


#write a program to find whether the number is prime or not
a = int(input("Enter a number"))
if a == 0 or a == 1:
    print("It is not a prime number")

elif a > 1:
    for a in range(2,n):
        if (a % 2) == 0:
            print("It is not a prime number")
            break

    else:
        print("It is a prime number")

else:
    print("It is not a prime number")


#Write a program to find the factorial of a number
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Sorry, factorial for negative numbers is not available")
elif n == 0:
    print("The factorial for zero is 1")
else:
    for i in range(2, n+1):
        factorial = factorial * i

print("The factorial for", n, "is", factorial)


#write a program to find the squares of first 10 numbers by using the list comprehension
squares = [x ** 2 for x in range(1, 11)]
print(squares)


#write a program to find the occurence of each element in the given sequence
ip_str = input("Enter a sequence: ")
total = {}
for x in ip_str:
    if x in total:
        total[x] += 1
    else:
        total[x] = 1

print("occurrence of each characters in ip_str is:\n" + str(total))


#write a program to find the given string is alphanumeric or not
def checkstring(str):
    flag_a = False
    flag_n = False

    for i in str:
        if i.isalpha():
            flag_a = True
        if i.isnumeric():
            flag_n = True
    return flag_a and flag_n


print(checkstring("MynameisVenkatiam33"))
print(checkstring("9876543210"))


#write a code snippet to generate the square of every element of list
n = [11, 12, 13, 14, 15]
#using list comprehension to square each element
n1 = [i ** 2 for i in n]
print(n1)

#write a program to find the entered string is a palindrome or not
a = input("Enter a string: ")
a = a.casefold()
b = "".join(reversed(a))
if a == b:
    print("The string is a palindrome")
else:
    print("This is not a palindrome")

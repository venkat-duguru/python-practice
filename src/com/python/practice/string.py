#1.Write a program to find the odd and even positions of a given string using slice operator
s = input("Enter some string")
print("Characters present at  odd position is: "[1::2])
print("Characters present at even position is: "[::2])

#2.Write a program to find the odd and even positions of a string without using inbuilt functions
a = input("Enter a string")
i = 0
print("The characters present at even position:")
while i < len(a):
    print(a[i])
    i = i + 2

print("The characters present at odd position:")
i = 1
while i < len(a):
    print(s[i])
    i = i + 2

#print(s[i], end=",")

#3.Changing case of a string by using built-in functions
A = "The Python Classes By Durga Sir"
print(A.upper())
print(A.lower())
print(A.swapcase())
print(A.title())
print(A.capitalize())

#4.
S = input("Enter some string")
i = S.split()
i1 = []
for x in i:
    i1.append(x[::-1])
    output = ''.join(i1)
    print(output)

#5.separate alphabets and numbers i an alphanumeric string
s = input("Enter some string")
s1 = s2 = output = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
for x in sorted(s1):
    output = output + x
for x in sorted(s2):
    output = output + x
print(output)
output = s1 + s2
print(sorted(output))

#6.
P = input("Enter some string:")
output = ''
for x in P:
    if x.isalpha():
        output = output + x
        previous = x
    else:
        output = output + previous * (int(x)-1)
print(output)

#7
s = input("Enter some string:")
output = ''
for x in s:
    if x.isalpha():
        output = output + x
        previous = x
    else:
        newch = chr(ord(previous)+int(x))
        output = output + newch
print(output)


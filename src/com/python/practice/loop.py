#print squares upto 20
for i in range(1, 20):
    print(f"the square of {i} is {i**2}")

#program printing squares of list
l = [1, 2, 3, 4, 5, 3, 7, 5]
for a in l:
    print(f"the square of {a} is {a**2}")

#program printing squares of a tuple
t = (1, 3, 5, 7, 9, 11)
for b in t:
    print(b**2)

#program printing squares of set
s = {2, 4, 5, 6, 8, 10, 2}
for i in s:
    print(f"the square of {i}, is {i**2}")

#Program for String
s = "Durga Prasad"
for x in s:
    print(x)

#Program
s = "Doguru Venkatesh Babu Dhruva Kumar"
count = 0
for x in s:
    count += 1
    print(x)
print("The number of characters in s is:", count)

#Program
l = [10, 20, 30, 40]
for c in l:
    print(c)

#Program
s = input("Enter a string:")
i = 0
for x in s:
    print("The character present at", i, "index is", x)
    i += 1

#Program
for x in range(10):
    print("Hello")

#Program
for y in range(11):
    print(y)

#Program display odd numbers only
for X in range(21):
    if ((X % 2) != 0): #or ((X % 2) == 0):
        print(X)

#Program
for a in range(1, 21, 2):
    print(a)

#Program
for Y in range(10, 0, -1):
    print(Y)

#Program read the following list
list = [10, 20, 30, 40, 50]
for d in list:
    print(d)
    d += 1

#Program find the sum of the numbers present the list
l = eval(input("Enter some values"))
sum = 0
for numbers in l:
    sum += numbers
    print(sum)
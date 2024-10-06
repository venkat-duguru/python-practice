#program1
import random

i = random.randint(0, 9)
print(f"{i=}")

j = random. randint(0, 9)
print(f"{j=}")

i = i + j
j = i - j
i = i - j

print("===========")
print("new i value =", i)
print("new j value =", j)

#program2
i = random.randint(10, 99)
print(f"{i=}")

j = random.randint(10, 99)
print(f"{j=}")

i = i + j
j = i - j
i = i - j

print("----------")
print("new i value =", i)
print("new j value =", j)

#program3
i = random.randint(5, 15)
print(f"{i=}")

j = random.randint(5, 15)
print(f"{j=}")

i = i + j
j = i - j
i = i - j

print("#######")
print("new i value = ", i)
print("new j value = ", j)

#program4
i = random.randint(1, 50)
print(f"{i=}")

j = random.randint(1, 50)
print(f"{j=}")

i = i + j
j = i - j
i = i - j

print("@@@@@@@@@")
print("new i value = ", i)
print("new j value = ", j)

#program5
i = random.randint(1, 100)
print(f"{i=}")

j = random.randint(1, 100)
print(f"{j=}")

i = i + j
j = i - j
i = i - j

print("$$$$$$$$$$")
print("new i value = ", i)
print("new j value = ", j)

#program6
a = int(input("Enter first number"))
b = int(input("Enter second number"))
a, b = b, a
print("new a value", a)
print("new b value", b)

#program7
c = float(input("Enter first decimal"))
d = float(input("Enter second decimal"))

c, d = d, c
print("new decimal c value is", c)
print("new decimal d value is", d)

#program8
e = [1, 2, 3, 4, 5]
f = [6, 7, 8, 9, 10]
e, f = f, e
print("new list of e is", e)
print("new list of f is", f)

#program9
g = input("Enter first string:")
h = input("Enter second string:")
g, h = h, g
print("Tne new first string is", g)
print("The new second string is", h)

#program10
i = (1, 2.3, 'abcd', True, 1+2j)
j = (4, 5.6, 'wxyz', False, 3+4j)
i, j = j, i
print("The new tuple i is", i)
print("The new tuple j is", j)

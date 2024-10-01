#Program1
str = 'x'
result = str in 'Python'
print(result)

#Program2
x = [1, 2]
y = x
print(x is y)

#Program3
x = 10
y = 0
result = x/y
print(result)

#Program4
x = 7
if x > 5:
    print("x is greater than 5")
elif x > 0:
    print("x is positive integer")

#Program5
n = 10
while n > 0 :
    print(n)
    n -= 1

#Program6
i = 0
while i < 10:
    print(i)
    i = i + 1

#Program7
x = 0
while i in range(0, 10):
    print(x)
    x = x + 1

#Program8
a = 0
while a < 5:
    if a == 2:
        a = a + 1
        continue
    print(a)
    a = a + 1

#Program9
name = "Venkat"
last_letter = name[5]
print(last_letter)

#Program10
my_dict = {"name": "Venkat", "age": 30, "city": "Hyderabad"}
print(my_dict["city"])

#Reverse a List Write a Python function that takes a list and returns a new list with the elements reversed.
#Do this without using the built-in reverse method.
a = [1, 2, 3, 4, 5]
r = []
for i in a:
    r.insert(0, i)
print(r)


A = ['a', 'b', 'c', 'd', 'e']
B = []
for i in A:
    B.insert(0, i)
print(B)


x = ['apple', 'banana', 'carrot']
y = []
for i in x:
    y.insert(0, i)
print(y)


#reversing a list elements without using built-in functions
c = ['s', 't', 'r', 'i', 'n', 'g']
d = []
for x in c:
    d.insert(0, x)
print(d)


#reversing a list without using built-in functions
m = ['!', '@', '#', '$', '%', '^', '&', '*']
n = []
for i in m:
    n.insert(0, i)
print(n)

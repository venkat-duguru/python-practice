l = ['a', 'c', 'd', 'b']
print(l)
[a, c, d, b] = l
print(a, c, d, b)

#Program to find the size of list and tuple
import sys

l1 = [10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 100]
t1 = (10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 100)
print(sys.getsizeof(l1))
print(sys.getsizeof(t1))

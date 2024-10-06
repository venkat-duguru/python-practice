x = ['a', 'b', 'c', 'd']
for x[-1] in x:
    print(x[-1], end='')


a = [0, 1, 2, 3]
for a[-1] in a:
    print(a[-1], end='\n')


#Print the squares of numbers in the list
numbers = [1, 2, 3, 4]


def square(number):
    return number * number


squared_numbers = map(square, numbers)
result = list(squared_numbers)
print(result)


#Working with map
def square(n):
    return n * n


numbers = (1, 2, 3, 4)
result = map(square, numbers)
print(result)

result = set(result)
print(result)

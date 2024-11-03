def count_up_to(max_value):
    count = 0
    while count <= max_value:
        yield count
        count += 1


counter = count_up_to(10)
for i in counter:
    print(i)


def my_range(start, end):
    count = 0
    while count < end:
        yield count
        count += 1


Range = my_range(10, 20)
for i in Range:
    print(i)



def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


my_fibo = fibonacci()
for x in range(20):
    print(next(my_fibo))



def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number

# Using the generator to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for even in even_numbers(numbers):
    print(even)



#
square_gen = (x**2 for x in range(10))
for squares in square_gen:
    print(squares)

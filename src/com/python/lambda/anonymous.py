# declare a lambda function
greet = lambda: print('Hello World')

greet()


# lambda that accepts one argument
greet_user = lambda name: print('Hey there,', name)

greet_user("Venkat")


#map() with Lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

print(set(result))


#Add Multiple Lists using map() and lambda
num1 = [1, 2, 3]
num2 = [10, 20, 40]


result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))



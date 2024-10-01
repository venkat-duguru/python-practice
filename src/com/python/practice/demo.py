print("Hello world!")

#write a program on exception.
print("Starting of the program")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a/b
    print(c)
except Exception as e:
    print(e)
    print("Enter an integer please!")
print("End of the program")
#If we enter integers it gives correct output
#If we give one of them as string it gives output but it gives an error called invalid literal
#If we give a zero in denominator it gives an error of dividion by zero
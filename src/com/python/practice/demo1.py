print("Start of the program")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print(c)
except Exception as e:
    print(e)
    print("Enter a valid literal")
print("End of the program")
# By observing this we enter a string in place of int type it gives an error of invalid literal
# But the program is executed


#without excpetion write a program using arithematic operations
x = 10
y = "Python"
z = y * x
print(z) #in case of multiplication it doesn't give any error
A = x + y
print(A)#in case of addition it gives an error as Type Error



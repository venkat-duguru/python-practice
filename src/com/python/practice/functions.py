#Program using function
def wish():
    print("Hello")
print(wish())

#Peogram2 using function name as calc
def calc(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div
t = calc(100, 50)
for x in t:
    print(x)


#Program3 using function
def calc(a, b):
    pass
calc(10, 20)
calc(a=10, b=30)
calc(b=20, a=30)
calc(50, b=120)


#Program4 using function var-arg
def f1(*n):
    print("Var-arg function")

f = f1(10, 2)


#Program5 write a program to print the sum of given n numbers with var-arg function
def sum(*n):
    result = 0
    for x in n:
        result = result +x
    print("The sum is", result)
s = sum()
s = sum(10)
s = sum(10, 20)
s = sum(10, 20, 30)
s = sum(10, 20, 30, 40)


#Program6 write a program to print the default arguments and var- arg parameters
def sum(name, *n):
    result = 0
    for x in n:
        result = result + x
    print("The sum:", name, result)


s = sum("Venkat", 100)
s = sum("Suma", 100, 200)
s = sum("Ushasri", 100, 200, 300)


#Program7 write a program to print var-arg parameters and default parameters
def mul(*n, name):
    result = 0
    for x in n:
        result = result + x
    print("The mul by", name, ":", result)



m = mul(name = "Family")
m = mul(10, name = "Venkat")
m = mul(10, 20, name = "Sumathi")
m = mul(10, 20, 30, name = "Ushasri")


#Program8 using keyword and var-arg parameters
def display(**kwargs):
    print("Record Information:")
    for k, v in kwargs.items():
        print(k, ".....", v)


display(name="Venkatesh", marks=92, age=32, wife="Suma")
display(name="Friend", wife1="ABC", wife2="XYZ", wife3="PQR")
display(name="Pavan", brand1="KF", brand2="KO", brand3="RC")


#Program9 usingf all parameters
def f1(arg1, arg2, arg3=4, arg4=8):
    print(arg1, arg2, arg3, arg4)


f1(3, 45)
f1(10, 20, 30, 40)
f1(25, 50, 4, 100)
f1()

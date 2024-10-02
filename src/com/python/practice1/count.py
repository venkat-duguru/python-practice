#Program
num = 7842553561

digit = 5

count = 0
n = num
while n != 0:
    rem = n % 10
    if rem == digit:
        count += 1

    n = n // 10
print("{} occured {} times in {}".format(digit, count, num))

#Program2
number = 9491989809
digit = 9
count = 0
n = number
while n != 0:
    j = n % 10
    if j == digit:
        count += 1

    n = n // 10
print("{} occured {} times in {}".format(digit, count, number))

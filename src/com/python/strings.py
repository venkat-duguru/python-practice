#python program to find the number of digits in the given number
num = int(input("Enter number: "))
count = 0
i = num

while i > 0:
    count = count+1
    i = i//10
print(f"The number of digits in {num}:", count)


#program for printing Multiplication tables.
num = int(input("Enter a number for the multiplication table: "))
print(num, "Tables\n")

for i in range(1, 11):
    print(num, 'x', i, '=', num * i)


#Python program to find largest number in a list
mylist = [101, 62, 66, 45, 99, 18, 266, 18]
max = mylist[0]
for i in mylist:
    if i > max:
        max = i

print("Largest number is:", max)


#String Modification using map()
actions = ['eat', 'sleep', 'read']
result = list(map(list, actions))
print(result)

#without comprehension
b = ["apple", "banana", "cherry", "dragon-fruit"]
A = []
for x in b:
    if 'a' in x:
        b.remove(x)
        A.append(x)

print(A)
print(b)


f = ["apple", "banana", "cherry", "kiwi", "mango"]

F = [x for x in f if "a" in x]

print(F)

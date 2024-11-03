n = int(input("Enter a number: "))
if n == 0 or n == 1:
    print(n, "is not a  prime number")
elif n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            print(i, 'times', n // i, 'is', n)
            break
    else:
        print(n, "is a prime number")

else:
    print(n, "is not a prime number")


#intersection of two lists
def intersection(l1, l2):
    return list(set(l1) & set(l2))


l1 = ["apple", "banana", "cherry", "donut", "elephant", "fish"]
l2 = ["apricot", "banana", "chia", "donut", "eagle", "fish"]
print(intersection(l1, l2))

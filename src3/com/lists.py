l = [1, 2, 1, 3, 2, 3, 1, 2, 3]
l = list(dict.fromkeys(l))
print(l)


l1 = ['z', 'l', 'm', 'a', 'q', 'l', 'm', 'q', 'a', 'p', 'z']
l1 = list(dict.fromkeys(l1))
print(l1)


a = ['apple', 'ant', 'amazon', 'ape', 'ant', 'apple', 'amazon', 'ape']
a = list(dict.fromkeys(a))
print(a)

b = ['a', 'an', 'the', 'ant', 'an', 'ant', 'the', 'a']
b = list(dict.fromkeys(b))
print(b)


#To find the maximum and minimum value in a given list
lists = [28, 3, 92, 19]
lists.sort()
print("The minimum number in the list is", lists[0])
print("The maximum number in the list is", lists[3])


liz = [8, 7, 93, 26, 9, 21, 28, 3, 92]
print(min(liz))
print(max(liz))

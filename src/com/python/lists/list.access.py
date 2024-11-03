mylist = ["ant", "basket", "cart", "donkey"]
print(len(mylist))
print(mylist[-1])
print(f"Value at negative index -1 is {mylist[-1]}")
print(mylist[0])
print(f"The value at negative index -4 and at zeroth index is {mylist[0]}")


#Formatting a list using indexes
F = ["anger", "fear", "dear"]
print(f"{F[2]} I am getting {F[0]} on your silly {F[1]}")


#Slicing of list
list = ["apple", "banana", "cherry", "orange", "kiwi"]
print(list[1:4])

#find the elements which start and end at the different positions
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[0:8:2])
print(list1[1:8:2])
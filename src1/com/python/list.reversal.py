l1 = [4, 7, 9, 2]
#reverse by built.in
l1.reverse()
#print(l1)


#reverse by slicing
l2 = l1[::-1]
print(l2)


#revserse by reversed function
l3 = list(reversed(l1))
print(l3)


#reverse by loop
list2 = []
list1 = [1, 2, 3, 4]
for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])
print(list2)



import datetime
today = datetime.datetime.now()
print(today.strftime("%y-%m-%d %H:%M:%S"))

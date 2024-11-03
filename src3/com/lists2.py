def Remove(duplicate):
    final_list = []
    for i in duplicate:
        if i not in final_list:
            final_list.append(i)
    return final_list

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))

def Removes(duplicates):
    new_list = []
    for i in duplicates:
        if i not in new_list:
            new_list.append(i)
    return new_list


duplicates = [2, 4, 10, 20, 5, 2, 20, 4]
print(Removes(duplicates))


#finding duplicates in a list
def lists(dup):
    n = []
    for j in dup:
        if j not in n:
            n.append(j)
    return n
dup = [7, 8, 4, 2, 5, 5, 3, 5, 6, 1]
print(lists(dup))



def my_list(old):
    new_list = []
    for i in old:
        if i not in new_list:
            new_list.append(i)

    return new_list
old = ['h', 'e', 'l', 'l', 'o', 'g', 'o', 'o', 'd', 'm', 'o', 'r', 'n', 'i', 'n', 'g']
print(my_list(old))


def s(list):
    s1 = []
    for i in list:
        if i not in s1:
            s1.append(i)
    return s1
list = [9, 4, 9, 1, 9, 1, 9, 8, 9, 8, 0, 9]
print(s(list))

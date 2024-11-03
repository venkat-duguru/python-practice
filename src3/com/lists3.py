def common_elements(a, b):
    set_a = set(a)
    set_b = set(b)
    if (set_a & set_b):
        print(set_a & set_b)
    else:
        print("No common elements")


a = [1, 2, 3, 4, 5, 6, 7]
b = [4, 5, 6, 7, 8]
common_elements(a,b)

a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9, 10, 11]
common_elements(a,b)


def common(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements found")


a = [11, 22, 33, 44, 55, 66]
b = [55, 66, 77, 11, 44, 33, 22, 10]
common(a, b)

def intersection(a, b):
    abc = set(a)
    cde = set(b)
    if (abc & cde):
        print(abc & cde)
    else:
        print("No intersection")


a = [123, 345, 456, 567, 678, 789, 901]
b = [102, 123, 234, 345, 456, 678, 890]
intersection(a, b)

def inter(a, b):
    max = set(a)
    min = set(b)
    if (max & min):
        print(max & min)
    else:
        print("No common elements in the two lists")


a = [123, 456, 789, 741, 852, 963]
b = [321, 654, 987, 147, 258, 369]
inter(a, b)































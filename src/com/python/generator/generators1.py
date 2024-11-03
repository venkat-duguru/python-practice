def count_up_to(max_value):
    count = 0
    while count <= max_value:
        yield count
        count += 1


counter = count_up_to(10)
for i in counter:
    print(i)
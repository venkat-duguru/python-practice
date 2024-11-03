def count(start, end):
    count = 0
    while count < end:
        yield count
        count += 1


Count = count(1, 101)
for i in Count:
    print(i)

class Birds:
    name = ""
    color = ""
    age = 0


bird1 = Birds()
bird1.name = "Parrot"
bird1.color = "Green"
bird1.age = 12


bird2 = Birds()
bird2.name = "Crow"
bird2.color = "Black"
bird2.age = 25


print(f"The bird name is {bird1.name}, and is in {bird1.color}, its life span is {bird1.age}")
print(f"The bird name is {bird2.name}, and is in {bird2.color}, its life span is {bird2.age}")

#access and modify global variable
c = 1


def add():
    print(c)


add()


#global variable
g = 1


def add():
    global g

    g = g + 2
    print(g)


add()


#Using global variable outside the function
x = 'Programming'


def myfunc():
    x = 'Excellent'


myfunc()
print('Python is ' + x)


#defining the variable as global inside the function
x = 'awesome'


def myfunc():
    global x
    x = 'fantastic'


myfunc()
print('Python is ' + x)

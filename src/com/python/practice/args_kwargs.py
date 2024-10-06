#1. *args python program
def sum(*args):
    total = 0
    for a in args:
        total = total + a
    print(total)

sum(1, 2, 3, 4, 5, 6)

#2. **kwargs python program
def show(**kwargs):
    print(kwargs)

show(A=1, B=2, C=3, D=4)
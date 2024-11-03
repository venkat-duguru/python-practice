class XYZ:
    def f1(self):
        try:
            n = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int value only")
        else:
            print(n)
        finally:
            print("I will execute always")


x = XYZ()
x.f1()


class Dog:
    name = None
    id = None

    def sleep(self):
        print("Sleeping")


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print(" ---- -----------------")

dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)



class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Telling about car with the name " + self.name)
        print("Telling make version of car " + self.make)
        print("Telling about the car model " + self.model)
        

lambo = Car("lambo", "V2", "2024")
lambo.start_engine()

xuv = Car("XUV", "V6", "2023")
xuv.start_engine()

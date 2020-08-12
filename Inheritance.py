class Vehicle:
    def general_usage(self):
        print("general use: transportation")


class Car(Vehicle):
    def __init__(self):
        print("I m car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I m motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")


c = Car()
c.general_usage()
c.specific_usage()

m = MotorCycle()
m.specific_usage()


print(isinstance(c, Car))
print(isinstance(c, MotorCycle))

print(issubclass(Car, Vehicle))
print(issubclass(Car, MotorCycle))

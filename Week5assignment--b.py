# Activity 2

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement abstract method.")


class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving.")


class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying.")


# Creating instances and testing
my_car = Car("Ford Mustang")
my_plane = Plane("Boeing 747")

# Using move method
my_car.move()
my_plane.move()
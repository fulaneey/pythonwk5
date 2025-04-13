# Base class: Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, and I protect {self.city} using {self.power}!"

# Subclass with inheritance: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def introduce(self):
        return f"I am {self.name}, and I fly around {self.city} at {self.flight_speed} km/h using {self.power}!"

# Creating objects
hero1 = Superhero("Captain Shield", "impenetrable force field", "Shield City")
hero2 = FlyingHero("Skyhawk", "super flight", "Cloud City", 800)

# Testing the methods
print(hero1.introduce())
print(hero2.introduce())

# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # This will be overridden by subclasses.

# Subclass 1: Car
class Car(Vehicle):
    def move(self):
        return "Driving "

# Subclass 2: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying"

# Subclass 3: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing "

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
vehicles = [car, plane, boat]
for vehicle in vehicles:
    print(vehicle.move())

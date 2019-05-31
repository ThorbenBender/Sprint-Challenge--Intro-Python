# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    def __init__(self, wheels=20, tank="Big", tankCapacity=20, fuel="Nukes"):
        self.wheels = 20
        self.tank = "Big"
        self.tankCapacity = 20
        self.fuel = "Nukes"


class FlightVehicle(Vehicle):

    def __init__(self, wheels=20, tank="Big", tankCapacity=20, fuel="Nukes", maxHeight="1000m"):
        super().__init__()
        self.maxHeight = maxHeight


class Starship(FlightVehicle):

    def __init__(self, wheels=20, tank="Big", tankCapacity=20, fuel="Nukes", maxHeight="1000m", lightSpeed=False):
        super().__init__()
        self.lightSpeed = lightSpeed


class Airplane(FlightVehicle):

    def __init__(self, wheels=20, tank="Big", tankCapacity=20, fuel="Nukes", maxHeight="1000m", passenger=200):
        super().__init__()
        self.passenger = passenger


class GroundVehicle(Vehicle):

    def __init__(self, wheels=20, tank="Big", tankCapacity=20, fuel="Nukes", weight=800):
        super().__init__()
        self.weight = weight


class Car(GroundVehicle):

    def __init__(self, wheels=20, tank="Big", tankCapacity=20, fuel="Nukes", weight=800, doors=5, PS=500):
        super().__init__()
        self.doors = doors
        self.PS = PS


class Motorcycle(GroundVehicle):

    def __init__(self, wheels=20, tank="Small", tankCapacity=20, fuel="Nukes", weight=800, offRoad=True):
        super().__init__()
        self.offRoad = offRoad

    def __str__(self):
        return str(self.tank)


bike = Motorcycle()
print(bike)

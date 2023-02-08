class Vehicle:

    def __init__(self, name: str, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def __repr__(self):
        return f"{self.__class__.__name__} Name: {self.name} Max Speed: {self.max_speed} Miles: {self.mileage}"

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

v1 = Bus("School", 140, 80)
print(v1.seating_capacity())
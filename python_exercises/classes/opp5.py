class Vehicle:

    def __init__(self, name: str, max_speed: int, mileage: int, color = "White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b1 = Bus("School Volvo", 180, 12)
c1 = Car(name = "Audi Q5", max_speed = 240, mileage = 18)

print(f"Color: {b1.color}, Vehicule name: {b1.name}, Speed: {b1.max_speed}, Mileage: {b1.mileage}")
print(f"Color: {c1.color}, Vehicule name: {c1.name}, Speed: {c1.max_speed}, Mileage: {c1.mileage}")

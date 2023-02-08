class Vehicule:
    def __init__(self, max_speed: int, mileage: int):
        self.max_speed = max_speed
        self.mileage = mileage

    def __repr__(self) -> str:
        return f"My max_speed is {self.max_speed} and my mileage is {self.mileage}"

TeslaXL = Vehicule(230, 70)
print(TeslaXL)
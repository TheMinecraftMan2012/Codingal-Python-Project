class Vehicle():
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 180, 12)
print(f"Vehicle name: {School_Bus.name}, Max Speed: {School_Bus.maxspeed}, Mileage: {School_Bus.mileage}")
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
modelY = Vehicle(360, 20)

print("Max Speed of ModelX:", modelX.max_speed)
print("Mileage of ModelX:", modelX.mileage)

print("Max Speed of ModelY:", modelY.max_speed)
print("Mileage of ModelY:", modelY.mileage)
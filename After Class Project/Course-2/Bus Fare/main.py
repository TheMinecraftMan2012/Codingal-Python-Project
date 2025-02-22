class Vehicle():
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

    def info(self):
        print(f"Bus Name: {self.name}, Max Speed: {self.maxspeed}, Mileage: {self.mileage}")

class Bus(Vehicle):
    def __init__(self, name, maxspeed, mileage, distance, isAC):
        self.distance = distance
        self.isAC = isAC

        super().__init__(name, maxspeed, mileage)
    
    def calculateFare(self):
        if self.isAC == True:
            bus_fare = (self.distance * 5) + 2000
            print("Your Total Bus Fare:", bus_fare)
        
        else:
            bus_fare = (self.distance * 5) + 500
            print("Your Total Bus Fare:", bus_fare)

shohagh_pres = Bus("Shohagh Prestige", 300, 20, 360, True)
shohagh_pres.info()
shohagh_pres.calculateFare()

shohagh_elite = Bus("Shohagh Elite", 300, 15, 360, False)
shohagh_elite.info()
shohagh_elite.calculateFare()
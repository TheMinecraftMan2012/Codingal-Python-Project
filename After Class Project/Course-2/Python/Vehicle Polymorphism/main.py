from class_car import cars

class BMW(cars):
    def origin(self):
        print("My origin is in Germany")

    def price(self):
        print("Price of my cars are 40,000$ - 180,000$")
    
    def maxspeed(self):
        print("My max speed is 330 km/h")
    
    def mileage(self):
        print("My mileage is 8-15 kmpl")

class Ferrari(cars):
    def origin(self):
        print("My origin is in Italy")

    def price(self):
        print("Price of my cars are 250,000$ - 2M$")
    
    def maxspeed(self):
        print("My max speed is 400 km/h")
    
    def mileage(self):
        print("My mileage is 3-6 kmpl")

obj_bmw = BMW()
obj_fer = Ferrari()

for obj_cars in (obj_bmw, obj_fer):
    obj_cars.origin()
    obj_cars.price()
    obj_cars.maxspeed()
    obj_cars.mileage()
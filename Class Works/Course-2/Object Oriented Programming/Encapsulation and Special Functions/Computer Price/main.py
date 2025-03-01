class Computer:
    def __init__(self):
        self.__maxPrice = 900
    
    def sell(self):
        print("Selling Price: %d" % self.__maxPrice)
    
    def setMaxPrice(self, price):
        self.__maxPrice = price

c = Computer()
c.sell()

c.__maxPrice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()
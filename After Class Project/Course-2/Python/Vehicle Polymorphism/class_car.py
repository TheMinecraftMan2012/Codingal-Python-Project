from abc import ABC, abstractmethod

class cars(ABC):
    @abstractmethod
    def origin(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def maxspeed(self):
        pass

    @abstractmethod
    def mileage(self):
        pass
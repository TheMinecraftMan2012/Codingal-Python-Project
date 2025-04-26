from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can rattle")

class Lion(Animal):
    def move(self):
        print("I can roar")

class Dog(Animal):
    def move(self):
        print("I can bark")

h = Human()
h.move()

s = Snake()
s.move()

l = Lion()
l.move()

d = Dog()
d.move()
class Dog:
    species = "Dog"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


def print_obj(name, breed, age):
    dog = Dog(name, breed, age)
    print(f"{dog.name} is a {dog.species}. He is {dog.age} old and his breed is {dog.breed}")

print_obj("Felix", "German Shepherd", 5)
print_obj("Dogglas", "Beagle", 7)
print_obj("Copir", "Bulldog", 10)
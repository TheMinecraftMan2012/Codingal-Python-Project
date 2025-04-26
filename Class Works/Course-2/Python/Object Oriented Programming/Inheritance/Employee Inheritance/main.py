class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idnumber}")

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)

        print(f"Salary: {self.salary}")
        print(f"Post: {self.post}")

a = Employee("Rahul", 24011, 20000, "Intern")
a.display()
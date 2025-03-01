from abc import abstractmethod, ABC

class AbstClass(ABC):
    def print(self, x):
        print("Passed Value:", x)
    
    @abstractmethod
    def task(self):
        print("We are inside AbstClass task")

class test_class(AbstClass):
    def task(self):
        print("We are inside test_class task method")

test_obj = test_class()
test_obj.print(100)
test_obj.task()
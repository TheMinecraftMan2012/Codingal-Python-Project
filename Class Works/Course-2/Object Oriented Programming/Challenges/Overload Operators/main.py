class A:
    def __init__(self, a):
        self.a = a
    
    def __lt__(self, other):
        if(self.a < other.a):
            return "Obj 1 is less than obj 2"
        else:
            return "Obj 1 is greater than obj 2"
    
    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"

ob1 = A(3)
ob2 = A(2)
print(ob1 < ob2)

ob3 = A(5)
ob4 = A(5)
print(ob3 == ob4)
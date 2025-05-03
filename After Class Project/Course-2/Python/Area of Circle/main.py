class circle:
    def __init__(self, radius, unit):
        self.radius = radius
        self.unit = unit
        print(f"Given radius: {self.radius} {self.unit}")
    
    def areaCalc(self):
        area = 3.1416 * self.radius * self.radius
        print(f"Area of Circle: {area} sq {self.unit}")
    
    def perimeterCalc(self):
        perimeter = 2 * 3.1416 * self.radius
        print(f"Perimeter of Circle: {perimeter} {self.unit}")

cirObj_1 = circle(5, "meter")
cirObj_1.areaCalc()
cirObj_1.perimeterCalc()
print("\n")
cirObj_2 = circle(15, "centimeter")
cirObj_2.areaCalc()
cirObj_2.perimeterCalc()
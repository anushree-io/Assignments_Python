
class Circle:
    Pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = float(input("Enter the radius:"))
    
    def CalculateArea(self):
        self.area = Circle.Pi * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.Pi * self.radius

    def Display(self):
        print("Radius is:",self.radius)
        print("Area is:",self.area)
        print("Circumference is:",self.circumference)

obj1 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2 = Circle()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()


class Arithmatic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter 1st number: "))
        self.Value2 = int(input("Enter 2nd number: "))

    def Addition(self):
        print("Addition is:", self.Value1 + self.Value2)

    def Substraction(self):
        print("Substraction is:", self.Value1 - self.Value2)

    def Multiplication(self):
        print("Multiplication is:", self.Value1 * self.Value2)

    def Division(self):
        try:
            print("Division is:", self.Value1 / self.Value2)
        except ZeroDivisionError:
            print("Division by zero not possible")



obj1 = Arithmatic()
obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()

obj2 = Arithmatic() 
obj2.Accept() 
obj2.Addition() 
obj2.Substraction() 
obj2.Multiplication() 
obj2.Division()


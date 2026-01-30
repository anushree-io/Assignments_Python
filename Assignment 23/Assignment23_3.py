
class Numbers:

    def __init__ (self,Value):
        self.Value = Value

    def ChkPrime(self):

        if self.Value <= 1:
            print(self.Value,"is not Prime")
            return 
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                print(self.Value,"is not Prime")
                return
        else:
            print("Prime")
            
    
    def ChkPerfect(self):

        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i

        if sum == self.Value:
            print(self.Value, "is a Perfect number")
        else:
            print(self.Value, "is not a Perfect number")
 

    def Factors(self):
        print("Factors are:")
        for i in range (1,self.Value + 1):
            if self.Value % i == 0:
                print(i,end = " ")
        print()


    def SumFactors(self):
        sum = 0 
        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum = sum + i
        return sum
        

num1 = int(input("Enter first number: "))
obj1 = Numbers(num1)

obj1.ChkPrime()
obj1.Factors()
obj1.SumFactors()
obj1.ChkPerfect()


num2 = int(input("Enter second number: "))
obj2 = Numbers(num2)

obj2.ChkPrime()
obj2.Factors()
obj2.SumFactors()
obj2.ChkPerfect()








class BankAccount:

    ROI = 10.5

    def __init__ (self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        
        print("Name of the Account Holder:",self.Name)
        print("Current Balance:",self.Amount)

    def Deposit(self):

        Balance = int(input("Enter amount to deposit:"))
        self.Amount += self.Amount + Balance
        print("Amount Deposited")
        
    def Withdraw(self):

        Balance = int(input("Enter amount to withdraw:"))

        if Balance <= self.Amount:
            self.Amount = self.Amount - Balance
            print("Amount Withdrawn")

        else:
            print("Insufficient Balance") 
    
    def CalculateIntrest(self):

        Intrest = (self.Amount * BankAccount.ROI) / 100
        print("Intrest is:",Intrest)



obj1 = BankAccount("Anushree", 50000)
print("Account 1:")

obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateIntrest()


obj2 = BankAccount("Pratik", 6000)
print("Account 2:")

obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateIntrest()


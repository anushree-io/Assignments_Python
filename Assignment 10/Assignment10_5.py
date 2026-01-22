# 5.Write a program which accepts one number and prints all odd numbers till that number.

def Odd(Value):
    
    for i in range (1,Value+1,2):
        print("Odd numbers are:",i)
        
def main():
    No = int(input("Enter a Number:"))
    Odd(No)

if __name__ == "__main__":
    main()


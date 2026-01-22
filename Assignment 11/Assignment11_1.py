# 1. Write a program which accepts one number and checks whether it is prime or not.

def ChkPrime(No):
    if No%2 == 1:
        return 0
    else:
        return 1
    
def main():
    No = int(input("Enter the Number:"))
    ChkPrime(No)

    if(ChkPrime(No) == 0):
        print("Number is prime")
    else:
        print("Number is not prime")

if __name__ =="__main__":
    main()
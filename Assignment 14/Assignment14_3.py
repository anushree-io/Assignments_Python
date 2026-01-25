# 3. Write a lambda function which accepts two numbers and returns maximum number.


MaxNum = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    
    Num1 = int(input("Enter the first number:"))
    Num2 = int(input("Enter the second number:"))

    Result = MaxNum(Num1,Num2)
    print("Max num is:",Result)


if __name__ == "__main__":
    main()
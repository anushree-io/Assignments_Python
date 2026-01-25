# 4. Write a lambda function which accepts two numbers and returns minimum number.


MinNum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    
    Num1 = int(input("Enter the first number:"))
    Num2 = int(input("Enter the second number:"))

    Result = MinNum(Num1,Num2)
    print("Min num is:",Result)


if __name__ == "__main__":
    main()
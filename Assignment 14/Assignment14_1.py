# 1. Write a lambda function which accepts one number and returns square of that number.


SqNum = lambda No : (No**2)

def main():
    Num = int(input("Enter the number:"))

    Result = SqNum(Num)

    print("Square is",Result)

if __name__ == "__main__":
    main()
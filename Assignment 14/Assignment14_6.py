# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.


OddNum = lambda No : No % 2 == 1

def main():
    
    Num = int(input("Enter the number:"))
    
    Result = OddNum(Num)
    print(Result)
 


if __name__ == "__main__":
    main()
# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.


EvenNum = lambda No : No % 2 == 0

def main():
  
    Num = int(input("Enter the number:"))
    
    Result = EvenNum(Num)
    print(Result)


if __name__ == "__main__":
    main()
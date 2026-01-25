# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

DivNum = lambda No : No % 5 == 0

def main():
    
    Num = int(input("Enter the number:"))
    
    Result = DivNum(Num)
    print(Result)
 
if __name__ == "__main__":
    main()
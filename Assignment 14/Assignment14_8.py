# 8. Write a lambda function which accepts two numbers and returns addition.

Add = lambda No1,No2 : No1+No2

def main():
    
    Num1 = int(input("Enter the First number:"))
    Num2 = int(input("Enter the Second number:"))


    Result = Add(Num1,Num2)
    print(Result)
 
if __name__ == "__main__":
    main()
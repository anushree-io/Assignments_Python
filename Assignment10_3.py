# 3. Write a program which accepts one number and prints factorial of that number.

def Factorial(Value):
    Result = 1
    for i in range(1,Value+1):
        Result = Result * i
    print("Factorial of ", Value, "natural numbers is:",Result)


def main():
    print("Enter a number:")
    Number = int(input())

    Factorial(Number)

if __name__ == "__main__":
    main()
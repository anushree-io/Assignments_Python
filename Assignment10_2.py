# 2. Write a program which accepts one number and prints sum of first N natural numbers.

def SumNatural(Value):
    Sum = 0
    for i in range(1,Value+1):
        Sum = Sum + 1
    print("Sum of first", Value, "natural numbers is:", Sum)


def main():
    print("Enter a number:")
    Number = int(input())

    SumNatural(Number)

if __name__ == "__main__":
    main()
# 3. Write a program which accepts one number and checks whether it is perfect number or not.

def CheckPerfect(No):
    Sum = 0
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    print("Enter number:")
    Value = int(input())
    CheckPerfect(Value)

if __name__ == "__main__":
    main()


# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5

def ChkDivisible(Value):
    if Value % 3 == 0  and Value % 5 == 0:
        print("Divisible by both 3 and 5")
    else:
        print("Not Divisible by both")

def main():
    print("Enter a Number:")
    Num = int(input())

    ChkDivisible(Num)

if __name__ == "__main__":
    main()
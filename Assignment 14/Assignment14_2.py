# 2. Write a lambda function which accepts one number and returns cube of that number.


CubeNum = lambda No : No ** 3

def main():
    Num = int(input("Enter the number:"))

    Result = CubeNum(Num)

    print("Square is",Result)

if __name__ == "__main__":
    main()
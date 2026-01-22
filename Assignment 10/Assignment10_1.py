# 1. Write a program which accepts one number and prints multiplication table of that number

def multiplication_table(Number):
    for i in range(1,11):
        Result = Number * i
        print(Result ,end=" ")
def main():
    print("Enter the Number: ")
    Value = int(input())

    multiplication_table(Value)

if __name__ == "__main__":
    main()
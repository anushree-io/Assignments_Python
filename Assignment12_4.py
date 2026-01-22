# 4. Write a program which accepts one number and prints that many numbers starting from 1.

def Display(No):
    for i in range(1, No + 1):
        print(i, end=" ")

def main():
    print("Enter value:")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()




# 5. Write a program which accepts one number and prints that many numbers in reverse order.

def Display(No):
    for i in range(No,0,-1):
        print(i, end=" ")

def main():
    print("Enter value:")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()




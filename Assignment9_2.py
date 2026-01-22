# Write a program which contains one function ChkGreater () that accepts two numbers
# and prints the greater number.

def ChkGreater(num1, num2):
    if num1 > num2:
        print(num1,"is greater")
    elif num2 > num1:
        print(num2,"is greater")
    else:
        print("Both numbers are equal")

def main():
    print("Enter two numbers:")
    value1 = int(input())
    value2 = int(input())
    
    ChkGreater(value1, value2)

if __name__ == "__main__":
    main()
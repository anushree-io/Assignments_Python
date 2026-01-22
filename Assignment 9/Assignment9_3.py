# 3. Write a program which accepts one number and prints square of that number.

def Square(Value):
    print("Square is: ",Value ** 2)
    
def main():
    print("Enter a Number: ")
    Num = int(input())
    Square(Num)

if __name__ == "__main__":
    main()
    
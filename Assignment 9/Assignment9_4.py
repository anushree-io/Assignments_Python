# 4. Write a program which accepts one number and prints cube of that number.

def Cube(Value):
    print("Cube is: ", Value*Value*Value)
    
def main():
    print("Enter a Number:")
    Num = int(input())

    Cube(Num)

if __name__ == "__main__":
    main()
#4. Write a program which accepts one number and prints all even numbers till thatnumber.

def Even(Value):
    for i in range(2,Value+1,2):
            print(i,end=" ")
def main():
    print("Enter the Number: ")
    Num = int(input())
    Even(Num)

if __name__ == "__main__":
    main()  
# 2. Write a program which accepts one number and prints its factors.

def Factor(No):
    for i in range (1,int(No/2)+1):
        if No % i == 0:
            print(i,end = " ")
def main():
    No = int(input("Enter the number:"))
    Factor(No)

if __name__ == "__main__":
    main()




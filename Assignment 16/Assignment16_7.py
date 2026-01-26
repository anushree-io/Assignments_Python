# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
# Input : 8    Output : False
# Input : 25   Output : True


def main():
    Num = int(input("Enter the Number:"))
 
    if Num % 5 == 0:
        print("True")
    else:
        print("False")

main()


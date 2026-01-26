# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11        Output : Positive Number
# Input : -8        Output : Negative Number
# Input : 0         Output : Zero


def main():
    Num = int(input("Enter the Number:"))
 
    if Num > 0:
        print("Positive Number")
    elif Num < 0:
        print("Negative Number")
    else:
        print("Zero") 

if __name__ == "__main__":
    main()


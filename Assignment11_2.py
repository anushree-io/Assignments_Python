# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def Count(Value):
    iCnt = len(str(Value))
    print("Count of digits:", iCnt)
    print("Count of Digits :",iCnt)

def main():
    num = int(input("Enter a number:"))
    Count(num)
 
if __name__ == "__main__":
    main()
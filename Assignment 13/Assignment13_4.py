
# 4. Write a program which accepts one number and prints binary equivalent.
def DisplayBinary(No):
    Binary = " "

    while No > 0:
        Binary = str(No % 2) + Binary
        No = No // 2

    print("Binary:", Binary)

Value = int(input("Enter number: "))
DisplayBinary(Value)

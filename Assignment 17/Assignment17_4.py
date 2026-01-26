# 4. Write a program which accept one number form user and return addition of its factors.
# Input : 12  Output : 16      (1+2+3+4+6)


def Factors():
    result = 0
    Num = int(input("Enter the number: "))
    for i in range(1,Num):
        if Num % i == 0:
            result = result + i
    print("Sum of factors is:",result)

Factors()



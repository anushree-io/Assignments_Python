# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5        Output : It is Prime Number


def Prime():

    Num = int(input("Enter the number:"))

    if Num <= 1:
        print("Not prime")
        return
    
    for i in range(2,Num):
        if(Num % i == 0):
            print("Not prime")
    else:
        print("Prime Number")

Prime()
# 3. Write a program which accept one number from user and return its factorial.
# Input :5  Output : 120

def Fact():
    result = 1
    Num = int(input("Enter the number: "))
    for i in range(1,Num+1):
        result = result * i
    print("Factorial is:",result)

Fact()
    

        




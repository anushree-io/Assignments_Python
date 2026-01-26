# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import Arithmatic

def ModArith():
    Num1 = int(input("Enter fisrt number: "))
    Num2 = int(input("Enter second number: "))

    print("Addition is: ",Arithmatic.Addition(Num1,Num2))
    print("Substraction is: ",Arithmatic.Substraction(Num1,Num2))
    print("Multiplication is: ",Arithmatic.Multiplocation(Num1,Num2))
    print("Division is: ",Arithmatic.Division(Num1,Num2))

ModArith()
# 3. Write a program which accepts one number and prints sum of digits.

def main():

     print("Enter a number: ")
     Number = input()     

     Sum = 0
     Size = len(Number)          

     for i in range(Size):
          Sum = Sum + int(Number[i])  

     print("Summation is : ", Sum)
     
if __name__ == "__main__":
    main()


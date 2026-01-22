# 5. Write a program which accepts one number and checks whether it is palindrome or not.

def main():

     print("Enter elements : ")
     Number = input()          

     Data = list()

     for n in Number:
          Data.append(int(n))

     Size = len(Data)
     
     Rev = list()
     for i in range(Size-1, -1, -1):
          Rev.append(Data[i])

     if Data == Rev:
          print("Number is Palindrome")
     else:
          print("Number is not Palindrome")                 


if __name__ == "__main__":
    main()



# 4. Write a program which accepts one number and prints reverse of that number.

def main():

     print("Enter elements : ")
     Number = input()          

     Size = len(Number)

     Reversed = list()

     for i in range(Size - 1, -1, -1):
          Reversed.append(Number[i])

     print("Reversed number is : ", Reversed)
    
if __name__ == "__main__":
    main()


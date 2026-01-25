# 9. Write a lambda function using reduce ( ) which accepts a list of numbers and returns the product of all elements.

from functools import reduce 
def main():

     print("Enter the number of elements ")
     Size = int(input())

     Data = list()
     print("Enter the elements: ")
     for i in range(Size):
          Value = int(input())
          Data.append(Value)
    
     FData = reduce(lambda No1,No2: No1*No2,Data)
     print("Reduced Data is",FData)

if __name__ == "__main__":
    main()

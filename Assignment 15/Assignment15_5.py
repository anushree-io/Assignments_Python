# 5. Write a lambda function using reduce () which accepts a list of numbers and returns the maximum element.

from functools import reduce 

def main():
     Size = 0
     Value = 0

     print("Enter the number of elements: ")
     Size = int(input())

     Data = list()
     print("Enter the elements: ")
     for i in range(Size):
          Value = int(input())
          Data.append(Value)   
    
     print("Data is:",Data)

     RData = reduce((lambda No1,No2: No1 if No1>No2 else No2),Data)
     print("Max Data is",RData)

if __name__ == "__main__":
    main()
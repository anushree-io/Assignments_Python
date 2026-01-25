# 1. Write a lambda function using map () which accepts a list of numbers and returns a list of squares of each number.

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

     MData = list(map(lambda No: No**2,Data))
     print("Mapped Data is",MData)

if __name__ == "__main__":
    main()
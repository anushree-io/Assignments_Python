# 3. Write a lambda function using filter () which accepts a list of numbers and returns a list of odd numbers.


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

     FData = list(filter(lambda No: No%2==1,Data))
     print("Filtered Data is",FData)

if __name__ == "__main__":
    main()
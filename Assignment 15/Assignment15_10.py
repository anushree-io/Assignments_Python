# 10.Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.


def main():

     print("Enter the number of elements ")
     Size = int(input())

     Data = list()
     print("Enter the elements: ")
     for i in range(Size):
          Value = (input())
          Data.append(Value)
    
     FData = list(filter(lambda No: No%2==0 and len(No),Data))
                  
     print("Reduced Data is",FData)

if __name__ == "__main__":
    main()
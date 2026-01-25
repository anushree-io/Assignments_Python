# 10.Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.


def main():

     print("Enter the number of elements ")
     Size = int(input())

     Data = list()
     print("Enter the elements: ")
     for i in range(Size):
          Data.append(int(input()))
    
     EvenNum = list(filter(lambda No: No % 2 == 0,Data))
     Length = len(EvenNum)
                  
     print("Count of even Num is:",Length)

if __name__ == "__main__":
    main()
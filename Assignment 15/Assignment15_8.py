# 8. Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers
# divisible by both 3 and 5.

def main():

     print("Enter the number of elements ")
     Size = int(input())

     Data = list()
     print("Enter the elements: ")
     for i in range(Size):
          Value = int(input())
          Data.append(Value)
    
     FData = list(filter(lambda s: s%3==0 and s%5==0,Data))
     print("Filtered Data is",FData)

if __name__ == "__main__":
    main()

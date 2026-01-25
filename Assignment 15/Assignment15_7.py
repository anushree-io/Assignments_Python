# 7. Write a lambda function using filter () which accepts a list of strings and returns a list of strings
# having length greater than 5.

def main():

     print("Enter the number of string: ")
     Size = int(input())

     Data = list()
     print("Enter the elements: ")
     for i in range(Size):
          Value = input()
          Data.append(Value)
    
     FData = list(filter(lambda s: len(s) > 5,Data))
     print("Filtered Data is",FData)

if __name__ == "__main__":
    main()

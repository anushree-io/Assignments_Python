# 2. Write a program which accept one number and display below pattern.
# Input : 5    Output : pattern should be matrix of 5x5 of *

def DispPattern():
    Pattern = int(input("Enter a number:"))
    for i in range(Pattern):        
            print("*  " * Pattern)
print()               

DispPattern()
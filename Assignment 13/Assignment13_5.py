
# 5. Write a program which accepts marks and displays grade.

Marks = int(input("Enter marks:"))

if Marks >= 75:
    print("Distinction")

elif Marks >= 60:
    print("First Class")
    
elif Marks >= 50:
    print("Second Class")
    
else:
    print("Fail")


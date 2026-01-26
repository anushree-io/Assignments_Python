
num = int(input("Enter number of elements: "))
lst = []

for i in range(num):
    lst.append(int(input()))

value = int(input("Enter element to check freq: "))

count = 0
for num in lst:
    if num == value:
        count = count + 1

print("Frequency:", count)


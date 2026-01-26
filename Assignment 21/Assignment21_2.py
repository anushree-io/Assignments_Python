import threading

def FindMax(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    print("Maximum:", maximum)

def FindMin(lst):
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    print("Minimum:", minimum)


n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))


t1 = threading.Thread(target=FindMax, args=(lst,))
t2 = threading.Thread(target=FindMin, args=(lst,))


t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")

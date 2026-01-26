import threading


def EvenList(lst):
    evensum = 0
    print("Even Numbers:")
    for num in lst:
        if num % 2 == 0:
            print(num)
            evensum = evensum + num
    print("Sum of Even Numbers:", evensum)


def OddList(lst):
    oddsum = 0
    print("Odd Numbers:")
    for num in lst:
        if num % 2 != 0:
            print(num)
            oddsum = oddsum + num
    print("Sum of Odd Numbers:", oddsum)

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))


t1 = threading.Thread(target=EvenList, args=(lst,))
t2 = threading.Thread(target=OddList, args=(lst,))


t1.start()
t2.start()


t1.join()
t2.join()

print("Exit from main")

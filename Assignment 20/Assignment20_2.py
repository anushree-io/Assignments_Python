import threading


def EvenFactor(n):
    total = 0
    print("Even Factors:")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            print(i)
            total = total + i
    print("Sum of Even Factors:", total)


def OddFactor(n):
    total = 0
    print("Odd Factors:")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            print(i)
            total = total + i
    print("Sum of Odd Factors:", total)

num = int(input("Enter a number: "))


t1 = threading.Thread(target=EvenFactor, args=(num,))
t2 = threading.Thread(target=OddFactor, args=(num,))


t1.start()
t2.start()


t1.join()
t2.join()

print("Exit from main")

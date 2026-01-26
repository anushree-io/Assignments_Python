import threading

def isPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def Prime(lst):
    print("Prime Numbers:")
    for num in lst:
        if isPrime(num):
            print(num)

def NonPrime(lst):
    print("Non-Prime Numbers:")
    for num in lst:
        if not isPrime(num):
            print(num)


n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))


t1 = threading.Thread(target=Prime, args=(lst,))
t2 = threading.Thread(target=NonPrime, args=(lst,))


t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")

import threading

def Small(text):
    count = 0
    for ch in text:
        if ch.islower():
            count = count + 1

    print("\nSmall Thread")
    print("Lowercase count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def Capital(text):
    count = 0
    for ch in text:
        if ch.isupper():
            count = count + 1

    print("\nCapital Thread")
    print("Uppercase count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def Digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count = count + 1

    print("\nDigits Thread")
    print("Digit count:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)


text = input("Enter a string: ")

t1 = threading.Thread(target=Small, args=(text,), name="Small")
t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
t3 = threading.Thread(target=Digits, args=(text,), name="Digits")


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

print("\nExit from main")

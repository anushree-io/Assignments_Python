

import MarvellousNum

def ListPrime(lst):
    total = 0
    for num in lst:
        if MarvellousNum.ChkPrime(num):
            total = total + num
    return total

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

result = ListPrime(lst)
print("Sum of prime numbers:", result)

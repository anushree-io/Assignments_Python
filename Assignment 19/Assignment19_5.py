
from functools import reduce


def Prime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True


def multiply(no):
    return no * 2


def Max(a, b):
    if a > b:
        return a
    else:
        return b


data = [2, 70, 11, 10, 17, 23, 31, 77]


fdata = list(filter(Prime, data))
print("List after filter =", fdata)


mdata = list(map(multiply, fdata))
print("List after map =", mdata)


result = reduce(Max, mdata)
print("Output of reduce =", result)


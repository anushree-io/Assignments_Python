
from functools import reduce

data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# Filter: numbers between 70 and 90
fdata = list(filter(lambda x: x >= 70 and x <= 90, data))
print("List after filter =", fdata)

# Map: add 10 to each number
mdata = list(map(lambda x: x + 10, fdata))
print("List after map =", mdata)

# Reduce: product of all numbers
result = reduce(lambda a, b: a * b, mdata)
print("Output of reduce =", result)

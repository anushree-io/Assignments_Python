
from functools import reduce

data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

# Filter: even numbers
fdata = list(filter(lambda x: x % 2 == 0, data))
print("List after filter =", fdata)

# Map: square of each number
mdata = list(map(lambda x: x * x, fdata))
print("List after map =", mdata)

# Reduce: sum of numbers
result = reduce(lambda a, b: a + b, mdata)
print("Output of reduce =", result)

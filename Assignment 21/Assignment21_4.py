import threading

sum_result = 0
prod_result = 1

def SumList(lst):
    global sum_result
    total = 0
    for num in lst:
        total = total + num
    sum_result = total

def ProductList(lst):
    global prod_result
    product = 1
    for num in lst:
        product = product * num
    prod_result = product


n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))


t1 = threading.Thread(target=SumList, args=(lst,))
t2 = threading.Thread(target=ProductList, args=(lst,))


t1.start()
t2.start()

t1.join()
t2.join()

print("Sum:", sum_result)
print("Product:", prod_result)

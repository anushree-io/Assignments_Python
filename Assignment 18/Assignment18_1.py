
def main():
    num = int(input("Enter number of elements: "))
    data = []
    sum = 0

    for i in range(num):
        value = int(input())
        data.append(value)
        sum  = sum + value

    print("Sum is :", sum)

if __name__ == "__main__":
    main()
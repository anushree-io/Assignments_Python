
def main():

    num = input("Enter a number: ")

    total = 0
    for i in num:
        values = int(i)
        total = total + values

    print("Sum of digits:", total)

if __name__ == "__main__":
    main()
# 1. Write a program which accepts one character and checks whether it is vowel or

def main():
    Vowels = ['a','e','i','o','u']
    print("Enter a charecter :")
    Data = input()

    if Data in Vowels:
        print(Data, "is Vowel")
    else:
        print("Not a Vowel")

if __name__ == "__main__":
    main()



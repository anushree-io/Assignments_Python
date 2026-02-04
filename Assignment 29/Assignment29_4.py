
import sys

def CompareContents(FileName1,FileName2):

    fobj1 = open(FileName1,"r")
    Data1 = fobj1.read()
    fobj1.close()

    fobj2 = open(FileName2, "r")
    Data2 = fobj2.read()
    fobj2.close()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")


def main():
    if len(sys.argv) != 3:
        print("Insufficient arguments")
        return

    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]
    CompareContents(FileName1,FileName2)


if __name__ == "__main__":
    main()


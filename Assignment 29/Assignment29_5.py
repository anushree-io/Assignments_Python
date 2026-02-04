import sys

def FreqStr(FileName,name):

    fobj = open(FileName,"r")
    Data = fobj.read()
    fobj.close()

    Count = Data.count(name)
    print("Frequency of string is:", Count)

def main():
    if len(sys.argv) != 3:
        print("Insufficient arguments")
        return

    FileName = sys.argv[1]
    name = sys.argv[2]
    FreqStr(FileName,name)

if __name__ == "__main__":
    main()


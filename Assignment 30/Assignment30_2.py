
import sys

def CountLines(FileName):

    count = 0

    fobj = open(FileName, "r")

    for i in fobj:
        count = count+1

    fobj.close()

    print("Total number of lines in the file are:", count)
    
def main():

    name = input("Enter file name:")
    CountLines(name)

if __name__ == "__main__":
    main()





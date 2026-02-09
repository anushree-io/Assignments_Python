# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo. txt, and copies all contents from the given file into Demo.txt.

import sys

def CopyContents(FileName):

    fobj = open(FileName, "r")
    Data = fobj.read()
    fobj.close()

    dobj = open("Demo.txt", "w") 
    dobj.write(Data)
    dobj.close()

def main():
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        return

    FileName = sys.argv[1]
    CopyContents(FileName)


if __name__ == "__main__":
    main()


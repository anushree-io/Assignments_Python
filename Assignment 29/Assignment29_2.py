import os

def main():
    fobj = None

    FileName = input("Enter the file name:")
    fobj = open(FileName, 'r')
    Data = fobj.read()
    print("Contents from file are:", Data)
    
    fobj.close()
    
if __name__ == "__main__":
    main()
    
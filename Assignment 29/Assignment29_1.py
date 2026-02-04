
import os

def main():
    FileName = input("Enter the file name:")

    Ret = os.path.exists(FileName)

    if Ret == True:
        print("File Exists")
    else:
        print("File does not exists")
    
if __name__ == "__main__":
    main()
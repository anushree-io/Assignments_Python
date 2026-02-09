# 1.Design automation script which accept directory name and display checksum of all files.

# Usage : DirectoryChecksum.py "Demo"

# Demo is name of directory.

import hashlib
import os
import sys

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)   # Update hash object with bytes that are completed reading from file
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

def DirectoryChecksum(DirectoryName = "Demo"):

    Ret = False
    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("It is not a directory")
        return  
    print("FILES FOUND IN DEMO:", os.listdir(DirectoryName))
    for FolderName, Subfolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateCheckSum(fname)
    
            print(f"File Name : {fname}  Checksum : {Checksum}")

    
def main():
    print("-----Directory Checksum Application-----")

    if len(sys.argv) != 2:
        print("Insufficient arguments")
        print("Usage : DirectoryChecksum.py <Directory Name>")
        return
    
    DirectoryChecksum(sys.argv[1])

if __name__ == "__main__":
    main()  
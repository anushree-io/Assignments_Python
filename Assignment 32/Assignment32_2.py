# 2. Design automation script which accept directory name and write names of duplicate files from
# that directory into log file named as Log.txt. Log.txt file should be created into current
# directory.

# Usage : DirectoryDusplicate.py "Demo"

# Demo is name of directory.

import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def DirectoryDuplicate(DirName = "Demo"):
    Ret = False
    Ret = os.path.exists(DirName)
    if Ret == False:
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if Ret == False:
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateCheckSum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            
            else:
                Duplicate[Checksum] = [fname]
            
            lobj = open("Log.txt","w")
            lobj.write("*"*60 + "\n")
            lobj.write("Duplicate Files in Directory : " + DirName + "\n")
            lobj.write("*"*60 + "\n")

            for checksum in Duplicate:
                if len(Duplicate[checksum]) > 1:
                    for fname in Duplicate[checksum]:
                        lobj.write(fname + "\n")
            lobj.close()

def main():

    print("-----Directory Duplicate File Application-----")

    if len(sys.argv) != 2:
        print("Insufficient arguments")
        return
    DirectoryDuplicate(sys.argv[1])


if __name__ == "__main__":
    main()
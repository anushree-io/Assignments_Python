# 3. Design automation script which accept directory name and delete all duplicate files from that directory. 
# Write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory.
# Usage : DirectoryDusplicateRemoval.py "Demo"
# Demo is name of directory.

import sys
import os
import hashlib

def CalculateChecksum(FileName):

    fobj = open(FileName , 'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while len(Buffer) > 0 :
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()
    return hobj.hexdigest()


def DirectoryDuplicateRemove(DirName = "Demo"):

    if not os.path.exists(DirName):
        print("There is no such directory")
        return

    if not os.path.isdir(DirName):
        print("It is not a directory")
        return

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            Checksum = CalculateChecksum(fname)
  
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
    
    return Duplicate


def DeleteDuplicate(Path = "Demo"):
    
    MyDict = DirectoryDuplicateRemove(Path)
        
    if(MyDict is None):
        return

    lobj = open("LogFile.txt", "w")

    lobj.write("*" * 60 + "\n")
    lobj.write("Duplicate Files Deleted From : " + Path + "\n")
    lobj.write("*" * 60 + "\n")

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
    
    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:

            Count = Count + 1 

            if Count > 1:
                lobj.write(subvalue + "\n")

                print("Deleted file:",subvalue)
                os.remove(subvalue)
                Cnt = Cnt +1

        Count = 0
    
    lobj.close()

    print("Total deleted files are:",Cnt)    

def main():
    print("-----Directory Duplicate Removal Application-----")

    if len(sys.argv) != 2:
        print("Usage : python Assignment32_3.py \"DirectoryName\"")
        return
    
    # DirectoryDuplicateRemove(sys.argv[1])
    DeleteDuplicate(sys.argv[1])



if __name__ == "__main__":
    main()
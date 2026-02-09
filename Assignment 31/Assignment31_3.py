# 3. Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.

# Usage : DirectoryCopy.py "Demo" "Temp"

# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp.

import os
import sys
import shutil

def DirectoryCopy(DirName1 = "Demo", DirName2 = "Temp"):

    Ret = False
    Ret = os.path.exists(DirName1)
    
    if Ret == False:
        print("There is no such directory.")
        return
    
    Ret = os.path.isdir(DirName1)

    if Ret == False:
        print("It is not a directory")
        return
    
    Ret = os.path.exists(DirName2)
    if Ret == False:
        os.makedirs(DirName2)

    
    for FolderName, SubFolder, FileName in os.walk(DirName1):
        print("FolderName:",FolderName)
        print("The files in Demo directory are:",FileName)
        for fname in FileName:
            Path1 = os.path.join(FolderName,fname)   # output: Assignment31\Demo\...(all files)
            Path2 = os.path.join(DirName2,fname)     # output: Assignment31\Temp\...(all files)
            shutil.copy(Path1,Path2)                 # copy file from Path1 to Path2
        print("Files copied successfully.")

def main():

    print(65*'*')
    print("Application to copy files from one directory to another directory")
    print(65*'*')

    if len(sys.argv) != 3:
        print("Insufficient number of arguments:")
        print("Usage: DirectoryCopy.py [Existing Directory] [New Directory]")

    DirName1 = sys.argv[1]
    DirName2 = sys.argv[2]

    DirectoryCopy(DirName1, DirName2)

if __name__ == "__main__":
    main()
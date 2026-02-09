# 4. Design automation script which accept two directory names and one file extension. Copy all
# files with the specified extension from first directory into second directory. Second directory
# should be created at run time.

# Usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"

# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files with extension .exe from Demo to Temp.

import sys
import os
import shutil

def DirectoryCopyExt(DirName1 = "Demo", DirName2 = "Temp1", Extension = ".exe"):

    Ret = os.path.exists(DirName1)
    if Ret == False:
        print("There is no such Directory.")
        return
        
    Ret = os.path.isdir(DirName1)
    if Ret == False:
        print("It is not a directory.")
        return
    
    Ret = os.path.exists(DirName2)
    if Ret == False:
        os.makedirs(DirName2)
  
    for FolderName,SubFolderName,FileName in os.walk(DirName1):
        print("FolderName:",FolderName)
        print("Files in Demo Directory are:",FileName)

        for fname in FileName:

            if fname.endswith(Extension):
                Path1 = os.path.join(FolderName,fname) 
                Path2 = os.path.join(DirName2,fname)
                shutil.copy(Path1,Path2)
                
        print("Files with exe extension copied sucessfully into Temp1")

def main():
    print("This Automation script copies .exe files from one directory to another.")
    print("*"*65)

    if len(sys.argv) != 4:
        print("Insufficient number of argumrnts.")
        return
    
    DirName1 = sys.argv[1]
    DirName2 = sys.argv[2]
    Extension = sys.argv[3]

    DirectoryCopyExt(DirName1,DirName2,Extension)

if __name__ == "__main__":
    main()


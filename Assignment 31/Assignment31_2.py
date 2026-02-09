
# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
# Usage : DirectoryRename.py "Demo"".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename
# with .doc.
# After execution this script each .txt file gets renamed as .doc.

import os
import sys

def DirectoryRename(DirName = "Demo",Extension1 = ".txt", Extension2 = ".doc"):

    Ret = False

    Ret = os.path.exists(DirName)
    if (Ret == False):
        print("There is no such directory.")
        return
    
    Ret = os.path.isdir(DirName)
    if (Ret == False):
        print("It is not a directory.")
        return
    
    
    for FolderName,SubFolder,FileName in os.walk(DirName):

        for fname in FileName:

            if fname.endswith(Extension1):
                
                path = os.path.join(FolderName,fname) 

                name = os.path.splitext(fname) [0]    # separating name and extension, [0] for name, [1] for extension. 
                newname = name + Extension2           # creating new name with new extension

                npath = os.path.join(FolderName,newname)   # creating new path with new name

                os.rename(path,npath)                      # and finally renaming old file to new file
                print("Renamed file from txt to doc: ", npath)

def main():

    if len(sys.argv) != 4:
        print("Invalid number of argumemts.")
        return
    
    DirName = sys.argv[1]
    Extension1 = sys.argv[2]
    Extension2 = sys.argv[3]

    DirectoryRename(DirName,Extension1,Extension2)

if __name__ == "__main__":
    main()


    
    








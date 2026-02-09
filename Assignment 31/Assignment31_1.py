
# 1.Design automation script which accept directory name and file extension from user. Display all
# files with that extension.
# Usage : DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search.

import os
import sys

def DirectoryFileSearch(DirName = "Demo",Extension = ".txt"):

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

            if fname.endswith(Extension):
                path = os.path.join(FolderName,fname) 
                print(path)

def main():

    if len(sys.argv) != 3:
        print("Invalid number of argumemts.")
        return
    
    DirName = sys.argv[1]
    Extension = sys.argv[2]

    DirectoryFileSearch(DirName,Extension)

if __name__ == "__main__":
    main()


    
    








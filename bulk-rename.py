#!/usr/bin/python3
import sys
import os


newName = str(sys.argv)
//get current working directory
cwd = os.getcwd()
current = 1

for filename in os.listdir(cwd):
    if not filename.contains(newName):
        //split filename at last .
        //combine string - newName + current + ending
        #os.rename(filename,  )
        current += 1


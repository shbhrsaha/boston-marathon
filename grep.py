
import os, sys

namesFile = open("names.txt","r")

for name in namesFile.readlines():

    sys.stderr.write(name)
    
    n = name.replace("\n","")
    
    os.system('grep "'+n+'" runners.txt')

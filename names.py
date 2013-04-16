
import os, sys, csv

file_path = sys.argv[1]
file  = open(file_path, "rU")
reader = csv.reader(file)

header = True
names = []

for row in reader:
    
    if header:
        header = False
        continue

    name = row[1] + ", " + row[0]
    names.append(name)

for name in names:

    print name
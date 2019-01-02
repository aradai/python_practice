#!/usr/bin/env python3
from datetime import datetime

def reader(path):
    with open(path, "r") as myf:
        temp = myf.read()
    
    return temp

def writer(cont1, cont2, cont3):
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    with open("{0}.txt".format(now), "w") as mf:
        #for i, j, k in zip(cont1, cont2, cont3):
        #    mf.write("{0}\n{1}\n{2}\n".format(i, j, k)) #looks overkill, but other kind of program it's useful <-not desired output
        mf.write("{0}\n".format(cont1))
        mf.write("{0}\n".format(cont2))
        mf.write("{0}".format(cont3))
        
writer(reader("file1.txt"), reader("file2.txt"), reader("file3.txt"))
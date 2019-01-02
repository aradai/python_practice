#!/usr/bin/env python3

temperatures = [10, -100, 100, 40000]

def c_to_f(c):
    return c * 9/5 +32
    
def writer(iterate, path):
    with open(path, "w") as myfile:
        for t in iterate:
            myfile.write("{0}\n".format(c_to_f(t)))

writer(temperatures, "temp.txt")
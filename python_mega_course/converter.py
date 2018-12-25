#!usr/bin/ env python3

def Cels_to_Fahr(cels = 0):
    return cels * 9.0/5.0 + 32

def Fahr_to_Cels(fahr = 0):
    return (fahr - 32) * 5.0/9.0

mylist = [0, 10, -20, 100]

for cels in mylist:
    print(Cels_to_Fahr(cels))
#!usr/bin/ env python3

def Cels_to_Fahr(cels = 0):
    return cels * 9.0/5.0 + 32

def Fahr_to_Cels(fahr = 0):
    return (fahr - 32) * 5.0/9.0

print(Cels_to_Fahr())
print(Cels_to_Fahr(36))
print(Fahr_to_Cels())
print(Fahr_to_Cels(90))
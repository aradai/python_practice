#!usr/bin/env python3.6

def length(a):
    if type(a) == str:
        return len(str(a))
    else:
        return "Sorry, give me a string"

print(length("mama"))
print(length(10))
print(length(True))
print(length("mamamamamamamama"))
#!/usr/bin/env python3
def logger(x):
    attempts = 0
    while x != "password" and attempts < 3:
        x = input("wrong password!\nTry again: ")
        attempts = attempts + 1
    
    return attempts < 3

pwrd = input("password: ")

if logger(pwrd) :
    print("logged in")
else:
    print("unauthorised attempt!")
    
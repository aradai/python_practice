#!/usr/bin/env python3

file = open("fruits.txt")
fruits = file.read()
fruits = fruits.splitlines()

for fruit in fruits:
    print(len(fruit))

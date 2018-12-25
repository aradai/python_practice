#!/usr/bin/env python3

file = open("fruits.txt")
fruits = file.read()
file.close
print(type(fruits))
fruits = fruits.splitlines()
print(fruits)
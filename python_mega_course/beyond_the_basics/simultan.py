#!/usr/bin/env python3

a = [1, 2, 3]
b = ["a", "b", "c"]

for i, j in zip(b, a):
    print("{0} is {1}".format(i, j))
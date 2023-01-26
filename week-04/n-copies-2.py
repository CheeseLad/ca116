#!/usr/bin/env python3

s = input()
n = int(input())

c = n != 0

#print(c * (n - 1) * (s + "-") + (s * (n + 1)))
print(c * (((s + "-") * (n - 1)) + s))

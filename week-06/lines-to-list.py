#!/usr/bin/env python3

a = []

n = input()
a.append(n)

while n != "end":
  n = input()
  a.append(n)

print(a[:- 1])

#!/usr/bin/env python3

a = []

n = input()
a.append(n)

while n != "end":
  n = input()
  a.append(n)

i = 0
while i < len(a) - 1:
  print(i, len(a) - 1, a[i])
  i = i + 1

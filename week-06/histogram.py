#!/usr/bin/env python3

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

n = input()
while n != "end":
  a[int(n)] += 1
  n = input()

i = 0
while i < 10:
  print(i, "*" * a[i])
  i = i + 1

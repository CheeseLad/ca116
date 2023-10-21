#!/usr/bin/env python3

import sys

n = int(input())
a = ["a"] * n

s = sys.stdin.readline().rstrip()
while len(s) > 0:
  a[int(s)] = int(s)
  s = sys.stdin.readline().rstrip()

b = []
i = 0
while i < len(a):
  if a[i] == i:
    b.append("*")
  else:
    b.append(" ")
  i = i + 1
print("|" + "".join(b) + "|")

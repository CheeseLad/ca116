#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
a = " ".join(s)
a = a.split()

i = 0
while i < len(a):
  if (a[i][0] >= "A" and a[i][0] <= "Z"):
    print(a[i])
  i = i + 1

#!/usr/bin/env python3

import sys
total = 0
a = sys.stdin.readlines()

i = 0
while i < len(a):
  total = total + int(a[i])
  i = i + 1

print(total)

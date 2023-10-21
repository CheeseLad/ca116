#!/usr/bin/env python3

import sys
files = sys.argv[1:]
b = []
i = 0
while i < len(files):
  with open(files[i]) as f:
    num = f.readlines()
    j = 0
    while j < len(num):
      split = num[j].rstrip()
      b.append(split)
      j = j + 1
  i = i + 1

total = 0
k = 0
while k < len(b):
  total = total + int(b[k])
  k = k + 1

print(total)

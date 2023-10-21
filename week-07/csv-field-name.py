#!/usr/bin/env python3

import sys

field = int(sys.argv[1])
a = []

s = "LatD,LatM,LatS,NS,LonD,LonM,LonS,EW,City,State"
i = 0
j = 0
while i < len(s):
  while i < len(s) and s[i] != ",":
    i = i + 1
  a.append(s[j:i])
  i = i + 1
  j = i

print(a[field])

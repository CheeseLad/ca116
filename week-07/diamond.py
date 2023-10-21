#!/usr/bin/env python3

import sys

n = int(sys.argv[1])

half = n // 2
k = half
i = 1

while i < n:
  print(" " * k + "*" * i)
  i = i + 2
  k = k - 1
print("*" * n)

j = 0
o = 1
while j < half:
  print(" " * o + "*" * (n - 2))
  o = o + 1
  j = j + 1
  n = n - 2

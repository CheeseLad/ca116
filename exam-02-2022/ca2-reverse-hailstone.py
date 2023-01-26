#!/usr/bin/env python3

import sys
a = []
n = int(sys.argv[1])
a.append(n)
i = 0
while i < 9:
  if n % 2 == 0:
    n = n // 2
  else:
    n = n * 3 + 1
  a.append(n)
  i = i + 1

i = len(a) - 1

while i >= 0:
  print(a[i])
  i = i - 1

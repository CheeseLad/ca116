#!/usr/bin/env python3

import sys
values = [0] * 20
s = sys.stdin.readline().rstrip()
while len(s) > 0:
  if int(s) >= 0:
    values[int(s)] += 1
  s = sys.stdin.readline().rstrip()

a = values
p = 0
j = p + 1
while j < len(a):
  if a[j] > a[p]:
    p = j
  j = j + 1
high = a[p]

final = []
j = 0
while j < high:
  i = 0
  line = []
  while i < len(values):
    if values[i] == 0:
      line.append(" ")
    elif values[i] >= 1:
      line.append("*")
      values[i] -= 1
    i = i + 1
  fline = "".join(line).rstrip()
  final.append(fline)
  j = j + 1

i = len(final) - 1
while i >= 0:
  print(" | " + final[i])
  i = i - 1

print(" " + "-" * 23)

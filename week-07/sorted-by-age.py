#!/usr/bin/env python3

a = []
b = []
s = input()
while s != "end":
  data = s[6:8] + s[3:5] + s[0:2] + s[9:]
  a.append(data)
  b.append(s[9:])
  s = input()

i = 0
while i < len(a):
  p = i
  j = i + 1
  while j < len(a):
    if a[j] < a[p]:
      p = j
    j = j + 1

  tmp = a[p]
  a[p] = a[i]
  a[i] = tmp

  i = i + 1

i = 0
while i < len(a):
  print(a[i][6:])
  i = i + 1

#!/usr/bin/env python3

i = 0
a = []

n = input()
if n != "end":
  a.append(int(n))
while n != "end":
  a.append(int(n))
  n = input()

while i < len(a):
  p = i
  j = i + 1
  while j < len(a):
    if a[j] > a[p]:
      p = j
    j = j + 1
  tmp = a[p]
  a[p] = a[i]
  a[i] = tmp

  i = i + 1

print(a[p])

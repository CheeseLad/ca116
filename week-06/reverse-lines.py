#!/usr/bin/env python3

a = []


n = input()
if n != "end":
  a.append(n)

while n != "end":
  n = input()
  if n != "end":
    a.append(n)

i = 0
while i < len(a):
  print(a[len(a) - i - 1])
  i = i + 1

#!/usr/bin/env python3

a = []

n = input()
if n != "end":
  v = int(n)
  a.append(v)
while n != "end":
  n = input()
  if n != "end":
    v = int(n)
    a.append(v)

print(a)

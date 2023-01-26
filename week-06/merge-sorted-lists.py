#!/usr/bin/env python3

a = []
b = []

s = input()
while s != "end":
  a.append(int(s))
  s = input()

n = input()
while n != "end":
  b.append(int(n))
  n = input()

i = 0
j = 0
while i < len(a) and j < len(b):
  if a[i] < b[j]:
    print(a[i])
    i = i + 1
  else:
    print(b[j])
    j = j + 1

while i < len(a):
  print(a[i])
  i = i + 1

while j < len(b):
  print(b[j])
  j = j + 1

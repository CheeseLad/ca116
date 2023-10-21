#!/usr/bin/env python3

a = []

n = input()
while n != "end":
  a.append(int(n))
  n = input()

if n == "end":
  num = int(input())

p = num
j = p + 1
while j < len(a):
  if a[j] < a[p]:
    p = j
  j = j + 1

print(p)

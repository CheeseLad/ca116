#!/usr/bin/env python3

a = []

n = input()
if n != "end":
  a.append(n)

while n != "end":
  n = input()
  if n != "end":
    a.append(n)
  if n == "end":
    final = int(input())


i = 0
while i < len(a):
  print(int(a[i]) + final)
  i = i + 1

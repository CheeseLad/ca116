#!/usr/bin/env python3

a = []

n = input()
if n != "end":
  a.append(n)

while n != "end":
  n = input()
  if n != "end":
    a.append(n)

#while n != "end":
#  n = input()
#  if n != "end":
#    i = 0
#    while i < len(a) and a[i] != n:
#      i = i + 1
#      if i < len(a) and a[i] != n:
#        a.append(n)

print(a)
#i = 0
#while i < len(a):
#  print(a[i])
#  i = i + 1

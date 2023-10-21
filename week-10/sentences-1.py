#!/usr/bin/env python3

import sys

a = []

#s = sys.stdin.readline().rstrip()
#while len(s) > 0:
#  a.append(s)
#  s = sys.stdin.readline().rstrip()
#print(a)

s = sys.stdin.readlines()
print(s)

i = 0
while i < len(s):
  s[i] = s[i].rstrip()
  i = i + 1


s = (" ".join(s))
s = s.split()
s = (" ".join(s))
print(s.split())

i = 0
while i < len(a):
  k = 0
  while k < len(s) and (a[s] >= "A" and a[s] <= "Z"):
    k = k + 1
  j = 0
  while j < len(s) and a[s] != "." and a[s] != "!" and a[s] != "?":
    j = j + 1
  if j < len(s):
    print(s[k:j + 1] + "\n")
  i = i + 1

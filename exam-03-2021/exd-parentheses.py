#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
a = []
#print(s)

i = 0
while i < len(s):
  split = s[i]
  j = 0
  k = 0
  while j < len(split) and split[j] != "(":
    j = j + 1
  while k < len(split) and split[k] != ")":
    k = k + 1
#  print(split[j])
#  print(split[k])
#  if split[j] == "(" and split[k] == ")":
  a.append(split[j + 1:k])
  i = i + 1
i = 0
while i < len(a):
  if len(a[i]) > 0:
    print(a[i])
  i = i + 1
#print(a)

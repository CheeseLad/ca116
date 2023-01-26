#!/usr/bin/env python3

s = str(input())
i = 0
t = ""
o = len(s)

while i < len(s):
  t = s[i:len(s)]
  print(t)
  i = i + 1
  o = o - 1

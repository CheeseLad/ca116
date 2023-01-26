#!/usr/bin/env python3

s = input()

i = 0
j = 0
o = 0

while j < len(s) and i < len(s):
  while s[i] != "," and i < len(s):
    i = i + 1
  print(s[o:i])

  i = i + 1
  o = i
  j = j + 1

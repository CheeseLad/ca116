#!/usr/bin/env python3

s = input()

i = 0
j = 0

while i < len(s):
  while i < len(s) and s[i] != ",":
    i = i + 1
  print(s[j:i])

  j = i + 1
  i = i + 1

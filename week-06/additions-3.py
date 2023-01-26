#!/usr/bin/env python3


while sum != 1000:
  s = input()
  i = 0
  while s[i] != "+":
    i = i + 1
  sum = (int(s[:i]) + int(s[i:]))
  print(sum)

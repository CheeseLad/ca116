#!/usr/bin/env python3


j = 0
i = 0

while j < 10:
  s = input()
  i = 0
  while s[i] != "+":
    i = i + 1
  print(int(s[:i]) + int(s[i:]))
  j = j + 1

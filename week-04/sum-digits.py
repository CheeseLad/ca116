#!/usr/bin/env python3

s = str(input())
i = 0
t = 0

while i < len(s):
  t = int(s[i]) + t
  i = i + 1
print(t)

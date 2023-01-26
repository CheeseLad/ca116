#!/usr/bin/env python3

s = input()
i = 0
p = -1
while i < len(s):
  if s[i] == " ":
    p = i
    i = len(s)
  i = i + 1
print(p)

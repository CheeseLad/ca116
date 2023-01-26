#!/usr/bin/env python3

s = input()
j = 0
i = 0

while i < len(s):
  if s[i] >= "a" and s[i] <= "z":
    j = j + 1
  i = i + 1
print(j)

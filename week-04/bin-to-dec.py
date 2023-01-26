#!/usr/bin/env python3

s = input()
i = 0
total = 0

while i < len(s):
  total = total + int(s[len(s) - i - 1]) * (2 ** i)
  i = i + 1
print(total)

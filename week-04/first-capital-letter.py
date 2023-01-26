#!/usr/bin/env python3

s = input()
i = 0

while i < len(s):
  ch = s[i]
  num = i
  if "A" <= ch and ch <= "Z":
    print(num)
    i = len(s)
  i = i + 1

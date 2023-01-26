#!/usr/bin/env python3

s = input()


i = 0
while i < len(s):
  ch = s[i]
  if "a" <= ch and ch <= "g":
    print(ch)
    i = len(s)
  i = i + 1

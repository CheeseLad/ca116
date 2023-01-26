#!/usr/bin/env python3

s = input()

i = 0
t = ""

while i < len(s):
  ch = s[i]
  if ch >= "a" and ch <= "z":
    o = ord(s[i]) - 32
    t = t + chr(o)
  else:
    t = t + ch
  i = i + 1
print(t)

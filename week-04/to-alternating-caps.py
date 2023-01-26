#!/usr/bin/env python3

s = input()
i = 0
small = True
t = ""

while i < len(s):
  if s[i] >= "A" and s[i] <= "Z" and small:
    t = t + chr(ord(s[i]) + ord("a") - ord("A"))
  elif s[i] >= "a" and s[i] <= "z" and not small:
    t = t + chr(ord(s[i]) + ord("A") - ord("a"))
  else:
    t = t + s[i]
  if s[i] >= "A" and s[i] <= "Z" or s[i] >= "a" and s[i] <= "z":
    small = not small
  i = i + 1
print(t)

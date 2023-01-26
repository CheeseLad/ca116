#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
  if s[i] >= "0" and s[i] <= "9":
    print(s[i], i)
    i = len(s)
  i = i + 1

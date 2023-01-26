#!/usr/bin/env python3

s = input()
i = 0
while i < len(s):
  if s[i] == ".":
    print(s[:i])
    print(s[i + 1:])
  i = i + 1

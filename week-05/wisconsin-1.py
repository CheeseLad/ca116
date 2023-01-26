#!/usr/bin/env python3

header = input()
s = input()
while s != "end":
  i = 0
  j = 0
  while i < len(s) and s[i] != ",":
    i = i + 1
  j = i + 1
  if i < len(s) and s[j] == "W":
    k = j + 1
    if i < len(s) and s[k] == "I":
      print(s[:i])
  s = input()

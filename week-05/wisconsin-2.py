#!/usr/bin/env python3

s = input()
total = 0
while s != "end":

  i = 0

  while i < len(s) and s[i] != ",":
    i = i + 1

  j = i + 1

  if s[j] == "W":
    j = j + 1
    if s[j] == "I":
      total = total + 1
  s = input()

print(total)

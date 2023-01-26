#!/usr/bin/env python3

header = input()
n = input()
while n != "end":
  i = 0
  while i < len(n) and n[i] != ",":
    i = i + 1
    if n[i] == ",":
      if n[i - 4:i] == "City":
        print(n[:i])
        i = len(n)
  n = input()

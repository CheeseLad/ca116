#!/usr/bin/env python3

total = 0
s = input()
while s != "end":
  token = s.split()
  total = total + int(token[2])
  s = input()

print(total)

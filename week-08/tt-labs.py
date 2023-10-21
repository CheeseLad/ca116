#!/usr/bin/env python3

s = input()
while s != "end":
  token = s.split()
  if int(token[2]) > 1:
    print(s)
  s = input()

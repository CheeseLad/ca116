#!/usr/bin/env python3

i = 0
p = int(input())

while i < 9:
  n = int(input())
  if n < p:
    p = n
  i = i + 1
print(p)

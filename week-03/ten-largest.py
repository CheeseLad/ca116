#!/usr/bin/env python3

i = 0
m = int(input())

while i < 9:
  n = int(input())
  if n > m:
    m = n
  i = i + 1
print(m)

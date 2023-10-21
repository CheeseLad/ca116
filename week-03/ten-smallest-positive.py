#!/usr/bin/env python3

i = 0
first = 1
m = int(input())

while i < 9:
  n = int(input())
  if n < m and n > 0:
    first = n
    m = n
  i = i + 1
print(first)

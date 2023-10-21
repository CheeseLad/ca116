#!/usr/bin/env python3

i = 0
m = 0

while i < 10:
  n = int(input())
  if n % 2 == 0:
    m = m + n
  i = i + 1
print(m)

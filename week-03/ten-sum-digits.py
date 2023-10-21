#!/usr/bin/env python3

i = 0
total = 0

while i < 10:
  n = int(input())
  if n < 0:
    n = n * -1
    r = n % 10
    total = total + r
  else:
    r = n % 10
    total = total + r
  i = i + 1
print(total)

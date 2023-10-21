#!/usr/bin/env python3

m = 0
i = 0
total = 0

while i < 10:
  n = int(input())
  if n > 0:
    m = n * -1
    total = total + m
  else:
    total = total + n
  i = i + 1
print(total * -1)

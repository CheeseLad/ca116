#!/usr/bin/env python3

total = 0
i = 0
while i < 5:
  n = int(input())
  if n < 0:
    positive = n * -1
  else:
    positive = n
  total = total + positive
  i = i + 1
print(total)

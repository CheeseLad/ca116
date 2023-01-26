#!/usr/bin/env python3

p = -1
i = 0
first = 0

while first != 1:
  n = int(input())
  if p // 2 == n and first != 1:
    a = p
    b = n
    first = 1
  elif (3 * p) + 1 == n and first != 1:
    a = p
    b = n
    first = 1
  i = i + 1
  p = n
if first == 1 and a > 0 and b > 0:
  print(a, b)

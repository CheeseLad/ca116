#!/usr/bin/env python3

total = 0
n = int(input())
#total = n
while n != 0:
  if n < 0:
    positive = n * -1
  else:
    positive = n
  total = total + positive
  n = int(input())
print(total)

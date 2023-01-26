#!/usr/bin/env python3

i = 0
while i < 10:
  n = int(input())
  if n < 0:
    print(str(n) + " is negative")
  elif n > 0:
    print(str(n) + " is positive")
  i = i + 1

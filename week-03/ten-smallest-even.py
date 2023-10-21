#!/usr/bin/env python3

p = 0
i = 0
o = 0

m = int(input())
if m % 2 == 0:
  o = m

while i < 9:
  n = int(input())
  if n % 2 == 0 and n < o:
    p = n
    o = n
  i = i + 1
print(p)

#!/usr/bin/env python3

n = int(input())
bin = ""
i = 0
p = 0
o = 1

while n > o:
  p = o
  o = 2 ** i
  i = i + 1

while p != 0:
  bine = n // p
  n = n % p
  bin = bin + str(bine)
  p = p // 2
  i = i + 1
print(bin)

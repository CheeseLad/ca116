#!/usr/bin/env python3

i = 0
realvalue = ""

while i < 10:
  value = input()
  realvalue = realvalue + value
  i = i + 1

i = 0

while i < 10:
  print(realvalue[len(realvalue) - i - 1])
  i = i + 1

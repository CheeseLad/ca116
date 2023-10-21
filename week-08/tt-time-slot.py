#!/usr/bin/env python3

s = input()
while s != "end":
  t = s.split()
  st = int(t[1])
  length = int(t[2])
  d = (st + length - 1) % 24
  line1 = " ".join(t[0:1]) + " " + str(st) + ":00"
  line2 = " " + str(d) + ":50" + " " + " ".join(t[3:])
  print(line1 + line2)
  s = input()

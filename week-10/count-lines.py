#!/usr/bin/env python3

import sys

line1 = sys.stdin.readline().strip().split()
line2 = sys.stdin.readline().strip().split()
line3 = sys.stdin.readline().strip().split()

print(line1)

i = 0
while i < len(line1):
  line1[i] = "1" + line1[i]
  i = i + 1

i = 0
while i < len(line2):
  line2[i] = "2" + line2[i]
  i = i + 1

i = 0
while i < len(line3):
  line3[i] = "3" + line3[i]
  i = i + 1

print(line1)

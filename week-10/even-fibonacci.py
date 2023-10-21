#!/usr/bin/env python3

import sys

args = sys.argv[1]
total = 0
prev = 0
curr = 1
i = 0
while curr <= int(args):
  tmp = curr
  curr = prev + curr
  prev = tmp
  if curr % 2 == 0 and curr < int(args):
    total = total + curr
  i = i + 1

print(total)

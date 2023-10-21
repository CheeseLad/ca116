#!/usr/bin/env python3

import sys

with open("input.txt") as f:
  lines = f.readlines()

j = 0
while j < len(lines):
  sys.stdout.write(lines[j])
  j = j + 1

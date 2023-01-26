#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
while len(s) > 0:
  tokens = s.split()
  if int(tokens[2]) >= 40:
    print(tokens[0] + " " + tokens[1])
  s = sys.stdin.readline().rstrip()

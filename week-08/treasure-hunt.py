#!/usr/bin/env python3

import os

with open("start.txt") as start:
  begin = start.readlines()
  begin = begin[0].rstrip()
  file = 1

tokens = begin.split(".")
#tokens = ["yes", "no"]
while len(tokens) > 1 or file == 1:
#  print(begin)
  if os.path.isfile(begin):
    with open(begin) as begin:
      begin = begin.readlines()
      begin = begin[0].rstrip()
      tokens = begin.split(".")
    file = 2

print(begin)

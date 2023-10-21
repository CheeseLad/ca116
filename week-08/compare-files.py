#!/usr/bin/env python3

import sys

files = sys.argv[1:]

with open(files[0]) as fa:
  filea = fa.readlines()

with open(files[1]) as fb:
  fileb = fb.readlines()

if len(filea) > len(fileb):
  print(len(filea) - len(fileb), 0)
if len(filea) < len(fileb):
  print(len(fileb) - len(filea), 0)

i = 0
while i < len(filea) and i < len(fileb):
  j = 0
  while j < len(filea[i]) and j < len(fileb[i]):
    if filea[i][j] != fileb[i][j]:
      print(i, j)
    j = j + 1
  i = i + 1

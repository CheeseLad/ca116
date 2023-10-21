#!/usr/bin/env python3

import sys

lines = {}
line = []

with open("a.txt") as fa:
  line = fa.readlines()

i = 0
while i < len(line):
  line[i] = line[i].rstrip()
  lines[line[i]] = 1
  i = i + 1

with open("b.txt") as fb:
  line = fb.readlines()

i = 0
while i < len(line):
  line[i] = line[i].rstrip()
  if line[i] in lines:
    lines[line[i]] = 3
  i = i + 1

for words in lines:
  if lines[words] == 1:
    print(words)

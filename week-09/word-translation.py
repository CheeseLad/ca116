#!/usr/bin/env python3

import sys

translation = {}

with open("translation.txt") as f:
  lines = f.readlines()

i = 0
while i < len(lines):
  lines[i] = lines[i].rstrip()
  i = i + 1

i = 0
while i < len(lines):
  tokens = lines[i].split()
  translation[tokens[0]] = tokens[1]
  i = i + 1

word = sys.stdin.readline().rstrip()
while len(word) > 0:
  if word in translation:
    print(translation[word])
  word = sys.stdin.readline().rstrip()

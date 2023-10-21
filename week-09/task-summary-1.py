#!/usr/bin/env python3

import sys

files = {}

s = sys.stdin.readline().rstrip()
while len(s) > 0:
  tokens = s.split(".")
  files[tokens[0]] = tokens[2]
  s = sys.stdin.readline().rstrip()

for words in files:
  if files[words] == "correct":
    print(words + "." + tokens[1])

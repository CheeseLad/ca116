#!/usr/bin/env python3

import sys

fruit = {
  "apple": True,
  "pear": True,
  "orange": True,
  "banana": True,
  "cherry": True,
}

words = sys.stdin.readline().rstrip()
while len(words) != 0:
  if words in fruit:
    print(words)

  words = sys.stdin.readline().rstrip()

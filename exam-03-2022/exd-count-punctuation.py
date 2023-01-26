#!/usr/bin/env python3

import sys
punctuation = {
  ".",
  ",",
  "?",
  "!"
}

total = 0
a = sys.stdin.readlines()
a = "".join(a)

i = 0
while i < len(a):
  if a[i] in punctuation:
    total = total + 1
  i = i + 1

print(total)

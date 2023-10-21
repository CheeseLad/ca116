#!/usr/bin/env python3

import sys
split = []
files = sys.argv[1:]
i = 0
total = 0
while i < len(files):
  with open(files[i]) as f:
    split = split + f.readlines()
  i = i + 1
#print(split)

j = 0
while j < len(split):
  split[j] = split[j].rstrip()
  j = j + 1
string = " ".join(split)

numbers = string.split()
#xprint(numbers)

k = 0
while k < len(numbers):
  total = total + int(numbers[k])
  k = k + 1

print(total)

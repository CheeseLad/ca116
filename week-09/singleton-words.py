#!/usr/bin/env python3

import sys

list = {}

words = sys.stdin.readlines()
i = 0
while i < len(words):
  word = words[i].rstrip()
  if word not in list:
    list[word] = 0
  list[word] = list[word] + 1
  i = i + 1
#print(list)

for animals in list:
  if list[animals] == 1:
    print(animals)

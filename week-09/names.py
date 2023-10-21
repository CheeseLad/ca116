#!/usr/bin/env python3

import sys

boys = {}

with open("boys.txt") as fb:
  bl = fb.readlines()

i = 0
while i < len(bl):
  word = bl[i].rstrip()
  boys[word] = "boy"
  i = i + 1

girls = {}

with open("girls.txt") as fg:
  gl = fg.readlines()

i = 0
while i < len(gl):
  word = gl[i].rstrip()
  girls[word] = "girl"
  i = i + 1


s = sys.stdin.readline().rstrip()
while len(s) > 0:
  if s in boys and s in girls:
    print(s, "either")
  elif s in girls:
    print(s, "girl")
  elif s in boys:
    print(s, "boy")
  s = sys.stdin.readline().rstrip()

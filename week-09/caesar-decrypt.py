#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
crypt = {}
src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

i = 0
while i < len(src):
  crypt[dst[i]] = src[i]
  i = i + 1

s = sys.stdin.readline().rstrip()
while len(s) > 0:
  i = 0
  word = ""
  while i < len(s):
    if s[i] not in crypt:
      word = word + str(s[i])
    else:
      word = word + str(crypt[s[i]])
    i = i + 1
  print(word)
  s = sys.stdin.readline().rstrip()

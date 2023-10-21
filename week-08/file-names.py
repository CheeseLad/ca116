#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()
i = 0
while i < len(a):
  a[i] = a[i].rstrip()
  token = a[i].split("/")
  print(str(token[len(token) - 1]).rstrip())
  i = i + 1

#i = 0
#while i < len(a):
#  string = str(a[i])
#  split = string.split("/n")
#  k = 0
#  print(split)
#  while k < len(split):
#    done = split[k].split("/")
#    print(done)
#    k = k + 1
#  i = i + 1

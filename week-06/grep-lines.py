#!/usr/bin/env python3

import sys

word = str(sys.argv[1])
a = []

n = input()
while n != "end":
  a.append(n)
  n = input()

#i = 0
#j = 0
#while j < len(a):
#  i = 0
#  while i < len(a) and a[j][i:len(word) - 1] != word:
#    k = 0
#    while k < len(a):
#      if a[j][i:len(word)] == word:
#        print(a[j])
#        j = j + 1
#      k = k + 1
#    i = i + 1
#  j = j + 1
i = 0
while i < len(a):
  j = 0
  while j < len(a[i]):
    if a[i][j:len(word) + j] == word:
      print(a[i])
      j = len(a[i])
    else:
      j = j + 1
  i = i + 1

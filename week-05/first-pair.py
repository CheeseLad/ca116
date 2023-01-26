#!/usr/bin/env python3

s = input()
i = 1
t = ""
p = ""
done = 0
while i < len(s) and done == 0:
  if s[i] == s[i - 1]:
    p = (s[i] + s[i - 1])
    done = 1
#  elif s[i + 1] == s[i]:
#    p = (s[i] + s[i + 1])
#    done = 1
  i = i + 1

if i < len(s) + 1 and p != "":
  print(p)

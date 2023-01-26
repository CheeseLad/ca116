#!/usr/bin/env python3

k = 0
s = input()
j = 0
i = 0
total = 0

while k < 5:
  while i < len(s) and s[i] != "+":
    i = i + 1
  total = total + int((s[j:i]))
  i = i + 1
  j = i
  k = k + 1
print(total)

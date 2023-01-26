#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and (s[i] < "0" or "9" < s[i]):
  i = i + 1

j = i
while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
  j = j + 1

k = j
while k < len(s) and (s[k] < "0" or "9" < s[k]):
  k = k + 1

o = k
while o < len(s) and ("0" <= s[o] and s[o] <= "9"):
  o = o + 1

if k < len(s):
  print(s[k:o], k)

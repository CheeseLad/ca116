#!/usr/bin/env python3

s = input()
i = 0
j = 0
num = ""
while i < len(s) and (s[i] < "0" or "9" < s[i]):
  i = i + 1
#  num = num + s[i]
if i < len(s):
  j = i
  while j < len(s) and "0" <= s[j] and s[j] <= "9":
    j = j + 1
  print(s[i:j], i)
#print(num, i)

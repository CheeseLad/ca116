#!/usr/bin/env python3

n = int(input())
i = 0
s = ""
string = "0123456789abcdef"
while n != 0:
  o = string[n % 16]
  s = o + s
  n = n // 16
  i = i + 1

j = 0
while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
  j = j + 1

if j < len(s):
  print(s[j])

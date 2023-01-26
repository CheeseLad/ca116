#!/usr/bin/env python3

s = input()
day = ""
month = ""
year = ""
date = ""
i = 0
j = 0

while ("a" <= s[i] and s[i] <= "z") or ("A" <= s[i] and s[i] <= "Z"):
  day = day + s[i]
  i = i + 1

i = i + 1

while ("a" <= s[i] and s[i] <= "z") or ("0" <= s[i] and s[i] <= "9"):
  date = date + s[i]
  i = i + 1

i = i + 1

while ("a" <= s[i] and s[i] <= "z") or ("A" <= s[i] and s[i] <= "Z"):
  month = month + s[i]
  i = i + 1

i = i + 2

while i < len(s) and ("0" <= s[i] and s[i] <= "9"):
  year = year + s[i]
  i = i + 1


print(month + " " + date + ", " + year + " " + "(" + day + ")")

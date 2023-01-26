#!/usr/bin/env python3

s = input()
i = 0
false = 0

value = ""
while i < len(s):
  if s[i] == (s[len(s) - i - 1]):
    value = "palindrome"
  elif (s[len(s) - i - 1]) == s[i]:
    value = "palindrome"
  else:
    false = 1
  i = i + 1

if value == "palindrome" and false == 0:
  print(value)

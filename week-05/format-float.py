#!/usr/bin/env python3

s = input()
i = 0
num = ""
after = "0"
while i < len(s):
  if s[i] == ".":
    num = s[:i]
    after = s[i + 1:]
  i = i + 1
i = i + 1
while i < len(s):
  after = after + s[i]
  i = i + 1

print(num + "." + after)

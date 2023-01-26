#!/usr/bin/env python3

newline = "\n"
with open("characters.txt") as f:
  input = f.readlines()

i = 0
while i < len(input):
  j = 0
  while j < len(input[i]):
    if input[i][j] == newline:
      print(newline.rstrip())
    else:
      print(input[i][j])
    j = j + 1

  i = i + 1

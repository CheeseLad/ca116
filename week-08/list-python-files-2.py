#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
  token = files[i].split(".")
  with open(files[i]) as f:
    if f.readlines() == []:
      j = 4
    elif token[len(token) - 1] == "py":
      print(files[i])
  i = i + 1

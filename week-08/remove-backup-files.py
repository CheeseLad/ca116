#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
  if os.path.isfile(files[i]):
    tokens = files[i].split(".")
    if tokens[len(tokens) - 1] == "bak" and len(tokens) > 1:
      os.unlink(files[i])
  i = i + 1

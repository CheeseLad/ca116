#!/usr/bin/env python3

import os
files = os.listdir(".")
i = 0
while i < len(files):
  token = files[i].split(".")
  if token[len(token) - 1] == "py":
    print(files[i])
  i = i + 1

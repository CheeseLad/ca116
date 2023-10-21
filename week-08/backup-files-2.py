#!/usr/bin/env python3

import os

files = os.listdir(".")
i = 0
while i < len(files):
  if os.path.isfile(files[i]):
    with open(files[i]) as f_in:
      lines = f_in.readlines()
    token = files[i].split(".")
    if token[len(token) - 1] != "bak":
      with open(files[i] + ".bak", "w") as f_out:
        f_out.writelines(lines)
  i = i + 1

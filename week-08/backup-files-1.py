#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
  token = files[i].split(".")
  if token[len(token) - 1] != "bak":
    with open(files[i]) as f_in:
      a = f_in.readlines()
    with open(files[i] + ".bak", "w") as f_out:
      f_out.writelines(a)
  i = i + 1

#!/usr/bin/env python3

i = 0
with open("irish-dobs.txt") as length:
  lines = length.readlines()

with open("american-dobs.txt", "w") as f:
  while i < len(lines):
    token = lines[i].split("/")
    dob = str(token[1]) + "/" + str(token[0]) + "/" + str(token[2])
    dob = dob.rstrip()
    f.writelines(dob + "\n")
    i = i + 1

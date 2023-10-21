#!/usr/bin/env python3

import sys

args = sys.argv[1]
data = []
args = args.split("=")
header = args[0]
value = args[1]

#print(header, value)

csvheader = input()
csvheader = csvheader.split(",")
i = 0
while i < len(csvheader) and value != csvheader[i]:
  i = i + 1

#print(i - 1)

csvdata = input()
while csvdata != "end":
  data.append(csvdata)
  csvdata = input()

#print(data)
j = 0
while j < len(data):
  csvdatas = data[j].split(",")
#  print(csvdatas)
  if csvdatas[1] == value:
    print(data[j])
  j = j + 1

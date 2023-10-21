#!/usr/bin/env python3

data = []

s = input()
while s != "end":
  data.append(s)
  s = input()
  if s == "end":
    day = int(input())

#print(data)
#print(day)

#print(data[0].split())
i = 0
while i < len(data):
  if int(data[i][0]) == day:
    print("".join(data[i]))
  i = i + 1

#!/usr/bin/env python3

odds = []

n = input()

if n != "end":
  if int(n) % 2 == 0:
    print(int(n))
  else:
    odds.append(int(n))

while n != "end":
  n = input()
  if n != "end":
    if int(n) % 2 == 0:
      print(int(n))
    else:
      odds.append(int(n))

i = 0
while i < len(odds):
  print(odds[i])
  i = i + 1

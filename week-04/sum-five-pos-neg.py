#!/usr/bin/env python3

i = 0
positive = 0
negative = 0

while i < 5:
  n = int(input())
  if n > 0:
    positive = positive + n
  else:
    negative = negative + n
  i = i + 1
print(negative, positive)

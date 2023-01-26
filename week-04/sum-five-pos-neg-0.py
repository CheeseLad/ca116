#!/usr/bin/env python3


positive = 0
negative = 0
n = int(input())
if n > 0:
  positive = positive + n
else:
  negative = negative + n
while n != 0:
  n = int(input())
  if n > 0:
    positive = positive + n
  else:
    negative = negative + n
print(negative, positive)

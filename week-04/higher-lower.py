#!/usr/bin/env python3


i = 0
prev = int(input())

while i < 5:
  curr = int(input())
  if curr > prev:
    print("higher")
  elif curr < prev:
    print("lower")
  elif curr == prev:
    print("equal")
  prev = curr
  i = i + 1

#!/usr/bin/env python3

prev = int(input())

while prev != 0:
  curr = int(input())
  if curr > prev and curr != 0:
    print("higher")
  elif curr < prev and curr != 0:
    print("lower")
  elif curr == prev and curr != 0:
    print("equal")
  prev = curr

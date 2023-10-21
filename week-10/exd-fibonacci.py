#!/usr/bin/env python3

prev = 0
curr = 1

n = int(input())

while curr < n:
  tmp = curr
  curr = prev + curr
  prev = tmp

if curr == n or curr == 1:
  print("yes")
else:
  print("no")

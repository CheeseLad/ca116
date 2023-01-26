#!/usr/bin/env python3

a = input()
b = input()

if a > b:
  if len(a) < len(b):
    print(b)
  else:
    print(a)

if b > a:
  if len(b) < len(a):
    print(a)
  else:
    print(b)

#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
if a[0] !"

while i < len(a) and a[i] == "":
  i = i + 1
  if a[i] != "" and i < len(a):
    print(a[i])
    i = len(a)

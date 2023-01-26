#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
  s = "mont"

i = 0
while i < len(a) and s != a[i][0:len(s) - 1]:
  if s == a[i][0:len(s)]:
    print(a[i])
    i = len(a)
  i = i + 1

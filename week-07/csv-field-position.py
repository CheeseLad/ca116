#!/usr/bin/env python3

import sys
field = sys.argv[1]

s = input()
position = 0
start = 0
end = 0

while end < len(s) and s[end] != ",":
  end = end + 1

while s[start:end] != field:
  position = position + 1

  start = end + 1
  end = start + 1
  while end < len(s) and s[end] != ",":
    end = end + 1

print(position)

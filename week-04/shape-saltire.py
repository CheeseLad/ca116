#!/usr/bin/env python3

i = 0
n = int(input())
s = n

while i < n:
  u = n // 2 - i
  if u < 0:
    u = -u
  if u == 0:
    print(n // 2 * " " + "*")
  else:
    print((n // 2 - u) * " " + "*" + (2 * u - 1) * " " + "*")
  i = i + 1


#while i < n // 3 + 1:
#  print(" " * i + "*" + " " * n + "*")
#  n = n - 2
#  i = i + 1

#print(" " * (s // 2) + "*")

#i = 0
#u = 1
#p = 1

#while i < s // 3 + 1:
#  print(" " * (s // 2 - u) + "*" + " " * p + "*")
#  i = i + 1
#  u = u + 1
#  p = p + 2###
#n = s
#i = 0

#while i < n:
#  print(" " * (n - i) + "*")
#  i = i + 1

#while i < 4:
#  print(" " * (i % 4) + "*")
#  i = i + 1

#i = 0
#o = 3
#while i < 4:
#  print(" " * ((o - 1) % 4) + "*")
#  i = i + 1

#n = 7
#p = n - 2

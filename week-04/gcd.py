#!/usr/bin/env python3

a = int(input())
b = int(input())

#while b != 0:
#  newa = b
#  newb = a % b
#  b = newa
#  a = b
#print(a)

i = 0
#while i < 3:
#  newa = a % b
#  a = newa
#  b = a
#  print(a)
#  i = i + 1


#819 % 490 = 329
#490 % 329 = 161
#329 % 161 = 7
#161 % 7 = 0

#a = newb
#a % b = b
#b = newb

#newa = oldb
#olda % oldb = newb
newa = a
while b != 0:
  newa = b
  b = a % b
  a = newa
  i = i + 1
print(b + a)

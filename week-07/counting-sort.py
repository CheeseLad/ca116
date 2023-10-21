#!/usr/bin/env python3

i = 0
a = []
n = input()
while n != "end":
  count = 0
  a.append([i, count])

  if int(n) <= i:
    a[int(n)][1] = a[int(n)][1] + 1
    n = input()
  i = i + 1

i = 0
#print(a)
#print(a[1])
#print(a[2][1])
#print(a[0][1], 4)
#print(a[4][1], 4)

while i < len(a):
  if a[i][1] != 0:
    print(i)
    a[i][1] = a[i][1] - 1
    i = i - 1
  i = i + 1

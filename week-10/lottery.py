#!/usr/bin/env python3

import sys
a = []
i = 0
while i < 20:
  a.append(i + 1)
  i = i + 1

print(a)
num1 = int(sys.argv[1])
num2 = int(sys.argv[1])
num3 = int(sys.argv[1])

s = sys.stdin.readline().rstrip()
s = s.split()
print(s)
nums = []
i = 0
while i < len(s):
  nums.append(s[i])
  i = i + 1

if num1 in int(nums[0]):
  print("1")

if num2 in int(nums[1]):
  print("2")

if num3 in nums:
  print("2")

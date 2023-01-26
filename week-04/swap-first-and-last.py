#!/usr/bin/env python3

s = str(input())
i = 0
reverse = ""

#while i < (len(s) - 1):
#  reverse = reverse + s[(i + 1):(len(s) - 1)]
#  reverse = reverse + s[len(s) - i - 1]
#  i = i + 1

#print(s[0] + s[1:len(s) - 1] + s[len(s) - 1])

print(s[len(s) - 1] + s[1:len(s) - 1] + s[0])

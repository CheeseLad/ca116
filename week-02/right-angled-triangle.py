#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

#print(a <= b + c or b <= a + c or c <= a + b)
d = (a ** 2 + b ** 2 == c ** 2)
e = (b ** 2 + c ** 2 == a ** 2)
f = (a ** 2 + c ** 2 == b ** 2)
print(d or e or f)

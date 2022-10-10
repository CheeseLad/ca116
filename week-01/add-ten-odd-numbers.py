#!/usr/bin/env python3

#total = 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

#print(total * (total % 2))
#print(total * % total * 2)
#print(total * (total % 2))
na = a * (a % 2) + b * (b % 2) + c * (c % 2) + d * (d % 2)
nb = e * (e % 2) + f * (f % 2) + g * (g % 2) + h * (h % 2)
nc = i * (i % 2) + j * (j % 2)
print(na + nb + nc)

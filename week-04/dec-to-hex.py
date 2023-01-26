#!/usr/bin/env python3

n = int(input())

power = 1
i = 0
hex = ""
truehex = ""
while n > power:
  truepower = power
  power = 16 ** i
  i = i + 1

truepower = truepower ** + 1
#19 // 16 = 1 rem 3
#n // truepower == 1
#n % 16 = 3
#3 // 1 = 3 rem 0
#print(truepower)

string = "0123456789abcdef"

i = 0
while n != 0:
  newhex = string[n % 16]
  truehex = newhex + truehex
  n = n // 16
  i = i + 1
print(truehex)
#power = n // (truepower // 16)
#print(n)
#hex = str(power) + hex
#print(n)
#print(hex)

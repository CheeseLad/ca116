#!/usr/bin/env python3



n = int(input())

digit = n % 10
case = n % 100

if case == 11 or case == 12 or case == 13:
    print(str(case) + "th")
elif digit == 1:
    print(str(digit) + "st")
elif digit == 2:
    print(str(digit) + "nd")
elif digit == 3:
    print(str(digit) + "rd")
else:
    print(str(digit) + "th")

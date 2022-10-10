#!/usr/bin/env python3

mark = int(input())

print("first:", mark >= 70)
print("second:", 69 >= mark and mark >= 50)
print("third:", 49 >= mark and mark >= 40)
print("fail:", mark < 40)

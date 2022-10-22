#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

<<<<<<< Updated upstream
print(c % 2 == 0)
print(c * (c % 2))
=======
t = c % 2 == 0
y = c % 2 > 0

print(int(t) * a or int(y) * b)
>>>>>>> Stashed changes

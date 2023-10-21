#!/usr/bin/env python3

#!/usr/bin/env python3

a = []

n = input()
while n != "end":
  a.append(n)
  n = input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
         print(a[j])
      j = j + 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

print(a[i - 1])

i = 0
while i < len(a) - 1:
  print(a[i])
  i = i + 1

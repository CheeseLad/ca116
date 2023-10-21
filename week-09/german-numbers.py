#!/usr/bin/env python3

import sys

english = "one two three four five six seven eight nine ten"
german = "eins zwei drei vier funf sechs sieben acht neun zehn"

english = english.split()
german = german.split()
translation = {}

i = 0
while i < len(english):
  translation[english[i]] = german[i]
  i = i + 1

#print(translation)

words = sys.stdin.readline().rstrip()
while len(words) != 0:
  if words in translation:
    print(translation[words])
  words = sys.stdin.readline().rstrip()

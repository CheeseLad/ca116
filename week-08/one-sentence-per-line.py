#!/usr/bin/env python3

lines = []

line = input()
while line != "end":
  lines.append(line)
  line = input()

token = " ".join(lines)
token = token.rstrip()
#print(token)

sentences = token.split(".")

#print(sentences)

i = 0
while i < len(sentences):
  sentences[i] = sentences[i].lstrip()
  i = i + 1

#print(sentences)


i = 0
while i < len(sentences) and len(sentences[i]) != 0:
  sentences[i] = sentences[i].split()
  print(str(" ".join(sentences[i])) + ".")
  i = i + 1

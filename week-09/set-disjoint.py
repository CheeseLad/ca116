#!/usr/bin/env python3

import sys

seta = []
setad = {}
setb = []
setbd = {}
line = []

items ={}

value = "disjoint"
with open("a.txt") as fa:
  line = fa.readlines()
  i = 0
  while i < len(line):
    line[i] = line[i].rstrip()
    if line[i] not in items:
      items[line[i]] = True
    i = i + 1

#print(items)
#i = 0
#while i < len(line):
#  line[i] = line[i].rstrip()
#  seta.append(line[i])
#  setad[line[i]] = 1
#  i = i + 1
with open("b.txt") as fb:
  line = fb.readlines()
  i = 0
  while i < len(line):
    line[i] = line[i].rstrip()
    if line[i] not in items:
      items[line[i]] = True
    i = i + 1

if len(items) > 0:
  print("intersecting")
else:
  print("disjoint")


#i = 0
#while i < len(line):
#  line[i] = line[i].rstrip()
#  setb.append(line[i])
#  setbd[line[i]] = 1
#  i = i + 1

#i = 0
#while i < len(seta) or i < len(setb):
#  if seta[i] == setb[i] and i < len(seta):
#    value = "intersecting"
#    i = len(seta)
#  i = i + 1

#if value == "intersecting":
#  print(value)
#else:
#  print("disjoint")

#print(setad, setbd)

#i = 0
#while i < len(setad):
#for animals in setad:
#  if setad[i] in setbd:
#    value = "intersecting"
#  i = i + 1

#print(value)

#!/usr/bin/env python3

import sys

files = sys.stdin.readlines()

files = " ".join(files)

files = files.split()
print("\n".join(files))

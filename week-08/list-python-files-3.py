#!/usr/bin/env python3

import os

files = os.listdir(".")
shebang = "#!/usr/bin/env python3\n"
i = 0
while i < len(files):
  token = files[i].split(".")
  if os.path.isfile(files[i]):
    with open(files[i]) as f:
      first = f.readline()
      end = token[len(token) - 1]
      if len(first) != 0 and (end == "py" or first == shebang):
        print(files[i])
  i = i + 1

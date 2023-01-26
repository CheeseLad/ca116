#!/usr/bin/env python3

import sys

filea = sys.argv[1]
fileb = sys.argv[2]

with open(filea) as fa:
  adata = fa.readlines()
  adata = "".join(adata)

with open(fileb) as fb:
  bdata = fb.readlines()
  bdata = "".join(bdata)

with open(filea, "w") as fa_write:
  fa_write.write(bdata)

with open(fileb, "w") as fb_write:
  fb_write.write(adata)

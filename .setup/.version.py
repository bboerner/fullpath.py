#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from __init__ import REPO, read

__all__ = ["version"]

path = os.path.join(REPO, "version.txt")
if os.path.exists(path) and os.path.isfile(path):
    version = read(path)
else:
    if __name__ == "__main__":
        print("%s NOT EXISTS" % path)
    if "VERSION" in os.environ:
        version = os.environ["VERSION"]

if __name__ == "__main__":
    for k in __all__:
        if k in globals():
            print("%s: %s" % (k, globals()[k]))

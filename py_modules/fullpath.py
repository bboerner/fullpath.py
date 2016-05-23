#!/usr/bin/env python
import os
from isstring import isstring
from public import public


@public
def fullpath(path):
    if not path:
        return None
    if not isstring(path):
        path = str(path)
    path = os.path.expanduser(path)
    if not os.path.isabs(path):
        path = os.path.abspath(path)
    return path


@public
def isfullpath(path):
    return path == fullpath(path)

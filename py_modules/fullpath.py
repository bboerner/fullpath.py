#!/usr/bin/env python
from os.path import *
from isstring import isstring
#from decorator import decorator
# me
#from argskwargs import *
#from definspect import *
from public import public

def _fullpath(path):
    if not path: return None
    if not isstring(path):
        path = str(path)
    path = expanduser(path)
    if not isabs(path):
        path = abspath(path)
    return path

@public
def fullpath(path):
    if not path: return None
    # todo: decorator
    return _fullpath(path)
    if isfunction(path):
        f = path
        def wrapper(f,*args, **kwargs):
            pos = 0
            if ismethod(f):
                pos = 1
            path = getarg(f,pos,args,kwargs)
            if path: 
                path = _fullpath(path)
                args,kwargs = setarg(f,pos,path,args,kwargs)
            return f(*args,**kwargs)
        return decorator(wrapper,f)
    return _fullpath(path)

@public
def isfullpath(path):
    return path==fullpath(path)

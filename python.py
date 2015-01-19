#!/usr/bin/env python
# -%- coding: utf-8 -%-

def f(a):
    pass

class A(B):
    # name error
    pass

# syntax error
1 = 'a'

# syntax error (pyflakes)
-=

# undefined variable
print(a)

# method could be a function
class A(object):

    def f(self):
        return True

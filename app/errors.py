#!/usr/bin/env python
# -%- coding: utf-8 -%-

# syntax error (cannot assign to None)
from sys import None
None = 1


def f():
    pass


# wrong signature
f(1)


# missing `:` (indentation error)
if True
    a = 1

# -*- coding: UTF-8 -*-

# import the SymPy library
from sympy import *

if __name__ == '__main__':
    # the comments below is another way to do the simplify job by compile
    # codeObj = compile("a = Symbol('a')", '', 'exec')
    # exec(codeObj)
    a = Symbol('a')

    expr = (((a * a) + (a / a)) - ((a - a) - a)) + \
           (((a * a) * a) * a) + \
           (((a / a) / a) - (a / a)) + \
           ((a * (a * a)) - ((a / a) / a))
    print(simplify(expr))
    print(factor(expr))
    print(expand(expr))

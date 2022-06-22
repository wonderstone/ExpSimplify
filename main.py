# -*- coding: UTF-8 -*-

# import the SymPy library
from sympy import *

if __name__ == '__main__':
    a = Symbol('a')
    expr = (((a * a) + (a / a)) - ((a - a) - a))+(((a * a) * a) * a)+(((a / a) / a) - (a / a))+((a * (a * a)) - ((a / a) / a))
    print(simplify(expr))
    print(factor(expr))
    print(expand(expr))

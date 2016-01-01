# Exercise 4.22: math_identities_failures_cml.py

import sys, random
from math import *
from scitools.StringFunction import StringFunction

def equal(expr1, expr2, A, B, n=500):
    failures = []
    for t in range(1, n + 1) :
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        f = StringFunction(expr1, independent_variables=('a','b'))
        s = StringFunction(expr2, independent_variables=('a','b'))
        
        first = f(a, b)
        second = s(a,b)
        
        if first != second:
            result = abs(first - second)
            failures.append(result)

    nFailures = float(len(failures))
    percentage = (nFailures/n)*100
    return n, nFailures, percentage


if __name__ == '__main__':
    print equal(expr1=sys.argv[1], expr2=sys.argv[2], A=eval(sys.argv[3]),
            B=eval(sys.argv[4]))



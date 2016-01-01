# Exercise 4.24: binomial_distribution.py
"""
Module for computing binomial distribution.

Symbols: x(integer) is the number of successful experinments,
n(integer) is the number of the prformed experinments
and p(float) is the probability of success'

In the command line must be provided with 3 numbers that represent x, n, p.
n should be greater than x (n>x) and p should be less than zero in decimal form.
"""


import sys
_filename = sys.argv[0]
_usage = """
Usage: %s x(integer) n(integer) p(float)
Program computes and prints the binomial distribution'
""" % _filename


from math import factorial

def binomial(x, n, p):
    B = ((factorial(n))*(p**x)*((1 - p)**(n-x)))/((factorial(x))*(factorial(n-x)))
    return B

def verify():
    x = eval(sys.argv[1])
    n = eval(sys.argv[2])
    p = eval(sys.argv[3])
    b = binomial(x, n, p)
    print ' For n = %d experinments and p = %f probability success,'\
          'the probability of getting success %d times is B = %f or %.2f%%!!' \
          % (n, p, x, b, b*100)



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print _usage
    else:
        verify()
    
    




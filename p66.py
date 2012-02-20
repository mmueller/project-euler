#!/usr/bin/env python
#coding: utf-8

"""
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2×2^2 = 1
2^2 - 3×1^2 = 1
9^2 - 5×4^2 = 1
5^2 - 6×2^2 = 1
8^2 - 7×3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""

# Rules:
# x+1 or x-1 is a multiple of D

from itertools import count
from math import sqrt
from p65 import compute_continued_fraction

def sqrt_seq(n):
    m, d, a = 0, 1, int(sqrt(n))
    a0 = a
    yield a
    while True:
        m = d * a - m
        d = (n - m**2) / d
        a = (a0 + m) / d
        yield a

def approximate_sqrt(n):
    for limit in count(1):
        yield compute_continued_fraction(sqrt_seq(n), limit)

def is_square(x):
    h = x & 0xF
    if h == 0 or h == 1 or h == 4 or h == 9:
        return int(sqrt(x))**2 == x
    return False

def find_minimal_x(d):
    # Turns out this is Pell's equation which approximates the sqrt of d
    # with the fraction x/y.  Using that knowledge, compute the continued
    # fraction convergents until a solution is found.
    for f in approximate_sqrt(d):
         x = f.numerator
         y = f.denominator
         if x**2 - d * y**2 == 1:
             return x
    # Too slow: Iterate over multiples of d
    #for m in count(d, d):
    #    for x in [m-1, m+1]:
    #        #y2 = (x**2 - 1)/d
    #        y2 = (x+1) * (x-1) / d
    #        if y2 <= 0: continue
    #        if is_square(y2):
    #            return x

if __name__ == '__main__':
    max_d = 1
    max_x = 0
    for d in range(1, 1001):
        if is_square(d):
            continue
        x = find_minimal_x(d)
        print d, x
        if x > max_x:
            max_x = x
            max_d = d
    print 'Found x = %d at D = %d.' % (max_x, max_d)

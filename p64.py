#!/usr/bin/env python

"""
Full problem here: http://projecteuler.net/problem=64

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
"""

from math import sqrt

def reverse_find_in_list(l, item):
    for i in range(len(l)-1, -1, -1):
        if item == l[i]:
            return i
    return -1

def find_continued_period(n, result=None):
    """
    Returns the length of the period of the continued fraction for sqrt(n).
    Recursive implementation of algorithm described here:
    http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    """
    if not result:
        m, d, a = 0, 1, int(sqrt(n))
        return find_continued_period(n, [(m, d, a)])
    else:
        a0 = result[0][2]
        prev_m, prev_d, prev_a = result[-1]
        m = prev_d * prev_a - prev_m
        d = (n - m**2) / prev_d
        a = (a0 + m) / d
        pos = reverse_find_in_list(result, (m, d, a))
        result.append((m, d, a))
        if pos >= 0:
            return len(result) - pos - 1
        else:
            return find_continued_period(n, result)

if __name__ == '__main__':
    nonsquares = [n for n in range(1, 10001) if int(sqrt(n))**2 != n]
    periods = [find_continued_period(n) for n in nonsquares]
    print 'Odd periods:', len(filter(lambda x: x % 2 == 1, periods))

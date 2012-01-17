#!/usr/bin/env python
# coding: utf-8

"""
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

    √2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""

from fractions import Fraction
from math import log10

def longer_numerator(f):
    return int(log10(f.numerator)) > int(log10(f.denominator))

def brute_force(limit):
    count = 0
    result = Fraction(1,2)
    for i in range(1, limit):
        n, d = (result.numerator, result.denominator)
        result = Fraction(d, n + 2*d)
        if longer_numerator(1 + result):
            count += 1
    return count

if __name__ == '__main__':
    print brute_force(1001)


#!/usr/bin/env python

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""

from digits import get_digits

if __name__ == '__main__':
    maxsum = 0
    for a in range(0, 100):
        for b in range(0, 100):
            s = sum(get_digits(a**b))
            if s > maxsum:
                maxsum = s
                maxa = a
                maxb = b
    print "%d^%d = %d" % (maxa, maxb, maxa**maxb)
    print "Sum: %d" % maxsum

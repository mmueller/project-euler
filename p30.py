#!/usr/bin/env python

"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

import sys

from digits import get_digits

def is_narcissistic(n, exp):
    value = 0
    digits = get_digits(n)
    for digit in digits:
        value += digit**exp
    return value == n

def find_narcissists(exp):
    results = []
    for n in range(10, 10**(exp+1)):
        if is_narcissistic(n, exp):
            print 'Works for', n
            results.append(n)
    print 'Sum:', sum(results)

if __name__ == '__main__':
    try:
        d = int(sys.argv[1])
    except:
        print 'Usage: %s <power>' % sys.argv[0]
        sys.exit(1)
    find_narcissists(int(sys.argv[1]))

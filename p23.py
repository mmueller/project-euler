#!/usr/bin/env python

"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number whose proper divisors are less than the number is called deficient
and a number whose proper divisors exceed the number is called abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

import sys

import p21

def abundant(n):
    "Returns true for abundant numbers n, false otherwise."
    return sum(p21.divisors(n)) > n

def sumOfAbundant(n, abundants):
    "Returns true iff n can be expressed as the sum of two abundant numbers."
    for value in abundants:
        if n-value in abundants:
            return True
    return False

def genAbundants():
    result = set()
    for i in xrange(12, 28123):
        if abundant(i):
            result.add(i)
    return result

def problem():
    abundants = genAbundants()
    nonSums = []
    for i in xrange(1, 28123):
        if not sumOfAbundant(i, abundants):
            nonSums.append(i)
    print sum(nonSums)

def main(argv):
    problem()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

#!/usr/bin/env python

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?
"""

from primes import factor

def find_consecutive_n_factor_integers(goal):
    n = 1
    in_a_row = 0
    while in_a_row < goal:
        factors = factor(n)
        if len(factors) == goal:
            in_a_row += 1
        else:
            in_a_row = 0
        n += 1
    return n - goal

if __name__ == '__main__':
    goal = 4
    n = find_consecutive_n_factor_integers(goal)
    print 'Number\tFactors'
    for offset in range(0, goal):
        print "%d\t%s" % (n+offset, str(factor(n+offset)))

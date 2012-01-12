#!/usr/bin/env python

"""
The 12th term, fib(12), is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import sys

from util import memoize

@memoize
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

def problem25():
    for i in xrange(1, 1000000000):
        val = fib(i)
        if len(str(val)) == 1000:
            print i
            break

def main(argv):
    problem25()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

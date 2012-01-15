#!/usr/bin/env python

from util import memoize

@memoize
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

def choose(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)

if __name__ == '__main__':
    count = 0
    for n in range(1, 101):
        for c in range(1, n+1):
            if choose(n, c) > 1000000:
                count += 1
    print count

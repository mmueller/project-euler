#!/usr/bin/env python

# Find the sum of the digits in the number 100!

import operator

def factorial(n):
    return reduce(operator.mul, xrange(1,n+1))

print sum(int(x) for x in str(factorial(100)))

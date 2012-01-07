#!/usr/bin/env python

# What is the value of the first triangle number to have over five hundred
# divisors?

import math

def triangleFactor(n):
    "Return the factors of the nth triangle number."
    result = set([1])
    m = n+1
    if n % 2 == 0:
        n /= 2
    else:
        m /= 2
    for x in factor(n):
        for y in factor(m):
            result.add(x*y)
    return result

factors = { }
def factor(n):
    "Return a list of all factors of a number."
    if n in factors:
        return factors[n]
    result = set([1, n])
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            result.add(i)
            result.add(n/i)
    factors[n] = result
    return result

def p12():
    n = 1
    count = 1
    while count <= 500:
        n += 1
        count = len(triangleFactor(n))
    print "The", str(n)+"th triangle (", n*(n+1)/2,
    print ") is the winner, with", count, "factors"

p12()

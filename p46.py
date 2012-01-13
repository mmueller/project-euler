#!/usr/bin/env python

"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

from math import sqrt
from primes import is_prime, prime_generator

def is_square(n):
    return int(sqrt(n))**2 == n

def odd_composites():
    "Generate the series of odd composite numbers."
    n = 9
    while True:
        if n % 2 == 1 and not is_prime(n):
            yield n
        n += 1

def p46_test(c):
    "Test if a prime and square that fit Goldbach's rule can be found."
    for p in prime_generator():
        diff = c - p
        if diff < 0:
            return False
        if is_square(diff / 2):
            return True

if __name__ == '__main__':
    done = False
    for c in odd_composites():
        if not p46_test(c):
            print 'Failed for composite:', c
            break

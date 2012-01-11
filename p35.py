#!/usr/bin/env python

"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

from digits import get_digits
from primes import sieve

def combine_digits(digits):
    "Combine a list of digits into the original number."
    if len(digits) == 0:
        return 0
    else:
        return 10*combine_digits(digits[0:-1]) + digits[-1]

def rotations(n):
    "Return the set of rotations of the given n. e.g. 37 outputs {37, 73}."
    digits = get_digits(n)
    result = set()
    for i in range(0, len(digits)):
        result.add(combine_digits(digits[i:] + digits[0:i]))
    return result

def find_circular_primes(limit):
    "Return a list of circular primes below the given limit."
    primes = set(sieve(limit))
    is_circular = lambda n: rotations(n).issubset(primes)
    return filter(is_circular, primes)

if __name__ == '__main__':
    primes = find_circular_primes(1000000)
    print 'Found %d circular primes: %s' % (
         len(primes),
         ', '.join(map(str, primes)),
    )

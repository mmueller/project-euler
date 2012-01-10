#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math import log10
from primes import is_prime, prime_generator

def isTruncatablePrime(n, direction):
    "Direction should be 1 (left-to-right) or -1 (right-to-left)."
    if direction == 1:
        # This removes too many digits for multiples of 10, but multiples
        # of 10 would fail the isPrime test above anyway.
        n %= 10**int(log10(n))
    else:
        n = n / 10
    # Truncated to zero, done
    if not n:
        return True
    # Test if truncated number is still prime
    if not is_prime(n):
        return False
    return isTruncatablePrime(n, direction)

def find_truncatable_primes(count):
    "Find the first count truncatable primes, assuming that many exist."
    result = []
    for n in prime_generator():
        if n < 10:
            continue
        if isTruncatablePrime(n, 1) and isTruncatablePrime(n, -1):
            result.append(n)
            if len(result) == count:
                break
    return result

if __name__ == '__main__':
    result = find_truncatable_primes(11)
    print 'Found %d results:' % len(result)
    for n in result:
        print ' ', n
    print 'Sum:', sum(result)

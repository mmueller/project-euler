#!/usr/bin/env python

"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from digits import is_pandigital
from primes import sieve

if __name__ == '__main__':
    # Note:
    #   8 digits: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36 (divisible by 3)
    #   9 digits: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9= 45 (divisible by 3)
    # So the highest possible pandigital prime is 7654321.
    print filter(is_pandigital, sieve(7654322))[-1]

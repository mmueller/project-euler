#!/usr/bin/env python

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from digits import get_digits
from primes import is_prime, sieve

def get_permutations(x):
    "Return a list of all permutations of digits of x (as integers)."
    digits = get_digits(x)
    if len(digits) == 1:
        return digits
    result = []
    for i in range(0, len(digits)):
        combine = lambda d, e: int("".join(map(str, d)) + "".join(map(str, e)))
        result += map(lambda x: x*10 + digits[i],
                get_permutations(combine(digits[:i], digits[i+1:])))
    return list(set(result)) # Hacky duplicate filter

if __name__ == '__main__':
    # Ugly
    limit = 10000
    primes = sieve(limit)
    for p in primes:
        choices = filter(is_prime, get_permutations(p))
        choices = filter(lambda x: x > p, choices)
        for x in sorted(choices):
            step = x - p
            seq = [p, x]
            while True:
                x += step
                if x in choices:
                    seq.append(x)
                else:
                    break
            if len(seq) > 2:
                print 'Found:', seq

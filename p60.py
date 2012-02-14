#!/usr/bin/env python

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from primes import naive_is_prime as is_prime, prime_generator
from util import memoize

SIZE = 5

@memoize
def remarkable_pair(c1, c2):
    x1 = int(str(c1) + str(c2))
    x2 = int(str(c2) + str(c1))
    return is_prime(x1) and is_prime(x2)

def generate_remarkable_set(size):
    sets = []
    for p in prime_generator():
        print p
        for j in range(0, len(sets)):
            good = True
            for q in sets[j]:
                if not remarkable_pair(p, q):
                    good = False
                    break
            if good:
                newset = sets[j] + [p]
                sets.append(newset)
                if len(newset) == size:
                    return newset
        sets.append([p])

if __name__ == '__main__':
    result = generate_remarkable_set(SIZE)
    print 'Found set:', result
    print 'Sum:', sum(result)

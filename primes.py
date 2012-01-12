#!/usr/bin/env python

"""
Prime generation and testing comes up frequently in these problems.  I wanted
a fast incremental prime generator.  This is the sieve of Eratosthenes with
some space-doubling magic to make it incremental.  It's reasonably fast for a
Python implementation, but not terribly space-efficient.
"""

from math import sqrt

primes = []        # Used for iteration and indexing
prime_set = set()  # Used for fast primality lookup
space = [False]*2  # Workspace for sieve
prev_limit = 2     # The limit last time sieve() ran

def sieve(limit):
    "Generate a sequence of primes less than limit."
    global primes, prime_set, space, prev_limit

    if limit < prev_limit:
        return primes
    elif limit < 2*prev_limit:
        limit = 2*prev_limit

    # Propagate previous prime multiples across new space
    space += [True] * (limit - prev_limit)
    for p in primes:
        start = p**2
        if start < prev_limit:
            offset = (prev_limit - start) / p
            start = start + offset*p
        for j in xrange(start, limit, p):
            space[j] = False

    # "Full" sieve of the new space
    for i in xrange(prev_limit, limit):
        if space[i]:
            primes.append(i)
            prime_set.add(i)
            for j in xrange(i**2, limit, i):
                space[j] = False
    prev_limit = limit
    return primes

def prime_generator():
    "Return an iterator that will generate all primes incrementally."
    limit = 32
    i = 0
    primes = sieve(limit)
    while True:
        while i == len(primes):
            limit *= 2
            primes = sieve(limit)
        yield primes[i]
        i += 1

def is_prime(n):
    "Using the prime sieve in this module, test a number for primality."
    global prime_set
    sieve(n+1)
    return n in prime_set

def naive_is_prime(n):
    "Naive prime test, does not generate a (potentially huge) sieve."
    for f in xrange(2, int(sqrt(n))+1):
        if n % f == 0:
            return False
    return True

# Test the sieve/generator by printing all primes under 5 million
if __name__ == '__main__':
    for p in prime_generator():
        if p > 5000000:
            break
        print p

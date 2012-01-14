#!/usr/bin/env python

"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from primes import sieve, is_prime

def find_prime_seq(limit):
    # Find the sequence of primes 2 + 3 + ... that just fits within the limit
    primes = sieve(limit)
    total = 0
    for i, p in enumerate(primes):
        total += p
        if total >= limit:
            total -= p
            end = i # primes[0:end] is the candidate sequence
            break
    # Now incrementally shorten the sequence until the total is prime.
    # This is the longest sequence possible below limit.
    for remove_terms in xrange(0, len(primes)):
        # ds = delta from start (0), de = delta from end
        for ds in xrange(0, remove_terms+1):
            de = remove_terms - ds
            tmp = total
            tmp -= sum(primes[0:ds])
            tmp -= sum(primes[end-de:end])
            if is_prime(tmp):
                return primes[ds:end-de]

if __name__ == '__main__':
    limit = 1000000
    seq = find_prime_seq(limit)
    print 'Value: ', sum(seq)
    print 'Length:', len(seq), 'terms'
    print '+'.join(map(str, seq))

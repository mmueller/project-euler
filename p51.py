#!/usr/bin/env python

"""
By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.
"""

from primes import sieve

def get_choices(values, c):
    "Return a list of c values chosen from the given values."
    if c == 1:
        for v in values:
            yield [v]
    elif c > 0:
        for i, v in enumerate(values):
            for choices in get_choices(values[i+1:], c-1):
                yield [v] + choices

def find_prime_group(target_size):
    length = 1
    while True:
        length += 1
        primes = map(str, sieve(10**length))
        n_length_primes = set(filter(lambda x: len(x) == length, primes))
        for count in range(1, length):
            for choices in get_choices(range(0, length), count):
                digits = "0123456789"
                if 0 in choices:
                    digits = "123456789"
                if length-1 in choices:
                    digits = "1379"
                for p in n_length_primes:
                    result = []
                    for d in digits:
                        candidate = ''
                        for i in range(0, length):
                            if i in choices:
                                candidate += d
                            else:
                                candidate += p[i]
                        if candidate in n_length_primes:
                            result.append(candidate)
                    if len(result) == target_size:
                        return result

if __name__ == '__main__':
    result = find_prime_group(8)
    print 'Found', len(result), result

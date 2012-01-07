#!/usr/bin/env python

import sys
from p07n import isPrime

def log(a, b, count):
    print "Coefficients %d and %d produced %d primes." % (a, b, count)

def consecutive_primes(a, b):
    n = 0
    while isPrime(n*n + a*n + b):
        n += 1
    return n

def find_coefficients(limit):
    max_count = 0
    result = (None, None)
    for a in range(-limit+1, limit):
        for b in range(-limit+1, limit):
            count = consecutive_primes(a, b)
            if count > max_count:
                log(a, b, count)
                max_count = count
                result = (a, b)
    return result

def main(argv):
    a, b = find_coefficients(1000)
    print 'Coefficients: a=%d b=%d' % (a, b)
    print 'Product:      %d' % (a*b)

if __name__ == '__main__':
    sys.exit(main(sys.argv))

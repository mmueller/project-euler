#!/usr/bin/env python

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def getPrimes(n):
    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes

# Assume the 10001st prime occurs below 1,000,000
primes = getPrimes(1000000)
print primes[10000]

#!/usr/bin/env python

# What is the largest prime factor of 317584931803?

value = 317584931803
prime = 2

while value != 1:
    if value % prime == 0:
        print prime
        value /= prime
    else:
        notPrime = True
        while notPrime:
            prime += 1
            notPrime = False
            for i in range(2, prime/2):
                if prime % i == 0:
                    notPrime = True
                    break





#!/usr/bin/env python

def sieve(n):
    """Return a list of primes less than n."""
    if n < 2:
        return []

    # Space is a list of tuples (bool, int) where the bool is true
    # if the int might still be prime, false if we know it's not.
    space = []
    for i in range(0,n):
        space.append((True, i))
    primes = []
    
    for i in range(2,n):
        if space[i][0] == True:
            primes.append(space[i][1])
            for j in range(i*i,n,i):
                if space[j][0] == True and space[j][1] % space[i][1] == 0:
                    space[j] = (False, space[j][1])

    return primes
    

# Assume the 10001st prime occurs below 100,000
primes = sieve(1000000)
print primes[10000]

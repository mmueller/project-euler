#!/usr/bin/env python

# Generator function:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Which starting number, under one million, produces the longest chain?

f = lambda(n): n/2 if n % 2 == 0 else 3*n+1

seqCache = { 1: 1 }
def seq(n):
    if n in seqCache:
        return seqCache[n]
    result = seq(f(n)) + 1
    seqCache[n] = result
    return result

maxCount = 1
for i in xrange(1,1000000):
    count = seq(i)
    if count > maxCount:
        maxCount = count
        print "New maximum", maxCount, "produced by", i

print maxCount


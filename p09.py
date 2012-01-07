#!/usr/bin/env python

# Find the Pythagorean triplet such that a+b+c = 1000.
# Ouptut the product abc.

for a in range(1, 999):
    for b in range(a, 999):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print "%d * %d * %d = %d" % (a, b, c, a*b*c)




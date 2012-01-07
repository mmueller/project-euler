#!/usr/bin/env python

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math
import sys

def divisors(n):
    result = [ 1 ]
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            j = n/i
            if j != i:
                result.append(n/i)
    return result

def d(n):
    return sum(divisors(n))

def findAmicableNumbers(n):
    result = []
    for i in xrange(1, n):
        x = d(i)
        if x < n and x != i and d(x) == i:
            result.append(i)
    return result

def main(argv):
    print sum(findAmicableNumbers(10000))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

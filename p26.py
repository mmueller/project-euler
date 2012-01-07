#!/usr/bin/env python

"""
A unit fraction contains 1 in the numerator.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""

import sys


def cycle(d):
    """
    Returns the cycle of repeating digits for 1/d as a string.

    For example:
        cycle(3) = "3"
        cycle(4) = "" (no cycle)
        cycle(7) = "142857"
    """
    result = ""
    num = 1
    posRemainderMap = {}

    for i in xrange(d):
        remainder = num % d
        if remainder == 0:
            return ""

        result += str(num/d)
        for k, v in posRemainderMap.iteritems():
            if v == remainder:
                return result[k+1:]
        posRemainderMap[i] = remainder
        num = remainder * 10

def problem26():
    maxD = 1
    maxCycle = ""
    maxLen = 0
    for d in xrange(2, 1000):
        newCycle = cycle(d)
        newLen = len(newCycle)
        if newLen > maxLen:
            maxD = d
            maxCycle = newCycle
            maxLen = newLen
    print "d: ", maxD
    print "len: ", maxLen
    print "cycle: ", maxCycle

def main(argv):
    problem26()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

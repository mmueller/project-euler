#!/usr/bin/env python

"""
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

Upper right corner of each spiral is a square: 1^2, 3^2, 5^2, ...
If you pretend all four are the same, you'd get 4 x size^2.

The other three corners are less than the square, so this answer is off by
12*n where n is the current iteration (size-1)/2, or 6*(size-1).

So the formula for each spiral iteration is 4 x size^2 - 6 x (size-1).
"""

import sys

def usage():
    print "Usage: %s <size>" % sys.argv[0]
    print "(Where size is an odd, positive integer.)"

def p28(size):
    return 1 if size == 1 else p28(size-2) + 4*size*size - 6*(size-1)

def main(argv):
    try:
        size = int(argv[1])
    except Exception:
        usage()
        return 1
    if size < 1 or size % 2 == 0:
        usage()
        return 1
    print p28(size)

if __name__ == '__main__':
    sys.exit(main(sys.argv))

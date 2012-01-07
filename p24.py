#!/usr/bin/env python

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
5, 6, 7, 8 and 9?
"""

import sys

# Brute force + generators = neat!  Uses 3k of memory, but takes a few seconds
# on a fast machine. :)

def genOrderings(text):
    if len(text) == 1:
        yield text
    result = []
    for i in xrange(len(text)):
        for ordering in genOrderings(text[0:i] + text[i+1:]):
            yield text[i] + ordering

def problem24():
    for i, ordering in enumerate(genOrderings("0123456789")):
        if i == 999999:
            print ordering
            break;

def main(argv):
    problem24()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

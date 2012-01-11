#!/usr/bin/env python

"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

from math import sqrt

def find_side_solutions(limit):
    solutions = {}
    for i in xrange(1, limit+1):
        solutions[i] = []
    for a in xrange(1, limit/2):
        a2 = a**2
        for b in range(a, limit-a):
            b2 = b**2
            target_c2 = a2 + b2
            c = int(sqrt(target_c2))
            if c < b: # c should be the hypotenuse, longer than a and b
                break
            p = a+b+c
            if p > limit:
                break
            if c**2 == target_c2:
                solutions[p].append((a, b, c))
    return solutions

def find_bountiful_perimeter(limit):
    solutions = find_side_solutions(limit)
    max_s = 0
    max_p = 0
    for p in xrange(1, limit+1):
        if len(solutions[p]) > max_s:
            max_s = len(solutions[p])
            max_p = p
            print 'New max solutions: %d (perimeter %d)' % (max_s, max_p)
    return max_p

if __name__ == '__main__':
    p = find_bountiful_perimeter(1000)
    print 'Most solutions:', p

#!/usr/bin/env python

"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

def find_side_solutions(p):
    solutions = []
    for a in xrange(1, p/2):
        a2 = a**2
        for b in range(a, p-a):
            c = p - a - b
            if c < b: # c should be the hypotenuse, longer than a and b
                break
            if c**2 == a2 + b**2:
                solutions.append((a, b, c))
    return solutions

def find_bountiful_perimeter(limit):
    max_s = 0
    max_p = 0
    for p in xrange(1, limit+1):
        solutions = find_side_solutions(p)
        if len(solutions) > max_s:
            max_s = len(solutions)
            max_p = p
            print 'New max solutions: %d (perimeter %d)' % (max_s, max_p)
    return max_p

if __name__ == '__main__':
    p = find_bountiful_perimeter(1000)
    print 'Most solutions:', p
    for solution in find_side_solutions(p):
        print ' ', solution

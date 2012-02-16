#!/usr/bin/env python

"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""

from itertools import count

TARGET = 5

def find_permutations():
    families = {}
    for n in count(1):
        cube = n**3
        key = str(sorted(str(cube)))
        if key in families:
            families[key].append(cube)
            if len(families[key]) == TARGET:
                return families[key]
        else:
            families[key] = [cube]
    return None

if __name__ == '__main__':
    result = find_permutations()
    print sorted(result)

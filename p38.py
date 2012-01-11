#!/usr/bin/env python

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9
and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from digits import get_digits, is_pandigital

def find_pandigitals():
    pandigitals = []
    for n in xrange(1, 10000):
        result = ''
        for f in xrange(1, 10):
            result += str(n*f)
            if len(result) > 9:
                break
            if is_pandigital(result):
                print n, '-->', result
                pandigitals.append(result)
    return pandigitals

if __name__ == '__main__':
    pandigitals = find_pandigitals()
    print 'Max:', max(pandigitals)


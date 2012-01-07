#!/usr/bin/env python

"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from math import log10

def is_pandigital(value):
    if len(value) != 9: return False
    return ''.join(sorted(value)) == '123456789'

def find_pandigital_products():
    result = set()
    # a and b must be less than 5 digits, otherwise the total digits would
    # exceed 9.  (e.g. 1 x 10000 = 10000 is 11 digits.)
    for a in range(1, 9999):
        for b in range(a, 9999):
            x = a*b
            string = str(a) + str(b) + str(x)
            # Short circuit if results get too long
            if len(string) > 9:
                break
            if is_pandigital(string):
                print a, 'x', b, '=', x
                result.add(x)
    return result

if __name__ == '__main__':
    products = find_pandigital_products()
    print 'Sum of pandigital products:', sum(products)

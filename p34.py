#!/usr/bin/env python

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from digits import get_digits
from math import factorial

def find_curious_numbers():
    # Numbers obeying this rule cannot be larger than 7 digits, because
    # 9! * 8 is 2903040, a 7-digit number.  (An 8 digit number can never
    # produce itself in this way.)
    limit = factorial(9) * 7 + 1
    is_curious = lambda n: sum(map(factorial, get_digits(n))) == n
    return filter(is_curious, range(10, limit))

if __name__ == '__main__':
    numbers = find_curious_numbers()
    print 'Curious numbers:'
    for n in numbers:
        print ' ', n
    print 'Sum:', sum(numbers)

#!/usr/bin/env python

"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

from digits import get_digits

def same_digits(numbers):
    expect = sorted(get_digits(numbers[0]))
    for i in range(1, len(numbers)):
        if sorted(get_digits(numbers[i])) != expect:
            return False
    return True

def find_p52_number():
    i = 1
    while not same_digits([i, 2*i, 3*i, 4*i, 5*i, 6*i]):
        i += 1
    return i

if __name__ == '__main__':
    print find_p52_number()

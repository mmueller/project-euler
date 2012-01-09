#!/usr/bin/env python

"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

def is_b2_b10_palindrome(n):
    is_palindrome = lambda s: not s.endswith('0') and s == s[::-1]
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])

if __name__ == '__main__':
    result = filter(is_b2_b10_palindrome, range(1, 1000000))
    print 'Found %d results: %s' % (
        len(result),
        ' '.join(map(str, result)),
    )
    print 'Sum:', sum(result)

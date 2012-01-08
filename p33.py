#!/usr/bin/env python

from fractions import Fraction

def get_digits(n):
    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n /= 10
    return digits

def is_stupid(n, d):
    ndigits = get_digits(n)
    ddigits = get_digits(d)
    if ndigits[1] == ddigits[0]:
        if ddigits[1] != 0:
            if Fraction(ndigits[0], ddigits[1]) == Fraction(n, d):
                return True
    return False

def find_stupid_fractions():
    result = []
    for n in range(10, 99):
        for d in range(n+1, 100):
            if is_stupid(n, d):
                result.append(Fraction(n, d))
    return result

if __name__ == '__main__':
    fractions = find_stupid_fractions()
    print "Found fractions:", " ".join(map(str, fractions))
    print "Product:", reduce(lambda x, y: x*y, fractions)

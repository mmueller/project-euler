#!/usr/bin/env python

"""
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""

from digits import get_digits
from fractions import Fraction
from itertools import count

def compute_continued_fraction(seq, limit):
    "Expand the given continued fration sequence to the nth convergent."
    a = seq.next()
    if limit == 1:
        result = Fraction(a)
    else:
        result = a + Fraction(1, compute_continued_fraction(seq, limit-1))
    return result

def e_seq():
    "The sequence of values given in the problem to compute e."
    yield 2
    for n in count(2):
        if n % 3 == 0:
            yield n/3 * 2
        else:
            yield 1

if __name__ == '__main__':
    result = compute_continued_fraction(e_seq(), 100)
    print '100th convergent:', result
    print 'Numerator digit sum:', sum(get_digits(result.numerator))

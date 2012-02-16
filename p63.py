#!/usr/bin/env python

"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from itertools import count

if __name__ == '__main__':
    total = 0
    for exp in count(1):
        prev_total = total
        for n in range(1, 10):
            val = n**exp
            if len(str(val)) == exp:
                total += 1
            elif len(str(val)) > exp:
                break
        if total == prev_total:
            print 'Stopped finding new results at exp', exp
            break
    print 'Total:', total

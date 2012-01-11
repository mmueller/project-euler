#!/usr/bin/env python

from operator import mul

def build_string(length):
    i = 1
    s = '.'
    while len(s) <= length:
        s += str(i)
        i += 1
    return s

if __name__ == '__main__':
    s = build_string(1000000)
    digits = [
        s[1],
        s[10],
        s[100],
        s[1000],
        s[10000],
        s[100000],
        s[1000000],
    ]
    print "%s = %d" % (
        " x ".join(digits),
        reduce(mul, map(int, digits)),
    )

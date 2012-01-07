#!/usr/bin/env python

# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.

print str(sum(map(int, file("p13_input.txt", "r"))))[0:10]

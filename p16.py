#!/usr/bin/env python

# What is the sum of the digits of the number 2^1000?

print sum(int(x) for x in str(2**1000))

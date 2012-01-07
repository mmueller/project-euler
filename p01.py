#!/usr/bin/env python

# Sum of all multiples of 3 and 5 below 1000

# The naive approach
def naiveSum(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print naiveSum(1000)

# A more idiomatic approach
def multiple(i):
    return i % 3 == 0 or i % 5 == 0

def pySum(n):
    return sum(filter(multiple, range(1, n)))

print pySum(100)

# A clever approach


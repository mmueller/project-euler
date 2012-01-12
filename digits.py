#!/usr/bin/env python

"""
Utilities involving digit extraction and combination in integers.
"""

def get_digits(n):
    "Extract the decimal digits and return in a list (highest place first)."
    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n /= 10
    return digits

def is_pandigital(x, n=None):
    "Check if number is pandigital, i.e. contains each digit 1-n exactly once."
    s = str(x)
    if n:
        if len(s) != n:
            return False
    else:
        n = len(s)
    return ''.join(sorted(s)) == '123456789'[0:n]

def generate_pandigitals(length, values=None):
    """
    Fast recursive length-digit pandigital generator, results in ascending
    order.
    """
    if not values:
        values = range(1, length+1)
    if length == 1:
        yield values[0]
    else:
        for i, value in enumerate(values):
            subvalues = values[:i] + values[i+1:]
            subresults = generate_pandigitals(length-1, subvalues)
            contribution = value * (10 ** (length-1))
            for subresult in subresults:
                yield contribution + subresult

if __name__ == '__main__':
    # Silly: Mutually test is_pandigital and generate_pandigitals
    result = 'OK'
    for p in generate_pandigitals(5):
        if not is_pandigital(p):
            print 'is_pandigital(%d) should be true.' % p
            result = 'FAIL'
            break
        p = p + 1
        if is_pandigital(p):
            print 'is_pandigital(%d) should not be true.' % p
            result = 'FAIL'
    print 'Pandigitals:', result

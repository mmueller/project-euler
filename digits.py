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


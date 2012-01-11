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

def is_pandigital(n):
    "Check if number is pandigital, i.e. contains each digit 1-9 exactly once."
    s = str(n)
    return len(s) == 9 and ''.join(sorted(s)) == '123456789'



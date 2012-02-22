#!/usr/bin/env python

"""
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2;
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using inputs/p42.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

from math import sqrt

def parse_words(filename):
    "Extract comma-separated, quoted words from file."
    words = file(filename, 'r').read().split(',')
    return map(lambda s: s[1:-1], words)

def is_triangle_number(n):
    "Check if a number obeys the rules that define a triangle."
    x = int(sqrt(n*2))
    return x * (x+1) == n*2

def is_triangle_word(word):
    "Check if the letters of a word add up to a triangle number."
    letter_value = lambda c: ord(c) - ord('A') + 1
    word_value = sum(map(letter_value, word))
    return is_triangle_number(word_value)

if __name__ == '__main__':
    words = parse_words('inputs/p42.txt')
    triangle_words = filter(is_triangle_word, words)
    for word in triangle_words:
        print word
    print 'Found %d triangle words.' % len(triangle_words)


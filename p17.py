#!/usr/bin/env python

# How many letters in the words "one" to "one thousand".
# (not counting spaces)

# Note they say "and" after "hundred" which is "gay"

def numToText(n):
    if n >= 1000:
        return numToText(n/1000) + "thousand" + numToText(n%1000)
    elif n >= 100:
        result = numToText(n/100) + "hundred"
        if n % 100 != 0:
            result += "and" + numToText(n%100)
        return result
    elif n >= 80 and n < 90:
        return "eighty" + numToText(n%10)
    elif n >= 60:
        return numToText(n/10) + "ty" + numToText(n%10)
    elif n >= 50:
        return "fifty" + numToText(n%10)
    elif n >= 40:
        return "forty" + numToText(n%10)
    elif n >= 30:
        return "thirty" + numToText(n%10)
    elif n >= 20:
        return "twenty" + numToText(n%10)
    elif n == 18:
        return "eighteen"
    elif n == 15:
        return "fifteen"
    elif n > 13:
        return numToText(n%10) + "teen"
    elif n == 13:
        return "thirteen"
    elif n == 12:
        return "twelve"
    elif n == 11:
        return "eleven"
    elif n == 10:
        return "ten"
    elif n == 9:
        return "nine"
    elif n == 9:
        return "nine"
    elif n == 8:
        return "eight"
    elif n == 7:
        return "seven"
    elif n == 6:
        return "six"
    elif n == 5:
        return "five"
    elif n == 4:
        return "four"
    elif n == 3:
        return "three"
    elif n == 2:
        return "two"
    elif n == 1:
        return "one"
    return ""

total = 0
for i in xrange(1,1001):
    text = numToText(i)
    print i, "\t", len(text), "\t", text
    total += len(text)

print total

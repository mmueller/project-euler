#!/usr/bin/env python

# What is the largest palindrome made from the product of two 3-digit numbers?

def isPalindrome(s):
    return len(s) < 2 or s[0] == s[len(s)-1] and isPalindrome(s[1:len(s)-1])

max = 0
for x in range(100, 1000):
    for y in range(100, x+1):
        if isPalindrome(str(x*y)):
            if max < x*y:
                max = x*y
print "Largest palindrome: " + str(max)




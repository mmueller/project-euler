#!/usr/bin/env python

"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher
text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42
= 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text.
"""

import re

# Top 20 common english words (lowercased)
COMMON_ENGLISH_WORDS = [
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it',
    'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
]

def key_generator():
    "Yield lowercase alphabet keys of length 3."
    keychars = 'abcdefghijklmnopqrstuvwxyz'
    for a in keychars:
        for b in keychars:
            for c in keychars:
                yield a+b+c

def decrypt_message(cipher, key):
    message = ""
    keyidx = 0
    for value in cipher:
        message += chr(value ^ ord(key[keyidx]))
        keyidx += 1
        keyidx %= len(key)
    return message

def score_message(message):
    words = re.findall(r'\w+', message)
    count = 0
    for word in words:
        if word in COMMON_ENGLISH_WORDS:
            count += 1
    return count

if __name__ == '__main__':
    cipher = map(int, file('p59_input.txt', 'r').readline().split(','))
    best_key = 'aaa'
    best_score = 0
    for key in key_generator():
        # Score based on the first 128 chars of the message
        message = decrypt_message(cipher[:128], key)
        score = score_message(message)
        if score > best_score:
            best_key = key
            best_score = score
    message = decrypt_message(cipher, best_key)
    print 'Key:', best_key
    print 'Message:', message
    print 'Sum:', sum(map(ord, message))

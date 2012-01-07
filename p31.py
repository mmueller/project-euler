#!/usr/bin/env python

COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def find_combinations(total, coins):
    "Find combinations of coins that amount to the total in pence."
    if not coins: return 0
    combinations = 0
    i = 0
    while True:
        value = total - i*coins[0]
        if value <= 0:
            if value == 0:
                combinations += 1
            break
        combinations += find_combinations(value, coins[1:])
        i += 1
    return combinations

if __name__ == '__main__':
    print 'Combinations:', find_combinations(200, COINS)

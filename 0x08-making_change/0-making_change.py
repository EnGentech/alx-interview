#!/usr/bin/python3
"""Creating solution to making changes challenge"""


def makeChange(coins, total):
    """A function to determine the best possible changes"""
    if total <= 0:
        return 0

    current_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - current_total) // coin
        current_total += r * coin
        used_coins += r
        if current_total == total:
            return used_coins

    return -1

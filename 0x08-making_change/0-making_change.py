#!/usr/bin/python3
""" 0x08. Making Change"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total."""

    count = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            count += total // coin
            total = total % coin

    return count if total == 0 else -1

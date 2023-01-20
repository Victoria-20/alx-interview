#!/usr/bin/python3
"""0. Minimum Operations"""


def minOperations(n: int) -> int:
    """ method that calculates the fewest number of operations needed
        to result in exactly n H characters in the file.
    """
    operations = 0
    i = 2
    while i <= n + 1:
        if n % i == 0:
            operations += i
            n = n / i
            i = 2
        else:
            i += 1

    return operations

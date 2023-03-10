#!/usr/bin/python3
""" Write a method that determines if a given data set
represents a valid UTF-8 encoding."""


def validUTF8(data):
    """Returns True if data is a valid UTF-8 encoding, else return False"""
    def check(num):
        mask = 1 << (8 - 1)
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i
    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            c = check(data[i])
            if c != 1:
                return False
            i += 1
    return True

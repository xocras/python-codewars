# Persistent Bugger

# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

from math import prod


def persistence(n):
    return 0 if n < 10 else persistence(prod(int(x) for x in str(n))) + 1

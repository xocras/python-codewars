# Beginner - Reduce but Grow

# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

from functools import reduce
from operator import mul


def grow(arr):
    return reduce(mul, arr)


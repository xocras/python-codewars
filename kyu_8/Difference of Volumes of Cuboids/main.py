# Difference of Volumes of Cuboids

# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python

from numpy import prod

def find_difference(a, b):
    return abs(prod(a) - prod(b))


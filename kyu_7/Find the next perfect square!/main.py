# Find the next perfect square!

# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

import math

def find_next_square(sq):
    return -1 if not math.sqrt(sq).is_integer() else (math.sqrt(sq) + 1) ** 2


